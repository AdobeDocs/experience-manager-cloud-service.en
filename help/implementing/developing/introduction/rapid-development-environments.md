---
title: Rapid Development Environments
description: Learn how to leverage Rapid Development Environments for rapid development iterations on a cloud environment.
---

# Rapid Development Environments {#rapid-development-environments}

Current Cloud Development environments require a CI/CD pipeline deployment, a process that can take up 30 minutes for each change. To minimize the amount of time needed to test features that are proven to work on a local development environment, customers can leverage Rapid Development Environments (RDEs for short) to quickly push changes, ensuring that they work in the cloud, and making modifications as needed.

Once the changes have been tested in an RDE, you can deploy them to a regular Development environment through the Cloud Manager pipeline.

## Introduction {#introduction}

RDEs can be used for code, content and Apache or Dispatcher configurations. Unlike regular Cloud Development environments, developers can use local command line tools to sync code built with the local SDK to an RDE.

Every program is provisioned with an RDE. In case of Sandbox accounts, they will be hibernated after a few hours of non use.

Typically, an RDE would be used by a single developer at a given time, for testing and debugging a specific feature. When the development session is done, the RDE can be reset into a default state for the next usage.

Additional RDEs may be purchased for Production programs beginning with late January.

## Enabling RDE in a Program {#enabling-rde-in-a-program}

You can use Cloud Manager to add an RDE, manage who has access to it, and assign custom domains. For more information, see the Cloud Manager documentation.

## Installing the RDE Command Line Tools {#installing-the-rde-command-line-tools}

Each developer who will interact with the RDE should setup their command line tools as described in the following steps:

