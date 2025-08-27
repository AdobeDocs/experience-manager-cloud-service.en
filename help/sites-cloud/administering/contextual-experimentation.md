---
title: Contextual Experimentation in AEM as a Cloud Service
description: Learn how to use the experimentation plugin  to add a experimentation capabilities to your sites.
feature: Administering
role: Admin
---

# Overview {#overview}

>[!NOTE]
>Currently, the contextual experimentation feature is available only through the beta program. Please contact either Adobe support or your account manager for access to the beta program. (EDS??)

Experimentation is the practice of testing your site’s design, functionality and code in order to improve performance and make your site more effective and streamlined. This is achieved by changing either content or functionality, comparing the results with a prior version and picking the improvements that have measurable effects.

When done right, it is a powerful pattern to improve conversions, engagement and visitor experience. In general, there are a couple of issues to avoid when looking to adopt the practice:

* **Too little**: most companies are not experimenting enough, and when they do, they experiment with too little traffic to get meaningful results.
* **Too slow**: many experimentation frameworks slow the site down so much that the potential new conversions can’t make up for the lost traffic and bounces due to slow rendering.
* **Too complex**: if it takes too much time to set up a new experiment, then fewer experiments will be run.

For sites running on Adobe Experience Manager, there is the "out of the box" **experimentation plugin** that allows developers to add an experimentation capability to their sites. Three things make this approach different from other experimentation frameworks:

* It is easy to set up tests with the tools your authors are already familiar with and no separate login is needed.
* It is deeply integrated into the AEM delivery system, does not slow down your site and is resilient to changes in code and content.
* It allows the testing of simple content changes as well as experiments covering design, functionality, and code.

## Before you start {#before-start}

