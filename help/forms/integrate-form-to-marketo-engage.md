---
Title: How to Integrate Marketo Engage with AEM Forms?
Description: Learn how to integrate your Marketo Engage instance with AEM Forms.
Keywords: How to connect a Marketo instance with form? , Connect a form to Marketo, Integrate a form with Marketo Engage, Integrate an Adaptive Form with a Marketo instance.
Feature: Adaptive Forms, Form Data Model
Role: User, Developer
exl-id: 74cd25f9-1ee1-4f3f-8e02-8714071e7c86
---
# Integrate Marketo Engage with AEM Forms

<span class="preview"> The feature is available under early adopter program. You can write to aem-forms-ea@adobe.com from your official email id to join the early adopter program and request access to the capability. </span>

Integrating AEM Forms with [Adobe Marketo Engage](https://experienceleague.adobe.com/en/docs/marketo/using/home) enables users to leverage the capabilities of Marketo Engage to create business logic from captured data and automate workflows, including smart campaigns and email automation. The configured form can send captured data to Marketo Engage for processing.

## Advantages of integrating Marketo Engage with forms

Below are a few advantages of connecting an AEM form with Adobe Marketo Engage:

* **Simplified integration**: Connecting forms with Marketo Engage eliminates the need to create a separate form data model. The integration process is straightforward and user-friendly.
* **Automated data capture**: It helps in automatically capture form submissions and store them in Marketo, eliminating manual data entry and reducing errors.

* **Lead management**: It streamlines lead management processes by integrating form submissions directly into your marketing database, enabling better tracking and nurturing of leads.

* **Improved campaign performance**: It uses form data to analyze and optimize marketing campaigns, enhancing overall performance and return on investment (ROI).

* **Analytics and reporting**: It helps in gaining access to robust analytics and reporting tools, such as Munchkin, within Marketo to measure the effectiveness of forms and campaigns.

* **Follow-up automation**: It helps in automating follow-up emails and workflows triggered by form submissions, ensuring timely communication with leads.

## Key Benefits of using AEM Forms over alternative Form solutions

The table below outlines the few reasons to choose AEM Forms over other alternative Form solutions:

| **Feature** | **AEM Forms**| **Other Form Solutions** |
|-------------------------------------|----------------------------------------------------------------------|-----------------------------------------------------------|
| **Customizations** | Allows to add specific custom functions, adjust form actions, and modify field behaviors to enhance form interactions, complex workflows | No customization support |
| **Rule Editor**| Supports a built-in Rule Editor for adding logic and conditions.      | No Rule Editor support|
| **Layout Options** | Supports multiple layout options| Limited layout options |
| **Prefill Service** | Offers a Prefill service to auto-populate form data. | No Prefill service available|
| **Embedding in Sites** | Can be embedded in Sites using iFrame| Cannot be embedded in Sites using iFrame|
| **Ease of Integration with Sites**  | No additional learning required; AEM Forms use the same skills as Sites | Additional learning may be required|
| **Data Submission**| Can submit data to various platforms and offers multiple connectors, such as Connect to SharePoint, Connect to OneDrive, Connect to Salesforce, and more.| Can submit data to limited connectors, for example to Salesforce |

## Considerations for integrating Marketo Engage with forms

Some considerations while integrating Marketo Engage with AEM Forms:

* AEM only supports the People(Leads) database among the various Marketo databases.
* Marketo allows the [creation of 10 custom objects](https://experienceleague.adobe.com/en/docs/marketo/using/product-docs/administration/marketo-custom-objects/add-marketo-custom-object-fields) as user-defined objects to store specialized data beyond the standard fields in Leads, supporting unique business needs.
* AEM can access custom objects only if they are associated with the Lead database

## Prerequisites for integrating Marketo Engage with forms

Below are the prerequisites to connect Marketo Engage with AEM Forms:

* A valid Adobe Marketo Engage license
* A working instance of Marketo Engage to [retrieve the Client ID and Client Secret](https://experienceleague.adobe.com/en/docs/marketo/using/product-docs/administration/additional-integrations/create-a-custom-service-for-use-with-rest-api) to create a cloud configuration.

## Create cloud service configuration to connect AEM Forms (Adaptive Forms) with Marketo Engage

![Workflow](/help/forms/assets/workflow-marketo-1.png)

>[!VIDEO](https://video.tv.adobe.com/v/3442865/engage-marketo-aem-forms-aem)

The Cloud configuration connects your Experience Manager instance to the Adobe Marketo Engage instance. Perform the following steps to create a Marketo Engage cloud configuration:

1. Go to **Tools** > **Cloud Services** > **Marketo Engage**.

    ![Marketo Engage](/help/forms/assets/marketo-engage.png)

2. Open a folder to host the configuration and click **Create**. The **Create Marketo Engage Configuration** window appears.

    >[!NOTE]
    >
    > You can also [configure folder for cloud service configurations](/help/forms/configure-data-sources.md#configure-folder-for-cloud-service-configurations).

3. Specify the **Title** of the configuration and credentials to connect to the service. You can retrieve the authentication credentials from the Adobe Marketo Engage dashboard:
   * **Client ID** and **Client Secret** are available in **Admin** > **Integration** > **LaunchPoint** by selecting the custom service and clicking **View Details**.
    * **Identity URL** is available in **Admin** > **Integration** > **Web Services** as **Identity** in the **REST API** section.

4. Click **Connect**.  On a successful connection, the `Authentication Successful` message appears. 
5. Click **[!UICONTROL Create]** to save the cloud configuration settings.

![Marketo Engage Cloud Configuration](/help/forms/assets/marketo-engage-cloud-configuration.png)

Now you can use the created cloud service configuration to connect the Marketo Engage data source to an Adaptive Form.

## Next step

You have created the cloud service configuration to integrate Adobe Marketo Engage with AEM Forms. Now, you can integrate:
* [New Adaptive Form with Marketo Engage](/help/forms/integrate-adaptive-form-with-marketo-engage.md)
* [Existing Adaptive Form with Marketo Engage](/help/forms/use-marketo-engage-data-source-in-form.md)

## Related articles

{{af-submit-action}}

## See also

{{marketo-engage-see-also}}
