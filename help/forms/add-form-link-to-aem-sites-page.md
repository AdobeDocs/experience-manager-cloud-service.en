---
title: How to add forms links on the AEM Sites page using the Link Forms Portal component?
description: Learn how to add forms links to the AEM Sites page.
feature: Adaptive Forms, Core Components
role: User, Developer, Admin
exl-id: a55d0776-8827-46cc-9625-5d6f5f6bda3b
---
# Add form links to Sites page

In the bank website scenario, the **Link** Forms Portal component enhances navigation by guiding users to specific forms across various sections of the site. It provides direct references to forms such as loan applications, account opening forms, or feedback surveys, strategically placed throughout the website. The **Link** component inserts links that direct users to specific Adaptive Forms within the Sites page. For example, on the bank's website, anonymous users can access a general inquiry form, while logged-in users can directly access more secure forms, such as loan applications or transaction authorization forms.

![Link icon](/help/forms/assets/link-forms.png)

## Pre-requisite

Before exploring the various capabilities of a Forms Portal component, ensure that Core Components are enabled for your environment. For detailed instructions on how to enable Core Components for your environment, [click here](/help/forms/enable-adaptive-forms-core-components.md).

After deploying the latest Core Components to your environment, the Forms Portal components become accessible in your authoring environment.

## Add the Link component to your Sites page

To add the **Link** portal component to your Sites page, perform the following steps:

1. Open the AEM Sites page in an **Edit** mode. 
1. Go to the **[!UICONTROL Page Information]** > **[!UICONTROL Edit Template]**
    ![Edit template policy](/help/forms/assets/save-form-as-draft-edit-template.png)

1. Click the **[!UICONTROL Policy]** and select the **[!UICONTROL Link]**  checkbox under the **[AEM Archetype Project Name] - Forms and Communications Portal**.

    ![Policy Selection](/help/forms/assets/add-link.png)

1. Click **[!UICONTROL Done]**.
1. Now, re-open the AEM Sites page in the authoring mode.
1. Locate the section within the page editor that allows you to add the Forms Portal component. 

1. Click the **Add** icon. The icon is a plus sign (+) that signifies the option to add new components.
    
    Clicking the **Add** icon displays an **Insert New Component** dialog box that displays various components for insertion.

    >[!NOTE]
    >
    > Alternatively, you can also drag and drop the component.

1. Browse the available components in the dialog box and select the desired component from the list. For example, select the **Link** component from the list to add the **Link** Forms Portal component. 

    ![Link component](/help/forms/assets/add-link-in-sites.png)

Now, configure the properties of the **Link** component.

## Understand the properties of the Link component

You can easily customize **Link** component properties using the Configure Dialog for a seamless user experience. To configure, select the component and then select the ![Configure icon](assets/configure_icon.png). The **[!UICONTROL Link]** dialog opens.

### Display Tab

![Display Tab](/help/forms/assets/link-asset-tab.png)

In the **[!UICONTROL Display]** tab, provide the link caption and tooltip to ease identification of the forms represented by the link.

### Asset Info tab

![Assets Info Tab](/help/forms/assets/link-asset-info.png)

In the **[!UICONTROL Asset Info]** tab, specify the repository path where the asset is stored. 

### Query Params tab

![Query Params Tab](/help/forms/assets/link-query-tab.png)

In the **[!UICONTROL Query Params]** tab, specify the additional parameters in the key-value pair format. When the link is clicked, these additional parameters and passed along with the form.

## View form links on the Sites page using the Link component

Preview the Sites page to view the link to an Adaptive Form, which is specified in the **Assets Info** properties tab of the **Link** component. Clicking the link displays the form on the screen for users, who can then access it based on the permissions. 

![Query Params Tab](/help/forms/assets/link-forms.png)

## Related articles

{{forms-portal-see-also}}

## See Also {#see-also}

{{see-also}}
