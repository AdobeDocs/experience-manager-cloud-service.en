---
title: How to save the core component based Adaptive Form as a draft?
description: Learn how to save core component based Adaptive Form as a draft and create a Forms Portal and use out-of-the-box core components on an AEM Sites page.
feature: Adaptive Forms, Core Components
exl-id: c0653bef-afeb-40c1-b131-7d87ca5542bc
role: User, Developer, Admin
---

# Save Core Component based Adaptive Form as a draft {#save-af-form}

To save Adaptive Form as a draft is an essential feature that enhances user efficiency and accuracy. This functionality allows users to save the progress and return to complete the tasks later without losing any entered information. Providing a  `save-as-draft` option ensures flexibility in managing time, reduces the risk of data loss, and maintains the precision of submissions. You can save forms as drafts to complete them later. 

## Considerations

* [Enable Adaptive Forms core components for your environment.](/help/forms/enable-adaptive-forms-core-components.md)

* Ensure that the [core component is set to version 3.0.24 or later](https://github.com/adobe/aem-core-forms-components) to use this feature.
* Ensure that you have an [Azure storage account and an access key](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal) to authorize access to the Azure storage account.

## Save an Adaptive Form as a Draft

[!DNL Experience Manager Forms] Data Integration (data-integration.md) provides [!DNL Azure] storage configuration to integrate forms with [!DNL Azure] storage services. The Form Data Model (FDM) can be used to create Adaptive Forms that interact with the [!DNL Azure] server to enable business workflows.

To save form as a draft, ensure that you have an Azure storage account and an access key to authorize access to the [!DNL Azure] storage account. To save form as a draft, perform the following steps:

1. [Create Azure Storage Configuration](#create-azure-storage-configuration)
1. [Configure Unified Storage Connector for Forms Portal](#configure-usc-forms-portal)
1. [Create Rule to Save an Adaptive Form as a Draft](#rule-to-save-adaptive-form-as-draft)


### 1. Create Azure Storage Configuration {#create-azure-storage-configuration}

Once, you have an Azure storage account and an access key to authorize access to the [!DNL Azure] storage account, perform the following steps to create Azure Storage configuration:

1. Navigate to **[!UICONTROL Tools]** &gt; **[!UICONTROL Cloud Services]** &gt; **[!UICONTROL Azure Storage]**.

    ![Azure Storage Card selection](/help/forms/assets/save-form-as-draft-azure-card.png)

1. Select a configuration folder to create the configuration and select **[!UICONTROL Create]**.

     ![Select Azure Storage Configuration Folder](/help/forms/assets/save-form-as-draft-select-config-folder.png)

1. Specify a title for the configuration in the **[!UICONTROL Title]** field.
1. Specify the name of the [!DNL Azure] storage account in the **[!UICONTROL Azure Storage Account]** and **[!UICONTROL Azure Access Key]** fields.

    ![Azure Storage Configuration](/help/forms/assets/save-form-as-draft-azure-storage.png)

1. Click **Save**.

>[!NOTE]
>
> You can retrieve the **[!UICONTROL Azure Storage Account]** and **[!UICONTROL Azure Access Key]** from the [Microsoft Azure Portal](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal).

 
### 2. Configure Unified Storage Connector for Forms Portal {#configure-usc-forms-portal}

After, you have successfully created the Azure Storage Configuration, configure the Unified Storage Connector for Forms Portal, using following steps:

1. Navigate to **[!UICONTROL Tools]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Unified Storage Connector]**.

    ![Unified connector Storage](/help/forms/assets/save-form-as-draft-unified-connector.png)

1. In the **[!UICONTROL Forms Portal]** section, select **[!UICONTROL Azure]** from the **[!UICONTROL Storage]** drop-down list.
1. Specify the [configuration path for the Azure storage configuration](#create-azure-storage-configuration) in the **[!UICONTROL Storage Configuration Path]** field.

    ![Unified connector Storage setting](/help/forms/assets/save-form-as-draft-unified-connector-storage.png)

1. Select **[!UICONTROL Save]** and then select **[!UICONTROL Publish]** to publish the configuration.

### 3. Create Rules to save an Adaptive Form as a draft {#rule-to-save-adaptive-form-as-draft}

To save a form as a Draft, create a **Save Form** rule on a form component, such as a button. When the button is clicked, the rule triggers, and the form is saved as a draft. Perform te following steps to create **Save Form** rule on a button component:

1. In the Author instance, open an Adaptive Form in an edit mode.
1. From the left pane, select ![Components icon](assets/components_icon.png) and drag the **[!UICONTROL Button]** component to the form.
1. Select the **[!UICONTROL Button]** component and then select the ![Configure icon](assets/configure_icon.png). 
1. Select the **[!UICONTROL Edit Rules]** icon to open the Rule Editor. 
1. Select **[!UICONTROL Create]** to configure and create the rule.
1. In the **[!UICONTROL When]** section, select **is clicked** and in the **[!UICONTROL Then]** section, select the **Save Form** option.
1. Select **[!UICONTROL Done]** to save the rule.

![Create rule for button](/help/forms/assets/save-form-as-drfat-create-rule.png)

When you preview an Adaptive Form, fill it out, and click the **Save Form** button, the form is saved as a draft for later use. 

## Drafts & Submissions component to list drafts on AEM Sites page

AEM Forms provides the **Drafts & Submissions** portal component out of the box to display saved forms on AEM Sites pages. The **Drafts & Submissions** component shows forms that are saved as drafts for later completion, as well as submitted forms. This component offers a personalized experience for any logged-in user by listing the drafts and submissions related to the Adaptive Forms created by the user.

You can use out-of-the-box Forms Portal components to list form drafts in the AEM Sites page. Perform the following steps to use the **Drafts & Submissions** portal component: 

1. [Enable Drafts & Submissions Forms Portal Component](#enable-component)
2. [Add Drafts & Submissions Component in AEM Sites page](#Add-drafts-submissions-component)
3. [Configure Drafts & Submissions Component](#configure-drafts-submissions-component)

### 1. Enable Drafts & Submissions Forms Portal Component{#enable-component}

To enable the **[!UICONTROL Drafts & Submissions]** component in the template policy, perform the following steps:

1. Open the AEM Sites page in an **Edit** mode. 
1. Go to the **[!UICONTROL Page Information]** > **[!UICONTROL Edit Template]**
    ![Edit template policy](/help/forms/assets/save-form-as-draft-edit-template.png)

1. Click the **[!UICONTROL Policy]** and select the **[!UICONTROL Drafts & Submissions]**  checkbox under the **[AEM Archetype Project Name] - Forms and Communications Portal**.

    ![Policy Selection](/help/forms/assets/save-form-as-draft-enable-policy.png)

1. Click **[!UICONTROL Done]**.

Once a portal component is enabled, you can use it in the author instance of your AEM Sites page.

### 2. Add Drafts & Submissions Component in AEM Sites page{#Add-drafts-submissions-component}

You can create and customize Forms Portal on websites authored using AEM by adding and configuring the portal components. Ensure that the [Drafts & Submissions component is enabled](#enable-component) before using them in the AEM Sites page.

To add a component, either drag and drop the component from the **Drafts & Submissions** component pane to the layout container on the page, or select the add icon on the layout container and add the component from the **[!UICONTROL Insert New Component]** dialog.

![Add Draft and Submission Component](/help/forms/assets/save-form-as-draft-add-dns.png)

### 3. Configure Drafts & Submissions Component {#configure-drafts-submissions-component}

The **Drafts & Submissions** component displays forms that are saved as draft for completing later and submitted forms. To configure **Drafts & Submissions**, perform the following steps:
1. Select the **Drafts & Submissions** component.
1. Click the ![Configure icon](assets/configure_icon.png) and the dialog box appears. 
1. In the **[!UICONTROL Drafts and Submissions]** dialog, specify the following:
   * **Title** To identify a component in a Sites page and by default, the title appears on top of the component.
   * **Type**: To indicate the form listing as draft or submitted forms.
   *  **Layout**: To display list draft forms or submitted forms in card or list format.
 
    ![Draft and Submission Component proeprties](/help/forms/assets/save-form-as-draft-dns-properties.png)

1. Click **Done**. 

When **[!UICONTROL Select Type]** is selected as **Draft Forms**, the forms saved as drafts appear:
![Drafts icon](assets/drafts-component.png)

When **[!UICONTROL Select Type]** is selected as **Submitted Forms**, the submitted forms appear:

![Submissions icon](assets/submission-listing.png)

You can open the form by clicking on the respective form.

<!--

### Configure Search & Lister Component {#configure-search-lister-component}

The Search & Lister component is used to list adaptive forms on a page and to implement search on the listed forms. 

![Search and Lister icon](assets/search-and-lister-component.png)

To configure, select the component and then select the ![Configure icon](assets/configure_icon.png). The [!UICONTROL Search and Lister] dialog opens.

1. In the [!UICONTROL Display] tab, configure the following:
    * In **[!UICONTROL Title]**, specify the title for the Search & Lister component. An indicative title enables the users perform quick search across the list of forms.
    * From the **[!UICONTROL Layout]** list, select the layout to represent the forms in card or list format.
    * Select **[!UICONTROL Hide Search]** and **[!UICONTROL Hide Sorting]** to hide the search and sort by features.
    * In **[!UICONTROL Tooltip]**, provide the tooltip that appears when you hover over the component. 
1. In the [!UICONTROL Asset Folder] tab, specify the location from where the forms are pulled and listed on the page. You can configure multiple folder locations.
1. In the [!UICONTROL Results] tab, configure the maximum number of forms to display per page. The default is eight forms per page.

### Configure Link Component {#configure-link-component}

The link component enables you to provide links to an adaptive form on the page. To configure, select the component and then select the ![Configure icon](assets/configure_icon.png). The [!UICONTROL Edit Link Component] dialog opens.

1. In the [!UICONTROL Display] tab, provide the link caption and tooltip to ease identification of the forms represented by the link.
1. In the [!UICONTROL Asset Info] tab, specify the repository path where the asset is stored. 
1. In the [!UICONTROL Query Params] tab, specify the additional parameters in the key-value pair format. When the link is clicked, these additional parameters and passed along with the form.

## Configure Asynchronous Form Submission Using Adobe Sign {#configure-asynchronous-form-submission-using-adobe-sign}

You can configure to submit an adaptive form only when all the recipients have completed the signing ceremony. Follow the steps below to configure the setting using Adobe Sign.

1. In the author instance, open an Adaptive Form in the edit mode.
1. From the left pane, select the Properties icon and expand the **[!UICONTROL ELECTRONIC SIGNTATURE]** option.
1. Select **[!UICONTROL Enable Adobe Sign]**. Various configuration options display. 
1. In the [!UICONTROL Submit the form] section, select the **[!UICONTROL after every recipient completes signing ceremony]** option to configure the Submit Form action, where the form is first sent to all the recipients for signing. Once all the recipients have signed the form, only then the form is submitted. 

## Save Adaptive Forms As Drafts {#save-adaptive-forms-as-drafts}

You can save forms as Drafts for completing them later. There are two ways in which a form is saved as a draft:

* Create a "Save Form" rule on a form component, for example, a button. On clicking the button, the rule triggers and the form are saved a draft.
* Enable Auto-Save feature, which saves the form as per the specified event or after a configured interval of time.

### Create Rules to Save an Adaptive Form as Draft {#rule-to-save-adaptive-form-as-draft}

To create a "Save Form" rule on a form component, for example, a button, follow the steps below:

1. In the author instance, open an Adaptive Form in edit mode.
1. From the left pane, select ![Components icon](assets/components_icon.png) and drag the [!UICONTROL Button] component to the form.
1. Select the [!UICONTROL Button] component and then select the ![Configure icon](assets/configure_icon.png). 
1. Select the [!UICONTROL Edit Rules] icon to open the Rule Editor. 
1. Select **[!UICONTROL Create]** to configure and create the rule.
1. In the [!UICONTROL When] section, select "is clicked" and in the [!UICONTROL Then] section, select the "Save Form" options.
1. Select **[!UICONTROL Done]** to save the rule.

### Enable Auto-save {#enable-auto-save}

You can configure the auto-save feature for an adaptive form as follows:

1. In the author instance, open an Adaptive Form in edit mode.
1. From the left pane, select the ![Properties icon](assets/configure_icon.png) and expand the [!UICONTROL AUTO-SAVE] option.
1. Select the **[!UICONTROL Enable]** check box to enable auto-save of the form. You can configure the following:
* By default, the [!UICONTROL Adaptive Form Event] is set to "true", which implies that the form is auto-saved after every event.
* In [!UICONTROL Trigger], configure to trigger auto-save based on the occurrence of an event or after a specific interval of time.
-->

## See Also {#see-also}

{{see-also}}



<!--

>[!MORELIKETHIS]
>
>* [Configure data sources for AEM Forms](/help/forms/configure-data-sources.md)
>* [Configure Azure storage for AEM Forms](/help/forms/configure-azure-storage.md)
>* [Integrate Microsoft Dynamics 365 and Salesforce with Adaptive Forms](/help/forms/configure-msdynamics-salesforce.md)

-->
