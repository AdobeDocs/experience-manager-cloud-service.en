---
title: "Tutorial: Scan file attachments with ClamAV"
description: A complete, step-by-step tutorial for scanning Adaptive Form file uploads with the ClamAV antivirus engine. Written to be followed by someone new to AEM, including all assumptions, prerequisites, and values to substitute.
keywords: ClamAV AEM Forms, virus scan file upload, antivirus scan form attachment, malware scanning tutorial, block malicious file upload
feature: Adaptive Forms, Core Components
role: Developer
hide: true
---

# Tutorial: Scan file attachments with ClamAV

[!BADGE AEM Forms]{type=Positive tooltip="Applies to AEM Forms"}

<span class="preview"> The File Attachment Virus Scanner / Validator capability is under the Early Adopter Program. You can write to aem-forms-ea@adobe.com from your official email id to join the early adopter program and request access to the capability. </span>

This tutorial takes you end to end. You will run the ClamAV antivirus engine, add a custom validator to AEM, create a sample Adaptive Form with a file-upload field, connect the validator, and confirm that infected files are rejected at submission. It is written to be followed even if you are new to AEM. Every command, screen path, and value you need is spelled out.

For the concepts behind the validator and the interface reference, see the companion article [Scan file attachments in Adaptive Forms with a custom validator](/help/forms/scan-file-attachments-custom-validator.md). You do not need to read it first to complete this tutorial, but it explains why each piece exists.

## What you will build {#what-you-will-build}

By the end you will have:

* A running ClamAV daemon (`clamd`) that scans files on request.
* A custom AEM service (the ClamAV Scanner) that sends each uploaded file to `clamd` and rejects infected ones.
* A sample Adaptive Form named **File Attachment Scanner Demo** with a file-upload field and a submit button.
* A working test: an ordinary file submits successfully, and a known test-virus file is blocked.

## Before you begin: assumptions and prerequisites {#assumptions}

This tutorial assumes the setup below. If any item is missing, install or obtain it before starting. Each item includes how to check it.

