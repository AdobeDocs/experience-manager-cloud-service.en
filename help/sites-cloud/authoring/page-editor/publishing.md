---
title: Publishing Content with the Page Editor
description: Learn how the Page Editor publishes content.
solution: Experience Manager Sites
feature: Authoring
role: User
---

# Publishing Content with the Sites Editor {#publishing}

Learn how the Page Editor publishes content.

## Publishing from the Page Editor {#publishing-from-the-page-editor}

If you are editing a page in the [page editor](/help/sites-cloud/authoring/page-editor/introduction.md), it can be published directly from the editor.

1. Select the **Page Information** icon to open the menu and then the **Publish Page** option.

   ![Publishing a page via page options](/help/sites-cloud/authoring/assets/publishing-page-options.png)

1. Depending on whether the page has references that need publishing:

   * The page is published directly if there are no references to be published.
   * If the page has references that need publishing, these are listed in the **Publish** wizard, where you can either:
     * Specify which of the assets, or tags, and so on, that you want to publish together with the page, then use **Publish** to complete the process.
     * Use **Cancel** to abort the action.

   ![Publishing references with the page](/help/sites-cloud/authoring/assets/publishing-references.png)

1. Selecting **Publish** will replicate the page to the publish environment. In the page editor, an information banner is shown confirming the publish action.

   ![Publish status info banner](/help/sites-cloud/authoring/assets/publishing-info.png)

   When viewing the same page in the console, the updated publication status is visible.

   ![Page publication status in column view in the sites console](/help/sites-cloud/authoring/assets/publishing-status-console-column.png)

>[!NOTE]
>
>Publishing from the page editor is a shallow publish, that is, only the selected page/pages is/are published and any child page(s) is/are not.

>[!NOTE]
>
>Pages accessed by [aliases](/help/sites-cloud/authoring/sites-console/page-properties.md#advanced) in the editor cannot be published. Publish options in the editor are only available for pages accessed via their actual paths.

## Unpublishing from the Page Editor {#unpublishing}

When editing a page using the Page Editor, if you want to unpublish that page, select **Unpublish Page** in the **Page Information** menu, much as you would [publish the page](#publishing-from-the-editor).

>[!NOTE]
>
>Pages accessed by [aliases](/help/sites-cloud/authoring/sites-console/page-properties.md#advanced) in the editor cannot be unpublished. Publish options in the editor are only available for pages accessed via their actual paths.

## Publishing and Unpublishing from the Sites Console {#publishing-sites-console}

You can also publish [from the Sites console,](/help/sites-cloud/authoring/sites-console/publishing-pages.md) which can be useful when you wish to publish multiple pages of content or schedule publication or unpublication.
