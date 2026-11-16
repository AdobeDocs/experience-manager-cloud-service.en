---
title: Signature Field Component in Interactive Communication Editor
description: Learn how to add a Signature Field in Interactive Communication Editor, lock fields after signing, and manage Collections for selective locking in AEM Forms.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: 5e7d26f6-4305-45b0-bcd9-826ef9393d7f
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---
# Signature Field Component in Interactive Communication Editor

## 1. Overview of Signature Field

The Signature Field component adds a digital signature placeholder to a form, and lets you lock some or all fields as read-only once that signature is applied, protecting data integrity after signing. At design time, the field renders as a static, non-interactive box with a caption in the Interactive Communication (IC) editor. It does not capture a live signature inside the editor. The actual e-signing happens later, when the generated PDF is opened and signed in Adobe Acrobat (or another compatible e-sign client), outside the IC editor. To sign the field, the generated PDF must be an interactive PDF; signature fields can't be signed in a flattened or non-interactive PDF output.

Beyond placing the signature placeholder itself, the component's **Lock fields after document signing** setting lets you protect data integrity once a document is signed, for example on an approval form, an internal sign-off form, or a vendor agreement. You can lock every field in the document, or selectively lock only the fields that belong to (or are excluded from) a named **Collection** that you define and manage directly from the component's properties panel.

>[!NOTE]
>This component requires the companion Collection support shipped alongside it to work end-to-end. Confirm your AEM Forms as a Cloud Service release includes the required platform updates before relying on selective (Collection-based) locking in production. Without those updates, Collection-locked fields can render as plain text, or Acrobat can report a field-locking error, when you sign the generated PDF.

## 2. Properties

These properties are grouped by tab in the signature field's properties panel.

### 2.1 Basic Field

The **Basic Field** tab controls the field's identity and caption.

- **Name:** A unique identifier used for referencing the signature field in data models, rules, or scripts.
- **Caption:** The descriptive label displayed next to the signature placeholder (for example, "Signature of the Consumer"). Unlike a text field, the caption is a static label and can't be edited at runtime.
- **Reserve:** The space reserved for the caption, with an alignment option (**Left**, **Right**, **Top**, or **Bottom**) relative to the signature box.

### 2.2 Lock Fields After Signing

This is where you configure which fields become read-only once the document is signed.

- **Lock fields after document signing:** When enabled, reveals a **Lock type** option that determines which fields in the document become read-only once this signature is applied.
- **Lock type:**
  - **All Fields in Document**: locks every field on the form after signing.
  - **A named Collection** (listed as **Collection - *name***): locks only the fields associated with that Collection. Selecting a Collection reveals two radio options:
    - **All Fields in Collection**: locks only the fields included in the Collection.
    - **All Fields not in Collection**: locks every field *except* the ones in the Collection.
  - **`<<New/Manage Collection...>>`**: a special option that opens the **Collection List** dialog instead of setting a lock type, so you can create or edit Collections without leaving the signature field's properties.

### 2.3 Styling and Accessibility

These sections behave the same way as on other IC components:

- **Typography:** Font family, size, weight, and color for the caption text.
- **Position:** X and Y coordinates, height, and width of the signature placeholder within the layout.
- **Margin:** Top, bottom, left, and right spacing around the component.
- **Appearance:** Fill, stroke, stroke width, style, and corner (edge) styling of the placeholder box.
- **Presence:** Whether the field is **Visible** or **Hidden (keeps space)** at runtime.
- **Accessibility:** Screen-reader text and tab-order settings for the field.

## 3. Managing Collections

A Collection is a named, reusable group of fields that you can reference from one or more signature fields' **Lock type** setting. Collections are created and managed from the **Collection List** dialog, opened via the signature field's **`<<New/Manage Collection...>>`** option.

### 3.1 Collection List dialog

Lists every Collection defined in the document, with these actions:

- **New**: opens the Collection Editor to create a Collection.
- **Duplicate**: copies the selected Collection.
- **Delete**: removes the selected Collection. Any signature field that referenced it falls back to no lock type for that reference.
- **Move Up / Move Down**: reorders Collections in the list.
- **Modify...**: opens the Collection Editor to edit the selected Collection.
- **Close**: closes the dialog.

### 3.2 Collection Editor dialog

Use this dialog to name a Collection and choose which fields it contains.