1. Add and RDE for your program using Cloud Manager. For more information, please consult the documentation.
1. Install the Adobe I/O CLI tools according by following the steps in [this article](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/development-tools.html?lang=en#aio-cli), or by following the procedure [here](https://developer.adobe.com/runtime/docs/guides/tools/cli_install/).
1. Install the Adobe aio command line tools cloud manager plugin, and configure them as described [here](https://github.com/adobe/aio-cli-plugin-cloudmanager).
1. Configure the cloud manager plugin for your IMS org:
   
   `aio config:set cloudmanager_orgid 9E07EZC05D54GS1A0B49431C@AdobeOrg`

   and replace the alpha numeric string with the one of your organization

1. Next, configure your program id:

   `aio config:set cloudmanager_programid 12345`

1. Then, configure the environment id the RDE is going to be attached to:

   `aio config:set cloudmanager_environmentid 123456`

1. Once you're done configuring the plugin, login by performing

   `aio login`

   The response on a successful login should resemble this output:

   ```
   ...
   You are currently in:
   1. Org: <no org selected>
   2. Project: <no project selected>
   3. Workspace: <no workspace selected>

   ```

1. Verify that the login completed successfully by running

   `aio cloudmanager:list-programs`

   This should list all programs under your configured organization.

1. Finally, install the Adobe aio command line tools AEM RDE plugin by running these commands:

   ```
   git clone git@git.corp.adobe.com:Granite/aio-cli-plugin-aem-rde.git
   cd aio-cli-plugin-aem-rde
   npm install
   aio plugins:link
   ```

   Note the above requires you be a member of the Cloud Manager **Developer - Cloud Service** Product Profile. See [this page](/help/journey-onboarding/assign-profiles-cloud-manager.md#assign-developer) for more details.

   Alternatively, you can confirm that you can have this developer role if you can login to the developer console by running this command:

   `aio cloudmanager:environment:open-developer-console`

## Using RDE while Developing a New Feature {#using-rde-while-developing-a-new-feature}

Adobe recommends the following workflow for developing a new feature:

* When an intermediate milestone is reached and successfully validated locally with the AEM as a Cloud Service SDK, the code should be committed to a git feature branch that is not yet part of the main line, although committing to git is optional. What constitutes an "intermediate milestone" will vary based on team habits. Examples include a small a few new lines of code, half a day of work, or completing a sub-feature.

* Reset the the RDE if it has been used by another feature and you want to reset it to a vanilla state. This can be done via Cloud Manager (see Cloud Manager documentation) or via command line (see RDE CLI commands section). Reset will take a few minutes and all existing content and code will be deleted. You can use the RDE status command to confirm the RDE is ready. See the [RDE Command Line Tools](#rde-cli-commands) for more information.

* Using the RDE command line interface or RDE CLI, sync local code to the RDE. Options include installing a content package, a specific bundle, an OSGI configuration file, a content file, and a zip file of an Apache/Dispatcher configuration. Referencing a remote content package is also possible. See the [RDE Command Line Tools](#rde-cli-commands) section for more information. You can use the status command to validate that the deployment was successful. Optionally, use Package Manager to install content packages.

* Test the code. Author and Publish URLs are available in Cloud Manager.

* If the code does not behave as expected, use standard debugging techniques to understand the problem and make the appropriate changes. Without committing the code modifications to git (since they haven't been validated), use the local CLI to sync the code to the RDE. Keep iterating until the issue is resolved.

* Once the code behaves as expected, commit the code to the git feature branch.

* Code synced to RDE doesn't use a Cloud Manager pipeline so now you should use Cloud Manager to deploy the git feature branch to the Cloud Dev environment. This validates that the code will pass the Cloud Manager quality gates and lets you be confident the code will later be successfully deployed to the Cloud Manager production pipeline.  

* Repeat the steps above for each intermediate milestone until all code for the feature is ready, and runs well on both the RDE and the Cloud Dev environment.

* Deploy the code to production via the Cloud Manager production pipeline. 

## Using RDE to Debug an Existing Feature {#use-rde-to-debug-an-existing-feature}

The workflow is similar to developing a new feature. The difference is that the code being synced to RDE would reflect the git label of whatever was pushed to the environment where the issue has been found. In addition, it may be useful to deploy content matching the upstream environment. This can be achieved through exporting and importing of content packages.

## Multiple Developers Collaborating on the Same RDE {#multiple-developers-collaborating-on-the-same-rde}

An RDE supports a single project at a time. Since code is synced from a local development environment to the RDE environment, it is most natural for one developer to be using it on their own at a given time.

However, with careful coordination, it is possible for more than one developer to validate a specific feature or debug a specific issue. The key is that each developers keep their local projects in sync so code changes made by a particular developer are absorbed by the other developers, otherwise one developer might inadvertently overwrite the others code. The recommended strategy is for each developer to commit their changes to a shared git branch before syncing to the RDE, so that the other developers pull the changes before making their own changes.

## RDE Command Line Tools Commands {#rde-cli-commands}

### Help/General Information {#help}

* For a list of commands, type:

  `aio aem:rde`

* For detailed help for a command, type:

  `aio aem rde <command> --help`

### Deploying to RDE {#deploying-to-rde}

This section deals with information on using the RDE CLI for deploying, installing or updating bundles, OSGI configurations, content packages, individual content files, and Apache or Dispatcher configurations.

The general usage pattern is `aio aem:rde:install <artifact>`.

You can find some examples below:

<u>Deploying a Content Package</u>

`aio io aem:rde:install sample.demo.ui.apps.all-1.0.0-SNAPSHOT.zip`

The response for a successful deployment will resemble the following:

```
...
#1: deploy completed for content-package sample.demo.ui.apps.all-1.0.0-SNAPSHOT.zip on author,publish - done by 9E072FC75D54FE1A2B49431C@AdobeID at 2022-09-13T11:32:06.229Z
```

Optionally, you can reference a remote repository:

`aio aem:rde:install 'https://repo1.maven.org/maven2/com/adobe/aem/guides/aem-guides-wknd.all/2.1.0/aem-guides-wknd.all-2.1.0.zip'`

<u>Deploying an OSGI Configuration</u>

`aio aem:rde:install com.adobe.granite.demo.MyServlet.cfg.json`

where the response for a succsessful deployment will resemble the following:

```
...
#2: deploy completed for osgi-config com.adobe.granite.demo.MyServlet.cfg.json on author,publish - done by 9E0725C05D54FE1A0B49431C@AdobeID at 2022-09-13T11:54:36.390Z
```

<u>Deploying a Bundle</u>

To deploy a bundle, use:

`aio aem:rde:install ~/.m2/repository/org/apache/felix/org.apache.felix.gogo.jline/1.1.8/org.apache.felix.gogo.jline-1.1.8.jar`

where the response for a successful deployment will resemble the following:

```
...
#3: deploy staged for osgi-bundle org.apache.felix.gogo.jline-1.1.8.jar on author,publish - done by 9E0725C05D53BE1A0B49431C@AdobeID at 2022-09-14T07:54:28.882Z
```

<u>Deploying a Content File</u>

To deploy a content file, use:

`aio aem:rde:install world.txt -p /apps/hello.txt`

where the response for a succesful deployment will resemble the following:

```
..
#4: deploy completed for content-file world.txt on author,publish - done by 9E0729C05C54FE1A0B49431C@AdobeID at 2022-09-14T07:49:30.644Z
```

<u>Deploying an Apache/Dispatcher Configuration</u>

>[NOTE!]
>
>For this type of configuration, the entire folder structure should be in the for of a zip file.

`aio aem:rde:install -t dispatcher-config dispatcher-wknd-2.1.0.zip`

where the response for a successful deplpoyment will resemble the following:

```
..
#5 deploy completed for dispatcher-config dispatcher.zip on author,publish - done by 9E0735C05T54FE1A0B49431C@AdobeID at 2022-10-03T10:26:31.286Z
```

Code deployed to RDE does not undergo a Cloud Manager pipeline and its associated quality gates, however the code does go through some analysis, which will report the errors, as illustrated in the code sample below:

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

The above code sample illustrates the behavior if a bundle doesn't resolve, in which case it is "staged" and will only be installed if its requirements (missing imports, in this case) are satisfied through installation of other code. 

### Checking the Status of the RDE {#checking-rde-status}

You can use the RDE CLI to check if the environment is ready to be deployed to, as what deployments have been made via the RDE plugin.

Running:

`aio aem:rde:status`

will return:

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

If he command returns a note about instances deploying, you can still go ahead and perform the next update, but your last one might not yet be visible on the instance.

### Show Deployment History {#show-deployment-history}

You can check the history of deployments made to the RDE by running:

`aio aem:rde:history`

which will return a response in the form of:

`#1: deploy completed for content-package aem-guides-wknd.all-2.1.0.zip on author,publish - done by 029039A55D4DE16A0A494025@AdobeID at 2022-09-12T14:41:55.393Z`

### Deleting from RDE {#deleting-from-rde}

You can delete configurations and bundles that have previously been deployed to RDE via the CLI tooling. Use the `status` command for a list of what can be deleted, which includes the `bsn` for bundles and `pid` for configs to reference in the delete command.

For example, if `com.adobe.granite.demo.MyServlet.cfg.json` has been installed, the `bsn` is just `com.adobe.granite.demo.MyServlet`, without the **cfg.json** suffix.

Deletion of content packages or content files is not supported.

See the example below for more details:

```
aio aem:rde:delete com.adobe.granite.csrf.impl.CSRFFilter
#13: delete completed for osgi-config com.adobe.granite.csrf.impl.CSRFFilter on author - done by karl at 2022-09-12T22:01:01.955Z
#14: delete completed for osgi-config com.adobe.granite.csrf.impl.CSRFFilter on publish - done by karl at 2022-09-12T22:01:12.979Z
```

## Logging {#logging}

Log levels can be set by modifying OSGI configurations. Check the [documentation](/help/implementing/developing/introduction/logging.md) for more information.

## How are RDEs Different from Cloud Development Environments? {#how-are-rds-different-from-cloud-development-environments}

* While the RDE is in many ways similar to a Cloud Development Environment, there are some minor architectural differences in order to allow for quick syncing of code.
* The mechanism for getting code to RDE is different. One syncs code from a local development environment to the RDE, while the other is deploying code via Cloud Manager to the Cloud Development Environment.
* For these reasons, it is recommended that after validating code on a RDE environment, you should deploy the code to a Cloud Development Environment using the non-production pipeline. Finally, test the code before deploying with the production pipeline.

## How many RDEs do I need? {#how-many-rds-do-i-need}

* The number of RDEs needed will depend on the make-up and processes of an organization.
* The most flexible model is where an organization purchases a dedicated RDE for each one of their AEM CS developers. In this model, each developer can test their code on the RDE without needing to coordinate with other team members around whether a RDE environment is available.
* At the other extreme, a team with a single RDE may use internal processes to coordinate which developer can use the environment at a given time. This can possibly be whenever a developer has hit an intermediate feature milestone and is ready to validate in a Cloud environment where they can quickly make the changes they need
* An intermediate model is one where an organization purchases a number of RDEs that will create a situation in which not every developer will have a dedicated environment, but there is a greater likelihood of an unused RDE being available. One strategy could be to allocate an RDE per scrum team or major feature. Internal processes may be used to coordinate usage of the environments.