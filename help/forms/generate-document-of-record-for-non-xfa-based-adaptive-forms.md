---
title: Generate Document of Record for Adaptive Forms
description: Explains how you can generate a template for a Document of Record (DoR) for Adaptive Forms.
exl-id: 15540644-c0c3-45ce-97d3-3bdaa16fb4b6
---
# Generate Document of Record for Adaptive Forms

## Overview {#overview}

When a form is filled or submitted, you can keep a record of the form, in print or in document format. This record is referred as a Document of Record (DoR). It is a print-friendly copy of the submitted form. You can also refer the document of record for the information customers have filled at a later date or use the Document of Record to archive forms and content together in PDF Format.  

![Document of Record](assets/document-of-record.png)

To create a Document of Record, an XFA or Acroform based template is merged with data collected via an adaptive form. You can generate a Document of Record automatically or on-demand. 
The on-demand option allows you to specify a custom XFA or Acroform based template to provide a custom appearance to your Document of Record.

You can:

* [Generate an XFA-based Document of Record](#generate-an-XFA-based-document-of-record)
* [Generate an Acroform-based (Acrobat Form PDF) Document of Record](#generate-an-Acroform-based-document-of-record)
* [Auto generate a Document of Record](#auto-generate-a-document-of-record) 

## Before you start {#components-to-automatically-generate-a-document-of-record}

Before you start learn and ready the assets required for a Document of Record:

**Base template:** An XFA template (XDP file) created in AEM Designer or an Acrobat Form (AcroForm). [Base template](#base-template-of-a-document-of-record) is used to specify styling and branding information for a Document of Record. Upload your XFA template (XDP file) to your AEM Forms instance before 

**Adaptive Form:** An Adaptive Form for which the Document of Record is to be generated.

## Generate an XFA-based Document of Record {#generate-an-XFA-based-document-of-record}

Upload your XFA template (XDP file) to your AEM Forms instance. Perform the following steps to configure an Adaptive Form to use XFA template (XDP file) as template for Document of Record:

1. In AEM author instance, click **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms and Documents].**
1. Select a form, and click **[!UICONTROL Properties]**.
1. In the Properties window, tap **[!UICONTROL Form Model]**.
1. On the  **[!UICONTROL Form Model]** tab, in the **[!UICONTROL Select From]** drop-down, select **[!UICONTROL Schema]** or **[!UICONTROL None]**. You can also select a form model when you create a form.
1. In the Document of Record Template Configuration section of the Form Model tab, select **Associate Form Template as Document of Record Template**. On selecting this option, all XFA template (XDP files) available on your machine are displayed. Select the appropriate file. Also, ensure same schema (data schema) is used for Adaptive Form and selected XFA template (XDP file).  
1. Click **[!UICONTROL Done.]**

Your Adaptive Form is now configured to use an XDP file as template for Document of Record. The next steps is to [bind Adaptive Form components with corresponding template fields](#bind-adaptive-form-components-with-template-fields).

## Generate an Acroform-based Document of Record {#generate-an-Acroform-based-document-of-record}

Upload your Adobe Acrobat PDF (Acroform) to your AEM Forms instance. Perform the following steps to configure an Adaptive Form to use Adobe Acrobat PDF (Acroform) as template for Document of Record:

1. In AEM author instance, click **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms and Documents].**
1. Select a form, and click **[!UICONTROL Properties]**.
1. In the Properties window, tap **[!UICONTROL Form Model]**.
1. On the  **[!UICONTROL Form Model]** tab, in the **[!UICONTROL Select From]** drop-down, select **[!UICONTROL Schema]** or **[!UICONTROL None]**. You can also select a form model when you create a form.
1. In the Document of Record Template Configuration section of the Form Model tab, select **Associate Form Template as Document of Record Template**. On selecting this option, all Acrobat PDF (Acroform) available on your machine are displayed. Select the appropriate file.
1. Click **[!UICONTROL Done.]**

Your Adaptive Form is now configured to use an Acroform as template for Document of Record. The next steps is to [bind Adaptive Form components with corresponding template fields](#bind-adaptive-form-components-with-template-fields).

## Automatically generate a Document of Record {#auto-generate-a-document-of-record}

When an Adaptive Form is configured to automatically generate a Document of Record, every time a form is changed, its Document of Record is updated immediately. For example, if a field is removed from an existing adaptive form, the corresponding field is also removed and is not visible in the Document of Record. There are many other advantages of automatically generating Document of Record. :

* Form developers do not have to maintain data bindings manually. Auto-generated Document of Record takes care of data binding related updates.
* Form developers do not have to manually hide fields which are marked exclude from Document of Record. Auto-generated Document of Records are pre-configured to exclude such fields.
* Auto-generated Document of Record option saves time required to create a Form template for Document of Record.
* Auto-generated Document of Record option allows you to use different styling and appearances using different base templates. It helps select best style and appearance for Document of Record for your organization. If you do not specify styling, system styles are set as default.
* Auto-generated Document of Records ensure any change in form is immediately reflected in Document of Record.

Perform the following steps to configure an Adaptive Form to automatically generate a Document of Record:

1. In AEM author instance, click **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms and Documents].**
1. Select a form, and click **[!UICONTROL Properties]**.
1. In the Properties window, tap **[!UICONTROL Form Model]**.
1. On the  **[!UICONTROL Form Model]** tab, in the **[!UICONTROL Select From]** drop-down, select **[!UICONTROL Schema]** or **[!UICONTROL None]**. You can also select a form model when you create a form.
1. In the Document of Record Template Configuration section of the Form Model tab, select **Generate Document of Record**.
1. Click **[!UICONTROL Done.]**

## Bind Adaptive Form components with template fields {#bind-adaptive-form-components-with-template-fields}

 Bind Adaptive Form fields with template fields to display captured form data in corresponding Document of Record Field. To bind Adaptive Form components with corresponding document of record template fields:

1. Open the Adaptive Form, configured to use a custom form template for editing.

1. Select an Adaptive Form component and click open Configure ![Configure](assets/Smock_Wrench_18_N.svg) icon. It opens properties browser. 

1. In the properties browser, browse and select a field.

   * (For AcroForm template) the **[!UICONTROL Document of Record Bind Reference field]** property.
   * (For XFA template) the **[!UICONTROL Data Model Bind Reference]** property.

1. Click **[!UICONTROL Save]**.

<!-- 
In the following video Adaptive Form components are binded with corresponding Acroform template fields and the Document of Record is sent as an email attachment.
-->

You can use Send Email, AEM Workflow submit action in conjunction with [Document of Record step, and other submit actions](configuring-submit-actions.md) to receive a Document of Record.  

## Incremental updates to Document of Record template {#document-of-record-template-incremental-updates}

Adaptive forms and corresponding document of record templates can evolve over the period of time. You can choose to add, remove, or modify fields to an Adaptive Form or a Document of Record template.

When you make changes to a Document of Record template and upload the changed Document of Record template to AEM Forms, the Adaptive Forms editor automatically detects the changed bindings and informs you about the adaptive form components that require new bindings. It allows you to make incremental updates to a Document of Record template. 

For example, an Organization, *We.Retail*, has an AcroForm-based Document of Record template, *we-retail-invoice.pdf*. The template looks like the following: 

![Original Template](assets/we-retail-invoice.png)

After using the template for some time, organization decides to rename `invoice-number` field to `bill-number` field and capture email address of buyers. A developer updates name of the `invoice-number` field and adds an email field to the template. He also creates a new version of template called  *we-retail-invoice-v2.pdf*.

![Updated Template](assets/we-retail-new-invoice.png)

The developer uploads and applies to the updated template to the adaptive form. The adaptive form automatically detects and displays list of fields where binding has changed.

![Binding Error](assets/we-retail-binding-error.png)

The form developer binds Adaptive Forms fields with corresponding Document of Record template. 
>[!VIDEO](assets/we-retail-binding.mp4)

Now, when the Adaptive Form is submitted an updated  Document of Record of record is created.

![Updated-](assets/we-retail-new-invoice-sent-to-customer.png)

## Key considerations when working with Document of Record {#key-considerations-when-working-with-document-of-record}

Keep in mind the following considerations and limitations when working on Document of Record for Adaptive Forms.

* Document of Record templates do not support rich text. Therefore, any rich text in the static Adaptive Form or in the information filled in by the end user appears as plain text in the Document of Record.
* Document fragments in an Adaptive Form do not appear in the Document of Record. However, Adaptive Form Fragments are supported.
* Content binding in Document of Record generated for XML Schema based Adaptive Form is not supported.
* Localized version of Document of Record is created on demand for a locale when the user requests the rendering of the Document of Record. Localization of Document of Record occurs along with localization of Adaptive Form. <!-- For more information on localization of Document of Record and Adaptive Forms see Using AEM translation workflow to localize Adaptive Forms and Document of Record.-->

<!-- ## Configure an adaptive form to generate  Document of Record {#adaptive-form-types-and-their-documents-of-record}

While creating an adaptive form, in the Form Model tab of Adaptive Form properties, select one the following option: 

* **None**
  Select the option to create an Adaptive Form without a form model. When the option is selected, the Document of Record is automatically generated for your Adaptive Form.

* **[Associate form template as a Document of Record template](creating-adaptive-form.md#create-an-adaptive-form-based-on-an-xfa-form-template)**
  
  Select the option to use an XFA Form as a template for Document of Record. 

* **[Generate Document of Record](creating-adaptive-form.md#create-an-adaptive-form-based-on-xml-or-json-schema)**
  Select the option to use an XFA Form as a template. When the option is selected, the Document of Record is automatically generated for your Adaptive Form. When you use an XML schema as a template for an Adaptive Form, ensure that the adaptive form and associated XFA Form use the same XML schema as your Adaptive Form
  


When you select a form model, configure Document of Record using options available under Document of Record Template Configuration. See [Document of Record Template Configuration](#document-of-record-template-configuration). -->

## Mapping of Adaptive Form elements {#mapping-of-adaptive-form-elements}

The following table describes Adaptive Form components and corresponding XFA components and if those appear in a Document of Record.

### Fields {#fields}

<table>
 <tbody>
  <tr>
   <th>Adaptive Form component</th>
   <th>Corresponding XFA component</th>
   <th>Included by default in Document of Record Template?</th>
   <th>Notes</th>
  </tr>
  <tr>
   <td>Button</td>
   <td>Button</td>
   <td>false</td>
   <td> </td>
  </tr>
  <tr>
   <td>Check box</td>
   <td>Check Box</td>
   <td>true</td>
   <td> </td>
  </tr>
  <tr>
   <td>Date picker</td>
   <td>Date/Time Field</td>
   <td>true</td>
   <td> </td>
  </tr>
  <tr>
   <td>Drop-down list</td>
   <td>Drop-down List</td>
   <td>true</td>
   <td> </td>
  </tr>
  <tr>
   <td>Scribble Signature</td>
   <td>Signature Scribble</td>
   <td>true</td>
   <td> </td>
  </tr>
  <tr>
   <td>Numeric box</td>
   <td>Numeric Field</td>
   <td>true</td>
   <td> </td>
  </tr>
  <tr>
   <td>Password box</td>
   <td>Password Field</td>
   <td>false</td>
   <td> </td>
  </tr>
  <tr>
   <td>Radio Button</td>
   <td>Radio Button</td>
   <td>true</td>
   <td> </td>
  </tr>
  <tr>
   <td>Text box</td>
   <td>Text Field</td>
   <td>true</td>
   <td> </td>
  </tr>
  <tr>
   <td>Reset button</td>
   <td>Reset Button</td>
   <td>false</td>
   <td> </td>
  </tr>
  <tr>
   <td>Submit button</td>
   <td><p>Email Submit Button</p> <p>HTTP Submit Button</p> </td>
   <td>false</td>
   <td> </td>
  </tr>
  <tr>
   <td>Terms and conditions</td>
   <td> </td>
   <td>true</td>
   <td> </td>
  </tr>
  <tr>
   <td>File Attachment</td>
   <td> </td>
   <td>false</td>
   <td>Not available in Document of Record template. Only Available in Document of Record through attachments.</td>
  </tr>
 </tbody>
</table>

### Containers {#containers}

<table>
 <tbody>
  <tr>
   <th>Adaptive Form component</th>
   <th>Corresponding XFA component</th>
   <th>Notes</th>
  </tr>
  <tr>
   <td>Panel<br /> </td>
   <td>Subform<br /> </td>
   <td>Repeatable panel maps to repeatable subform.</td>
  </tr>
 </tbody>
</table>

### Static components {#static-components}

| Adaptive Form component |Corresponding XFA component |Notes |
|---|---|---|
| Image |Image |The TextDraw and Image components, whether bound or unbound, always appear in the Document of Record for an XSD-based Adaptive Form, unless excluded using the Document of Record settings. |
| Text |Text |

### Tables {#tables}

The Adaptive Forms table components such as header, footer, and row map to corresponding XFA components. You can map repeatable panels to tables in Document of Record.

## Base template of a Document of Record {#base-template-of-a-document-of-record}

Base template provides styling and appearance information to Document of Record. It allows you to customize default appearance of auto generated Document of Record. For example, you can use base template to add your company logo in the header and copyright information in the footer of the Document of Record. 

The master page from base template is used as a master page for Document of Record template. The master page can have information such as page header, page footer, and page number that you can apply to Document of Record. You can apply such information to Document of Record using base template for auto generation of Document of Record. Using base template enables you to change default properties of fields.

Always follow [Base template conventions](#base-template-conventions) when you design base template.

## Base template conventions {#base-template-conventions}

A base template is used to define header, footer, styling, and appearance for a Document of Record. The header and footer can include information like the company logo and copyright text. The first master page in the base template is copied and used as a master page for the Document of Record, which contains header, footer, page number, or any other information that should appear across all pages in the Document of Record. If you use a base template which does not conform to base template conventions, the first master page from the base template is still used in Document of Record template. It is highly recommended that you design your base template as per its conventions, and use it for auto generation of Document of Record.

**Master page conventions**

* In the base template, name the root subform as `AF_METATEMPLATE` and the master page as `AF_MASTERPAGE`.

* The master page with the name `AF_MASTERPAGE` located under the `AF_METATEMPLATE` root subform is preferred for extracting header, footer, and styling information.

* If `AF_MASTERPAGE` is absent, the first master page present in the base template is used.

**Styling conventions for fields**

* To apply style on the fields in the Document of Record, the base template provides fields located in the `AF_FIELDSSUBFORM` subfrom under the `AF_METATEMPLATE` root subform.

* The properties of these fields are applied to the fields in the Document of Record. These fields should follow the `AF_<name of field in all caps>_XFO` naming convention. For example, the field name for check box should be `AF_CHECKBOX_XFO`.

To create a base template, do the following in AEM Designer.

1. Click **[!UICONTROL File]** &gt; **[!UICONTROL New]**.
1. Select the **[!UICONTROL Based on a template]** option.

1. Select the **[!UICONTROL Forms - Document of Record]** category.
1. Select **[!UICONTROL DoR Base Template]**.
1. Click **[!UICONTROL Next]** and provide the required information.

1. (Optional) Modify the styling and appearance of fields that you want to apply on the fields in the Document of Record.
1. Save the form.

You can now use the saved form as a base template for Document of Record. Do not modify or remove any scripts present in the base template.

**Modifying base template**

* If do not apply any styling over fields in base template, it is advisable to remove those fields from base template so any upgrades to base template are automatically picked up.
* While modifying base template, do not remove, add, or modify scripts.

Strictly follow above mentioned conventions and instructions to design a base template.

## Customize the branding information in Document of Record {#customize-the-branding-information-in-document-of-record}

While generating a Document of Record, you can change branding information for the Document of Record on the Document of Record tab. The Document of Record tab includes options such as logo, appearance, layout, header and footer, disclaimer, and whether or not you want to include unselected check box and radio button options.

To localize the branding information that you enter in the Document of Record tab, ensure the locale of the browser is set appropriately. To customize the branding information of Document of Record, perform the following steps:

1. Select a panel (root panel) in the Document of Record and then tap ![configure](assets/configure.png).
1. Tap ![dortab](assets/dortab.png). The Document of Record tab appears.
1. Select either the default template or a custom template for rendering the Document of Record. If you select the default template, a thumbnail preview of the Document of Record appears below the Template drop-down.

   ![brandingtemplate](assets/brandingtemplate.png)

   If you choose to select a custom template, browse a select an XDP on your [!DNL AEM Forms] server. If you want to use a template that is not already on your [!DNL AEM Forms] server, you need to first upload the XDP to your [!DNL AEM Forms] server.

1. Based on whether you select a default or a custom template, some or all of the following properties appear in the Document of Record tab. Specify these appropriately:

    * **Logo Image**: You can either choose to use the logo image from the Adaptive Form, choose one from DAM, or upload one from your computer.
    * **Form Title**
    * **Header Text**
    * **Disclaimer Label**
    * **Disclaimer**
    * **Disclaimer Text**
    * **Accent Color**: The color in which header text and separator lines are rendered in the document or record PDF
    * **Font Family**: Font family of the text in the Document of Record PDF
    * **For Check Box and Radio Button components, show only the selected values**
    * **Separator for multiple selected value(s)**
    * **Include form objects that are not bound to data model**
    * **Exclude hidden fields from the Document of Record**
    * **Hide description of panels**

   >[!NOTE]
   >
   >If you are using an Adaptive Form template created with a verision of Designer prior to 6.3, for Accent Color and Font Family properties to work, ensure that the following is present in your Adaptive Form template under the root subform:

   ```xml
   <proto>
   <font typeface="Arial"/>
   <fill>
   <color value="4,166,203"/>
   </fill>
   <edge>
   <color value="4,166,203"/>
   </edge>
   </proto>
   ```

1. To save the branding changes, tap Done.

## Table and column layouts for panels in Document of Record {#table-and-column-layouts-for-panels-in-document-of-record}

Your Adaptive Form may be a lengthy one with several form fields. You may not want to save a Document of Record as an exact copy of the Adaptive Form. Now you can choose a table or column layout for saving one or more Adaptive Form panels in the Document of Record PDF.

Before generating a Document of Record, in a panel's settings, select Layout For The Document of Record for that panel as Table or Column. The fields in the panel get organized accordingly in the Document of Record.

![Fields in a panel rendered in a table layout in the Document of Record](assets/dortablelayout.png)

Fields in a panel rendered in a table layout in the Document of Record

![Fields in a panel rendered in a column layout in the Document of Record](assets/dorcolumnlayout.png)

Fields in a panel rendered in a column layout in the Document of Record

## Document of Record settings {#document-of-record-settings}

Document of Record settings let you choose options you want to include in the Document of Record. For example, a bank accepts name, age, social security number, and phone number in a form. The form generates a bank account number, and branch details. You can choose to display only the name, social security number, bank account, and branch details in Document of Record.

The Document of Record settings of a component are available under its properties. To access the properties a component, select the component and click ![cmppr](assets/cmppr.png) in the overlay. The properties are listed in the sidebar, and you can find the following settings in it.

**Field level settings**

* **Exclude From Document of Record**: Setting the property true excludes the field from Document of Record. This is script-able property named `excludeFromDoR`. Its behavior depends on **Exclude fields from DoR if hidden** form level property.

* **Display panel as table:** Setting the property displays panel as table in Document of Record if panel has less than 6 fields in it. Applicable for panel only.
* **Exclude title from Document of Record:** Setting the property excludes title of the panel/table from Document of Record. Applicable for panel and table only.
* **Exclude description from Document of Record:** Setting the property excludes description of the panel/table from Document of Record. Applicable for panel and table only.

**Form level settings**

* **Include unbound fields in DoR:** Setting the property includes unbound fields from Schema based Adaptive Form in Document of Record. By default it is true.
* **Exclude fields from DoR if hidden:** Setting the property overrides the behavior of “Exclude From Document of Record” field level property when it’s not true. If fields are hidden at the time of form submission, they will be excluded from Document of Record if the property is set true, provided “Exclude From Document of Record” property is not set.
