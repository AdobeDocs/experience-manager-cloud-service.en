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
