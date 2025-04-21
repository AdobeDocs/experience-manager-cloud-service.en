---
title: Getting Started with Refactoring Tools
description: Learn how to get started with Refactoring Tools in AEM as a Cloud Service
---
# Getting Started with Refactoring Tools {#getting-started-refactoring-tools}

## Availability {#availability}

<!-- Alexandru: duplicate contextualhelp id, drafting this for now

>[!CONTEXTUALHELP]
>id="aemcloud_rs_upload"
>title="Download"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/release-notes/release-notes/release-notes-current.html" text="Release Notes"
>additional-url="https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html" text="Software Distribution Portal"

-->

## Running the Refactoring Tools {#running-refactoring-tools}

Use the Refactoring Tool to migrate your code for compatibility with AEM as a Cloud Service.

1. If you haven’t created a CAM project yet, refer to [Creating and Managing a Project in CAM](/help/journey-migration/cloud-acceleration-manager/using-cam/getting-started-cam.md#create-project).
1. Click the **Code Refactoring** card to upload the source code.

   ![image](/help/journey-migration/refactoring-tools/assets/rscam1.png)

1. When you first access the **Source Code View**, you will see an empty state prompting you to upload your source code.

   ![image](/help/journey-migration/refactoring-tools/assets/rscam2.png)

---

## Uploading Source Code {#uploading}

When customers first access the **Refactoring Tools**, they are presented with an empty state in the **Source Code View**. Follow the steps below to upload your project and begin the inspection process:

1. **Access the Project Upload Page**  
   Click on the **Project Upload** button in the empty state to start the upload process.

   ![image](/help/journey-migration/refactoring-tools/assets/rscam3.png)

1. **Upload Your Source Code**
    - In the upload dialog, select your source code ZIP file.
    - Click **Upload** to begin.
    - The upload progress will be displayed in the dialog. Duration depends on your project's size.

   ![image](/help/journey-migration/refactoring-tools/assets/rscam4.png)

1. **Inspection Process**
    - After uploading, the **Inspection Process** begins automatically in the background.
    - The **Source Code View** will now display your uploaded project and its inspection status.

1. **Inspection Status**  The inspection process is designed to simplify the execution of refactoring tools by reducing the overhead of manual configurations.

   The inspection will show one of the following statuses:
    - **Running** – The inspection is in progress.
    - **Ready** – The inspection is complete; you may now run refactoring tools.
    - **Failed** – An error occurred. Click the project to review the inspection report and resolve any issues.

   ![image](/help/journey-migration/refactoring-tools/assets/rscam5.png)

>[!NOTE]
>Uploading a new project will delete the existing one. Ensure any necessary data is saved before proceeding.

>[!NOTE]
>Refactoring jobs can only be executed if the source code upload is successful.

---

## Refactoring Jobs {#refactoring-jobs}

When you click the **Refactoring Job** tab, you will see a list of existing jobs. If no jobs have been created yet, an empty state will be displayed prompting job creation.

![image](/help/journey-migration/refactoring-tools/assets/rscam6.png)

### 1. Create a New Refactoring Job

- Click the **Create New Job** button.
- Select the desired refactoring tool(s).
- Click **Start** to initiate the refactoring process.

![image](/help/journey-migration/refactoring-tools/assets/rscam7.png)

>[!NOTE]
>You can trigger individual refactoring jobs or execute all available tools in one go using the **All Tools Together** option.

---

### 2. Job Status

- **Running** – The job is currently in progress. Status updates automatically upon completion or failure.
- **Completed** – The job finished successfully. You can now review results or download the refactored code.
- **Failed** – The job encountered an error. Click on the job to view detailed logs and troubleshoot the issue.

![image](/help/journey-migration/refactoring-tools/assets/rscam8.png)

When the job is completed successfully, the **Download** button becomes available, allowing you to retrieve:

- **The Refactored Project**: This is the updated code after the transformation is applied. Customers can download the latest code for their project.
- **Activity Logs**: During the job execution, all steps performed by the tool and the changes made are logged as part of this.
- **Findings Report**: This report contains items that were not fully executed by the tool but still need to be addressed. All such changes are logged here.

![image](/help/journey-migration/refactoring-tools/assets/rscam9.png)

>[!NOTE]
>Each job can take up to 1 hour to complete. If the status is not updated, please contact Adobe Support.

