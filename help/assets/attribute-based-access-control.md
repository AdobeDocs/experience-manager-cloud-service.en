---
title: Attribute-based access control
description: Learn how to enable Attribute-based access control to define metadata-based rules to define the level of access to assets available in Content Hub
role: Admin
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 05f54b05-40b8-4a6c-af8f-5c3f7a2089d4
---

# Attribute-based access control {#attribute-based-access-control}

Attribute-based access control (ABAC) allows Content Hub Administrators to define metadata-based rules to control the level of access to assets available in Content Hub.

Administrators for an organization define rules for user groups, which are mapped to a Group ID. Rules are a mix of [logical and comparison operators](#supported-rule-constructs), and administrators can define as many rules as needed to manage asset access within Content Hub.

The rules are based on metadata. If the conditions defined in a rule match the asset metadata, the asset is displayed to the user group. Content Hub scans the asset metadata, including custom metadata, for all assets available within **All Assets** and **Collections** to display the results to user groups.

For example, ALLOW access to user group with Group ID = 1011 when asset metadata matches "Brand = Brand X" AND "Region = EMEA OR Americas". Content Hub displays only those assets to the user group with ID = 1011 where ''Brand = Brand X'' and ''Region = EMEA or Americas''.

ABAC rules in Content Hub can be configured using the following approaches:

* **Self-serve configuration** using [AI Assistant in Content Hub](#configure-abac-using-ai-assistant-in-content-hub), powered by AEM Governance Agent  
* **Spreadsheet-based configuration** through [Adobe Support](#configure-abac-using-spreadsheet)

With AI Assistant in Content Hub, administrators can define and manage ABAC rules using metadata and natural language. This enables faster rule configuration and reduces dependency on manual support workflows.

Some of the key benefits of attribute-based access control include:

* Eliminates the dependency on folder structure for permissions
* Allows administrators to upload assets and retroactively determine permission structures
* Reduces the number of duplicates and improves asset integrity. Duplicates are needed in folder-based permissions when the same assets are shared with different groups.
* Enables granular, rule-based access
* Supports scalable governance across brands and regions
* Improves asset management

>[!VIDEO](https://video.tv.adobe.com/v/3475413/?learn=on&enablevpops){transcript=true}

## How to enable Attribute-based access control {#enable-attribute-based-access-control}

ABAC rules in Content Hub can be configured using the following approaches:

* **Self-serve configuration using AI Assistant in Content Hub (powered by AEM Governance Agent)**  
  Administrators can define and manage ABAC rules directly using natural language within Content Hub.

* **Spreadsheet-based configuration via Adobe Support**  
  Administrators can define ABAC rules in a spreadsheet and submit them through Adobe Support for configuration.

## Configure ABAC using AI Assistant in Content Hub

With AI Assistant in Content Hub, powered by AEM Governance Agent, you can create and manage ABAC rules directly in Content Hub using natural language.

You can:
* Search for existing rules
* Create rules
* Update rules
* Delete rules

This enables administrators to create and manage access rules without relying on support workflows.

### Before you begin {#before-you-begin-ai-assistant}

Ensure the following before using AI Assistant in Content Hub for ABAC rule configuration:

* You are licensed for AEM as a Cloud Service
* AI Assistant powered by AEM Governance Agent is available for your organization
* If you do not yet have access, contact your Adobe representative and complete the required licensing steps
* A GenAI rider is not required for the try-buy program

### Steps to configure ABAC rules using AI Assistant {#steps-ai-assistant}

1. Open AI Assistant in Content Hub.

1. Start with a simple instruction.

   For example:

   `Create a new rule in Content Hub`

   AI Assistant guides you on the information required to create the rule.

1. Define the rule in natural language.

   For example:

   `Frescopa Web Marketers user group should have access to assets where product equals Frescopa`

1. Select the environment where the ABAC rule must apply.

1. Review the rule before applying it.

   AI Assistant generates a structured preview of the rule. Nothing is applied automatically. You can review the generated rule, adjust it if needed, or cancel the action before applying it.

1. Save and apply the rule.

   Once saved, the rule is enforced dynamically based on metadata.

This review step helps ensure accuracy before the rule is applied.

### Manage ABAC rules using prompts {#manage-abac-rules-using-prompts}

After you start using AI Assistant, you can manage ABAC rules conversationally.

**Discover rules**

* Show all existing Content Hub ABAC rules

**Create rules**

* Create a rule that gives Product Marketing group access to all assets
* Give Sales group access to assets where region equals EMEA

**Update rules**

* Update rule for EMEA marketing group to include APAC

**Delete rules**

* Delete the rule for Product Marketing group

**Explore metadata and groups**

* Show available groups and metadata properties to set rules

## Configure ABAC using Spreadsheet

If AI Assistant is not enabled for your organization, you can configure ABAC rules using the spreadsheet-based workflow.

Click **Download Spreadsheet** to download and define rules in a spreadsheet. Create an Adobe Support ticket and provide the rules defined in the spreadsheet to Adobe.

[!BADGE Download Spreadsheet]{type=Informative url="https://helpx.adobe.com/content/dam/help/en/experience-manager/aem-assets/ABAC_Get_Started_Template.xlsx"}

Define rules in the spreadsheet using the guidelines described in this article.

>[!IMPORTANT]
>
>After defining the rules, navigate to the **Validation Errors** tab of the spreadsheet and click **Run ABAC Validations**. The **All validations passed** message confirms that you can provide the defined rules to Adobe.

### Steps to configure ABAC rules using Spreadsheet {#steps-spreadsheet}

1. Download the ABAC spreadsheet template.
1. Define rules in the spreadsheet using metadata-based conditions.
1. Map each rule to the appropriate IMS Group ID.
1. Capture the business intent of the rule in comments.
1. Submit an Adobe Support ticket and share the completed spreadsheet with Adobe.
1. Adobe configures the rules for your organization.

## Example Attribute-based access control use case {#example-metadata-based-rules}

To support a large-scale marketing rollout, various team members across regions and brands need access to digital assets. Each persona has a specific scope based on region and brand. ABAC enforces these rules automatically using asset metadata. The following table illustrates the personas for this use case and the rules that are applied:

| Persona | Role | Role Description | Group ID | ABAC Rule |
|---|---|---|---|---|
| John | EMEA Marketing Lead | Oversees marketing execution across all brands in EMEA. Needs access to approved assets for all brands intended for EMEA markets. | group-emea-marketing | region = "EMEA" |
| Mike | APAC Marketing Lead | Oversees marketing execution across all brands in APAC. Needs access to approved assets for all brands intended for APAC markets. | group-apac-marketing | region = "APAC" |
| Sophie | Brand X Manager (EMEA) | Manages Brand X identity in EMEA. Needs to see only Brand X approved content tailored to EMEA markets. | group-emea-brandx | region = "EMEA" && brand = "Brand X" |
| Tom | Brand Y Manager (APAC) | Manages Brand Y identity in APAC. Needs to see only Brand Y approved content tailored to APAC markets. | group-apac-brandy | region = "APAC" && brand = "Brand Y" |

Using these rules, Content Hub administrators have:

* **Granular, rule-based access**: Users see only the assets relevant to their region and brand without manual permission assignments.
* **Seamless global collaboration**: Regional and brand teams work in parallel without access conflicts.
* **Scalable and future-proof permissions**: As new regions or brands are added, rules can be updated based on metadata.

### Additional scenarios where ABAC is useful {#additional-scenarios-abac}

ABAC can also help address the following scenarios:

* **Global brand and regional access**: Teams see only assets relevant to their brand and market.
* **Agency and partner collaboration**: External agencies and partners can access only the campaign assets relevant to them.
* **Role-based access for different teams**: Teams such as marketing, sales, and legal can access assets relevant to their function.
* **Region-specific legal compliance**: Users can be restricted to assets approved for specific regulatory or regional requirements.

>[!IMPORTANT]
>
>By default, all other user groups that are not specified with any rules in the [spreadsheet](#configure-abac-spreadsheet) are denied access. If a user is not part of any group for which ABAC rules are defined, they cannot access any assets. If some users must have access to all assets, for example Admins, include a group with a Group ID in the spreadsheet and specify that the group requires access to all assets so Adobe can configure it accordingly.

## Supported rule constructs {#supported-rule-constructs}

* **Logical operators**:
  * AND: All conditions must be true
  * OR: At least one condition must be true

* **Comparison operators**:
  * Equals (=): Checks if a user or asset attribute matches a value
  * Not Equals (!=): Checks if a user or asset attribute does not match a value

When asset metadata fields contain arrays, for example multiple regions or tags, Equals refers to contains logic and Not Equals refers to does not contain logic.

This allows you to write simple and expressive rules, such as ALLOW if region = emea AND assetType != prototype AND tags != confidential.

## Guidelines {#guidelines-attribute-based-access-control}

The following guidelines apply to both AI Assistant-based and spreadsheet-based configuration:

* ABAC rules are applicable only for assets approved for Content Hub. For more information, see [Approve Assets for Content Hub](/help/assets/approve-assets-content-hub.md).
* Do not define DENY rules. Always convert DENY rules into ALLOW rules. For example, ALLOW if region = user-region DENY if assetType = prototype AND confidential = yes can be converted to ALLOW if region = user-region AND (assetType != prototype OR confidential != yes).
* ABAC rules are applied to user groups using the IMS Group ID, which is available in the Admin Console.
* You can set the [Approval Target](/help/assets/approve-assets-content-hub.md#set-approval-target) for assets using AEM as a Cloud Service author environment. ABAC rules are applied to assets approved with Approval Target = Content Hub, as Approval Target = Delivery is for assets available for Delivery + Content Hub. Assets marked as Approval Target = Delivery are visible to all in Content Hub.
* Ensure that the metadata schemas used in ABAC rules are correctly defined and available in AEM. Provide the full path of the metadata schema or schemas in AEM that define properties referenced in ABAC rules. You can optionally create a test folder with sample assets that match the ABAC conditions to help verify rule behavior and evaluate access accurately.
* Capture the business intent of the rule in comments, even if the condition is correctly written, because the intent helps validate and correct the logic if required.
* Ensure metadata values used for access rules, such as brand, region, and product, are maintained consistently across assets.
* Start with key use cases such as brand-based or region-based access.
* Use clear prompts when defining rules with AI Assistant. Describe the intent in business language so that AI Assistant can translate it into a structured rule.
* License PDF files that are set for DRM must remain visible to all users so they can review the license information when downloading the asset with license.

## Frequently asked questions {#faqs-attribute-based-access-control-content-hub}

### What is Attribute-based Access Control (ABAC) in AEM Assets Content Hub?

Attribute-based Access Control (ABAC) in AEM Assets Content Hub allows administrators to define metadata-based rules to control the level of access different user groups have to digital assets. Access is determined by whether the asset metadata matches the conditions specified in the rules, allowing for granular and dynamic management of asset visibility.

### How do administrators define access rules using ABAC in AEM Assets Content Hub?

Administrators define access rules by creating conditions based on asset metadata, such as brand or region, and linking these to specific user group IDs. These rules use logical and comparison operators to specify exactly which assets are visible to which user groups.

### What are the main benefits of using ABAC over traditional folder-based permissions in AEM Assets Content Hub?

ABAC eliminates the dependency on folder structures for permissions, allows administrators to upload assets and assign permissions retroactively, and reduces the number of duplicate assets needed. This improves asset integrity and simplifies permission management, especially when assets need to be shared with multiple groups.

### Can administrators set up ABAC rules directly in the AEM Assets Content Hub interface?

Administrators can configure ABAC rules using AI Assistant in Content Hub, if enabled for their organization. They can also continue to use the spreadsheet-based workflow through Adobe Support.

### What types of metadata conditions can be used while setting up ABAC rules in AEM Assets Content Hub?

ABAC rules in AEM Assets Content Hub can use logical operators such as AND and OR, and comparison operators such as equals and not equals. Metadata properties used in the rules must be correctly defined and available in the AEM metadata schemas, and can include fields such as region, brand, product, campaign, asset type, or publishing status.

### Why is AEM Assets Content Hub ABAC particularly useful for organizations with large teams and diverse asset needs?

ABAC is useful for organizations with large teams because it enables granular, rule-based access to assets based on user roles, regions, brands, or business needs. It ensures that users see only assets relevant to their responsibilities, without manual permission assignments or excessive duplication of assets.

### How should administrators prepare the ABAC spreadsheet for AEM Assets Content Hub before submitting it to Adobe Support?

Administrators should create user groups in the Adobe Admin Console, note their Group IDs, clearly define the permissions and conditions for each group in the spreadsheet, ensure all metadata properties are correctly mapped to the appropriate schemas, and use the comments column to clarify the business intent of each rule.