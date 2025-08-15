---
title: Contextual Experimentation in AEM as a Cloud Service
description: Learn how to use the experimentation plugin  to add a experimentation capabilities to your sites.
feature: Administering
role: Admin
---

# Overview {#overview}

Experimentation is the practice of making your site more effective by changing content or functionality, comparing the results with the prior version, and picking the improvements that have measurable effects.

When done right, it is a powerful pattern to improve conversions, engagement, and visitor experience. There are three main pitfalls to avoid when looking to adopt the practice:

* Too little: most companies are not experimenting enough, and when they do, they experiment with too little traffic to get meaningful results.
* Too slow: many experimentation frameworks slow the site down so much that the potential new conversions can’t make up for the lost traffic and bounces due to slow rendering
* Too complex: if it takes too much time to set up a new experiment, then fewer experiments will be run.

For sites running on Adobe Experience Manager, there is the **experimentation plugin** that allows developers to add an experimentation capability to their sites. Three things make this approach different:

* It’s easy to set up tests in the tools your authors are already familiar with, no separate login is needed
* It’s deeply integrated into the AEM delivery system, does not slow down your site and is resilient to changes in code and content
* It allows testing simple content changes as well as experiments covering design, functionality, and code

Follow the rest of this guide to set up your first experiment. There are a few terms that you will find used repeatedly:

* Control: the experience prior to running the experiment. Any experiment tries to prove an improvement over the control experience.
* Challenger: an experience that differs from the control experience and that may or may not have better results such as conversions
* Variants: control and challenger are all variants of an experiment
* Significance: is your challenger really better than the control or is this just luck? Calculating significance allows you to rule out luck and concentrate on results that have a real effect

## Setting up your experiment {#setting-up-experiment}

TBD intro text here. ADD VIDEO WITH INTRO SETUP

### Experiment variants {#experiment-variants}

Experiment variants are the easiest way to get started with experimentation. This approach uses the page you already have as the control, you then create a challenger page that will replace the control for some of your visitors. In your challenger page, you can test different variants of your hero blocks, different page layout or call-to-action (CTA) placements and verbiage.

As long as you stay within the established design language of your website and use existing block functionality you should be able to set up an experiment variant and send it to production in a matter of a few minutes using your established authoring tools.

### Experiment Identifier {#experiment-identifier}

Every experiment should have its own identifier for tracking and analytics purposes.
A good starting point is to come up with a good, unique identifier for your experiment, called the “Experiment ID”.
Experiments are often numbered linearly or correlated to their Issue ID in an issue tracker or management system that is used. Experiment IDs often use a prefix for the project. Examples are OPT-0134, EXP0004 or CCX0076.

### Create your Challenger Page {#create-challenger-page}

By convention it is recommended to create a folder with a lowercase experiment ID in your /experiments/ folder (for example /experiments/ccx0076/) which is where all the pages for your challenger variants live.

Your experiments folder will look something like this:

FIG 1

Once the folder has been created, put a copy of your control page into that folder, and apply the changes on the page that you would like to test as part of your experiment variant. As an example let’s assume we have the following page on the website that we want to run an experiment on.

FIG 2

Your copy of the challenger placed in the experiments/<experiment-id> folder might look like this:

FIG 3

Preview and publish the challenger page using the sidekick and when you are done authoring the challenger page, the URL of the published challenger will be used in the next section - setting up the experiment.

### Configure your experiment {#configure-experiment}

As soon as you have your challengers ready to go, all you need to do is to go back to the control page and add some metadata indicating that this page is now part of a test.

There are two metadata rows that need to be added for an experiment variant.

Experiment : containing your experiment ID

Experiment Variants: containing URLs for all the challengers of this page, separated by line breaks if you have more than one challenger

See example below:

FIG 4

For an experiment variant the traffic split between all the variants (control + challengers) is automatically set to an even distribution. If you have one challenger, there will automatically be an even 50/50 split between control and the challenger. If you have 2 challengers, you will automatically see a third of the traffic allocated to control and each challenger and so on.

You can override the traffic split via metadata. For more information, see the following [page](https://github.com/adobe/aem-experience-decisioning/wiki/Experiments#authoring)

### Preview and Stage your Experiment Variants {#preview-stage-experiment}

As soon as you are ready to preview and stage your experiment you can preview the control page with the additional metadata. Whenever you are previewing a page that has a running experiment, you will see the experimentation overlay in your .hlx.page preview environment that lets you switch between the variants and gives you confidence that your test is setup correctly and ready to be launched.

FIG 5

Authors can get quick insights on the performance of experiments being run on the production site. These insights are helpful in making a decision about the duration of the experiment, but also about which variant is best suited for production.

The data collection to measure the effectiveness of each variant is based on Real User Monitoring (CHANGE LINK).

### Send your Experiment Variant to Production {#production-experiment}

To send your experiment to production and collect data about the performance of each variant, the only step left is to publish the control page as well as each of the challenger pages.

## Use Case Examples {#use-case-examples}

INTRO TBD

### Engagement versus Conversion {#engagement-conversion}

Experiments can be set-up to address Conversion (tracks clickable elements on your page) or Engagement (tracks time on page and/or scrolling activity). 

All experiments must be defined for the following:

* Experiment type
* What experience block the experiment will apply to
* How many variants will the experiment contain
* What is the composition of each variant

### Make sure Experiment Variants are not indexed {#experiment-not-indexed}

When running experiments, it is usually best practice to exclude the variants from the sitemap and ensure they are not indexed by search engines, as the page could be seen as duplicate content and negatively impact SEO.

This can be achieved by either of the following 2 methods:

* If you centralize all experiments in a dedicated folder, like /experiments: make sure your bulk metadata.xlsx sheet contains a row with /experiments/** as path, and a robots column with the value noindex, nofollow.
* If you keep the experiment control and variants with the regular content: add a robots entry in the page metadata for each variant, with the value noindex, nofollow.

## Developer and Technical Resources {#dev-resources}

Adobe Experience Manager uses Operational Telemetry to gather operations data that is strictly necessary to discover and fix functional and performance issues on Adobe Experience Manager-powered sites. Operational Telemetry data can be used to diagnose performance issues. Operational Telemetry preserves the privacy of visitors through sampling LINK TBD (only a small portion of all page views will be monitored).

### Privacy {#privacy-experimentation}

Operational Telemetry in Adobe Experience Manager is designed to preserve visitor privacy and minimize data collection. As a visitor, this means that Adobe will not attempt to collect personal information about you or information that can be tracked back to you. As a site operator, review the data items collected below to understand if they require consent.
AEM Operational Telemetry does not use any client-side state or ID, such as cookies or localStorage, sessionStorage or similar, to collect usage metrics. Data is submitted transparently through a Navigator.sendBeacon call, not through pixels or similar techniques. There is no “fingerprinting” of devices or individuals via their IP address, User Agent string, or any other data for the purpose of capturing sampled data.

It is not permitted to add any personal data into the Operational Telemetry data collection nor may Operational Telemetry data be used for use cases that go beyond strictly necessary.

TELEMETRY LINK TBD
