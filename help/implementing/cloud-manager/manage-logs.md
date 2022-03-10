---
title: Accessing and Managing Logs
description: Learn how to access and manage logs to aid your development process in AEM as a Cloud Service.
exl-id: f17274ce-acf5-4e7d-b875-75d4938806cd
---

# Accessing and Managing Logs {#manage-logs} 

Learn how to access and manage logs to aid your development process in AEM as a Cloud Service.

You can access a list of available log files for the selected environment using the **Environments** card from the **Overview** page or Environment Details page.

## Downloading Logs {#download-logs}

Follow these steps to download logs.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Environments** card from the **Overview** page.

1. Select **Download Logs** from the ellipsis menu.

   ![Download logs menu item](assets/download-logs1.png)

1. In the **Download Logs** dialog, select the appropriate **Service** from the drop-down menu

   ![Download Logs dialog](assets/download-preview.png)

1. Once you select your service, click the download icon next to the log you wish to retrieve.

You can also access your logs from the **Environments** page.

![Logs from the Environments screen](assets/download-logs.png)

## Logs Via API {#logs-through-api}

In addition to downloading logs through the UI, logs are available through the API and the command line interface. 

To download the log files for a specific environment, the command would be similar to the following.

```shell
$ aio cloudmanager:download-logs --programId 5 1884 author aemerror
```

You can also tail logs via the command line interface.

```shell
$ aio cloudmanager:tail-log --programId 5 1884 author aemerror
```

In order to obtain the environment Id (1884 in this example) and the available service or log name options you can use the following commands.

```shell
$ aio cloudmanager:list-environments
Environment Id Name                     Type  Description                          
1884           FoundationInternal_dev   dev   Foundation Internal Dev environment  
1884           FoundationInternal_stage stage Foundation Internal STAGE environment
1884           FoundationInternal_prod  prod  Foundation Internal Prod environment
 
 
$ aio cloudmanager:list-available-log-options 1884
Environment Id Service    Name         
1884           author     aemerror     
1884           author     aemrequest   
1884           author     aemaccess    
1884           publish    aemerror     
1884           publish    aemrequest   
1884           publish    aemaccess    
1884           dispatcher httpderror   
1884           dispatcher aemdispatcher
1884           dispatcher httpdaccess
```

### Additional Resources {#resources}

Refer to the following additional resources to learn more about the Cloud Manager API and Adobe I/O CLI:

* [Cloud Manager API Documentation](https://www.adobe.io/apis/experiencecloud/cloud-manager/docs.html)
* [Adobe I/O CLI](https://github.com/adobe/aio-cli-plugin-cloudmanager)
