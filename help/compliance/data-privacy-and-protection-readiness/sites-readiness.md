---
title: Data Protection and Data Privacy Regulations - AEM Sites Readiness
description: Learn about Experience Manager as a Cloud Service Sites support for the various Data Protection and Data Privacy Regulations; including the EU General Data Protection Regulation (GDPR), the California Consumer Privacy Act and how to comply when implementing a new AEM as a Cloud Service project.
exl-id: fdcad111-0cdd-46cc-964c-3f8669ca2030
feature: Compliance
role: Admin, Architect, Developer, Leader
---
# Experience Manager Sites readiness for data protection and data privacy regulations {#aem-sites-readiness-for-data-protection-and-data-privacy-regulations}

>[!WARNING]
>
>The contents of this document do not constitute legal advice and are not meant as a substitute for legal advice. 
>
>Consult your company's legal department for advice concerning Data Protection and Data Privacy regulations. 

>[!NOTE]
>
>For more information about Adobe's response to privacy issues, and what this means for you as an Adobe customer, see [Adobe's Privacy Center](https://www.adobe.com/privacy.html). 

Adobe Experience Manager as a Cloud Service Sites is ready to help customers with their data privacy and protection compliance obligations. This page guides customers through the procedures to handle such requests in AEM Sites. It describes the location of private data stored, and how to remove them manually or with code.

For more information, see the [Adobe Privacy Center](https://www.adobe.com/privacy.html).

>[!NOTE]
>
>See [Adobe Experience Manager as a Cloud Service Readiness for Data Protection and Data Privacy Regulations](/help/compliance/data-privacy-and-protection-readiness/aem-readiness.md) for further details.

## AEM Author Tier {#aem-author-tier}

User accounts and UGC content on the author server are covered in the [AEM Foundation documentation](/help/compliance/data-privacy-and-protection-readiness/foundation-readiness.md).

## AEM Publish Tier {#aem-publish-tier}

User accounts used to authenticate visitors on the site, and UGC content on the publish server are covered in the [AEM Foundation documentation](/help/compliance/data-privacy-and-protection-readiness/aem-readiness.md).

By default AEM Sites components do not store form-data entered by visitors on the  publish  server. It is recommended to forward the data to a third-party system, or Adobe Campaign for further processing.

## Opt-In/Opt-Out {#opt-in-opt-out}

<!--
AEM has a [cookie opt-out service](/help/sites-developing/cookie-optout.md ) that can be used for managing the opt-in/opt-out for users.
-->

Adobe Experience Manager is subject to a cookie opt-out service that is used for managing the opt-in/opt-out for users.

To Opt-out:

1. Navigate to: 
   [Adobe Privacy Center - Opt-out](https://www.adobe.com/privacy/opt-out.html)

1. Scroll down to **Services** - **Experience Cloud service usage data**.

1. Select the referenced link; currently titled **here**.

1. You are presented with the following details, together with the options to opt out or in:

    * To opt-out of aggregation and analysis of data about your visit to this site, it is necessary to install a cookie on your browser. This cookie identifies that you have opted-out.

      If you delete the opt-out cookie, or if you change computers or Web browsers, you need to opt-out again.

      Opt-out - Exclude me from visitor session aggregation and analysis (install the `amcglobal.sc.omtrdc.net` opt-out cookie) - Click Here.

      Opt-in - Include me in visitor session aggregation and analysis (do not install the `amcglobal.sc.omtrdc.net` opt-out cookie) - Click Here. 

    Follow the above steps to access the actual links.

    >[!NOTE]
    >
    > There is a further description in the **2. Privacy.** section of the [Adobe General Terms of Use](https://www.adobe.com/legal/terms.html).

## Analytics Foundation {#analytics-foundation}

AEM Sites includes an optional integration with Analytics Foundation which uses functionality within the Adobe Analytics On-demand Service.

For more information on managing data subject requests related to Adobe Analytics see [Adobe Analytics and Data Privacy](https://experienceleague.adobe.com/docs/analytics/admin/data-governance/gdpr-view-settings.html).

## Personalization Foundation by Target {#personalization-foundation-by-target}

AEM Sites includes an optional integration with Personalization Foundation by Target which uses functionality within the Adobe Target On-demand Service.

For information on managing data subject requests related to Adobe Target see [Adobe Target - Privacy and General Data Protection Regulation](https://experienceleague.adobe.com/docs/target-dev/developer/implementation/privacy/cmp-privacy-and-general-data-protection-regulation.html).

## ContextHub {#contexthub}

<!--
AEM provides an optional data layer with [ContextHub](/help/sites-developing/contexthub.md).
-->

AEM provides an optional data layer with ContextHub. This keeps visitor-specific data in the browser, to be used for rules-based personalization.

By default, this visitor-data is not stored in AEM; AEM sends rules to the data layer to make personalization decisions in the browser.

### Implementing Opt-in/Opt-Out {#implementing-opt-in-opt-out}

The site owner must implement an opt-out component according to the following guidelines.

These guidelines implement opt-in as the default. Thus, a website visitor must clearly agree, before any personal data is stored in the browser's (client-side) persistence.

* The opt-out component should be included every time the ContextHub component is included.
* The terms and conditions that relate to data protection and privacy for the website, must be displayed to the website visitor, allowing them to:

    * accept
    * reject
    * change their previous choice

* If a site visitor accepts the site's terms and conditions, the ContextHub opt-out cookie should be removed:

  ```
  ContextHub.Utils.Cookie.removeItem('cq-opt-out');
  ```

* If a site visitor does not accept the site's terms and conditions, the ContextHub opt-out cookie should be set:

  ```
  ContextHub.Utils.Cookie.setItem('cq-opt-out', 1);
  ```

* To check whether ContextHub is running in opt-out mode, the following call should be made in the browser's console:

  ```
  var isOptedOut = ContextHub.isOptedOut(true) === true;
  // if isOptedOut is true, ContextHub is running in opt-out mode
  ```

### Previewing Persistence of ContextHub {#previewing-persistence-of-contexthub}

To preview persistance used ContextHub, a user can:

* Use the browser's console; for example:

    * Chrome:

        * Open Developer Tools &gt; Application &gt; Storage:

            * Local Storage &gt; (website) &gt; ContextHubPersistence
            * Session Storage &gt; (website) &gt; ContextHubPersistence
            * Cookies &gt; (website) &gt; SessionPersistence

    * Firefox:

        * Open Developer Tools &gt; Storage:

            * Local Storage &gt; (website) &gt; ContextHubPersistence
            * Session Storage &gt; (website) &gt; ContextHubPersistence
            * Cookies &gt; (website) &gt; SessionPersistence

    * Safari:

        * Open Preferences &gt; Advanced &gt; Show Develop menu in menu bar
        * Open Develop &gt; Show JavaScript Console

            * Console &gt; Storage &gt; Local Storage &gt; (website) &gt; ContextHubPersistence
            * Console &gt; Storage &gt; Session Storage &gt; (website) &gt; ContextHubPersistence
            * Console &gt; Storage &gt; Cookies &gt; (website) &gt; ContextHubPersistence

    * Internet Explorer:

        * Open Developer Tools &gt; Console

            * `localStorage.getItem('ContextHubPersistence')`
            * `sessionStorage.getItem('ContextHubPersistence')`
            * `document.cookie`

* Use the ContextHub API, in the browser's console:

    * ContextHub provides following data persistence layers:

        * `ContextHub.Utils.Persistence.Modes.LOCAL` (default)
        * `ContextHub.Utils.Persistence.Modes.SESSION`
        * `ContextHub.Utils.Persistence.Modes.COOKIE`
        * `ContextHub.Utils.Persistence.Modes.WINDOW`

      The ContextHub store defines which persistence layer is used, thus to view the current state of the persistence all layers should be checked.

For example, to view data stored in localStorage:

To preview persistance used ContextHub, a user can:

* Use the browser's console:

    * Chrome - open Developer Tools &gt; Application &gt; Storage:

        * Local Storage &gt; (website) &gt; ContextHubPersistence
        * Session Storage &gt; (website) &gt; ContextHubPersistence
        * Cookies &gt; (website) &gt; SessionPersistence

    * Firefox - open Developer Tools &gt; Storage:

        * Local Storage &gt; (website) &gt; ContextHubPersistence
        * Session Storage &gt; (website) &gt; ContextHubPersistence
        * Cookies &gt; (website) &gt; SessionPersistence

* Use the ContextHub API, in the browser's console:

    * ContextHub provides following data persistence layers:

        * `ContextHub.Utils.Persistence.Modes.LOCAL` (default)
        * `ContextHub.Utils.Persistence.Modes.SESSION`
        * `ContextHub.Utils.Persistence.Modes.COOKIE`
        * `ContextHub.Utils.Persistence.Modes.WINDOW`

      The ContextHub store defines which persistence layer is used, thus to view the current state of the persistence all layers should be checked.

For example, to view data stored in localStorage:

```
var storage = new ContextHub.Utils.Persistence({ mode: ContextHub.Utils.Persistence.Modes.LOCAL });
console.log(storage.getTree());
```

### Clearing Persistence of ContextHub {#clearing-persistence-of-contexthub}

To clear the ContextHub persistence:

* To clear persistence of currently loaded stores:

  ```
  // to be able to fully access persistence layer, Opt-Out must be turned off
  ContextHub.Utils.Cookie.removeItem('cq-opt-out');

  // following call asks all currently loaded stores to clear their data
  ContextHub.cleanAllStores();

  // following call asks all currently loaded stores to set back default values (provided in their configs)
  ContextHub.resetAllStores();

  ```

* To clear a specific persistence layer; for example, sessionStorage:

  ```
  var storage = new ContextHub.Utils.Persistence({ mode: ContextHub.Utils.Persistence.Modes.SESSION });
  storage.setItem('/store', null);
  storage.setItem('/_', null);

  // to confirm that nothing is stored:
  console.log(storage.getTree());
  ```

* To clear all ContextHub persistence layers, the appropriate code must be called for all layers:

    * `ContextHub.Utils.Persistence.Modes.LOCAL` (default)
    * `ContextHub.Utils.Persistence.Modes.SESSION`
    * `ContextHub.Utils.Persistence.Modes.COOKIE`
    * `ContextHub.Utils.Persistence.Modes.WINDOW`
