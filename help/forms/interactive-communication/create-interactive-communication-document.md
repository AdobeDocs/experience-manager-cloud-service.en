---
title: Create an Interactive Communication
description: Create personalized, data-driven communications. Explore key features, onboarding steps, and real-world use cases with guides and tutorials.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Adaptive Forms, Interactive Communication
role: User, Developer, Author, Admin
---

# Create an Interactive Communication

Interactive communication enables you to create, manage, and deliver personalized and interactive communications, including customer service, billing, onboarding documents, offer letters, account updates, and more. It is designed to support any scenario where dynamic, user-specific content enhances the communication experience across industries.
Imagine you need to send a bank statement, insurance policy, or utility bill to thousands of customers. Each one has the same layout but personalized data. Interactive Communication (IC) makes that possible efficiently.

![Find IC Docu](/help/forms/interactive-communication/assets/Picture1.png)

Manually producing these documents can be time-consuming and often results in inconsistencies, especially when personalization and data integration are required. With the Interactive Communication Editor, users can streamline the process of creating Interactive communication. 

## Prerequisite

User must be part of forms-users group

## Create an Interactive Communication

Choose from different scenarios to create an Interactive Communication, based on the level of reuse and data integration required:

+++ Create a Blank Interactive Communication

Creating a blank interactive communication allows you to start from scratch, ideal when you want full control over layout, structure, and logic.
Steps to follow:

* Open your **Adobe Experience Manager (AEM) Forms as a Cloud Service instance**.
* Navigate to **Forms > Forms & Documents**.
* Click **Create > Interactive Communication**.


![Find IC Docu](/help/forms/interactive-communication/assets/comm.png)

* In the creation screen, leave the **Template** field blank.

![Find IC Docu](/help/forms/interactive-communication/assets/create-ic-document.png)

* Fill out other details like Title, Name, Author, etc.
* Click **Create** to enter the Interactive Communication Editor UI and begin designing.
* It opens the IC Editor, where you can begin designing your communication.
+++

+++ 1.2. Create a Template-based Interactive Communication

Using a template helps speed up design by reusing consistent layout elements such as headers, footers, logos, or standard formatting.
Templates ensure brand consistency and save time for commonly used communication types. Perform the below steps:

* Open AEM Forms as a Cloud Service instance.
* Go to **Forms > Forms & Documents**, click **Create > Interactive Communication**.
* In the creation form, select an enabled template from the dropdown.
* Fill out other details like Title, Name, Author, etc.
* Click **Create** to design your communication with the selected template structure.
* It opens the IC Editor, where you can begin designing your communication.
+++

+++ 1.3. Create a Data-Interacted Interactive Communication

Data-interacted communications automatically personalize content using backend data.
Ideal for statements, invoices, or notices where structure remains constant, but the data varies per recipient. Steps to follow:

* Open AEM Forms as a Cloud Service instance.
* Go to **Forms > Forms & Documents**, click **Create > Interactive Communication**.
* In the **Form Data Model** field, link your predefined **FDM (Form Data Model)**.
* Fill out other details like Title, Name, Author, etc.
* Use **Data Model** inside the editor to bind fields to dynamic data (e.g., customer name, balance, account number).
* Use **Content Areas, Subforms**, and **Fragments** to structure and repeat data where needed.
* Preview using **PDF Preview** and finalize the communication for delivery.
* It opens the IC Editor, where you can begin designing your communication.

![Find IC Docu](/help/forms/interactive-communication/assets/ic-ui.png)
+++

Start building Interactive Communications to streamline your workflows and deliver impactful, user-specific experiences.
