---
title: How to create a Forms Portal on an Experience Manager Sites page?
description: Learn how to create a Forms Portal and use out-of-the-box core components on an AEM Sites page.
feature: Adaptive Forms, Core Components
exl-id: 13cfe3ba-2e85-46bf-a029-2673de69c626
role: User, Developer
---

# Introduction to Forms Portal component

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/publish-process-aem-forms/introduction-publishing-forms.html)                  |
| AEM as a Cloud Service (Core Components)     | This article         |

The Forms portal components in Adobe Experience Manager (AEM) provides a streamlined and efficient way to manage and display Adaptive Forms on your Sites page. This component integrates forms management directly into your web application, offering significant advantages over traditional methods where forms and web applications are developed and managed separately.

Forms Portal enhances the accessibility and management of your Adaptive Forms on a Sites page. It not only simplifies the organization of your forms but also provides options for presenting them to a broader audience, including anonymous or non-logged-in users.

The Form Portal components allow you to add the following functionality:

* List forms in customized layouts. Out of the box, List view and Card view layouts are provided. You can create your own custom layouts.
* Enables you to display custom metadata and custom actions while listing them.
* List forms published by AEM Forms UI on the publish instance where Forms Portal components are being used.
* Allow end users to render forms in HTML and PDF format.
* Enable searching of forms based on title and description.
* Use custom CSS to customize the look and feel of the portal.
* Create links to forms.
* Lists drafts and submissions related to Adaptive Forms created by the user.

## Components of a Forms Portal 

AEM Forms provide the following portal components out of the box:

* **Search & Lister**: It lets you list forms on your portal page and provides configuration options to list forms based on specified criteria. 
* **Drafts & Submissions**:It displays forms which are made public by Forms author, the Drafts & Submissions component displays forms that are saved as draft for completing later and submitted forms. This component provides personalized experience to any logged in user.
* **Link**: It lets you create a link to a form anywhere on the page.

Consider a scenario where an organization needs to manage and display multiple Adaptive Forms on AEM Sites page. The developer creates and organizes these forms—such as applications, surveys, and feedback forms—in the AEM Forms repository. To manage these forms, the developer uses the Forms Portal component, which dynamically lists all forms on the Sites page. The **Search & Lister** component allows users to search and filter the forms. Anonymous or non-logged-in users can view and browse the list of available forms, but to access draft versions or submit completed forms, they must log in. The **Drafts & Submissions** component allows users to edit drafts or submit forms by the authenticated users. The Forms portal components provides accessibility with security and improves the overall user experience by integrating form management directly into the AEM Sites page. On an AEM Sites page, you can also use the **Link** component to place a reference to a form at any location on the page.

## Next Steps

In the next article, let us learn how to list Adaptive Forms on a AEM Sites page using the **Search & Lister** Forms portal component.

## See Also {#see-also}

{{see-also}}