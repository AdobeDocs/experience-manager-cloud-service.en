---
title: SecurBank Sample App for the Universal Editor
description: Learn about the Universal Editor with hands-on experience by using the SecurBank App, designed to showcase the power, flexibility, and usability of the Universal Editor to accelerate content creation.
---

# SecurBank Sample App for the Universal Editor {#securbank}

Learn about the Universal Editor with hands-on experience by using the SecurBank App, designed to showcase the power, flexibility, and usability of the Universal Editor to accelerate content creation.

## Introduction {#introduction}

## Installing SecurBank {#installation}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization

1. Create a new sandbox program for the SecurBank app.

   * Use the default options when selecting **Solutions &amp; Add-Ons**.
   * For details on how to create a sandbox program, please see the document [Creating Sandbox Programs.](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-sandbox-programs.md)

1. Once the program is created, open it and on the **Repositories** tab, tap or click the **Access Repo Info** button to open the **Repository Info** dialog and view the credentials necessary to access the git repository for the sandbox environment.

   * For details on how to access your repository information, please see the document [Accessing Repositories.](/help/implementing/cloud-manager/managing-code/accessing-repos.md) 

1. Using the credentials in the **Repository Info** dialog, clone the repository on your local machine.

1. Local the folder of the local clone, open it and delete all content except for the hidden/dot files.

1. Retrieve the latest SecurBank code from GitHub at [`https://github.com/Adobe-Marketing-Cloud/summit-2024-l425-securbank`](https://github.com/Adobe-Marketing-Cloud/summit-2024-l425-securbank) by clicking **Code** and then **Download ZIP** in the dropdown.

1. Decompress the contents of the zip file on your local file system and move it to the repository folder.

1. Using the terminal, switch to the folder of the git project commit all the content and push it to git.

   1. `git add --all`
   1. `git commit -m "Adding SecurBank app code"`
   1. `git push`

1. Return to your sandbox program in Cloud Manager and return to the **Overview** tab and run the full-stack non-production pipeline.

   * Uncheck all options for the pipeline run.
   * For more information about running pipelines, please see the document [Managing Pipelines.](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md#running-pipelines)

1. While the pipeline is running, on the **Overview** tab of your program in Cloud Manger, 