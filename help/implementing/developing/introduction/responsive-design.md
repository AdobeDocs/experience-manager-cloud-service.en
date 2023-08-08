---
title: Responsive Design
description: With responsive design, the same experiences can be effectively displayed on multiple devices in multiple orientations
---

# Responsive Design {#responsive-design}

Design your experiences so that they adapt to the client viewport in which they are displayed. With responsive design, the same pages can be effectively displayed on multiple devices in both orientations. The following image demonstrates some ways in which a page can respond to changes in viewport size:

* Layout: Use single-column layouts for smaller viewports, and multiple-column layouts for larger viewports.
* Text size: Use larger text size (when appropriate, such as headings) in larger viewports.
* Content: Include only the most important content when displaying on smaller devices.
* Navigation: Device-specific tools are provided for accessing other pages.
* Images: Serving image renditions that are appropriate for the client viewport according to the window dimensions.

![Examples of responsive design](assets/responsive-example.png)

Develop Adobe Experience Manager (AEM) applications that generate HTML5 that adapts to multiple window sizes and orientations. For example, the following ranges of viewport widths correspond with various device types and orientations

* Maximum width of 480 pixels (phone, portrait)
* Maximum width of 767 pixels (phone, landscape)
* Width between 768 pixels and 979 pixels (tablet, portrait)
* Width between 980 pixels and 1199 pixels (tablet, landscape)
* Width of 1200px or greater (desktop)

See the following topics for information about implementing responsive design behavior:

