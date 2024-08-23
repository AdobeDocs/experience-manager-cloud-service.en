---
title: How to create a Forms Portal on an Experience Manager Sites page?
description: Learn how to create a Forms Portal and use out-of-the-box Core components on an AEM Sites page.
feature: Adaptive Forms, Core Components
exl-id: 13cfe3ba-2e85-46bf-a029-2673de69c626
role: User, Developer
---

# Introduction to Forms Portal component

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/publish-process-aem-forms/introduction-publishing-forms.html)                  |
| AEM as a Cloud Service (Core Components)     | This article         |

The Forms Portal components in Adobe Experience Manager (AEM) provide a streamlined and efficient way to manage and display Adaptive Forms on your Sites page. This component integrates forms management directly into your web application, offering significant advantages over traditional methods where forms and web applications are developed and managed separately.

Forms Portal enhances the accessibility and management of your Adaptive Forms on the Sites page. It not only simplifies the organization of your forms but also offers options for presenting them to a broader audience, including anonymous or non-logged-in users.

The Form Portal components allow you to add the following functionality:

* List forms in customized layouts. Out of the box, List view and Card view layouts are provided. You can create your own custom layouts.
* Enables you to display custom metadata and custom actions while listing them.
* List forms published by AEM Forms UI on the publish instance where Forms Portal components are used.
* Allow end users to render forms in HTML and PDF format.
* Enable searching of forms based on title and description.
* Use custom CSS to customize the look and feel of the portal.
* Create links to forms.
* Lists drafts and submissions related to Adaptive Forms created by the user.

## Components of a Forms Portal 

![Components of Forms Portal](/help/forms/assets/forms-portal.png)

AEM Forms provide the following portal components out of the box:

* **Search & Lister**: It lists forms on the Sites page and offers configuration options to filter forms based on specified criteria.
* **Drafts & Submissions**: It displays forms that are saved as draft for completing later and submitted forms. It shows both forms saved as drafts for later completion and forms that have been submitted. It provides a personalized experience for any logged-in user. 
The **Drafts & Submissions** component needs a storage setup for saving drafts. The Unified Storage Connector offers a framework to link the AEM instance with external storage.
* **Link**: It creates a link to a form anywhere on the page.

Consider a scenario where a bank needs to manage and display various forms on its website. The developer creates and organizes these forms such as loan applications, account opening forms, and feedback surveys on the website. To manage and display these forms, the developer uses the Forms Portal component, which dynamically lists all forms on the website. The Forms Portal components enhance accessibility and security while integrating form management seamlessly into the bank’s website.

The **Search & Lister** component enables users to search and filter through the forms. Non-logged-in users can view and browse the list of available forms, but to access draft versions or submit completed forms, they need to be logged in. The **Drafts & Submissions** component allows authenticated users to save draft versions of forms and manage their submissions. Additionally, the **Link** component is used to reference specific forms from any location on the page, providing convenient access to users. Form references are controlled based on user permissions. For instance, non-logged-in users can view the Contact Us or Account Opening forms, while only logged-in users can access the Loan Application or Investment forms.  

## Next Steps

In the next article, let us learn [how to list forms on the Sites page using the Search & Lister Forms Portal component](/help/forms/list-forms-on-sites-page.md).

## Related articles

{{forms-portal-see-also}}

## See Also {#see-also}

{{see-also}}