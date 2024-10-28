---
Title: How to Integrate an Adaptive Form with Marketo Engage?
Description: Learn how to integrate your Adaptive Form with a Marketo Engage instance.
Keywords: How to connect a Marketo instance with an Adaptive Form? , Connect a form to Marketo, Integrate a form with Marketo Engage, Integrate an Adaptive Form with a Marketo instance, Submit data from form to Marketo. 
Feature: Adaptive Forms, Core Components
Role: User, Developer
---

# Connect an Adaptive Form to Marketo Engage

You can configure an Adaptive Form to submit data to [Adobe Marketo Engage](https://experienceleague.adobe.com/en/docs/marketo/using/home) on submission. The configured Adaptive Form sends captured data to Marketo Engage for processing. It helps you build custom data capture experience while harnessing the power of Adobe Marketo Engage to build business logics around captured data and automate workflows.

Adaptive Forms editor provides the **Submit to Marketo Engage** submit action to send Adaptive Forms data to Adobe Marketo Engage. 

AEM as a Cloud Service offers various out of the box submit actions for handling form submissions. You can learn more about these options in the [Adaptive Form Submit Action](/help/forms/configure-submit-actions-core-components.md) article.

## Advantages to connect forms with Marketo Engage

Below are the few advantages to connect an Adaptive Form with Adobe Marketo Engage:

* **Automated data capture**: It helps in automatically capture form submissions and store them in Marketo, eliminating manual data entry and reducing errors.

* **Lead management**: It streamlines lead management processes by integrating form submissions directly into your marketing database, enabling better tracking and nurturing of leads.

* **Improved campaign performance**: It uses form data to analyze and optimize marketing campaigns, enhancing overall performance and return on investment (ROI).

* **Analytics and reporting**: It helps in gaining access to robust analytics and reporting tools, such as Munchkin, within Marketo to measure the effectiveness of forms and campaigns.

* **Follow-up automation**: It helps in automating follow-up emails and workflows triggered by form submissions, ensuring timely communication with leads.

## Why choose AEM Forms over Marketo Forms?

The table below outlines the reasons to choose AEM Forms over Marketo Forms:

| **Feature** | **AEM Forms**| **Marketo Engage Forms** |
|-------------------------------------|----------------------------------------------------------------------|-----------------------------------------------------------|
| **Customizations** | Allows to add specific custom functions, adjust form actions, and modify field behaviors to enhance form interactions, complex workflows | No customization support |
| **Rule Editor**| Supports a built-in Rule Editor for adding logic and conditions.      | No Rule Editor support|
| **Layout Options** | Supports multiple layout options| Limited layout options |
| **Prefill Service** | Offers a Prefill service to auto-populate form data. | No Prefill service available|
| **Embedding in Sites** | Can be embedded in Sites using iFrame| Cannot be embedded in Sites using iFrame|
| **Ease of Integration with Sites**  | No additional learning required; AEM Forms use the same skills as Sites | Additional learning may be required|
| **Data Submission**| Can submit data to various platforms and offers multiple connectors, such as Connect to SharePoint, Connect to OneDrive, Connect to Salesforce, and more.| Can submit data to limited connectors, for example to Salesforce |

## Pre-requisites to integrate Adaptive Forms with Marketo Engage

The following are required to integrate an Adaptive Form with Marketo Engage:

* A valid Adobe Marketo Engage license
* A working instance of Marketo Engage to [retrieve the Client ID and Client Secret](https://experienceleague.adobe.com/en/docs/marketo/using/product-docs/administration/additional-integrations/create-a-custom-service-for-use-with-rest-api).

## Considerations while integrating Adaptive Forms with Marketo Engage

Some considerations for integrating an Adaptive Form with Marketo Engage are:

* AEM only supports the People(Leads) database among the various Marketo databases.
* Marketo allows the [creation of 10 custom objects](https://experienceleague.adobe.com/en/docs/marketo/using/product-docs/administration/marketo-custom-objects/add-marketo-custom-object-fields) as user-defined objects to store specialized data beyond the standard fields in Leads, supporting unique business needs.
* AEM can access custom objects only if they are associated with the Lead database.
* It is not possible to connect Edge Delivery Services Forms with Marketo Engage.

## How to connect forms with Marketo Engage?

To connect the Adaptive Form with Adobe Marketo Engage:
1. [Create a Marketo Engage configuration](#1-create-a-marketo-engage-configuration) 
1. [Configure Submit action of an Adaptive Form](#2-configure-submit-action-of-an-adaptive-form)


### 1. Create a Marketo Engage configuration

**Steps will be added**

### 2. Configure Submit action of an Adaptive Form

**Steps will be added**

## FAQs

**Q: Can you change the submit action for forms configured to connect with the Marketo Engage schema?**
    **A:** By default, the **Submit to Marketo** action is selected when a form is configured to connect with the Marketo Engage schema. However, you can change the submit action for the forms if needed.

**Q: What happens when you change the connector of the form?**  
    **A:** If you change the connector of the form, the existing bindings become invalid.

**Q: What are the three operations available in the Invoke Service of the Rule Editor for forms integrated with Marketo Engage?**  
    **A:** The three available out of the box operations available in the **Invoke Service** for forms integrated with Marketo Engage are:
* Sync Lead
* Get Lead by ID
* Get Lead by Filter Type

## Next Step

You can also connect an AEM Form with the [Munchkin library](https://experienceleague.adobe.com/en/docs/marketo/using/product-docs/administration/setup/munchkin) to track the number of visits, clicks, and form submissions.

## Related Articles

{{af-submit-action}}

## See Also

{{see-also}}





