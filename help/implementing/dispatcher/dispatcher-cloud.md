---
title: Dispatcher in the Cloud
seo-title: Dispatcher in the Cloud
description: Dispatcher in the Cloud 
seo-description: Dispatcher in the Cloud 
---

# Dispatcher in the Cloud {#Dispatcher-in-the-cloud}

## Apache and Dispatcher configuration and testing {#apache-and-dispatcher-configuration-and-testing}

This section describes how to structure the AEM as a Cloud Service Apache and Dispatcher configuration, as well as how to validate  and run it locally before deploying to Cloud environments. It also describes debugging in Cloud environments. For additional information about Dispatcher, see the [AEM Dispatcher documentation](https://docs.adobe.com/content/help/en/experience-manager-dispatcher/using/dispatcher.html).

>[!NOTE]
>Windows users will need to use Windows 10 Professional or other distributions that support Docker. This is a pre-requisite for running and debugging Dispatcher on a local computer. The sections below include commands using the Mac or Linux versions of the SDK, but the Windows SDK can be used in a similar way.

## Dispatcher SDK {#dispatcher-sdk}

The Dispatcher SDK provides:

* A vanilla file structure containing the configuration files to include in a maven project for dispatcher;
* Tooling for customers to validate a dispatcher configuration locally;
* A Docker image that brings up the dispatcher locally.

## Downloading and extracting the SDK {#extracting-the-sdk}

The Dispatcher SDK can be downloaded from the Software Distribution portal at the URL ??? from a folder corresponding to the desired AEM version. Any new configuration available in that new dispatcher SDK version can be used to deploy to Cloud environments running that version of AEM in the Cloud or higher.  

**For macOS and Linux**, download the shell script to a folder on your machine, make it executable and run it. It will self extract the Dispatcher SDK files underneath the directory you stored it to (where <version> is the version of the dispatcher SDK).

```bash
$ chmod +x DispatcherSDKv<version>.sh
$ ./DispatcherSDKv<version>.sh
Verifying archive integrity...  100%   All good.
Uncompressing DispatcherSDKv<version>  100% 
```

**For Windows**, download the zip archive and extract it.

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
It is recommended that the above files reference the unmodifiable files listed below, followed by any additional statements or overrides. When dispatcher configuration is deployed to a cloud environment, the latest version of the unmodifiable files will be used, regardless of what version was used in local development.

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

>[!NOTE]The AEM as a Cloud Service maven archetype will generate the same dispatcher configuration file structure.

The sections below describe how to validate the configuration locally so it can pass the associated quality gate in Cloud Manager when deploying an internal release.

## Local validation of Dispatcher configuration {#local-validation-of-dispatcher-configuration}

The validation tool is available in the SDK at `bin/validator` as a Mac OS, Linux, or Windows binary, allowing customers to run the same validation that Cloud Manager will perform while building and deploying a release.

It is invoked as: `validator full [-d folder] [-w whitelist] zip-file | src folder`

The tool validates the Apache and dispatcher configuration. It scans all files with pattern `conf.d/enabled_vhosts/*.vhost` and checks that only whitelisted directives are used. The directives allowed in Apache configuration files can be listed by running the validator's whitelist command:

```

$ validator whitelist
Cloud manager validator 2.0.4
 
Whitelisted directives:
  <Directory>
  ...
  
  ```

The table below shows the supported apache modules:

| Maintenance Task | Who owns the configuration |
|---|---|
| core | [https://httpd.apache.org/docs/2.4/mod/core.html](https://httpd.apache.org/docs/2.4/mod/core.html) |
| mod_access_compat | [https://httpd.apache.org/docs/2.4/mod/mod_access_compat.html](https://httpd.apache.org/docs/2.4/mod/mod_access_compat.html) |
| mod_alias | [https://httpd.apache.org/docs/2.4/mod/mod_alias.html](https://httpd.apache.org/docs/2.4/mod/mod_alias.html) |
| mod_allowmethods | [https://httpd.apache.org/docs/2.4/mod/mod_allowmethods.html](https://httpd.apache.org/docs/2.4/mod/mod_allowmethods.html) |
| mod_auth_basic | [https://httpd.apache.org/docs/2.4/mod/mod_auth_basic.html](https://httpd.apache.org/docs/2.4/mod/mod_auth_basic.html) |
| mod_authn_core | [https://httpd.apache.org/docs/2.4/mod/mod_authn_core.html](https://httpd.apache.org/docs/2.4/mod/mod_authn_core.html) |
| mod_authn_file | [https://httpd.apache.org/docs/2.4/mod/core.html](https://httpd.apache.org/docs/2.4/mod/mod_authn_file.html) |
| mod_authz_core | [https://httpd.apache.org/docs/2.4/mod/core.html](https://httpd.apache.org/docs/2.4/mod/mod_authz_core.html) |
| mod_authz_groupfile | [https://httpd.apache.org/docs/2.4/mod/mod_authz_groupfile.html](https://httpd.apache.org/docs/2.4/mod/mod_authz_groupfile.html) |
| mod_deflate | [https://httpd.apache.org/docs/2.4/mod/mod_deflate.html](https://httpd.apache.org/docs/2.4/mod/mod_deflate.html) |
| mod_dir | [https://httpd.apache.org/docs/2.4/mod/mod_dir.html](https://httpd.apache.org/docs/2.4/mod/mod_dir.html) |
| mod_env | [https://httpd.apache.org/docs/2.4/mod/mod_env.html](https://httpd.apache.org/docs/2.4/mod/mod_env.html) |
| mod_filter | [https://httpd.apache.org/docs/2.4/mod/mod_filter.html](https://httpd.apache.org/docs/2.4/mod/mod_filter.html) |
| mod_headers | [https://httpd.apache.org/docs/2.4/mod/mod_headers.html](https://httpd.apache.org/docs/2.4/mod/mod_headers.html) |
| mod_mime | [https://httpd.apache.org/docs/2.4/mod/mod_mime.html](https://httpd.apache.org/docs/2.4/mod/mod_mime.html) |
| mod_remoteip | [https://httpd.apache.org/docs/2.4/mod/mod_remoteip.html](https://httpd.apache.org/docs/2.4/mod/mod_remoteip.html) |
| mod_reqtimeout | [https://httpd.apache.org/docs/2.4/mod/mod_reqtimeout.html](https://httpd.apache.org/docs/2.4/mod/mod_reqtimeout.html) |
| mod_rewrite | [https://httpd.apache.org/docs/2.4/mod/mod_rewrite.html](https://httpd.apache.org/docs/2.4/mod/mod_rewrite.html) |
| mod_security | [https://modsecurity.org/](https://modsecurity.org/) |
| mod_setenvif | [https://httpd.apache.org/docs/2.4/mod/mod_setenvif.html](https://httpd.apache.org/docs/2.4/mod/mod_setenvif.html) |
| mod_substitute | [https://httpd.apache.org/docs/2.4/mod/mod_substitute.html](https://httpd.apache.org/docs/2.4/mod/mod_substitute.html) |
| mod_userdir| [https://httpd.apache.org/docs/2.4/mod/mod_userdir.html](https://httpd.apache.org/docs/2.4/mod/mod_userdir.html) |


Customers cannot add arbitrary modules, however additional modules may be considered for inclusion in the product in the future. Customers can find the list of directives available for a given Dispatcher version by executing "validator whitelist" in the SDK, as described in Dispatcher SDK documentation.

The whitelist contains a list of Apache directives that are permitted in a customer configuration. If a directive is not whitelisted,the tool logs an error and returns a non-zero exit code. If no whitelist is given on the command line (which is the way it should be invoked), the tool uses a default whitelist that Cloud Manager will use for validation before deploying to Cloud environments.

 Also, it further scans all files with pattern `conf.dispatcher.d/enabled_farms/*.farm` and checks that:

* No filter rule exists that uses allows via `/glob` (see [CVE-2016-0957](https://nvd.nist.gov/vuln/detail/CVE-2016-0957) for more details)
* No admin feature is exposed. For example, access to paths such as `/crx/de or /system/console`. 

When run against your maven artifact or your `dispatcher/src` subdirectory, it will report validation failures:

 ```

$ validator full dispatcher/src
Cloud manager validator 1.0.4
2019/06/19 15:41:37 Apache configuration uses non-whitelisted directives:
  conf.d/enabled_vhosts/aem_publish.vhost:46: LogLevel
2019/06/19 15:41:37 Dispatcher configuration validation failed:
  conf.dispatcher.d/enabled_farms/999_ams_publish_farm.any: filter allows access to CRXDE

```

Note that the validation tool reports only the prohibited use of Apache directives that have not been whitelisted. It does not report syntactical or semantical problems with your Apache configuration, as this information is only available to Apache modules in a running environment.

When no validation failures are reported, your configuration is ready for deployment.

## Testing your Apache and Dispatcher configuration locally {#testing-apache-and-dispatcher-configuration-locally}

It is also possible to test drive your Apache and Dispatcher configuration locally. It requires Docker to be installed locally and your configuration to pass the validation as described above.

By using the "`-d`" parameter, the validator outputs a folder with all the configuration files needed by the dispatcher.

Then, the `docker_run.sh` script can point to that folder, starting the container with your configuration.

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

The following strategy can be used to increase the log output for the dispatcher module and see the result of the `RewriteRule` evaluation in both local and cloud environments.

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

When running the Dispatcher locally, logs are also directly printed to the terminal output. Most of the time, these logs should be in DEBUG, which can be accomplished by passing in the Debug level as a parameter when running Docker. For example: 

`DISP_LOG_LEVEL=Debug ./bin/docker_run.sh out docker.for.mac.localhost:4503 8080`

Logs for cloud environments will be exposed through the logging service available in Cloud Manager.

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

### Remove whitelists

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

If you see Apache directives that are not whitelisted, remove them.

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

Using the script `docker_run.sh` in the AEM as a Cloud Service Dispatcher SDK, you can test that
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

## Dispatcher and CDN {#dispatcher-cdn}

The data flow is as follows:

1. URL put in browser
2. Request made to CDN mapped in DNS to that domain
3. If content is fully cached on CDN, CDN serves it to the browser
4. If content is not fully cached, the CDN calls out (reverse proxy) to the dispatcher
5. If content is fully cached on dispatcher, dispatcher serves it to the CDN
6. If content is not fully cached, the dispatcher calls out (reverse proxy) to the AEM publish
7. Content rendered by browser

### CDN {#cdn}

AEM offers two options:

1. Managed CDN - AEM's out-of-the-box CDN.
2. Unmanaged CDN - Customer brings their own CDN and is entirely responsible for managing it.

The first option is highly recommended and Adobe is not responsible for the result of any misconfiguration when using the second option.

#### Managed CDN  {#managed-cdn}

After Adobe provisions the CDN, you should create a CNAME, mapping your application's domains to an Adobe controlled domain hosted at the managed CDN domain.

The CDN acts as a layer 7 web application firewall, which requires SSL termination, hence it will need a customer-signed SSL certificate. During the pre-release phase, you have to provide the certificate to Adobe through manual processes.

At the time of GA, you should upload the certificate to Cloud Manager, which will in turn upload it to the CDN. When SSL certificates are expiring, you will be notified so you can refresh the certificates in Cloud Manager.

#### Unmanaged CDN {#unmanaged-cdn}

You may manage your own CDN, provided:

1. You have an existing CDN. 
2. You will manage it.
3. Your application does not make extensive API calls to the CDN that are not already accommodated in AEM architecture.
4. AEM as a Cloud Service is able to establish that the end-to-end system functions properly.
5. You will need to provide Adobe with the whitelist of CDN urls to allow.

Adobe will provide a AEM Cloud url for to use as your CDN's origin. 


#### CDN cache invalidation {#CDN-cache-invalidation}

Cache invalidation follows these rules:

* In general, HTML content is cached in the CDN for 5 minutes, based on the cache-control header emitted by the dispatcher.
* Client libraries (JavaScript and CSS) are cached indefinitely using the cache-control set to either immutable or 30 days for older browsers which don't respect the immutable value. Note that the client libraries are served on a unique path that changes if the client libraries change. In other words, HTML that references the client libraries will be produced as needed so you can experience new content as it is published.
* By default, images are not cached.

## Explicit dispatcher cache invalidation {#explicit-invalidation}

Prior to AEM as a Cloud Service, there were 2 ways of invalidating the dispatcher cache.

1. Invoke the replication API, specifying the publish dispatcher flush agent
2. Directly calling the `invalidate.cache` API (e.g. POST /dispatcher/invalidate.cache)

The `invalidate.cache` approach will no longer be supported since it addresses only a specific dispatcher node.
AEM as a Cloud Service operates at the service level, not the individual node level and thus the invalidation instructions in the [Dispatcher Help](https://docs.adobe.com/content/help/en/experience-manager-dispatcher/using/dispatcher.html) documentation are no longer accurate. 
Instead, the replication API approach should be used. [API documentation](https://helpx.adobe.com/experience-manager/6-5/sites/developing/using/reference-materials/javadoc/com/day/cq/replication/Replicator.html) is available and for an example of flushing the cache, see the [API example page](https://helpx.adobe.com/experience-manager/using/aem64_replication_api.html) and specifically the CustomStep example issuing a replication action of type ACTIVATE to all available agents. 

The diagram below illustrates this.

<!-- [CDN](assets/cdn.png "CDN") -->

<!-- See [Apache and Dispatcher Configuration and Testing](../developing/introduction/developer-experience.md#apache-and-dispatcher-configuration-and-testing) for instructions on how a developer can configure apache and the dispatcher module. -->

### Dispatcher Cache Invalidation during Activation/Deactivation {#cache-activation-deactivation}

This publish-triggered invalidation is the same as quickstart:
When the publish instance receives a new version of a page or asset from the author (via the replication and pipeline queue), it uses the flush agent to invalidate appropriate paths on its dispatcher. The updated path is removed from the dispatcher cache, together with its parents, up to some level that you can configure with the [statfileslevel](https://docs.adobe.com/content/help/en/experience-manager-dispatcher/using/configuring/dispatcher-configuration.html#invalidating-files-by-folder-level).

### Content Freshness and Version Consistency {#content-consistency}

* Pages are made of HTML, Javascript, CSS, and images.
* You are encouraged to leverage the clientlibs framework to import Javascript and CSS resources into HTML pages, taking into account dependencies between JS libraries.
* Automatic version management is provided, meaning that developers can check in changes to JS libraries in source control, and the latest version will be made available when a release is pushed. Without this, developers would need to manually change HTML with references to the new version of the library, which is especially onerous if many HTML templates share the same library.
* When the new versions of libraries are released to production, the referencing HTML pages are updated with new links to those updated library versions. Once the browser cache has expired for a given HTML page, there is no concern that the old libraries will be loaded from the browser cache since the refreshed page (from AEM) now is guaranteed to reference the new versions of the libraries. In other words, a refreshed HTML page will include all the latest library versions.
