---
title: Configuring Search Forms
description: Learn how to configure Search Forms.
---
# Configure search filters for Inbox {#configure-search-filters-inbox}

You can configure search filters for Inbox items. Base your search criteria on a specific Inbox column to filter the results.

For example, to filter the Inbox items based on a Date of Birth Inbox column range, you can use the Date Range predicate to define the date range.

The following are the available predicate types for Inbox:

* Range Predicate

* Text Predicate

* Date Range Predicate

* Options Property Predicate

## Creating or opening a customized configuration {#creating-opening-customized-configuration}

1. Navigate to **[!UICONTROL Tools]**, **[!UICONTROL General]**, **[!UICONTROL Search Forms]**.

1. Select the **[!UICONTROL Inbox Search Rail]** configuration and tap **[!UICONTROL Edit]**.
1. Incorporate the predicate configuration changes using **[!UICONTROL Edit Search Form]**.
1. Select **[!UICONTROL Done]** to save the configuration.

## Range Predicate {#range-predicate}

You can filter Inbox items based on a column of Number type using the Range Predicate. You can also choose to include decimal values for numbers.

To configure a Range Predicate:

1. Open the [form for configuration](#creating-opening-customized-configuration).
1. Tap the **[!UICONTROL Select Predicate]** tab and drag **[!UICONTROL Range Predicate]** to the form.
1. In the **[!UICONTROL Settings]** tab, select the Inbox column name to base your search on, from **[!UICONTROL Column Name]** field.
1. Specify the label for the filter in the **[!UICONTROL Filter Label]** field. Select the **[!UICONTROL Enable Decimal Values]** checkbox to accept decimal values for numbers while defining the range.
1. Specify an optional description for the configuration and tap **[!UICONTROL Done]** to save it.

The configuration changes reflect when you open the Filters page. The filter label that you specified in step 4 displays as the label with an option to define the maximum and minimum values. [!DNL Experience Manager] applies the search criteria on the column name specified in step 3 and returns the Inbox items.

