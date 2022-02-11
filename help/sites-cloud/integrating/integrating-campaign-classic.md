---
title: Integrating with Adobe Campaign Classic
description: Integrating with Adobe Campaign Classic 
feature: Administering
role: Admin
---

# Integrating with Adobe Campaign Classic {#integrating-campaign-classic}

Adobe Campaign lets you manage email delivery content and forms directly in AEM as a Cloud Service. To use both solutions together at the same time, you must first configure them to connect to one another. This involves configuration steps in both Adobe Campaign Classic and AEM as a Cloud Service.

Be aware that AEM as a Cloud Service and Adobe Campaign Classic can be used independently. For example, marketers can start creating their campaigns and targeting in Adobe Campaign, while content creators can work on the design in AEM as a Cloud Service.

## Integration workflow {#integration-workflow}

This page details the configuration steps needed in both Adobe Campaign Classic and AEM as a Cloud Service to integrate the solutions.
Since the starting point is the Adobe Campaign Classic installation you may have already performed some of the configuration steps presented below. In such a case, please jump to the appropiate chapter according to your current configuration.

For Adobe Campaign Classic you will learn how to:

* [Install Adobe Campaign Classic](#acc-installation)
* [First start-up the Adobe Campaign Classic server](#first-startup)
* [Create the Adobe Campaign Classic Instance](#instance-creation)
* [Create a Database](#creation-database)
* [Create the Operator User](#create-operator)

On the AEM as a Cloud Service side you will learn how to:

* [Configure AEM as a Cloud Service for the integration](#aem-configuration)
* [Configure the Campaign Remote User](#configure-user)
* [Setup the Adobe Campaign Classic External Account](#acc-setup)

Having configured both Adobe Campaign Classic and AEM as a Cloud Service, you will then learn how to create an [Adobe Experience Manager Newsletter](#creating-newsletter).

## Adobe Campaign Classic Configuration {#campaign-classic-configuration}

In the following chapters you will learn how to install, setup and configure Adobe Campaign Classic so it can be integrated with AEM as a Cloud service. Please be aware that in order to perform the operations presented below you must have the **administration** role in Adobe Campaign.

### Prerequisites {#prerequisites-campaign-classic}

To install and configure Adobe campaign classic you need the following:

1. Install java 7 or later.
1. Install Postgres.
1. Install PgAdmin.

### Installing Adobe Campaign Classic {#acc-installation}

If you do not have Adobe Campaign Classic installed follow these steps:

1. Download the Adobe Campaign Classic installation from the Adobe software distribution portal as per your [platform](https://experience.adobe.com/#/downloads/content/software-distribution/en/campaign.html)
1. Locate the setup.exe file in the extracted folder.
1. Run setup.exe as an administrator (right-click and run as administrator) and click **Next**.
1. Select the installation type as **Application server** and click **Next**.
>[!NOTE]
>Be aware that there are several installation types available depending on your requirements:
>**Installation of an application server** : Install the Adobe Campaign application server and the client console.
>**Minimal installation (Network)**: Installation of the client's machine from the network.
>**Installation of a client**: Installation of the required components for the Adobe Campaign client.
>**Custom installation**: The customer chooses the elements that will be installed.
1. Select the installation directory and click **Next**.
1. Click **Finish**.

Once the installation is complete, a message window will appear. Click the **Finish** button.

>[!NOTE]
>
>Once the server installation is complete you can reboot the server to avoid any network issues.

### First start-up of the Adobe Campaign Classic Server {#first-startup}

After the installation is complete you can start up the server Adobe Campaign Classic Server. Follow the steps below to ensure a smooth startup:

1. Start command prompt as an administrator
1. Navigate to the Adobe Campaign directory, for example: `C:\Program Files\Adobe\Adobe Campaign Classic v7`
1. Run the following command: `nlserver web`
   * Press Ctrl+C to stop the process, then enter the following command: (unclear/more context)
1. Run the following command to setup the password: `nlserver config -internalpassword`
   * The user name is internal and default password is "empty/blank" (unclear/more context)
1. Enter following command to start the server: `nlserver start web`
   >[!NOTE]
   >
   >If needed, you can enter the following command to stop the server `nlserver stop web`.
1. Open the hosts file as administrator in any text editor.
1. Add an entry for your Adobe Campaign Classic server's name: `127.0.0.1 <server name>.corp.adobe.com`. For example:

```
127.0.0.1   acc-test.corp.adobe.com

```

### Creating the Adobe Campaign Classic Instance {#instance-creation}

After the server startup, follow these steps to create an Adobe Campaign Classic instance:

1. Open the Adobe Campaign Classic client from the start menu.
1. Click on the Adobe Inc. v6 link.
1. Double click on Adobe Inc. v6 under Connections and add the Adobe Campaign Classic server FQN in the connection URL field. The default port for the Adobe Campaign Classic server is 8080. Click **OK** to save.
1. Login with your credentials. The user name and the password is what you set in the previous steps of the [First start-up of the server](#first-startup) procedure.

### Creating the Database {#creation-database}

Since this is first time you log in the **Declare a new instance** window is displayed. You will now be able to create a database, as follows:

1. In the Declare a new instance window:
   * Enter the `<server name>` into the Name field (we set acc-test, note that the system will change this to acc_test) (unclear/more context)
   * Enter * into the DNS masks field
   * Choose the language
Once you've clicked ok, you will go back to the login page. Log in again with your credentials.
1. The database creation wizard will appear.
   * Choose PostgreSQL as Engine
   * Enter localhost in field Server
   * Choose Create or recycle a database
   * Click **Next**.
1. Enter the user name and password for the postgresSQL admin account (postgres/postgres) (unclear/more context)
   * Click **Next**.
1. On the database creation screen, enter the following details:
   * Enter a name for the database to be created (for example, campaign)
   * Switch to Create a new user account for this database
   * Specify a database account and password
   * (optional) You can leave everything else as the default
   * Click **Next**.
1. Select the following packages to install:
   * Delivery
   * Marketing campaigns (Campaign)
   * AEM integration
   * Click **Next**.
1. Enter the password on the Creation Steps screen(admin) (unclear/more context) and click **Next**.
1. Click on the **Start** button to start the database creation execution. Click **Close** after progress the bar is full.

### Creating the Operator user {#create-operator}

After the database creation you need to create an Operator user, as follows:

Open the Adobe Campaign Classic client console from start menu and log in. The home page should appear.

1. Click on **Explorer** to open the Explorer view.
1. In the tree view on the left, navigate to **Administration->Access Management->Operators**.
1. Double-click on the `aemserver` entry in the Operators list on the right.
1. Switch to the **Edit** tab. Set the password for the aemserver.
1. Click on the **Access rights** tab and click on the **Edit the access parameters** link under the security settings.
1. Under Encryption, select public network as the authorized connection zone. Click **OK**.
1. Click on **Save**.
1. Log out using the ACC client. (unclear)
1. Go to the Adobe Campaign Classic v7 install location, for example `C:\Program Files\Adobe\Adobe Campaign Classic v7\conf` and open the serverConf.xml as an administrator.
    * Search for **security zone**
    * Set the following parameters `allowHTTP="true"` `sessionTokenOnly="true"` `allowUserPassword="true"`
    * Save the file
1. Ensure that the security zone does not get overridden by the respective setting in `config-<server name>.xml` file (C:\Program Files\Adobe\Adobe Campaign Classic v7\conf\config_acc-test.xml).
    * If the configuration file contains a separate security zone setting then change the `allowUserPassword` attribute to true.
1. If you want to change the Adobe Campaign Classic server port, replace 8080 with the desired port(for example: 80).
>[!NOTE]
>
>By default, no security zone is configured for the operator. To connect to Adobe Campaign with AEM as a Cloud Service, you must select one (see the steps above). We strongly recommend creating a security zone dedicated to AEM to avoid any security problems.

## AEM as a Cloud Service Setup {#aem-setup}

After installing and configuring Adobe Campaign Classic you need to configure the AEM as a Cloud service solution.

### Configuring AEM as a Cloud service {#aem-configuration}

1. Log into cloud manager and launch the AEM as a Cloud Service author instance.
1. Go to **Tools→Cloud Service→Legacy Cloud Service**.
1. Scroll down to Adobe Campaign and click on the **Configure Now** link.
    * Enter a title
    * Enter a name
    * Click **Create**
1. On the Edit Component screen
    * Enter the Username, See [Create the Operator User](#create-operator)
    * Enter the Password
    * Enter the Adobe Campaign Classic server API end point (for example, `http://3.22625.51:80`)
    * Click **Connect to Adobe Campaign**
    * Click **OK**.
    >[!NOTE]
    >
    >Please make sure that your Adobe Campaign server is reachable on the internet as AEM as a Cloud Service can not reach private networks.
1. Please check the publish instance in the Link Externalizer configuration.
You can check this configuration by checking the status dump (unclear/more context) of the OSGi services in the developer console.
If it is not correct then make changes in git and then deploy the configuration by using cloud manager (link needed).

```
Service 3310 - [com.day.cq.commons.Externalizer] (pid: com.day.cq.commons.impl.ExternalizerImpl)",
"  from Bundle 420 - Day Communique 5 Commons Library (com.day.cq.cq-commons), version 5.12.16",
"    component.id: 2149",
"    component.name: com.day.cq.commons.impl.ExternalizerImpl",
"    externalizer.contextpath: ",
"    externalizer.domains: [local https://author-p17558-e33255-cmstg.adobeaemcloud.com, author https://author-p17558-e33255-cmstg.adobeaemcloud.com,
     publish https://publish-p17558-e33255-cmstg.adobeaemcloud.com]",
"    externalizer.encodedpath: false",
"    externalizer.host: ",
"    feature-origins: [com.day.cq:cq-quickstart:slingosgifeature:cq-platform-model_quickstart_author:6.6.0-V23085]",
"    service.bundleid: 420",
"    service.description: Creates absolute URLs",
"    service.scope: bundle",
"    service.vendor: Adobe Systems Incorporated",

```

>[!NOTE]
>
>The publish instance must also be reachable from the Adobe Campaign server.

### Configuring the Campaign Remote User {#configure-user}

You need to set the password for the campaign-remote user. It is necessary in order to connect Adobe Campaign Classic with AEM as a Cloud service.

1. Go to **AEM→Tools→Security→Users**.
1. Search for the `campaign-remote` user and click on it.
1. Click on Change Password
    * Enter the new password twice
    * Enter your AEM password
    * Click **Save**.

### Configuring the Adobe Campaign Classic External Account {#acc-setup}

You must configure an external account in order to connect Adobe Campaign Classic with the AEM as a Cloud Service instance.

1. Log into the Adobe Campaign Classic server by using the client console.
1. Go to the Explorer View.
1. In the tree view on the left, go to **Administration→Platform→External Accounts**.
1. In the list view on the top right, click AEM instance.
1. In the AEM instance configuration
    * Enter AEM as a Cloud Service author IP/FQN for example `https://author-p17558-e33255-cmstg.adobeaemcloud.com`.
    * Enter the user and account (for example campaign-remote)
    * Enter the password for campaign-remote user which you set in the AEM as a Cloud Service instance (see the procedure above)
    * Select the **Enabled** checkbox
    * Click **Save**.
    >[!NOTE]
    >
    >The AEM Author server IP/FQN must be reachable from the Adobe Campaign Classic server instance. Also do not add the backslash character in the AEM Author server IP/FQN.

## Creating an Adobe Experience Manager Newsletter {#creating-newsletter}

Having configured both Adobe Campaign Classic and AEM as a Cloud Service, you will now learn how to create an Adobe Experience Manager Newsletter.

1. From the AEM author instance, click the Adobe Experience Manager logo in the upper left side of the page and select **Sites**.
1. Select Campaign, click **Create→Page**.
1. Select Brand and click **Next**.
1. Enter the title and click **Create** and **Done**.
1. To create a Campaign page, go to **Campaign→AdobeDemo→Master** and click on **Create→Page**.
1. Select the Campaign template then click **Next** and **Done**
1. Enter the Title (for example: CampaignPage), click **Create** and **Done**.
1. Go to **Campaign→AdobeDemo→Master**and select the CampaignPage checkbox. Click on **Properties** on the top left.
1. Go to the Cloud Service tab
    * Select Adobe Campaign from Cloud Service Configurations drop-down list.
    * Select the desired name for the Adobe Campaign configuration(for example, AEM-ACC-AWS_WIN180521).
    * **Save** and **Close**.
1. To create an Adobe Campaign Classic Email page, go to **Campaign→AdobeDemo→Master→CampaignPage** and click on **Create→Page**.
1. Select the Adobe Campaign Email(for example, AC 6.1) template and click **Next**.
1. On the Create page, enter the title for newsletter, click **Create** and **Done**.
1. Go to **Campaign→AdobeDemo→Master→CampaignPage**, select the Campaign Classic checkbox and click on **Edit** on top left to open the email page.
1. Edit the Adobe Campaign Classic email newsletter page as per your requirements.
1. Click on **Page Information** button on top left and click on **Publish Page**.
1. Select the configuration on which the page has to be published. Click **Publish**.
1. The newsletter page has been published on the publish instance and also on the AEM-Adobe Campaign Classic configuration.
    * Now the newsletter page will be visible in Adobe Campaign Classic
1. Click on the Page Information button and click on **Start Workflow**
1. Select **Approve for Adobe Campaign** as the workflow model and click on the **Start Workflow** button.
1. A disclaimer appears on top of the page. Click **Complete** to confirm the review and again click **OK**.
1. Click **Complete** and select **Newsletter approval** in the Next Step drop-down list and click **OK** button.

### Creating a Recipient {#creating-recipient}

1. Open the Adobe Campaign Classic server by using the Adobe Campaign Classic client console.
1. Go to the Explorer view.
1. In the tree view on the left, go to Profiles and Targets and select **Recipients**.
1. Fill the Details of the recipient.
   * Enter the First name
   * Enter the Last Name
   * Enter the Email
   * Click **Save**.

### Creating an Email Delivery in Adobe Campaign Classic {#create-delivery}

1. Open the Adobe Campaign Classic server by using the Adobe Campaign Classic client console.
1. Go to the Explorer view.
1. In the tree view on the left, select **Campaign Management** and select **Deliveries**.
1. On top right corner, click on **New**.
1. Select **Email Delivery with AEM Content** from the Delivery template drop-down list and click **Continue**.
1. Click on From link under Email parameters.
    * Enter the Sender address
    * Enter the From field
    * Click **OK**.
1. Click on **To** link then click on **Add** on the select target screen
1. Select **A recipient** and click **Next**.
1. Select the recipient created [previously](#creating-recipient) and click **Finish**.
1. The recipient has been selected. Click **OK**.
1. Click **Synchonize**.
1. Select the email page from the list, click **OK**.
1. The email template is synchronized.  Click **Refresh Content** if it is not loaded.
1. Click on **Send** to send the email.
1. On next screen, select **Delivery as soon as possible** and then click **Analyze**.
1. Now as the delivery has been created, click on **Confirm Delivery** to start sending the email. Click **Yes** to confirm.
1. The delivery has started. Click **Close**.
1. Click **Save** to save the delivery.
