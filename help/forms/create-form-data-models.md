---
title: How to Create Form Data Model?
description: Experience Manager Forms data integration provides an intuitive user interface to create and work with form data models. Learn how to create form data models with or without configured data sources.
feature: Form Data Model
role: User, Developer
level: Beginner, Intermediate
exl-id: b17b7441-912c-44c7-a835-809f014a8c86
---
# Create Form Data Model {#create-form-data-model}

 ![Data integration](do-not-localize/data-integeration.png)

[!DNL Experience Manager Forms] data integration provides an intuitive user interface to create and work with form data models. A Form Data Model relies on data sources for exchange of data; however, you can create a Form Data Model with or without a data source. There are two approaches to create a from data model depending on whether you have configured data sources:

* **Using preconfigured data sources**: If you have configured data sources as described in [Configure data sources](configure-data-sources.md), you can select them while creating a form data model. It brings all data model objects, properties, and services from the selected data sources available for use in the form data model.

* **Without data sources**: If you have not configured data sources for your form data model, you can still create it without data sources. You can use the Form Data Model to author Adaptive Forms <!--and interactive communication--> and test them using sample data. When data sources are available, you can bind the Form Data Model with data sources, which automatically reflects in the associated Adaptive Forms<!--and interactive communications-->.

>[!NOTE]
>
>You must be a member of both **fdm-author** and **forms-user** groups to be able to create and work with form data model. Contact your [!DNL Experience Manager] administrator to become a member of the groups.

## Create Form Data Model {#data-sources}

Ensure that you have configured the data sources you intend to use in the Form Data Model as described in [Configure data sources](configure-data-sources.md). Do the following to create a Form Data Model based on configured data sources:

1. In [!DNL Experience Manager] author instance, navigate to **[!UICONTROL Forms > Data Integrations]**.
1. Tap **[!UICONTROL Create > Form Data Model]**.
1. In the Create Form Data Model dialog:

    * Specify a name for the form data model. 
    * (**Optional**) Specify title, description, and tags for the form data model.
    * (**Optional and applicable only if data sources are configured**) Tap the tick icon next to the **[!UICONTROL Data Source Configuration]** field and select the configuration node where cloud services for the data sources you want to use reside. It restricts the list of data sources available for selection on the next page to the ones available in the selected configuration node. However, any JDBC database and [!DNL Experience Manager] user profile data sources are listed by default. If you do not select a configuration node, data sources from all configuration nodes are listed.

1. Tap **[!UICONTROL Next]**.

1. (**Applicable only if data sources are configured**) The **[!UICONTROL Select Datasource]** screen lists available data sources, if any. Select data sources you want to use in the form data model.
1. Tap **[!UICONTROL Create]** and on the confirmation dialog, tap **[!UICONTROL Open]** to open the Form Data Model editor.

    Let us review the different components of the Form Data Model editor UI.

    ![A Form Data Model with three data sources - a RESTful service, [!DNL Experience Manager] user profile, and an RDBMS](assets/fdm-ui.png)

   A. **[!UICONTROL Data Sources]** Lists data sources in a form data model. Expand a data source to view its data model objects and services.

   B. **[!UICONTROL Refresh Data Source Definitions]** Fetches any changes in data source definitions from configured data sources and updates them in the Data Sources tab of the Form Data Model editor.

   C. **[!UICONTROL Model]** Content area where added data model objects appear.

   D. **[!UICONTROL Services]** Content area where added data source operations or services appear.

   E. **[!UICONTROL Toolbar]** Tools to work with form data model. The toolbar shows more options depending on the selected object in form data model.

   F. **[!UICONTROL Add Selected]** Adds selected data model objects and services to the form data model.

For more information about Form Data Model editor and how you can work with it to edit and configure form data model, see [Work with form data model](work-with-form-data-model.md).

## Update data sources {#update}

Do the following to add or update data sources to an existing form data model.

1. Go to **[!UICONTROL Forms > Data Integrations]**, select the Form Data Model in which you want to add or update data sources, and tap **[!UICONTROL Properties]**.
1. In the Form Data Model properties, go to the **[!UICONTROL Update Source]** tab.

   In the **[!UICONTROL Update Source]** tab:

    * Tap the browse icon in the **[!UICONTROL Context-Aware Configuration]** field and select a configuration node where cloud configuration for the data source you want to add resides. If you do not select a node, cloud configurations residing only in the `global` node are listed when you tap **[!UICONTROL Add Sources]**.
  
    * To add a new data source, tap **[!UICONTROL Add Sources]** and select the data sources to add to the form data model. All data sources configured in `global` and the selected configuration node, if any, are displayed.
  
    * To replace an existing data source with another data source of the same type, tap the **[!UICONTROL Edit]** icon for the data source and select from the list of available data sources.
    * To delete an existing data source, tap the **[!UICONTROL Delete]** icon for the data source. The Delete icon is disabled if a data model object in the data source is added in the form data model.

      ![fdm-properties](assets/fdm-properties.png)

1. Tap **[!UICONTROL Save & Close]** to save the updates.

>[!NOTE]
>
>Once you add new data sources or update existing data sources in a form data model, ensure that you update the binding references, as appropriate, in Adaptive Forms<!--and interactive communications--> that use the updated form data model.

## Next steps {#next-steps}

You now have a Form Data Model with data sources added to it. Next, you can edit the Form Data Model to add and configure data model objects and services, add associations between data model objects, edit properties, add custom data model objects and properties, generate sample data, and so on.

For more information, see [Work with form data model](work-with-form-data-model.md).
