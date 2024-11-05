---
title: How to Configure Data Sources?
description: Learn how to configure RESTful web services, SOAP-based web services, and OData services as data sources for a form data model (FDM).
feature: Adaptive Forms, Form Data Model
role: User, Developer
level: Beginner
exl-id: cb77a840-d705-4406-a94d-c85a6efc8f5d
---

# Configure data sources {#configure-data-sources}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/form-data-model/configure-data-sources.html)                  |
| AEM as a Cloud Service     | This article        |

![Data integration](do-not-localize/data-integeration.png)

[!DNL Experience Manager Forms] Data Integration lets you configure and connect to disparate data sources. The following types are supported out-of-the-box:

* Relational databases - MySQL, [!DNL Microsoft® SQL Server], [!DNL IBM® DB2®], postgreSQL, and [!DNL Oracle RDBMS] 
* RESTful web services  
* SOAP-based web services
* OData services (Version 4.0)
* Microsoft&reg; Dynamics
* SalesForce
* Microsoft&reg; Azure Blob Storage

Data integration supports OAuth2.0([Authorization Code](https://oauth.net/2/grant-types/authorization-code/), [Client Credentials](https://oauth.net/2/grant-types/client-credentials/)), Basic Authentication, and API Key authentication types out-of-the-box, and allows implementing custom authentication for accessing web services. While RESTful, SOAP-based, and OData services are configured in [!DNL Experience Manager] as a Cloud Service, JDBC for relational databases and connector for [!DNL Experience Manager] user profile are configured in [!DNL Experience Manager] web console.

## Configure relational database {#configure-relational-database}

### Prerequisites

Before configuring relational databases using [!DNL Experience Manager] Web Console Configuration, it is mandatory to:
* [Enable advanced networking through the cloud manager API](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/networking/advanced-networking.html), as ports are disabled by default.  
* [Add JDBC driver dependencies in Maven](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/networking/examples/sql-datasourcepool.html?lang=en#mysql-driver-dependencies).


### Steps to configure a relational database

You can configure relational databases using [!DNL Experience Manager] Web Console Configuration. Do the following:

1. Go to [!DNL Experience Manager] web console at `https://server:host/system/console/configMgr`.
1. Locate **[!UICONTROL Day Commons JDBC Connections Pools]** configuration. Select to open the configuration in edit mode.

   ![JDBC Connector Pool](/help/forms/assets/jdbc_connector.png)

1. In the configuration dialog, specify the details for the database you want to configure, such as:

    * Java&trade; class name for the JDBC driver
    * JDBC connection URI
    * Username and password to establish connection with the JDBC driver
    * Specify a SQL SELECT query in the **[!UICONTROL Validation Query]** field to validate connections from the pool. The query must return at least one row. Based on your database, specify one of the following:
      * SELECT 1 (MySQL and MS® SQL) 
      * SELECT 1 from dual (Oracle)
    * Name of the data source

   Sample strings for configuring a relational database:

   ```text
      "datasource.name": "sqldatasourcename-mysql",
      "jdbc.driver.class": "com.mysql.jdbc.Driver",
      "jdbc.connection.uri": "jdbc:mysql://$[env:AEM_PROXY_HOST;default=proxy.tunnel]:30001/sqldatasourcename"
   ```

   >[!NOTE]
   >
   > See [SQL connections using JDBC DataSourcePool](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/networking/examples/sql-datasourcepool.html) for more detailed information.
    
1. Select **[!UICONTROL Save]** to save the configuration.

Now, you can use the configured relational database with your Form Data Model (FDM). 

<!-- ## Configure [!DNL Experience Manager] user profile {#configure-aem-user-profile}

You can configure [!DNL Experience Manager] user profile using User Profile Connector configuration in [!DNL Experience Manager] Web Console. Do the following:

1. Go to [!DNL Experience Manager] web console at `https://[server]:[port]/system/console/configMgr`.
1. Look for **[!UICONTROL AEM Forms Data Integrations - User Profile Connector Configuration]** and select to open the configuration in edit mode.
1. In the User Profile Connector Configuration dialog, you can add, remove, or update user profile properties. The specified properties are available for use in form data model (FDM). Use the following format to specify user profile properties:

   `name=[property_name_with_location_in_user_profile],type=[property_type]`

   Examples:

    * `name=profile/phoneNumber,type=string`
    * `name=profile/empLocation/*/city,type=string`

   >[!NOTE]
   >
   >The **&#42;** in the above example denotes all nodes under the `profile/empLocation/` node in [!DNL Experience Manager] user profile in CRXDE structure. It means that the Form Data Model (FDM) can access the `city` property of type `string` present in any node under the `profile/empLocation/` node. However, the nodes that contain the specified property must follow a consistent structure.

1. Select **[!UICONTROL Save]** to save the configuration. -->

## Configure folder for cloud service configurations {#cloud-folder}

Configuration for cloud services folder is required for configuring cloud services for RESTful, SOAP, and OData services.

All cloud service configurations in [!DNL Experience Manager] are consolidated in the `/conf` folder in [!DNL Experience Manager] repository. By default, the `conf` folder contains the `global` folder where you can create cloud service configurations. However, you must manually enable it for cloud configurations. You can also create additional folders in `conf` to create and organize cloud service configurations.

To configure the folder for cloud service configurations:

1. Go to **[!UICONTROL Tools > General > Configuration Browser]**.
   * See the [Configuration Browser](https://experienceleague.adobe.com/docs/experience-manager-65/administering/introduction/configurations.html) documentation for more information.
1. Do the following to enable the global folder for cloud configurations or skip this step to create and configure another folder for cloud service configurations.

    1. In the **[!UICONTROL Configuration Browser]**, select the `global` folder and select **[!UICONTROL Properties]**.

    1. In the **[!UICONTROL Configuration Properties]** dialog, enable **[!UICONTROL Cloud Configurations]**.

    1. Select **[!UICONTROL Save & Close]** to save the configuration and exit the dialog.

1. In the **[!UICONTROL Configuration Browser]**, select **[!UICONTROL Create]**.
1. In the **[!UICONTROL Create Configuration]** dialog, specify a title for the folder, and enable **[!UICONTROL Cloud Configurations]**.
1. Select **[!UICONTROL Create]** to create the folder enabled for cloud service configurations.

## Configure RESTful web services {#configure-restful-web-services}

RESTful web services can be described using [Swagger specifications](https://swagger.io/specification/v2/) in JSON or YAML format in a [!DNL Swagger] definition file. To configure RESTful web service in [!DNL Experience Manager] as a Cloud Service, ensure that you have either the [!DNL Swagger] file ([Swagger Version 2.0](https://swagger.io/specification/v2/)) or [!DNL Swagger] file ([Swagger Version 3.0](https://swagger.io/specification/v3/)) on your file system or the URL where the file is hosted.

### Configure RESTful services for Open API Specification version 2.0 {#configure-restful-services-open-api-2.0}

1. Go to **[!UICONTROL Tools > Cloud Services > Data Sources]**. Select to select the folder where you want to create a cloud configuration.

   See [Configure folder for cloud service configurations](configure-data-sources.md#cloud-folder) for information about creating and configuring a folder for cloud service configurations.

1. Select **[!UICONTROL Create]** to open the **[!UICONTROL Create Data Source Configuration wizard]**. Specify a name and optionally a title for the configuration, select **[!UICONTROL RESTful Service]** from the **[!UICONTROL Service Type]** drop-down, optionally browse and select a thumbnail image for the configuration, and select **[!UICONTROL Next]**.
1. Specify the following details for the RESTful service:

    * Select a URL or File from the [!UICONTROL Swagger Source] drop-down, and accordingly specify the [!DNL Swagger URL] to the[!DNL  Swagger] definition file or upload the [!DNL Swagger] file from your local file system.
    * Based on the[!DNL  Swagger] Source input., the following fields are pre-populated with values:

        * Scheme: The transfer protocols used by the REST API. The number of scheme types that display in the drop-down list depend on the schemes defined in the [!DNL Swagger] source.
        * Host: The domain name or IP address of the host that serves the REST API. It is a mandatory field.
        * Base Path: The URL prefix for all API paths. It is an optional field.  
          If necessary, edit the pre-populated values for these fields.

    * Select the authentication type — None, OAuth2.0([Authorization Code](https://oauth.net/2/grant-types/authorization-code/), [Client Credentials](https://oauth.net/2/grant-types/client-credentials/)), Basic Authentication, API Key, or Custom Authentication — to access the RESTful service, and accordingly provide details for authentication.

    If you select **[!UICONTROL API Key]** as the authentication type, specify the value for the API key. The API key can be sent as a request header or as a query parameter. Select one of these options from the **[!UICONTROL Location]** drop-down list and specify the name of the header or the query parameter in the **[!UICONTROL Parameter Name]** field accordingly.

    <!--If you select **[!UICONTROL Mutual Authentication]** as the authentication type, see [Certificate-based mutual authentication for RESTful and SOAP web services](#mutual-authentication).-->

1. Select **[!UICONTROL Create]** to create the cloud configuration for the RESTful service.

### Configure RESTful services for Open API Specification version 3.0 {#configure-restful-services-open-api-3.0}

1. Go to **[!UICONTROL Tools > Cloud Services > Data Sources]**. Select to select the folder where you want to create a cloud configuration.

   See [Configure folder for cloud service configurations](configure-data-sources.md#cloud-folder) for information about creating and configuring a folder for cloud service configurations.

1. Select **[!UICONTROL Create]** to open the **[!UICONTROL Create Data Source Configuration wizard]**. Specify a name and optionally a title for the configuration, select **[!UICONTROL RESTful Service]** from the **[!UICONTROL Service Type]** drop-down, optionally browse and select a thumbnail image for the configuration, and select **[!UICONTROL Next]**.
1. Specify the following details for the RESTful service:

    * Select a URL or File from the [!UICONTROL Swagger Source] drop-down, and accordingly specify the [!DNL Swagger 3.0 URL] to the[!DNL  Swagger] definition file or upload the [!DNL Swagger] file from your local file system.
    * Based on the[!DNL  Swagger] Source input, the connection information with the target server is displayed.
    * Select the authentication type — None, OAuth2.0([Authorization Code](https://oauth.net/2/grant-types/authorization-code/), [Client Credentials](https://oauth.net/2/grant-types/client-credentials/)), Basic Authentication, API Key, or Custom Authentication — to access the RESTful service, and accordingly provide details for authentication.

    If you select **[!UICONTROL API Key]** as the authentication type, specify the value for the API key. The API key can be sent as a request header or as a query parameter. Select one of these options from the **[!UICONTROL Location]** drop-down list and specify the name of the header or the query parameter in the **[!UICONTROL Parameter Name]** field accordingly.

    <!--If you select **[!UICONTROL Mutual Authentication]** as the authentication type, see [Certificate-based mutual authentication for RESTful and SOAP web services](#mutual-authentication).-->

1. Select **[!UICONTROL Create]** to create the cloud configuration for the RESTful service.

Some of the operations not supported by RESTful services Open API Specification version 3.0  are:
* Callbacks
* oneof/anyof
* Remote reference
* Links
* Different request bodies for different MIME types for a single operation

See [OpenAPI 3.0 Specification](https://swagger.io/specification/v3/) for detailed information. 

### Form data model (FDM) HTTP client configuration to optimize performance {#fdm-http-client-configuration}

[!DNL Experience Manager Forms] form a data model when integrating with RESTful web services as the data source includes HTTP client configurations for performance optimization. 

Set the following properties of the **[!UICONTROL Form Data Model HTTP Client Configuration for REST data source]** configuration to specify the regular expression:

* Use the `http.connection.max.per.route` property to set the maximum number of permitted connections between form data model (FDM) and RESTful web services. The default value is 20 connections.

* Use the `http.connection.max` property to specify the maximum number of permitted connections for each route. The default value is 40 connections.

* Use the `http.connection.keep.alive.duration` property to specify the duration, for which a persistent HTTP connection is kept alive. The default value is 15 seconds.

* Use the `http.connection.timeout` property to specify the duration, for which the [!DNL Experience Manager Forms] server waits for a connection to establish. The default value is 10 seconds.

* Use the `http.socket.timeout` property to specify the maximum time period for inactivity between two data packets. The default value is 30 seconds.

The following JSON file displays a sample:


```json
{   
   "http.connection.keep.alive.duration":"15",   
   "http.connection.max.per.route":"20",   
   "http.connection.timeout":"10",   
   "http.socket.timeout":"30",   
   "http.connection.idle.connection.timeout":"15",   
   "http.connection.max":"40" 
} 
```

1. Select **[!UICONTROL Form Data Model HTTP Client Configuration for REST data source]**.

1. In the [!UICONTROL Form Data Model HTTP Client Configuration for REST data source] dialog:

   * Specify the maximum number of permitted connections between form data model (FDM) and RESTful web services in the **[!UICONTROL Connection limit in total]** field. The default value is 20 connections.

   * Specify the maximum number of permitted connections for each route in the **[!UICONTROL Connection limit on per route basis]** field. The default value is two connections.

   * Specify the duration, for which a persistent HTTP connection is kept alive, in the **[!UICONTROL Keep alive]** field. The default value is 15 seconds.

   * Specify the duration, for which the [!DNL Experience Manager Forms] server waits for a connection to establish, in the **[!UICONTROL Connection timeout]** field. The default value is 10 seconds.

   * Specify the maximum time period for inactivity between two data packets in the **[!UICONTROL Socket timeout]** field. The default value is 30 seconds.

## Configure SOAP web services {#configure-soap-web-services}

SOAP-based web services are described using [Web Services Description Language (WSDL) specifications](https://www.w3.org/TR/wsdl). [!DNL Experience Manager Forms] do not support the RPC-style WSDL model.

To configure SOAP-based web service in [!DNL Experience Manager] as a Cloud Service, ensure that you have the WSDL URL for the web service, and do the following:

1. Go to **[!UICONTROL Tools > Cloud Services > Data Sources]**. Select to select the folder where you want to create a cloud configuration.

   See [Configure folder for cloud service configurations](configure-data-sources.md#cloud-folder) for information about creating and configuring a folder for cloud service configurations.

1. Select **[!UICONTROL Create]** to open the **[!UICONTROL Create Data Source Configuration wizard]**. Specify a name and optionally a title for the configuration, select **[!UICONTROL SOAP Web Service]** from the **[!UICONTROL Service Type]** drop-down, optionally browse and select a thumbnail image for the configuration, and select **[!UICONTROL Next]**.
1. Specify the following for the SOAP web service:

    * WSDL URL for the web service.
    * Service Endpoint. Specify a value in this field to override the service endpoint mentioned in WSDL.
    * Select the authentication type — None, OAuth2.0([Authorization Code](https://oauth.net/2/grant-types/authorization-code/), [Client Credentials](https://oauth.net/2/grant-types/client-credentials/)), Basic Authentication, or Custom Authentication — to access the SOAP service, and accordingly provide the details for authentication.

      <!--If you select **[!UICONTROL X509 Token]** as the Authentication type, configure the X509 certificate. For more information, see [Set up certificates](install-configure-document-services.md#set-up-certificates-for-reader-extension-and-encryption-service).-->
      <!--Specify the KeyStore alias for the X509 certificate in the **[!UICONTROL Key Alias]** field. Specify the time, in seconds, until the authentication request remains valid, in the **[!UICONTROL Time To Live]** field. Optionally, select to sign the message body or timestamp header or both.-->

      <!--If you select **[!UICONTROL Mutual Authentication]** as the authentication type, see [Certificate-based mutual authentication for RESTful and SOAP web services](#mutual-authentication).-->

1. Select **[!UICONTROL Create]** to create the cloud configuration for the SOAP web service.

### Enable the use of import statements in SOAP web services WSDL {#enable-import-statements}

You can specify a regular expression that serves as the filter for absolute URLs that are allowed as import statements in SOAP web services WSDL. By default, there is no value in this field. As a result, [!DNL Experience Manager] blocks all import statements available in WSDL. If you specify `.*` as the value in this field, [!DNL Experience Manager] allows all import statements.

Set the `importAllowlistPattern` property of the **[!UICONTROL Form Data Model SOAP Web Services Import Allowlist]** configuration to specify the regular expression. The following JSON file displays a sample:

```json
{
  "importAllowlistPattern": ".*"
}
```

To set values of a configuration, [Generate OSGi Configurations using the AEM SDK](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/deploying/configuring-osgi.html?lang=en#generating-osgi-configurations-using-the-aem-sdk-quickstart), and [deploy the configuration](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/deploy-code.html?lang=en#deployment-process) to your Cloud Service instance.

## Configure OData services {#config-odata}

An OData service is identified by its service root URL. To configure an OData service in [!DNL Experience Manager] as a Cloud Service, ensure that you have service root URL for the service, and do the following:

>[!NOTE]
>
> Form data model (FDM) supports [OData version 4](https://www.odata.org/documentation/).
>For a step-by-step guide to configure [!DNL Microsoft®&reg; Dynamics 365], online or on-premises, see [[!DNL Microsoft&reg; Dynamics] OData Configuration](ms-dynamics-odata-configuration.md).

1. Go to **[!UICONTROL Tools > Cloud Services > Data Sources]**. Select to select the folder where you want to create a cloud configuration.

   See [Configure folder for cloud service configurations](#cloud-folder) for information about creating and configuring a folder for cloud service configurations.

1. Select **[!UICONTROL Create]** to open the **[!UICONTROL Create Data Source Configuration wizard]**. Specify a name and optionally a title for the configuration, select **[!UICONTROL OData Service]** from the **[!UICONTROL Service Type]** drop-down, optionally browse and select a thumbnail image for the configuration, and select **[!UICONTROL Next]**.
1. Specify the following details for the OData service:

    * Service Root URL for the OData service to be configured.
    * Select the authentication type — None, OAuth2.0([Authorization Code](https://oauth.net/2/grant-types/authorization-code/), [Client Credentials](https://oauth.net/2/grant-types/client-credentials/)), Basic Authentication, API Key, or Custom Authentication — to access the OData service, and accordingly provide the details for authentication.

    If you select **[!UICONTROL API Key]** as the authentication type, specify the value for the API key. The API key can be sent as a request header or as a query parameter. Select one of these options from the **[!UICONTROL Location]** drop-down list and specify the name of the header or the query parameter in the **[!UICONTROL Parameter Name]** field accordingly.

   >[!NOTE]
   >
   >Select the OAuth 2.0 authentication type to connect with [!DNL Microsoft®&reg; Dynamics] services using the OData endpoint as the service root.

1. Select **[!UICONTROL Create]** to create the cloud configuration for the OData service.

<!--
## Configure Microsoft® SharePoint List {#config-sharepoint-list}

<span class="preview"> This is a pre-release feature and accessible through our [pre-release channel](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/release-notes/prerelease.html#new-features). </span>

To save data in a tabular form use, Microsoft® SharePoint List. To configure a Microsoft SharePoint List in [!DNL Experience Manager] as a Cloud Service, do the following:

1. Go to **[!UICONTROL Tools]** > **[!UICONTROL Cloud Services]** >  **[!UICONTROL Microsoft® SharePoint]**.   
1. Select a **Configuration Container**. The configuration is stored in the selected Configuration Container. 
1. Click **[!UICONTROL Create]** > **[!UICONTROL SharePoint List]** from the drop-down list. The SharePoint configuration wizard appears.  
1. Specify the **[!UICONTROL Title]**, **[!UICONTROL Client ID]**, **[!UICONTROL Client Secret]** and **[!UICONTROL OAuth URL]**. For information on how to retrieve Client ID, Client Secret, Tenant ID for OAuth URL, see [Microsoft&reg; Documentation](https://learn.microsoft.com/en-us/graph/auth-register-app-v2).
    * You can retrieve the `Client ID` and `Client Secret` of your app from the Microsoft&reg; Azure portal.
    * In the Microsoft&reg; Azure portal, add the Redirect URI as `https://[author-instance]/libs/cq/sharepointlist/content/configurations/wizard.html`. Replace `[author-instance]` with the URL of your Author instance.
    * Add the API permissions `offline_access` and `Sites.Manage.All` in the **Microsoft® Graph** tab to provide read/write permissions. Add `AllSites.Manage` permission in the **Sharepoint** tab to interact remotely with SharePoint data.
    * Use OAuth URL: `https://login.microsoftonline.com/tenant-id/oauth2/v2.0/authorize`. Replace `<tenant-id>` with the `tenant-id` of your app from the Microsoft&reg; Azure portal.

      >[!NOTE]
      >
      > The **client secret** field is mandatory or optional depends upon your Azure Active Directory application configuration. If your application is configured to use a client secret, it is mandatory to provide the client secret.

1. Click **[!UICONTROL Connect]**. On a successful connection, the `Connection Successful` message appears.
1. Select **[!UICONTROL SharePoint Site]** and **[!UICONTROL SharePoint List]** from the drop-down list.
1. Select **[!UICONTROL Create]** to create the cloud configuration for the Microsoft® SharePointList.

-->

<!--## Certificate-based mutual authentication for RESTful and SOAP web services {#mutual-authentication}

When you enable mutual authentication for form data model (FDM), both the data source and [!DNL Experience Manager] Server running Form Data Model (FDM) authenticate each other's identity before sharing any data. You can use mutual authentication for REST and SOAP-based connections (data sources). To configure mutual authentication for a Form Data Model (FDM) on your [!DNL Experience Manager Forms] environment:

1. Upload the private key (certificate) to [!DNL Experience Manager Forms] server. To upload the private key:
   1. Log in to your [!DNL Experience Manager Forms] server as an administrator.
   1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Security]** > **[!UICONTROL Users]**. Select the `fd-cloudservice` user and select **[!UICONTROL Properties]**.
   1. Open the **[!UICONTROL Keystore]** tab, expand the **[!UICONTROL Add Private Key from KeyStore file]** option, upload the KeyStore File, specify the aliases, passwords, and select **[!UICONTROL Submit]**. The Certificate is uploaded.  The private key alias is mentioned in the certificate and set while creating the certificate.
1. Upload trust certificate to Global Trust Store. To upload the certificate:
   1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Security]** > **[!UICONTROL Trust Store]**.
   1. Expand the **[!UICONTROL Add Certificate from CER file]** option, select **[!UICONTROL Select Certificate File]**, upload the certificate, and select **[!UICONTROL Submit]**.
1. Configure [SOAP](#configure-soap-web-services) or [RESTful](#configure-restful-web-services) web services as the data source and select **[!UICONTROL Mutual authentication]** as the authentication type. If you configure multiple self-signed certificates for `fd-cloudservice` user, specify the Key Alias name for the certificate.-->

## Next steps {#next-steps}

You have configured the data sources. Next you can create a Form Data Model (FDM) or if you have already created a Form Data Model (FDM) without a data source, you can associate it with the data sources you configured. See [Create form data model](create-form-data-models.md) for details.

<!--

>[!MORELIKETHIS]
>
>* [Configure Azure storage for AEM Forms](/help/forms/configure-azure-storage.md)
>* [Integrate Microsoft Dynamics 365 and Salesforce with Adaptive Forms](/help/forms/configure-msdynamics-salesforce.md)
>*  [Add Forms Portal to an AEM Sites page](/help/forms/configure-forms-portal.md)

-->