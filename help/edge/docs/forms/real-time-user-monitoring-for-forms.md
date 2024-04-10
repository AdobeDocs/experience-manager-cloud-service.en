---
title: Real time user monitoring for Edge Delivery Services Forms
description: Real-time user monitoring for Edge Delivery Services Forms involves the ongoing tracking and analysis of user interactions with forms.
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
exl-id: 184fc7dc-d583-4a63-9e30-80d324ec9d7e
---
# Real time user monitoring for Edge Delivery Services Forms

Adobe Experience Manager uses Real User Monitoring (RUM) to understand visitor interactions with Adobe Experience Manager-driven sites. It helps in diagnosing the performance challenges, and gauging experiment effectiveness. Real User Monitoring maintains the visitor privacy by using the sampling techniques, ensuring that no personal information is collected by the sites you are visiting. It is not permitted to add personal data to the RUM data collection. Real User Monitoring in Adobe Experience Manager is designed to preserve visitor privacy and minimize data collection.

## Advantages of using Real time user monitoring for Edge Delivery Services Forms {#advantages} 

AEM uses real time user monitoring for the following:

* To identify and fix performance bottlenecks on sites.
* To estimate the number of page views to customer sites
* To comprehend the interaction of Adobe Experience Manager with analytics, targeting, or external libraries on the same page, enhancing compatibility..

## Pre-requisites

You can view the real-time user monitoring dashboard for Edge Delivery Services Forms by accessing the following URL:
https://data.aem.live/?ext=forms

![RUM Login Screen for Edge Delivery Services Forms ](/help/edge/assets/rum-login-screen.png)

To log in to your real-time user monitoring dashboard for Edge Delivery Services Forms, enter the following:
* **URL**: The URL is specific to user site or domain. The users have the option to filter the site or domain to view the dashboard as per their requirements.
* **Domain Key**: The user manually generates the domain key. For assistance or inquiries, refer to the [Generate RUM Domain Key](https://aemcs-workspace.adobe.com/rum/generate-domain-key) documentation.

### Real time user monitoring dashboard for Edge Delivery Services Forms

After entering the URL and Domain key into the login screen, you gain access to the real time user monitoring dashboard for Edge Delivery Services Forms.

The below illustration demonstrates the RUM dashboard for Edge Delivery Services Forms:

![RUM Forms Dashboard](/help/edge/assets/rum-forms-dashboard.png)

### Different key metrics of RUM dashboard for Forms {#different-metrics-rum-dashboard-forms}

You can assess visitor interactions with Adobe Experience Manager-driven sites using the following key metrics:

* **Formviews**: It is the total number of forms rendered for a URL within the specified date range.
* **Formsubmission**: It is the total number of forms submitted for a URL within the specified date range.
* **Largest Contentful Paint**: It shows the speed at which the URL loads, indicating the time taken to render the largest content element visible in the viewport from the moment the user requests the URL. This largest content element could be an image, video, or a substantial block-level text element. The performance ratings for URL loading speed are categorized as follows:
    * **Good**: If the loading time is 2.5 seconds or less.
    * **Okay**: If the loading time is more than 2.5 seconds but 4 seconds or less.
    * **Bad**: If the loading time exceeds 4 seconds

* **Cumulative Layout Shift**: It measures the total sum of all individual layout shift scores for each unexpected layout shift that occurs throughout the entire lifespan of the page. It plays a crucial role in identifying the performance of a page because when page elements shift while a user is trying to interact with them, it leads to a poor user experience. This score ranges from zero to any positive number: zero indicates no shifting, while a higher number signifies more layout shifts on the page. The performance metrics used to assess the layout shift scores are categorized as follows:
   
  * **Good**: If the layout shift score is 0.1 or less.
  * **Okay**: If the layout shift score is greater than 0.1 but 0.25 or less.
  * **Bad**: If the layout shift score exceeds 0.25.

* **Interaction to Next Paint**:  It evaluates how quickly a page reacts to user interactions, considering the time it takes for the page to respond to clicks, taps, and keyboard inputs during a user's visit to the page. The final value is the longest interaction observed, disregarding any anomalies. The performance metrics for Interaction to Next Paint are categorized as follows:
    * **Good**: If the duration between user actions is 200 milliseconds (ms) or less.
    * **Okay**: If the duration is more than 200 ms but 500 ms or less.
    * **Bad**: If the duration exceeds 500 ms.
