---
title: Attribute-based access control
description: Learn how to enable Attribute-based access control to define metadata-based rules to define the level of access to assets available in Content Hub
role: Admin
exl-id: 05f54b05-40b8-4a6c-af8f-5c3f7a2089d4
---
# Attribute-based access control {#attribute-based-access-control}

Attribute-based access control (ABAC) allows Content Hub Administrators to define metadata-based rules to define the level of access to assets available in Content Hub.

Administrators for an organization define rules for user groups, which are mapped to a Group ID. Rules are a mix of [logical and comparison operators](#supported-rule-constructs) and Admins can define as many rules as they need to manage asset access within Content Hub.

The rules are based on metadata and if the conditions defined in the rule match the asset metadata, the asset gets displayed to the user group. Content Hub scans the asset metadata including the custom metadata for all assets available within **All Assets** and **Collections** to display the results to user groups.

For example, ALLOW access to user group with Group ID = 1011, when asset metadata matches "Brand = Brand X" AND "Region = EMEA OR Americas". Content Hub displays only those assets to the user group with ID = 1011 where Brand = `Brand X` and Region = `EMEA` or `Americas`.

Some of the key benefits of attribute-based access control include:

* Eliminates the dependency on folder structure for permissions

* Allows administrators to upload assets and retroactively determine permission structures

* Reduces number of duplicates - improves asset integrity. Duplicates are needed in folder based permissions when same assets are shared with different groups.

>[!VIDEO](https://video.tv.adobe.com/v/3475413/?learn=on&enablevpops){transcript=true}

## How to enable Attribute-based access control? {#enable-attribute-based-access-control}

As of now, you cannot create Attribute-based access control rules on your own using the Content Hub User Interface.

Click **Download Spreadsheet** to download and define rules in a spreadsheet. Create an Adobe support ticket and provide the rules defined in the spreadsheet to Adobe.

[!BADGE Download Spreadsheet]{type=Informative url="https://helpx.adobe.com/content/dam/help/en/experience-manager/aem-assets/ABAC_Get_Started_Template.xlsx"}


Define rules in the spreadsheet using the guidelines defined in this article.

<!--

>[!IMPORTANT]
>
> After defining the rules, navigate to the **Validation Errors** tab of the spreadsheet and click **Run ABAC Validations**. **All validations passed** message confirms that you can provide the defined rules to Adobe.

-->

## Example Attribute-based Access Control use case {#example-metadata-based-rules}

To support a large-scale marketing rollout, various team members across regions and brands need access to digital assets. Each persona has a specific scope based on region and brand. ABAC enforces these rules automatically via asset metadata. The following table illustrates the different type of personas for this use case and the rules that are applied:

| Persona      | Role   | Role Description | Group ID | ABAC Rule |
|---------------------|----------------|-----------------|------------|------------|
| John  | EMEA Marketing Lead | Oversees marketing execution across all brands in EMEA. Needs access to approved assets for all brands intended for EMEA markets. | group-emea-marketing | region = "EMEA" |
| Mike  | APAC Marketing Lead | Oversees marketing execution across all brands in APAC. Needs access to approved assets for all brands intended for APAC markets. | group-apac-marketing | region = "APAC" |
| Sophie  | Brand X Manager (EMEA) | Manages Brand X identity in EMEA. Needs to see only Brand X approved content tailored to EMEA markets. | group-emea-brandx | region = "EMEA" && brand = "Brand X" |
| Tom  | Brand Y Manager (APAC) | Manages Brand Y identity in APAC. Needs to see only Brand Y approved content tailored to APAC markets. | group-apac-brandy | region = "APAC" && brand = "Brand Y" |

Using these rules, Content Hub administrators have:

* **Granular, rule-based access**: Users see only the assets relevant to their region and brand — no manual permission assignments.

* **Seamless global collaboration**: Regional and brand teams worked in parallel without access conflicts.

* **Scalable and future-proof permissions**: As new regions or brands are added, rules can be updated based on metadata.

>[!IMPORTANT]
>
> By default, all other user groups, which are not specified with any rules in the [spreadsheet](#enable-attribute-based-access-control), are denied access. If a user is not part of any group for which ABAC rules are defined, they are not able to access any assets. If you need to have some users to have access to all assets (for example, Admins), a group with a group ID must be mentioned in the spreadsheet with the details that this particular group needs access to all assets and Adobe will configure it for you.


## Supported rule constructs {#supported-rule-constructs}

* **Logical operators**:
  * AND: All conditions must be true
  * OR: At least one condition must be true
* **Comparison operators**:
  * Equals (=): Checks if a user or asset attribute matches a value
  * Not Equals (!=): Checks if a user or asset attribute does not match a value

When asset metadata fields contain arrays (for example, multiple regions or tags), `Equals` refers to `contains` logic and `Not Equals` refers to `does not contain` logic.

This allows you to write simple and expressive rules, such as: ALLOW if region = emea AND assetType != prototype AND tags != confidential.

## Guidelines {#guidelines-attribute-based-access-control}

* ABAC rules are applicable only for assets approved for Content Hub. For more information, see [Approve Assets for Content Hub](/help/assets/approve-assets-content-hub.md).

* Do not give DENY rules, instead always convert DENY to ALLOW rule. For example, `ALLOW if region = <user-region> DENY if assetType = prototype AND confidential = yes` can be converted to `ALLOW if region = <user-region> AND (assetType != prototype OR confidential != yes)`.

* ABAC rules are applied to user groups using the IMS Group ID, which is available in the Admin Console.


* You can set the [Approval Target](/help/assets/approve-assets-content-hub.md#set-approval-target) for assets using AEM as a Cloud Service author environment. ABAC rules are applied to assets approved with Approval Target = `Content Hub`, as Approval Target = `Delivery` is for assets available for `Delivery` + `Content Hub`. Assets marked as Approval Target = `Delivery` are visible to all in Content hub.

* Ensure that the metadata schemas used in ABAC rules are correctly defined and available in AEM. Provide full path of the metadata schema(s) in AEM that define properties referenced in ABAC rules. You can optionally create a test folder with a few sample assets with metadata values that match the ABAC conditions. This helps in verifying rule behaviour and evaluating access accurately.

* Capture the business intent of the rule in comment, regardless of whether the condition is correctly written, as the intent helps us validate and correct the logic, if required.

* The license PDF files, which are set for DRM need to be visible to all, so that users are able to see them when they are downloading the asset with license.
