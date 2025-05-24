---
title: How to send an adaptive form for review?
description: Share an Adaptive Form for review with one or more reviewers.
uuid: 58c8c8fb-9262-4c37-b9b2-e46fe21b77d9
products: SG_EXPERIENCEMANAGER/6.5/FORMS
topic-tags: author
discoiquuid: 71d1aa10-d191-49bc-a50f-1098324f1cfe
feature: Adaptive Forms
role: User, Developer
hide: yes
hidefromtoc: yes
exl-id: 27c52969-1213-4fd3-8e16-988caafb4ad6
---
# Associating submission reviewers with a form {#associating-submission-reviewers-with-a-form}

When you create a form, you can specify users who review the submissions of the form via forms portal and provide feedback. Your organization can collect feedback and rework on the submitted forms.

[!DNL AEM Forms] lets you associate a reviewer group with a form. Users added to a review group of a form see submissions of this form, and provide feedback.

Reviewer groups assigned to a form can only review the submissions of the specified form.

## Prerequisite {#prerequisite}

### Enabling submission reviewer groups property for Adaptive Forms using metadata schema editor {#enabling-submission-reviewer-groups-property-for-adaptive-forms-using-metadata-schema-editor}

To associate a reviewer group with a form, edit the metadata schema of Adaptive Forms. By default, you cannot add a reviewer group to a submitted form.

To edit metadata schema:

1. In the author mode, under Experience Manager, click **Tools** &gt; **Assets** &gt; **Metadata Schemas**.
1. In the Schema Forms page, navigate to **Forms** &gt; **Forms Authored in AEM.**

   The URL of the page is:

   ```html
   https://<hostname>:<port>/mnt/overlay/dam/gui/content/metadataschemaeditor/
    schemalist.html/forms/aem-authored
   ```

1. Select **Adaptive Form** and click **Edit**.
1. In the Edit Form page, click **Advanced**.
1. In the Advanced tab, drag-and-drop the **Single Line Text** component available under Build Form.
1. Select the added text component to see its settings.

   Under Settings, enter `./jcr:content/metadata/form-submission-reviewer-group` in the Map to Property field.

   The submission reviewer group field in the Advanced properties of your Adaptive Form is enabled with the name you specify under Field Label.

## Associating submission reviewers with a form {#associating-submission-reviewers-with-a-form-1}

To associate submission reviewers with an Adaptive Form, create a reviewer group and add users to it. Add the created reviewer group under the form submission reviewer field in the advanced properties of the form.
User groups let you associate different sets of submission reviewers with different Adaptive Forms. This feature prevents a submission review from an unauthorized user.

Before you perform the following steps, see [Prerequisite](adding-reviewers-form.md#prerequisite).

To create a group and add members to it, navigate to **Tools** &gt; **Operations** &gt; **Security** &gt; **Groups**.
For more information, see [User Administration and Services](https://experienceleague.adobe.com/docs/experience-manager-65/administering/security/security.html).
Ensure that you add the group you create as a member of the out-of-the-box user group: **forms-submission-reviewers**. This user group is shipped with [!DNL AEM Forms], and it ensures that users are added as submission reviewers.

To associate user groups with an Adaptive Form:

1. In the authoring mode, navigate to **Forms** &gt; **Forms & Documents**.
1. Use the **Select **option to select an Adaptive Form, and click **View Properties**.
1. In the Properties window of the form, click **Edit**, and then click **ADVANCED**.
1. Enter the group in the submission reviewer group field, and click **Done**.

   The submission reviewer group field appears with the name you specified in the edited metadata schema of Adaptive Forms.

>[!NOTE]
>
>Replicate users and forms to ensure availability of the users and forms in the remote implementation of [!DNL AEM Forms].
>
>Ensure that all users are replicated as reviewing members of the user groups in the remote implementation.

>[!MORELIKETHIS]
>
>* [Creating and managing reviews to forms](/help/forms/create-reviews-forms.md)
>* [Create and manage reviews for an Adaptive Form](/help/forms/review-adaptiveforms-in-sites-page.md)