- **Name:** A unique name for the Collection.
- **Collection Type:** Fixed to **Signature**. Collections referenced by a signature field's lock setting are always this type.
- **Field tree:** A checkbox tree of every field in the form's hierarchy. Check the fields that should belong to the Collection.
- **Hide unsupported nodes:** When checked (the default), hides container/structural nodes that can't be added to a Collection, leaving only selectable fields.
- **Form Object Resolve Status:** Automatically checks whether each field reference in the Collection can still be found in the form's current field structure, and flags any reference that no longer resolves, for example after a field was renamed, moved, or deleted.
- **OK** is disabled until the Collection has a name.

## 4. Usage: a synthetic approval form example

### Which fields stay editable after signing?

Which fields remain editable after signing depends entirely on how you configure **Lock type**. Consider a simple approval form with four fields: **Name**, **Age**, **Date**, and a **Signature Field** captioned "Signature of the Consumer". After laying out the fields, you can configure the signature field's lock behavior in one of three ways:

- **Lock all fields:** Set **Lock fields after document signing** > **Lock type** to **All Fields in Document**. After the form is filled in and signed in Acrobat, **Name**, **Age**, and **Date** all become read-only, alongside the signature itself.
- **Lock only specific fields (include):** Create a Collection (for example, `ApprovalLock`) containing just the **Name** field, set **Lock type** to that Collection, and choose **All Fields in Collection**. After signing, only **Name** becomes read-only, **Age** and **Date** remain editable.
- **Lock everything except specific fields (exclude):** Using the same Collection, choose **All Fields not in Collection** instead. After signing, every field *except* **Name** becomes read-only.

In every case, the signature placeholder itself renders as an empty bordered box in the IC editor canvas. It has no design-time preview value. The actual signing step happens after you generate the PDF: open it in Adobe Acrobat, use **Sign** (or **Fill & Sign**) to apply a digital signature to the signature field, and Acrobat then applies the lock behavior you configured, making the appropriate fields read-only in the signed document.

## 5. Best Practices

- Use a descriptive **Caption** so signers understand what they're signing (for example, "Signature of the Consumer" rather than a generic label).
- Prefer Collection-based (selective) locking over **All Fields in Document** when only part of the form represents what the signature is attesting to. This avoids unnecessarily locking unrelated fields (such as internal notes or later workflow steps).
- Give Collections clear, purpose-based names (for example, `ApprovalLock`) so their intent is obvious when reused across multiple signature fields.
- Run **Form Object Resolve Status** in the Collection Editor after restructuring a form (adding, removing, or moving subforms) to catch any field references that no longer resolve.
- Verify the signed-document behavior by generating a PDF and performing an actual signing pass in Acrobat. Selectively locked fields only behave correctly end-to-end when the required companion platform updates are present.

In short: use **Lock Fields After Signing** with a named **Collection** whenever only part of a form needs to become read-only after the signature is applied, and use **All Fields in Document** when the entire form should lock.

## Frequently Asked Questions: Signature Field

**Can I edit a field after signing?**

It depends on the signature field's **Lock type** setting in AEM Forms. If **Lock type** is set to **All Fields in Document**, every field on the form becomes read-only after signing. If it's set to a named **Collection** with **All Fields in Collection**, only the fields in that Collection become read-only and the rest stay editable. With **All Fields not in Collection**, every field except those in the Collection becomes read-only.

**Where does the signing happen?**

Signing happens outside the Interactive Communication (IC) editor, in Adobe Acrobat (or another compatible e-sign client). The IC editor only places a static digital signature placeholder on the form at design time; it does not capture a live signature. After you generate the PDF, you open it in Acrobat and use **Sign** (or **Fill & Sign**) to apply the signature, which is when AEM Forms applies the field-locking behavior you configured.

**Can I lock only some fields?**

Yes. Create a named **Collection** containing only the fields you want to govern, set the signature field's **Lock type** to that Collection, and choose **All Fields in Collection** to lock just those fields, or **All Fields not in Collection** to lock everything except them. This lets an AEM Forms signature field protect specific data, such as an approved amount or an approver's name, without locking the whole form.

**What if I delete a used Collection?**

The signature field falls back to no lock type for that reference. Deleting a Collection from the **Collection List** dialog does not delete the signature field itself, but any signature field that pointed to the deleted Collection no longer locks fields on signing until you assign it a new **Lock type**.

## See also

- [Configure Data Binding in Interactive Communication Editor](/help/forms/interactive-communication/configure-data-binding.md)
- [Use the Rule Editor in Interactive Communication Editor](/help/forms/interactive-communication/use-the-rule-editor.md)
- [Generate PDF Preview in Interactive Communication Editor](/help/forms/interactive-communication/generate-pdf-preview.md)
