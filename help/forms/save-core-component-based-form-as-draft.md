---
title: How to save the Core Components based Adaptive Form as a draft and use the Drafts and Submissions component to list drafts and submissions?
description: Learn how to save Core Components based Adaptive Form as a draft. Also understand how to use the Drafts and Submissions component to list drafts and submissions for logged-in users?
feature: Adaptive Forms, Core Components
exl-id: c0653bef-afeb-40c1-b131-7d87ca5542bc
role: User, Developer
---

# Save forms as drafts and list them on Sites page

<span class="preview"> This article contains content about the **Drafts** feature, a pre-release feature. The pre-release feature is accessible only through our [pre-release channel](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/release-notes/prerelease.html#new-features).</span>

Consider a user who begins filling out a form but needs to pause and return later. AEM offers a `save-as-draft` option, allowing the user to save the form as a draft for future completion. To facilitate this, AEM provides the **Drafts & Submissions** Forsm Portal component out of the box, which displays drafts and submissions on AEM Sites pages. The component lists forms that have been saved as drafts for later completion, as well as those that have been submitted. Only logged-in users can edit their drafts or view their submitted forms. However, if an anonymous user navigates through the list of forms using the **Search & Lister** component and saves a form as a draft, that draft is not listed by the **Drafts & Submissions** component. To view drafts and submissions, users must be logged in at the time of form submission.

![Drafts icon](assets/drafts-component.png)

## Pre-requisites

* [Enable Adaptive Forms Core Components for your environment.](/help/forms/enable-adaptive-forms-core-components.md)

    After deploying the latest Core Components to your environment, the Forms Portal components become accessible in your authoring environment.

* [Configure Azure Storage and Unified Storage Connector for Drafts & Submissions Forms Portal component](#configure-azure-storage-and-unified-storage-connector-for-drafts--submissions-forms-portal-component) 

### Configure Azure Storage and Unified Storage Connector for Drafts & Submissions Forms Portal component

The **Drafts & Submissions** component needs a storage setup for saving and listing drafts on AEM Sites page. The Unified Storage Connector offers a framework to link AEM with external storage. To save the form as a draft, ensure that you have an Azure storage account and an access key to authorize access to the [!DNL Azure] storage account. Once, you have Azure storage account and the access key, perform the following steps to create an Azure Storage configuration:

1. Navigate to **[!UICONTROL Tools]** &gt; **[!UICONTROL Cloud Services]** &gt; **[!UICONTROL Azure Storage]**.

    ![Azure Storage Card selection](/help/forms/assets/save-form-as-draft-azure-card.png)

1. Select a configuration folder to create the configuration and select **[!UICONTROL Create]**.

     ![Select Azure Storage Configuration Folder](/help/forms/assets/save-form-as-draft-select-config-folder.png)

1. Specify a title for the configuration in the **[!UICONTROL Title]** field.
1. Specify the name of the [!DNL Azure] storage account in the **[!UICONTROL Azure Storage Account]** and **[!UICONTROL Azure Access Key]** fields.

    ![Azure Storage Configuration](/help/forms/assets/save-form-as-draft-azure-storage.png)

    Enter `Connection String` in the `Azure Storage Account` textbox and  `Azure Key` in the `Azure Access key` textbox.

1. Click **Save**.

    >[!NOTE]
    >
    > You can retrieve the **[!UICONTROL Azure Storage Account]** and **[!UICONTROL Azure Access Key]** from the [Microsoft Azure Portal](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal).

    After, you have successfully created the Azure Storage Configuration, configure the Unified Storage Connector for Forms Portal, using the following steps:

1. Navigate to **[!UICONTROL Tools]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Unified Storage Connector]**.

    ![Unified connector Storage](/help/forms/assets/save-form-as-draft-unified-connector.png)

1. In the **[!UICONTROL Forms Portal]** section, select **[!UICONTROL Azure]** from the **[!UICONTROL Storage]** drop-down list.
1. Specify the configuration path for the Azure storage configuration in the **[!UICONTROL Storage Configuration Path]** field.

    ![Unified connector Storage setting](/help/forms/assets/save-form-as-draft-unified-connector-storage.png)

1. Select **[!UICONTROL Save]**.

>[!NOTE]
>
> If you need to configure a storage option, other than Azure, write to aem-forms-ea@adobe.com from your official email address with your detailed requirements.

Once you have successfully configured Azure Storage and Unified Storage Connector for storing the drafts and submitted forms, add the **Drafts & Submissions** component on AEM Sites page.

## How to add the Drafts & Submissions component to an AEM Sites page?

You can use out-of-the-box Forms Portal components to list drafts and submissions on the Sites page. Perform the following steps to add the **Drafts & Submissions** portal component: 

1. Open the AEM Sites page in an **Edit** mode. 
1. Go to the **[!UICONTROL Page Information]** > **[!UICONTROL Edit Template]**
    ![Edit template policy](/help/forms/assets/save-form-as-draft-edit-template.png)

1. Click the **[!UICONTROL Policy]** and select the **[!UICONTROL Drafts & Submissions]**  checkbox under the **[AEM Archetype Project Name] - Forms and Communications Portal**.

    ![Policy Selection](/help/forms/assets/save-form-as-draft-enable-policy.png)

1. Click **[!UICONTROL Done]**.
1. Now re-open the AEM Sites page in the authoring mode.
1. Locate the section within the page editor that allows you to add the Forms Portal component. 
1. Click the **Add** icon. The icon is a plus sign (+) that signifies the option to add new components.
    
    Clicking the **Add** icon displays an **Insert New Component** dialog box that displays various components for insertion.

    >[!NOTE]
    >
    > Alternatively, you can also drag and drop the component.

1. Browse the available components in the dialog box and select the desired component from the list. For example, select the **Drafts & Submissions** component from the list to add the **Drafts & Submissions** Forms Portal component. 

    ![Add Draft and Submission Component](/help/forms/assets/save-form-as-draft-add-dns.png)

Now, configure the properties of the **Drafts and Submissions** component according to the requirements.

## Configure properties of the Drafts & Submissions Component 

You can configure the properties of the **Drafts & Submissions**:
1. Select the **Drafts & Submissions** component.
1. Click the ![Configure icon](assets/configure_icon.png) and the dialog box appears. 
1. In the **[!UICONTROL Drafts and Submissions]** dialog, specify the following:
   * **Title** To identify a component in a Sites page and by default, the title appears on top of the component.
   * **Select Type**: To indicate the form listing as draft or submitted forms. If you choose **Draft Forms**, the forms saved as drafts are displayed. Alternatively, selecting **Submitted Forms** shows the forms submitted by logged-in users.
   *  **Layout**: To display list draft forms or submitted forms in the card or list format.
 
    ![Draft and Submission Component proeprties](/help/forms/assets/save-form-as-draft-dns-properties.png)

## Configure forms to save as drafts

You can configure Adaptive Forms in the following two ways to save them as drafts for later use:
* [User action](#user-action)
* [Auto-save](#auto-save)

### User action

>[!NOTE]
>
> Ensure that the [Core Components version is set to 3.0.24 or later](https://github.com/adobe/aem-core-forms-components) to save forms as drafts using the **Save Form** rule.

To save a form as a Draft, create a **Save Form** rule on a form component, such as a button. When the button is clicked, the rule triggers, and the form is saved as a draft. Perform the following steps to create a **Save Form** rule on a button component:

1. Open an Adaptive Form in an edit mode.
1. Select the **[!UICONTROL Edit Rules]** icon to open the Rule Editor for the **Button** component. 
1. Select **[!UICONTROL Create]** to configure and create the rule for button.
1. In the **[!UICONTROL When]** section, select **is clicked** and in the **[!UICONTROL Then]** section, select the **Save Form** option.
1. Select **[!UICONTROL Done]** to save the rule.

    ![Create rule for button](/help/forms/assets/save-form-as-drfat-create-rule.png)

When you preview an Adaptive Form, fill it out, and click the **Save Form** button, the form is saved as a draft.

### Drafts

>[!NOTE]
>
> Ensure that the [Core Components version is set to 3.0.52 or later](https://github.com/adobe/aem-core-forms-components) to save forms as drafts using the auto save feature.

You can also configure an Adaptive Form to save automatically based on a time-based event, ensuring the form is saved after the specified duration. When you [enable Forms Portal components for your environment](/help/forms/list-forms-on-sites-page.md#enable-forms-portal-components-for-your-existing-environment), the **Auto Save** tab appears in the Forms container properties. You can configure the auto-save feature for an Adaptive Form:

1. In the author instance, open an Adaptive Form in an edit mode.
1. Open the Content browser, and select the **[!UICONTROL Guide Container]** component of your Adaptive Form. 
1. Click the Guide Container properties ![Guide properties](/help/forms/assets/configure-icon.svg) icon and open the **[!UICONTROL Drafts]** tab.

    ![Auto-save](/help/forms/assets/auto-save.png)

1. Select the **[!UICONTROL Automatically Save Drafts]** check box to enable auto-save of the form as drafts.
1. Configure **[!UICONTROL Save Preference]** as **Save drafts at regular intervals**, to auto-save the form <!--based on the occurrence of an event or--> after a specific interval of time.
1. Specify the time interval in **[!UICONTROL Save interval frequency (Seconds)]** to set the duration that triggers the automatic saving of the form at the defined interval.
1. Click **[!UICONTROL Done]**.
 
## View drafts/submitted forms on Sites page using the Drafts & Submissions component

To view saved drafts or submitted forms, use the **Drafts & Submissions** Forms Portal component. 
When **[!UICONTROL Select Type]** is selected as **Draft Forms** in the [configure dialog of the Drafts & Submissions component](#configure-properties-of-the-drafts--submissions-component), the forms saved as drafts appear on the Sites page. You can open the drafts by clicking on the ellipsis (...) to complete the form.

![Drafts icon](assets/drafts-component.png)

When **[!UICONTROL Select Type]** is selected as **Submitted Forms** in the [configure dialog of the Drafts & Submissions component](#configure-properties-of-the-drafts--submissions-component), the submitted forms appear. You can view the submitted forms but cannot edit them.

![Submissions icon](assets/submission-listing.png)

You can also discard the forms by clicking on the ellipsis (...) that appears in the bottom-right corner of the form.

## Next Steps

In the next article, let us learn [how to add references to forms on the Sites page using the Link Forms Portal component](/help/forms/add-form-link-to-aem-sites-page.md).

## Related articles

{{forms-portal-see-also}}

## See Also {#see-also}

{{see-also}}