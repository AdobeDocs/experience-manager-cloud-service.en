---
title: Best practices for working with components
seo-title: Best practices for working with components
description: Some best practices and key points to remember when working with Adaptive Form components
seo-description: Some best practices and key points to remember when working with Adaptive Form components

---

# Best practices for working with components{#best-practices-for-working-with-components}

Some best practices and key points to remember when working with Adaptive Form components are as follows:

* Each component has associated properties that control its appearance and functionality. To configure the properties of a component, tap the component and tap ![properties](assets/Smock_Wrench_18_N.svg) to open the component properties in the Properties browser.
* A component is identified with its element name. When you tap ![properties](assets/Smock_Wrench_18_N.svg), you can change the name of the component by changing the **[!UICONTROL Element Name]** field value in the properties browser. The Element Name field accepts letters, numbers, hyphens (-), and underscores (_) only. Other special characters are not allowed, and element name should begin with a letter.

* You can modify the Title property of an Adaptive Form component inline in the form editor without opening the Properties browser as long as the title is visible on the form. To do so:

    1. Tap to select a component that has a **[!UICONTROL Title]** property and whose **[!UICONTROL Hide title]** property is disabled.

    1. Tap ![Edit icon](assets/Smock_Edit_18_N.svg) to make the title editable.

    1. Modify the title and tap the Return key or tap anywhere outside the component to save the changes. Tap the Esc key to discard the changes.

* Some Adaptive Form components like Email and Telephone include out-of-the-box validation patterns. However, you can specify custom validation by updating the **[!UICONTROL Validation Pattern]** field under the Patterns accordion in the component properties. See component descriptions in the table above for more information about default validations.

* Adaptive Forms fields, such as Numeric Box and Email can be configured to include specialized HTML5 input types. When these fields are in focus on mobile devices and tablets, the keypad displays specific alphabet, numbers, and characters upfront that are commonly used to input information in the fields. It helps users enter information quickly without having to toggle between characters sets on the keypad. To allow specialized input for a component, enable the **[!UICONTROL Use HTML Type Number]** check box in its component properties.

* You can enable a Text Box component to accept Rich Text. To enable rich text for a text box, enable the **[!UICONTROL Allow Rich Text]** check box in the component properties.

* You can enable Text Box, Email, and Telephone components to autofill values for fields like name, address, credit card, telephone, and email from the information stored in browser's autofill settings. To enable this feature, select **[!UICONTROL Enable Autofill]** in the component properties and select an **[!UICONTROL Autofill Attribute]**. When a user fills an Adaptive Form, the values are suggested from the autofill profile in the browser or based on the values earlier filled by the user. Note that autofill works if autofill settings in user's browser are turned on.

* Specify values for Radio Button and Check Box items in `{value}={text}` format in component properties.
* The File attachment component, by default, allows a user to attach only one file. However, you can configure the component properties to support multiple attachments. In addition, if a user attaches multiple files with the same filename, the attachments can cause some issues. Therefore, it is recommended to associate a unique identifier for each submitted attachment at form submission. To do so:

    1. On your [!DNL AEM Forms] server, navigate to **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Tools]** &gt; **[!UICONTROL Operations]** &gt; **[!UICONTROL Web Console]**.
    1. Find and tap **[!UICONTROL Adaptive Forms Configuration Service]**.
    1. In the Adaptive Forms Configuration Service dialog, enable **[!UICONTROL Make File Names Unique]**. By default, it is disabled.

* To enable users to attach a PDF using Safari browser, ensure that **application/pdf** is added to the Supported File Types property of the File attachment component. Adaptive Forms created with previous [!DNL AEM Forms] version may contain **.pdf** instead of **application/pdf** in the Supported File Types property.

>[!NOTE]
>
>Adaptive Form components do not support right to left (RTL) languages. For example, Hebrew.