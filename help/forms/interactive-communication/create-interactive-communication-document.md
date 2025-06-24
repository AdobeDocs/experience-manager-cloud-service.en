
# Create Communication Document

A Communication Document allows users to create personalized, data-driven communications, such as insurance summaries, policy updates, or customer notices, and distribute them across channels including email, print, or web. It's ideal for delivering dynamic, multi-platform customer communication.

When you launch the Interactive Communication Editor, you can create a new document, use an existing template, or reuse sample fragments—guided steps will help you define the layout, structure, and data integration for your first communication.

## 1. Create a Communication Document

To create a communication document, perform the following steps:
1. Open your Adobe Experience Manager (AEM) environment.
2. Navigate to **Forms > Forms & Documents**.
3. Click the **Create** button and select **Interactive Communication**.

![Find IC Docu](/help/)

## 2. Define Communication Document Properties

When you click Interactive Communication, a configuration window appears where you can define key details of your communication document. This includes the following sections:

1. Provide a **Title** as the display name visible to users and authors.
2. Assign a unique **Name** for repository identification.
3. Include a brief **Description** of the communication.
4. Link a **Form Data Model** to populate the document dynamically.
5. Add relevant **Tags** for easier categorization and searchability.
6. Mention the **Author** responsible for creating the content.
7. Set a **Publish Date** to schedule when the document should go live.
8. Specify an **Unpublished Date** to define when the document should expire.

Once these fields are completed, click the **Create** button to start building your first Interactive Communication Document.

## 3. Interactive Communication Editor UI

After clicking the Create button, a new window opens displaying the Interactive Communication Editor UI. This interface presents components and segments such as Design View, Master Pages, PDF Preview, Object Library, Fragments, and more, allowing you to visually build, customize, and preview your communication document with real-time data integration.

## 4. Components and Segments

These views help you visually design and structure your communication document with ease.

### 4.1 Master Pages
In Master Pages, you can define layout elements like headers, footers, watermarks, and logos that appear on every page of the communication. This ensures brand consistency and saves time by reusing common design components.

### 4.2 Design View
Use Design View to build the actual layout of your communication. Simply drag and drop components like text fields, images, and tables from the Object Library onto your document. You can adjust spacing, align components, and group related items to match your communication design. After building your layout in Design View, make sure to save your changes before using the PDF previewer.

### 4.3 PDF Preview
The PDF Preview lets you instantly see how your communication will appear as a finalized PDF. It reflects all current data bindings and layout elements, helping you quickly identify and correct any formatting issues before publishing.

## 5. Core Interface Elements

These tools allow you to define structure, bind data, and manage component behavior in your communication document.

### 5.1 Component Hierarchy
This panel shows the tree structure of your document layout. You can manage the nesting of containers, forms, and elements, rename components, and rearrange them to maintain a logical flow.

### 5.2 Object Library
The Object Library provides a collection of reusable components such as text boxes, images, buttons, tables, checkboxes, and more. You can drag these objects into your Design View and configure their properties as per your communication needs.

### 5.3 Fragments
Fragments are reusable content blocks like disclaimers, legal notices, or reusable layouts. You can import them into different communication documents, ensuring consistency and reducing duplication of effort.

### 5.4 Data Model
The Data Model allows you to bind your communication document to XML or JSON data sources. This ensures that customer-specific data (like name, address, policy number) is dynamically inserted into the document at runtime.

### 5.5 Add Pages
If your communication spans multiple sections, use this option to add one or more pages. This is useful when working with long statements or multi-part documents.

### 5.6 Content Areas
Content Areas are zones where data-driven or personalized content will be displayed. You can assign data-bound components here that change based on the user or data context.

### 5.7 Subforms
Subforms are used to group related fields—like a list of transactions or dependent names—that may repeat dynamically depending on the input data. You can define if they repeat horizontally or vertically.

### 5.8 Object
Use this panel to configure individual component properties like visibility, size, layout alignment, conditional behavior, and interactivity. This helps you tailor the experience based on user data or actions.

### 5.9 Data Binding
This is where you link form fields to backend data, ensuring that user information is pre-filled automatically from connected systems. It ensures accuracy and eliminates manual input.

## 6. Conclusion

By using views and interface elements, users can drag, drop, configure, and preview personalized communications that meet customer needs. AEM's Interactive Communication Editor simplifies the design and delivery of consistent, dynamic, and automated experiences across platforms.
