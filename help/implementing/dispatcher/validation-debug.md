---
title: Validating and Debugging using Dispatcher Tools
description: Validating and Debugging using Dispatcher Tools
feature: Dispatcher
exl-id: 9e8cff20-f897-4901-8638-b1dbd85f44bf
---
# Validating and Debugging using Dispatcher Tools {#Dispatcher-in-the-cloud}

## Introduction {#apache-and-dispatcher-configuration-and-testing}

>[!NOTE]
>For more information about Dispatcher in the Cloud and how to download Dispatcher Tools, see the [Dispatcher in the Cloud](/help/implementing/dispatcher/disp-overview.md) page. If your dispatcher configuration is in legacy mode, refer to the [legacy mode documentation](/help/implementing/dispatcher/validation-debug-legacy.md).

The following sections describe the flexible mode file structure, local validation, debugging and migrating from legacy mode to the flexible mode.

This article assumes that your project's dispatcher configuration includes the file `opt-in/USE_SOURCES_DIRECTLY`, which causes the SDK and runtime to validate and deploy the configuration in an improved way compared to the legacy mode, removing limitations around the number and size of files.

As such, if your dispatcher configuration does not include the aforementioned file, it is **highly recommended** that you migrate from legacy mode to the flexible mode as outlined in the [Migrating from legacy mode to flexible mode](#migrating) section.

## File structure {#flexible-mode-file-structure}

The structure of the project's Dispatcher subfolder is as follows:

```bash
./
├── conf.d
│   ├── available_vhosts
│   │   └── default.vhost
│   ├── dispatcher_vhost.conf
│   ├── enabled_vhosts
│   │   ├── README
│   │   └── default.vhost -> ../available_vhosts/default.vhost
│   └── rewrites
│   │   ├── default_rewrite.rules
│   │   └── rewrite.rules
│   └── variables
|       ├── custom.vars
│       └── global.vars
│── opt-in
│   └── USE_SOURCES_DIRECTLY
└── conf.dispatcher.d
    ├── available_farms
    │   └── default.farm
    ├── cache
    │   ├── default_invalidate.any
    │   ├── default_rules.any
    │   └── rules.any
    ├── clientheaders
    │   ├── clientheaders.any
    │   └── default_clientheaders.any
    ├── dispatcher.any
    ├── enabled_farms
    │   ├── README
    │   └── default.farm -> ../available_farms/default.farm
    ├── filters
    │   ├── default_filters.any
    │   └── filters.any
    ├── renders
    │   └── default_renders.any
    └── virtualhosts
    │   ├── default_virtualhosts.any
    │   └── virtualhosts.any
    
```

Below is an explanation of notable files that can be modified:

**Customizable Files**

The following files are customizable and will get transferred to your Cloud instance on deployment:

* `conf.d/available_vhosts/<CUSTOMER_CHOICE>.vhost`

You can have one or more of these files. They contain `<VirtualHost>` entries that match host names and allow Apache to handle each domain traffic with different rules. Files are created in the `available_vhosts` directory and enabled with a symbolic link in the `enabled_vhosts` directory. From the `.vhost` files, other files like rewrites and variables will be included.

>[!NOTE]
>
>In flexible mode you should use relative paths instead of absolute paths.

* `conf.d/rewrites/rewrite.rules`

This file is included from inside your `.vhost` files. It has a set of rewrite rules for `mod_rewrite`.

* `conf.d/variables/custom.vars`

This file is included from inside your `.vhost` files. You can add defines for Apache variables in this location.

* `conf.d/variables/global.vars`

This file is included from inside the `dispatcher_vhost.conf` file. You can change your Dispatcher and rewrite log level in this file.

* `conf.dispatcher.d/available_farms/<CUSTOMER_CHOICE>.farm`

You can have one or more of these files, and they contain farms to match host names and allow the Dispatcher module to handle each farm with different rules. Files are created in the `available_farms` directory and enabled with a symbolic link in the `enabled_farms` directory. From the `.farm` files, other files like filters, cache rules and others will be included.

* `conf.dispatcher.d/cache/rules.any`

This file is included from inside your `.farm` files. It specifies caching preferences.

* `conf.dispatcher.d/clientheaders/clientheaders.any`

This file is included from inside your `.farm` files. It specifies what request headers should be forwarded to the backend.

* `conf.dispatcher.d/filters/filters.any`

This file is included from inside your `.farm` files. It has a set of rules that change what traffic should be filtered out and not make it to the backend.

* `conf.dispatcher.d/virtualhosts/virtualhosts.any`

This file is included from inside your `.farm` files. It has a list of host names or URI paths to be matched by glob matching. This determines what backend to use to serve a request.

* `opt-in/USE_SOURCES_DIRECTLY`

This file enables a more flexible dispatcher configuration and removes previous limitations around the number and size of files. It also causes the SDK and runtime to validate and deploy the configuration in an improved way.

The above files reference the immutable configuration files listed below. Changes to the immutable files will not be processed by Dispatchers in Cloud environments.

**Immutable Configuration Files**

These files are part of the base framework and enforce standards and best practices. The files are considered immutable because modifying or deleting them locally will have no impact on your deployment, as they will not get transferred to your Cloud instance.

It is recommended that the above files reference the immutable files listed below, followed by any additional statements or overrides. When Dispatcher configuration is deployed to a cloud environment, the latest version of the immutable files will be used, regardless of what version was used in local development.

* `conf.d/available_vhosts/default.vhost`

Contains a sample virtual host. For your own virtual host, create a copy of this file, customize it, go to `conf.d/enabled_vhosts` and create a symbolic link to your customized copy.

Ensure that a virtual host is always available that matches ServerAlias `\*.local` and also localhost, needed for internal Adobe processes.

* `conf.d/dispatcher_vhost.conf`

Part of the base framework, used to illustrate how your virtual hosts and global variables are included.

* `conf.d/rewrites/default_rewrite.rules`

Default rewrite rules suitable for a standard project. If you need customization, modify `rewrite.rules`. In your customization, you can still include the default rules first, if they suit your needs.

* `conf.dispatcher.d/available_farms/default.farm`

Contains a sample Dispatcher farm. For your own farm, create a copy of this file, customize it, go to `conf.d/enabled_farms` and create a symbolic link to your customized copy.

* `conf.dispatcher.d/cache/default_invalidate.any`

Part of the base framework, gets generated on startup. You are **required** to include this file in every farm you define, in the `cache/allowedClients` section.

* `conf.dispatcher.d/cache/default_rules.any`

Default cache rules suitable for a standard project. If you need customization, modify `conf.dispatcher.d/cache/rules.any`. In your customization, you can still include the default rules first, if they suit your needs.

* `conf.dispatcher.d/clientheaders/default_clientheaders.any`

Default request headers to forward to the backend, suitable for a standard project. If you need customization, modify `clientheaders.any`. In your customization, you can still include the default request headers first, if they suit your needs.

* `conf.dispatcher.d/dispatcher.any`

Part of base framework, used to illustrate how your Dispatcher farms are included.

* `conf.dispatcher.d/filters/default_filters.any`

Default filters suitable for a standard project. If you need customization, modify `filters.any`. In your customization, you can still include the default filters first, if they suit your needs.

* `conf.dispatcher.d/renders/default_renders.any`

Part of base framework, this file gets generated on startup. You are **required** to include this file in every farm you define, in the `renders` section.

* `conf.dispatcher.d/virtualhosts/default_virtualhosts.any`

Default host globbing suitable for a standard project. If you need customization, modify `virtualhosts.any`. In your customization, you shouldn't include the default host globbing, as it matches **every** incoming request.

## Supported Apache Modules {#apache-modules}

See [Supported Apache Modules](/help/implementing/dispatcher/disp-overview.md#supported-directives).

## Local validation {#local-validation-flexible-mode}

>[!NOTE]
>
>The sections below include commands using either the Mac or Linux versions of the SDK, but the Windows SDK can also be used in a similar way.

Use the `validate.sh` script as shown below:

```
$ validate.sh src/dispatcher
opt-in USE_SOURCES_DIRECTLY marker file detected
Phase 1: Dispatcher validator
Cloud manager validator 2.0.32
Phase 1 finished
Phase 2: httpd -t validation in docker image
values.csv not found in deployment folder: /Users/foo/src - using files in 'conf.d' and 'conf.dispatcher.d' subfolders directly
processing configuration subfolder: conf.d
processing configuration subfolder: conf.dispatcher.d
Running script /docker_entrypoint.d/10-check-environment.sh
Running script /docker_entrypoint.d/20-create-docroots.sh
Running script /docker_entrypoint.d/30-wait-for-backend.sh
Waiting until localhost is available
localhost resolves to ::1
Running script /docker_entrypoint.d/40-generate-allowed-clients.sh
Running script /docker_entrypoint.d/50-check-expiration.sh
Running script /docker_entrypoint.d/60-check-loglevel.sh
Running script /docker_entrypoint.d/70-check-forwarded-host-secret.sh
# Dispatcher configuration: (/etc/httpd/conf.dispatcher.d/dispatcher.any)
/farms {

... 

}
Syntax OK
Phase 2 finished
Phase 3: Immutability check
reading immutable file list from /etc/httpd/immutable.files.txt

...

no immutable file has been changed - check is SUCCESSFUL
Phase 3 finished
```

The script has the following three phases:

1. It runs the validator. If the configuration isn't valid, the script fails.
2. It executes the `httpd -t` command to test if syntax is correct such that apache httpd can start. If successful, the configuration should be ready for deployment.
3. Checks that the subset of the Dispatcher SDK configuration files, which are intended to be immutable as described in the [File structure section](##flexible-mode-file-structure), has not been modified.

During a Cloud Manager deployment, the `httpd -t` syntax check will be executed as well and any errors will be included in the Cloud Manager `Build Images step failure` log.

>[!NOTE]
>
>See the [Automatic reloading and validation](#automatic-loading) section for an efficient alternative to running `validate.sh` after each configuration modification.

### Phase 1 {#first-phase}

If a directive is not allowlisted, the tool logs an error and returns a non-zero exit code. Also, it further scans all files with pattern `conf.dispatcher.d/enabled_farms/*.farm` and checks that:

* No filter rule exists that uses allows via `/glob` (see [CVE-2016-0957](https://nvd.nist.gov/vuln/detail/CVE-2016-0957) for more details.
* No admin feature is exposed. For example, access to paths such as `/crx/de or /system/console`. 

Note that the validation tool reports only the prohibited use of Apache directives that have not been allowlisted. It does not report syntactical or semantical problems with your Apache configuration, as this information is only available to Apache modules in a running environment.

Presented below are troubleshooting techniques for debugging common validation errors that are output by the tool:

**unable to locate a `conf.dispatcher.d` subfolder in the archive**

Your archive should contain folders `conf.d` and `conf.dispatcher.d`. Note, that you should **not**
use the prefix `etc/httpd` in your archive.

**unable to find any farm in `conf.dispatcher.d/enabled_farms`**

Your enabled farms should be located in the mentioned subfolder.

**file included (...) must be named: ...**

There are two sections in your farm configuration that **must** include a
specific file: `/renders` and `/allowedClients` in the `/cache` section. Those 
sections must look as follows:

```
/renders {
    $include "../renders/default_renders.any"
}
```

and:

```
/allowedClients {
    $include "../cache/default_invalidate.any"
}
```

**file included at unknown location: ...**

There are four sections in your farm configuration where you're allowed to include your own file: `/clientheaders`, `filters`, `/rules` in `/cache` section and `/virtualhosts`. The included files need to be named as follows:

| Section          | Include file name                    |
|------------------|--------------------------------------|
| `/clientheaders` | `../clientheaders/clientheaders.any` |
| `/filters`       | `../filters/filters.any`             |
| `/rules`         | `../cache/rules.any`                 |
| `/virtualhosts`  | `../virtualhosts/virtualhosts.any`   |

Alternatively, you can include the **default** version of those files, whose names are prepended with the word `default_`, e.g. `../filters/default_filters.any`.

**include statement at (...), outside any known location: ...**

Apart from the six sections mentioned in the paragraphs above, you are not allowed
to use the `$include` statement, e.g. the following would generate this error:

```
/invalidate {
    $include "../cache/invalidate.any"
}
```

**allowed clients/renders are not included from: ...**

This error is generated when you don't specify an include for `/renders` and `/allowedClients` in the `/cache` section. See the 
**file included (...) must be named: ...** section for more information.

**filter must not use glob pattern to allow requests**

It is not secure to allow requests with a `/glob` style rule, which is matched against the complete request line, e.g.

```

/0100 {
    /type "allow" /glob "GET *.css *"
}

```

This statement is meant to allow requests for `css` files, but it also allows requests to **any** resource followed by the query string `?a=.css`. It is therefore forbidden to use such filters (see also CVE-2016-0957).

**included file (...) does not match any known file**

There are two types of files in your Apache virtual host configuration that can be specified as includes: rewrites and variables.
The included files need to be named as follows:

| Type      | Include file name               |
|-----------|---------------------------------|
| Rewrites  | `conf.d/rewrites/rewrite.rules` |
| Variables | `conf.d/variables/custom.vars`  |

Alternatively, you can include the **default** version of the rewrite rules, whose name is `conf.d/rewrites/default_rewrite.rules`.
Note, that there is no default version of the variables files.

**Deprecated configuration layout detected, enabling compatibility mode**

This message indicates that your configuration has the deprecated version 1 layout, containing a complete
Apache configuration and files with `ams_` prefixes. While this is still supported for backwards
compatibility, you should switch to the new layout.

Please note that the first phase can also be **run separately**, rather than from the wrapper `validate.sh` script.

When run against your maven artifact or your `dispatcher/src` subdirectory, it will report validation failures:

```
$ validator full -relaxed dispatcher/src
Cloud manager validator 1.0.4
2019/06/19 15:41:37 Apache configuration uses non-allowlisted directives:
  conf.d/enabled_vhosts/aem_publish.vhost:46: LogLevel
2019/06/19 15:41:37 Dispatcher configuration validation failed:
  conf.dispatcher.d/enabled_farms/999_ams_publish_farm.any: filter allows access to CRXDE
```

On Windows, the dispatcher validator is case-sensitive. As such, it can fail to validate the configuration if you do not respect the capitalization of the path where your configuration resides, for example:

```
bin\validator.exe -relaxed full src
Cloud manager validator 2.0.xx
2021/03/15 18:15:40 Dispatcher configuration validation failed:
  conf.dispatcher.d\available_farms\default.farm:15: parent directory outside server root: c:\k\a\aem-dispatcher-sdk-windows-symlinks-testing3\dispatcher\src
```

Avoid this error by copying and pasting the path from Windows Explorer and then on the command prompt using a `cd` command into that path.

### Phase 2 {#second-phase}

This phase checks the apache syntax by starting Docker in an image. Docker must be installed locally, but note that it’s not necessary for AEM to be running.

>[!NOTE]
>
>Windows users need to use Windows 10 Professional or other distributions that support Docker. This is a pre-requisite for running and debugging Dispatcher on a local computer.

This phase can also be run independently through `bin/docker_run.sh src/dispatcher host.docker.internal:4503 8080`.

During a Cloud Manager deployment, the `httpd -t` syntax check will also be executed and any errors will be included in the Cloud Manager Build Images step failure log.

### Phase 3 {#third-phase}

If there is a failure in this phase, it implies that Adobe has changed one or more immutable files and you must replace the corresponding immutable files with the new version delivered in the `src` directory of the SDK. The log sample bellow illustrates this issue:

```

Phase 3: Immutability check
reading immutable file list from /etc/httpd/immutable.files.txt
(...)
checking existing 'conf.dispatcher.d/clientheaders/default_clientheaders.any' for changes
immutable file 'conf.dispatcher.d/clientheaders/default_clientheaders.any' has been changed:
--- /etc/httpd/conf.dispatcher.d/clientheaders/default_clientheaders.any
+++ /etc/httpd-actual/conf.dispatcher.d/clientheaders/default_clientheaders.any
@@ -40,4 +40,3 @@
"Sling-uploadmode"
"x-requested-with"
"If-Modified-Since"
-"Authorization"
** error: immutable file 'conf.dispatcher.d/clientheaders/default_clientheaders.any' has been changed!
  
```

This phase can also be run independently through `bin/docker_immutability_check.sh src/dispatcher`.

## Debugging your Apache and Dispatcher configuration {#debugging-apache-and-dispatcher-configuration}

Please note that you can run apache dispatcher locally by using `./bin/docker_run.sh src/dispatcher docker.for.mac.localhost:4503 8080`.

As stated previously, Docker must be installed locally and it is not necessary for AEM to be running. Windows users need to use Windows 10 Professional or other distributions that support Docker. This is a pre-requisite for running and debugging Dispatcher on a local computer.

The following strategy can be used to increase the log output for the Dispatcher module and see the results of the `RewriteRule` evaluation in both local and cloud environments.

Log levels for those modules are defined by the variables `DISP_LOG_LEVEL` and `REWRITE_LOG_LEVEL`. They can be set in the file `conf.d/variables/global.vars`. Its relevant part follows:

```

# Log level for the dispatcher
#
# Possible values are: Error, Warn, Info, Debug and Trace1
# Default value: Warn
#
# Define DISP_LOG_LEVEL Warn
 
# Log level for mod_rewrite
#
# Possible values are: Error, Warn, Info, Debug and Trace1 - Trace8
# Default value: Warn
#
# To debug your RewriteRules, it is recommended to raise your log
# level to Trace2.
#
# More information can be found at:
# https://httpd.apache.org/docs/current/mod/mod_rewrite.html#logging
#
# Define REWRITE_LOG_LEVEL Warn

```

When running Dispatcher locally, logs are printed directly to the terminal output. Most of the time, you want these logs to be in DEBUG, which can be done by passing the Debug level as a parameter when running Docker. For example: `DISP_LOG_LEVEL=Debug ./bin/docker_run.sh src docker.for.mac.localhost:4503 8080`.

Logs for cloud environments are exposed through the logging service available in Cloud Manager.

### Automatic reloading and validation {#automatic-reloading}

>[!NOTE]
>
>Due to a Windows operating system limitation, this feature is available only for macOS and Linux users.

Instead of running local validation (`validate.sh`) and starting the docker container (`docker_run.sh`) each time the configuration is modified, you can alternatively run the `docker_run_hot_reload.sh` script.  The script watches for any changes to the configuration and will automatically reload it and re-run the validation. By using this option you can save a significant amount of time when debugging.

You can run the script by using the following command: `./bin/docker_run_hot_reload.sh src/dispatcher host.docker.internal:4503 8080`

Note that the first lines of output will look similar to what would run for `docker_run.sh`, for example:

```
~ bin/docker_run_hot_reload.sh src host.docker.internal:8081 8082
opt-in USE_SOURCES_DIRECTLY marker file detected
Running script /docker_entrypoint.d/10-check-environment.sh
Running script /docker_entrypoint.d/15-check-pod-name.sh
Running script /docker_entrypoint.d/20-create-docroots.sh
Running script /docker_entrypoint.d/30-wait-for-backend.sh
Waiting until host.docker.internal is available
host.docker.internal resolves to 192.168.65.2
Running script /docker_entrypoint.d/40-generate-allowed-clients.sh
Running script /docker_entrypoint.d/50-check-expiration.sh
Running script /docker_entrypoint.d/60-check-loglevel.sh
Running script /docker_entrypoint.d/70-check-forwarded-host-secret.sh
Running script /docker_entrypoint.d/80-frontend-domain.sh
Running script /docker_entrypoint.d/zzz-import-sdk-config.sh
WARN Mon Jul  4 09:53:54 UTC 2022: Pseudo symlink conf.d seems to point to a non-existing file!
INFO Mon Jul  4 09:53:55 UTC 2022: Copied customer configuration to /etc/httpd.
INFO Mon Jul  4 09:53:55 UTC 2022: Start testing
Cloud manager validator 2.0.43
2022/07/04 09:53:55 No issues found
INFO Mon Jul  4 09:53:55 UTC 2022: Testing with fresh base configuration files.
INFO Mon Jul  4 09:53:55 UTC 2022: Apache httpd informationServer version: Apache/2.4.54 (Unix)

```

## Different Dispatcher configurations per environment {#different-dispatcher-configurations-per-environment}

Currently, the same Dispatcher configuration is applied to all AEM as a Cloud Service environments. The runtime will have an environment variable `ENVIRONMENT_TYPE` that contains the current run mode (dev, stage or prod) as well as a define. The define can be `ENVIRONMENT_DEV`, `ENVIRONMENT_STAGE` or `ENVIRONMENT_PROD`. In the Apache configuration, the variable can be used directly in an expression. Alternatively, the define can be used to build logic:

```

# Simple usage of the environment variable
ServerName ${ENVIRONMENT_TYPE}.company.com
 
# When more logic is required
<IfDefine ENVIRONMENT_STAGE>
  # These statements are for stage
  Define VIRTUALHOST stage.example.com
</IfDefine>
<IfDefine ENVIRONMENT_PROD>
  # These statements are for production
  Define VIRTUALHOST prod.example.com
</IfDefine>

```

In the Dispatcher configuration, the same environment variable is available. If more logic is required, define the variables as shown in the example above and then use them in the Dispatcher configuration section:

```

/virtualhosts {
  { "${VIRTUALHOST}" }
}

```

Alternatively, you can use Cloud Manager environment variables in your httpd/dispatcher configuration, although not environment secrets. This method is especially important if a program has multiple dev environments and some of those dev environments have different values for httpd/dispatcher configuration. The same ${VIRTUALHOST} syntax would be used as in the example above, however the Define declarations in the above variables file would not be used. Read the [Cloud Manager documentation](/help/implementing/cloud-manager/environment-variables.md) for instructions on configuring Cloud Manager environment variables.

When testing your configuration locally, you can simulate different environment types by passing the variable `DISP_RUN_MODE` to the `docker_run.sh` script directly:

```

$ DISP_RUN_MODE=stage docker_run.sh src docker.for.mac.localhost:4503 8080

```

The default runmode when not passing in a value for DISP_RUN_MODE is "dev". 
For a complete list of options and variables available, run the script `docker_run.sh` without arguments.

## Viewing the Dispatcher configuration in use by your Docker container {#viewing-dispatcher-configuration-in-use-by-docker-container}

With environment specific configurations, it can be difficult to determine what the actual Dispatcher configuration looks like. After having started your docker container with `docker_run.sh` it can be dumped as follows:

* Determine the docker container ID in use:

```

$ docker ps
CONTAINER ID       IMAGE
d75fbd23b29        adobe/aem-ethos/dispatcher-publish:...

```

*  Execute the following command line with that container ID:

```

$ docker exec d75fbd23b29 httpd-test
# Dispatcher configuration: (/etc/httpd/conf.dispatcher.d/dispatcher.any)
/farms {
  /publishfarm {
    /clientheaders {
...

```

## Migrating from legacy mode to flexible mode {#migrating}

With the Cloud Manager 2021.7.0 release, new Cloud Manager programs generate maven project structures with [AEM archetype 28](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/overview.html?lang=en) or higher,which includes the file **opt-in/USE_SOURCES_DIRECTLY**. This removes previous limitations of the [legacy mode](/help/implementing/dispatcher/validation-debug-legacy.md) around the number and size of files, also causing the SDK and runtime to validate and deploy the configuration in an improved way. If your dispatcher configuration does not have this file, it is highly recommended that you migrate. Use the following steps to ensure a safe transition:

1. **Local testing.** Using the most recent dispatcher tools SDK, add the folder and file `opt-in/USE_SOURCES_DIRECTLY`. Follow the "local validation" instructions in this article to test that the dispatcher works locally.
1. **Cloud development testing:**
   * Commit the file `opt-in/USE_SOURCES_DIRECTLY` to a git branch that is deployed by the non-production pipeline to a Cloud development environment.
   * Use Cloud Manager to deploy to a Cloud development environment.
   * Test thoroughly. It is critical to validate that your apache and dispatcher configuration behaves as you expect before deploying changes to higher environments. Check all behavior related to your custom configuration! File a customer support ticket if you believe the deployed dispatcher configuration does not reflect your custom configuration.
   >[!NOTE]
   >
   >In flexible mode you should use relative paths instead of absolute paths.
1. **Deploy to production:**
   * Commit the file `opt-in/USE_SOURCES_DIRECTLY` to a git branch that is deployed by the production pipeline to the Cloud stage and production environments.
   * Use Cloud Manager to deploy to staging.
   * Test thoroughly. It is critical to validate that your apache and dispatcher configuration behaves as you expect before deploying changes to higher environments. Check all behavior related to your custom configuration! File a customer support ticket if you believe the deployed dispatcher configuration does not reflect your custom configuration.
   * Use Cloud Manager to continue the deployment to production.
