---
title: Text Box Component in Interactive Communication Editor 
description: Text Box Component in Interactive Communication Editor in AEM Forms allows authors to input and display text content within a communication.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
---

# Text Box Component in Interactive Communication Editor 

>[!NOTE]
>
> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This prompt library is currently being tested against the product and is subject to updates and revisions. Prompts, examples, and best practices may change as the Forms Experience Builder continues to evolve during the early-adopter program.

## 1. Introduction 

The **Text Box** component in the Interactive Communication Editor allows authors to input and display text content within a communication. It is one of the most fundamental and widely used components, commonly used to collect names, comments, feedback, or custom data when designing interactive communications or communication fragments.  

The Text Box supports **data binding**, enabling authors to combine static and dynamic content seamlessly, for example: ***"User's name: @name"***, where @name is a bound data field that dynamically populates when the document is saved as a PDF. Additionally, it supports rich text formatting and flexible positioning for precise layout control. 

![Find IC Doc](/help/forms/interactive-communication/assets/textbox.png)

## 2. Properties 

The text box component provides a wide set of properties to help configure its look, feel, and behavior. 

2.1 Typography 

**Font Family:** Allows selection of font styles such as Arial, Helvetica, Times New Roman, etc. 

**Font Validation:** Optional input constraints can be applied to ensure only text, numeric, or special formats are accepted. 

**Text Alignment:** Options include left, right, center, or justified alignment. 

**Text Styling:** Enable text formatting with bold, italic, strikethrough and underline features. 

**Lists:** Supports insertion of ordered (numbered) and unordered (bulleted) lists. 

2.2 Position 

**Width & Height:** Set the dimensions of the text box in pixels or percentage relative to the container. 

2.3 Margin 

Define spacing around the text box: 

- Top (Up) 

- Bottom (Down) 

- Left 

- Right 

2.4 Appearance 

- **Text Fill:** Customize color and transparency for text. 

- **Fill:** Set background color of the text box. 

- **Stroke:** Add borders with customizable: 

    - Width (thickness) 

    - Style (solid, dashed, dotted) 

    - Edge (rounded or sharp corners) 

2.5 Presence 

**Visible:** Default setting; text box is displayed to the user. 

**Hidden:** Text box is included in the form but not shown. 

 

## 3. Usage 

The Text Box is used for: 

- Collecting customer information like names, comments, or feedback. 

- Entering alphanumeric values. 

- Integrating personalized messages using bound data models. 

- Embedding inside fragments for repeated use across documents. 

Authors can drag the Text Box from the component Library into the Design View, or master view and configure its behavior using the Properties Panel. 

## 4. Best Practices 

- Always associate Text Boxes with meaningful field labels to improve accessibility. 

- Use appropriate input validations to prevent data entry errors. 

- Ensure responsive layout by setting margins and widths relative to parent containers. 

- Avoid excessive font styles that could hinder readability. 

By configuring the Text Box properties thoughtfully, authors can create interactive, responsive, and user-friendly communication experiences within AEM's Interactive Communication Editor. 
