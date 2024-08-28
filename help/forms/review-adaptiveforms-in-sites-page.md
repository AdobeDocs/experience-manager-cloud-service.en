---
title: How to send an adaptive form for review? How to manage reviews for an aem adaptive form?
description: Review is a mechanism that allows reviewer to perform different tasks for adaptive forms using Assign Task step.
feature: Adaptive Forms
hide: yes
hidefromtoc: yes
role: User
exl-id: e53535a8-cd6b-4f30-9523-773243098757
---
# Create and manage reviews for an Adaptive Form {#review-step-forms-aem-sites-page}

Using the [Assign step](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/create-form-centric-workflows/aem-forms-workflow-step-reference.html#assign-task-step) of the AEM workflow, the reviewer reviews the submitted form and performs action on it. To review the submitted form using the Assign task step, follow these steps:

1. [Create an AEM workflow](#create-an-aem-workflow)
1. [Configure the submit action of Adaptive Form container](#configure-submit-action)
1. [Submit an Adaptive form after review](#submit-af-after-review) 

## Create an AEM workflow {#create-an-aem-workflow}

1. Open your author instance in edit mode.
1. Go to **[!UICONTROL Tools]** >  **[!UICONTROL Workflow]** >  **[!UICONTROL Models]** > **[!UICONTROL Create]** > **[!UICONTROL Create Model]**
1. Specify the Title of workflow and add the **[Assign task]** step
1. Select ![settings_icon](assets/settings_icon.png) on the action bar. The **[!UICONTROL Assign Task]** dialog opens.
1. Open [!UICONTROL Form and Document] tab and open [!UICONTROL Pre-populated] drop-down and specify:

   * Select input data file using
   * Select input attachments using

    ![Review step](/help/forms/assets/assigntask-review1.gif)

1. Open **[!UICONTROL Assignee]** tab and open [!UICONTROL Pre-populated] drop-down and specify **[!UICONTROL Assign  options]**:
  
    ![Review step](/help/forms/assets/review-assignstep.png)

1. Click **[!UICONTROL Done]** to save the changes. 

## Configure Submit Action {#configure-submit-action}

Now, configure the Submit action of an Adaptive Form Container component on Site's page :

1. Go to Site's page.
1. Select ![settings_icon](assets/settings_icon.png) of an Adaptive Form container. The **[!UICONTROL Adaptive Form Container]** dialog opens.
1. Open the **[!UICONTROL Submission]** tab and specify **[!UICONTROL Submit Action]** to [Invoke an AEM workflow](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-foundation-components/configure-submit-actions-and-metadata-submission/configuring-submit-actions.html?lang=en#invoke-an-aem-workflow)

1. Click [Done] to save the settings.

![submissiontab-reviewstep](/help/forms/assets/submissiontab-reviewstep.gif)

## Submit an Adaptive form after review {#submit-af-after-review}

To review and confirm the submitted Adaptive Form:

1. Go to [!UICONTROL Tools] >  [!UICONTROL Workflow] >  [!UICONTROL Instances] 
1. In Inbox, you can see that an instance is being created.
1. Select the instance and Click [!UICONTROL Open].
1. Now, you can see the submitted form. 

The reviewer performs different actions as:

* **Submit**: The reviewer completes the form and submits it for further processing.
* **Save**: The reviewer saves the form in its current state without submitting it.
* **Reset**: The reviewer clears any changes made to the form and restores it to its original state.
* **Delegate**: The reviewer transfers ownership of the form to another person for further action or review.
