---
title: Scan file attachments in Adaptive Forms with a custom validator
description: Learn how the File Attachment Virus Scanner / Validator works in AEM Adaptive Forms, understand the FileAttachmentValidator interface, and build a validator that can call any antivirus or validation engine.
keywords: virus scan file attachment, antivirus scan Adaptive Forms, malware scanning form upload, block malicious file upload, file attachment security AEM Forms, FileAttachmentValidator
feature: Adaptive Forms, Core Components
role: Developer, Admin
hide: true
---

# Scan file attachments in Adaptive Forms with a custom validator

[!BADGE AEM Forms]{type=Positive tooltip="Applies to AEM Forms"}

<span class="preview"> The File Attachment Virus Scanner / Validator capability is under the Early Adopter Program. You can write to aem-forms-ea@adobe.com from your official email id to join the early adopter program and request access to the capability. </span>

Adaptive Forms can pass every uploaded attachment to a validator of your choice at submission time. The validator runs on the server, receives the file in memory, and decides whether the submission is accepted or rejected, so a malicious or non-compliant file is never persisted. Because you supply the validator, you can connect any antivirus engine, malware scanner, or custom validation logic you already use.

This article explains the capability, documents the `FileAttachmentValidator` interface you implement, and walks through building an antivirus-agnostic validator. For a complete, engine-specific example, see the companion tutorial [Scan file attachments with ClamAV](/help/forms/scan-file-attachments-clamav.md).

## How it works {#how-it-works}

When a user submits an Adaptive Form that has a validator selected, AEM invokes your validator for the uploaded attachment before the submission is processed:

1. The user attaches a file and selects **Submit**.
1. On the server, AEM calls your validator's `validateFileAttachment` method, passing the attachment (including its raw bytes) as a `FileAttachmentWrapper`.
1. Your validator inspects the file by calling an antivirus engine, applying validation rules, or both, then returns a `FileAttachmentValidationResult`.
1. If the result is valid, submission continues. If it is invalid, AEM blocks the submission, shows the user the message from the result, and flags the attachment field.

Two properties of this model matter for security:

* **Server-side.** The check runs on the server, so it cannot be bypassed from the browser.
* **Scan before persist.** The file is evaluated from memory before it is stored, so a rejected file is never written to the repository.

## Availability and prerequisites {#prerequisites}

