---
title: Real Use Monitoring (RUM) for Edge Delivery Services for AEM Forms as a Cloud Service
description: Real Use Monitoring (RUM) for Edge Delivery Services for AEM Forms as a Cloud Service involves the ongoing tracking and analysis of user interactions with forms.
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
role: Admin, Architect, Developer
exl-id: 184fc7dc-d583-4a63-9e30-80d324ec9d7e
---
# Real Use Monitoring (RUM) for Edge Delivery Services for AEM Forms as a Cloud Service

Real Use Monitoring (RUM) empowers you to gain real-world insights into how visitors interact with your Adobe Experience Manager (AEM) websites. This built-in tool provides valuable data to understand user behavior, diagnose performance issues, and measure the effectiveness of website experiments. RUM goes beyond synthetic testing by capturing Real Use interactions, offering a more accurate picture of your site's performance.

However, RUM prioritizes visitor privacy. It utilizes sampling techniques to collect data from a representative subset of users, ensuring no personally identifiable information (PII) is ever captured. Additionally, RUM is designed with data minimization in mind, collecting only the essential metrics required for performance analysis. This approach allows you to optimize your AEM sites while maintaining user trust.


## Pre-requisites

You can view the monitoring dashboard for Edge Delivery Services for AEM Forms as a Cloud Service by accessing the following URL:

https://data.aem.live/?ext=forms

![RUM Login Screen for Edge Delivery Services for Forms](/help/edge/assets/rum-login-screen.png)

To log in to the monitoring dashboard for Edge Delivery Services for AEM Forms as a Cloud Service, enter the following:

* **URL**: The URL is specific to user site or domain. The users have the option to filter the site or domain to view the dashboard as per their requirements.

* **Domain Key**: The user manually generates the domain key. To obtain domain keys for your  forms, contact your Adobe representative. 

### Monitoring dashboard for Edge Delivery Services for AEM Forms as a Cloud Service

After entering the URL and domain keys into the login screen, you gain access to the monitoring dashboard for Edge Delivery Services for AEM Forms as a Cloud Service.

The below illustration demonstrates the dashboard for Edge Delivery Services for AEM Forms as a Cloud Service:

![RUM Forms Dashboard](/help/edge/assets/rum-forms-dashboard.png)

### Different key metrics of dashboard for Forms {#different-metrics-rum-dashboard-forms}

This dashboard provides key insights into how visitors interact with forms on your Adobe Experience Manager (AEM) website. By monitoring these metrics, you can identify areas for improvement and optimize your forms for better user experience and conversion rates:

* **Form Views**: Track the total number of times forms are displayed 
* **Form Submissions**: Track the  total number of completed submissions 

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

## Actionable Insights

By analyzing these metrics, you can identify opportunities to:

* Simplify forms and reduce the number of fields.
* Improve form clarity with clear instructions and labels.
* Optimize form layout for mobile responsiveness.
* Address technical issues that slow down form loading.

By focusing on these areas, you can create forms that are easier to use and encourage visitors to complete them, ultimately leading to higher conversion rates.

## See also

{{see-more-forms-eds}}
