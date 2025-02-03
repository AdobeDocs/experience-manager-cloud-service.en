---
title: Publish AEM Forms for Edge Delivery Services.
description: Publish your Edge Delivery Services forms quickly and seamlessly. 
feature: Edge Delivery Services
role: Admin, Architect, Developer
---
# Publish your Adaptive Form to Edge Delivery Services

When your form is finalized and ready for use, you can publish it to make it accessible to your customers for data collection and submission. Publishing ensures that the form is available on Edge Delivery, enabling users to interact with it seamlessly. This process allows customers to fill out and submit the form in real time, ensuring efficient data capture and streamlined processing.

## Prerequisites

* Ensure that Edge Delivery is configured for your Form AEM.
* A form created using the **Edge Delivery Services (EDS) template**. [Learn more] about creating an EDS-based form.

## Publish Your Form

You can publish any **EDS-based Adaptive Form** to Edge Delivery by following these steps:

1. Select the **Adaptive Form** that you want to publish and click the **Edit** (![edit icon](/help/forms/assets/edit.svg)) icon.
   ![Select EDS-Based Form](/help/forms/assets/select-eds-based-form.png)

2. In the editor, select the **Adaptive Form Block** and click **Publish**.
   ![Click Publish](/help/forms/assets/click-publish.png)

3. On the **Publish** screen, you can see that your form is configured with the `edge-delivery-service-configuration` along with the selected template. In this example, a **Wknd_Form** template is used. Click **Publish**, and a confirmation pop-up appears indicating that your form is published.
   ![Publish Success](/help/forms/assets/publish-success.png)

4. To check the form’s publish status, click **Publish** again.
   ![Publish Status](/help/forms/assets/publish-status.png)

5. To **unpublish** a form, click the three-dot menu in the upper-right corner and select **Unpublish**.

## Enable Form Submission on Edge Delivery by Configuring a Referrer Filter for AEM Publisher

To ensure secure form submission, you need to configure a **Referrer Filter** in AEM Publisher. This filter ensures that only authorized requests from Edge Delivery can perform write operations (POST, PUT, DELETE, COPY, MOVE), preventing unauthorized modifications. Following are the steps given to configure a Referrer Filter for AEM Publisher:

### 1. Update the AEM Instance URL in Edge Delivery

Modify the `submitBaseUrl` in the **constant.js** file within the form block to specify the AEM instance URL:

- **For Cloud Setup:**
  ```js
  export const submitBaseUrl = 'https://publish-p120-e12.adobeaemcloud.com';
  ```
- **For Local Development:**
  ```js
  export const submitBaseUrl = 'http://localhost:4503';
  ```

### 2. Modify the CORS Configuration

Adjust the **CORS settings** to allow form submission requests from Edge Delivery domains. Refer to the [CORS Configuration Guide](https://experienceleague.adobe.com/en/docs/experience-manager-learn/getting-started-with-aem-headless/deployments/configurations/cors) for details.

**Sample CORS Configuration:**
```apache
# Developer Localhost
SetEnvIfExpr "env('CORSProcessing') == 'true' && req_novary('Origin') =~ m#(http://localhost(:\d+)?$)#" CORSTrusted=true

# Franklin Stage
SetEnvIfExpr "env('CORSProcessing') == 'true' && req_novary('Origin') =~ m#(https://.*\.hlx\.page$)#" CORSTrusted=true  

# Franklin Live
SetEnvIfExpr "env('CORSProcessing') == 'true' && req_novary('Origin') =~ m#(https://.*\.hlx\.live$)#" CORSTrusted=true
```
For local development, refer to the [documentation](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/deployment/referrer-filter) to enable CORS from your **development UI host URL**.

### 3. Configure the Referrer Filter

Set up the **Referrer Filter** in AEM Cloud Service via Cloud Manager. [Know more](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/security/understand-cross-origin-resource-sharing) about configuring the referrer filter on an AEM Cloud Service instance using a cloud manager.

**JSON Configuration for the Referrer Filter:**
```json
{
  "allow.empty": false,
  "allow.hosts": [],
  "allow.hosts.regexp": [
    "https://.*\\.hlx\\.page:443",
    "https://.*\\.hlx\\.live:443"
  ],
  "filter.methods": [
    "POST",
    "PUT",
    "DELETE",
    "COPY",
    "MOVE"
  ],
  "exclude.agents.regexp": [
    ""
  ]
}
```

This configuration specifies which HTTP methods are filtered, which referrers are allowed, and which user agents are excluded from the filter. By implementing these configurations, **form submissions via Edge Delivery** will be secured and restricted to authorized sources only.

### Access Your Published Adaptive Form

Your Adaptive Form is now accessible via **Edge Delivery** using the following URL format:

```
https://<branch>--<repo>--<owner>.aem.page/content/forms/af/<form_name>
```

For example, the URL for the **Wknd-Form** is:
```
https://main--universaleditor--wkndforms.aem.live/content/forms/af/wknd-form
```

---


















