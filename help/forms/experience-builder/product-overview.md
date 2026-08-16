---
title: Forms Experience Builder
description: Leverage generative AI to create adaptive forms using natural language. Forms Experience Builder enables both technical and non-technical users to design forms without coding.
feature: Edge Delivery Services
role: Admin, Developer
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: 183e999c-9896-49a2-b29b-7c77da380df9
---
# Overview

The AEM Forms Experience Builder leverages Generative AI to accelerate the creation of digital forms through natural language. This powerful tool enables both technical and non-technical users to design, modify, and optimize professional-grade forms using a simple, conversational interface.

Forms Experience Builder enables rapid form creation through conversational AI while empowering non-technical users to create sophisticated forms without coding knowledge. You can design complex layouts, implement validation rules, and configure submission actions through simple conversational commands.

## Core capabilities

Forms Experience Builder offers two primary workflows for creating powerful digital forms:

### AI-powered form creation

**Natural Language Form Generation**

Create complete forms from scratch using plain English descriptions. Simply describe your requirements, such as "Create a customer feedback form with rating scales and comment fields," and the Forms Experience Builder generates the appropriate form structure. You use the experience builder of visual editors to add more fields, validation rules, and submission logic. 

**Dynamic Field Management**

Add, modify, or remove form fields through conversational commands. The AI understands context and can intelligently suggest field types, validation rules, and user interface improvements based on your requirements.

**Layout Optimization**

Update form layouts and configurations through natural language. Request changes like "Change form layout to wizard layout" and the Forms Experience Builder applies appropriate styling and layout adjustments.

### Intelligent import and conversion

Transform existing documents into interactive digital experiences. The Forms Experience Builder supports various formats, analyzing uploaded content to detect field types, preserve layouts, and enhance forms with responsive design and advanced logic. Supported formats include:

- **Acroforms**: Interactive PDF forms with existing field structures
- **XFA PDFs**: Complex XML-based form architectures
- **Flat PDFs**: Static documents converted to interactive forms
- **Images and Screenshots**: JPG, PNG formats
- **Hand-drawn Forms**: Sketches and paper form photographs


## Forms Experience Builder demo {#forms-experience-builder-demo}

>[!VIDEO](https://video.tv.adobe.com/v/3463164/)

## Onboarding & pre-requisites 

Experience Builder requires AEM Forms as a Cloud Service production author environment with [Adaptive Forms Core Components](/help/forms/enable-adaptive-forms-core-components.md).  

## Access the Forms Experience Builder


1. Navigate to **AEM > Forms > Forms & Documents**.
1. Click **Create** and select **Adaptive Form**
1. Use the Wizard to create a new form using a [Core Components template](/help/forms/creating-adaptive-form-core-components.md) or [Edge Delivery Services](/help/edge/docs/forms/universal-editor/create-forms.md) template, depending on your requirement and open the form for editing. 
1. Select the **Forms Experience Builder** icon in the editor's toolbar to open the Forms Experience builder interface to create forms using natural language.


| ![Adaptive Forms Editor - Forms Experience Builder](/help/edge/docs/forms/assets/adaptive-forms-editor.gif "Adaptive Forms Editor - Forms Experience Builder") | ![Universal Editor - Forms Experience Builder](/help/forms/assets/ue-forms-experience-builder.gif "Universal Editor - Forms Experience Builder") |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| *Adaptive Forms Editor* | *Universal Editor* |

## Start exploring

Here are a few ways you can start exploring the Forms Experience Builder:

- **Build forms incrementally**: Start with a simple form and add complexity step-by-step. For example, create a basic contact form, then add validation rules, placeholder text, and conditional logic. [Learn more](/help/forms/experience-builder/forms-experience-builder-prompt-examples-library.md#incremental-development-examples).

- **Create smart fields**: Leverage the AI's knowledge to create fields with pre-populated, context-aware options, such as a dropdown list of all countries, major airports, or industry-standard job titles. [Learn more](/help/forms/experience-builder/forms-experience-builder-prompt-examples-library.md#llm-enhanced-smart-fields).

- **Implement complex business logic**: Define conditional rules that show or hide form sections based on user input. For example, create a rule that reveals a "Spouse Information" section only when a user's marital status is "Married". [Learn more](/help/forms/experience-builder/forms-experience-builder-prompt-examples-library.md#rule-creation--business-logic).

- **Integrate with your systems**: Configure form submissions to connect with your existing business workflows, whether it's sending data to a REST API, creating a new lead in your CRM, or saving documents to cloud storage. [Learn more](/help/forms/experience-builder/forms-experience-builder-prompt-examples-library.md#data-integration--submission). 
