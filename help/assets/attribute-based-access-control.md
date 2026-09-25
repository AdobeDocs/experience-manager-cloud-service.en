---
title: Attribute-based access control
description: Learn how to enable Attribute-based access control to define metadata-based rules to define the level of access to assets available in Content Hub
role: Admin
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 05f54b05-40b8-4a6c-af8f-5c3f7a2089d4
---
# Attribute-based access control {#attribute-based-access-control}

Attribute-based access control (ABAC) enables Content Hub Administrators to define **metadata-based rules** that control the level of access to assets available in Content Hub. Rather than relying on where assets are stored, ABAC governs access according to the attributes attached to each asset.

Administrators for an organization define rules for user groups, which are mapped to a **Group ID**. Rules are a mix of [logical and comparison operators](#supported-rule-constructs), and administrators can define as many rules as needed to manage asset access within Content Hub.

The rules are based on **metadata**. When the conditions defined in a rule match the asset metadata, Content Hub displays the asset to the user group. As a result, access is determined dynamically by the metadata itself rather than by where an asset is stored. Content Hub scans the asset metadata, including custom metadata, for all assets available within **All Assets** and **Collections** to display the results to user groups.

For example, ALLOW access to a user group with **Group ID = 1011** when asset metadata matches "Brand = Brand X" AND "Region = EMEA OR Americas". Content Hub then displays to the user group with ID = 1011 only those assets where ''Brand = Brand X'' and ''Region = EMEA or Americas''.

ABAC rules in Content Hub can be configured using the following approaches:

* **Self-serve configuration** using [AI Assistant in Content Hub](#configure-abac-using-ai-assistant-in-content-hub), powered by AEM Governance Agent  
* **Spreadsheet-based configuration** through [Adobe Support](#configure-abac-using-spreadsheet)

With AI Assistant in Content Hub, administrators define and manage ABAC rules using metadata and natural language. This enables faster rule configuration and reduces dependency on manual support workflows, so administrators can adjust access policies directly instead of routing every change through a support ticket.

Some of the key benefits of attribute-based access control include:

* **Eliminates the dependency on folder structure for permissions**, decoupling access control from storage location
* **Allows administrators to upload assets and retroactively determine permission structures**, so permissions can be applied after assets are already in the system
* **Reduces the number of duplicate assets and improves asset integrity**, because a single asset can be governed by rules rather than copied for each group. Duplicates are needed in folder-based permissions when the same assets must be shared with different groups.
* **Enables granular, rule-based access** driven by specific metadata attributes
* **Supports scalable governance across brands and regions**, so access policies can grow with the organization
* **Improves asset management** by centralizing access decisions around metadata

>[!VIDEO](https://video.tv.adobe.com/v/3475413/?learn=on&enablevpops){transcript=true}

## How to enable Attribute-based access control {#enable-attribute-based-access-control}

**Attribute-based access control (ABAC)** in Content Hub governs access by evaluating attributes—such as user, resource, and contextual properties—against defined rules, allowing fine-grained permissions beyond simple role assignment. Administrators enable and configure ABAC rules in Content Hub using either of the following two approaches:

* **Self-serve configuration using AI Assistant in Content Hub (powered by AEM Governance Agent)**  
  Administrators define and manage ABAC rules directly using natural language within Content Hub. This enables rapid, self-service rule creation without external tickets, making it the fastest approach for teams that want to iterate on access policies directly inside Content Hub.

* **Spreadsheet-based configuration via Adobe Support**  
  Administrators define ABAC rules in a spreadsheet and submit them through Adobe Support for configuration. This approach suits large or bulk rule sets that benefit from structured, offline preparation and review before Adobe Support applies them.

## Configure ABAC (Attribute-Based Access Control) using AI Assistant in Content Hub

With **AI Assistant** in Content Hub, powered by the **AEM Governance Agent**, you can create and manage **ABAC (Attribute-Based Access Control)** rules directly in Content Hub using natural language.

**ABAC (Attribute-Based Access Control)** governs access to content based on attributes—such as user roles, asset metadata, and contextual conditions—rather than fixed, predefined permission lists. This attribute-driven model makes access policies more granular and adaptable to changing organizational needs.

### What you can do {#what-you-can-do-ai-assistant}

Using the AI Assistant, administrators can manage the full lifecycle of ABAC rules directly through conversational prompts:

* **Search for existing rules** — locate and review current access policies quickly.
* **Create rules** — define new access controls using plain-language instructions.
* **Update rules** — modify existing policies without navigating complex configuration interfaces.
* **Delete rules** — remove outdated or unnecessary access controls.

### Why this matters {#why-this-matters-ai-assistant}

The AI Assistant empowers administrators to create and manage access rules independently, without relying on support workflows. Because rules are expressed in natural language, administrators do not need to master specialized syntax or route requests through support teams. This reduces turnaround time for access changes, minimizes dependency on external support, and gives governance teams direct, self-service control over how content is accessed and protected within Content Hub.

### Before you begin {#before-you-begin-ai-assistant}

Confirm the following prerequisites before using AI Assistant in Content Hub for attribute-based access control (ABAC) rule configuration. Each requirement below must be met to ensure the AI Assistant is available and functional within your environment:

* **Licensed for Adobe Experience Manager (AEM) as a Cloud Service** — a valid AEM as a Cloud Service license is required to access AI Assistant capabilities.
* **AI Assistant powered by the AEM Governance Agent** is enabled and available for your organization — this agent underpins the assisted ABAC rule configuration workflow.
* If access is not yet available, contact your Adobe representative and complete the required licensing steps, because entitlement is provisioned at the organization level before the AI Assistant becomes usable.
* A **generative AI (GenAI) rider is not required** for the try-buy program, allowing organizations to evaluate the AI Assistant without that additional licensing component.

### Steps to configure Attribute-Based Access Control (ABAC) rules using AI Assistant {#steps-ai-assistant}

**Attribute-Based Access Control (ABAC)** governs who can access assets based on attributes such as user group and product **metadata**, rather than static, manually maintained permission lists. In Content Hub, AI Assistant lets you create these rules using plain, **natural language** instructions, then generates a structured preview for review before anything is applied.

1. Open AI Assistant in Content Hub.

1. Start with a simple instruction.

   Begin with a broad prompt that tells AI Assistant what you want to accomplish. For example:

   `Create a new rule in Content Hub`

   AI Assistant then guides you through the information required to create the rule, prompting for any missing details.

1. Define the rule in **natural language**.

   Describe the access condition in plain language, specifying the user group, the assets, and the attribute that determines access. For example:

   `Frescopa Web Marketers user group should have access to assets where product equals Frescopa`

1. Select the environment where the **ABAC** rule must apply.

   Choosing the correct environment ensures the rule is scoped only to the intended target and does not affect other environments.

1. Review the rule before applying it.

   AI Assistant generates a structured preview of the rule. Nothing is applied automatically. You can review the generated rule, adjust it if needed, or cancel the action before applying it. This preview step gives you full control and prevents unintended access changes.

1. Save and apply the rule.

   Once saved, the rule is enforced dynamically, evaluating asset **metadata** in real time each time access is requested. Because enforcement is metadata-driven, the rule automatically applies to matching assets as they are added or updated, without requiring manual reassignment of permissions.

This mandatory review step ensures accuracy before the rule is applied, reducing the risk of granting or denying access incorrectly.

### Manage ABAC rules using prompts {#manage-abac-rules-using-prompts}

After you start using AI Assistant, you manage **Attribute-Based Access Control (ABAC)** rules conversationally, using plain-language prompts instead of navigating configuration menus. **ABAC** governs who can access assets based on attributes such as user group, region, or other metadata properties, and the AI Assistant lets you discover, create, update, and delete these rules through natural conversation. This conversational approach streamlines access management, reduces the need to memorize rule syntax, and makes it easier to keep permissions accurate as teams and content evolve.

**Discover rules**

Use these prompts to review the access rules already in place before making changes:

* Show all existing Content Hub ABAC rules

**Create rules**

Use these prompts to grant a group access to assets, either broadly or scoped to specific metadata values such as region:

* Create a rule that gives Product Marketing group access to all assets
* Give Sales group access to assets where region equals EMEA

**Update rules**

Use these prompts to extend or modify an existing rule, for example to broaden the regions a group can reach:

* Update rule for EMEA marketing group to include APAC

**Delete rules**

Use these prompts to remove an access rule that is no longer needed:

* Delete the rule for Product Marketing group

**Explore metadata and groups**

Use these prompts to see the groups and metadata properties available before defining new rules, so that your conditions reference valid attributes:

* Show available groups and metadata properties to set rules

## Configure ABAC using Spreadsheet

If AI Assistant is not enabled for your organization, you can configure Attribute-Based Access Control (ABAC) rules using the spreadsheet-based workflow. ABAC governs access to Adobe Experience Manager Assets by evaluating user, resource, and environment attributes, and the spreadsheet method provides an alternative to the AI Assistant for defining these rules.

Follow these steps to define and submit ABAC rules:

1. Click **Download Spreadsheet** to download the template and define your rules in the spreadsheet.
2. Define the rules in the spreadsheet using the guidelines described in this article.
3. Create an Adobe Support ticket and provide the rules defined in the spreadsheet to Adobe.

[!BADGE Download Spreadsheet]{type=Informative url="https://helpx.adobe.com/content/dam/help/en/experience-manager/aem-assets/ABAC_Get_Started_Template.xlsx"}

Define rules in the spreadsheet using the guidelines described in this article.

>[!IMPORTANT]
>
>After defining the rules, navigate to the **Validation Errors** tab of the spreadsheet and click **Run ABAC Validations**. Running this validation checks the defined rules for errors before submission, which ensures the rules are correctly structured. The **All validations passed** message confirms that you can provide the defined rules to Adobe.

### Steps to configure ABAC rules using Spreadsheet {#steps-spreadsheet}

Configure **Attribute-Based Access Control (ABAC)** rules through the spreadsheet workflow by completing the following steps in order:

1. Download the ABAC spreadsheet template. This template provides the standardized structure Adobe uses to interpret and apply your access rules.
1. Define access rules in the spreadsheet using **metadata-based conditions** — conditions that grant or restrict access based on content attributes such as tags, properties, or classifications rather than on individual assets. This attribute-driven approach allows rules to scale automatically as new content matching those attributes is added.
1. Map each rule to the appropriate **IMS (Identity Management System) Group ID**. Accurate mapping ensures each rule applies to the intended group of users, preventing access from being granted or denied to the wrong audience.
1. Capture the business intent of each rule in the comments field. This ensures Adobe clearly understands the purpose behind every condition and configures access accurately, reducing the risk of misinterpretation.
1. Submit an Adobe Support ticket and share the completed spreadsheet with Adobe. Attaching the finalized template gives the Adobe team everything required to review and implement your rules.
1. Adobe configures the rules for your organization based on the submitted spreadsheet, applying the defined ABAC conditions to your environment.

## Example Attribute-based access control use case {#example-metadata-based-rules}

To support a large-scale marketing rollout, team members across multiple regions and brands require access to shared digital assets, with each persona granted a specific scope defined by region and brand. **Attribute-based access control (ABAC)** enforces these access rules automatically by evaluating **asset metadata** — such as the `region` and `brand` attributes attached to each asset — rather than relying on manually maintained permission lists. Because access is determined by matching a user's assigned attributes against the metadata on each asset, permissions stay consistent and current as the asset library grows. The following table illustrates the personas for this use case and the rules that are applied:

| Persona | Role | Role Description | Group ID | ABAC Rule |
|---|---|---|---|---|
| John | EMEA Marketing Lead | Oversees marketing execution across all brands in EMEA. Needs access to approved assets for all brands intended for EMEA markets. | group-emea-marketing | region = "EMEA" |
| Mike | APAC Marketing Lead | Oversees marketing execution across all brands in APAC. Needs access to approved assets for all brands intended for APAC markets. | group-apac-marketing | region = "APAC" |
| Sophie | Brand X Manager (EMEA) | Manages Brand X identity in EMEA. Needs to see only Brand X approved content tailored to EMEA markets. | group-emea-brandx | region = "EMEA" && brand = "Brand X" |
| Tom | Brand Y Manager (APAC) | Manages Brand Y identity in APAC. Needs to see only Brand Y approved content tailored to APAC markets. | group-apac-brandy | region = "APAC" && brand = "Brand Y" |

Using these rules, Content Hub administrators gain:

* **Granular, rule-based access**: Users see only the assets relevant to their region and brand. Because the ABAC rule evaluates metadata automatically, this scoping requires no manual permission assignments, which reduces administrative overhead and the risk of misconfigured access.
* **Seamless global collaboration**: Regional and brand teams work in parallel without access conflicts, because each team's visibility is bounded precisely by its own metadata-driven rule.
* **Scalable and future-proof permissions**: As new regions or brands are added, administrators update the rules directly against the underlying metadata rather than reassigning permissions user by user. This makes the access model straightforward to extend, ensuring the permission structure keeps pace with organizational growth without disruptive rework.

### Additional scenarios where ABAC is useful {#additional-scenarios-abac}

Attribute-Based Access Control (ABAC) also addresses the following scenarios, granting or restricting access based on user attributes such as brand, market, team function, and region:

* **Global brand and regional access**: Teams see only assets relevant to their brand and market. This maintains brand consistency and reduces the risk of accidental cross-brand or cross-market asset exposure.
* **Agency and partner collaboration**: External agencies and partners can access only the campaign assets relevant to them. This limits third-party exposure to unrelated internal assets while enabling focused collaboration.
* **Role-based access for different teams**: Teams such as marketing, sales, and legal can access assets relevant to their function, ensuring each team works only with content pertinent to its responsibilities.
* **Region-specific legal compliance**: Users can be restricted to assets approved for specific regulatory or regional requirements, helping enforce compliance boundaries and prevent use of unapproved content in a given jurisdiction.

>[!IMPORTANT]
>
>ABAC operates on a **default-deny** principle. By default, **all other user groups that are not specified with any rules** in the [spreadsheet](#configure-abac-spreadsheet) are **denied access**. Because access is granted only through explicitly defined rules, if a user is not part of any group for which ABAC rules are defined, that user cannot access any assets. If some users must have access to all assets — for example, Admins — include a group with a Group ID in the spreadsheet and specify that the group requires access to all assets so Adobe can configure it accordingly.

## Supported rule constructs {#supported-rule-constructs}

Rules are built from two categories of constructs: **logical operators**, which combine multiple conditions, and **comparison operators**, which test individual user or asset attributes against a value. Together these constructs define exactly when access is granted or denied.

* **Logical operators** (combine conditions into a single evaluation):
  * **AND**: All conditions must evaluate to true for the rule to match. Because every clause must hold, AND narrows the scope of a rule and enforces stricter access requirements.
  * **OR**: At least one condition must evaluate to true for the rule to match. Because any single satisfied clause is sufficient, OR broadens the scope of a rule and covers multiple qualifying cases.

* **Comparison operators** (test a single attribute against a value):
  * **Equals (=)**: Checks whether a user or asset attribute **matches** a specified value. This ensures an access decision applies only when the attribute exactly corresponds to the target value.
  * **Not Equals (!=)**: Checks whether a user or asset attribute **does not match** a specified value. This ensures a rule excludes entities whose attribute differs from the target value.

**Array-valued metadata behavior**: When asset metadata fields contain arrays — for example, multiple regions or multiple tags — the comparison operators shift to set-membership semantics. In this case, **Equals resolves to *contains* logic**, matching when the specified value is present anywhere in the array, and **Not Equals resolves to *does not contain* logic**, matching only when the specified value is absent from the array entirely. This complete definition matters because it determines how multi-valued attributes are evaluated during access decisions.

Because these operators combine cleanly, they let you write simple yet expressive rules that read almost like plain language. For example, the rule **ALLOW if region = emea (Europe, Middle East, and Africa) AND assetType != prototype AND tags != confidential** grants access only to assets located in the EMEA region, excludes any asset marked as a prototype, and excludes any asset whose tags array contains the value `confidential`. As a result, a single readable statement expresses a precise, multi-condition access policy.

## Guidelines {#guidelines-attribute-based-access-control}

The following guidelines apply to both AI Assistant-based and spreadsheet-based configuration of **Attribute-Based Access Control (ABAC)** rules:

* **ABAC rules apply only to assets approved for Content Hub.** For more information, see [Approve Assets for Content Hub](/help/assets/approve-assets-content-hub.md).
* **Do not define DENY rules. Always convert DENY rules into ALLOW rules.** ABAC evaluation in Content Hub is built around allow-based logic, so expressing every condition as an **ALLOW** rule ensures access is granted explicitly and predictably rather than inferred from exclusions. For example, `ALLOW if region = user-region DENY if assetType = prototype AND confidential = yes` can be converted to `ALLOW if region = user-region AND (assetType != prototype OR confidential != yes)`.
* **ABAC rules are applied to user groups using the Identity Management System (IMS) Group ID**, which is available in the Admin Console. Using the IMS Group ID ensures rules bind to the correct group identity consistently.
* You can set the [Approval Target](/help/assets/approve-assets-content-hub.md#set-approval-target) for assets using the AEM as a Cloud Service author environment. **ABAC rules are applied to assets approved with Approval Target = Content Hub.** In contrast, **Approval Target = Delivery** is for assets available for both Delivery and Content Hub. Because assets marked as **Approval Target = Delivery** are visible to all users in Content Hub, ABAC restrictions do not limit their visibility.
* Ensure that the metadata schemas used in ABAC rules are correctly defined and available in AEM. Provide the full path of the metadata schema or schemas in AEM that define the properties referenced in ABAC rules. Optionally, create a test folder with sample assets that match the ABAC conditions to verify rule behavior and evaluate access accurately.
* Capture the business intent of the rule in comments, even when the condition is correctly written, because the documented intent helps validate and correct the logic if required.
* Ensure that metadata values used for access rules, such as **brand**, **region**, and **product**, are maintained consistently across assets. Consistent metadata values prevent rules from failing to match assets that should be governed by them.
* Start with key use cases such as **brand-based** or **region-based** access, as these represent the most common and straightforward access-control scenarios.
* Use clear prompts when defining rules with AI Assistant. Describe the intent in business language so that AI Assistant can accurately translate it into a structured rule.
* License **Portable Document Format (PDF)** files that are set for **Digital Rights Management (DRM)** must remain visible to all users, so that users can review the license information when downloading the asset with its license.

## Frequently asked questions {#faqs-attribute-based-access-control-content-hub}

### What is Attribute-Based Access Control (ABAC)?

**Attribute-Based Access Control (ABAC)** is an authorization model that grants or denies access to resources by evaluating **attributes** rather than fixed roles alone. In ABAC, access decisions are determined dynamically at request time by comparing the attributes of the user, the resource, the action, and the surrounding environment against a set of defined **policies**. Because these decisions are computed from attribute values rather than static permissions, ABAC supports fine-grained, context-aware access control that scales across large and complex systems.

### Which attributes does ABAC evaluate?

ABAC policies typically draw on four categories of attributes:

- **Subject attributes** — characteristics of the user or entity requesting access, such as department, job title, clearance level, or group membership.
- **Resource (object) attributes** — properties of the content or asset being accessed, such as classification, owner, content type, or sensitivity label.
- **Action attributes** — the operation being requested, such as read, edit, publish, or delete.
- **Environmental attributes** — contextual conditions at the time of the request, such as time of day, location, device type, or network.

By combining these attributes, ABAC evaluates each request against policy rules and returns an allow or deny decision. This mechanism ensures that access reflects the specific circumstances of a request rather than a single predefined role.

### How does ABAC differ from Role-Based Access Control (RBAC)?

Unlike **Role-Based Access Control (RBAC)**, which grants permissions based on a user's assigned role, ABAC grants permissions based on multiple attributes evaluated together. RBAC assigns access through relatively static role definitions, which can become difficult to manage as the number of roles multiplies. ABAC, in contrast, expresses access rules as policies that reference attributes, allowing a single policy to cover many scenarios without creating a new role for each combination. As a result, ABAC generally offers greater flexibility and finer granularity, while RBAC is often simpler to configure for straightforward permission structures. Many organizations combine both models, using roles as one attribute within a broader attribute-based policy.

### Why use ABAC in a content hub?

In a content hub, ABAC is used to control who can view, edit, or publish specific content items based on their attributes. This approach enables administrators to define access rules once and apply them consistently across large content libraries, because access is evaluated from attributes such as content classification and user department rather than manually assigned permissions on each item. Practical benefits include:

- **Fine-grained control** — access can be tailored to individual content items and conditions.
- **Scalability** — policies apply automatically as new content and users are added, reducing manual administration.
- **Context-awareness** — access can respond to environmental factors such as location, time, or device.
- **Consistency** — centralized policies enforce uniform access rules across the entire content hub.

### How are ABAC policies defined?

ABAC policies are defined as rules that specify which attribute conditions must be satisfied for an action to be permitted. Each policy links **subjects**, **resources**, **actions**, and **environmental conditions** into logical statements that the access control engine evaluates at request time. Because policies reference attributes rather than named individuals, they remain valid as users and content change, which reduces ongoing maintenance and helps enforce the principle of least privilege.

### Is ABAC more secure than role-based approaches?

ABAC can strengthen security by enabling more precise, context-sensitive access decisions than role-only models. Evaluating multiple attributes together allows an organization to enforce nuanced conditions — for example, restricting access to sensitive content unless several criteria are met simultaneously. The effectiveness of ABAC depends on well-designed policies and accurate attribute data, so security outcomes improve when attribute sources are kept reliable and up to date.

### What is Attribute-based Access Control (ABAC) in AEM Assets Content Hub?

**Attribute-based Access Control (ABAC)** in AEM Assets Content Hub is a permission model that lets administrators define **metadata-based rules** to control the level of access that different user groups have to digital assets. Rather than assigning permissions asset-by-asset, administrators express access policies as conditions evaluated against the attributes stored in each asset's metadata.

**How ABAC Determines Access**

Access is granted or denied based on whether an asset's metadata matches the conditions specified in the rules. Because the asset's metadata is evaluated against these conditions at request time, permissions apply automatically and consistently across the asset library. As a result, when an asset's metadata satisfies a rule's conditions, the associated user group can view or work with that asset; when it does not, the asset remains hidden from that group.

**Key Characteristics of Attribute-based Access Control**

- **Metadata-driven:** Access decisions are based on asset attributes such as classification, department, region, campaign, or usage rights, rather than on static, per-asset permission lists.
- **Granular:** Rules can target precise combinations of metadata conditions, giving administrators fine-grained control over exactly which assets each user group can access.
- **Dynamic:** Because access follows the metadata, visibility updates automatically as asset metadata changes or as new assets that match existing rules are added — no manual re-permissioning is required.
- **Group-oriented:** Policies are applied to defined user groups, ensuring each audience sees only the assets relevant to its role.

**Practical Applications and Benefits**

Attribute-based Access Control is well suited to large, shared asset repositories where many teams work from the same Content Hub but require different levels of visibility. Common applications include restricting confidential or unreleased assets to specific teams, limiting region-specific content to the corresponding markets, and enforcing usage-rights or licensing constraints by exposing assets only to groups permitted to use them. This dynamic, metadata-based approach reduces manual administrative overhead, minimizes the risk of assets being exposed to the wrong users, and keeps access policies aligned with the asset library as it grows and changes.

### How do administrators define access rules using ABAC in AEM Assets Content Hub?

Administrators define access rules in **Attribute-Based Access Control (ABAC)** within **Adobe Experience Manager (AEM) Assets Content Hub** by building conditions on asset metadata and linking those conditions to specific user groups. **ABAC** is an access model in which permissions are granted dynamically based on the **attributes** of an asset rather than fixed, manually assigned permissions, allowing visibility to scale automatically as new content is added.

**How ABAC Access Rules Work**

Administrators create access rules through the following steps:

1. **Define metadata conditions** — Set conditions based on asset metadata attributes, such as **brand** or **region**.
2. **Apply logical and comparison operators** — Combine attributes using operators to express precisely which assets qualify for a rule.
3. **Link conditions to user group IDs** — Associate each condition with specific **user group IDs**, mapping matching assets to the groups that should see them.

**Key Components of ABAC Rules**

- **Metadata attributes:** Asset properties such as brand or region serve as the basis for each condition, so access follows the content itself rather than individual asset assignments.
- **Logical and comparison operators:** These operators enable granular, precise control, allowing administrators to define narrow or broad conditions that match exactly the intended set of assets.
- **User group IDs:** Rules connect qualifying assets to defined user groups, determining precisely which assets remain visible to each user group.

Because access is driven by attributes, ABAC rules apply automatically to any asset that matches the defined conditions. As a result, new assets tagged with the relevant metadata inherit the correct visibility without requiring manual reassignment, which reduces administrative overhead and helps enforce consistent, scalable governance across large asset libraries.

### What are the main benefits of using ABAC over traditional folder-based permissions in AEM Assets Content Hub?

**Attribute-Based Access Control (ABAC)** in Adobe Experience Manager (AEM) Assets Content Hub grants permissions based on asset attributes and metadata rather than physical folder location. This is the primary advantage over traditional folder-based permissions: access is determined by what an asset *is*, not where it is stored.

**Key Benefits of ABAC in AEM Assets Content Hub**

- **Eliminates dependency on folder structures for permissions.** Access rights are driven by attributes and metadata rather than a fixed folder hierarchy, so administrators are no longer forced to design folder trees around who can see what.
- **Enables retroactive permission assignment.** Administrators can upload assets first and assign permissions afterward, decoupling the ingestion of content from the definition of access rules.
- **Reduces the number of duplicate assets needed**, because a single asset can be governed by multiple attribute-based rules rather than being copied into separate folders to serve different audiences.
- **Simplifies sharing across multiple groups.** When the same asset must be made available to several teams or audiences, ABAC allows one authoritative copy to be exposed to each group through attribute rules instead of duplicated placements.

**Why ABAC Simplifies Permission Management**

Because permissions are attached to attributes rather than folder paths, ABAC removes the rigidity that forces administrators to duplicate assets or restructure folders whenever access needs change. This is especially valuable when assets need to be shared with multiple groups, since one governed asset can satisfy many access scenarios at once.

As a result, ABAC improves asset integrity and simplifies permission management. Maintaining fewer duplicate copies means a single source of truth for each asset, which reduces version drift and the risk of outdated files circulating. By separating asset upload from permission assignment, ABAC gives administrators a more flexible, scalable model for controlling access across large and evolving asset libraries.

### Can administrators set up ABAC rules directly in the AEM Assets Content Hub interface?

Yes. Administrators can configure **Attribute-Based Access Control (ABAC)** rules directly within the **Adobe Experience Manager (AEM) Assets Content Hub** interface. ABAC governs asset access based on attributes such as user roles, asset metadata, and organizational context, allowing permissions to be applied dynamically rather than through fixed, manually assigned lists.

Administrators have two supported paths for setting up ABAC rules:

- **AI Assistant in Content Hub** — Administrators configure ABAC rules directly in the interface using the **AI Assistant**, provided this capability is enabled for their organization. This in-interface approach lets teams define and adjust access rules without leaving Content Hub.
- **Spreadsheet-based workflow through Adobe Support** — Administrators can continue to use the established **spreadsheet-based workflow through Adobe Support**, which remains available as an alternative method for defining ABAC rules.

Because both options produce the same ABAC governance outcome, organizations can choose the AI Assistant for direct, in-interface configuration or retain the spreadsheet-based workflow according to their operational preferences and the features enabled for their environment.

### What types of metadata conditions can be used while setting up ABAC rules in AEM Assets Content Hub?

Attribute-Based Access Control (ABAC) rules in Adobe Experience Manager (AEM) Assets Content Hub support two categories of metadata conditions: **logical operators** and **comparison operators**, evaluated against metadata attributes defined in the AEM metadata schemas. ABAC governs who can access which assets by evaluating the attributes attached to content, so the metadata conditions form the core logic that determines access outcomes.

**Supported Operators**

ABAC rules combine and compare metadata values using the following operator types:

- **Logical operators** — **AND** and **OR**, used to combine multiple metadata conditions within a single rule.
- **Comparison operators** — **equals** and **not equals**, used to test whether a metadata attribute matches or does not match a specified value.

Combining logical and comparison operators allows a single rule to express both broad and precise access conditions.

**Eligible Metadata Attributes**

Metadata conditions can be built on a range of attribute fields commonly associated with digital assets, including:

- **Region**
- **Brand**
- **Product**
- **Campaign**
- **Asset type**
- **Publishing status**

These attributes let organizations scope access according to how assets are categorized — for example, restricting visibility by market region, brand ownership, product line, campaign association, asset format, or publication state.

**Metadata Schema Requirement**

Metadata properties referenced in ABAC rules must be correctly defined and available in the AEM metadata schemas. This requirement ensures the rule engine can reliably locate and evaluate each attribute; if a property is missing or improperly configured in the schema, the corresponding condition cannot be assessed and the rule may not apply as intended. Confirming that every field used in a rule exists in the schema is therefore essential to consistent and predictable access control.

### Why is AEM Assets Content Hub ABAC particularly useful for organizations with large teams and diverse asset needs?

**Attribute-Based Access Control (ABAC)** in Adobe Experience Manager (AEM) Assets Content Hub is particularly useful for organizations with large teams because it enables **granular, rule-based access to assets** determined automatically by user and asset attributes rather than manually maintained permission lists. This makes ABAC well suited to enterprises managing diverse asset libraries across multiple teams, markets, and product lines.

**How ABAC Controls Asset Access**

Unlike static, role-only permission models, ABAC evaluates a combination of attributes at the moment of access and grants visibility only when the defined rules are satisfied. Access decisions are typically driven by attributes such as:

- **User roles** — matching assets to a person's job function or responsibilities
- **Regions** — restricting or exposing assets based on geography or market
- **Brands** — separating assets by brand identity within a multi-brand organization
- **Business needs** — aligning access with team, department, or campaign requirements

Because these rules are applied dynamically, administrators define the logic once and let the system enforce it consistently across the entire asset catalog.

**Practical Benefits for Large, Distributed Teams**

ABAC ensures that users see only the assets relevant to their responsibilities, which directly reduces clutter, prevents accidental use of unauthorized content, and keeps large asset libraries navigable. As a result, organizations gain several practical advantages:

- **No manual permission assignments** — access is governed by rules rather than one-by-one grants, reducing administrative overhead as teams grow.
- **No excessive duplication of assets** — a single, centrally managed asset can be exposed to the right audiences through attributes, rather than copied into separate silos for each team, region, or brand.
- **Relevant, filtered experiences** — because visibility is tied to responsibilities, each user works from a view scoped to their needs, improving efficiency and asset governance.

This attribute-driven approach scales cleanly for organizations with large teams and diverse asset needs, since adding new users, regions, or brands requires updating attributes and rules rather than rebuilding permissions across the system.

### How should administrators prepare the ABAC spreadsheet for AEM Assets Content Hub before submitting it to Adobe Support?

To prepare the **Attribute-Based Access Control (ABAC)** spreadsheet for **AEM Assets Content Hub**, administrators must complete a sequence of configuration and documentation steps before submitting it to Adobe Support. ABAC governs access by evaluating attributes—such as user group membership, permissions, and metadata conditions—so a correctly structured spreadsheet is essential for Adobe Support to translate the intended access model into a working configuration.

**Steps to Prepare the ABAC Spreadsheet**

1. **Create user groups in the Adobe Admin Console.** Set up the required user groups within the **Adobe Admin Console**, the central location for managing users and groups across Adobe products. Establishing groups here ensures that access rules map to real, provisioned identities rather than placeholder values.
2. **Record the Group IDs.** Note the **Group IDs** for each user group. These identifiers uniquely reference each group in the spreadsheet, allowing Adobe Support to match every access rule to the correct group without ambiguity.
3. **Define permissions and conditions for each group.** Clearly specify the permissions and conditions that apply to each group directly in the spreadsheet. Explicit definitions prevent misinterpretation and ensure each group receives exactly the access it is intended to have.
4. **Map metadata properties to the appropriate schemas.** Confirm that all **metadata properties** are correctly mapped to their corresponding **schemas**. Accurate mapping is critical because ABAC conditions rely on metadata attributes, and any mismatch between properties and schemas can cause access rules to fail or behave unexpectedly.
5. **Document business intent in the comments column.** Use the **comments column** to clarify the business intent behind each rule. This context helps Adobe Support understand the purpose of every rule, reducing back-and-forth clarification and ensuring the final configuration reflects the organization's actual access-governance goals.

Completing these steps produces a self-explanatory, verifiable spreadsheet that streamlines the handoff to Adobe Support and reduces the risk of configuration errors during implementation.

**See also**

* [Translate Assets](/help/assets/translate-assets.md)
* [Assets HTTP API](/help/assets/mac-api-assets.md)
* [Assets supported file formats](/help/assets/file-format-support.md)
* [Search assets](/help/assets/search-assets.md)
* [Connected assets](/help/assets/use-assets-across-connected-assets-instances.md)
* [Asset reports](/help/assets/asset-reports.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Download assets](/help/assets/download-assets-from-aem.md)
* [Manage metadata](/help/assets/manage-metadata.md)
* [Manage Dynamic Media templates](/help/assets/dynamic-media/manage-dynamic-media-templates.md)
* [Manage reports in Assets view](/help/assets/manage-reports-assets-view.md)
* [Search facets](/help/assets/search-facets.md)
* [Manage collections](/help/assets/manage-collections.md)
* [Bulk metadata import](/help/assets/metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)
