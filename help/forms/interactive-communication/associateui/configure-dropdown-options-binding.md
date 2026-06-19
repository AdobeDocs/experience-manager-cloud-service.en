---
title: Configure Dropdown Options for Associate UI
description: Learn how to configure Options Binding or manual static options for dropdown fields in the Interactive Communication Editor so choices render correctly in the Associate UI.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: configure-dropdown-options-associate-ui
---

# Configure Dropdown Options for Associate UI

Dropdown fields in the Interactive Communication Editor use a focused **Options Binding** model for dynamic, data-driven choices in the Associate UI. **Data Binding** is no longer supported for dropdown fields — authors configure either **Options Binding** (bound data source) or manual static options in the **Properties** panel.

| Who | Benefit |
|-----|---------|
| **Author (interactive communication designer)** | Deliver accurate, data-driven dropdown choices to associates without unsupported Data Binding configurations. |
| **Associate (agent / service representative)** | See the correct option list and pre-selected value when completing customer communications in the Associate UI. |

## Before you begin

Enable **Associate View** on the interactive communication before configuring dropdown behaviour for the Associate UI. See [Associate UI in Interactive Communication Editor](/help/forms/interactive-communication/associate-ui-in-interactive-communication-editor.md).

Associates must be members of the **forms-associates** group.

## Options Binding enabled (dynamic options)

When **Options Binding** is enabled:

- Dropdown options are driven entirely by the bound data source.
- Options are rendered and available for selection in the Associate UI.
- **Default Value** is not available — the first value from the bound options is automatically pre-selected when the form is presented to the associate.

## Options Binding disabled (manual options)

When **Options Binding** is not enabled:

- Authors add options manually through the **Properties** panel.
- **Default Value** remains available — the form designer can explicitly select which option appears as the pre-selected value in the Associate UI.

## Configure dropdown options

1. Open the interactive communication in the Interactive Communication Editor.

1. Select the **Dropdown** component on the design canvas.

1. Open the **Properties** panel.

1. Choose whether to enable **Options Binding** and bind to your data source, or add manual options.

   Do not configure **Data Binding** on dropdown fields — use **Options Binding** or manual options only.

1. If using manual options, set **Default Value** as needed.

1. Click **Save**, publish the interactive communication, and verify option behaviour in the Associate UI preview.

## Considerations

- **Data Binding is not supported** for dropdown fields. Use **Options Binding** for dynamic lists or manual options for static lists.
- With **Options Binding** enabled, associates cannot set a custom default — the first bound option is always pre-selected.
- With manual options, test the **Default Value** in the Associate UI preview to confirm the expected option appears before publishing.

## Frequently asked questions

**Why is Default Value unavailable for my dropdown?**
**Default Value** is disabled when **Options Binding** is enabled. The first value from the bound data source is pre-selected automatically in the Associate UI.

**Can I use Data Binding and Options Binding together on a dropdown?**
No. Dropdown fields support **Options Binding** or manual options only. **Data Binding** is not supported for dropdown fields.

**How do I verify dropdown options before associates use the interactive communication?**
Publish the interactive communication and open the Associate UI preview. Confirm that bound or manual options appear in the left-hand data entry panel and that the pre-selected value matches your configuration.

## See also

- [Associate UI in Interactive Communication Editor](/help/forms/interactive-communication/associate-ui-in-interactive-communication-editor.md)
- [Configure Bound and Unbound Variables for Associate UI](/help/forms/interactive-communication/associateui/configure-bound-unbound-variables-associate-ui.md)
- [Create an Interactive Communication](/help/forms/interactive-communication/create-interactive-communication.md)
