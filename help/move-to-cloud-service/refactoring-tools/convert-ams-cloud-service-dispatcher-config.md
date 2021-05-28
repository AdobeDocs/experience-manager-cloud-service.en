---
title: Converting an AMS to an Adobe Experience Manager as a Cloud Service Dispatcher Configuration
description: Converting an AMS to an Adobe Experience Manager as a Cloud Service Dispatcher Configuration
---

# Converting an AMS to an Adobe Experience Manager (AEM) as a Cloud Service Dispatcher Configuration

## Introduction {#introduction}

This section provides step by step instructions on how to convert an AMS configuration. 

>[!NOTE]
>It assumes that you have an archive with a structure similar to the one described in [Manage your Dispatcher Configurations](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/getting-started/dispatcher-configurations.html).

## Steps for Converting an AMS to AEM as a Cloud Service Dispatcher Configuration

1. **Extract the archive and remove an eventual prefix**

   Extract the archive to a folder, and make sure the immediate subfolders start with conf, conf.d, conf.dispatcher.d and conf.modules.d. If they don't, move them up in the hierarchy.

1. **Get rid of ununsed subfolders and files**

   Remove subfolders conf and conf.modules.d, as well as files matching conf.d/*.conf.

1. **Get rid of all non-publish virtual hosts**

1. **Remove any virtual host file**
   
    In conf.d/enabled_vhosts that has author, unhealthy, health, lc or flush in its name. All virtual host files in conf.d/available_vhosts that are not linked to can be removed as well.

1. Remove or comment virtual host sections that do not refer to port 80

   If you still have sections in your virtual host files that exclusively refer to other ports than port 80, e.g.

   `<VirtualHost *:443>`
    `...`
    `</VirtualHost>`
   remove or comment them. Statements in these sections will not get processed, but if you keep them around, you might still end up editing them with no effect, which is confusing.

1. **Check rewrites**

   * Enter directory conf.d/rewrites.

   * Remove any file named base_rewrite.rules and xforwarded_forcessl_rewrite.rules and remember to remove Include statements in the virtual host files referring to them.

   * If conf.d/rewrites now contains a single file, it should be renamed to rewrite.rules and don't forget to adapt the Include statements referring to that file in the virtual host files as well.

   * If the folder however contains multiple, virtual host specific files, their contents should be copied to the Include statement referring to them in the virtual host files.

1. **Check variables**

   1. Enter directory conf.d/variables.

   1. Remove any file named ams_default.vars and remember to remove Include statements in the virtual host files referring to them.

   1. If conf.d/variables now contains a single file, it should be renamed to custom.vars and don't forget to adapt the Include statements referring to that file in the virtual host files as well.

   1. If the folder however contains multiple, virtual host specific files, their contents should be copied to the Include statement referring to them in the virtual host files.

1. **Remove whitelists**

   Remove the folder conf.d/whitelists and remove Include statements in the virtual host files referring to some file in that subfolder.

1. **Replace any variable that is no longer available**

   In all virtual host files:

   Rename PUBLISH_DOCROOT to DOCROOT
   Remove sections referring to variables named DISP_ID, PUBLISH_FORCE_SSL or PUBLISH_WHITELIST_ENABLED

1. **Check your state by running the validator**

    Run the dispatcher validator in your directory, with the httpd subcommand:

    `$ validator httpd`
    If you see errors about missing include files, check whether you correctly renamed those files.

    If you see Apache directives that are not whitelisted, remove them.

1. **Get rid of all non-publish farms**

     Remove any farm file in conf.dispatcher.d/enabled_farms that has author, unhealthy, health, lc or flush in its name. All farm files in conf.dispatcher.d/available_farms that are not linked to can be removed as well.

1. **Rename farm files**

     All farms in conf.dispatcher.d/enabled_farms must be renamed to match the pattern *.farm, so e.g. a farm file called customerX_farm.any should be renamed customerX.farm.

1. **Check cache**

     Enter directory conf.dispatcher.d/cache.

     Remove any file prefixed ams_.

     If conf.dispatcher.d/cache is now empty, copy the file conf.dispatcher.d/cache/rules.any from the standard dispatcher configuration to this folder. The standard dispatcher configuration can be found in the folder src of this SDK. Don't forget to adapt the $include statements referring to the ams_*_cache.any rule files in the farm files as well.

    If instead conf.dispatcher.d/cache now contains a single file with suffix _cache.any, it should be renamed to rules.any and don't forget to adapt the $include statements referring to that file in the farm files as well.

    If the folder however contains multiple, farm specific files with that pattern, their contents should be copied to the $include statement referring to them in the farm files.

    Remove any file that has the suffix _invalidate_allowed.any.

    Copy the file conf.dispatcher.d/cache/default_invalidate_any from the default dispatcher configuration to that location.

    In each farm file, remove any contents in the cache/allowedClients section and replace it with:

    $include "../cache/default_invalidate.any"

1. **Check client headers**

   Enter directory conf.dispatcher.d/clientheaders.

   Remove any file prefixed ams_.

   If conf.dispatcher.d/clientheaders now contains a single file with suffix _clientheaders.any, it should be renamed to clientheaders.any and don't forget to adapt the $include statements referring to that file in the farm files as well.

   If the folder however contains multiple, farm specific files with that pattern, their contents should be copied to the $include statement referring to them in the farm files.

   Copy the file conf.dispatcher/clientheaders/default_clientheaders.any from the default dispatcher configuration to that location.

   In each farm file, replace any clientheader include statements that looks as follows:

    `$include "/etc/httpd/conf.dispatcher.d/clientheaders/ams_publish_clientheaders.any"`

    `$include "/etc/httpd/conf.dispatcher.d/clientheaders/ams_common_clientheaders.any"`
    
    with the statement:

    `$include "../clientheaders/default_clientheaders.any"`

1. **Check filter**

   * Enter directory conf.dispatcher.d/filters.

   * Remove any file prefixed ams_.

   * If conf.dispatcher.d/filters now contains a single file it should be renamed to filters.any and don't forget to adapt the $include statements referring to that file in the farm files as well.

   * If the folder however contains multiple, farm specific files with that pattern, their contents should be copied to the $include statement referring to them in the farm files.

   * Copy the file conf.dispatcher/filters/default_filters.any from the default dispatcher configuration to that location.

   * In each farm file, replace any filter include statements that looks as follows:

   * $include `"/etc/httpd/conf.dispatcher.d/filters/ams_publish_filters.any"`
    with the statement:

     `$include "../filters/default_filters.any"`

1. **Check renders**

   * Enter directory conf.dispatcher.d/renders.

   * Remove all files in that folder.

   * Copy the file conf.dispatcher.d/renders/default_renders.any from the default dispatcher configuration to that location.

   * In each farm file, remove any contents in the renders section and replace it with:

     `$include "../renders/default_renders.any"`

1. **Check virtualhosts**

   * Rename the directory `conf.dispatcher.d/vhosts to conf.dispatcher.d/virtualhosts` and enter it.

   * Remove any file prefixed `ams_`.

    * If conf.dispatcher.d/virtualhosts now contains a single file it should be renamed to virtualhosts.any and don't forget to adapt the $include statements referring to that file in the farm files as well.

    * If the folder however contains multiple, farm specific files with that pattern, their contents should be copied to the $include statement referring to them in the farm files.

    * Copy the file conf.dispatcher/virtualhosts/default_virtualhosts.any from the default dispatcher configuration to that location.

    * In each farm file, replace any filter include statements that looks as follows:

      `$include "/etc/httpd/conf.dispatcher.d/vhosts/ams_publish_vhosts.any"`
     with the statement:

      `$include "../virtualhosts/default_virtualhosts.any"`


1. **Check your state by running the validator**

    * Run the dispatcher validator in your directory, with the dispatcher subcommand:

      `$ validator dispatcher`

    * If you see errors about missing include files, check whether you correctly renamed those files.

    * If you see errors concerning undefined variable `PUBLISH_DOCROOT`, rename it to `DOCROOT`.

    * For every other error, see the Troubleshooting section of the validator tool documentation.

## Testing your configuration with a local deployment {#testing-config-local-deployment}

>[!IMPORTANT]
>
>The testing of your configuration with a local deployment requires Docker installation.

Using the script `docker_run.sh` in the Dispatcher SDK, you can test that your configuration does not contain any other error that would only show up in deployment:

1. Generate deployment information with the validator

   `validator full -d out`
   This validates the full configuration and generates deployment information in out

1. Start the dispatcher in a docker image with that deployment information

   With your AEM publish server running on your macOS computer, listening on port 4503, you can run start the dispatcher in front of that server as follows:

   `$ docker_run.sh out docker.for.mac.localhost:4503 8080`

   This will start the container and expose Apache on local port 8080.

## Using your new dispatcher configuration {#using-dispatcher-config}

If the validator no longer reports any issue and the docker container starts up without any failures or warnings, you are ready to move your configuration to a d`ispatcher/src` subdirectory of your git repository.