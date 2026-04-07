---
title: Visual Content Fragments
description: Learn how to preview and publish visualized Content Fragments. 
feature: Content Fragments
role: User, Developer
---
# Visual Content Fragments {#visual-content-fragments}

AEM allows you to preview, and deliver, your Content Fragments using a visual layout based on an HTML template:

* Previewing a fragment visually helps content quality assurance, allowing authors and readers to review content before it is used. 

* Delivering a visual fragment aids omnichannel delivery; such as embedding in email systems or mobile apps.

A **Generic Template** is always available within AEM as a default, but you can also [create and customize your own templates](/help/implementing/developing/extending/content-fragments-visualization-templates.md).

## Create a Template {#create-a-template}

The templates used for previewing and delivering visual Content Fragments are HTML templates developed using Handlebars.

For details on developing your own templates see [Visual Content Fragments - Templates](/help/implementing/developing/extending/content-fragments-visualization-templates.md).

## Upload and Assign your Template {#upload-and-assign-your-template}

A template is associated with a Content Fragment Model so that it can be used with any Content Fragments created from that model.

To upload your new HTML template:

1. In the Content Fragment console open the tab for **Content Fragment Models**.
1. Navigate to the location of your fragment model.
1. Select the information icon (i) for the required model. The right panel will be shown. 
1. Scroll down to show **HTML Templates**, the **Generic Template** is already listed as it is the default:

   ![Preview Fragment with Generic HTML Template](/help/sites-cloud/administering/content-fragments/assets/cf-visual-html-template-configure-default.png)

1. Select **+** to upload your template from an HTML file (`.html`). A dialog will allow you to **Browse** your local file system and select your template file.
1. Once uploaded two views of the template are shown for you to review:

   ![Review HTML template on upload](/help/sites-cloud/administering/content-fragments/assets/cf-visual-html-template-upload-review.png)

1. Select **Next** to continue.
1. Enter a **Template name** for use in AEM.
1. Confirm with **Create Template**.
1. The template will be created in AEM and listed under **HTML Templates**.
   Once loaded it can be used for [previewing fragments](#preview-your-fragment-with-a-template). You can also **[Download](#download-your-template)** or **[Delete](#download-your-template)** the template.

## Preview your fragment with a Template {#preview-your-fragment-with-a-template}

To preview your Content Fragment using a template:

>[!NOTE]
>
>As the **Generic Template** is always available you can preview your fragment without loading any customized templates.

1. In the Content Fragment console navigate to the location of your fragment.
1. Either:
   * Select your fragment in the console
   * Open your fragment in the editor
1. Select **Preview** from the top toolbar of:

   * the Content Fragment console 
   * the editor, where you can then select **Template**

In both cases a new model window will open. 

1. If no customized templates are available, then AEM will use the **Generic Template** to display your fragment. The **Generic Template**:

   * displays the fields of your fragment in table form; name and content
   * shows the content of referenced fragments in separate tables, with the same format
1. If customized templates are available, you can select the template you want to use (including the **Generic Template**)
1. If configured you can also select the **Preview URL** and the **Publish URL**.

For example, preview with the **Generic Template**:

![Preview Fragment with Generic HTML Template](/help/sites-cloud/administering/content-fragments/assets/cf-visual-html-template-referenced-fragment.png)

## Deliver your visual fragment {#deliver-your-visual-fragment}

The visual fragment can be delivered by directly accessing the HTML using either the **Preview URL** or the **Publish URL**.

## Download your Template {#download-your-template}

To download your new HTML template from AEM:

1. In the Content Fragment console open the tab for **Content Fragment Models**.
1. Navigate to the location of your fragment model.
1. Select the information icon (i) for the required model. The right panel will be shown. 
1. Scroll down to show **HTML Templates**.
1. Select the ellipse by the template you want to download.
1. Select **Download**.
1. Specify the file name and location.
1. Confirm with **Save**.

## Delete your Template {#delete-your-template}

To delete your new HTML template (from AEM):

1. In the Content Fragment console open the tab for **Content Fragment Models**.
1. Navigate to the location of your fragment model.
1. Select the information icon (i) for the required model. The right panel will be shown. 
1. Scroll down to show **HTML Templates**.
1. Select the ellipse by the template you want to download.
1. Select **Delete**.
1. In the following dialog confirm the action with **Delete**.
