
# Interactive Communication Fragment

A Communication Fragment allows users to create reusable, modular content blocks such as headers, footers, or standard disclaimers that can be used across multiple communication documents. These fragments help maintain consistency, reduce repetitive work, and accelerate the design process when building personalized, data-driven communications.

When you launch the Interactive Communication Editor, you can choose to create communication fragments that integrate seamlessly into various templates and documents. Guided steps will help you define layout, reusable logic, and styling for fragment reuse.

---

## 1. Create a Communication Fragment

To create a communication fragment, perform the following steps:

1. Open your Adobe Experience Manager (AEM) environment.  
2. Navigate to `Forms > Forms & Documents`.  
3. Click the **Create** button and select **Interactive Communication Fragment**.

---

## 2. Define Communication Fragment Properties

When you click **Interactive Communication Fragment**, a configuration window appears where you can define the key details of your reusable content block. This includes the following sections:

- **Provide a Title** as the display name visible to users and authors.  
- **Assign a unique Name** for repository identification.  
- **Include a brief Description** to explain the purpose of the fragment.  
- **Link a Form Data Model** if the fragment needs to bind dynamic data.  
- **Add relevant Tags** for easier categorization and searchability.  
- **Mention the Author** responsible for creating the fragment.  
- **Set a Publish Date** to schedule when the fragment should go live.  
- **Specify an Unpublished Date** to define when the fragment should expire.  

Once these fields are completed, click the **Create** button to begin designing your reusable Communication Fragment.

---

## 3. Interactive Communication Fragment Editor UI

After clicking the **Create** button, a new window opens displaying the **Interactive Communication Fragment Editor UI**. This interface provides access to components and segments such as **Design View**, **PDF Preview**, **Object Library**, **Fragments**, and more enabling you to visually build, configure, and preview your reusable content blocks with support for dynamic data integration.

---

## 4. Components and Segments

These views help you visually design and structure your communication fragment with ease.

### 4.1 Design View

Use **Design View** to build the actual layout of your communication. Simply drag and drop components like text fields, images, and tables from the **Object Library** onto your document. You can adjust spacing, align components, and group related items to match your design. After building your layout in Design View, make sure to save your changes before using the PDF Previewer.

### 4.2 PDF Preview

The **PDF Preview** lets you instantly see how your communication will appear as a finalized PDF. It reflects all current data bindings and layout elements, helping you quickly identify and correct any formatting issues before publishing.

---

## 5. Core Interface Elements

These tools allow you to define structure, bind data, and manage component behavior in your communication fragment.

### 5.1 Component Hierarchy

This panel shows the tree structure of your document layout. You can manage the nesting of containers, forms, and elements, rename components, and rearrange them to maintain a logical flow.

### 5.2 Object Library

The **Object Library** provides a collection of reusable components such as text boxes, images, buttons, tables, checkboxes, and more. You can drag these objects into your Design View and configure their properties based on your communication needs.

### 5.3 Fragments

**Fragments** are reusable content blocks like disclaimers, legal notices, or layout components. You can import them into different communication documents to ensure consistency and reduce duplication of effort.

### 5.4 Data Model

The **Data Model** allows you to bind your communication fragment to XML or JSON data sources. This ensures that customer-specific data (like name, address, policy number) is dynamically inserted at runtime.

### 5.5 Data Binding

This section enables you to link form fields to backend data sources, ensuring that user information is pre-filled automatically from connected systems. It enhances accuracy and reduces manual input.

---

## 6. Conclusion

By using the provided views and interface elements, users can drag, drop, configure, and preview personalized communication fragments that meet customer needs. AEM's Interactive Communication Editor simplifies the design and delivery of consistent, dynamic, and automated experiences across platforms.
