---
title: Create your first Interactive Communication 
description: Design Dynamic, Data-Driven Communications with Ease with AEM Forms Interactive Communications
feature: Release Information
role: Admin
hide: yes
hidefromtoc: yes
---

# Create your first Interactive Communication 


>[!VIDEO](https://video.tv.adobe.com/v/3444094/)

## Step 1: Plan the Interactive Communication

The first step in planning an Interactive Communication is to finalize the content of the Interactive Communication. After the content is finalized, you must analyze it to identify the various asset types that are required to create the Interactive Communication.

### Planning considerations

An interactive communication includes the following elements:

* **Static text** mostly includes the parts of the interactive communication that are generic in nature and are included in communication to all the customers. For example, header, footer, salutation, or disclaimers.

* **Data sourced from a backend system (form data model)** is customer-specific and is dynamically merged with the interactive communication. For example, the policy number or address can be sourced using form data model.

* **Layout or templates** for the Print and Web version of the Interactive Communication.

* **Order** in which the various text paragraphs appear in the Interactive Communication.

* **Conditional data** that gets populated based on predefined conditions. For example, the date when the interactive communication is generated.

* **Images stored in a repository**, such as logos and signature images. Images such as corporate logos would appear in most or all interactive communication.

* **Charts and tables** required to simplify the representation of complex data in an Interactive Communication

### Anatomy of the Interactive Communication

Once you have finalized the content and elements that are used to create your Interactive Communication, you can create an anatomy of the Interactive Communication. The anatomy must have the details listed in the Planning Considerations section. For example, an anatomy of the monthly bill that a telecom operator sends to its customers.

The anatomy includes data with the following modes of input:

* Static text
* Form data model
* Conditional data
* Images

 
## Step 2: Create form data model

A form data model lets you connect an Interactive Communication to disparate data sources. For example, AEM user profile, RESTful web services, SOAP-based web services, OData services, and relational databases. A form data model is a unified data representation schema of business entities and services available in connected data sources. You can use the form data model with an Interactive Communication to retrieve data from connected data sources. For more information about form data model, see [AEM Forms Data Integration](/help/forms/data-integration.md).
 
## Step 3: Create fragments

Document fragments are reusable components of a correspondence that are used to compose an Interactive Communication. The document fragments are of types: Text, List, and Condition.

 
## Step 4: Create templates

Interactive Communications editor provides multiple templates OOTB. You can modify these templates as per requirements of your organization or create a template from scratch.

 
## Step 5: Create an Interactive Communication

Once you create all the building blocks such as form data model, document fragments, and templates for the web version, you can start creating an Interactive Communication. To start creating an interactive communication:

1. Login to your AEM Forms as a Cloud Service environment.
1. Go to Forms > Forms & Documents
1. Click **Create** and select **Communication Document**. You are presented with a configuration screen to set up the following options:

    |Field | Description | Mandatory |
    |-------|-------------|----------|
    | Name | Unique identifier for the communication | Yes |
    | Title | Display name of your communication | Yes |
    | Description | Brief description of the communication's purpose | No |
    | Template | Select a pre-configured template or start from scratch | Yes |
    | Tags | Add metadata tags for better organization | No |

1. Go to the 'Presets' tab, and configure the following options:

    |Field | Description |
    |-------|-------------|
    | Preset List | Select a pre-configured preset for the document's size. Common options include A4, Letter, and more. |
    | Preset Width | Displays the preset width for selected preset list.  |
    | Preset Height | Displays the preset height for selected preset list. |
    | Preset Unit | Select the unit of measurement for the document's dimensions (e.g., Millimeters, Inches). |
    | Preset Orientation | Choose the orientation of the document - either Portrait or Landscape. |

1. Click **Create**. The Communication opens in the editor. 
1. Drag and drop components and fragments to design the Interactive Communication. 

    * Use **Master Page** for the content common across pages. Master pages are designated to format pages, and they help to facilitate design consistency because they can provide a background and layout format for more than one page in a document design.

    * Use **Pages** to layout content and layout of your document. Each page derives its size and orientation from a master page and, by default, each page is associated with the default master page that Designer creates.
   

1. Use the `@` notation to autocomplete data fields based on the connected data model. 
1. Use the `PDF Preview` option to preview the document along with data. You require the data file in JSON Format. 
