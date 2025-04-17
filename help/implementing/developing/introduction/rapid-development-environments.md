---
title: Rapid Development Environments
description: Learn how to use Rapid Development Environments for rapid development iterations in a cloud environment.
exl-id: 1e9824f2-d28a-46de-b7b3-9fe2789d9c68
feature: Developing
role: Admin, Architect, Developer
---
# Rapid Development Environments {#rapid-development-environments}

To deploy changes, current Cloud Development environments require the use of a process that employs extensive code security and quality rules called a CI/CD pipeline. For situations where quick and iterative changes are needed, Adobe has introduced Rapid Development Environments (RDEs for short).

RDEs let developers swiftly deploy and review changes, minimizing the amount of time needed to test features that are proven to work in a local development environment.

Once the changes have been tested in an RDE, they can be deployed to a regular Cloud Development environment through the Cloud Manager pipeline.

>[!NOTE]
> Get in touch with the RDE developers on Adobe's [Discord channel](https://discord.com/channels/1131492224371277874/1245304281184079872). Feel free to ask any questions or give feedback regarding RDE topics.

>[!VIDEO](https://video.tv.adobe.com/v/3415582/?quality=12&learn=on)


You can see additional videos demonstrating [how to set it up](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/developing/rde/how-to-setup), [how to use it](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/developing/rde/how-to-use), and the [development life cycle](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/developing/rde/development-life-cycle) using RDE.

## Introduction {#introduction}

RDEs can be used for code, content, and Apache or Dispatcher configurations. Unlike regular Cloud Development environments, developers can use local command-line tools to sync code built locally to an RDE.

Every program is provisioned with an RDE. If there are Sandbox accounts, they are hibernated after a few hours of non-use.

Upon creation, RDEs are set to the most recently available Adobe Experience Manager (AEM) version. An RDE reset, which can be performed using Cloud Manager, cycles the RDE and set it to the most recently available AEM version.

Typically, an RDE is used by a single developer at a given time, for testing and debugging a specific feature. When the development session is done, the RDE can be reset into a default state for the next usage.

Additional RDEs may be licensed for Production (non-sandbox) programs.

## Enable RDE in a program {#enabling-rde-in-a-program}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Click the program to which you want to add an RDE to show its details.

   * RDEs can be added to both [sandbox programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-sandbox-programs.md) and [production programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/introduction-production-programs.md).

1. From the **Program Overview** page, on the **Environments** card, click **Add Environment**.

   ![Environments card](/help/implementing/cloud-manager/assets/no-environments.png)

   * The **Add Environment** option is also available on the **Environments** tab.

     ![Environments tab](/help/implementing/cloud-manager/assets/environments-tab.png)

   * The **Add Environment** option may be disabled due to lack of permissions or depending on the licensed resources.

1. In the **Add environment** dialog box, do the following:

   * Select **Rapid Development** under the **Select environment type** heading.
     * The number of available/used environments is displayed in parentheses behind the environment type.
   * Provide a **Name** for the environment.
   * Provide an optional **Description** for the environment.
   * Select a **Cloud Region**.

   ![Add environment dialog](/help/implementing/cloud-manager/assets/add-environment-wizard.png)

1. Click **Save** to add the specified environment.

The **Overview** screen now displays your new environment in the **Environments** card.

Upon creation, RDEs are set to the most recently available AEM version. An RDE reset, which can also be performed using Cloud Manager, cycles the RDE and set it to the most recently available AEM version.

For more information about using Cloud Manager to create environments, manage who has access to them, and assign custom domains, see [Programs and Program Types](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/program-types.md) in the Cloud Manager documentation.

## Install the RDE command-line tools {#installing-the-rde-command-line-tools}

After you have added an RDE for your program using Cloud Manager, you can interact with it by setting up the command-line tools as described in the following steps:

>[!IMPORTANT]
>
>Make sure you have version 20 of [Node and NPM installed](https://nodejs.org/en/download/) for Adobe I/O CLI and related plugins to work properly.


1. Install the Adobe I/O CLI tools according to this [procedure](https://developer.adobe.com/runtime/docs/guides/tools/cli_install/).
1. Install the Adobe I/O CLI tools AEM RDE plugin:

   ```
   aio plugins:install @adobe/aio-cli-plugin-aem-rde
   aio plugins:update
   ```

1. Login using the aio client. 

   ```
   aio login
   ```

   The login information (token) is stored in the global aio configuration and therefore supports one login and organization only. In case you want to use multiple RDEs that need different logins or organizations, follow the below example introducing contexts. 
   
   <details><summary>Follow this example to set up a local context for one of your RDE logins</summary>
   To store the login information locally in an `.aio` file in the current directory within a specific context, follow these steps. A context is also a clever way to set up a CI/CD environment or script.  To make use of this feature, ensure to use at least aio-cli version 10.3.1. Update it using `npm install -g @adobe/aio-cli`.

   Now, create a context called m`ycontext` that you set as the default context using the auth plugin before calling the login command.

   ```
   aio config set --json -l "ims.contexts.mycontext" "{ cli.bare-output: false }"
   aio auth ctx -s mycontext
   aio login --no-open
   ```

   >[!NOTE]
   > The login command with the `--no-open` option outputs a URL in the terminal instead of opening your default browser. You can copy and open it with an **incognito** window of your browser. This ability ensures that your current session in the main browser window remains unaffected, letting you log in with the specific account and organization required for your task.

   The first command creates a new login context configuration, called `mycontext`, in your local `.aio` configuration file (the file is created if needed. The second command sets the context `mycontext` to be the "current" context; that is, the default.

   With this configuration in place, the login command automatically stores the login tokens in the context `mycontext`, and thus keeps it local.

   Multiple contexts can be managed either by keeping local configurations in multiple folders. Alternatively, it is also possible to set up multiple context within a single configuration file, and switch between them by changing the "current" context.
   </details>
 
1. Configure the RDE plugin to use your organization, program, and environment. The setup command below interactively provides the user with a list of programs in their organization, and show RDE environments in that program to choose from.

   ```
   aio aem:rde:setup
   ```

   You can skip the setup step if you are using a scripted environment. In that case, include the organization, program, and environment values directly in each command. [See RDE commands below for more information](#rde-cli-commands).

### Interactive setup {#installing-the-rde-command-line-tools-interactive}

The setup command asks if the provided configuration should be stored locally or globally.

```
Setup the CLI configuration necessary to use the RDE commands.
? Do you want to store the information you enter in this setup procedure locally? (y/N)
```

Choose `no` to

* store the organization, program and environment globally in your aio configuration.
* work with a single RDE only.

Choose `yes` to do the following:

* Store the organization, program and environment locally in the current directory, in a `.aio` file. This approach is convenient if you want to commit the file to version control so others cloning the Git repository can use it.
* Be able to work with many RDEs, so that switching to another directory uses that configuration instead.
* Use the configuration in a programmatic context like a script, which can reference it.


Once local or global configuration is selected, the setup command tries to read your organization id from your current login and then read the organization's programs. In case the organization cannot be found, you can enter it manually along with some guidance.

```
Selected only organization: XYXYXYXYXYXYXYXXYY
retrieving programs of your organization ...
```

Once the programs are retrieved, the user can select from the list and also type to filter. When the program is selected, a list of RDE environments is listed to choose from. If there is only one program, or only one RDE environment available, or both, it is selected automatically.

To see the current environment context, run the following:

```aio aem rde setup --show```

The command responds with a result similar to the following:

```Current configuration: cm-p1-e1: programName - environmentName (organization: ...@AdobeOrg)```

### Manual setup procedure in a non-interactive environment {#manual-setup}

In environments where no user can interactively run the setup command (such as CI/CD or scripts), manual configuration is required. You can set the organization, program, and environment parameters using the steps below.


<details>
  <summary>Expand to find details on how to configure manually</summary>

1. Configure your organization ID and replace the alphanumeric string with your own organization ID.

   `aio config:set cloudmanager_orgid 4E03EQC05D34GL1A0B49421C@AdobeOrg`

   * Your own organization ID can be looked up using the method documented under [View your organization ID](https://experienceleague.adobe.com/en/docs/core-services/interface/administration/organizations#concept_EA8AEE5B02CF46ACBDAD6A8508646255).

1. Next, configure your program ID:

   `aio config:set cloudmanager_programid 12345`

1. Then, configure the environment ID that the RDE is going to be attached to:

   `aio config:set cloudmanager_environmentid 123456`

1. After you are done configuring the plugin, login by performing

   `aio login`

   These steps require you to be a member of the Cloud Manager **Developer - Cloud Service** Product Profile. See [Assign Team Members to Cloud Manager Product Profiles - Assign the Developer Product Profile](/help/journey-onboarding/assign-profiles-cloud-manager.md#assign-developer) for more details.

For more information and demonstration, watch the video tutorial [how to set up an RDE (06:24)](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/developing/rde/how-to-setup).
</details>

## Use RDE while developing a new feature {#using-rde-while-developing-a-new-feature}

Adobe recommends the following workflow for developing a new feature:

* When an intermediate milestone is reached and successfully validated locally with the AEM as a Cloud Service SDK, commit the code to a Git feature branch. The branch should not be part of the main line yet, although committing to git is optional. What constitutes an "intermediate milestone" varies based on team habits. Examples include a few new lines of code, half a day of work, or completing a subfeature.

* Reset the RDE if it has been used by another feature and you want to [reset it to a default state](#reset-rde). <!-- Alexandru: hiding for now, do not delete This can be done by way of [Cloud Manager](#reset-the-rde-cloud-manager) or by way of the [command line](#reset-the-rde-command-line). -->Reset takes a few minutes and all existing content and code is deleted. You can use the RDE status command to confirm the RDE is ready. The RDE comes back up with the most recent AEM release version.

  >[!IMPORTANT]
  >
  >If your staging and production environments are not receiving automatic AEM release updates and are behind the latest version, the RDE may run a different version of AEM. As a result, the code behavior in the RDE might not match how it functions in staging and production. In that case, it is important to perform thorough testing of the code on staging before deploying it to production.


* Using the RDE command-line interface, sync local code to the RDE. You can install various types of files, including the following:

  * Content packages
  * Specific bundles
  * OSGi configuration files
  * Content files
  * ZIP files containing Apache/Dispatcher configurations 
  
  Referencing a remote content package is also possible. See [RDE Command-Line Tools](/help/implementing/developing/introduction/rapid-development-environments.md#rde-cli-commands) for more information. You can use the status command to validate that the deployment was successful. Optionally, use Package Manager to install content packages.

* Test the code in the RDE. Author and Publish URLs are available in Cloud Manager.

* If the code does not behave as expected, use standard debugging techniques to understand the problem and make the appropriate changes. Without committing the code modifications to Git (since they have not been validated), use the local CLI to sync the code to the RDE. Keep iterating until the issue is resolved.

* Once the code behaves as expected, commit the code to the git feature branch.

* Code synced to RDE does not use a Cloud Manager pipeline so now you should use a Cloud Manager non-production pipeline to deploy the Git feature branch to the Cloud Development environment. This process validates that the code passes the Cloud Manager quality gates and lets you be confident the code is later successfully deployed using the Cloud Manager production pipeline.  

* Repeat the steps above for each intermediate milestone until all code for the feature is ready, and runs well on both the RDE and the Cloud Development environment.

* Deploy the code to production by way of the Cloud Manager production pipeline. 

## Use RDE to debug an existing feature {#use-rde-to-debug-an-existing-feature}

The workflow is similar to developing a new feature. The difference is that the code synced to the RDE reflects the Git label of what was pushed to the environment where the issue occurred. This workflow helps ensure consistency when investigating or reproducing the issue. In addition, it may be useful to deploy content matching the upstream environment. This approach can be achieved through exporting and importing of content packages.

## Multiple developers collaborating on the same RDE {#multiple-developers-collaborating-on-the-same-rde}

An RDE supports a single project at a time. Since code is synced from a local development environment to the RDE environment, it is most natural for one developer to be using it on their own at a given time.

However, with careful coordination, it is possible for more than one developer to validate a specific feature or debug a specific issue. The key is that each developer keeps their local projects in sync so code changes made by a particular developer are absorbed by the other developers. Otherwise, one developer might inadvertently overwrite the other's code. The recommended strategy is for each developer to commit their changes to a shared Git branch before syncing to the RDE, so that the other developers pull the changes before making their own changes.

## RDE command-line tools Commands {#rde-cli-commands}

### Help/General Information {#help}

* For a list of commands, type:

  `aio aem:rde`

* For detailed help for a command, type:

  `aio aem rde <command> --help`

### Global flags {#global-flags}

* For a less verbose output, use the quiet flag:

  `aio aem rde <command> --quiet`

  This flag removes certain elements, such as spinners and progress bars, and limits the need for user input.

* For JSON instead of console log output, use the json flag:

  `aio aem rde <command> --json`

  This flag returns valid JSON while suppressing any console output. See JSON examples further below.

* To avoid configuring the RDE connection information using the setup command, or any aio config creation, use the three flags for organization, program and environment:

  `aio aem rde <command> --organizationId=<value> --programId=<value> --environmentId=<value>`

  Requires an ```aio login``` to be performed.

### Deploy to RDE {#deploying-to-rde}

This section explains how to use the RDE CLI to deploy, install, or update various resources. These resources include the following:

  * Content packages
  * OSGi configurations
  * Bundles
  * Content files
  * Apache or Dispatcher configurations

The general usage pattern is `aio aem:rde:install <artifact>`.

You can find some examples below:

#### Deploy a content package {#deploy-content-package}

`aio aem:rde:install sample.demo.ui.apps.all-1.0.0-SNAPSHOT.zip`

The response for a successful deployment resembles the following:

```
...
#1: deploy completed for content-package sample.demo.ui.apps.all-1.0.0-SNAPSHOT.zip on author,publish - done by 9E072FC75D54FE1A2B49431C@AdobeID at 2022-09-13T11:32:06.229Z
```

Optionally, you can reference a remote repository:

`aio aem:rde:install -t content-package "https://repo1.maven.org/maven2/com/adobe/aem/guides/aem-guides-wknd.all/2.1.0/aem-guides-wknd.all-2.1.0.zip"`

By default, artifacts are deployed to both author and publish tiers, but the `-s` flag can be used to target a specific tier.

Any AEM package can be deployed, such as packages with code, content, or a [container package](/help/implementing/developing/introduction/aem-project-content-package-structure.md#container-packages) (also called the "all" package).

>[!IMPORTANT]
>
>The above content-package installation does not deploy the Dispatcher configuration for the WKND project. Deploy it separately following the "Deploying an Apache/Dispatcher Configuration" steps.

#### Deploy an OSGI configuration {#deploy-OSGI-config}

`aio aem:rde:install com.adobe.granite.demo.MyServlet.cfg.json`

Where the response for a successful deployment resembles the following:

```
...
#2: deploy completed for osgi-config com.adobe.granite.demo.MyServlet.cfg.json on author,publish - done by 9E0725C05D54FE1A0B49431C@AdobeID at 2022-09-13T11:54:36.390Z
```

#### Deploy a bundle {#deploy-bundle}

To deploy a bundle, use:

`aio aem:rde:install ~/.m2/repository/org/apache/felix/org.apache.felix.gogo.jline/1.1.8/org.apache.felix.gogo.jline-1.1.8.jar`

Where the response for a successful deployment resembles the following:

```
...
#3: deploy staged for osgi-bundle org.apache.felix.gogo.jline-1.1.8.jar on author,publish - done by 9E0725C05D53BE1A0B49431C@AdobeID at 2022-09-14T07:54:28.882Z
```

#### Deploy a content file {#deploy-content-file}

To deploy a content file, use:

`aio aem:rde:install world.txt -p /apps/hello.txt`

Where the response for a successful deployment resembles the following:

```
..
#4: deploy completed for content-file world.txt on author,publish - done by 9E0729C05C54FE1A0B49431C@AdobeID at 2022-09-14T07:49:30.644Z
```

#### Deploy an Apache/Dispatcher configuration {#deploy-apache-config}

The entire folder structure must be in the form of a zip file for this type of configuration. 

From the `dispatcher` module of an AEM project, you can zip the Dispatcher configuration by running the below maven command:

`mvn clean package`

Or using the below zip command from the `src` directory of the `dispatcher` module:

`zip -y -r dispatcher.zip .`

Then deploy the configuration by this command:

`aio aem:rde:install target/aem-guides-wknd.dispatcher.cloud-X.X.X-SNAPSHOT.zip`

>[!TIP]
>
>The above command assumes you are deploying the [WKND](https://github.com/adobe/aem-guides-wknd) project's Dispatcher configurations. Make sure to replace the `X.X.X` with the corresponding WKND project version number or your project-specific version number when deploying your project's Dispatcher configuration.

>[!NOTE]
>
>RDE supports "Flexible Mode" Dispatcher configuration, but not "Legacy Mode" Dispatcher configuration. See [Dispatcher documentation](/help/implementing/dispatcher/disp-overview.md#validation-debug) for information about the two modes. You can also consult the documentation on [migrating to Flexible mode](/help/implementing/dispatcher/validation-debug.md#migrating), if you have not done so already.

A successful deployment generates a response that resembles the following:

```
..
#5 deploy completed for dispatcher-config dispatcher.zip on author,publish - done by 9E0735C05T54FE1A0B49431C@AdobeID at 2022-10-03T10:26:31.286Z
Logs:
  Cloud manager validator 2.0.49
  2022/10/03 10:26:37 No issues found
  Syntax OK
```

Code deployed to RDE does not undergo a Cloud Manager pipeline and its associated quality gates. However, the code does go through some analysis, which reports the errors, as illustrated in the code sample below:

```
$ aio aem:rde:install ~/.m2/repository/org/apache/felix/org.apache.felix.gogo.jline/1.1.8/org.apache.felix.gogo.jline-1.1.8.jar
...
#19: deploy staged for osgi-bundle org.apache.felix.gogo.jline-1.1.8.jar on author,publish - done by 9E0725C05D74FR1A0B49431C@AdobeID at 2022-09-14T07:54:28.882Z
Logs:
The analyser found the following errors for author :
[requirements-capabilities] com.adobe.aem.temp:org.apache.felix.gogo.jline:1.1.8: Artifact com.adobe.aem.temp:org.apache.felix.gogo.jline:1.1.8 requires [org.apache.felix.gogo.jline/1.1.8] org.apache.felix.gogo; filter:="(&(org.apache.felix.gogo=command.implementation)(version>=1.0.0)(!(version>=2.0.0)))"; effective:=active in start level 20 but no artifact is providing a matching capability in this start level.
[api-regions-exportsimports] com.adobe.aem.temp:org.apache.felix.gogo.jline:1.1.8: Bundle org.apache.felix.gogo.jline:1.1.8 is importing package(s) [org.jline.builtins, org.jline.utils, org.apache.felix.service.command, org.apache.felix.service.threadio, org.jline.terminal, org.jline.reader, org.apache.felix.gogo.runtime, org.jline.reader.impl] in start level 20 but no bundle is exporting these for that start level.
The analyser found the following errors for publish :
[requirements-capabilities] com.adobe.aem.temp:org.apache.felix.gogo.jline:1.1.8: Artifact com.adobe.aem.temp:org.apache.felix.gogo.jline:1.1.8 requires [org.apache.felix.gogo.jline/1.1.8] org.apache.felix.gogo; filter:="(&(org.apache.felix.gogo=command.implementation)(version>=1.0.0)(!(version>=2.0.0)))"; effective:=active in start level 20 but no artifact is providing a matching capability in this start level.
[api-regions-exportsimports] com.adobe.aem.temp:org.apache.felix.gogo.jline:1.1.8: Bundle org.apache.felix.gogo.jline:1.1.8 is importing package(s) [org.jline.builtins, org.jline.utils, org.apache.felix.service.command, org.apache.felix.service.threadio, org.jline.terminal, org.jline.reader, org.apache.felix.gogo.runtime, org.jline.reader.impl] in start level 20 but no bundle is exporting these for that start level.
```

The above code sample illustrates the behavior if a bundle does not resolve. In which case, it is "staged" and is only installed if its requirements (missing imports, in this case) are satisfied through the installation of other code. 

#### Deploy config pipeline related configuration (yaml configurations) {#deploy-config-pipeline}

The environment-specific configurations (one or more yaml files) described in the article [Using Config Pipelines](/help/operations/config-pipeline.md) can be deployed as follows:

`aio aem:rde:install -t env-config ./my-config-folder`
Where `my-config-folder` is the parent folder containing your yaml configurations.

Alternatively, it is also possible to install a zip file containing the config folder tree:

`aio aem:rde:install -t env-config config.zip` 

Note that the yaml file's envTypes array includes the value `rde`, as in the example below:

```
kind: "CDN"
version: "1"
metadata:
  envTypes: ["rde"]
```

### Deploy front-end code based on site themes and site templates {#deploying-themes-to-rde}

RDEs support front-end code built with [site themes](/help/sites-cloud/administering/site-creation/site-themes.md) and [site templates](/help/sites-cloud/administering/site-creation/site-templates.md). Instead of using the Cloud Manager [Front-End Pipeline](/help/sites-cloud/administering/site-creation/enable-front-end-pipeline.md) like other environment types, RDEs deploy front-end packages using a command-line directive.

As usual, build your front-end package using npm: 

`npm run build`

It generates a `dist/` folder, so your front-end package folder contains a `package.json` file and `dist` folder:

```
ls ./path-to-frontend-pkg-folder/
...
dist
package.json
```

Now, you are ready to deploy the front-end package to the RDE by pointing to the front-end package folder in the following manner:

```
aio aem:rde:install -t frontend ./path-to-frontend-pkg-folder/
...
#1: deploy completed for frontend frontend-pipeline.zip on author,publish - done by ... at 2024-01-18T15:33:22.898Z
Logs:
> Deployed artifact wknd-1.0.0-1705592008-26e7ec1a
> with workspace hash 692021864642a20d6d298044a927d66c0d9cf2adf42d4cca0c800a378ac3f8d3
```

Alternatively, you can zip the `package.json` file and `dist` folder and deploy that zip file:

`zip -r frontend-pkg.zip ./path-to-frontend-pkg-folder/dist ./path-to-frontend-pkg-folder/package.json`

```
aio aem:rde:install -t frontend frontend-pkg.zip
...
#1: deploy completed for frontend frontend-pipeline.zip on author,publish - done by ... at 2024-01-18T15:33:22.898Z
Logs:
> Deployed artifact wknd-1.0.0-1705592008-26e7ec1a
> with workspace hash 692021864642a20d6d298044a927d66c0d9cf2adf42d4cca0c800a378ac3f8d3
```

>[!NOTE]
>
>The naming of the files in the front-end package must adhere to the following naming conventions:
>
> * `dist` folder, for the npm build output package folder
> * `package.json` file, for the npm dependencies package

>[!TIP]
>
>If you created your RDE before April 2023 and encounter the `UNEXPECTED_API_ERROR` when using the front-end feature for the first time, it may be due to an outdated setup. To resolve this issue, delete the environment and create a new one.














### Check the status of the RDE {#checking-rde-status}

You can use the RDE CLI to check if the environment is ready to be deployed to, as what deployments have been made by way of the RDE plug-in.

Running the following:

`aio aem:rde:status`

Returns with the following:

```
Info for cm-p12345-e987654
Environment: Ready
- Bundles Author:
 com.adobe.granite.sample.demo-1.0.0.SNAPSHOT
- Bundles Publish:
 com.adobe.granite.sample.demo-1.0.0.SNAPSHOT
- Configurations Author:
 com.adobe.granite.demo.MyServlet
- Configurations Publish:
 com.adobe.granite.demo.MyServlet

```

If the command returns a note about instances deploying, you can still go ahead and perform the next update, but your last one might not yet be visible on the instance.

### Show deployment history {#show-deployment-history}

You can check the history of deployments made to the RDE by running:

`aio aem:rde:history`

Which returns a response in the form of:

`#1: deploy completed for content-package aem-guides-wknd.all-2.1.0.zip on author,publish - done by 029039A55D4DE16A0A494025@AdobeID at 2022-09-12T14:41:55.393Z`

### Deleting from RDE {#deleting-from-rde}

You can use the CLI tooling to delete configurations and bundles that you previously deployed to the RDE. Use the `status` command for a list of what can be deleted, which includes the `bsn` for bundles and `pid` for configurations to reference in the delete command.

For example, if `com.adobe.granite.demo.MyServlet.cfg.json` has been installed, the `bsn` is just `com.adobe.granite.demo.MyServlet`, without the **cfg.json** suffix.

Deletion of content packages or content files is not supported. To remove them, reset the RDE, which returns it to a default state.

See the example below for more details:

```
aio aem:rde:delete com.adobe.granite.csrf.impl.CSRFFilter
#13: delete completed for osgi-config com.adobe.granite.csrf.impl.CSRFFilter on author - done by karl at 2022-09-12T22:01:01.955Z
#14: delete completed for osgi-config com.adobe.granite.csrf.impl.CSRFFilter on publish - done by karl at 2022-09-12T22:01:12.979Z
```

For more information and demonstration, see the video tutorial [how to use RDE commands (10:01)](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/developing/rde/how-to-use).

## Logs {#rde-logging}

Similar to other environment types, log levels can be set by modifying OSGi configurations, although as described above, the deployment model for RDEs involves a command line rather than a Cloud Manager deployment. Check the [logging documentation](/help/implementing/developing/introduction/logging.md) for more information about how to view, download, and interpret logs.

The RDE CLI also has its own log command that is used to configure quickly which classes and packages are logged, and at what log level. These configurations can be viewed as ephemeral, as they do not modify the OSGI properties in version control. This feature is focused on tailing logs in real time, rather than looking up logs from the distant past. 

The following example illustrates how to tail the author tier, with one package set to a debug log level, and two packages (separated by spaces) set to an info debug level. Output that includes an **auth** package is highlighted.

`aio aem:rde:logs --target=author --debug=org.apache.sling --info=org.apache.sling.commons.threads.impl org.apache.sling.jcr.resource.internal.helper.jcr -H .auth.`

>[!TIP]
>
>If you see the error `RDECLI:UNEXPECTED_API_ERROR` when playing with the logs commands for the author service, please reset your environment and try again. This error is thrown if your latest reset operation was before the end of May 2024.
>
>```
>aio aem:rde:reset
>```

See `aio aem:rde:logs --help` for the full set of command line options.

Features include the following:

* declaring log levels on a per package or class level 
* customizing the log output format
* tailing up to four current log configurations, each in its own terminal
* highlighting specific logs

Note that logs are stored in memory on the RDE and these logs are recycled and thus discarded if not tailed or if the network is too slow.


## Reset the RDE {#reset-rde}

Resetting the RDE removes all custom code, configurations, and content from both the author and publish instances. Resetting the RDE is helpful when you have finished testing one feature and want to return the environment to a default state before testing another.

A reset sets the RDE to the most recently available AEM version.

You can reset the RDE using either [Cloud Manager](#reset-the-rde-cloud-manager) or the [command line](#reset-the-rde-command-line). Resetting takes a few minutes and all existing content and code is deleted from the RDE.

>[!NOTE]
>
>Make sure you are assigned the Cloud Manager Developer role before using the reset feature. Otherwise, the reset action fails with an error.

### Reset the RDE using the command line {#reset-the-rde-command-line}

You can reset the RDE and return it to a default state by running the following:

`aio aem:rde:reset`

This process usually takes a few minutes and reports ```Environment reset.``` when successful or ```Failed to reset the environment.``` on errors. For a structured output, see the chapter about ```--json``` output below.

Use the [status command](#checking-rde-status) to check when the environment is ready again.

### Reset the RDE in Cloud Manager {#reset-the-rde-cloud-manager}

You can use Cloud Manager to reset your RDE by following the below steps:

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Click the program for which you want to reset the RDE.

1. From the **Overview** page, click the **Environments** tab at the top of the screen.

   ![Environments tab](/help/implementing/cloud-manager/assets/environments-tab2.png)

   * Alternatively, click the **Show All** button on the **Environments** card to jump directly to the **Environments** tab.

     ![Show all option](/help/implementing/cloud-manager/assets/environment-showall.png)

1. The **Environments** window opens and lists all environments for the program.

   ![The environments tab](/help/implementing/cloud-manager/assets/environments-tab-populated.png)

1. Click the ellipsis button of the RDE that you want to reset, and then select **Reset**.

   ![View environment details](/help/implementing/cloud-manager/assets/rde-reset.png)

1. Confirm that you want to reset the RDE by clicking **Reset** in the dialog.

   ![Confirm reset](/help/implementing/cloud-manager/assets/rde-reset-confirm.png)

1. Cloud Manager confirms by way of a banner notification that the reset process started.

   ![Reset banner notification](/help/implementing/cloud-manager/assets/rde-reset-banner.png)

After the RDE reset starts, it usually takes a few minutes to complete and restore the environment to its default state. You can view the reset status anytime in the **Status** column of the **Environments** card or window.

![RDE reset status](/help/implementing/cloud-manager/assets/rde-reset-status-environments-card.png)

You can also reset the RDE using the ellipsis button directly from the **Environments** card on the **Overview** page.

![Reset RDE from Environments card](/help/implementing/cloud-manager/assets/rde-reset-environments-card.png)

For more information about how to use Cloud Manager to manage your environments, see [the Cloud Manager documentation](/help/implementing/cloud-manager/manage-environments.md).

## Commands that support JSON output {#json-commands}

Most commands support the global ```--json``` flag which suppresses console output and returns valid json to be processed in scripts. Below are some supported commands, with examples of the json output.

### Status {#status}

<details>
  <summary>Expand to see Status examples</summary>

#### A clean RDE {#clean-rde}

```$ aio aem rde status --json```

```json
{
  "programId": "myProgram",
  "environmentId": "myEnv",
  "status": "Modification in progress | Deployment in progress | Upload in progress | Ready (instances are currently deploying) | Ready",
  "author": {
    "osgiBundles": [],
    "osgiConfigs": []
  },
  "publish": {
    "osgiBundles": [],
    "osgiConfigs": []
  }
}
```

#### An RDE with some installed bundles {#rde-installed-bundles}

```$ aio aem rde status --json```

```json
{
  "programId": "myProgram",
  "environmentId": "myEnv",
  "status": "Ready",
  "author": {
    "osgiBundles": [
      {
        "id": "author_osgi-bundle_com.adobe.granite.hotdev.demo",
        "updateId": "80",
        "service": "author",
        "type": "osgi-bundle",
        "metadata": {
          "name": "hotdev.demo.ui.apps.all-1.0.0-SNAPSHOT.zip",
          "bundleSymbolicName": "com.adobe.granite.hotdev.demo",
          "bundleName": "HotDev Bundle",
          "bundleVersion": "1.0.0.SNAPSHOT"
        }
      }
    ],
    "osgiConfigs": [
      {
        "id": "publish_osgi-config_com.adobe.granite.demo.MyServlet",
        "updateId": "80",
        "service": "publish",
        "type": "osgi-config",
        "metadata": {
          "name": "hotdev.demo.ui.apps.all-1.0.0-SNAPSHOT.zip",
          "configPid": "com.adobe.granite.demo.MyServlet"
        }
      }
    ]
  },
  "publish": {
    "osgiBundles": [
      {
        "id": "author_osgi-bundle_com.adobe.granite.hotdev.demo",
        "updateId": "80",
        "service": "author",
        "type": "osgi-bundle",
        "metadata": {
          "name": "hotdev.demo.ui.apps.all-1.0.0-SNAPSHOT.zip",
          "bundleSymbolicName": "com.adobe.granite.hotdev.demo",
          "bundleName": "HotDev Bundle",
          "bundleVersion": "1.0.0.SNAPSHOT"
        }
      }
    ],
    "osgiConfigs": [
      {
        "id": "publish_osgi-config_com.adobe.granite.demo.MyServlet",
        "updateId": "80",
        "service": "publish",
        "type": "osgi-config",
        "metadata": {
          "name": "hotdev.demo.ui.apps.all-1.0.0-SNAPSHOT.zip",
          "configPid": "com.adobe.granite.demo.MyServlet"
        }
      }
    ]
  }
}
```

</details>

### Install {#install}

<details>
  <summary>Expand to see Install examples</summary>

```$ aio aem rde install ~/Downloads/hotdev.demo.ui.apps.all-1.0.0-SNAPSHOT.zip --json```

```json
{
  "programId": "myProgram",
  "environmentId": "myEnv",
  "items": [
    {
      "updateId": "4",
      "info": "deploy",
      "action": "deploy",
      "metadata": {
        "name": "hotdev.demo.ui.apps.all-1.0.0-SNAPSHOT.zip"
      },
      "services": [
        "author",
        "publish"
      ],
      "status": "completed",
      "timestamps": {
        "received": "2024-05-21T12:30:44.578Z",
        "processed": "2024-05-21T12:31:07.886468Z"
      },
      "user": "userId",
      "type": "content-package",
      "hash": "2ad73507",
      "logs": [
        "No logs available for this update."
      ]
    }
  ]
}
```

</details>

### Delete {#delete}

<details>
  <summary>Expand to see Delete examples</summary>

```$ aio aem rde delete com.adobe.granite.hotdev.demo-1.0.0.SNAPSHOT --json```

```json
{
  "programId": "myProgram",
  "environmentId": "myEnv",
  "items": [
    {
      "updateId": "84",
      "info": "delete author_osgi-bundle_com.adobe.granite.hotdev.demo",
      "action": "delete",
      "metadata": {},
      "services": [
        "author"
      ],
      "status": "completed",
      "timestamps": {
        "received": "2024-05-21T11:49:16.889Z",
        "processed": "2024-05-21T11:49:18.188420Z"
      },
      "user": "userId",
      "type": "osgi-bundle",
      "deletedArtifact": {
        "id": "author_osgi-bundle_com.adobe.granite.hotdev.demo",
        "metadata": {
          "name": "hotdev.demo.ui.apps.all-1.0.0-SNAPSHOT.zip",
          "bundleSymbolicName": "com.adobe.granite.hotdev.demo",
          "bundleName": "HotDev Bundle",
          "bundleVersion": "1.0.0.SNAPSHOT"
        },
        "service": "author",
        "type": "osgi-bundle",
        "updateId": "83"
      },
      "hash": "636f6d2e",
      "logs": [
        "No logs available for this update."
      ]
    },
    {
      "updateId": "85",
      "info": "delete publish_osgi-bundle_com.adobe.granite.hotdev.demo",
      "action": "delete",
      "metadata": {},
      "services": [
        "publish"
      ],
      "status": "completed",
      "timestamps": {
        "received": "2024-05-21T11:49:23.857Z",
        "processed": "2024-05-21T11:49:25.237930Z"
      },
      "user": "userId",
      "type": "osgi-bundle",
      "deletedArtifact": {
        "id": "publish_osgi-bundle_com.adobe.granite.hotdev.demo",
        "metadata": {
          "name": "hotdev.demo.ui.apps.all-1.0.0-SNAPSHOT.zip",
          "bundleSymbolicName": "com.adobe.granite.hotdev.demo",
          "bundleName": "HotDev Bundle",
          "bundleVersion": "1.0.0.SNAPSHOT"
        },
        "service": "publish",
        "type": "osgi-bundle",
        "updateId": "83"
      },
      "hash": "636f6d2e",
      "logs": [
        "No logs available for this update."
      ]
    }
  ]
}
```

</details>

### History {#history}

<details>
  <summary>Expand to see History examples</summary>

```$ aio aem rde history --json```

```json
{
  "programId": "myProgram",
  "environmentId": "myEnv",
  "status": "Ready",
  "items": [
    {
      "updateId": "112",
      "info": "delete publish_osgi-bundle_com.adobe.granite.hotdev.demo",
      "action": "delete",
      "metadata": {},
      "services": [
        "publish"
      ],
      "status": "completed",
      "timestamps": {
        "received": "2024-05-21T12:53:07.934Z",
        "processed": "2024-05-21T12:53:09.118766Z"
      },
      "user": "userId",
      "type": "osgi-bundle",
      "deletedArtifact": {
        "id": "publish_osgi-bundle_com.adobe.granite.hotdev.demo",
        "metadata": {
          "name": "hotdev.demo.ui.apps.all-1.0.0-SNAPSHOT.zip",
          "bundleSymbolicName": "com.adobe.granite.hotdev.demo",
          "bundleName": "HotDev Bundle",
          "bundleVersion": "1.0.0.SNAPSHOT"
        },
        "service": "publish",
        "type": "osgi-bundle",
        "updateId": "110"
      },
      "hash": "636f6d2e"
    },
    {
      "updateId": "111",
      "info": "delete author_osgi-bundle_com.adobe.granite.hotdev.demo",
      "action": "delete",
      "metadata": {},
      "services": [
        "author"
      ],
      "status": "completed",
      "timestamps": {
        "received": "2024-05-21T12:53:00.824Z",
        "processed": "2024-05-21T12:53:02.101560Z"
      },
      "user": "userId",
      "type": "osgi-bundle",
      "deletedArtifact": {
        "id": "author_osgi-bundle_com.adobe.granite.hotdev.demo",
        "metadata": {
          "name": "hotdev.demo.ui.apps.all-1.0.0-SNAPSHOT.zip",
          "bundleSymbolicName": "com.adobe.granite.hotdev.demo",
          "bundleName": "HotDev Bundle",
          "bundleVersion": "1.0.0.SNAPSHOT"
        },
        "service": "author",
        "type": "osgi-bundle",
        "updateId": "110"
      },
      "hash": "636f6d2e"
    },
    {
      "updateId": "110",
      "info": "deploy",
      "action": "deploy",
      "metadata": {
        "name": "hotdev.demo.ui.apps.all-1.0.0-SNAPSHOT.zip"
      },
      "services": [
        "author",
        "publish"
      ],
      "status": "completed",
      "timestamps": {
        "received": "2024-05-21T12:52:12.123Z",
        "processed": "2024-05-21T12:52:31.026147Z"
      },
      "user": "userId",
      "type": "content-package",
      "hash": "2ad73507"
    }
  ]
}
```

</details>

### Reset {#reset}

<details>
  <summary>Expand to see Reset examples</summary>

#### Fire and forget, no-wait {#fire-no-wait}

```$ aio aem rde reset --no-wait --json```

```json
{
  "programId": "myProgram",
  "environmentId": "myEnv",
  "status": "resetting"
}
```

#### Wait for completion, reset successfully {#wait-success}

```$ aio aem rde reset --json```

```json
{
  "programId": "myProgram",
  "environmentId": "myEnv",
  "status": "reset"
}
```
  
#### Wait for completion, reset failed {#wait-failed}

```$ aio aem rde reset --json```

```json
{
  "programId": "myProgram",
  "environmentId": "myEnv",
  "status": "reset_failed"
}
```

</details>

### Restart {#restart}

<details>
  <summary>Expand to see restart examples</summary>

```$ aio aem rde restart --json```

```json
{
  "programId": "myProgram",
  "environmentId": "myEnv",
  "status": "restarted"
}
```

</details>

## Run modes {#runmodes}

RDE-specific OSGI configuration can be applied by using suffixes on the folder name, like in the examples below:

* `config.rde`
* `config.author.rde`
* `config.publish.rde`

See the [run mode documentation](/help/implementing/deploying/overview.md#runmodes) for general information about run modes.

>[!NOTE]
>
>RDE OSGI configuration is unique in that it inherits the values of any OSGI properties declared by the bundle's `dev` run mode.

RDEs are distinct from other environments in that content can be installed in an `install.rde` folder (or `install.author.rde` or `install.publish.rde`) under `/apps`. This ability lets you commit content to Git and deliver it to the RDE using the command-line tooling.

## Populate with content {#populating-content}

When an RDE is reset, all content is removed and so if desired, explicit action must be taken to add content. As a best practice, consider assembling a set of content to be used as test content for validating or debugging features in the RDE. There are several possible strategies for populating the RDE with that content:

1. Sync the content package explicitly to the RDE using the command-line tooling

1. Place and commit the sample content in git inside an `install.rde` folder under `/apps` and then sync the overarching content package to the RDE using the command-line tooling.

1. Use the [content copy tool](/help/implementing/developing/tools/content-copy.md) to copy a defined content set from prod, stage, or dev environments, or from another RDE.

1. Use Package Manager

You are limited to 1 GB when syncing content packages.


## How are RDEs different from cloud development environments? {#how-are-rds-different-from-cloud-development-environments}

While the RDE is in many ways similar to a Cloud Development environment, there are some minor architectural differences to allow for quick syncing of code. The mechanism for getting code to RDE is different -- for RDEs, one syncs code from a local development environment, while for Cloud Development environments, one deploys code by way of Cloud Manager.

For these reasons, it is recommended that after validating code on an RDE environment, you deploy the code to a Cloud Development environment using the non-production pipeline. Finally, test the code before deploying with the production pipeline.

Also note the following considerations: 

* RDEs do not include a preview tier
* RDEs do not currently support the prerelease channel.


## How many RDEs do I need? {#how-many-rds-do-i-need}

An RDE is available for each licensed solution and Adobe also offers additional RDEs, which can be licensed for Production (non-sandbox) programs.

The number of RDEs needed depends on the make-up and processes of an organization. The most flexible model is where an organization purchases a dedicated RDE for each one of their AEM Cloud Service developers. In this model, each developer can test their code on the RDE without coordinating with other team members on whether an RDE environment is available.

At the other extreme, a team with only one RDE may rely on internal coordination to decide which developer uses the environment at a given time. This approach works well when a developer reaches a feature milestone and needs to validate their work in a Cloud environment with the flexibility to make quick changes.

An in-between model is one where an organization purchases several RDEs so there is a greater likelihood of an unused RDE being available. One strategy could be to allocate an RDE per scrum team or major feature. Internal processes may be used to coordinate usage of the environments.

## How a AEM Forms Cloud Service RDE is different from other environments? {#how-are-forms-rds-different-from-cloud-development-environments}

Forms developers can use AEM Forms Cloud Service Rapid Development Environment to develop quickly Adaptive Forms, Workflows, and customizations like customizing core components, integrations with third-party systems, and more. The AEM Forms Cloud Service Rapid Development Environment (RDE) has no support for Communication APIs. It also has not support for features and capabilities that require Document of Record, like generating a Document of Record on submission of an Adaptive Form. The below listed AEM Forms features are not available on a Rapid Development Environment (RDE):
 
* Configuring a Document of Record for an Adaptive Form
* Generating a Document of Record on submission of an Adaptive Form or with a Workflow step
* Send Document of Record as an attachment with Email Submit action or with Email step in a Workflow
* Using Adobe Sign in an Adaptive Form or in a Workflow step
* Communication APIs

>[!NOTE]
>
> There is no difference between the UI of Rapid Development Environment (RDE) and other Cloud Service environments for Forms. All Document of Record related options, like selecting a document of record template for an Adaptive Form, continues to appear in the UI. These environments have no Communication APIs and Document of Record capabilities to test such options. So, if you choose an option that requires Communication APIs or Document of Record capabilities, the system does not perform the action. Instead, it displays an error message.

## RDE tutorial

To learn about RDE in AEM as a Cloud Service, see the video tutorial that demonstrates [how to set it up, how to use it, and the development life cycle (01:25)](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/developing/rde/overview).

## Troubleshoot {#troubleshooting}

### Troubleshoot RDE (#rde-troublehooting)

#### How to obtain the latest AEM version for an existing RDE {#get-latest-aem-version}

Upon creation, RDEs are set to the most recently available Adobe Experience Manager (AEM) version. An [RDE reset](#reset-rde), which can be performed using Cloud Manager or the `aio aem:rde:reset` command, cycles the RDE and set it to the most recently available AEM version.

### Troubleshoot aio RDE plugin {#aio-rde-plugin-troubleshooting}

#### Errors regarding insufficient permissions {#insufficient-permissions}

To use the RDE plugin, it requires you to be a member of the Cloud Manager **Developer - Cloud Service** Product Profile. See [Assign Team Members to Cloud Manager Product Profiles - Assign the Developer Product Profile](/help/journey-onboarding/assign-profiles-cloud-manager.md#assign-developer) for more details.

Alternatively, you can confirm that you have this developer role if you log in to the developer console by running the following command:

   `aio cloudmanager:environment:open-developer-console`

   >[!TIP]
   >
   >If you see the `Warning: cloudmanager:* is not a aio command.` error, you must install the [aio-cli-plugin-cloudmanager](https://github.com/adobe/aio-cli-plugin-cloudmanager) by running the following command:
   >
   >```
   >aio plugins:install @adobe/aio-cli-plugin-cloudmanager
   >```

Verify that the login was completed successfully by running the following:

`aio cloudmanager:list-programs`

This process lists all programs under your configured organization and confirms that you have the correct role assigned.

#### Use deprecated context `aio-cli-plugin-cloudmanager` {#aio-rde-plugin-troubleshooting-deprecatedcontext}

Due to the history of the `aio-cli-plugin-aem-rde`, the context name `aio-cli-plugin-cloudmanager` was used for some time. The RDE plugin now uses the IMS method for managing context information, allowing you to store context either globally or locally. You can also configure a default context to apply to all AIO calls automatically. The default context configured is stored locally and enables the developers to track and use individual contexts and their information inside a folder. For further details, read [the example to set up a local context](/help/implementing/developing/introduction/rapid-development-environments.md#installing-the-rde-command-line-tools) above.

Developers who use both plugins, the `aio-cli-plugin-cloudmanager` and the `aio-cli-plugin-aem-rde` and would like to keep all information in the same context have to options right now:

##### Keep using context `aio-cli-plugin-cloudmanager`

The context can still be used. A deprecation warning is shown in the RDE plugin. This warning can be omitted by using the ```--quiet``` mode. More recent versions of the RDE plugin do not offer the fallback to read the context `aio-cli-plugin-cloudmanager` any longer. To continue to use it, simply configure the default context to `aio-cli-plugin-cloudmanager`. See [the example to set up a local context](/help/implementing/developing/introduction/rapid-development-environments.md#installing-the-rde-command-line-tools) above.

##### Use any other context name also for the Cloud Manager plug-in

The Cloud Manager plug-ins offer a parameter to define a context to be used. It does not support the IMS default context configuration just yet. To do so, configure the RDE plugin using [the example to set up a local context](/help/implementing/developing/introduction/rapid-development-environments.md#installing-the-rde-command-line-tools) and tell the Cloud Manager plugin to use `myContext` like ```--imsContextName=myContext``` in every call to it.
