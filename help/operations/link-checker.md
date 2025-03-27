---
title: Link Checker
description: Learn how the Link Checker helps authors by validating links as they are added to content and what configuration options it offers.
feature: Operations
role: Admin
exl-id: f5f71e2f-69e3-44f9-812d-71fe417896f8
---
# Link Checker {#link-checker}

Learn how the Link Checker helps authors by validating links as they are added to content and what configuration options it offers.

## Overview {#overview}

Content authors should not have to concern themselves with validating every link that they include in their content. The Link Checker runs automatically to assist content authors with their links including:

* Validating links as they are added to content
* Showing a list of all external links in the content
* Performing link transformations

The Link Checker has several [configuration options](#configuring) such as defining the validation of internal links, allowing certain links or link patters to be omitted from validation, and defining link rewriting rules.

The Link Checker validates both [internal links](#internal) and [external links.](#external)

>[!NOTE]
>
>Because the Link Checker checks every content page's links, the Link Checker can impact performance on large repositories. In such cases, you may need to [configure how often the Link Checker runs](#configuring) or [disable it.](#disabling)

## Internal Link Checking {#internal}

Internal links are links to other content in your AEM repository. Internal links can be added using the path picker, the rich text editor, or using a custom component. For example:

* You create the page `/content/wknd/us/en/adventures/ski-touring`
* That page contains a link to `/content/wknd/us/en/adventures/extreme-ironing` in a [Text Component.](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/wcm-components/text)

Internal links are validated as soon as the content author adds an such a link to a page. If the link becomes invalid:

* It is removed from the publisher.
  * The link itself is removed.
  * The text of the link remains.
* It is shown as a broken link in the authoring interface.

![Link Checker checking internal links](assets/link-checker-internal.png)

## External Link Checking {#external}

External links are links to content outside of your AEM repository. External links can be added using the rich text editor or using a custom component. For example:

* You create the page `/content/wknd/us/en/adventures/ski-touring`
* That page contains a link to `https://bunwarmerthermalunderwear.com` in a [Text Component.](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/wcm-components/text)

External links are validated for syntax and by checking their availability. This check is done asynchronously at a configurable interval. If the Link Checker finds an external link invalid:

* It is removed from the publisher.
  * The link itself is removed.
  * The text of the link remains.
* It is shown as a broken link in the authoring interface.

![Link Checker checking external links](assets/link-checker-external.png)

### How the External Link Checker Works {#external-details}

The External Link Checker relies on several services and understanding how they work helps you understand how to [configure the Link Checker to meet your needs.](#configuring)

1. Whenever a content author saves any link to a page, an event handler is triggered.
1. The event handler traverses all content under `/content` and checks for new or updated links and adds them to a cache for the Link Checker.
1. The **Day CQ Link Checker Service** then executes on a regular schedule to check the entries in the cache for valid syntax.
1. The syntax-validated links then appear in the [External Link Checker window.](#external-using) However they will be in a **Pending** state.
1. The **Day CQ Link Checker Task** then executes on a regular basis to validate the links by making a GET call.
1. The **Day CQ Link Checker Task** then updates the entries in the [External Link Checker window](#external-using) with the results of the GET calls.

### Using the External Link Checker {#external-using}

The External Link Checker is a console that provides an overview of all external links in your AEM content. To use the External Link Checker:

1. From the Global Navigation, select **Tools** -&gt; **Sites**.
1. Select **External Link Checker** and a list of all external links is displayed.

![External link checker](assets/external-link-checker.png)

Each entry in the table represents an external link detected by the Link Checker service. The following columns are displayed:

* **Status** - The validation status of the link which can be one of the following:
  * **Valid** - The external link is reachable by the Link Checker.
  * **Pending** - The external link was added to site content, but has not yet been validated by the Link Checker.
  * **Invalid** - The external link is not reach able by the Link Checker.
* **URL** - The external link
* **Referrer** - The content page that contains the external link
  * This is only populated [if configured.](#configuring)
* **Last Checked** - The last time the Link Checker validated the external link
  * How often links are checked [is configurable.](#configuring)
* **Last Status** - The last HTML status code returned when the Link Checked last checked the external link
* **Last Available** - Time since the link was last available to the Link Checker
* **Last Accessed** - Time since the page with the external link was last accessed in the authoring interface

You can manipulate the content of the window by using the two buttons at the top of the list of links:

* **Refresh** - To refresh the content of the list
* **Check** - To check an individual external link selected in the list

All other icons in the External Link Checker window are inactive.

## Configuring the Link Checker {#configuring}

The Link Checker is available automatically out-of-the-box in AEM. However, there are several OSGi configurations that can be modified to change its behavior:

* **Day CQ Link Checker Info Storage Service** - This service defines the size of the Link Checker cache in the repository.
* **Day CQ Link Checker Service** - This service performs asynchronous checking of the syntax of external links.
  * You can define the check period and which types of links are skipped by the checker among other options.
* **Day CQ Link Checker Task** - This service performs the GET validation of external links. 
  * It allows separate definitions of intervals to check bad and good links among other options.
* **Day CQ Link Checker Transformer** - This service converts links based on a user-defined rule set.

See the document [Configuring OSGi](/help/implementing/deploying/configuring-osgi.md) for more details on how to change OSGi settings.

## Disabling the Link Checker {#disabling}

You may choose to disable the Link Checker entirely. To do so:

1. Open the OSGi console.
1. Edit the **Day CQ Link Checker Transformer**
1. Check the option(s) you wish to disable:
   * **Disable Checking** - to disable validation of links
   * **Disable Rewriting** - to disable link transformations
