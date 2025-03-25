---
title: How to create Form Data Model (FDM)?
description: Learn to create a form data model (FDM), and send or retrieve data to a datasource using an Adaptive Form or an AEM Workflow.
feature: Adaptive Forms, Form Data Model
role: User, Developer
level: Beginner, Intermediate
exl-id: b17b7441-912c-44c7-a835-809f014a8c86
---
# Create Form Data Model (FDM) {#create-form-data-model}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/form-data-model/create-form-data-models.html)                  |
| AEM as a Cloud Service     | This article        |


 ![Data integration](do-not-localize/data-integeration.png)

[!DNL Experience Manager Forms] data integration provides an intuitive user interface to create and work with form data models. A Form Data Model (FDM) relies on data sources for exchange of data; however, you can create a Form Data Model (FDM) with or without a data source. There are two approaches to create a from data model depending on whether you have configured data sources:

* **Using preconfigured data sources**: If you have configured data sources as described in [Configure data sources](configure-data-sources.md), you can select them while creating a form data model (FDM). It brings all data model objects, properties, and services from the selected data sources available for use in the form data model (FDM).

* **Without data sources**: If you have not configured data sources for your form data model (FDM), you can still create it without data sources. You can use the Form Data Model(FDM) to author Adaptive Forms <!--and interactive communication--> and test them using sample data. When data sources are available, you can bind the Form Data Model (FDM) with data sources, which automatically reflects in the associated Adaptive Forms<!--and interactive communications-->.

>[!NOTE]
>
>You must be a member of both **fdm-author** and **forms-user** groups to be able to create and work with form data model (FDM). Contact your [!DNL Experience Manager] administrator to become a member of the groups.

## Create Form Data Model (FDM) {#data-sources}

Ensure that you have configured the data sources you intend to use in the Form Data Model (FDM) as described in [Configure data sources](configure-data-sources.md). Do the following to create a Form Data Model (FDM) based on configured data sources:

1. In [!DNL Experience Manager] author instance, navigate to **[!UICONTROL Forms > Data Integrations]**.
1. Select **[!UICONTROL Create > Form Data Model]**.
1. In the Create Form Data Model dialog:

    * Specify a name for the form data model (FDM).
    * (**Optional**) Specify title, description, and tags for the form data model (FDM).
    * (**Optional and applicable only if data sources are configured**) Select the tick icon next to the **[!UICONTROL Data Source Configuration]** field and select the configuration node where cloud services for the data sources you want to use reside. It restricts the list of data sources available for selection on the next page to the ones available in the selected configuration node. However, any [!DNL Experience Manager] user profile data sources are listed by default. If you do not select a configuration node, data sources from all configuration nodes are listed.

1. Select **[!UICONTROL Next]**.

1. (**Applicable only if data sources are configured**) The **[!UICONTROL Select Datasource]** screen lists available data sources, if any. Select data sources you want to use in the form data model.
1. Select **[!UICONTROL Create]** and on the confirmation dialog, select **[!UICONTROL Open]** to open the Form Data Model editor.

    Let us review the different components of the Form Data Model editor UI.

    ![A Form Data Model with three data sources - a RESTful service, [!DNL Experience Manager] user profile, and an RDBMS](assets/fdm-ui.png)

   A. **[!UICONTROL Data Sources]** Lists data sources in a form data model. Expand a data source to view its data model objects and services.

   B. **[!UICONTROL Refresh Data Source Definitions]** Fetches any changes in data source definitions from configured data sources and updates them in the Data Sources tab of the Form Data Model editor.

   C. **[!UICONTROL Model]** Content area where added data model objects appear.

   D. **[!UICONTROL Services]** Content area where added data source operations or services appear.

   E. **[!UICONTROL Toolbar]** Tools to work with form data model (FDM) . The toolbar shows more options depending on the selected object in form data model(FDM).

   F. **[!UICONTROL Add Selected]** Adds selected data model objects and services to the form data model.

For more information about Form Data Model editor and how you can work with it to edit and configure form data model (FDM), see [Work with form data model](work-with-form-data-model.md).

## Update data sources {#update}

Do the following to add or update data sources to an existing form data model (FDM).

1. Go to **[!UICONTROL Forms > Data Integrations]**, select the Form Data Model (FDM) in which you want to add or update data sources, and select **[!UICONTROL Properties]**.
1. In the Form Data Model properties, go to the **[!UICONTROL Update Source]** tab.

   In the **[!UICONTROL Update Source]** tab:

    * Select the browse icon in the **[!UICONTROL Context-Aware Configuration]** field and select a configuration node where cloud configuration for the data source you want to add resides. If you do not select a node, cloud configurations residing only in the `global` node are listed when you select **[!UICONTROL Add Sources]**.
  
    * To add a new data source, select **[!UICONTROL Add Sources]** and select the data sources to add to the form data model (FDM). All data sources configured in `global` and the selected configuration node, if any, are displayed.
  
    * To replace an existing data source with another data source of the same type, select the **[!UICONTROL Edit]** icon for the data source and select from the list of available data sources.
    * To delete an existing data source, select the **[!UICONTROL Delete]** icon for the data source. The Delete icon is disabled if a data model object in the data source is added in the form data model (FDM).

      ![fdm-properties](assets/fdm-properties.png)

1. Select **[!UICONTROL Save & Close]** to save the updates.

>[!NOTE]
>
>Once you add new data sources or update existing data sources in a form data model (FDM), ensure that you update the binding references, as appropriate, in Adaptive Forms<!--and interactive communications--> that use the updated form data model (FDM).

