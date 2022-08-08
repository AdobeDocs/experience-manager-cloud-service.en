---
title: Creating Campaign Newsletters with AEM
description: Learn how to use AEM to create newsletters that can be sent with Adobe Campaign Classic.
feature: Authoring
role: Author
exl-id: 60a6a9d0-f5e6-424f-b320-dd4943c55d45
---

# Creating Campaign Newsletters with AEM {#creating-newsletters}

In this document you will learn how to use AEM to create newsletters that can be sent with Adobe Campaign Classic.

By leveraging the integration between AEM as a Cloud Service and Adobe Campaign Classic, you can create your newsletters using AEM's powerful authoring tools. Then when you are ready to send your newsletter, you can send it using Campaign's recipient management and distribution features.

## Prerequisites {#prerequisites}

Before you can create a newsletter with AEM and send it with Campaign, you must first [integrate Adobe Campaign Classic and AEM as a Cloud Service.](/help/sites-cloud/integrating/integrating-campaign-classic.md)

## Creating Newsletter Structure {#create-structure}

Newsletter content is managed in AEM much like you would manage your site content. You start by creating a "site" to hold your content. Within this "site" you can collect your newsletters by brand.

1. Sign into your AEM author instance.

1. From the main navigation page, open the **Sites** console.

1. In a standard installation of AEM, there will be an existing **Campaign** folder. Select it and click on the **Create** button and then **Page**.

   ![Create page](assets/create-page.png)

1. Select **Brand** as your site template and click **Next**.

   ![Create brand](assets/create-brand.png)

1. Enter a **Title** and click **Create** and then **Done**.

   ![Provide brand details](assets/create-brand-page.png)

You now have a basic content structure to create your campaigns.

![Content structure](assets/content-structure.png)

## Creating a Campaign {#create-campaign}

Now that you have a basic content structure for your campaign, you can create the campaign itself. The campaign will be used to organize possibly multiple newsletters.

1. Using [column view](/help/sites-cloud/authoring/getting-started/basic-handling.md#viewing-and-selecting-resources) in the sites console, select the brand that you previously created (in this case, **WKND Escapes**) and then select **Master Area**, which was automatically created for you, and then click the **Create** button and then **Page**.

   ![Create campaign page](assets/create-campaign-page.png)

1. Select **Campaign** as the template then click **Next** and **Done**.

   ![Select campaign template](assets/select-campaign-template.png)

1. Enter a **Title** for the campaign and then click **Create** and **Done**.

   ![Campaign title](assets/campaign-title.png)

You now have a campaign where you can create your newsletters.

![Campaign structure](assets/campaign-structure.png)

## Selecting Campaign Configuration {#campaign-configuration}

AEM can support multiple integration configurations. For your new campaign, you must define which configurations to use to send your newsletter content.

1. Using [column view](/help/sites-cloud/authoring/getting-started/basic-handling.md#viewing-and-selecting-resources) in the sites console, find the campaign that you previously created (in this case, **WKND Escape Summer Campaign**) and then select it using the checkbox and then click the **Properties** button on toolbar.

   ![Select campaign](assets/select-campaign.png)

1. In the **Properties** window, select the **Cloud Service** tab to define the integration to use with this campaign.

   * Select **Adobe Campaign** from the **Cloud Service Configurations** drop-down list.
   * Select the desired Adobe Campaign integration configuration from the **Adobe Campaign** drop-down list.
   * Click **Save &amp; Close**.

   ![Campaign configuration properties](assets/campaign-configuration-properties.png)

Your campaign is now linked to your Adobe Campaign integration. You are ready to create a newsletter in AEM and send it with Adobe Campaign.

## Create a Newsletter {#create-newsletter}

You create and manage your newsletters under the campaign content structure that you have already created and configured.

1. Using [column view](/help/sites-cloud/authoring/getting-started/basic-handling.md#viewing-and-selecting-resources) in the sites console, find the campaign that you previously configured (in this case, **WKND Escape Summer Campaign**), select it, and then click the **Create** button and then **Page**.

   ![Create newsletter](assets/create-newsletter.png)

1. In the create page wizard, select the **Adobe Campaign Email (AC 6.1)** template and click **Next**.

   ![Select campaign email template](assets/adobe-campaign-email-template.png)

1. For the **Properties** step of the wizard, enter the **Title** for the newsletter, click **Create** and **Open**.

   ![Title for the newsletter](assets/create-newsletter-wizard-properties.png)

1. Edit the newsletter page as you would any other AEM content page to meet your requirements.

You now have a newsletter ready to send with Adobe Campaign.

## Publishing Your Newsletter {#publishing-newsletter}

1. When you are ready to send your newsletter, click on the **Page Information** button on top left and click on **Publish Page**.
1. Select the configuration on which the page has to be published. Click **Publish**.
![publish page](assets/publish.png)
1. The newsletter page has been published on the publish instance and also on the AEM Adobe Campaign Classic configuration.
    * Now the newsletter page will be visible in Adobe Campaign Classic
1. Click on the Page Information button and click **Start Workflow**.
1. Select **Approve for Adobe Campaign** as the workflow model and click the **Start Workflow** button.
1. A disclaimer appears on the top of the page. Click **Complete** to confirm the review and again click **OK**.
1. Click **Complete** and select **Newsletter approval** in the Next Step drop-down list and click the **OK** button.

## Creating a Recipient {#creating-recipient}

1. Open the Adobe Campaign Classic server by using the Adobe Campaign Classic client console.
1. Go to the Explorer view.
1. In the tree view on the left, go to Profiles and Targets and select **Recipients**.
![recipients](assets/recipients.png)
1. Fill the Details of the recipient.
   * Enter the First name.
   * Enter the Last Name.
   * Enter the Email.
   * Click **Save**.

## Creating an Email Delivery in Adobe Campaign Classic {#create-delivery}

1. Open the Adobe Campaign Classic server by using the Adobe Campaign Classic client console.
1. Go to the Explorer view.
1. In the tree view on the left, select **Campaign Management** and select **Deliveries**.
1. On top right corner, click **New**.
1. Select **Email Delivery with AEM Content** from the Delivery template drop-down list and click **Continue**.
1. Click on From link under Email parameters.
    * Enter the Sender address.
    * Enter the From field.
    * Click **OK**.
1. Click **To** link then click **Add** on the select target screen.
1. Select **A recipient** and click **Next**.
![target type](assets/publish.png)
1. Select the recipient created [previously](#creating-recipient) and click **Finish**.
1. The recipient has been selected. Click **OK**.
1. Click **Synchonize**.
1. Select the email page from the list, click **OK**.
1. The email template is synchronized. Click **Refresh Content** if it is not loaded.
1. Click **Send** to send the email.
1. On next screen, select **Delivery as soon as possible** and then click **Analyze**.
![delivery target](assets/deliverytarget.png)
1. Now as the delivery has been created, click **Confirm Delivery** to start sending the email. Click **Yes** to confirm.
![confirm delivery](assets/confirmdelivery.png)
1. The delivery has started. Click **Close**.
1. Click **Save** to save the delivery.