| # | Assumption | How to verify | Notes |
|---|---|---|---|
| 1 | A local AEM author instance is running and reachable at `http://localhost:4502` | Open `http://localhost:4502` in a browser. You should see the AEM sign-in or Start screen. | This tutorial uses the local AEM as a Cloud Service SDK quickstart. |
| 2 | You can sign in to AEM as an administrator | Sign in at `http://localhost:4502` with an admin account (default local credentials are `admin` / `admin`) | Admin rights are needed to deploy code, change OSGi configuration, and author forms. |
| 3 | Your AEM environment is entitled to the Early Access file-attachment validator feature, with feature toggle `FT_FORMS-23497` enabled | Confirm with your Early Adopter Program contact | This toggle gates the underlying `FileAttachmentValidatorManager` capability. The Submission tab field itself is something this tutorial adds in Step 7 — it does not exist out of the box either way. |
| 4 | You have, or can create, an Adaptive Form Container **proxy component** in your project's `ui.apps` module | See Step 7 | This is the standard pattern for extending an AEM Core Component. Step 7 creates the dialog extension on it. |
| 5 | Java JDK is installed and matches your AEM SDK's required version | Run `java -version` in a terminal | Use the Java version required by your AEM SDK (for current SDKs this is Java 11 or Java 21). |
| 6 | Apache Maven 3.x is installed | Run `mvn -version` | Used to build and deploy the custom code. |
| 7 | Docker is installed (recommended path for running ClamAV) | Run `docker --version` | If you cannot use Docker, see the native-install note in Step 1. |
| 8 | You have, or can create, an AEM Maven project to hold custom code | See Step 2 | Step 2 creates one if you do not have it. |
| 9 | You have downloaded the **latest available build** of the AEM Forms add-on SDK, which bundles the Early Access dependency that provides the `com.adobe.forms.common.service` interfaces | Download `aem-forms-addon-sdk-<version>.zip` from the [Adobe Software Distribution portal](https://experience.adobe.com/#/downloads) (requires Early Adopter Program entitlement) | **Required.** This dependency is not published to a public Maven repository — it's extracted from the SDK download. Earlier builds may not include it. See Step 3. |

### Values you will substitute {#substitute-values}

Wherever you see these placeholders, replace them with your own values:

* `<PROJECT_ROOT>`: the folder of your AEM Maven project.
* `<APP_ID>`: your project's application id or bundle module name (for example, `mysite`).
* `<SDK_DEPENDENCY_VERSION>`: the `adobe-xfaforms-common` version bundled in the SDK you downloaded (the group id and artifact id are fixed — see Step 3).

>[!NOTE]
>
>All terminal commands are shown for macOS and Linux. On Windows, run them in PowerShell or WSL. The Docker and Maven commands are the same.

## Roadmap {#roadmap}

You complete these steps in order:

1. Start a ClamAV daemon (`clamd`).
1. Set up an AEM Maven project (skip if you already have one).
1. Add the Early Access dependency.
1. Add the ClamAV validator class.
1. Build and deploy to AEM.
1. Configure the `clamd` connection in AEM.
1. Add the validator field to the form dialog.
1. Create the sample Adaptive Form.
1. Connect the ClamAV Scanner to the form.
1. Test with a clean file and a test-virus file.

## Step 1: Start a ClamAV daemon {#step-1-clamd}

ClamAV runs as a background service called `clamd`. The validator you build streams each uploaded file to `clamd`, which replies `OK` for a clean file or reports the threat name when it detects one.

The quickest way to get `clamd` running is Docker.

1. Start ClamAV:

   ```
   docker run -d --name clamav -p 3310:3310 clamav/clamav:latest
   ```

   >[!NOTE]
   >
   >On Apple Silicon (arm64) Macs, this image has no native arm64 build and the command above fails with `no matching manifest for linux/arm64/v8`. Add `--platform linux/amd64` to run it under emulation instead:
   >
   >```
   >docker run -d --name clamav --platform linux/amd64 -p 3310:3310 clamav/clamav:latest
   >```

1. Wait for it to become ready. On first start it downloads the virus database, which can take a few minutes. Watch the logs until the database has loaded and `clamd` is listening:

   ```
   docker logs -f clamav
   ```

   Press `Ctrl+C` to stop following the logs once it is ready.

1. Verify `clamd` is reachable on port `3310`:

   ```
   printf 'PING\n' | nc localhost 3310
   ```

   **Expected result:** the response is `PONG`.

>[!NOTE]
>
>If you cannot use Docker, install ClamAV natively from [clamav.net](https://www.clamav.net), enable the `clamd` daemon and TCP socket on port `3310` in `clamd.conf`, update the database with `freshclam`, and start `clamd`. Then run the verification in step 3 above.

>[!IMPORTANT]
>
>`clamd` runs as its own process, separate from AEM. This local setup is for development. On AEM as a Cloud Service you cannot run `clamd` on the AEM host, so in real environments you run it as a co-located or external service and point the validator at it. Prefer a co-located instance in the same region to keep file content within your environment for data-residency and compliance.

## Step 2: Set up an AEM Maven project {#step-2-project}

Custom Java code is deployed to AEM as a bundle built by a Maven project. If you already have an AEM project, skip to Step 3 and use its bundle module (often named `core`).

If you do not have one, create a project with the AEM Project Archetype:

1. In a terminal, go to the folder where you keep code and run the archetype. Replace `<APP_ID>` with a short lowercase name such as `mysite`:

   ```
   mvn -B org.apache.maven.plugins:maven-archetype-plugin:generate -D archetypeGroupId=com.adobe.aem -D archetypeArtifactId=aem-project-archetype -D archetypeVersion=LATEST -D appId=<APP_ID> -D appTitle="<APP_ID>" -D name="<APP_ID>" -D groupId=com.example -D artifactId=<APP_ID> -D aemVersion=cloud
   ```

   **Expected result:** a new folder `<APP_ID>` (this is your `<PROJECT_ROOT>`) containing modules including `core`, `ui.apps`, and `all`.

1. The Java code you add later goes in the `core` module, under:

   ```
   <PROJECT_ROOT>/core/src/main/java/
   ```

>[!NOTE]
>
>Use the current archetype version. See the [AEM Project Archetype documentation](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/developing/archetype/overview). The archetype generates many files, but for this tutorial you only edit the `core` module.

## Step 3: Add the Early Access dependency {#step-3-dependency}

Your code compiles against the `FileAttachmentValidator` interface, which comes from `com.adobe.forms.foundation:adobe-xfaforms-common` (assumption #9). This dependency isn't published to a public Maven repository — it ships bundled inside the AEM Forms add-on SDK, so you extract it from there and install it into your local Maven repository.

1. Download the **latest available build** of `aem-forms-addon-sdk-<version>.zip` from the [Adobe Software Distribution portal](https://experience.adobe.com/#/downloads) (requires Early Adopter Program entitlement). Always use the latest build — earlier builds may not include this dependency yet.

1. Extract the dependency jar. The SDK zip contains a feature archive (`.far`), and the jar is bundled inside that:

   ```
   unzip -p aem-forms-addon-sdk-<version>.zip aem-forms-addon-<version>.far > addon.far
   unzip -l addon.far | grep adobe-xfaforms-common
   ```

   The second command shows you the exact jar path and version bundled in your download, for example `com/adobe/forms/foundation/adobe-xfaforms-common/<version>/adobe-xfaforms-common-<version>.jar`. Use that path and version in the next step.

   ```
   unzip -p addon.far "com/adobe/forms/foundation/adobe-xfaforms-common/<version>/adobe-xfaforms-common-<version>.jar" > adobe-xfaforms-common.jar
   ```

1. Install the extracted jar into your local Maven repository so `pom.xml` can resolve it. Include `-DgeneratePom=true` — the jar embeds its own internal Adobe build POM with a parent reference your project can't resolve, and this flag replaces it with a clean, self-contained one:

   ```
   mvn install:install-file -Dfile=adobe-xfaforms-common.jar -DgroupId=com.adobe.forms.foundation -DartifactId=adobe-xfaforms-common -Dversion=<version> -Dpackaging=jar -DgeneratePom=true
   ```

1. Open `<PROJECT_ROOT>/core/pom.xml`.

1. Inside the `<dependencies>` section, add the dependency using the same version you just installed. Use `provided` scope, because the interface is supplied by AEM at runtime:

   ```xml
   <dependency>
       <groupId>com.adobe.forms.foundation</groupId>
       <artifactId>adobe-xfaforms-common</artifactId>
       <version><SDK_DEPENDENCY_VERSION></version>
       <scope>provided</scope>
   </dependency>
   ```

1. Save the file.

>[!IMPORTANT]
>
>If you don't have Software Distribution portal access yet, request Early Adopter Program entitlement from your Adobe contact. Without this dependency the project does not compile.

## Step 4: Add the ClamAV validator class {#step-4-class}

1. Create a new file at:

   ```
   <PROJECT_ROOT>/core/src/main/java/com/example/forms/security/ClamAVFileAttachmentValidator.java
   ```

   Create the `forms/security` folders if they do not exist. You may use your own package name. If you do, change the `package` line to match.

1. Paste the following code:

   ```java
   package com.example.forms.security;

   import com.adobe.forms.common.service.FileAttachmentValidator;
   import com.adobe.forms.common.service.FileAttachmentValidationResult;
   import com.adobe.forms.common.service.FileAttachmentWrapper;
   import org.osgi.service.component.annotations.Activate;
   import org.osgi.service.component.annotations.Component;
   import org.osgi.service.metatype.annotations.AttributeDefinition;
   import org.osgi.service.metatype.annotations.Designate;
   import org.osgi.service.metatype.annotations.ObjectClassDefinition;

   import java.io.ByteArrayOutputStream;
   import java.io.DataOutputStream;
   import java.io.InputStream;
   import java.io.OutputStream;
   import java.net.InetSocketAddress;
   import java.net.Socket;
   import java.nio.charset.StandardCharsets;

   @Component(service = FileAttachmentValidator.class)
   @Designate(ocd = ClamAVFileAttachmentValidator.Config.class)
   public class ClamAVFileAttachmentValidator implements FileAttachmentValidator {

       @ObjectClassDefinition(name = "ClamAV File Attachment Scanner")
       public @interface Config {
           @AttributeDefinition(name = "clamd Host")
           String clamd_host() default "localhost";

           @AttributeDefinition(name = "clamd Port")
           int clamd_port() default 3310;

           @AttributeDefinition(name = "Scan Timeout (ms)")
           int clamd_timeout() default 30000;
       }

       private static final String VALIDATOR_NAME = "ClamAV Scanner";
       private static final int CHUNK_SIZE = 8192;

       private String host;
       private int port;
       private int timeout;

       @Activate
       protected void activate(Config config) {
           this.host = config.clamd_host();
           this.port = config.clamd_port();
           this.timeout = config.clamd_timeout();
       }

       @Override
       public FileAttachmentValidationResult validateFileAttachment(FileAttachmentWrapper wrapper) {

           if (wrapper == null) {
               return new FileAttachmentValidationResult(false, "No attachment was received.", wrapper);
           }

           byte[] content = wrapper.getValue();
           if (content == null || content.length == 0) {
               return new FileAttachmentValidationResult(false, "The attached file is empty.", wrapper);
           }

           try {
               String response = scan(content);

               if (response.endsWith("OK")) {
                   return new FileAttachmentValidationResult(true, "File passed the virus scan.", wrapper);
               }
               if (response.contains("FOUND")) {
                   return new FileAttachmentValidationResult(false,
                           "A virus was detected in the attached file. Upload was rejected.", wrapper);
               }
               return new FileAttachmentValidationResult(false,
                       "The file could not be scanned. Please try again later.", wrapper);

           } catch (Exception e) {
               // Fail closed: reject when clamd is unreachable rather than accept an unscanned file.
               return new FileAttachmentValidationResult(false,
                       "The virus scanner is unavailable. Please try again later.", wrapper);
           }
       }

       /**
        * Streams the file to clamd using the INSTREAM command and returns the daemon's response.
        */
       private String scan(byte[] data) throws Exception {
           try (Socket socket = new Socket()) {
               socket.connect(new InetSocketAddress(host, port), timeout);
               socket.setSoTimeout(timeout);

               try (OutputStream raw = socket.getOutputStream();
                    DataOutputStream out = new DataOutputStream(raw);
                    InputStream in = socket.getInputStream()) {

                   out.writeBytes("zINSTREAM\0");

                   for (int offset = 0; offset < data.length; offset += CHUNK_SIZE) {
                       int len = Math.min(CHUNK_SIZE, data.length - offset);
                       out.writeInt(len);
                       out.write(data, offset, len);
                   }

                   out.writeInt(0); // zero-length chunk signals end of stream
                   out.flush();

                   ByteArrayOutputStream responseBuffer = new ByteArrayOutputStream();
                   byte[] buffer = new byte[512];
                   int read;
                   while ((read = in.read(buffer)) != -1) {
                       responseBuffer.write(buffer, 0, read);
                   }
                   return responseBuffer.toString(StandardCharsets.US_ASCII.name()).trim();
               }
           }
       }

       @Override
       public String getFileAttachmentValidatorName() {
           return VALIDATOR_NAME;
       }
   }
   ```

1. Save the file.

## Step 5: Build and deploy to AEM {#step-5-deploy}

1. With AEM running (assumption #1), build and deploy from your project root. This command installs the bundle onto the local author instance:

   ```
   cd <PROJECT_ROOT>
   mvn clean install -PautoInstallBundle
   ```

   **Expected result:** the build ends with `BUILD SUCCESS`.

1. Confirm the service is running. Open the components console:

   ```
   http://localhost:4502/system/console/components
   ```

   This page has no built-in search box — with 5,000+ components listed, use your browser's own find-in-page (Cmd+F or Ctrl+F) and search for `ClamAVFileAttachmentValidator`.

   **Expected result:** the component is listed and its state is **active** (or **satisfied**). If it is unsatisfied, see Troubleshooting.

   ![Components console showing ClamAVFileAttachmentValidator and FileAttachmentValidatorDataSourceServlet as active](/help/forms/assets/file-attachment-validator-osgi-components.png)

## Step 6: Configure the clamd connection {#step-6-config}

Tell the validator where `clamd` is. For local development the defaults (`localhost:3310`) already match Step 1, so this step is only needed if your values differ. Do it once to confirm the settings exist.

1. Open the configuration console:

   ```
   http://localhost:4502/system/console/configMgr
   ```

1. This page also has no built-in search box — use your browser's find-in-page (Cmd+F or Ctrl+F) for **ClamAV File Attachment Scanner** and open it.

1. Confirm or set:

   | Setting | Value for this tutorial |
   |---|---|
   | clamd Host | `localhost` |
   | clamd Port | `3310` |
   | Scan Timeout (ms) | `30000` |

   ![ClamAV File Attachment Scanner configuration dialog in the OSGi configuration console](/help/forms/assets/clamav-scanner-configmgr.png)

1. Select **Save**.

>[!NOTE]
>
>For real environments, deploy these values as a repository OSGi configuration in your project (a `.cfg.json` file per environment) so they travel with each deployment instead of being set by hand.

## Step 7: Add the validator field to the form dialog {#step-7-dialog-field}

The **File Attachment Virus Scanner / Validator** field does not exist in the out-of-the-box Adaptive Form Container dialog — for Core Components-based forms, you add it once, in your own project. This is a one-time step; you don't repeat it if you later add more validators.

1. If your `formcontainer` proxy component doesn't already exist, create it at:

   ```
   <PROJECT_ROOT>/ui.apps/src/main/content/jcr_root/apps/<APP_ID>/components/adaptiveForm/formcontainer/.content.xml
   ```

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <jcr:root xmlns:jcr="http://www.jcp.org/jcr/1.0" xmlns:sling="http://sling.apache.org/jcr/sling/1.0"
       jcr:primaryType="cq:Component"
       jcr:title="Form Container"
       sling:resourceSuperType="core/fd/components/form/container/v2/container"/>
   ```

   If you already have this component (most projects created from the Core Components archetype do), skip to the next step.

1. Create a dialog extension at:

   ```
   <PROJECT_ROOT>/ui.apps/src/main/content/jcr_root/apps/<APP_ID>/components/adaptiveForm/formcontainer/_cq_dialog/.content.xml
   ```

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <jcr:root xmlns:jcr="http://www.jcp.org/jcr/1.0" xmlns:sling="http://sling.apache.org/jcr/sling/1.0"
       jcr:primaryType="nt:unstructured">
     <content jcr:primaryType="nt:unstructured">
       <items jcr:primaryType="nt:unstructured">
         <tabs jcr:primaryType="nt:unstructured">
           <items jcr:primaryType="nt:unstructured">
             <submitActions jcr:primaryType="nt:unstructured">
               <items jcr:primaryType="nt:unstructured">
                 <columns jcr:primaryType="nt:unstructured">
                   <items jcr:primaryType="nt:unstructured">
                     <fileAttachmentValidator
                         jcr:primaryType="nt:unstructured"
                         sling:resourceType="granite/ui/components/coral/foundation/form/select"
                         fieldLabel="File Attachment Virus Scanner/Validator"
                         fieldDescription="Select a registered validator configuration to scan submitted file attachments. Select None to disable validation for this form."
                         emptyText="None"
                         name="./fileAttachmentValidator">
                       <datasource
                           jcr:primaryType="nt:unstructured"
                           sling:resourceType="<APP_ID>/datasources/fileattachmentvalidators"/>
                     </fileAttachmentValidator>
                   </items>
                 </columns>
               </items>
             </submitActions>
           </items>
         </tabs>
       </items>
     </content>
   </jcr:root>
   ```

   This only defines the one new field, mirroring the real dialog's node names down to the insertion point — it does not redefine or replace any of the existing Submission tab fields. See [Add the validator field to the form dialog](/help/forms/scan-file-attachments-custom-validator.md#add-dialog-field) in the companion article for why this works.

1. Add the datasource servlet that lists your registered validators. It's identical regardless of which validator engine you're using — see [Add the validator field to the form dialog](/help/forms/scan-file-attachments-custom-validator.md#add-dialog-field) in the companion article for what it does and why. Create it at:

   ```
   <PROJECT_ROOT>/core/src/main/java/com/example/forms/security/FileAttachmentValidatorDataSourceServlet.java
   ```

   ```java
   package com.example.forms.security;

   import com.adobe.forms.common.service.FileAttachmentValidator;
   import com.adobe.forms.common.service.FileAttachmentValidatorManager;
   import com.adobe.granite.ui.components.ds.DataSource;
   import com.adobe.granite.ui.components.ds.SimpleDataSource;
   import com.adobe.granite.ui.components.ds.ValueMapResource;
   import org.apache.sling.api.SlingHttpServletRequest;
   import org.apache.sling.api.SlingHttpServletResponse;
   import org.apache.sling.api.resource.Resource;
   import org.apache.sling.api.resource.ResourceMetadata;
   import org.apache.sling.api.servlets.HttpConstants;
   import org.apache.sling.api.servlets.SlingSafeMethodsServlet;
   import org.apache.sling.api.wrappers.ValueMapDecorator;
   import org.apache.sling.servlets.annotations.SlingServletResourceTypes;
   import org.osgi.service.component.annotations.Component;
   import org.osgi.service.component.annotations.Reference;
   import org.osgi.service.component.annotations.ReferenceCardinality;
   import org.osgi.service.component.annotations.ReferencePolicy;

   import javax.servlet.Servlet;
   import java.util.ArrayList;
   import java.util.HashMap;
   import java.util.List;
   import java.util.Map;

   @Component(service = { Servlet.class })
   @SlingServletResourceTypes(
           resourceTypes = "<APP_ID>/datasources/fileattachmentvalidators",
           methods = HttpConstants.METHOD_GET)
   public class FileAttachmentValidatorDataSourceServlet extends SlingSafeMethodsServlet {

       @Reference(cardinality = ReferenceCardinality.OPTIONAL, policy = ReferencePolicy.DYNAMIC)
       private volatile FileAttachmentValidatorManager fileAttachmentValidatorManager;

       @Override
       protected void doGet(SlingHttpServletRequest request, SlingHttpServletResponse response) {
           List<Resource> options = new ArrayList<>();

           FileAttachmentValidatorManager manager = fileAttachmentValidatorManager;
           if (manager != null) {
               List<FileAttachmentValidator> validators = manager.getValidators();
               if (validators != null) {
                   for (FileAttachmentValidator validator : validators) {
                       String name = validator.getFileAttachmentValidatorName();
                       if (name != null && !name.isEmpty()) {
                           options.add(createOption(request, name));
                       }
                   }
               }
           }

           DataSource dataSource = new SimpleDataSource(options.iterator());
           request.setAttribute(DataSource.class.getName(), dataSource);
       }

       private Resource createOption(SlingHttpServletRequest request, String name) {
           Map<String, Object> props = new HashMap<>();
           props.put("value", name);
           props.put("text", name);
           return new ValueMapResource(request.getResourceResolver(), new ResourceMetadata(),
                   "nt:unstructured", new ValueMapDecorator(props));
       }
   }
   ```

   Replace `<APP_ID>` in both the dialog XML and the servlet's `resourceTypes` with your project's actual application ID (matching assumption #4), and adjust the package name if yours differs from Step 4.

1. Build and deploy both changes. You changed content (the dialog) and code (the servlet), so use both profiles together — `autoInstallPackage` alone only deploys the content and leaves the servlet's bundle un-redeployed:

   ```
   cd <PROJECT_ROOT>
   mvn clean install -PautoInstallPackage,autoInstallBundle
   ```

   **Expected result:** the build ends with `BUILD SUCCESS`, and the `ui.apps` content package (including this dialog change) and the `core` bundle (including the new servlet) are both installed.

>[!NOTE]
>
>You might register more than one validator over time — for example, one per antivirus engine, or several differently configured instances of the same engine. Nothing here needs to change for that: every registered `FileAttachmentValidator` shows up in the drop-down automatically because each has its own `getFileAttachmentValidatorName()`, and `emptyText="None"` keeps "no validator" as the default so existing forms are unaffected until you explicitly choose one.

## Step 8: Create the sample Adaptive Form {#step-8-form}

Now create a simple form with a file-upload field.

1. Open Forms & Documents:

   ```
   http://localhost:4502/aem/forms.html/content/dam/formsanddocuments
   ```

1. Select **Create** (top right), then **Adaptive Form**.

1. Pick a template from the gallery. The foundation isn't a separate question — it's part of the template you pick, shown as a small subtitle under each template's name (for example, **Adaptive Form (Core Components)**).

   >[!IMPORTANT]
   >
   >Several templates are all named **Blank Form** — one for Core Components, one for Foundation Components, one for Edge Delivery Services. Picking the wrong one is easy to miss and fails silently: the rest of this tutorial still appears to work, but the File Attachment Virus Scanner / Validator field never gets invoked, because that pipeline only exists for Core Components-based forms. Confirm the subtitle reads **Adaptive Form (Core Components)** before continuing.

1. In **Properties**, set:

   * **Title:** `File Attachment Scanner Demo`
   * **Theme:** pick any available theme (for example, Canvas)

   Then select **Create**.

1. In the confirmation dialog, select **Open** to open the form in the editor.

   **Expected result:** the Adaptive Form editor opens with an empty form.

1. Add a file-upload field:

   * Open the **Components** browser (the components icon in the left rail, or select the empty form area and choose the insert-component option).
   * Find the **File Attachment** component and drag it onto the form.

1. Add a submit button:

   * From the same Components browser, drag an **Adaptive Form Button** onto the form, below the file field.
   * Select the button, open its properties (the wrench icon), set its **Button Type** to **Submit**, and confirm.

1. Save the form. The editor saves automatically, but you can force it by leaving the editor.

   **Expected result:** the form now has a file-attachment field and a submit button.

## Step 9: Connect the ClamAV Scanner to the form {#step-9-connect}

1. In the form editor, select the **Guide Container** (the outermost container) to open the **Adaptive Form Container** properties. Use the properties (wrench) icon.

1. Open the **Submission** tab.

1. Find the **File Attachment Virus Scanner / Validator** drop-down list and select **ClamAV Scanner**.

   >This field and its list of options came from Step 7 — the dialog extension and datasource servlet you deployed to your own project. The entry is the name returned by `getFileAttachmentValidatorName()` in your code. If you changed `VALIDATOR_NAME`, select that name instead.

   >[!IMPORTANT]
   >
   >If this field is missing entirely, you haven't completed Step 7, or the `ui.apps` package from Step 7 didn't deploy. This field is never present out of the box for Core Components-based forms.

1. Select **Done**, then save the form.

![Submission tab of the Adaptive Form Container dialog with ClamAV Scanner selected in the File Attachment Virus Scanner/Validator field](/help/forms/assets/file-attachment-validator-submission-tab.png)

## Step 10: Test the integration {#step-10-test}

Test both outcomes.

### Test A: a clean file is accepted {#test-clean}

1. Open the form's preview:

   ```
   http://localhost:4502/content/dam/formsanddocuments/file-attachment-scanner-demo/jcr:content?wcmmode=disabled
   ```

   If your form's path differs, open it from Forms & Documents and select **Preview**.

1. Attach an ordinary PDF or image, then select **Submit**.

   **Expected result:** the form submits successfully.

### Test B: a test virus is blocked {#test-virus}

1. Create a plain text file named `eicar.txt` whose only contents are the standard EICAR antivirus test string. This is a harmless file that every antivirus engine detects on purpose:

   ```
   X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
   ```

   You can also download it from [eicar.org](https://www.eicar.org/download-anti-malware-testfile/).

1. In the form, attach `eicar.txt` and select **Submit**.

   **Expected result:** the submission is blocked. How the rejection is surfaced varies by the form's configured **Submit action** — a standard thank-you-page flow typically shows an inline error on the file field, while **Submit to REST endpoint** (this tutorial's sample form uses this) tends to show a generic submission-failed message instead of a field-level one. Either way, the form does not submit.

1. Confirm the validator actually ran and rejected the file — check the AEM error log, which is the reliable way to see what happened regardless of how the failure was displayed in the browser:

   ```
   <AEM_SDK_FOLDER>/crx-quickstart/logs/error.log
   ```

   Look for the rejection message from your validator (for example, `A virus was detected in the attached file`).

## Troubleshooting {#troubleshooting}

**`docker run` fails with `no matching manifest for linux/arm64/v8`.** You're on an Apple Silicon Mac; the `clamav/clamav` image has no native arm64 build. Add `--platform linux/amd64` to the command in Step 1.

**`PONG` not returned in Step 1.** `clamd` is not ready or the port is not published. Check `docker logs clamav` for database-load completion, and confirm the container maps port `3310` (`docker ps`).

**Step 2's archetype command fails with `Unsupported class file major version...`.** Your default `java`/`mvn` is running on a newer JDK than assumption #5 allows — the archetype's post-generation script can't parse class files from Java versions newer than 21. Point `JAVA_HOME` at a Java 11 or 21 installation and re-run the command. If the first attempt already partially generated a project (mismatched module folders, missing files), delete that output directory before retrying rather than re-running in place.

**Project does not compile (cannot find `FileAttachmentValidator`).** The Early Access dependency (Step 3) is missing, wasn't installed to your local Maven repository, or `pom.xml`'s version doesn't match the jar you installed. Re-check the version with `unzip -l addon.far | grep adobe-xfaforms-common`.

**Component is unsatisfied in Step 5.** Open `http://localhost:4502/system/console/components`, find `ClamAVFileAttachmentValidator`, and read the reason. A missing interface usually means the dependency is not present at runtime. Confirm your AEM environment has the Early Access feature.

**The File Attachment Virus Scanner / Validator field doesn't appear on the Submission tab at all (Step 9).** Confirm the Step 7 `ui.apps` package (the dialog extension and datasource servlet) actually deployed — check `http://localhost:4502/system/console/components` for `FileAttachmentValidatorDataSourceServlet`. Also confirm the `FT_FORMS-23497` feature toggle is enabled for your program; it gates the underlying `FileAttachmentValidatorManager` capability the datasource depends on.

**The field appears, but ClamAV Scanner isn't in the drop-down (Step 9).** Confirm the `ClamAVFileAttachmentValidator` component is active, that `getFileAttachmentValidatorName()` returns a unique non-empty value, and reload the form editor after deploying.

**Every file is rejected, even clean ones.** The validator fails closed, so this usually means it cannot reach `clamd`. Recheck Step 1 (is `clamd` running and returning `PONG`?) and Step 6 (host, port, timeout). Look in `error.log` for connection errors or `ERROR` responses.

**Scans time out or `INSTREAM size limit exceeded`.** The file is too large for the timeout or for `clamd`'s `StreamMaxLength`. Increase the timeout in Step 6, raise `StreamMaxLength` in `clamd.conf`, and set a maximum file size on the File Attachment component so oversized files are stopped earlier.

**EICAR submission shows a generic error, not an inline field message (Step 10).** This is expected with a **Submit to REST endpoint** submit action — it doesn't change whether the file was actually rejected. Check `error.log` for the validator's rejection message to confirm.

## Frequently asked questions {#faq}

**Can AEM Forms scan uploads with ClamAV?**
Yes. You implement the `FileAttachmentValidator` interface with a service that streams each uploaded file to a ClamAV daemon (`clamd`) at submission and rejects the file if ClamAV reports a threat.

**Do I need to install ClamAV on the AEM server?**
No. `clamd` runs as a separate process. Your validator connects to it over TCP. Run it locally for development, and as a co-located or external service in real environments.

**Which port does clamd use?**
By default, TCP port `3310`. The sample validator uses this port and lets you change it through OSGi configuration.

**How do I test that virus scanning works?**
Submit an ordinary file to confirm it is accepted, then submit the EICAR test file (a harmless, industry-standard test string) to confirm it is detected and blocked.

**Why are all my files being rejected?**
The sample validator fails closed, so a connection problem with `clamd` causes every file to be rejected. Confirm `clamd` is running and reachable, and check the host, port, and timeout settings.

**Can I use ClamAV with AEM as a Cloud Service?**
Yes, but you cannot run `clamd` on the AEM host. Run it as a co-located or external service and point the validator at it, ideally in the same region to keep file content within your environment.

## Related articles {#related-articles}

* [Scan file attachments in Adaptive Forms with a custom validator](/help/forms/scan-file-attachments-custom-validator.md)
* [Configure the File Attachment component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/file-attachment)
