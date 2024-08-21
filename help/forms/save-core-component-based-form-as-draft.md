---
title: How to save the Core Components based Adaptive Form as a draft?
description: Learn how to save Core Components based Adaptive Form as a draft and create a Forms Portal and use out-of-the-box Core Components on an AEM Sites page.
feature: Adaptive Forms, Core Components
exl-id: c0653bef-afeb-40c1-b131-7d87ca5542bc
role: User, Developer, Admin
---

# Save an Adaptive Form as a draft 

The Forms Portal component provides accessibility with security and improves the overall user experience by integrating form management directly into the AEM Sites page. The **Drafts & Submissions** Forms Portal component allows users to edit drafts or view submitted forms by the authenticated users. This functionality allows users to save the progress and return to complete the tasks later without losing any entered information. Providing the  `save-as-draft` option ensures flexibility in managing time, reduces the risk of data loss, and maintains the precision of submissions. You can save forms as drafts to complete them later. 

## Pre-requisites

* [Enable Adaptive Forms Core Components for your environment.](/help/forms/enable-adaptive-forms-core-components.md)

    >[!NOTE]
    >
    > Ensure that the [Core Components version is set to 3.0.24 or later](https://github.com/adobe/aem-core-forms-components) to use `save-as-draft` feature.

* [Configure Azure Storage and Unified Storage Connector for Drafts & Submissions Forms Portal component](#configure-azure-storage-and-unified-storage-connector-for-drafts--submissions-forms-portal-component) 

### Configure Azure Storage and Unified Storage Connector for Drafts & Submissions Forms Portal component

To save the form as a draft, ensure that you have an Azure storage account and an access key to authorize access to the [!DNL Azure] storage account. Once, you have Azure storage account and the access key, perform the following steps to create an Azure Storage configuration:

1. Navigate to **[!UICONTROL Tools]** &gt; **[!UICONTROL Cloud Services]** &gt; **[!UICONTROL Azure Storage]**.

    ![Azure Storage Card selection](/help/forms/assets/save-form-as-draft-azure-card.png)

2. Select a configuration folder to create the configuration and select **[!UICONTROL Create]**.

     ![Select Azure Storage Configuration Folder](/help/forms/assets/save-form-as-draft-select-config-folder.png)

3. Specify a title for the configuration in the **[!UICONTROL Title]** field.
4. Specify the name of the [!DNL Azure] storage account in the **[!UICONTROL Azure Storage Account]** and **[!UICONTROL Azure Access Key]** fields.

    ![Azure Storage Configuration](/help/forms/assets/save-form-as-draft-azure-storage.png)

5. Click **Save**.

    >[!NOTE]
    >
    > You can retrieve the **[!UICONTROL Azure Storage Account]** and **[!UICONTROL Azure Access Key]** from the [Microsoft Azure Portal](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal).

    After, you have successfully created the Azure Storage Configuration, configure the Unified Storage Connector for Forms Portal, using the following steps:

6. Navigate to **[!UICONTROL Tools]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Unified Storage Connector]**.

    ![Unified connector Storage](/help/forms/assets/save-form-as-draft-unified-connector.png)

7. In the **[!UICONTROL Forms Portal]** section, select **[!UICONTROL Azure]** from the **[!UICONTROL Storage]** drop-down list.
8. Specify the configuration path for the Azure storage configuration in the **[!UICONTROL Storage Configuration Path]** field.

    ![Unified connector Storage setting](/help/forms/assets/save-form-as-draft-unified-connector-storage.png)

9. Select **[!UICONTROL Save]**.

Once you have successfully configured Azure Storage and Unified Storage Connector for storing the drafts and submitted forms, add the **Drafts & Submissions** component on AEM Sites page.

## How to add the Drafts & Submissions component to an AEM Sites page?

AEM provides the **Drafts & Submissions** component out of the box to display forms on AEM Sites pages. The **Drafts & Submissions** component shows forms that are saved as drafts for later completion, as well as submitted forms. This component provides a personalized experience for logged-in users by displaying the drafts and form submissions.

You can use out-of-the-box Forms Portal components to list form on the Sites page. Perform the following steps to add the **Drafts & Submissions** portal component: 

1. Open the AEM Sites page in an **Edit** mode. 
2. Go to the **[!UICONTROL Page Information]** > **[!UICONTROL Edit Template]**
    ![Edit template policy](/help/forms/assets/save-form-as-draft-edit-template.png)

3. Click the **[!UICONTROL Policy]** and select the **[!UICONTROL Drafts & Submissions]**  checkbox under the **[AEM Archetype Project Name] - Forms and Communications Portal**.

    ![Policy Selection](/help/forms/assets/save-form-as-draft-enable-policy.png)

4. Click **[!UICONTROL Done]**.
5. Now, re-open the AEM Sites page in the authoring mode.
6. Add the **Drafts and Submissions** component, either by dragging and dropping the component to the layout container on the page, or selecting the **Add** icon on the layout container and adding the component from the **[!UICONTROL Insert New Component]** dialog.

![Add Draft and Submission Component](/help/forms/assets/save-form-as-draft-add-dns.png)

Now, configure the properties of the **Drafts and Submissions** component according to the requirements.

## Configure properties of the Drafts & Submissions Component 

The **Drafts & Submissions** component displays forms that are saved as draft for completing later and submitted forms. You can configure the properties of the **Drafts & Submissions**:
1. Select the **Drafts & Submissions** component.
2. Click the ![Configure icon](assets/configure_icon.png) and the dialog box appears. 
3. In the **[!UICONTROL Drafts and Submissions]** dialog, specify the following:
   * **Title** To identify a component in a Sites page and by default, the title appears on top of the component.
   * **Select Type**: To indicate the form listing as draft or submitted forms. If you choose **Draft Forms**, the forms saved as drafts are displayed. Alternatively, selecting **Submitted Forms** shows the forms submitted by logged-in users.
   *  **Layout**: To display list draft forms or submitted forms in the card or list format.
 
    ![Draft and Submission Component proeprties](/help/forms/assets/save-form-as-draft-dns-properties.png)

## Save forms as drafts

You can configure Adaptive Forms in the following two ways to save them as drafts for the later use:
* [User action](#user-action)
* [Auto-save](#auto-save)

### User action

To save a form as a Draft, create a **Save Form** rule on a form component, such as a button. When the button is clicked, the rule triggers, and the form is saved as a draft. Perform the following steps to create a **Save Form** rule on a button component:

1. Open an Adaptive Form in an edit mode.
1. Select the **[!UICONTROL Edit Rules]** icon to open the Rule Editor for the **Button** component. For example, let us say a button labeled **Save Form** is added to a form.
1. Select **[!UICONTROL Create]** to configure and create the rule for button.
1. In the **[!UICONTROL When]** section, select **is clicked** and in the **[!UICONTROL Then]** section, select the **Save Form** option.
1. Select **[!UICONTROL Done]** to save the rule.

    ![Create rule for button](/help/forms/assets/save-form-as-drfat-create-rule.png)

When you preview an Adaptive Form, fill it out, and click the **Save Form** button, the form is saved as a draft.

### Auto save

You can also configure an Adaptive Form to save automatically based on a time-based event, ensuring the form is saved after the specified duration. When you [enable Forms Portal components for your environment](/help/forms/list-forms-on-sites-page.md#enable-forms-portal-components-for-your-existing-environment), the **Auto Save** tab appears in the Forms container properties. You can configure the auto-save feature for an Adaptive Form:

1. In the author instance, open an Adaptive Form in an edit mode.
1. Open the Content browser, and select the **[!UICONTROL Guide Container]** component of your Adaptive Form. 
1. Click the Guide Container properties ![Guide properties](/help/forms/assets/configure-icon.svg) icon and open the **[!UICONTROL Auto-Save]** tab.

    ![Auto-save](/help/forms/assets/auto-save.png)

1. Select the **[!UICONTROL Enable]** check box to enable auto-save of the form.
1. Configure **[!UICONTROL Trigger]** as **Time based**, to auto-save the form <!--based on the occurrence of an event or--> after a specific interval of time.
1. Specify the time interval in **[!UICONTROL Auto save on this interval (In seconds)]** to set the duration that triggers the automatic saving of the form at the defined interval.
1. Click **[!UICONTROL Done]**.
 
## View drafts/submitted forms using the  Drafts & Submissions component

To view saved drafts or submitted forms, use the  **Drafts & Submissions** Forms Portal component. 
When **[!UICONTROL Select Type]** is selected as **Draft Forms** in the [configure dialog of the Drafts & Submissions component](#configure-properties-of-the-drafts--submissions-component), the forms saved as drafts appear on Sites page. You can open the drafts by clicking on the ellipsis (...) to complete the form.

![Drafts icon](assets/drafts-component.png)

When **[!UICONTROL Select Type]** is selected as **Submitted Forms** in the [configure dialog of the Drafts & Submissions component](#configure-properties-of-the-drafts--submissions-component), the submitted forms appear. You can view the submitted forms but cannot edit them.

![Submissions icon](assets/submission-listing.png)

You can also discard the forms by clicking on the ellipsis (...) that appears in the bottom-right corner of the form.

## Related articles

{{forms-portal-see-also}}

## See Also {#see-also}

{{see-also}}



<!--

>[!MORELIKETHIS]
>
>* [Configure data sources for AEM Forms](/help/forms/configure-data-sources.md)
>* [Configure Azure storage for AEM Forms](/help/forms/configure-azure-storage.md)
>* [Integrate Microsoft Dynamics 365 and Salesforce with Adaptive Forms](/help/forms/configure-msdynamics-salesforce.md)

-->
