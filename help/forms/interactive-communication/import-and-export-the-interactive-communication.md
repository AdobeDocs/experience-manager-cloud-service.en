---
title: Import and Export Interactive Communication
description: Import and Export Interactive Communication enables users to seamlessly migrate, reuse, and manage communications across environments.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
exl-id: 7e328932-070d-4eb3-8176-500ef31581be
---
# Import and Export Interactive Communication

>[!NOTE]
>
> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

Import and export feature in Interactive Communication (IC) enables users to seamlessly migrate, reuse, and manage communications across environments. It allows you to export an Interactive Communication (IC) along with its associated fragments and data models from one environment and import it into another, ensuring consistency and reducing duplication of effort during deployment.

## Key Benefits

- Simplifies migration of ICs across environments.
- Preserves fragments, data models, and dependencies.
- Reduces effort in recreating ICs across projects.

## Import and Export Interactive Communication

Create an Interactive Communication (IC) in one environment and reuse it in another by exporting and importing it by following below steps:

+++1. How to Export Interactive Communication

1.1. Select a [created Interactive Communication](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/forms/interactive-communication/create-interactive-communication) (IC).
1.2. Click the **Download** option to export it as a ZIP file.
1.3. The downloaded ZIP file includes the IC along with its selected **template**, **fragments**, and **data model**.

![Find IC Docu](/help/forms/interactive-communication/assets/downloadic.png)
+++

+++2. How to Import Interactive Communication

2.1. Go to the target environment.
2.2. Navigate to **Forms > Forms and Documents > Create > File Upload**.
2.3. Upload the ZIP file to **import** the IC.

![Find IC Docu](/help/forms/interactive-communication/assets/uploadfile.png)

2.4. After uploading, the IC appears along with its associated fragments and data model.

![Find IC Docu](/help/forms/interactive-communication/assets/importfragment.png)
+++

+++3. Import and Export Fragment

3.1. To export, select the required fragment from **Forms > Forms and Documents**, then click **Download** to export it as a ZIP file.

3.2. To import, go to the target environment, navigate to Forms > Forms and Documents > Create > **File Upload**, and upload the exported ZIP file.

This allows easy reuse of fragments across different environments, ensuring design consistency and reducing duplication of effort.
+++
