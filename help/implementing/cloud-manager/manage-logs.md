---
title: Manage Logs - Cloud Service
description: Manage Logs - Cloud Service
exl-id: f17274ce-acf5-4e7d-b875-75d4938806cd
---
# Accessing and Managing Logs {#manage-logs} 

Users can access a list of available log files for the selected environment using the **Environments** card from the **Overview** page or Environment Details page.

## Downloading Logs {#download-logs}

Follow the steps below to download logs. 

1. Navigate to the **Environments** card from the **Overview** page.

1. Select **Download Logs** from the **...** menu.

   ![](assets/download-logs1.png)

   *Or*, 
   
    From the Environment Details page:

    ![](assets/download-logs.png)

   >[!NOTE]
   >Regardless of where it is opened, the same dialog appears and allows for an individual log file to be downloaded.

1. From the **Service** drop-down menu, select options such as **Preview** or **Preview Dispatcher**, followed by clicking on the download icon. 

   ![](assets/download-preview.png)


## Logs through API {#logs-through-api}

In addition to downloading logs through the UI, logs will be available through the API and the Command Line Interface. 

For example, to download the log files for a specific environment, the command would be something along the lines of

```java
$ aio cloudmanager:download-logs --programId 5 1884 author aemerror
```

The following command allows the tailing of logs:

```java
$ aio cloudmanager:tail-log --programId 5 1884 author aemerror
```

In order to obtain the environment Id (1884 in this case) and the available service or log name options you can use:

```java
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

>[!NOTE]
>While **Log Downloads** will be available through both the UI and API, **Log Tailing** is API/CLI-only.

### Additional Resources {#resources}

Refer to the following additional resources to learn more about the Cloud Manager API and Adobe I/O CLI:

* [Cloud Manager API Documentation](https://www.adobe.io/apis/experiencecloud/cloud-manager/docs.html)
* [Adobe I/O CLI](https://github.com/adobe/aio-cli-plugin-cloudmanager)
