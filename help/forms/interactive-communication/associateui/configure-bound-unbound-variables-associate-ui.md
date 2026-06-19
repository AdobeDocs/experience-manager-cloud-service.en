---
title: Configure Bound and Unbound Variables for Associate UI
description: Learn how to configure bound and unbound variables for the Associate UI so associates can edit fields on the left-hand side and values propagate correctly to the right-hand preview canvas.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: configure-bound-unbound-variables-associate-ui
---

# Configure Bound and Unbound Variables for Associate UI

Authors configure how bound variables and unbound variables appear and behave in the Associate UI (Agent UI) — including which fields associates can edit on the left-hand side (LHS) and how values propagate to the right-hand side (RHS) preview canvas. Correct configuration avoids duplicate entry, blank RHS fields, and conflicting associate-editing settings with **Text Box** components.

| Who | Benefit |
|-----|---------|
| **Author (interactive communication designer)** | Control which variables associates edit once on the LHS and how values flow to the RHS preview. |
| **Associate (agent / service representative)** | Enter data once and see it reflected consistently across the document preview. |

## Before you begin

Enable **Associate View** on the interactive communication. See [Associate UI in Interactive Communication Editor](/help/forms/interactive-communication/associate-ui-in-interactive-communication-editor.md).

Associates must be members of the **forms-associates** group.

## Mutual exclusivity — associate editing toggles

Associate editing for a **Text Box** and associate editing for bound or unbound variables are mutually exclusive:

- Enabling associate editing on a bound or unbound variable automatically disables associate editing on **Text Box** components (and vice versa).
- Plan your Associate UI data-entry model around variables or text boxes — not both with associate editing enabled.

## Blank unbound variables on the RHS

An unbound variable with associate editing disabled and no default value appears as a blank field on the RHS of the Associate UI.

- Only unbound variables with a default value display that value on the RHS.
- To show content on the RHS without associate entry, set a default value in the Interactive Communication Editor.

## Duplicate variable names (bound and unbound)

When bound and unbound variables share the same variable name:

- Only one instance appears on the LHS of the Associate UI.
- Only variables for which associate editing is enabled are edited on the RHS.
- The associate enters the value once on the LHS; it propagates automatically to all corresponding occurrences on the RHS canvas.

## Configure variables for Associate UI

1. Open the interactive communication in the Interactive Communication Editor and enable **Associate View**.

1. Select each bound or unbound variable and configure associate editing, default values, and data reference paths as needed.

1. Verify that **Text Box** associate editing is disabled if variable associate editing is enabled (or the reverse).

1. Click **Save**, publish the interactive communication, and test in the Associate UI.

1. Confirm LHS fields, RHS preview, and value propagation for duplicate variable names behave as expected.

## Considerations

**Unbound variables with the same name but different default values**

When multiple unbound variables share a variable name but use different default values, the Associate UI displays the default value of the first variable for which associate editing is enabled on the LHS.

**Bound variables with the same name but different data reference paths**

When multiple bound variables share a variable name but use different data reference paths, the LHS displays the value of the first variable for which associate editing is enabled. Any value entered or updated by the associate on the LHS propagates to all variables with that name, regardless of their data reference paths.

## Frequently asked questions

**Why does my unbound variable appear blank on the RHS preview?**
The variable likely has associate editing disabled and no default value. Set a default value in the Interactive Communication Editor to display content on the RHS without requiring associate entry.

**Why can I not enable associate editing on both a Text Box and a variable?**
Associate editing on **Text Box** components and on bound or unbound variables is mutually exclusive. Choose one data-entry model for the Associate UI.

**What happens when two variables share the same name?**
Only one field appears on the LHS. The associate enters the value once, and it propagates to all matching occurrences on the RHS canvas.

## See also

- [Associate UI in Interactive Communication Editor](/help/forms/interactive-communication/associate-ui-in-interactive-communication-editor.md)
- [Configure Dropdown Options for Associate UI](/help/forms/interactive-communication/associateui/configure-dropdown-options-binding.md)
- [Enable and configure Associate UI for Interactive Communications](/help/forms/interactive-communication/enable-configure-associate-ui.md)
