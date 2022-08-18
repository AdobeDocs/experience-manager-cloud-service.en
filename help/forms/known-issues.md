---
title: Known issues and limitations
description: Known issues and limitations of  [!DNL AEM Forms] as a Cloud Service environment
contentOwner: khsingh
role: User, Developer
level: Intermediate
topic: Administration
exl-id: 871f294d-f251-4966-a021-39df65b613f0
---
# Known issues and limitations {#known-issues-and-limitations}

Before you begin using [!DNL AEM Forms] as a Cloud Service, review the following known issues and limitations:

## Known issues {#known-issues}

* Do not add and run a test that submits an Adaptive Form from a publish instance to an AEM Workflow running on an Author instance until further notice.

* When you import an Adaptive Form that uses a template containing the **[!UICONTROL Save]** button, the **[!UICONTROL Save]** button continues to appear in the Adaptive Form even after it is removed from corresponding template. Remove the **[!UICONTROL Save]** button from your Adaptive Forms before publishing it. Keep an eye on release notes for the availability of the Forms Portal and Save as a draft feature to restore and use the button.

* The **[!UICONTROL Set variable]** step of AEM Workflows does not support variables of type array list. You can use the process step to set variables of type array list. 

* When you submit an adaptive form containing a standard HTML upload field from an Apple iOS device the content of the file are not sent and a 0 byte file is received at the other end. The issue occurs intermittently and only on using synchronous submission. This is a [known issue](https://feedbackassistant.apple.com/feedback/9117687) in Apple iOS.

* When you submit a form containing a standard HTML upload field from an Apple iOS device, sometimes, the content of the file are not sent and a 0 byte file is received at the other end. This is a known issue in Apple iOS. [FB9117687](https://feedbackassistant.apple.com/feedback/9117687)


## Limitations {#limitations}

* Support for XFA-based Adaptive Forms is not available out of the box. If you intend to use XFA-based Adaptive Forms, contact Adobe Support with details of your use case and specific requirements.

