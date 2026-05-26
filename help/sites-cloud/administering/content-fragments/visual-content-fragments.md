---
title: Visual Content Fragments
description: Learn how to visualize and publish Visual Content Fragments using HTML templates. 
feature: Content Fragments
role: User, Developer
---
# Visual Content Fragments {#visual-content-fragments}

Content Fragments contain structured content that is intended for JSON output, without design or layout. The addition of HTML templates allows you to create fully decorated, visual experiences with structured content in HTML format:

* Visualizing a content fragment helps content quality assurance, allowing stakeholders to review content before it is used, without having to open Content Fragment Editor

* Delivering a visual fragment aids omnichannel delivery, for reuse of modular experiences across channels such as web, email or mobile apps.

The rendered output of an AEM Content Fragment that uses the layout and design of an attached HTML template is called a *Visual Content Fragment*. 

HTML templates contain layout and design information, enabling the visualization of Content Fragments. The connection between a template and a Content Fragment is established using Handlebars syntax to map HTML tags to data types (fields) defined in the Content Fragment Model. This definition allows content authored in the respective fields of the Content Fragment Editor to be displayed in the appropriate locations within the template. 

You, or your development team, can [create and customize your own HTML templates](/help/implementing/developing/extending/content-fragments-visualization-templates.md), then [upload and attach one, or more, to Content Fragment Models](#upload-and-assign-your-template) so that the corresponding fragments can be rendered into experiences, [previewed](#preview-your-fragment-with-a-template) and [delivered as required](#deliver-your-visual-content-fragment).

>[!NOTE]
>
>A **Generic Template** is always available within AEM as a default, associated with every model. This template enables key/value pairs in structured content to be displayed in a clean, table-style format to support content Quality Assurance (QA) use cases. 

## Create a Template {#create-a-template}

HTML templates developed using Handlebars allow you to preview and deliver Visual Content Fragments in HTML format. The Handlebars.js syntax defines placeholders for content that is authored in Content Fragment fields.

For details on developing your own templates see [Visual Content Fragments - Templates](/help/implementing/developing/extending/content-fragments-visualization-templates.md).

## Upload and Assign your Template {#upload-and-assign-your-template}

A template is associated with a Content Fragment Model so that it can be used with any Content Fragments created from that model.

To upload your new HTML template:

1. In the Content Fragment console open the tab for **Content Fragment Models**.
1. Navigate to the location of your fragment model.
1. Select the information icon (i) for the required model:

   ![Content Fragment Console - Information icon](/help/sites-cloud/administering/content-fragments/assets/cfc-information-icon.png)

   The right panel will be shown. 
1. Scroll down to show **HTML Templates**, the **Generic Template** is already listed as it is the default:

   ![Preview Fragment with Generic HTML Template](/help/sites-cloud/administering/content-fragments/assets/cf-visual-html-template-configure-default.png)

1. Select **+** to upload your template from an HTML file (`.html`). A dialog will allow you to **Browse** your local file system and select your template file.
1. Once uploaded two views of the template are shown for you to review:

   * left: a rendering of the template without content
   * right: the HTML code, that can also be edited here before importing to AEM

   ![Review HTML template on upload](/help/sites-cloud/administering/content-fragments/assets/cf-visual-html-template-upload-review.png)

1. Select **Next** to continue.
1. Enter a **Template name** for use in AEM.
1. Confirm with **Create Template**.
1. The template will be created in AEM and listed under **HTML Templates**, in properties of Content Fragment Models.
   Once loaded it can be used for [previewing fragments](#preview-your-fragment-with-a-template). You can also **[Download](#download-your-template)** or **[Delete](#download-your-template)** the template.

## Preview your fragment with a Template {#preview-your-fragment-with-a-template}

To preview your Content Fragment using a template:

>[!NOTE]
>
>As the **Generic Template** is always available you can preview your fragment without loading any custom templates.

1. In the Content Fragment console navigate to the location of your fragment.

1. Either:
   * select your fragment in the console
   * open your fragment in the editor

1. Select **Preview** from the top toolbar of:

   * the Content Fragment console 
   * the editor, where you can then select **Template**

In both cases a new modal window will open. 

1. If no custom templates are available, then AEM will use the **Generic Template** to display your fragment. The **Generic Template**:

   * displays the fields of your fragment in table form; name and content
   * shows the fully hydrated content of referenced fragments in the same view 

1. If custom templates are available, you can select the template you want to use (including the **Generic Template**).

1. If the Content Fragment is published you can also view and copy its **Preview URL** and **Publish URL**.

For example, preview with the **Generic Template**:

![Preview Fragment with Generic HTML Template](/help/sites-cloud/administering/content-fragments/assets/cf-visual-html-template-referenced-fragment.png)

## Deliver your Visual Content Fragment {#deliver-your-visual-content-fragment}

The Visual Content Fragment can be delivered to a range of targets in HTML format.

### Deliver to the browser {#deliver-to-the-browser}

Copy the **Preview URL** or the **Publish URL**. Access this directly from your browser to see your Visual Content Fragment.

### Deliver to Edge Delivery Services {#deliver-to-edge-delivery-services}

You can deliver your visual fragment in an Edge Delivery Service (EDS) page.

1. Navigate to your EDS Project.
1. Add, or access, a **[Block](https://www.aem.live/developer/block-collection)** of the type **[embed](https://sidekick-library--aem-block-collection--adobe.aem.page/tools/sidekick/library.html?plugin=blocks&path=/block-collection/embed&index=0)**.
1. Paste the **Publish URL** to the block.
1. Publish your EDS page. The HTML representation of your fragment is seen.

>[!NOTE]
>
>For full details see [Integration with Edge Delivery Services (Embed Block)](/help/implementing/developing/extending/content-fragments-visualization-publish-url.md#integration-with-edge-services-embed-block)

### Deliver to an AEM page {#deliver-to-an-AEM-page}

You can deliver your Visual Content Fragment in an AEM page using the Core Component: Content Fragment.

When configuring a **Content Fragment** [component on your page](/help/sites-cloud/authoring/fragments/content-fragments.md#adding-a-content-fragment-to-your-page):

1. Specify the required **Content Fragment**.
1. Select **Content Fragment Visualization**.
1. Select the required **Visualization Template** from the drop down list.

   ![Configure Content Fragment component for a visual fragment](/help/sites-cloud/administering/content-fragments/assets/cf-visual-template-aem-page.png)

1. The visual fragment will be shown in the page.

>[!NOTE]
>
>For full details see [Integration - AEM Sites with Core Components](/help/implementing/developing/extending/content-fragments-visualization-publish-url.md#integration-aem-sites-with-core-components)

## Download your template {#download-your-template}

To download your HTML template from AEM:

1. In the Content Fragment console open the tab for **Content Fragment Models**.
1. Navigate to the location of your fragment model.
1. Select the information icon (i) for the required model:

   ![Content Fragment Console - Information icon](/help/sites-cloud/administering/content-fragments/assets/cfc-information-icon.png)

   The right panel will be shown.

1. Scroll down to show **HTML Templates**.
1. Select the ellipse by the template you want to download.
1. Select **Download**.
1. Specify the file name and location.
1. Confirm with **Save**.

## Delete your template {#delete-your-template}

To delete your new HTML template (from AEM):

1. In the Content Fragment console open the tab for **Content Fragment Models**.
1. Navigate to the location of your fragment model.
1. Select the information icon (i) for the required model:

   ![Content Fragment Console - Information icon](/help/sites-cloud/administering/content-fragments/assets/cfc-information-icon.png)

   The right panel will be shown. 
1. Scroll down to show **HTML Templates**.
1. Select the ellipse by the template you want to download.
1. Select **Delete**.
1. In the following dialog confirm the action with **Delete**.
