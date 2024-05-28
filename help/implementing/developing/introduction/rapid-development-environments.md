---
title: Rapid Development Environments
description: Learn how to use Rapid Development Environments for rapid development iterations on a cloud environment.
exl-id: 1e9824f2-d28a-46de-b7b3-9fe2789d9c68
---
# Rapid Development Environments {#rapid-development-environments}

To deploy changes, current Cloud Development environments require the use of a process that employs extensive code security and quality rules called a CI/CD pipeline. For situations where quick and iterative changes are needed, Adobe has introduced Rapid Development Environments (RDEs for short).

RDEs allow developers to swiftly deploy and review changes, minimizing the amount of time needed to test features that are proven to work on a local development environment.

Once the changes have been tested in an RDE, they can be deployed to a regular Cloud Development environment through the Cloud Manager pipeline.

>[!VIDEO](https://video.tv.adobe.com/v/3415582/?quality=12&learn=on)


You can see additional videos demonstrating [how to set it up](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/developing/rde/how-to-setup.html), [how to use it](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/developing/rde/how-to-use.html), and the [development life cycle](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/developing/rde/development-life-cycle.html) using RDE.

## Introduction {#introduction}

RDEs can be used for code, content, and Apache or Dispatcher configurations. Unlike regular Cloud Development environments, developers can use local command-line tools to sync code built locally to an RDE.

Every program is provisioned with an RDE. If there are Sandbox accounts, they are hibernated after a few hours of non-use.

Upon creation, RDEs are set to the most recently available Adobe Experience Manager (AEM) version. An RDE reset, which can be performed using Cloud Manager, cycles the RDE and set it to the most recently available AEM version.

Typically, an RDE would be used by a single developer at a given time, for testing and debugging a specific feature. When the development session is done, the RDE can be reset into a default state for the next usage.

Additional RDEs may be licensed for Production (non-sandbox) programs.

## Enabling RDE in a Program {#enabling-rde-in-a-program}

Follow these steps so you can use Cloud Manager to create an RDE for your program.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Click the program to which you want to add an RDE to show its details.

   * RDEs can be added to both [sandbox programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-sandbox-programs.md) and [production programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/introduction-production-programs.md).

1. From the **Program Overview** page, click **Add Environment** on the **Environments** card to add an environment.

   ![Environments card](/help/implementing/cloud-manager/assets/no-environments.png)

   * The **Add Environment** option is also available on the **Environments** tab.

     ![Environments tab](/help/implementing/cloud-manager/assets/environments-tab.png)

   * The **Add Environment** option may be disabled due to lack of permissions or depending on the licensed resources.

1. In the **Add environment** dialog that appears:

   * Select **Rapid Development** under the **Select environment type** heading.
     * The number of available/used environments is displayed in parentheses behind the environment type.
   * Provide a **Name** for the environment.
   * Provide an optional **Description** for the environment.
   * Select a **Cloud Region**.

   ![Add environment dialog](/help/implementing/cloud-manager/assets/add-environment-wizard.png)

1. Click **Save** to add the specified environment.

The **Overview** screen now displays your new environment in the **Environments** card.

Upon creation, RDEs are set to the most recently available AEM version. An RDE reset, which can also be performed using Cloud Manager, cycles the RDE and set it to the most recently available AEM version.

For more information about using Cloud Manager to create environments, manage who has access to them, and assign custom domains, see [the Cloud Manager documentation](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/program-types.md).

## Installing the RDE Command-Line Tools {#installing-the-rde-command-line-tools}

After you have added an RDE for your program using Cloud Manager, you can interact with it by setting up the command-line tools as described in the following steps:

>[!IMPORTANT]
>
>Make sure you have the latest version of [Node and NPM installed](https://nodejs.org/en/download/) for Adobe I/O CLI and related plugins to work properly.


1. Install the Adobe I/O CLI tools according by following the procedure [here](https://developer.adobe.com/runtime/docs/guides/tools/cli_install/).
1. Install the Adobe I/O CLI tools cloud manager plugin, and configure them as described [here](https://github.com/adobe/aio-cli-plugin-cloudmanager).
1. Install the Adobe I/O CLI tools AEM RDE plugin by running these commands:

   ```
   aio plugins:install @adobe/aio-cli-plugin-aem-rde
   aio plugins:update
   ```

1. Configure the cloud manager plugin for your organization ID:

   `aio config:set cloudmanager_orgid 4E03EQC05D34GL1A0B49421C@AdobeOrg`

   and replace the alphanumeric string with your own organization ID, which can be looked up using the strategy [here](https://experienceleague.adobe.com/docs/core-services/interface/administration/organizations.html#concept_EA8AEE5B02CF46ACBDAD6A8508646255).

1. Next, configure your program id:

   `aio config:set cloudmanager_programid 12345`

1. Then, configure the environment id the RDE is going to be attached to:

   `aio config:set cloudmanager_environmentid 123456`

1. After you are done configuring the plugin, login by performing

   `aio login`

   The response on a successful login should resemble the output below, but you can ignore the values that are displayed.

   ```
   ...
   You are currently in:
   1. Org: <no org selected>
   2. Project: <no project selected>
   3. Workspace: <no workspace selected>

   ```
   
   This step requires you to be a member of the Cloud Manager **Developer - Cloud Service** Product Profile. See [this page](/help/journey-onboarding/assign-profiles-cloud-manager.md#assign-developer) for more details.

   Alternatively, you can confirm that you have this developer role if you can log in to the developer console by running this command:

   `aio cloudmanager:environment:open-developer-console`

   >[!TIP]
   >
   >If you see the `Warning: cloudmanager:list-programs is not a aio command.` error, you must install the [aio-cli-plugin-cloudmanager](https://github.com/adobe/aio-cli-plugin-cloudmanager) by running the command below:
   >
   >```
   >aio plugins:install @adobe/aio-cli-plugin-cloudmanager
   >```

1. Verify that the login was completed successfully by running

   `aio cloudmanager:list-programs`

   This should list all programs under your configured organization.

   
For more information and demonstration, watch the video tutorial [how to set up an RDE (06:24)](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/developing/rde/how-to-setup.html).

## Installing the RDE Command-Line Tools (end of June) {#installing-the-rde-command-line-tools-june}

After you have added an RDE for your program using Cloud Manager, you can interact with it by setting up the command-line tools as described in the following steps:

>[!IMPORTANT]
>
>Make sure you have the latest version of [Node and NPM installed](https://nodejs.org/en/download/) for Adobe I/O CLI and related plugins to work properly.


1. Install the Adobe I/O CLI tools according to this [procedure](https://developer.adobe.com/runtime/docs/guides/tools/cli_install/).
1. Install the Adobe I/O CLI tools AEM RDE plugin:

   ```
   aio plugins:install @adobe/aio-cli-plugin-aem-rde
   aio plugins:update
   ```

1. Configure the RDE plugin to use your organization, program and environment. Below setup command will interactively provide the user with a list of programs in their origanization, and show RDE environments in that program to choose from.
   ```
   aio login
   aio aem:rde:setup
   ```
   
   The setup step can be skipped while always passing the arguments for organization, program and environment to each command, i.e. in a scripted environment. [See rde commands below for more information](#rde-cli-commands).
   
### The Interactive Setup (end of June)

  The setup command will ask if the provided configuration shall be stored locally or globally.
   
   ```
   Setup the CLI configuration necessary to use the RDE commands.
   ? Do you want to store the information you enter in this setup procedure locally? (y/N)
   ```
   
   Choose `no` to 
   * store the organization, program and environment globally in your aio configuration.
   * work with a single RDE only.
   
   Choose `yes` to
   * store the organization, program and environment locally in the current directory, in a `.aio` file. This is convenient if you want to commit the file to version control so others cloning the git repository can use it.
   * work with many RDEs, so that switching the to another directory will use that configuration instead.
   * use the configuration in a programmatic context like a script, which can reference it.


   Once local or global configuration is selected, the setup command will try to read your oriagnization ID from your current login and then read the programs of your organization. In case the organization cannot be found, you can enter it manually along with some guidance.
   
  ```
   Selected only organization: XYXYXYXYXYXYXYXXYY
   retrieving programs of your organization ...
   ```
   
   Once the programs are retrieved, the user can select from the list and also type to filter.
   When the program was selected, a list of RDE environments is provided to choose from.
   In case there is only one program and/or RDEenvironment available, it is selected automatically.
   
   Use ```aio aem rde setup --show``` to show the ```Current configuration: cm-p1-e1: programName - environmentName (organization: ...@AdobeOrg)``` information.

## Using RDE while Developing a New Feature {#using-rde-while-developing-a-new-feature}

Adobe recommends the following workflow for developing a new feature:

* When an intermediate milestone is reached and successfully validated locally with the AEM as a Cloud Service SDK, commit the code to a git feature branch. The branch should not be part of the main line yet, although committing to git is optional. What constitutes an "intermediate milestone" varies based on team habits. Examples include a few new lines of code, half a day of work, or completing a subfeature.

* Reset the RDE if it has been used by another feature and you want to [reset it to a default state](#reset-rde). <!-- Alexandru: hiding for now, do not delete This can be done by way of [Cloud Manager](#reset-the-rde-cloud-manager) or by way of the [command line](#reset-the-rde-command-line). -->Reset takes a few minutes and all existing content and code is deleted. You can use the RDE status command to confirm the RDE is ready. The RDE comes back up with the most recent AEM release version.  
  
  >[!IMPORTANT]
  >
  > If your staging and production environments are not receiving automatic AEM release updates and are behind the most recent AEM release version, the code running on the RDE may not match how the code functions on staging and production. In that case, it is especially important to perform thorough testing of the code on staging before deploying it to production.


* Using the RDE command-line interface, sync local code to the RDE. Options include installing a content package, a specific bundle, an OSGI configuration file, a content file, and a zip file of an Apache/Dispatcher configuration. Referencing a remote content package is also possible. See [RDE Command-Line Tools](/help/implementing/developing/introduction/rapid-development-environments.md#rde-cli-commands) for more information. You can use the status command to validate that the deployment was successful. Optionally, use Package Manager to install content packages.

* Test the code in the RDE. Author and Publish URLs are available in Cloud Manager.

* If the code does not behave as expected, use standard debugging techniques to understand the problem and make the appropriate changes. Without committing the code modifications to git (since they haven't been validated), use the local CLI to sync the code to the RDE. Keep iterating until the issue is resolved.

* Once the code behaves as expected, commit the code to the git feature branch.

* Code synced to RDE does not use a Cloud Manager pipeline so now you should use a Cloud Manager non-production pipeline to deploy the git feature branch to the Cloud Development environment. This validates that the code passes the Cloud Manager quality gates and lets you be confident the code is later successfully deployed using the Cloud Manager production pipeline.  

* Repeat the steps above for each intermediate milestone until all code for the feature is ready, and runs well on both the RDE and the Cloud Development environment.

* Deploy the code to production by way of the Cloud Manager production pipeline. 

## Using RDE to Debug an Existing Feature {#use-rde-to-debug-an-existing-feature}

The workflow is similar to developing a new feature. The difference is that the code being synced to RDE would reflect the git label of whatever was pushed to the environment where the issue has been found. In addition, it may be useful to deploy content matching the upstream environment. This can be achieved through exporting and importing of content packages.

## Multiple Developers Collaborating on the Same RDE {#multiple-developers-collaborating-on-the-same-rde}

An RDE supports a single project at a time. Since code is synced from a local development environment to the RDE environment, it is most natural for one developer to be using it on their own at a given time.

However, with careful coordination, it is possible for more than one developer to validate a specific feature or debug a specific issue. The key is that each developer keeps their local projects in sync so code changes made by a particular developer are absorbed by the other developers, otherwise one developer might inadvertently overwrite the other's code. The recommended strategy is for each developer to commit their changes to a shared git branch before syncing to the RDE, so that the other developers pull the changes before making their own changes.

## RDE Command Line Tools Commands {#rde-cli-commands}

### Help/General Information {#help}

* For a list of commands, type:

  `aio aem:rde`

* For detailed help for a command, type:

  `aio aem rde <command> --help`
  
  
### new run modes (end of June)

* For a less verbose output, use the quiet mode:

  `aio aem rde <command> --quiet`
  
  This removes certain user information like spinners, progress bars and tries to avoid user input.
  
* For JSON instead of console log output, type:
  
  `aio aem rde <command> --json`
  
  This returns valid JSON while suppressing any console output. See below for JSON examples.
  
* To avoid configuring the RDE connection information using the setup command, or any aio config creation, type:
  
  `aio aem rde <command> --organizationId=<value> --programId=<value> --environmentId=<value>`
  
  This still needs an ```aio login``` to be performed.

### Deploying to RDE {#deploying-to-rde}

This section describes using the RDE CLI for deploying, installing, or updating bundles, OSGI configurations, content packages, individual content files, and Apache or Dispatcher configurations.

The general usage pattern is `aio aem:rde:install <artifact>`.

You can find some examples below:

<u>Deploying a Content Package</u>

`aio aem:rde:install sample.demo.ui.apps.all-1.0.0-SNAPSHOT.zip`

The response for a successful deployment resembles the following:

```
...
#1: deploy completed for content-package sample.demo.ui.apps.all-1.0.0-SNAPSHOT.zip on author,publish - done by 9E072FC75D54FE1A2B49431C@AdobeID at 2022-09-13T11:32:06.229Z
```

Optionally, you can reference a remote repository:

`aio aem:rde:install -t content-package "https://repo1.maven.org/maven2/com/adobe/aem/guides/aem-guides-wknd.all/2.1.0/aem-guides-wknd.all-2.1.0.zip"`

By default, artifacts are deployed to both author and publish tiers, but the "-s" flag can be used to target a specific tier.

Any AEM package can be deployed, such as packages with code, content, or a [container package](/help/implementing/developing/introduction/aem-project-content-package-structure.md#container-packages) (also called the "all" package).

>[!IMPORTANT]
>
>The Dispatcher configuration for the WKND project is not deployed by way of the above content-package installation. Deploy it separately following the "Deploying an Apache/Dispatcher Configuration" steps.

<u>Deploying an OSGI Configuration</u>

`aio aem:rde:install com.adobe.granite.demo.MyServlet.cfg.json`

Where the response for a successful deployment resembles the following:

```
...
#2: deploy completed for osgi-config com.adobe.granite.demo.MyServlet.cfg.json on author,publish - done by 9E0725C05D54FE1A0B49431C@AdobeID at 2022-09-13T11:54:36.390Z
```

<u>Deploying a Bundle</u>

To deploy a bundle, use:

`aio aem:rde:install ~/.m2/repository/org/apache/felix/org.apache.felix.gogo.jline/1.1.8/org.apache.felix.gogo.jline-1.1.8.jar`

Where the response for a successful deployment resembles the following:

```
...
#3: deploy staged for osgi-bundle org.apache.felix.gogo.jline-1.1.8.jar on author,publish - done by 9E0725C05D53BE1A0B49431C@AdobeID at 2022-09-14T07:54:28.882Z
```

<u>Deploying a Content File</u>

To deploy a content file, use:

`aio aem:rde:install world.txt -p /apps/hello.txt`

Where the response for a successful deployment resembles the following:

```
..
#4: deploy completed for content-file world.txt on author,publish - done by 9E0729C05C54FE1A0B49431C@AdobeID at 2022-09-14T07:49:30.644Z
```

<u>Deploying an Apache/Dispatcher Configuration</u>

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
>RDE supports "Flexible mode" Dispatcher configuration, but not "Legacy mode" Dispatcher configuration. See [Dispatcher documentation](/help/implementing/dispatcher/disp-overview.md#validation-debug) for information about the two modes. You can also consult the documentation on [migrating to Flexible mode](/help/implementing/dispatcher/validation-debug.md#migrating), if you have not done so already.

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

<u>Deploying front-end code bsed on site themes and site templates</u>

>[!NOTE]
>
>This feature is not yet GA, but can be used by early adopters. Please reach out to **aemcs-rde-support@adobe.com** to try it out and provide feedback.

RDEs support front-end code based on [site themes](/help/sites-cloud/administering/site-creation/site-themes.md) and [site templates](/help/sites-cloud/administering/site-creation/site-templates.md). With RDEs, this is done using a command line directive to deploy front-end packages, rather than the Cloud Manager [Front-End Pipeline](/help/sites-cloud/administering/site-creation/enable-front-end-pipeline.md) used for other environment types.

As usual, build your front-end package using npm: 

`npm run build`

It should generate a `dist/` folder, so your front-end package folder should contain a `package.json` file and `dist` folder:

```
ls ./path-to-frontend-pkg-folder/
...
dist
package.json
```
Now you are ready to deploy the front-end package to the RDE by pointing to the front-end package folder:

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
> * "dist" folder, for the npm build output package folder
> * "package.json" file, for the npm dependencies package

### Checking the Status of the RDE {#checking-rde-status}

You can use the RDE CLI to check if the environment is ready to be deployed to, as what deployments have been made by way of the RDE plug-in.

Running:

`aio aem:rde:status`

Returns the following:

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

### Show Deployment History {#show-deployment-history}

You can check the history of deployments made to the RDE by running:

`aio aem:rde:history`

Which returns a response in the form of:

`#1: deploy completed for content-package aem-guides-wknd.all-2.1.0.zip on author,publish - done by 029039A55D4DE16A0A494025@AdobeID at 2022-09-12T14:41:55.393Z`

### Deleting from RDE {#deleting-from-rde}

You can delete configurations and bundles that have previously been deployed to RDE by way of the CLI tooling. Use the `status` command for a list of what can be deleted, which includes the `bsn` for bundles and `pid` for configs to reference in the delete command.

For example, if `com.adobe.granite.demo.MyServlet.cfg.json` has been installed, the `bsn` is just `com.adobe.granite.demo.MyServlet`, without the **cfg.json** suffix.

Deletion of content packages or content files is not supported. To remove them, the RDE should be reset, which returns it to a default state.

See the example below for more details:

```
aio aem:rde:delete com.adobe.granite.csrf.impl.CSRFFilter
#13: delete completed for osgi-config com.adobe.granite.csrf.impl.CSRFFilter on author - done by karl at 2022-09-12T22:01:01.955Z
#14: delete completed for osgi-config com.adobe.granite.csrf.impl.CSRFFilter on publish - done by karl at 2022-09-12T22:01:12.979Z
```

For more information and demonstration, see the video tutorial [how to use RDE commands (10:01)](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/developing/rde/how-to-use.html).

## Logs (end of June){#tail-logs-from-rde}

Using the logs command, the user can tail live logs of an RDE directly in his CLI. Ther can be up to four concurrent log configurations be active on an RDE. Once a fifth log configuration is added, an old one has to be replaced. 

Note: A certain amount of logs are kept in memory on the RDE. The memory is recycled if the logs are not tailed, or if the network is too slow. Log messages could be lost in such rare cases.

A simple usecase would be to tail debug logs for some packages, while highlighting anything that mentiones the auth package: `aio aem:rde:logs -d com.adobe -d com.day -H .auth.`

See `aio aem:rde:logs --help` for details.

## Reset {#reset-rde}

Resetting the RDE removes all custom code, configurations, and content from both the author and publish instances. This reset is useful, for example, if the RDE has been used to test a specific feature and you want to reset it to a default state so you can test a different feature.

A reset sets the RDE to the most recently available AEM version.

<!-- Alexandru: hiding for now, do not delete

Resetting can be done by way of [Cloud Manager](#reset-the-rde-cloud-manager) or by way of the [command line](#reset-the-rde-command-line). Resetting takes a few minutes and all existing content and code is deleted from the RDE.

>[NOTE!]
>
>You must be assigned the Cloud Manager Developer role to use the reset feature. If not, a reset action results in an error.

### Reset the RDE by way of Command Line {#reset-the-rde-command-line}

You can reset the RDE and return it to a default state by running:

`aio aem:rde:reset`

This usually takes a few minutes. Use the [status command](#checking-rde-status) to check when the environment is ready again.

### Reset the RDE in Cloud Manager {#reset-the-rde-cloud-manager} -->

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

Once the RDE reset process is started, it usually takes a few minutes to complete and return the environment to its default state. The status of the reset process can be viewed at any time in the **Status** column of the **Environments** card or in the **Environments** window.

![RDE reset status](/help/implementing/cloud-manager/assets/rde-reset-status-environments-card.png)

You can also reset the RDE using the ellipsis button directly from the **Environments** card on the **Overview** page.

![Reset RDE from Environments card](/help/implementing/cloud-manager/assets/rde-reset-environments-card.png)

For more information about how to use Cloud Manager to manage your environments, see [the Cloud Manager documentation](/help/implementing/cloud-manager/manage-environments.md).

## Commands that support JSON output (end of June)

Most commands support the global ```--json``` flag. This suppresses any console output and returns valid json to be processed in scripts.

### Status

#### Clean RDE

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

#### Some installed bundles (example)

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

### Install

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

### Delete

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

### History (empty)

```$ aio aem rde history --json```
```json
{
  "programId": "myProgram",
  "environmentId": "myEnv",
  "status": "Ready"
}
```

### History

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

### Reset

#### fire and forget, no-wait

```$ aio aem rde reset --no-wait --json```
```json
{
  "programId": "myProgram",
  "environmentId": "myEnv",
  "status": "resetting"
}
```

#### wait for completion

```$ aio aem rde reset --json```
```json
{
  "programId": "myProgram",
  "environmentId": "myEnv",
  "status": "reset"
}
```

### Restart

```$ aio aem rde restart --json```
```json
{
  "programId": "myProgram",
  "environmentId": "myEnv",
  "status": "restarted"
}
```

## Run Modes {#runmodes}

RDE-specific OSGI configuration can be applied by using suffixes on the folder name, like in the examples below:

* `config.rde`
* `config.author.rde`
* `config.publish.rde`

See the [run mode documentation](/help/implementing/deploying/overview.md#runmodes) for general information about run modes.

>[!NOTE]
>
>RDE OSGI configuration is unique in that it inherits the values of any OSGI properties declared by the bundle's `dev` run mode.

RDEs are distinct from other environments in that content can be installed in an install.rde folder (or install.author.rde or install.publish.rde) under /apps. This lets you commit content to git and deliver it to the RDE using the command-line tooling.

## Populating with Content {#populating-content}

When an RDE is reset, all content is removed and so if desired, explicit action must be taken to add content. As a best practice, consider assembling a set of content to be used as test content for validating or debugging features in the RDE. There are several possible strategies for populating the RDE with that content:

1. Sync the content package explicitly to the RDE using the command-line tooling

1. Place and commit the sample content in git inside an install.rde folder under /apps and then sync the overarching content package to the RDE using the command-line tooling.

1. Use the [content copy tool](/help/implementing/developing/tools/content-copy.md) to copy a defined content set from prod, stage, or dev environments, or from another RDE.

1. Use Package Manager

You are limited to 1 GB when syncing content packages.

## Logging {#logging}

Log levels can be set by modifying OSGi configurations. Check the [documentation](/help/implementing/developing/introduction/logging.md) for more information.

## How are RDEs Different from Cloud Development Environments? {#how-are-rds-different-from-cloud-development-environments}

While the RDE is in many ways similar to a Cloud Development Environment, there are some minor architectural differences to allow for quick syncing of code. The mechanism for getting code to RDE is different -- for RDEs, one syncs code from a local development environment, while for Cloud Development Environments, one deploys code by way of Cloud Manager.

For these reasons, it is recommended that after validating code on an RDE environment, you should deploy the code to a Cloud Development Environment using the non-production pipeline. Finally, test the code before deploying with the production pipeline.

Also note the following considerations: 

* RDEs do not include a preview tier
* RDEs do not currently support the prerelease channel.
* While RDE support for viewing and debugging front-end code based on [site themes](/help/sites-cloud/administering/site-creation/site-themes.md) and [site templates](/help/sites-cloud/administering/site-creation/site-templates.md) deployed is not yet GA-ready, it can be used by early adopters. Please reach out to **aemcs-rde-support@adobe.com** to try it out and provide feedback.



## How many RDEs do I need? {#how-many-rds-do-i-need}

An RDE is available for each licensed solution and Adobe also offers additional RDEs, which can be licensed for Production (non-sandbox) programs.

The number of RDEs needed depends on the make-up and processes of an organization. The most flexible model is where an organization purchases a dedicated RDE for each one of their AEM Cloud Service developers. In this model, each developer can test their code on the RDE without coordinating with other team members around whether an RDE environment is available.

At the other extreme, a team with a single RDE may use internal processes to coordinate which developers can use the environment at a given time. This can possibly be whenever a developer has hit an intermediate feature milestone and is ready to validate in a Cloud environment where they can quickly make the changes they need.

An in-between model is one where an organization purchases several RDEs so there is a greater likelihood of an unused RDE being available. One strategy could be to allocate an RDE per scrum team or major feature. Internal processes may be used to coordinate usage of the environments.

## How a AEM Forms Cloud Service Rapid Development Environment (RDE) is different from other environments? {#how-are-forms-rds-different-from-cloud-development-environments}

Forms developers can use AEM Forms Cloud Service Rapid Development Environment to quickly develop Adaptive Forms, Workflows, and customizations like customizing core components, integrations with third-party systems, and more. The AEM Forms Cloud Service Rapid Development Environment (RDE) has no support for Communication APIs. It also has not support for features and capabilities that require Document of Record, like generating a Document of Record on submission of an Adaptive Form. The below listed AEM Forms features are not available on a Rapid Development Environment (RDE):
 
* Configuring a Document of Record for an Adaptive Form
* Generating a Document of Record on submission of an Adaptive Form or with a Workflow step
* Send Document of Record as an attachment with Email Submit action or with Email step in a Workflow
* Using Adobe Sign in an Adaptive Form or in a Workflow step
* Communication APIs

>[!NOTE]
>
> There is no difference between the UI of Rapid Development Environment (RDE) and other Cloud Service environments for Forms. All Document of Record related options, like selecting a document of record template for an adaptive form, continues to appear in the UI. These environments have no Communication APIs and Document of Record capabilities to test such options. So, when you choose any option that requires Communication APIs or Document of Record capabilities, no action is performed, and an error message is displayed.

## RDE tutorial

To learn about RDE in AEM as a Cloud Service, see the video tutorial that demonstrates [how to set it up, how to use it, and the development life cycle (01:25)](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/developing/rde/overview.html).

# Troubleshooting (end of June)

## aio RDE plugin

### errors regarding insufficient permissions

To use the RDE plugin, it requires you to be a member of the Cloud Manager **Developer - Cloud Service** Product Profile. See [this page](/help/journey-onboarding/assign-profiles-cloud-manager.md#assign-developer) for more details.

Alternatively, you can confirm that you have this developer role if you can log in to the developer console by running this command:

   `aio cloudmanager:environment:open-developer-console`

   >[!TIP]
   >
   >If you see the `Warning: cloudmanager:* is not a aio command.` error, you must install the [aio-cli-plugin-cloudmanager](https://github.com/adobe/aio-cli-plugin-cloudmanager) by running the command below:
   >
   >```
   >aio plugins:install @adobe/aio-cli-plugin-cloudmanager
   >```

Verify that the login was completed successfully by running

   `aio cloudmanager:list-programs`

   This should list all programs under your configured organization and confirm that you have the correct role assigned.

## Detailed Permission Information

If not mentioned differently, all APIs prefix with ```/program/${programId}/environment/${environmentId}```

```serviceName```is ```author``` or ```publisher```

| Operation | API  | Product Profile(s) |
| :----- | :--- | :--- |
| get AEM logs | GET /runtime/${serviceName}/logs | [Developer - Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console#developer-console-access) |
| get AEM log | GET /runtime/${serviceName}/logs/${id} | [Developer - Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console#developer-console-access) |
| tail AEM log | GET /runtime/${serviceName}/logs/${id}/tail | [Developer - Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console#developer-console-access) |
| create AEM logs | POST /runtime/${serviceName}/logs | [Developer - Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console#developer-console-access) |
| delete AEM log | DEL /runtime/${serviceName}/logs/${id} | [Developer - Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console#developer-console-access) |
| get changes | GET /runtime/updates | [Developer - Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console#developer-console-access) |
| get change | GET /runtime/updates/${id} | [Developer - Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console#developer-console-access) |
| get logs of change | GET /runtime/updates/${id}/logs | [Developer - Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console#developer-console-access) |
| get status | GET /runtime/updates/artifacts | [Developer - Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console#developer-console-access) |
| install artifact | PUT /runtime/updates/${id} | [Developer - Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console#developer-console-access) |
| delete artifact | DEL /runtime/updates/artifacts/${id} | [Developer - Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console#developer-console-access) |
| reset | called on cloud manager (CM) | see [resetRDE](https://developer.adobe.com/experience-cloud/cloud-manager/guides/getting-started/permissions/#detailed-permission-information) | 