## Context aware configurations for specific run modes {#runmode-specific-context-aware-config}

[!UICONTROL Form Data Model (FDM)] utilizes [Sling context-aware configurations](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/context-aware-configs.html) to support different data source parameters to connect with data sources for different [!DNL Experience Manager] run modes.

When [!UICONTROL Form Data Model (FDM)] uses cloud configurations to store parameters, which when checked-in and deployed through source control (Cloud-Manager GIT repository) creates cloud configuration with same parameters for all the run modes (Development, Stage, and Production). However, for use cases where there is a need to have different data sets for test and production environments, then we use data source parameters (for example, data source URL) for different [!DNL Experience Manager] run modes.

To achieve this you need to create an OSGi configuration that contains data source parameters-value pairs. This overrides the same pair from [!UICONTROL Form Data Model (FDM)] cloud configuration at run time. As the OSGi configurations support these run modes by default, you can override a data source parameter to different values based on run mode.

To enable deployment-specific cloud configurations in [!UICONTROL Form Data Model (FDM)]:

1. Create cloud configuration on local development instance. For detailed steps, see [How to configure data sources](/help/forms/configure-data-sources.md).

1. Store your cloud configuration to file system.
    1. Create package with filter `/conf/{foldername}/settings/cloudconfigs/fdm`. Use the same `{foldername}` as in step 1. And replace `fdm` with `azurestorage` for Azure storage configuration.
    1. Build and download package. For details, see [package actions](/help/implementing/developing/tools/package-manager.md).

1. Integrate cloud configuration in [!DNL Experience Manager] Archetype Project.
    1. Unzip the downloaded package.
    1. Copy `jcr_root` folder and put it your `ui.content` > `src` > `main` > `content`.
    1. Update `ui.content` > `src` > `main` > `content` > `META-INF` > `vault` > `filter.xml` to contain filter `/conf/{foldername}/settings/cloudconfigs/fdm`. For details, see [ui.content module of AEM Project Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/uicontent.html). When this archetype project is deployed through CM pipeline, the same cloud configuration gets installed on all the environments (or runmodes). To change the value of fields (like URL) of cloud configurations based on environment, use the OSGi configuration discussed in the following step.

1. Create an Apache Sling context aware configuration. To create the OSGi configuration:
    1. **Set up OSGi configuration files in [!DNL Experience Manager] Archetype project.**
       Create OSGi Factory Configuration files with PID `org.apache.sling.caconfig.impl.override.OsgiConfigurationOverrideProvider`. Create file with same name under each run mode folder where the values need be changed per run mode. For details, see [Configuring OSGi for [!DNL Adobe Experience Manager]](/help/implementing/deploying/configuring-osgi.md#creating-sogi-configurations).

    1. **Set the OSGI configuration json.** To use Apache Sling Context-Aware Configuration Override Provider:
        1. On local development instance `/system/console/configMgr`, select factory OSGi configuration with the name **[!UICONTROL Apache Sling Context-Aware Configuration Override Provider: OSGi configuration]**.
        1. Provide description.
        1. Select **[!UICONTROL enabled]**.
        1. Under overrides, provide fields that need to be changed based on environment in sling override syntax. For details, see [Apache Sling Context-Aware Configuration - Override](https://sling.apache.org/documentation/bundles/context-aware-configuration/context-aware-configuration-override.html#override-syntax). For example, `cloudconfigs/fdm/{configName}/url="newURL"`.
        Multiple overrides can be added by selecting **[!UICONTROL +]**.
        1. Select **[!UICONTROL Save]**.
        1. To get OSGi Configuration JSON, follow the steps in [Generating OSGi Configurations using the AEM SDK Quickstart](/help/implementing/deploying/configuring-osgi.md#generating-osgi-configurations-using-the-aem-sdk-quickstart).
        1. Place JSON in OSGi Factory Configuration Files created in the previous step.
        1. Change the value of `newURL` based on environment (or runmode).
        1. To change secret value based on runmode, secret variable can be created using [cloud manager API](/help/implementing/deploying/configuring-osgi.md#cloud-manager-api-format-for-setting-properties) and later can be referenced in the [OSGi Configuration](/help/implementing/deploying/configuring-osgi.md#secret-configuration-values).
        When this archetype project is deployed through CM pipeline, override will provide different values on different environments (or run mode).
        
        >[!NOTE]
        >
        >[!DNL Adobe Managed Service] users can encrypt the secret values using crypto support for details, see [encryption support for configuration properties](https://experienceleague.adobe.com/docs/experience-manager-65/administering/security/encryption-support-for-configuration-properties.html#enabling-encryption-support) and place encrypted text in the value after [context aware configurations are vailable in service pack 6.5.13.0](https://experienceleague.adobe.com/docs/experience-manager-65/forms/form-data-model/create-form-data-models.html#runmode-specific-context-aware-config).

1. Refresh the data source definitions using the option to refresh data source definitions in the [Form Data Model editor](#data-sources) to refresh FDM cache through FDM UI and get the latest configuration.

## Next steps {#next-steps}

You now have a Form Data Model (FDM) with data sources added to it. Next, you can edit the Form Data Model (FDM) to add and configure data model objects and services, add associations between data model objects, edit properties, add custom data model objects and properties, generate sample data, and so on.

For more information, see [Work with form data model](work-with-form-data-model.md).


>[!MORELIKETHIS]
>
>* [Use Form Data Model(FDM)](/help/forms/using-form-data-model.md)