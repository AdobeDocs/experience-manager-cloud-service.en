---
title: Mask Numeric Values
description: Learn how to mask numeric values in the Interactive Communication Editor with predefined or custom display patterns and verify the masked canvas output.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms."
hide: true
---

# Mask numeric values {#mask-numeric-values}

Use numeric display patterns to mask values in the Interactive Communication Editor in Adobe Experience Manager (AEM) Forms. You can leave selected trailing digits visible or use a custom pattern to mask all significant digits. Display masking changes the presentation, not the underlying value.

For example, use masked presentation for credit card details instead of displaying the complete number on the canvas.

## Prerequisites

Before you begin, make sure you have:

* Access to an Interactive Communication Editor build that includes numeric masking.
* An Interactive Communication containing a [Numeric Field component](/help/forms/interactive-communication/numeric-field.md).
* A synthetic numeric value in the field, entered through its **[!UICONTROL Value]** property or supplied through data binding.

Use synthetic test data rather than real credit card details.

## Apply the masking pattern

Choose the predefined pattern for its default masked presentation, or use a custom pattern to control which digit positions remain visible.

### Select the predefined pattern

Use the predefined option to apply a masking pattern without entering a picture clause.

1. Select the Numeric Field on the design canvas.
1. Open **[!UICONTROL Properties]**.
1. In **[!UICONTROL Display type]**, select **[!UICONTROL \*\*\*\* 1234]**.
1. Check the masked value on the canvas.

### Enter a custom pattern

Use a custom numeric picture clause to leave selected trailing digits visible or mask all significant digits.

1. Select the Numeric Field on the design canvas.
1. Open **[!UICONTROL Properties]**.
1. In **[!UICONTROL Display type]**, select **[!UICONTROL Custom]**.
1. In **[!UICONTROL Pattern]**, enter a numeric picture clause from the examples below.
1. Check the masked value on the canvas.

For the synthetic value `1234567812345678`, these patterns produce the following results:

| Pattern | Result |
|---------|--------|
| `num{mmmmmmmmmmmm9999}` | `************5678` |
| `num{mmmmmmmmmmmmmmm9}` | `***************8` |
| `num{mmmmmmmmmmmmmmmm}` | `****************` |

## Verify the masked value

Compare the canvas value with the expected result for your custom pattern. For the predefined pattern `num{mmmm mmmm mmmm mmmm zzz9}`, the synthetic value `12345678901234567890` displays as `**** **** **** **** 7890`.

Check representative values from your data, including the shortest and longest values, before using the pattern.

## Pattern considerations

The symbols in a numeric picture clause determine which digit positions are masked or displayed.

| Symbol | Meaning |
|--------|---------|
| `m` | Masks an integer digit with `*`; suppresses leading zeros until the first significant or required digit |
| `9` | Displays a required digit |
| `z` | Displays a digit while suppressing leading zeros |

Keep these considerations in mind when choosing a pattern:

* Include enough digit positions for the longest value. Values exceeding the pattern's capacity display unchanged in the canvas.
* Leading zeros can be suppressed; an all-zero value displays as `0`.
* Spaces and hyphens in a pattern remain in the displayed result.
* If the preset is unavailable for the [selected locale](/help/forms/interactive-communication/support-localization.md), enter its picture clause using **[!UICONTROL Custom]**.
* These examples mask integer values, not decimal digits.

>[!IMPORTANT]
>
> Do not rely on display masking to protect stored or transmitted payment information.

## Related tasks

For related field configuration tasks, see:

* [Numeric Field component](/help/forms/interactive-communication/numeric-field.md)
* [Configure the locale](/help/forms/interactive-communication/support-localization.md)
* [Configure data binding](/help/forms/interactive-communication/configure-data-binding.md)