* [Media queries](#using-media-queries)
* [Fluid grids](#developing-a-fluid-grid)
* [Adaptive images](#using-adaptive-images)

As you design, use the **Emulator** toolbar to preview your pages for various screen sizes.

## Before You Develop {#before-you-develop}

Before you develop the AEM application that supports your web pages, several design decisions should be made. For example, you need to have the following information:

* The devices you are targeting
* The target viewport sizes
* The page layouts for each of the targeted viewport size

### Application Structure {#application-structure}

The typical AEM application structure supports all responsive design implementations:

* Page components reside below `/apps/<application_name>/components`
* Templates reside below `/apps/<application_name>/templates`

## Using Media Queries {#using-media-queries}

Media queries enable the selective use of CSS styles for page rendering. AEM development tools and features enable you to effectively and efficiently implement media queries in your applications.

The W3C group provides the [Media Queries](https://www.w3.org/TR/css3-mediaqueries/) recommendation that describes this CSS3 feature and the syntax.

### Creating the CSS File {#creating-the-css-file}

In your CSS file, define media queries based on the properties of the devices that you are targeting. The following implementation strategy is effective for managing styles for each media query:

* Use a [Client Library folder](clientlibs.md) to define the CSS that is assembled when the page is rendered.
* Define each media query and the associated styles in separate CSS files. It is useful to use file names that represent the device features of the media query.
* Define styles that are common to all devices in a separate CSS file.
* In the css.txt file of the Client Library folder, order the list CSS files as is required in the assembled CSS file.

The [WKND tutorial](develop-wknd-tutorial.md) uses this strategy to define styles in the site design. The CSS file used by WKND is located at `/apps/wknd/clientlibs/clientlib-grid/less/grid.less`.

### Using Media Queries with AEM Pages {#using-media-queries-with-aem-pages}

[The WKND sample project](/help/implementing/developing/introduction/develop-wknd-tutorial.md) and [AEM Project Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/overview.html) use the [Page Core Component,](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/wcm-components/page.html) which includes the clientlibs via the page policy.

If your own page component is not based on the Page Core Component, you can also include the client library folder in the HTL or JSP script of it. Doing so helps generate the CSS file that includes the media queries, and references the file.

#### HTL {#htl}

<sly data-sly-use.clientlib="${'/libs/granite/sightly/templates/clientlib.html'}">
<sly data-sly-call="${clientlib.all @ categories='apps.weretail.all'}"/>

#### JSP {#jsp}

```xml
<ui:includeClientLib categories="apps.weretail.all"/>
```

The JSP script generates the following HTML code that references the style sheets:

```xml
<link rel="stylesheet" href="/etc/designs/weretail/clientlibs-all.css" type="text/css">
<link href="/etc/designs/weretail.css" rel="stylesheet" type="text/css">
```

## Previewing for Specific Devices {#previewing-for-specific-devices}

The emulator allows you to see previews of your pages in different viewport sizes so you can test the behavior of your responsive design. When editing a page in the Sites Console, you can tap or click the **Emulator** icon to reveal the emulator.

![The emulator icon in the toolbar](assets/emulator-icon.png)

In the emulator toolbar you can tap or click the **Devices** icon to reveal a drop-down menu where you can select a device. When you select a device, the page changes to adapt to the viewport size.

![The emulator toolbar](assets/emulator.png)

### Specifying Device Groups {#specifying-the-device-groups}

To specify the device groups that appear in the **Devices** list, add a `cq:deviceGroups` property to the `jcr:content` node of the template page of your site. The value of the property is an array of paths to the device group nodes.

For example, the template page of the WKND site is `/conf/wknd/settings/wcm/template-types/empty-page/structure`. And the `jcr:content` node beneath it includes the following property:

* Name: `cq:deviceGroups`
* Type: `String[]`
* Value: `mobile/groups/responsive`

Device group nodes are in the `/etc/mobile/groups` folder.

## Responsive Images {#responsive-images}

Responsive pages will dynamically adapt to the device on which they are rendered, offering a better experience for the user. However it is also important that assets that are appropriate to the device are also delivered and thus minimizing page load time.

[The Core Component Image Component](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/wcm-components/image.html) features adaptive image selection and responsive behavior with lazy loading.

* By default, the Image Component uses the [Adaptive Image Servlet](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/adaptive-image-servlet.html) to deliver the proper rendition.
* [Web-Optimized Image Delivery](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/web-optimized-image-delivery.html) is also available, which delivers image assets from the DAM in WebP format and can reduce the download size of an image by about 25% on average.

## Developing a fluid grid {#developing-a-fluid-grid}

AEM enables you to efficiently and effectively implement fluid grids. This page explains how you can integrate your fluid grid or an existing grid implementation (such as [Bootstrap](https://github.com/topics/twitter-bootstrap?l=css)) into your AEM application.

If you are not familiar with fluid grids, see the [Introduction to Fluid Grids](/help/sites-developing/responsive.md#developing-a-fluid-grid) section at the bottom of this page. This introduction provides an overview of fluid grids and guidance for designing them.

### Defining the grid using a Page component {#defining-the-grid-using-a-page-component}

Use page components to generate the HTML elements that define the content blocks of the page. The ClientLibraryFolder that the page references provides the CSS that controls the layout of the content blocks:

* Page component: Adds div elements that represent rows of content blocks. The div elements that represent content blocks include a parsys component where authors add content.
* Client library folder: Provides the CSS file that includes media queries and styles for the div elements.

For example, the sample geometrixx-media application contains the media-home component. This page component inserts two scripts, which generate two `div` elements of class `row-fluid`:

* The first row contains a `div` element of class `span12` (the content spans 12 columns). The `div` element contains the parsys component.

* The second row contains two `div` elements, one of class `span8` and the other of class `span4`. Each `div` element includes the parsys component.

```xml
<div class="page-content">
    <div class="row-fluid">
        <div class="span12">
            <cq:include path="grid-12-par" resourceType="foundation/components/parsys" />
        </div>
    </div>
    <div class="row-fluid">
        <div class="span8">
            <cq:include path="grid-8-par" resourceType="foundation/components/parsys" />
        </div>
        <div class="span4">
            <cq:include path="grid-4-par" resourceType="foundation/components/parsys" />
        </div>
    </div>
</div>
```

>[!NOTE]
>
>When a component includes multiple `cq:include` elements that reference the parsys component, each `path` attribute must have a different value.
>

#### Scaling the Page component grid {#scaling-the-page-component-grid}

The design that is associated with the geometrixx-media page component (`/etc/designs/geometrixx-media`) contains the `clientlibs` ClientLibraryFolder. This ClientLibraryFolder defines CSS styles for `row-fluid` classes, `span*` classes, and `span*` classes that are children of `row-fluid` classes. Media queries enable styles to be redefined for different viewport sizes.

The following example CSS is a subset of those styles. This subset focuses on `span12`, `span8`, and `span4` classes, and media queries for two viewport sizes. Notice the following characteristics of the CSS:

* The `.span` styles define element widths using absolute numbers.
* The `.row-fluid .span*` styles define element widths as percentages of the parent. Percentages are calculated from the absolute widths.
* Media queries for larger viewports assign larger absolute widths.

>[!NOTE]
>
>The Geometrixx Media sample integrates the [Bootstrap](https://getbootstrap.com/2.0.2/) JavaScript framework into its fluid grid implementation. The Bootstrap framework provides the bootstrap.css file.

```xml
/* default styles (no media queries) */
 .span12 { width: 940px }
 .span8 { width: 620px }
 .span4 { width: 300px }
 .row-fluid .span12 { width: 100% }
 .row-fluid .span8 { width: 65.95744680851064% }
 .row-fluid .span4 { width: 31.914893617021278% }

@media (min-width: 768px) and (max-width: 979px) {
 .span12 { width: 724px; }
 .span8 {     width: 476px; }
 .span4 {     width: 228px; }
 .row-fluid .span12 {     width: 100%;}
 .row-fluid .span8 {     width: 65.74585635359117%; }
 .row-fluid .span4 {     width: 31.491712707182323%; }
}

@media (min-width: 1200px) {
 .span12 { width: 1170px }
 .span8 { width: 770px }
 .span4 { width: 370px }
 .row-fluid .span12 { width: 100% }
 .row-fluid .span8 { width: 65.81196581196582% }
 .row-fluid .span4 { width: 31.623931623931625% }
}
```

#### Repositioning content in the Page component grid {#repositioning-content-in-the-page-component-grid}

The pages of the sample Geometrixx Media application distribute rows of content blocks horizontally in wide viewports. In smaller viewports, the same blocks are distributed vertically. The following example CSS shows the styles that implement this behavior for the HTML code that the media-home page component generates:

* The default CSS for the media-welcome page assigns the `float:left` style for `span*` classes that are inside `row-fluid` classes.

* Media queries for smaller viewports assign the `float:none` style for the same classes.

```xml
/* default styles (no media queries) */
    .row-fluid [class*="span"] {
        width: 100%;
        float: left;
}

@media (max-width: 767px) {
    [class*="span"], .row-fluid [class*="span"] {
        float: none;
        width: 100%;
    }
}
```

#### Modularize your Page components {#tip-modularize-your-page-components}

Modularize your components so you can make efficient use of the code. Your site likely uses several different types of pages, such as a welcome page, an article page, or a product page. Each type of page contains different types of content and likely use different layouts. However, when certain elements of each layout are common across multiple pages, you can reuse the code that implements that part of the layout.

**Use page component overlays**

Create a main page component that provides scripts for generating the various parts of a page, such as `head` and `body` sections, and `header`, `content`, and `footer` sections within the body.

Create other page components that use the main page component as the `cq:resourceSuperType`. These components include scripts that override the scripts of the main page as needed.

For example, the goemetrixx-media application includes the page component (the `sling:resourceSuperType` is the foundation page component). Several child components (such as article, category, and media-home) use this page component as the `sling:resourceSuperType`. Each child component includes a content.jsp file that overrides the content.jsp file of the page component.

**Reuse scripts**

Create multiple JSP scripts that generate row and column combinations that are common for multiple page components. For example, the `content.jsp` script of the article and media-home components both reference the `8x4col.jsp` script.

**Organize CSS styles by targeted viewport size**

Include CSS styles and media queries for different viewport sizes in separate files. Use client library folders to concatenate them.

### Inserting components into the page grid {#inserting-components-into-the-page-grid}

When components generate a single block of content, generally the grid that the page component establishes controls the placement of the content.

As an author, the content block can be rendered in various sizes and relative positions. Content text should not use relative directions to refer to other content blocks.

If necessary, the component should provide any CSS or JavaScript libraries that are required for the HTML code that it generates. Use a client library folder inside the component so the CSS and JS files are generated. To expose the files, [create a dependency or embed the library](/help/sites-developing/clientlibs.md#creating-client-library-folders) in another client library folder below the /etc folder.

**Sub-grids**

If the component contains multiple blocks of content, add the content blocks inside a row to establish a sub-grid on the page:

* Use the same class names as the containing page component so you can express div elements as rows and content blocks.
* To override the behavior that the page design's CSS implements, use a second class name for the row div element and provide the associated CSS in a client library folder.

For example, the `/apps/geometrixx-media/components/2-col-article-summary` component generates two columns of content. The HTML that it generates has the following structure:

```xml
<div class="row-fluid mutli-col-article-summary">
    <div class="span6">
        <article>
            <div class="article-summary-image">...</div>
            <div class="social-header">...</div>
            <div class="article-summary-description">...</div>
            <div class="social">...</div>
        </article>
    </div>
</div>
```

The `.row-fluid .span6` selectors of the page's CSS applies to the `div` elements of the same class and structure in this HTML. However, the component also includes the /apps/geometrixx-media/components/2-col-article-summary/clientlibs client library folder:

* The CSS uses the same media queries as the page component to establish changes in layout at the same discrete page widths.
* Selectors use the `multi-col-article-summary` class of the row `div` element to override the behavior of the page's `row-fluid` class.

For example, the following styles are included in the `/apps/geometrixx-media/components/2-col-article-summary/clientlibs/css/responsive-480px.css` file:

```xml
@media (max-width: 480px) {
    .mutli-col-article-summary .article-summary-image {
        float: left;
        width: 127px;
    }
    .mutli-col-article-summary .article-summary-description {
        width: auto;
        margin-left: 127px;
    }
    .mutli-col-article-summary .article-summary-description h4 {
        padding-left: 10px;
    }
    .mutli-col-article-summary .article-summary-text {
        margin-left: 127px;
        min-height: 122px;
        top: 0;
    }
}
```

## Introduction to fluid grids {#introduction-to-fluid-grids}

Fluid grids enable page layouts to adapt to the dimensions of the client viewport. Grids consist of logical columns and rows that position the blocks of content on the page.

* Columns determine the horizontal positions and widths of content blocks.
* Rows determine the relative vertical positions of content blocks.

Using HTML5 technology you can implement the grid and manipulate it to adapt page layouts to different viewport sizes:

* HTML `div` elements contain blocks of content that span some columns.
* One or more of these div elements comprise a row when they share a common parent div element.

### Using discrete widths {#using-discrete-widths}

For each range of viewport widths that you are targeting, use a static page width and content blocks of constant width. When manually resizing a browser window, changes to content size occur at discrete window widths (also known as breakpoints). Therefore, page designs are more closely adhered to, maximizing the user experience.

#### Scaling the grid {#scaling-the-grid}

Use grids to scale content blocks to adapt to different viewport sizes. Content blocks span a specific number of columns. As column widths increase or decrease to fit different viewport sizes, the widths of the content blocks increase or decrease accordingly. Scaling can support both large- and medium-sized viewports that are wide enough to accommodate the side-by-side placement of content blocks.

![Image of two grids, one that is scaled smaller than the other.](do-not-localize/chlimage_1-1a.png)

#### Repositioning content in the grid {#repositioning-content-in-the-grid}

The size of content blocks can be constrained by a minimum width, beyond which scaling is no longer effective. For smaller viewports, the grid can be used to vertically distribute blocks of content rather than horizontally.

![Image of two grids, one that is repositioned smaller than the other.](do-not-localize/chlimage_1-2a.png)

### Designing the grid {#designing-the-grid}

Determine the columns and rows that you must position the blocks of content on your pages. Your page layouts determine the number of columns and rows that span your grid.

**Number of columns**

Include enough columns to horizontally position the content blocks in all of your layouts, for all viewport sizes. Use more columns than are currently needed so you can accommodate future page designs.

**Row contents**

Use rows to control the vertical positioning of content blocks. Determine the content blocks that share the same row:

* Content blocks that are located next to each other horizontally in any of the layouts are in the same row.
* Content blocks that are located next to each other horizontally (wider viewports) and vertically (smaller viewports) are in the same row.

### Grid implementations {#grid-implementations}

Create CSS classes and styles so you can control the layout of the content blocks on a page. Page designs are often based on the relative size and position of content blocks within the viewport. The viewport determines the actual size of the content blocks. Your CSS must account for the relative and the absolute sizes. You can implement a fluid grid using three types of CSS classes:

* A class for a `div` element that is a container for all rows. This class sets the absolute width of the grid.
* A class for `div` elements that represent a row. This class controls the horizontal or vertical positioning of the content blocks that it contains.
* Classes for `div` elements that represent blocks of content of different widths. Widths are expressed as a percentage of the parent (the row).

Targeted viewport widths (and their associated media queries) demarcate discrete widths that are used for a page layout.

#### Widths of content blocks {#widths-of-content-blocks}

Generally, the `width` styles of content block classes are based on the following characteristics of your page and grid:

* The absolute page width that you are using for each targeted viewport size. Known values.
* The absolute width of the grid columns for each page width. You determine these values.
* The relative width of each column as a percentage of the total page width. You calculate these values.

The CSS includes a series of media queries that use the following structure:

```xml
@media(query_for_targeted_viewport){

  .class_for_container{ width:absolute_page_width }
  .class_for_row { width:100%}

  /* several selectors for content blocks   */
  .class_for_content_block1 { width:absolute_block_width1 }
  .class_for_content_block2 { width:absolute_block_width2 }
  ...

  /* several selectors for content blocks inside rows */
  .class_for_row .class_for_content_block1 { width:relative_block_width1 }
  .class_for_row .class_for_content_block2 { width:relative_block_width2 }
  ...
}
```

Use the following algorithm as a starting point for developing the element classes and CSS styles for your pages.

1. Define a class name for the div element that contains all rows, for example `content.`
1. Define a CSS class for div elements that represent rows, such as `row-fluid`.
1. Define class names for content block elements. A class is required for all possible widths, in terms of column spans. For example, use the `span3` class for `div` elements that span three columns, use `span4` classes for spans of four columns. Define as many classes as there are columns in your grid.

1. For each viewport size that you are targeting, add the corresponding media query to your CSS file. Add the following items in each media query:

    * A selector for the `content` class, for example `.content{}`.
    * Selectors for each span class, for example `.span3{ }`.
    * A selector for the `row-fluid` class, for example `.row-fluid{ }`
    * Selectors for span classes that are inside row-fluid classes, for example `.row-fluid span3 { }`.

1. Add width styles for each selector:

    1. Set the width of `content` selectors to the absolute size of the page, for example `width:480px`.
    1. Set the width of all row-fluid selectors to 100%.
    1. Set the width of all span selectors to the absolute width of the content block. A trivial grid uses evenly distributed columns of the same width: `(absolute width of page)/(number of columns)`.
    1. Set the width of the `.row-fluid .span` selectors as a percentage of the total width. Calculate this width using the `(absolute span width)/(absolute page width)*100` formula.

#### Positioning Content Blocks in Rows {#positioning-content-blocks-in-rows}

Use the float style of the `.row-fluid` class so you can control whether the content blocks in a row are arranged horizontally or vertically.

* The `float:left` or `float:right` style causes the horizontal distribution of child elements (content blocks).

* The `float:none` style causes vertical distribution of child elements.

Add the style to the `.row-fluid` selector inside each media query. Set the value according to the page layout that you are using for that media query. For example, the following diagram illustrates a row that distributes content horizontally for wide viewports, and vertically for narrow viewports.

![Two images of content blocks in a row, the second image showing the row repositioned.](do-not-localize/chlimage_1-3a.png)

The following CSS could implement this behavior:

```xml
@media (min-width: 768px) and (max-width: 979px) {
   .row-fluid {
       width:100%;
       float:left
   }
}

@media (max-width:480px){
    .row-fluid {
       width:100%;
       float:none
   }
}
```

#### Assigning classes to content blocks {#assigning-classes-to-content-blocks}

For the page layout of each viewport size you are targeting, determine the number of columns that each content block spans. Then, determine which class to use for the div elements of those content blocks.

When you have established the div classes, you can implement the grid using your AEM application.