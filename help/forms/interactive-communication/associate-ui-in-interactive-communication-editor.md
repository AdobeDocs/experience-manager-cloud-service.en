
# Associate UI in Interactive Communication Editor

The **Associate UI** is a purpose-built interface for field associates, service agents, and other customer-facing teams who interact with customers either in person or virtually. It empowers them to generate personalized, compliant communications—such as notices, letters, and service updates—during real-time customer interactions.

Built on top of **Interactive Communications (IC)**, the Associate UI provides a simplified and controlled environment where only the necessary fields are exposed for data entry, ensuring accuracy, compliance, and ease of use.

## Overview of the Associate UI

The Associate UI offers a clean, intuitive workspace where associates can:

* Select and use published Interactive Communications.
* Fill in fields on the **left panel**.
* View a real-time preview of the communication on the **right panel**.
* Generate and send notices instantly, ensuring consistency and compliance.

This interface limits unnecessary editing options, reduces errors, and supports associates in high-volume service scenarios.

## User Personas in the Associate UI

The Associate UI operates around **three primary user personas**, each with distinct responsibilities:

### Administrator

Administrators manage the overall setup, permissions, and backend configurations required for the Associate UI.

**Key Responsibilities:**

* Assign and manage user permissions for associate UI access.
* Create and manage user groups such as **forms-associates**.
* Configure backend systems including:

  * Form Data Models (FDM)
  * Customer data retrieval services
  * Output services (PDF generation, email)
* Ensure secure, compliant access aligned with organizational rules.
* Maintain performance, integration, and security for all related systems.

### Author / IC Designer

Authors design, configure, and prepare the Interactive Communication to be used by associates.

**Key Responsibilities:**

* Design IC templates, fragments, and layouts.
* Configure Form Data Models (FDM) and map fields correctly.
* Determine which fields should be **editable**, **mandatory**, or **read-only** for associates.
* Apply data validations to ensure correct and regulated data entry.
* Enable the Associate UI for each IC and assign field-level access.
* Publish the IC and provide the **published IC link** to associates.
* Ensure that the IC output (PDF, email, print) meets compliance, branding, accessibility, and regulatory requirements.

### Business Associate (End User)

The associate uses the published IC through the Associate UI to generate and deliver real-time communications.

**Key Responsibilities:**

* Open the link to the published IC provided by the author.
* Enter or confirm customer-specific data in the left panel.
* View a live preview of the document on the right panel.
* Generate, download, or send notices to customers via approved channels (email/print).
* Ensure accuracy of customer information during the interaction.

## Enabling the Associate UI for an Interactive Communication

To make an IC available within the Associate UI, the following steps must be performed:

### Step 1: Create and Publish the Interactive Communication

The author designs and configures the IC, including:

* Layout, components, and fragments
* Data bindings and validations
* Prefill logic and data model connectivity
* Output configurations

After review, the author publishes the IC.

### Step 2: Enable Associate UI Access

In the IC settings, the author must:

* Enable the *Associate UI* for the communication.
* Choose which fields are:

  * Editable
  * Mandatory
  * Read-only
* Define the allowed communication modes (PDF, email, print).

### Step 3: Assign User Permissions

Administrators assign permissions to the **forms-associates** group.

Permissions define:

* Which IC templates associates can view and access.
* Whether they can generate/download/send communications.
* Any restricted fields or data elements.

### Step 4: Provide the Published IC Link to Associates

Authors share the published IC URL with associates.

When associates open the link:

* The **left panel** displays fields they can fill.
* The **right panel** displays a real-time preview of the communication.

This ensures a seamless fill-and-preview workflow.

### Step 5: Enable in Business Portal (Optional)

Organizations can embed the published IC in their business portals by using the generated **HTML file**, allowing associates easy access within their existing systems.

## Authoring Best Practices

* Keep only essential fields editable.
* Provide clear labels, instructions, and validation messages.
* Use conditional sections to reduce clutter.
* Apply correct data bindings and prefill configurations.
* Ensure accessibility and compliance for all components.
* Protect legal texts and disclaimers from being edited.

## Administrative Best Practices

* Maintain accurate user group membership (e.g., **forms-associates**).
* Validate backend integrations and data availability.
* Monitor audit logs for traceability.
* Test email/print channels periodically.

The Associate UI in the Interactive Communication Editor bridges the gap between IC authoring and real-time customer engagement. By coordinating the roles of admins, authors, and associates and ensuring the right permissions, data models, and workflows. The Associate UI enables organizations to deliver fast, accurate, and compliant communications directly during customer interactions.