* An Adaptive Form based on Core Components.
* A Maven project set up to build and deploy an AEM bundle.
* A compile-time dependency that provides the `com.adobe.forms.common.service` interfaces (`FileAttachmentValidator`, `FileAttachmentWrapper`, `FileAttachmentValidationResult`, `FileAttachmentValidatorManager`) — `com.adobe.forms.foundation:adobe-xfaforms-common`, bundled in the AEM Forms add-on SDK. See [Step 3 of the ClamAV tutorial](/help/forms/scan-file-attachments-clamav.md#step-3-dependency) for where to get it and how to install it locally.
* An Adaptive Form Container **proxy component** in your project (the standard pattern for extending Core Components), so you have somewhere to add the Submission tab field described in [Add the validator field to the form dialog](#add-dialog-field). This applies to Core Components-based forms only.

>[!NOTE]
>
>The **File Attachment Virus Scanner / Validator** field is **not** provided out of the box — you add it yourself with a small dialog extension on your project's Adaptive Form Container component. This is a one-time step per project (not per validator). See [Add the validator field to the form dialog](#add-dialog-field).

## The FileAttachmentValidator interface {#interface-reference}

You add a validator by implementing `com.adobe.forms.common.service.FileAttachmentValidator` and registering it as an OSGi service. The interface defines two methods.

### FileAttachmentValidator {#fileattachmentvalidator}

| Method | Returns | Description |
|---|---|---|
| `validateFileAttachment(FileAttachmentWrapper fileAttachmentWrapper)` | `FileAttachmentValidationResult` | Called by the framework for an uploaded attachment. Inspect the attachment and return a result indicating whether it is accepted. |
| `getFileAttachmentValidatorName()` | `String` | Returns the name that identifies this validator. This name is used to select the validator on a form. |

### FileAttachmentWrapper {#fileattachmentwrapper}

The wrapper gives your code access to the uploaded file and its metadata. The accessors used in a typical validator are:

| Method | Returns | Description |
|---|---|---|
| `getFileNameV2()` | `String` | The name of the uploaded file, for example `invoice.pdf`. |
| `getContentType()` | `String` | The MIME type reported for the file, for example `application/pdf`. |
| `getValue()` | `byte[]` | The raw contents of the file, held in memory. This is what you pass to your scanning engine. |

>[!NOTE]
>
>The table lists the accessors commonly used in a validator. The SDK version you build against may expose additional methods on `FileAttachmentWrapper`. Check the interface in your dependency for the complete set.

### FileAttachmentValidationResult {#fileattachmentvalidationresult}

Your validator returns a `FileAttachmentValidationResult` to tell the framework whether to accept the attachment. Construct it with these parameters:

| Parameter | Type | Description |
|---|---|---|
| `isValid` | `boolean` | `true` to accept the attachment, `false` to reject it and block submission. |
| `message` | `String` | A human-readable message. On rejection, this explains why the file was not accepted. |
| `fileAttachmentWrapper` | `FileAttachmentWrapper` | The wrapper that was validated. |

For example: `new FileAttachmentValidationResult(false, "The attached file failed the security scan.", wrapper)`.

>[!NOTE]
>
>If you need to read a `FileAttachmentValidationResult` back (for example, in a test or in code that calls a validator directly), use `isFileAttachmentValid()` and `getResponseString()`/`setResponseString()`. The class does not expose `isValid()` or `getMessage()` methods — those names describe the constructor parameters above, not the getters.

### FileAttachmentValidatorManager {#fileattachmentvalidatormanager}

AEM registers a single `FileAttachmentValidatorManager` service that sits between the framework and every validator you deploy. You don't normally need to call it yourself — AEM uses it to look up the validator selected on a form and to invoke it — but it's useful to know about when troubleshooting, since it's what the Submission tab's dropdown and the core submission pipeline both go through.

| Method | Returns | Description |
|---|---|---|
| `getValidators()` | `List<FileAttachmentValidator>` | All currently registered `FileAttachmentValidator` OSGi services. |
| `getFileAttachmentValidator(String name)` | `FileAttachmentValidator` | The validator whose `getFileAttachmentValidatorName()` matches `name`, or throws if none matches. |
| `validateFileAttachment(String name, List<FileAttachmentWrapper> attachments)` | `List<FileAttachmentValidationResult>` | Runs the named validator against multiple attachments at once. Used internally when a submission includes more than one file. |

### Registering the OSGi service {#register-service}

Annotate your implementation so it is registered under the `FileAttachmentValidator` interface. After you deploy it, the validator becomes selectable on your forms.

>[!NOTE]
>
>This article uses the modern OSGi Declarative Services annotations (`org.osgi.service.component.annotations`). Older samples you may find elsewhere use the Apache Felix SCR annotations (`org.apache.felix.scr.annotations`); those are deprecated and should not be used for new validators.

## Build an antivirus-agnostic validator {#build-validator}

The following implementation shows the structure of a validator without tying it to a specific engine. Replace the `scanWithYourEngine` method with a call to your antivirus, scanning API, or validation service.

```java
package com.example.forms.security;

import com.adobe.forms.common.service.FileAttachmentValidator;
import com.adobe.forms.common.service.FileAttachmentValidationResult;
import com.adobe.forms.common.service.FileAttachmentWrapper;
import org.osgi.service.component.annotations.Component;

@Component(service = FileAttachmentValidator.class)
public class CustomFileAttachmentValidator implements FileAttachmentValidator {

    private static final String VALIDATOR_NAME = "Custom Antivirus Scanner";

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
            boolean clean = scanWithYourEngine(content);
            if (clean) {
                return new FileAttachmentValidationResult(true, "File passed the security scan.", wrapper);
            }
            return new FileAttachmentValidationResult(false,
                    "The attached file failed the security scan and was rejected.", wrapper);

        } catch (Exception e) {
            // Fail closed: if the scanner cannot be reached, reject rather than let an
            // unscanned file through. See Best practices for the fail-open alternative.
            return new FileAttachmentValidationResult(false,
                    "The file could not be scanned at this time. Please try again later.", wrapper);
        }
    }

    @Override
    public String getFileAttachmentValidatorName() {
        return VALIDATOR_NAME;
    }

    /**
     * Integrate your antivirus or validation engine here.
     * Return true if the file is safe to accept, false if it should be rejected.
     */
    private boolean scanWithYourEngine(byte[] content) {
        // TODO: call a local scanning daemon (for example over a socket)
        // or a remote scanning API, and interpret its verdict.
        return true;
    }
}
```

## Build and deploy the bundle {#build-deploy}

Compile your project and install the bundle so the validator is registered on the AEM instance.

**Deploy to a local instance during development.** From your project root, build and install the bundle onto the running author instance:

```
mvn clean install -PautoInstallBundle
```

The `autoInstallBundle` profile pushes the compiled bundle to a local AEM instance (by default `http://localhost:4502`). If your instance runs on a different host, port, or credentials, pass them to the build, for example:

```
mvn clean install -PautoInstallBundle -Daem.host=localhost -Daem.port=4502 -Dvault.user=admin -Dvault.password=admin
```

**Deploy to higher environments.** For staging and production, do not install the bundle by hand. Deploy it as part of your project's `all` content package through your CI/CD pipeline. For the full procedure, see [Deploying to AEM as a Cloud Service](/help/implementing/deploying/overview.md).

**Confirm the service is registered.** Open the components console and search for your validator class:

```
http://localhost:4502/system/console/components
```

The component should be listed with its state shown as **active** (or **satisfied**), registered under the `FileAttachmentValidator` service. If it is unsatisfied, see [Verify your validator loads and runs](#verify).

![Components console showing a custom validator and its datasource servlet as active](/help/forms/assets/file-attachment-validator-osgi-components.png)

## Add the validator field to the form dialog {#add-dialog-field}

This section applies to Adaptive Forms based on **Core Components**. The **File Attachment Virus Scanner / Validator** field does not exist in the out-of-the-box Adaptive Form Container dialog — you add it once, in your own project, as a small extension. Every validator you deploy afterward (see [Build an antivirus-agnostic validator](#build-validator)) then shows up as an option automatically; you don't repeat this step per validator.

Your project's Adaptive Form Container is a **proxy component** — a component under `/apps` that points at the real Core Component using `sling:resourceSuperType`, for example:

```xml
<!-- /apps/<project>/components/adaptiveForm/formcontainer/.content.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<jcr:root xmlns:jcr="http://www.jcp.org/jcr/1.0"
    jcr:primaryType="cq:Component"
    jcr:title="Form Container"
    sling:resourceSuperType="core/fd/components/form/container/v2/container"
    xmlns:sling="http://sling.apache.org/jcr/sling/1.0"/>
```

Because of `sling:resourceSuperType`, you can add **one new field** to the inherited Submission tab without copying the whole dialog. The Sling Resource Merger only needs the node-name path recreated down to the insertion point — see [Extending Component Dialogs](/help/implementing/developing/components/reference.md#extending-component-dialogs) for the general mechanism. The real OOTB Submission tab keeps its fields under `content/items/tabs/items/submitActions/items/columns/items/`, so that's the path to mirror:

```xml
<!-- /apps/<project>/components/adaptiveForm/formcontainer/_cq_dialog/.content.xml -->
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
                        sling:resourceType="<project>/datasources/fileattachmentvalidators"/>
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

Two details worth calling out:

* **`emptyText="None"`** gives the field an unselected default state, so a form with nothing chosen simply has no validator applied. You don't need to add a fake "None" entry to the datasource below.
* **Multiple configurations are expected.** You might register more than one validator — one per antivirus engine, or several differently configured instances of the same engine. Each registered `FileAttachmentValidator` has its own `getFileAttachmentValidatorName()`, so each one appears as a separate option automatically; nothing about this dialog fragment changes based on how many you register.

The `datasource` child node points at a small Sling servlet you also write. It has one job: ask [`FileAttachmentValidatorManager`](#fileattachmentvalidatormanager) for `getValidators()`, and turn each validator's `getFileAttachmentValidatorName()` into a drop-down option. For the complete, ready-to-use implementation, see [Step 7 of the ClamAV tutorial](/help/forms/scan-file-attachments-clamav.md#step-7-dialog-field) — the servlet is identical regardless of which validator engine you're using, so you can copy it as-is into your project.

Deploy both files as part of your project's `ui.apps` content package and `core` bundle (see [Build and deploy the bundle](#build-deploy)). Once deployed, this dialog extension is verified working: the field appears on the Submission tab alongside the existing OOTB fields (not replacing them), and setting it persists a plain `fileAttachmentValidator` property on the guide container node, which AEM's submission pipeline reads via `FileAttachmentValidatorManager.getFileAttachmentValidator(name)`.

## Select the validator on your form {#select-validator}

1. Open your Adaptive Form for editing and select the **Guide Container** to open the **Adaptive Form Container** properties.
1. Go to the **Submission** tab.
1. From the **File Attachment Virus Scanner / Validator** drop-down list, select your validator. Assuming you've completed [Add the validator field to the form dialog](#add-dialog-field), this list is populated with the names returned by `getFileAttachmentValidatorName()` for every currently registered validator. Select **None** (the default) to disable validation for this form.
1. Select **Done** and save the form.

![Submission tab of the Adaptive Form Container dialog with a validator selected in the File Attachment Virus Scanner/Validator field](/help/forms/assets/file-attachment-validator-submission-tab.png)

>[!IMPORTANT]
>
>If you don't see a **File Attachment Virus Scanner / Validator** field on the Submission tab at all, you (or your project) haven't completed [Add the validator field to the form dialog](#add-dialog-field) yet — for Core Components-based forms, this field is never present out of the box.

## Runtime behavior and user experience {#runtime-behavior}

* **File accepted.** When your validator returns a valid result, submission proceeds as normal.
* **File rejected.** When your validator returns an invalid result, AEM stops the submission, displays the message from the result to the user, and marks the file attachment field with a validation error. The form data is not submitted.

## Verify your validator loads and runs {#verify}

1. After deploying, confirm the bundle is active and the component is satisfied in the OSGi console (**Status** > **Components**), listed under the `FileAttachmentValidator` service.
1. Open a form's **Submission** settings and confirm your validator appears in the drop-down.
1. Submit the form with a test file and confirm your validator is invoked (add a log statement during development).

If the **File Attachment Virus Scanner / Validator** field itself does not appear on the Submission tab:

* Confirm your project has deployed the dialog extension and datasource servlet from [Add the validator field to the form dialog](#add-dialog-field) — this field is not present out of the box for Core Components-based forms.
* Confirm the `FT_FORMS-23497` feature toggle is enabled for your program; it gates the underlying `FileAttachmentValidatorManager` capability that the datasource servlet depends on.

If the field appears, but your validator is not listed in the drop-down:

* Confirm the bundle is installed and active, and that the component is registered under `FileAttachmentValidator` and not in an unsatisfied state.
* Confirm `getFileAttachmentValidatorName()` returns a non-empty, unique name.
* Reload the form editor after deploying the bundle.

## Best practices and considerations {#best-practices}

**Decide where scanning happens.** Your validator can call a scanning engine that runs locally (or co-located with AEM) or a remote scanning API. A local or co-located engine keeps file content inside your environment, which helps satisfy data-residency and compliance requirements. A remote API sends file bytes outside the environment, so confirm that is acceptable for your data before choosing it.

**Choose a failure mode deliberately.** When the scanning engine is unreachable or errors, you can fail closed (reject the file, as in the sample above) or fail open (accept it). Fail closed is the safer default for security-sensitive forms. Fail open favors availability. Make the choice explicit rather than accidental.

**Account for latency.** Scanning happens synchronously during submission, so the scan time is added to the user's submit experience. Set sensible timeouts on calls to your engine, and set expectations with a service-level agreement if you depend on an external service.

**Bound the payload.** `getValue()` returns the file as an in-memory `byte[]`, so large uploads consume heap. Constrain uploads at the source using the File Attachment component's maximum file size and supported file types, so the validator only handles reasonably sized, expected files.

**Layer your controls.** A validator is strongest as one layer among several. Restrict file types and sizes on the File Attachment component, scan at submission with your validator, and add bot protection such as CAPTCHA. No single layer is sufficient on its own.

**Write clear rejection messages.** The `message` in the result is shown to the user, so make it actionable, for example "This file type is not allowed. Upload a PDF." Consider localization if your forms serve multiple languages.

**Secure and monitor the scan channel.** Use secure transport to your scanning engine, keep it highly available because it sits in the submission path, and log scan outcomes for auditing and troubleshooting.

## Frequently asked questions {#faq}

**What is a file attachment validator in AEM Forms?**
It is a server-side service you register in AEM that inspects each file uploaded through an Adaptive Form at submission time and tells AEM whether to accept or reject the file. You select it on a form through the **File Attachment Virus Scanner / Validator** setting.

**When does AEM call the validator?**
At submission, before the form data and attachment are persisted. AEM calls your `validateFileAttachment` method with the attachment, and blocks the submission if the result is invalid.

**Does the validator run in the browser or on the server?**
On the server. The check cannot be bypassed by disabling JavaScript or editing the page in the browser.

**Can I use any antivirus with this interface?**
Yes. The interface does not depend on any specific engine. Your implementation can call a local scanning daemon, a commercial antivirus or data-loss-prevention product, or a remote scanning API, then map the result to a `FileAttachmentValidationResult`.

**Does a rejected file get saved in AEM?**
No. Because the file is evaluated from memory before it is persisted, a rejected file is never written to the repository.

**How do I show a custom message when a file is rejected?**
Set the `message` value when you construct the `FileAttachmentValidationResult`. AEM displays that message to the user when it rejects the file.

## Related articles {#related-articles}

* [Scan file attachments with ClamAV](/help/forms/scan-file-attachments-clamav.md)
* [Configure the File Attachment component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/file-attachment)
* [Configure an Adaptive Form for REST Endpoint submit action](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/forms/integrate/set-submit-action/configure-submit-action-restpoint)