The experimentation plug-in is used within the context of [Edge Delivery Services](/help/edge/overview.md) so you will need a Github account, a content repository like SharePoint or Google Drive, and also you will need the [AEM Sidekick](https://www.aem.live/docs/sidekick). See also the [Getting Started – Universal Editor Developer Tutorial page](https://www.aem.live/developer/tutorial) and [Getting Started – Developer Tutorial](https://www.aem.live/developer/tutorial).

After you have everything set up, **please watch this video** titled [Instant experimentation](https://business.adobe.com/products/experience-manager/sites/testing-optimization.html) for a short demonstration on how the experimentation plug-in works.

## Frequently used terms {#frequently-used-terms}

Before following the rest of the guide to set up your first experiment, there are a few frequently used terms that you should be familiar with:

* **Control**: the experience prior to running the experiment. All experiments try to test and demonstrate an improvement over the control experience.
* **Challenger**: an experience that is different from the control experience and is "tested" against it or alongside it.
* **Variants**: control and challenger are all variants of an experiment.
* **Significance**: Evaluating if your challenger is really better than the control. Calculating statistical significance allows you to rule out luck and concentrate on the results that have a real effect.

## Experiment variants and general workflow {#experiment-variants-workflow}

Generally speaking, when setting up an experiment you will use a pre-existing page as the control page. You will then create a challenger page that will replace the control page for some of your visitors. In the challenger page, you can test different things like content variants, different page layouts, call-to-action (CTA) and so on. You can configure these experiment variants by adding metadata parameters in the control page (see below).

The [Operational Telemetry service](/help/sites-cloud/administering/operational-telemetry-for-aem-as-a-cloud-service.md) then gathers data, for example, the number of visitors in the control page versus the challenger page. You then use this data to pick the necessary improvements for your site. As long as you stay within the established design language of your website and use the existing block functionality you should be able to set up an experiment variant and send it to production in a matter of minutes.

>[!NOTE]
>Keep in mind that the plug-in doesn't use any, nor persists any, end-user data that could lead to their identification. No end-user opt-in nor cookie consent is required when using the default configuration that uses the AEM The [Operational Telemetry service in AEM as a Cloud Service](/help/sites-cloud/administering/operational-telemetry-for-aem-as-a-cloud-service.md) .

### Experiment Identifier {#experiment-identifier}

Before you start, every experiment should have its own identifier for tracking and analytics purposes. A good starting point is to come up with a good, unique identifier for your experiment which will be the “Experiment ID”. Experiments are often numbered linearly or correlated to their Issue ID in an issue tracker or management system. Experiment IDs often use a prefix for the project, for example: OPT-0134, EXP0004 or CCX0076.

### Create your Challenger Page {#create-challenger-page}

By convention, it is recommended to create a folder with a lowercase experiment ID in your `/experiments/ folder` (for example /experiments/ccx0076/). All the pages for the challenger variants are located in this folder. You create this folder in your local repository, for example, Sharepoint or Goggle Drive.

Your experiments folder should look something like this:

![experiments-folder](/assets/experiments-folder.png)

Once the folder is created, put a copy of your control page into that folder, and apply the changes on the page that you would like to test as part of your experiment variant (see video above). As an example let’s assume we have the following page on the website that we want to run an experiment on:

![control-page](/assets/control-page.png)

Your copy of the challenger placed in the `experiments/<experiment-id>` folder might look like this:

![challenger-page](/assets/challenger-page.png)

Preview and publish the challenger page using the sidekick and when you are done authoring the challenger page. The URL of the published challenger will be used in the next section - configuring the experiment.

### Configuring the experiment {#configure-experiment}

As soon as the challenger pages are ready to go, you need to go back to the control page and add metadata indicating that the page(s) are now part of the test.

There are two metadata rows that need to be added for an experiment variant.

* **Experiment**: containing your experiment ID.

* **Experiment Variants**: containing URLs for all the challengers of this page, separated by line breaks if you have more than one challenger.

See the example below:

![metadata-page](/assets/metadata-page.png)

For each experiment, the traffic is split between all the variants (control and challengers) and is automatically set to an even distribution. As such, if you have one challenger, there will automatically be an even 50/50 split between control and the challenger. If you have two challengers, you will automatically see a third of the traffic allocated to control and each challenger and so on.

You can override the traffic split by configuring the metadata. For more information on how you can customize the metadata used in your experiments, see the following [page](https://github.com/adobe/aem-experience-decisioning/wiki/Experiments#authoring)

### Preview and Stage your Experiment Variants {#preview-stage-experiment}

As soon as you are ready to preview and stage your experiment, click Preview from the side-kick in the upper left side. Whenever you are previewing a page that has a running experiment, you will see the experimentation overlay in your `.hlx.page` preview environment. The experimentation overlay lets you switch between the experiment variants and also provides traffic data.

![experimentation-overlay](/assets/experimentation-overlay.png)

By using the experimentation overlay, authors can get quick insights on the performance of experiments being run on the production site. These insights are helpful in making a decision about the duration of the experiment, but also about which variant is best suited for production.

The data collection to measure the effectiveness of each variant is based on the [Operational Telemetry service](/help/sites-cloud/administering/operational-telemetry-for-aem-as-a-cloud-service.md).

### Send your Experiment Variant to Production {#production-experiment}

Select the experiment pages and click Publish from the side-kick to push both the control and the challenger variant(s) live.

### Use Case Examples {#use-case-examples}

Presented below are several use case examples for experiment variants. Generally speaking, the basic worklflow will be similar to the one described above, with particular changes for each use case (like the number of challenger pages or metadata changes).

#### Full Page Experiment {#full-page}

You use a full page experiment to test between two variants of the same page. This is a full page variant of an a/b test where you have a control and a challenger page. You will replace the whole content of the "original" control page in the challenger variant with a different type of content. Keep in mind that by default the customer traffic is split evenly (50/50), but you can create custom splits if you like. The metadata on the control page should look like this:

METADATA SETUP

#### Sections of the page Experiment {#sections-of-the-page}

This is experiment is similar to the full page one presented above but now the a/b test will contain changes to a section of the page instead of the whole content. For example, you can modify and test a carousel element, the call to action element and so on. As such, you will have a control and a challenger page, with the challenger page containing the modified elements. The metadata on the control page should look like this:

METADATA SETUP

#### Multi-path Experiment {#multi-path}

By leveraging the experimentation plug-in, you can set up a/b tests on several pages of your website at once. For example, on all product pages, photo galleries, all blog posts and so on.

The configuration logic is the same as above - you will create a control page and one or more challenger variants of that page. What changes in the multi-page use-case, is the following:

• You will create multiple control pages each with one or more variants.
• The control pages must have the same experiment ID in metadata field.

For example: We have 5 different production pages for which we need to set up an a/b test. We create 5 control pages (as detailed in the chapters above) and 5 (or more) challenger variants.

We then create an experiment ID, let’s say `prod-exp` and add this ID in the experiment metadata field for each control page. This basically means that all pages with the same ID are now “grouped”. We then assign the challenger variants for each control page, taking care to sequence them properly in case we have more than one variant for each control.

The metadata on the control page should look like this:

METADATA SETUP

#### Code-level experiments {#code-level}

Note that the examples above assume you have different content variants to serve, but if you want to run a pure code-based a/b test, this is achievable via:

Metadata

Experiment    Hero Test
Experiment Variants    2

This will create just two variants, without touching the content, and you'll be able to target those based on the `experiment-hero-test` and `variant-control/variant-challenger-1/variant-challenger-`2 CSS classes that will be set on the `<body>` element.

#### Browser based audience experiment {#browser-based}

You can create browser based experiments, where you deliver separate challenger pages depending on the browser used. You can, for example, serve a different challenger page to a Firefox user as opposed to a Chrome user. This is achieved by leveraging the audience parameter.

Once you configure the experiment, the target audience will be evaluated based on the context of the browser (client side) and limited to the browser APIs available. As such, you do not need to use server side third-party systems or customer profile data for your experiment.

Before you start authoring this experiment variant, the audience parameter needs to be defined in the project codebase. For more details, see ee the following [page](https://github.com/adobe/aem-experience-decisioning/wiki/Experiments#authoring).

Once the audiences have been defined you are ready to author the experiment. As stated previously, let’s say you want to create a Firefox versus Chrome experiment where you will serve different pages depending on the browser.

You need two different challenger pages, so set up the experiment as follows:

1.Duplicate the Control page by right-clicking and copying it to the experiment folder. You need to copies, one for Firefox and one for Chrome.
2.Rename the copies. Give them specific names like “page-for-firefox”.
3.Change the content of the pages depending on what you need to serve on Firefox versus Chrome.
4.Change the metadata as explained in the section below.
5.Click Preview from the side-kick in the upper left side, to preview the changes.

The most important part when authoring this experiment is to change the metadata in the control page. Let’s say you defined the browser audiences in the codebase as: Audience: Firefox and Audience: Chrome. You need to edit the control page and add these audiences and point to the appropriate challenge page you set up previously. It should look similar to this:

Metadata
Title Control Page
Description This is the control page.
Experiment ExpBrowser
Experiment Variants `https://{ref}--{repo}--{org}.hlx.page/my-page-for-firefox https://{ref}--{repo}--{org}.hlx.page/my-page-for-chrome`
Audience: Firefox `https://{ref}--{repo}--{org}.hlx.page/page-for-firefox`
Audience: Chrome `https://{ref}--{repo}--{org}.hlx.page/page-for-chrome`

After this configuration, the users will be triaged based on the browser they connect with and the appropriate challenger page will be served.

Please keep in mind that the names above are only for illustration purposes. You can define the Audiences parameter and the challenger pages according to your needs, for example: Audience (Firefox) or Audience Firefox.

## Other Considerations {#other-considerations}

Presented below are several other aspects you should consider when using context experimentation.

### Engagement versus Conversion {#engagement-conversion}

Experiments can be set-up to address conversion (tracks clickable elements on your page) or engagement (tracks time on page and/or scrolling activity).

All experiments must be defined for the following:

* Experiment type
* What experience block the experiment will apply to
* How many variants will the experiment contain
* What is the composition of each variant

### Make sure Experiment Variants are not indexed {#experiment-not-indexed}

When running experiments, it is usually best practice to exclude the variants from the sitemap and ensure they are not indexed by search engines. This is because the variant page could be seen as duplicate content and negatively impact SEO.

You can do this by using either of the following two methods:

* If you centralize all experiments in a dedicated folder, like `/experiments`: make sure your bulk `metadata.xlsx` sheet contains a row with `/experiments/**` as path, and a robots column with the values `noindex`, `nofollow`.
* If you keep the experiment control and variants with the regular content: add a robots entry in the page metadata for each variant, with the value `noindex`, `nofollow`.

## Developer and Technical Resources {#dev-resources}

Adobe Experience Manager uses Operational Telemetry to gather operations data that is strictly necessary to discover and fix functional and performance issues on Adobe Experience Manager-powered sites. Operational Telemetry data can be used to diagnose performance issues. Operational Telemetry preserves the privacy of visitors through sampling LINK TBD (only a small portion of all page views will be monitored).

### Privacy {#privacy-experimentation}

[Operational Telemetry service in AEM as a Cloud Service](/help/sites-cloud/administering/operational-telemetry-for-aem-as-a-cloud-service.md) is designed to preserve visitor privacy and minimize data collection. As a visitor, this means that Adobe will not attempt to collect personal information about you or information that can be tracked back to you. As a site operator, review the data items collected below to understand if they require consent.
AEM Operational Telemetry does not use any client-side state or ID, such as cookies or `localStorage`, `sessionStorage` or similar, to collect usage metrics. Data is submitted transparently through a `Navigator.sendBeacon` call, not through pixels or similar techniques. There is no “fingerprinting” of devices or individuals via their IP address, User Agent string, or any other data for the purpose of capturing sampled data.

It is not permitted to add any personal data into the Operational Telemetry data collection nor may Operational Telemetry data be used for use cases that go beyond strictly necessary.

### FAQ {#faq}

TBD
