---
Title: How to Connect AEM Adaptive Forms with Azure SQL Storage
Description: Learn how to configure an Azure SQL Database connection in AEM Forms and integrate it with your Adaptive Forms to store or retrieve data efficiently using JDBC.
Keywords: Azure SQL integration with AEM Forms, Connecting Adaptive Forms to Azure SQL Database, JDBC connection for Azure SQL in AEM Forms, Storing Adaptive Form data in Azure SQL
feature: Adaptive Forms, Core Components
role: User, Developer
---
# Connect an Adaptive Form to Azure SQL Storage

Adaptive Forms in Adobe Experience Manager (AEM) can integrate with external databases to store or retrieve data. 
This article outlines how to connect an Adaptive Form to an Azure SQL database using JDBC through AEM as a Cloud Service.

> ![NOTE]
> 
> This guide applies to non-sandbox AEM as a Cloud Service environments with advanced networking enabled.

## Advantages 

Integrating Adaptive Forms with Azure SQL offers several benefits:

* **Real-time data interaction:** Enables live reading and writing of data between forms and the Azure database.
* **Scalability:** Azure SQL provides scalable database performance suitable for enterprise-level applications.
* **Centralized data storage:** Keeps form submissions and retrieved data securely stored in one central location.
* **Security compliance:** Leverages Azure's built-in network, firewall, and encryption options to ensure secure communication.
* **Cloud-native integration:** Ideal for modern, cloud-first architectures using AEM as a Cloud Service.

## Prerequisites

* Create [Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/single-database-create-quickstart?view=azuresql&tabs=azure-portal) and ensure **proxy connection** is enabled.
    
    >[!NOTE]
    >
    > Navigate to: `Azure Portal → SQL Server → Security → Networking → Connectivity` to enable **proxy connection**.

   ![Create Azure Db](/help/forms/assets/create-azure-db.png)

* Enable [Advanced networking configured using a dedicated egress IP](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/networking/dedicated-egress-ip-address) for the created Azure database.

    >[!NOTE]
    >
    >    After enabling dedicated egress IP. Go to `Azure Portal → SQL Server → Security → Networking → Public Access` and add the egress IP to the firewall rules.

    ![Egress IP](/help/forms/assets/cretae-azure-db-egress-ip.png)

* Set port forwarding in the cloud environment with:
    * **portOrigin**: Between `30000–30999`
    * **portDest**: `1433` (default port for Azure SQL) 
    For example: `portOrigin: 30433 → portDest: 1433`

        > ![NOTE]
        > 
        > You can contact Adobe Cloud Manager support to configure the port forwarding.


## Steps to Connect Adaptive Forms to Azure SQL

**Step1: Clone AEM as a Cloud Service Git repository**

1. Open the command line and choose a directory to store your AEM as a Cloud Service repository, such as `/cloud-service-repository/`.

1. Run the below command to clone the repository:

    ```
    git clone https://git.cloudmanager.adobe.com/<organization-name>/<app-id>/
    ```

   **Where to find this information?**

   For step-by-step instructions on locating these details, refer to the Adobe Experience League article "[Accessing Git](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#accessing-git)".

   When the command completes successfully, you see a new folder created in your local directory. This folder is named after your application. 

1. Open the repository folder in an editor. 

**Step2: Add Required JARs**

Include the [SQL driver dependency](https://central.sonatype.com/artifact/com.microsoft.sqlserver/mssql-jdbc/12.8.0.jre11?smo=true) to the AEM project via the `all` package.:

>[!NOTE]
>
> To include the SQL dependency in your project, refer to the [SQL driver dependencies](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/networking/examples/sql-datasourcepool#mysql-driver-dependencies) section.

**Step 3: Add JDBC Configuration**

1. Navigate to the following directory within your `<application folder>` where the OSGi configuration for the JDBC pool should be placed:

   ```bash
   cd ui.config/src/jcr_root/apps/<application folder>/osgiconfig/config/
   ```

**Step 4: Create the Azure SQL Connection Configuration File**

1. Create the file:

      ```bash
      com.day.commons.datasource.jdbcpool.JdbcPoolService~<application folder>-sql.cfg.json
      ```

1. Add the below lines of code:

    ```json
    {
    "datasource.name": "azuredbshr",
    "jdbc.driver.class": "com.microsoft.sqlserver.jdbc.SQLServerDriver",
    "jdbc.username": "<azureuser>",
    "jdbc.connection.uri": "jdbc:sqlserver://$[env:AEM_PROXY_HOST;default=proxy.tunnel]:30433;database=testdb;user=<azureuser>;password=<azurepassword>;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30;",
    "jdbc.password": "******",
    "jdbc.validation.query": "SELECT 1"
        }
    ```

    > ![NOTE]
    >
    > Replace `jdbc.username` with actual Azure username and `jdbc.password` with the actual secure password.

**Step 5: Commit and Push the Changes**

Open the terminal and run the below commands:

```bash
git add .
git commit -m "<commit message>"
git push 
```

**Step 6: Deploy the Changes via Cloud Manager Pipeline**

1. Log in to **AEM Cloud Manager**.
1. Navigate to your project and run the pipeline to deploy the changes.

**Step 7: Create a Form Data Model (FDM)**

Once the AEM and Azure setup is complete and the code changes are deployed:

1. Go to AEM Author instance.
1. Navigate to **Tools** > **Forms** > **Data Integrations**.
1. Create new **Form Data Model**.
1. In the **Data Sources** tab, select the created JDBC configuration.
1. Click **[!UICONTROL Create]** and verify the connection.

![Create Form Data Model](/help/forms/assets/create-azure-sql-fdm.png)

**Step 8:  Use the created FDM in an Adaptive Form**

1. Open an Adaptive Form in edit mode.
1. Select the FDM created in the previous step as the data model.
1. Use [data bindings to connect form fields with the Azure SQL data source](/help/forms/work-with-form-data-model.md#add-data-model-objects-and-services) and configure submission action.

## Best Practices

* Use **secrets management** to avoid hardcoding passwords in configuration files.
* Regularly rotate database credentials and update the config securely.
* Monitor JDBC connectivity logs for failures and latency.
* Follow Azure best practices for securing SQL databases and firewall configurations.
* Avoid using high-privilege database accounts for form access.
