---
title: How do I reuse the metadata properties of an adaptive form?
description: Discover to efficiently repurpose an existing Adaptive Form to create new one.
seo-description: You can reuse an existing Adaptive Form to create new Adaptive Forms.
feature: Adaptive Forms, Foundation Components
exl-id: fb8cf3a9-fd19-46bf-b40e-2af76ca68b9f
role: User, Developer
---
# Reuse metadata properties of an Adaptive Form {#reusing-adaptive-forms}

>[!NOTE]
>
> Adobe recommends using the modern and extensible data capture [Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html) for [creating new Adaptive Forms](/help/forms/creating-adaptive-form-core-components.md) or [adding Adaptive Forms to AEM Sites pages](/help/forms/create-or-add-an-adaptive-form-to-aem-sites-page.md). These components represent a significant advancement in Adaptive Forms creation, ensuring impressive user experiences. This article describes older approach to author Adaptive Forms using foundation components.


| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/reusing-adaptive-forms.html)                  |
| AEM as a Cloud Service     | This article         |

If you want to use some of the properties of an existing Adaptive Form to generate a new one, you can simply use the copy-paste functionality. In addition, you can paste the new Adaptive Form at the desired folder path. All metadata properties are replicated and the XFA and XSDs for XFA- and XSD-based Adaptive Forms are also copied.

>[!NOTE]
>
>The status and the review details are not copied. For example, if your Adaptive Form is published and then if you copy it, the pasted Adaptive Form is in unpublished state. Similarly, if a copied asset is under review, the pasted asset is not under the same review.

## Copy an Adaptive Form {#copy-an-adaptive-form}

Copy an Adaptive Form using either of the following approaches:

1. Click copy ![aem6forms_copy](assets/aem6forms_copy.png) icon from Quick actions.

   >[!NOTE]
   >
   >Quick actions are the action items that get displayed over a thumbnail on mouse hover.

1. Select the Adaptive Form. The selection process is different for different views.

   If you are in card view, go to selection mode by clicking the selection ![aem6forms_check-circle](assets/aem6forms_check-circle.png) icon and click all the Adaptive Forms that you want to copy.

   If you are in list view, click the check boxes of all Adaptive Forms to select them.

   >[!NOTE]
   >
   >All selected assets must be Adaptive Forms because copy-paste functionality is supported only for Adaptive Forms, and all assets that are selected must be present in the same folder.

   After selecting the assets, click the copy ![aem6forms_copy](assets/aem6forms_copy.png) icon present in the toolbar to copy the selected Adaptive Form.

## Paste an Adaptive Form {#paste-an-adaptive-form}

Clicking the copy action automatically exits the selection mode and makes the paste ![Paste](assets/Smock_Paste_18_N.svg) icon visible. Now go to the desired folder path and click the paste ![Paste](assets/Smock_Paste_18_N.svg) icon to paste the copied Adaptive Form.

If you are pasting in the same folder or another file with the same node name (with which it is stored in the CRX repository) exists in this target folder, 1 is appended to the suffix (for example, myaf becomes myaf1 and if myaf1 exists at the same location, myaf becomes myaf2. All other properties remain same as the original Adaptive Form.

After clicking the paste ![Paste](assets/Smock_Paste_18_N.svg) icon, it will again become hidden. At one time, you can only paste once. To again create a copy of same asset, copy it again.

## Change contents of new Adaptive Form {#change-contents-of-new-adaptive-form}

The content of a pasted Adaptive Forms can be changed using the following approaches to make it different from the copied form:

1. **Change metadata properties:**

   You can change the metadata properties of the Adaptive Form for example, title and description. For more details about metadata properties and how they can be changed, see [Managing Form Metadata](manage-form-metadata.md)

1. **Change XFA/XSD for XFA/XSD-based Adaptive Forms:**

   You can change the XFA/XSD used in Adaptive Forms. To know how these Adaptive Forms can be changed, see [Managing form metadata](manage-form-metadata.md)

1. **Republish:**

   The pasted asset is different from the copied one. You can publish it as a new asset to make it available for end users. To know how to publish an asset, <!-- see [Publishing and unpublishing forms](publishing-unpublishing-forms.md) -->


## See Also {#see-also}

{{see-also}}