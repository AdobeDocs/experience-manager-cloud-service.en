---
title: Dispatcher in the Cloud
description: Dispatcher in the Cloud 
feature: Dispatcher
---

# Dispatcher in the Cloud {#Dispatcher-in-the-cloud}

## Apache and Dispatcher configuration and testing {#apache-and-dispatcher-configuration-and-testing}

This section describes how to structure the AEM as a Cloud Service Apache and Dispatcher configurations, as well as how to validate  and run it locally before deploying to Cloud environments. It also describes debugging in Cloud environments. For additional information about Dispatcher, see the [AEM Dispatcher documentation](https://docs.adobe.com/content/help/en/experience-manager-dispatcher/using/dispatcher.html).

>[!NOTE]
>Windows users will need to use Windows 10 Professional or other distributions that support Docker. This is a pre-requisite for running and debugging Dispatcher on a local computer. The sections below include commands using the Mac or Linux versions of the SDK, but the Windows SDK can be used in a similar way.

## Dispatcher Tools {#dispatcher-sdk}

The Dispatcher Tools are part of the overall AEM as a Cloud Service SDK and provide:

* A vanilla file structure containing the configuration files to include in a maven project for dispatcher.
* Tooling for customers to validate that the dispatcher configuration includes only AEM as a Cloud Service supported directives.        Additionally, the tooling also validates that the syntax is correct so apache can start successfully.
* A Docker image that brings up the dispatcher locally.

## Downloading and Extracting the Tools {#extracting-the-sdk}

The Dispatcher Tools, part of the [AEM as a Cloud Service SDK](/help/implementing/developing/introduction/aem-as-a-cloud-service-sdk.md), can be downloaded from a zip file at the [Software Distribution](https://downloads.experiencecloud.adobe.com/content/software-distribution/en/aemcloud.html) portal. Any new configuration available in that new dispatcher Tools version, can be used to deploy to Cloud environments running that version of AEM in the Cloud or higher.

Unzip the SDK, which bundles Dispatcher Tools for both macOS/Linux and Windows.

**For macOS/Linux**, make the dispatcher tool artifact executable and run it. It will self extract the Dispatcher Tools files underneath the directory you stored it to (where `version` is the version of the dispatcher Tools).

```bash
$ chmod +x aem-sdk-dispatcher-tools-<version>-unix.sh
$ ./aem-sdk-dispatcher-tools-<version>-unix.sh
Verifying archive integrity...  100%   All good.
Uncompressing aem-sdk-dispatcher-tools-<version>-unix.sh 100%
```

**For Windows**, extract the Dispatcher Tooling zip archive.

## File Structure {#file-structure}

The structure of the project's dispatcher subfolder is described below and should be copied into the maven project dispatcher folder:

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
        ├── default_virtualhosts.any
        └── virtualhosts.any
```

Below is an explanation of notable files that can be modified:

**Customizable Files**

The following files are customizable and will get transferred to your Cloud instance on deployment:

* `conf.d/available_vhosts/<CUSTOMER_CHOICE>.vhost`

You can have one or more of these files. They contain `<VirtualHost>` entries that match host names and allow Apache to handle each domain traffic with different rules. Files are created in the `available_vhosts` directory and enabled with a symbolic link in the `enabled_vhosts` directory. From the `.vhost` files, other files like rewrites and variables will be included.

* `conf.d/rewrites/rewrite.rules`

This file is included from inside your `.vhost` files. It has a set of rewrite rules for `mod_rewrite`. 

>[!NOTE]
>
>At this time, a single rewrite file must be used rather than site specific files. That file size must be less than 1MB.

* `conf.d/variables/custom.vars`

This file is included from inside your `.vhost` files. You can put defines for Apache variables in this location.

* `conf.d/variables/global.vars`

This file is included from inside the `dispatcher_vhost.conf` file. You can change your dispatcher and rewrite log level in this file.

* `conf.dispatcher.d/available_farms/<CUSTOMER_CHOICE>.farm`

You can have one or more of these files, and they contain farms to match host names and allow the dispatcher module to handle each farm with different rules. Files are created in the `available_farms` directory and enabled with a symbolic link in the `enabled_farms` directory. From the `.farm` files, other files like filters, cache rules and others will be included.

* `conf.dispatcher.d/cache/rules.any`

This file is included from inside your `.farm` files. It specifies caching preferences.

* `conf.dispatcher.d/clientheaders/clientheaders.any`

This file is included from inside your `.farm` files. It specifies what request headers should be forwarded to the backend.

* `conf.dispatcher.d/filters/filters.any`

This file is included from inside your `.farm` files. It has a set of rules that change what traffic should be filtered out and not make it to the backend.

* `conf.dispatcher.d/virtualhosts/virtualhosts.any`

This file is included from inside your `.farm` files. It has a list of host names or URI paths to be matched by glob matching. This determines what backend to use to serve a request.

The above files reference the immutable configuration files listed below. Changes to the immutable files will not be processed by dispatchers in Cloud environments.

**Immutable Configuration Files**

These files are part of the base framework and enforce standards and best practices. The files are considered immutable because modifying or deleting them locally will have no impact on your deployment, as they will not get transferred to your Cloud instance.

It is recommended that the above files reference the immutable files listed below, followed by any additional statements or overrides. When dispatcher configuration is deployed to a cloud environment, the latest version of the immutable files will be used, regardless of what version was used in local development.

* `conf.d/available_vhosts/default.vhost`

Contains a sample virtual host. For your own virtual host, create a copy of this file, customize it, go to `conf.d/enabled_vhosts` and create a symbolic link to your customized copy.

* `conf.d/dispatcher_vhost.conf`

Part of the base framework, used to illustrate how your virtual hosts and global variables are included.

* `conf.d/rewrites/default_rewrite.rules`

Default rewrite rules suitable for a standard project. If you need customization, modify `rewrite.rules`. In your customization, you can still include the default rules first, if they suit your needs.

* `conf.dispatcher.d/available_farms/default.farm`

Contains a sample dispatcher farm. For your own farm, create a copy of this file, customize it, go to `conf.d/enabled_farms` and create a symbolic link to your customized copy.

* `conf.dispatcher.d/cache/default_invalidate.any`

Part of the base framework, gets generated on startup. You are **required** to include this file in every farm you define, in the `cache/allowedClients` section.

* `conf.dispatcher.d/cache/default_rules.any`

Default cache rules suitable for a standard project. If you need customization, modify `conf.dispatcher.d/cache/rules.any`. In your customization, you can still include the default rules first, if they suit your needs.

* `conf.dispatcher.d/clientheaders/default_clientheaders.any`

Default request headers to forward to the backend, suitable for a standard project. If you need customization, modify `clientheaders.any`. In your customization, you can still include the default request headers first, if they suit your needs.

* `conf.dispatcher.d/dispatcher.any`

Part of base framework, used to illustrate how your dispatcher farms are included.

* `conf.dispatcher.d/filters/default_filters.any`

Default filters suitable for a standard project. If you need customization, modify `filters.any`. In your customization, you can still include the default filters first, if they suit your needs.

* `conf.dispatcher.d/renders/default_renders.any`

Part of base framework, this file gets generated on startup. You are **required** to include this file in every farm you define, in the `renders` section.

* `conf.dispatcher.d/virtualhosts/default_virtualhosts.any`

Default host globbing suitable for a standard project. If you need customization, modify `virtualhosts.any`. In your customization, you shouldn't include the default host globbing, as it matches **every** incoming request.

>[!NOTE]
>
>The AEM as a Cloud Service maven archetype will generate the same dispatcher configuration file structure.

The sections below describe how to validate the configuration locally so it can pass the associated quality gate in Cloud Manager when deploying an internal release.

## Local validation of supported directives in Dispatcher configuration {#local-validation-of-dispatcher-configuration}

The validation tool is available in the SDK at `bin/validator` as a Mac OS, Linux, or Windows binary, allowing customers to run the same validation that Cloud Manager will perform while building and deploying a release.

It is invoked as: `validator full [-d folder] [-w allowlist] zip-file | src folder`

The tool validates that the dispatcher configuration is using the appropriate directives supported by AEM as a Cloud service by scanning all files with pattern `conf.d/enabled_vhosts/*.vhost`. The directives allowed in Apache configuration files can be listed by running the validator's allowlist command:

```

$ validator allowlist
Cloud manager validator 2.0.4
 
Allowlisted directives:
  <Directory>
  ...
  
```

The table below shows the supported apache modules:

| Module Name | Reference Page |
|---|---|
| `core` | [https://httpd.apache.org/docs/2.4/mod/core.html](https://httpd.apache.org/docs/2.4/mod/core.html) |
| `mod_access_compat` | [https://httpd.apache.org/docs/2.4/mod/mod_access_compat.html](https://httpd.apache.org/docs/2.4/mod/mod_access_compat.html) |
| `mod_alias` | [https://httpd.apache.org/docs/2.4/mod/mod_alias.html](https://httpd.apache.org/docs/2.4/mod/mod_alias.html) |
| `mod_allowmethods` | [https://httpd.apache.org/docs/2.4/mod/mod_allowmethods.html](https://httpd.apache.org/docs/2.4/mod/mod_allowmethods.html) |
| `mod_authn_core` | [https://httpd.apache.org/docs/2.4/mod/mod_authn_core.html](https://httpd.apache.org/docs/2.4/mod/mod_authn_core.html) |
| `mod_authn_file` | [https://httpd.apache.org/docs/2.4/mod/core.html](https://httpd.apache.org/docs/2.4/mod/mod_authn_file.html) |
| `mod_authz_core` | [https://httpd.apache.org/docs/2.4/mod/core.html](https://httpd.apache.org/docs/2.4/mod/mod_authz_core.html) |
| `mod_authz_groupfile` | [https://httpd.apache.org/docs/2.4/mod/mod_authz_groupfile.html](https://httpd.apache.org/docs/2.4/mod/mod_authz_groupfile.html) |
| `mod_deflate` | [https://httpd.apache.org/docs/2.4/mod/mod_deflate.html](https://httpd.apache.org/docs/2.4/mod/mod_deflate.html) |
| `mod_dir` | [https://httpd.apache.org/docs/2.4/mod/mod_dir.html](https://httpd.apache.org/docs/2.4/mod/mod_dir.html) |
| `mod_env` | [https://httpd.apache.org/docs/2.4/mod/mod_env.html](https://httpd.apache.org/docs/2.4/mod/mod_env.html) |
| `mod_filter` | [https://httpd.apache.org/docs/2.4/mod/mod_filter.html](https://httpd.apache.org/docs/2.4/mod/mod_filter.html) |
| `mod_headers` | [https://httpd.apache.org/docs/2.4/mod/mod_headers.html](https://httpd.apache.org/docs/2.4/mod/mod_headers.html) |
| `mod_mime` | [https://httpd.apache.org/docs/2.4/mod/mod_mime.html](https://httpd.apache.org/docs/2.4/mod/mod_mime.html) |
| `mod_remoteip` | [https://httpd.apache.org/docs/2.4/mod/mod_remoteip.html](https://httpd.apache.org/docs/2.4/mod/mod_remoteip.html) |
| `mod_reqtimeout` | [https://httpd.apache.org/docs/2.4/mod/mod_reqtimeout.html](https://httpd.apache.org/docs/2.4/mod/mod_reqtimeout.html) |
| `mod_rewrite` | [https://httpd.apache.org/docs/2.4/mod/mod_rewrite.html](https://httpd.apache.org/docs/2.4/mod/mod_rewrite.html) |
| `mod_security` | [https://modsecurity.org/](https://modsecurity.org/) |
| `mod_setenvif` | [https://httpd.apache.org/docs/2.4/mod/mod_setenvif.html](https://httpd.apache.org/docs/2.4/mod/mod_setenvif.html) |
| `mod_substitute` | [https://httpd.apache.org/docs/2.4/mod/mod_substitute.html](https://httpd.apache.org/docs/2.4/mod/mod_substitute.html) |
| `mod_userdir` | [https://httpd.apache.org/docs/2.4/mod/mod_userdir.html](https://httpd.apache.org/docs/2.4/mod/mod_userdir.html) |

Customers cannot add arbitrary modules, however additional modules may be considered for inclusion in the product in the future. Customers can find the list of directives available for a given Dispatcher version by executing validator's allowlist command in the SDK, as described above.

The allowlist contains a list of Apache directives that are permitted in a customer configuration. If a directive is not allowlisted, the tool logs an error and returns a non-zero exit code. If no allowlist is given on the command line (which is the way it should be invoked), the tool uses a default allowlist that Cloud Manager will use for validation before deploying to Cloud environments.

 Also, it further scans all files with pattern `conf.dispatcher.d/enabled_farms/*.farm` and checks that:

* No filter rule exists that uses allows via `/glob` (see [CVE-2016-0957](https://nvd.nist.gov/vuln/detail/CVE-2016-0957) for more details)
* No admin feature is exposed. For example, access to paths such as `/crx/de or /system/console`. 

When run against your maven artifact or your `dispatcher/src` subdirectory, it will report validation failures:

```

$ validator full dispatcher/src
Cloud manager validator 1.0.4
2019/06/19 15:41:37 Apache configuration uses non-allowlisted directives:
  conf.d/enabled_vhosts/aem_publish.vhost:46: LogLevel
2019/06/19 15:41:37 Dispatcher configuration validation failed:
  conf.dispatcher.d/enabled_farms/999_ams_publish_farm.any: filter allows access to CRXDE

```

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
Apache configuration and files with `ams_` prefixes. While this is still supported for backward
compatibility you should switch to the new layout.

## Local validation of dispatcher configuration syntax so that apache httpd can start {#local-validation}

Once it has been established that the dispatcher module configuration includes only supported directives, you should check that the syntax is correct so that apache can start up. In order to test this, the docker must be installed locally. And note that it's not necessary for AEM to be running.

Use the `validate.sh` script as shown below:

```

$ validate.sh src/dispatcher
Phase 1: Dispatcher validator
2019/06/19 16:02:55 No issues found
Phase 1 finished
Phase 2: httpd -t validation in docker image
Running script /docker_entrypoint.d/10-create-docroots.sh
Running script /docker_entrypoint.d/20-wait-for-backend.sh
Waiting until aemhost is available
aemhost resolves to xx.xx.xx.xx
Running script /docker_entrypoint.d/30-allowed-clients.sh
# Dispatcher configuration: (/etc/httpd/conf.dispatcher.d/dispatcher.any)
/farms {
...
}
Syntax OK
Phase 2 finished

```

The script does the following:

1. It runs the validator from the previous section to ensure that only the supported directives are included. If the configuration isn't valid, the script will fail.
2. It executes the `httpd -t command` to test if syntax is correct such that apache httpd can start. If successful, the configuration should be ready for deployment.
3. Checks that the subset of the dispatcher SDK configuration files, which are intended to be immutable as described in the [File structure section](#file-structure), has not been modified. This is a new check, introduced with AEM SDK version v2021.1.4738 that also includes Dispatcher Tools version 2.0.36. Before this update, customers might have incorrectly assumed that any local SDK modifications of those immutable files would also be applied to the Cloud environment.

During a Cloud Manager deployment, the `httpd -t syntax` check will be executed as well and any errors will be included in the Cloud Manager `Build Images step failure` log.

## Testing your Apache and Dispatcher configuration locally {#testing-apache-and-dispatcher-configuration-locally}

It is also possible to test drive your Apache and Dispatcher configuration locally. It requires the docker to be installed locally and your configuration to pass the validation as described above.

Execute the validator tool (note that it is different from the `validator.sh` mentioned earlier), by using the `-d` parameter which outputs a folder with all the dispatcher configuration files. Then execute the `docker_run.sh` script, passing that folder as an argument. By providing the port number (here: 8080) to expose the dispatcher endpoint, a Docker container is started, running the dispatcher with your configuration.

```

$ validator full -d out src/dispatcher
2019/06/19 16:02:55 No issues found
$ docker_run.sh out docker.for.mac.localhost:4503 8080
Running script /docker_entrypoint.d/10-create-docroots.sh
Running script /docker_entrypoint.d/20-wait-for-backend.sh
Waiting until aemhost is available
aemhost resolves to xx.xx.xx.xx
Running script /docker_entrypoint.d/30-allowed-clients.sh
Starting httpd server
...

```

This will start the dispatcher in a container with its backend pointing to an AEM instance running on your local Mac OS machine at port 4503.

## Debugging your Apache and Dispatcher configuration {#debugging-apache-and-dispatcher-configuration}

The following strategy can be used to increase the log output for the dispatcher module and see the results of the `RewriteRule` evaluation in both local and cloud environments.

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

When running dispatcher locally, logs are printed directly to the terminal output. Most of the time, you want these logs to be in DEBUG, which can be done by passing the Debug level as a parameter when running Docker. For example: `DISP_LOG_LEVEL=Debug ./bin/docker_run.sh out docker.for.mac.localhost:4503 8080`.

Logs for cloud environments are be exposed through the logging service available in Cloud Manager.

## Different Dispatcher configurations per environment {#different-dispatcher-configurations-per-environment}

At this time, the same dispatcher configuration is applied to all AEM as a Cloud Service environments. The runtime will have an environment variable `ENVIRONMENT_TYPE` that contains the current run mode (dev, stage or prod) as well as a define. The define can be `ENVIRONMENT_DEV`, `ENVIRONMENT_STAGE` or `ENVIRONMENT_PROD`. In the Apache configuration, the variable can be used directly in an expression. Alternatively, the define can be used to build logic:

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

When testing your configuration locally, you can simulate different environment types by passing the variable `DISP_RUN_MODE` to the `docker_run.sh` script directly:

```

$ DISP_RUN_MODE=stage docker_run.sh out docker.for.mac.localhost:4503 8080

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

## Main Differences between AMS Dispatcher and AEM as a Cloud Service {#main-differences-between-ams-dispatcher-configuration-and-aem-as-a-cloud-service}

As described on the reference page above, the Apache and Dispatcher configuration in AEM as a Cloud Service is quite similar to the AMS one. The main differences are:

* In AEM as a Cloud Service, some Apache directives may not be used (for example `Listen` or `LogLevel`)
* In AEM as a Cloud Service, only some pieces of the Dispatcher configuration can be put in include files and their naming is important. For example, filter rules that you want to reuse across different hosts must be put in a file called `filters/filters.any`. See the reference page for more information.
* In AEM as a Cloud Service there is extra validation to disallow filter rules written using `/glob` to prevent security issues. Since `deny *` will be used rather than `allow *` (which cannot be used), customers will benefit from running the Dispatcher locally and doing trial and error, looking at the logs to know exactly what paths the Dispatcher filters are blocking in order for those can be added.

## Guidelines for migrating dispatcher configuration from AMS to AEM as a Cloud Service

The dispatcher configuration structure has differences between Managed Services and AEM as a Cloud Service. Presented below, is a a step by step guide on how to migrate from AMS Dispatcher configuration version 2 to AEM as a Cloud Service.

## How to convert an AMS to an AEM as a Cloud service dispatcher configuration

The following section provides a step by step instructions on how to convert an AMS configuration. It assumes
that you have an archive with a structure similar to the one described in [Cloud Manager dispatcher configuration](https://docs.adobe.com/content/help/en/experience-manager-cloud-manager/using/getting-started/dispatcher-configurations.html)

### Extract the archive and remove an eventual prefix

Extract the archive to a folder, and make sure the immediate subfolders start with `conf`, `conf.d`,
 `conf.dispatcher.d` and `conf.modules.d`. If they don't, move them up in the hierarchy.

### Get rid of ununsed subfolders and files

Remove subfolders `conf` and `conf.modules.d`, as well as files matching `conf.d/*.conf`.

### Get rid of all non-publish virtual hosts

Remove any virtual host file in `conf.d/enabled_vhosts` that has `author`, `unhealthy`, `health`,
`lc` or `flush` in its name. All virtual host files in `conf.d/available_vhosts` that are not
linked to can be removed as well.

### Remove or comment virtual host sections that do not refer to port 80

If you still have sections in your virtual host files that exclusively refer to other ports than port 80, e.g.

```
<VirtualHost *:443>
...
</VirtualHost>
```

remove or comment them. Statements in these sections will not get processed, but if you
keep them around, you might still end up editing them with no effect, which is confusing.

### Check rewrites

Enter directory `conf.d/rewrites`.

Remove any file named `base_rewrite.rules` and `xforwarded_forcessl_rewrite.rules` and remember to
remove `Include` statements in the virtual host files referring to them.

If `conf.d/rewrites` now contains a single file, it should be renamed to `rewrite.rules` and don't
forget to adapt the `Include` statements referring to that file in the virtual host files as well. 

If the folder however contains multiple, virtual host specific files, their contents should be
copied to the `Include` statement referring to them in the virtual host files.

### Check variables

Enter directory `conf.d/variables`.

Remove any file named `ams_default.vars` and remember to remove `Include` statements in the virtual
host files referring to them. 

If `conf.d/variables` now contains a single file, it should be renamed to `custom.vars` and don't
forget to adapt the `Include` statements referring to that file in the virtual host files as well. 

If the folder however contains multiple, virtual host specific files, their contents should be
copied to the `Include` statement referring to them in the virtual host files.

### Remove allowlists

Remove the folder `conf.d/whitelists` and remove `Include` statements in the virtual host files referring to
some file in that subfolder.

### Replace any variable that is no longer available

In all virtual host files:

Rename `PUBLISH_DOCROOT` to `DOCROOT`
Remove sections referring to variables named `DISP_ID`, `PUBLISH_FORCE_SSL` or `PUBLISH_WHITELIST_ENABLED`

### Check your state by running the validator

Run the dispatcher validator in your directory, with the `httpd` subcommand:

```
$ validator httpd .
```

If you see errors about missing include files, check whether you correctly renamed those
files.

If you see Apache directives that are not allowlisted, remove them.

### Get rid of all non-publish farms

Remove any farm file in `conf.dispatcher.d/enabled_farms` that has `author`, `unhealthy`, `health`,
`lc` or `flush` in its name. All farm files in `conf.dispatcher.d/available_farms` that are not
linked to can be removed as well.

### Rename farm files

All farms in `conf.d/enabled_farms` must be renamed to match the pattern `*.farm`, so e.g. a 
farm file called `customerX_farm.any` should be renamed `customerX.farm`. 

### Check cache

Enter directory `conf.dispatcher.d/cache`.

Remove any file prefixed `ams_`. 

If `conf.dispatcher.d/cache` is now empty, copy the file `conf.dispatcher.d/cache/rules.any`
from the standard dispatcher configuration to this folder. The standard dispatcher
configuration can be found in the folder `src` of this SDK. Don't forget to adapt the
`$include` statements referring to the `ams_*_cache.any` rule files  in the farm files
as well. 

If instead `conf.dispatcher.d/cache` now contains a single file with suffix `_cache.any`,
it should be renamed to `rules.any` and don't forget to adapt the `$include` statements
referring to that file in the farm files as well. 

If the folder however contains multiple, farm specific files with that pattern, their contents
should be copied to the `$include` statement referring to them in the farm files.

Remove any file that has the suffix `_invalidate_allowed.any`.

Copy the file `conf.dispatcher.d/cache/default_invalidate_any` from the default
AEM in the Cloud dispatcher configuration to that location.

In each farm file, remove any contents in the `cache/allowedClients` section and replace it
with:

```
$include "../cache/default_invalidate.any"
```

### Check client headers

Enter directory `conf.dispatcher.d/clientheaders`.

Remove any file prefixed `ams_`. 

If `conf.dispatcher.d/clientheaders` now contains a single file with suffix `_clientheaders.any`,
it should be renamed to `clientheaders.any` and don't forget to adapt the `$include` statements
referring to that file in the farm files as well. 

If the folder however contains multiple, farm specific files with that pattern, their contents
should be copied to the `$include` statement referring to them in the farm files.

Copy the file `conf.dispatcher/clientheaders/default_clientheaders.any` from the default
AEM as a Cloud Service dispatcher configuration to that location.

In each farm file, replace any clientheader include statements that looks as follows:

```
$include "/etc/httpd/conf.dispatcher.d/clientheaders/ams_publish_clientheaders.any"
$include "/etc/httpd/conf.dispatcher.d/clientheaders/ams_common_clientheaders.any"
```

with the statement:

```
$include "../clientheaders/default_clientheaders.any"
```

### Check filter

Enter directory `conf.dispatcher.d/filters`.

Remove any file prefixed `ams_`. 

If `conf.dispatcher.d/filters` now contains a single file it should be renamed to
`filters.any` and don't forget to adapt the `$include` statements referring to that
file in the farm files as well. 

If the folder however contains multiple, farm specific files with that pattern, their contents
should be copied to the `$include` statement referring to them in the farm files.

Copy the file `conf.dispatcher/filters/default_filters.any` from the default
AEM as a Cloud Service dispatcher configuration to that location.

In each farm file, replace any filter include statements that looks as follows:

```
$include "/etc/httpd/conf.dispatcher.d/filters/ams_publish_filters.any"
```

with the statement:

```
$include "../filters/default_filters.any"
```

### Check renders

Enter directory `conf.dispatcher.d/renders`.

Remove all files in that folder.

Copy the file `conf.dispatcher.d/renders/default_renders.any` from the default
AEM as a Cloud Service dispatcher configuration to that location.

In each farm file, remove any contents in the `renders` section and replace it
with:

```
$include "../renders/default_renders.any"
```

### Check virtualhosts

Rename the directory `conf.dispatcher.d/vhosts` to `conf.dispatcher.d/virtualhosts` and enter it.

Remove any file prefixed `ams_`. 

If `conf.dispatcher.d/virtualhosts` now contains a single file it should be renamed to
`virtualhosts.any` and don't forget to adapt the `$include` statements referring to that
file in the farm files as well. 

If the folder however contains multiple, farm specific files with that pattern, their contents
should be copied to the `$include` statement referring to them in the farm files.

Copy the file `conf.dispatcher/virtualhosts/default_virtualhosts.any` from the default
AEM as a Cloud Service dispatcher configuration to that location.

In each farm file, replace any filter include statements that looks as follows:

```
$include "/etc/httpd/conf.dispatcher.d/vhosts/ams_publish_vhosts.any"
```

with the statement:

```
$include "../virtualhosts/default_virtualhosts.any"
```

### Check your state by running the validator

Run the AEM as a Cloud Service dispatcher validator in your directory, with the `dispatcher` subcommand:

```
$ validator dispatcher .
```

If you see errors about missing include files, check whether you correctly renamed those
files.

If you see errors concerning undefined variable `PUBLISH_DOCROOT`, rename it to `DOCROOT`.

For every other error, see the Troubleshooting section of the
validator tool documentation.

### Test your configuration with a local deployment (requires Docker installation)

Using the script `docker_run.sh` in the AEM as a Cloud Service Dispatcher Tools, you can test that
your configuration does not contain any other error that would only show up in 
deployment:

### Step 1: Generate deployment information with the validator

```
validator full -d out .
```

This validates the full configuration and generates deployment information in `out`

### Step 2: Start the dispatcher in a docker image with that deployment information

With your AEM publish server running on your macOS computer, listening on port 4503,
you can run start the dispatcher in front of that server as follows:

``` 
$ docker_run.sh out docker.for.mac.localhost:4503 8080
```

This will start the container and expose Apache on local port 8080.

### Use your new dispatcher configuration

Congratulations! If the validator no longer reports any issue and the
docker container starts up without any failures or warnings, you're
ready to move your configuration to a `dispatcher/src` subdirectory
of your git repository.

**Customers who are using AMS Dispatcher configuration version 1 should contact customer support to help them migrate from version 1 to version 2 so the instructions above can be followed.**
