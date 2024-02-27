---
title: Creating Pages
description: Learn how to create new pages for your website using the Sites console.
---

# Creating Pages {#creating-pages}

Learn how to create new pages for your website using the **Sites** console.

>[!TIP]
>
>Before you begin creating new pages, become familiar with [how your pages are organized in AEM.](/help/sites-cloud/authoring/sites-console/organizing-pages.md)

## Access Privileges {#access-privileges}

Your account needs the appropriate access rights and permissions to create pages.

If you encounter any problems we suggest you contact your system administrator.

## Creating a New Page {#creating-a-new-page}

Unless all pages have been created for you in advance, you must create a page before you can start creating content:

1. Open [the **Sites** console.](/help/sites-cloud/authoring/sites-console/introduction.md)
1. Navigate to the location where you want to create the new page.
1. Open the drop-down selector using **Create** in the toolbar, then select **Page** from the list:

   ![Creating a page](/help/sites-cloud/authoring/assets/organizing-create-page.png)

1. From the first stage of the wizard you can either:

    * Select the template you want used to create the new page, then select **Next** to proceed.

    * **Cancel** to abort the process.

   ![Selecting a template for a new page](/help/sites-cloud/authoring/assets/organizing-create-page-template.png)

1. From the final stage of the wizard you can either:

    * Use the three tabs to enter the [page properties](/help/sites-cloud/authoring/sites-console/page-properties.md) you want assigned to the new page, then select **Create** to actually create the page.

    * Use **Back** to return to template selection.

   Key fields are:

    * **Title**:

        * This is displayed to the user and is mandatory.

    * **Name**:

        * This is used to generate the URI. If not specified, the name is derived from the title.
        * If you supply a page **Name** when creating a page, AEM [validates the name according to the conventions](/help/implementing/developing/introduction/naming-conventions.md) imposed by AEM and JCR.
        * You **cannot submit invalid characters** in the **Name** field. When AEM detects invalid characters the field is highlighted and an explanatory message shown to indicate the characters that need removing/replacing.

   >[!TIP]
   >
   >See [Page Naming Conventions](#page-naming-conventions).

   The minimum information required to create a page is the **Title**.

   ![Providing page title](/help/sites-cloud/authoring/assets/organizing-create-page-title.png)

1. Use **Create** to complete the process and create your new page. The confirmation dialog will ask whether you want to **Open** the page immediately or return to the console (**Done**):

   ![Page creation success](/help/sites-cloud/authoring/assets/organizing-create-page-success.png)

   >[!NOTE]
   >
   >If you create a page using a name that already exists at that location, the system will automatically generate a variation of the name by appending a number. For example, if `beach` already exists, a new page becomes `beach1`.

1. If you return to the console you can see your new page:

   ![Resulting new page](/help/sites-cloud/authoring/assets/organizing-create-page-result.png)

>[!CAUTION]
>
>Once a page has been created its template cannot be changed - unless you [create a launch with a new template](/help/sites-cloud/authoring/launches/creating.md#create-launch-with-new-template), though this will lose any existing content.
