---
title: Configure Dropdown Options for Associate UI
description: Learn how to configure Options Binding or manual static options for dropdown fields in the Interactive Communication Editor so choices render correctly in the Associate UI.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms."
exl-id: configure-dropdown-options-associate-ui
---

# Configure Dropdown Options for Associate UI

Dropdown fields in the Interactive Communication Editor use a focused **Options Binding** model for dynamic, data-driven choices in the Associate UI. **Data Binding** is no longer supported for dropdown fields — authors configure either **Bind from Data** (bound data source) or manual static options in the **Properties** panel.

| Who | Benefit |
|-----|---------|
| **Author (interactive communication designer)** | Deliver accurate, data-driven dropdown choices to associates without unsupported Data Binding configurations. |
| **Associate (service representative)** | See the correct option list and pre-selected value when completing customer communications in the Associate UI. |

## Before you begin

Enable **Associate View** on the interactive communication before configuring dropdown behaviour for the Associate UI. See [Associate UI in Interactive Communication Editor](/help/forms/interactive-communication/associate-ui-in-interactive-communication-editor.md).

Associates must be members of the **forms-associates** group.

## Bind from Data enabled (dynamic options)

When **Options Source** is set to **Bind from Data**:

- Dropdown options are driven entirely by the bound data source configured in **Options Ref**.
- Options are rendered and available for selection in the Associate UI.
- **Default Value** is not available — the first value from the bound options is automatically pre-selected when the form is presented to the associate.

## Manual options (static options)

When **Options Source** is not set to **Bind from Data**:

- Authors add options manually through the **Properties** panel.
- **Default Value** remains available — the form designer can explicitly select which option appears as the pre-selected value in the Associate UI.

## Configure dropdown options

1. Open the interactive communication in the Interactive Communication Editor.

1. On the **Design** tab, select the **Drop Down** component on the design canvas.

1. Open the **Properties** panel.

1. Configure the dropdown for the Associate UI:

   - Set **Caption** to the label associates see in the left-hand data entry panel. For example, enter **Installment month**.
   - Under **Options Source**, choose **Bind from Data** to populate options from your data model, or add manual options for a static list.
   - If you selected **Bind from Data**, set **Options Ref** to the data path that supplies the option list. For example, bind to `$.GMFletter.installmentDetails.installmentMonth`.

   Do not configure **Data Binding** on dropdown fields — use **Bind from Data** or manual options only.

   ![Configure dropdown options binding](/help/forms/interactive-communication/assets/associate-ui-configure-drop-down1.png)

1. Turn on **Allow Editing By Associate** so associates can select a value in the Associate UI.

1. Optionally configure **Tooltip** and **Validations** under **Associate Properties**.

1. If using manual options, set **Default Value** as needed.

1. Click **Save** and publish the interactive communication.

## Verify in Associate UI

1. Open the interactive communication in the **Associate View**.

1. Confirm the dropdown appears in the left-hand data entry panel with the caption you configured. For example, **Installment month** shows the bound options such as **June 2026**, **July 2026**, and **August 2026**.

1. Verify that the first bound option is pre-selected when the Associate UI loads.

1. Select a different option and confirm the value updates in the right-hand preview. For example, selecting **June 2026** updates the document text to **Installment month June 2026**.

   ![Verify dropdown options in Associate UI](/help/forms/interactive-communication/assets/associate-ui-configure-drop-down2.png)

## Considerations

- **Data Binding is not supported** for dropdown fields. Use **Bind from Data** for dynamic lists or manual options for static lists.
- With **Bind from Data** enabled, associates cannot set a custom default — the first bound option is always pre-selected.
- With manual options, test the **Default Value** in the Associate UI preview to confirm the expected option appears before publishing.
- **Allow Editing By Associate** must be enabled for the dropdown to appear as an editable field on the left-hand side of the Associate UI.

## Frequently asked questions

**Why is Default Value unavailable for my dropdown?**
**Default Value** is disabled when **Options Source** is set to **Bind from Data**. The first value from the bound data source is pre-selected automatically in the Associate UI.

**Can I use Data Binding and Options Binding together on a dropdown?**
No. Dropdown fields support **Bind from Data** or manual options only. **Data Binding** is not supported for dropdown fields.

**What is Options Ref?**
**Options Ref** is the data reference path that supplies the list of choices when **Options Source** is set to **Bind from Data**. Select the path that points to the collection of option values in your Form Data Model.

**How do I verify dropdown options before associates use the interactive communication?**
Publish the interactive communication and open the Associate UI preview. Confirm that bound or manual options appear in the left-hand data entry panel and that the pre-selected value matches your configuration.

## See also

- [Associate UI in Interactive Communication Editor](/help/forms/interactive-communication/associate-ui-in-interactive-communication-editor.md)
- [Configure Bound and Unbound Variables for Associate UI](/help/forms/interactive-communication/associateui/configure-bound-unbound-variables-associate-ui.md)
- [Create an Interactive Communication](/help/forms/interactive-communication/create-interactive-communication.md)
