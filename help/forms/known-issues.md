---
title: What are the known issues and limitations of AEM Forms as a Cloud Service environment?
description: Known issues and limitations of  [!DNL AEM Forms] as a Cloud Service environment.
contentOwner: khsingh
role: Admin, Developer, User
feature: Adaptive Forms
topic: Administration
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: 871f294d-f251-4966-a021-39df65b613f0
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
---
# Known issues and limitations {#known-issues-and-limitations}

Before you begin using [!DNL AEM Forms] as a Cloud Service, review the following known issues and limitations:

## Known issues {#known-issues}

* Do not add and run a test that submits an Adaptive Form from a publish instance to an AEM Workflow running on an Author instance until further notice.

* When you import an Adaptive Form that uses a template containing the **[!UICONTROL Save]** button, the **[!UICONTROL Save]** button continues to appear in the Adaptive Form even after it is removed from corresponding template. Remove the **[!UICONTROL Save]** button from your Adaptive Forms before publishing it. Keep an eye on release notes for the availability of the Forms Portal and Save as a draft feature to restore and use the button.

* The **[!UICONTROL Set variable]** step of AEM Workflows does not support variables of type array list. You can use the process step to set variables of type array list. 

* When you submit an adaptive form containing a standard HTML upload field from an Apple iOS device the content of the file are not sent and a 0 byte file is received at the other end. The issue occurs intermittently and only on using synchronous submission. This is a [known issue](https://feedbackassistant.apple.com/feedback/9117687) in Apple iOS.

* When you submit a form containing a standard HTML upload field from an Apple iOS device, sometimes, the content of the file are not sent and a 0 byte file is received at the other end. This is a known issue in Apple iOS. [FB9117687](https://feedbackassistant.apple.com/feedback/9117687)

* AEM Forms as a Cloud Service does not generate thumbnails for XDP and JSON schema files. The service displays default icons in place of thumbnails.

    ![Forms Thumbnail known issue](/help/forms/assets/forms-tumbnail-known-issue.png)

* When you use a schema with repeatable elements to create a Core Components based Adaptive Form, the option to drag-and-drop repeatable elements from data model tree in the Adaptive Forms Editor does not work.

## Limitations {#limitations}

* Support for XFA-based Adaptive Forms is not available out of the box. If you intend to use XFA-based Adaptive Forms, contact Adobe Support with details of your use case and specific requirements.

