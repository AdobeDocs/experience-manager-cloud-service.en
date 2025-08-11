
# Create an Interactive Communication

Interactive communication enables you to create, manage, and deliver personalized and interactive communications, including customer service, billing, onboarding documents, offer letters, account updates, and more. It is designed to support any scenario where dynamic, user-specific content enhances the communication experience across industries.

Imagine you need to send a bank statement, insurance policy, or utility bill to thousands of customers. Each one has the same layout but personalized data. Interactive Communication (IC) makes that possible efficiently.

![Find IC Docu](/help/forms/interactive-communication/assets/Picture1.png)

Manually producing these documents can be time-consuming and often results in inconsistencies, especially when personalization and data integration are required. With the Interactive Communication Editor, users can streamline the process of creating Interactive communication. 

In this article, we'll explore how to create your first Interactive Communication. 

## 1. Create an Communication Communication

Below are three ways to start an Interactive Communication, depending on the level of reuse and data integration you need.

### 1.1. Create a Blank Interactive Communication

Creating a blank interactive communication allows you to start from scratch, ideal when you want full control over layout, structure, and logic.
Steps to follow:

* Open your **Adobe Experience Manager (AEM) Forms as a Cloud Service instance**.
* Navigate to **Forms > Forms & Documents**.
* Click **Create > Interactive Communication**.


![Find IC Docu](/help/forms/interactive-communication/assets/find-ic-documnet.png)

* In the creation screen, leave the **Template** field blank.

![Find IC Docu](/help/forms/interactive-communication/assets/create-ic-document.png)

* Fill out other details like Title, Name, Author, etc.
* Click **Create** to enter the Interactive Communication Editor UI and begin designing.

### 1.2. Create a Template-based Interactive Communication

Using a template helps speed up design by reusing consistent layout elements such as headers, footers, logos, or standard formatting.
Templates ensure brand consistency and save time for commonly used communication types. Perform the below steps:

* Open AEM Forms as a Cloud Service instance.
* Go to **Forms > Forms & Documents**, click **Create > Interactive Communication**.
* In the creation form, select an enabled template from the dropdown.
* Fill out other details like Title, Name, Author, etc.
* Click **Create** to design your communication with the selected template structure.

### 1.3. Create a Data-Interacted Interactive Communication
Data-interacted communications automatically personalize content using backend data.
Ideal for statements, invoices, or notices where structure remains constant, but the data varies per recipient. Steps to follow:
*    Open AEM Forms as a Cloud Service instance.
*    Go to **Forms > Forms & Documents**, click **Create > Interactive Communication**.
*    In the **Form Data Model** field, link your predefined **FDM (Form Data Model)**.
*    Fill out other details like Title, Name, Author, etc.
*    Use **Data Model** inside the editor to bind fields to dynamic data (e.g., customer name, balance, account number).
*    Use **Content Areas, Subforms**, and **Fragments** to structure and repeat data where needed.
*    Preview using **PDF Preview** and finalize the communication for delivery.

## 2. Interactive Communication Editor UI

A new window opens displaying the **Interactive Communication Editor UI**. 

![Find IC Docu](/help/forms/interactive-communication/assets/ic-ui.png)

## 3. Interactive Communication Views

These views help you visually design and structure your communication document with ease.

![Find IC Docu](/help/forms/interactive-communication/assets/ic-component-and-segment.png)

**Master Pages:** Define reusable elements like headers, footers, and logos for consistent layout across all pages.
**Design View:** Build your layout using drag-and-drop components from the Object Library.
**PDF Preview:** Instantly preview the final PDF with applied layout and data bindings.

**[Note: See article Components and Segments for more information]**

## 4. Interface Elements

Core interface elements allow you to define structure, bind data, and manage component behavior in your communication document.

![Find IC Docu](/help/forms/interactive-communication/assets/ic-core-interface-element.png)

**Component Hierarchy:** Displays the layout's hierarchical structure to manage nesting, rename, or reorder elements.

**Object Library:** Provides reusable drag-and-drop components like text boxes, buttons, and tables.

**Fragments:** Lets you insert prebuilt, reusable content blocks for consistency and efficiency.

**Data Model:** Connects your document to FDM for real-time dynamic personalization.

**Add Pages:** Allows insertion of additional pages to support long or sectioned documents.

**Properties Panel (Right side of UI showing selected element properties):** Displays editable properties of the selected object, allowing you to customize behavior, appearance, and data bindings.

**[Note: See article Interface Elements for more information]**

These interface elements help achieve visually structured, data-integrated documents tailored to each recipient. They streamline design while enabling consistent, automated communication experiences.
