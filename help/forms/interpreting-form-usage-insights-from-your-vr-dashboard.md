---
title: Interpreting Form Usage insights using the Value Realization Dashboard
description: Learn how to use the Forms Usage Insights dashboard to monitor and understand the performance of your forms and form fragments.
role: User, Developer
level: Intermediate
feature: Adaptive Forms, Foundation Components, Core Components
hide: yes
hidefromtoc: yes
exl-id: c57e548b-a254-4fe8-82e2-762ec1a81cfd
---
# Interpreting Forms Usage insights using the Value Realization dashboard

<span class="preview"> This feature is available through the early access program. To request access, send an email from your official address to aem-forms-ea@adobe.com. <span>

![Value realization dashboard](/help/edge/docs/forms/universal-editor/assets/forms-insights-banner.svg)


By regularly monitoring the metrics presented in the "Forms Usage Insights" dashboard, you can gain valuable insights into the performance of your forms, documents, and form fragments. Use this data to make informed decisions about form design, fragment management, and overall form strategy.

This article provides detailed usage instructions and metrics interpretation for the Value Realization Dashboard. For a conceptual overview and benefits of the dashboard, see [Understanding your value realization dashboard](/help/forms/aem-forms-value-realization-dashboard.md).


## Accessing the usage insights dashboard

To access the Forms Usage Insights dashboard:

1. Navigate to the **Forms** > **Forms and Documents** 
1. Click **Insights Dashboard**. The dashboard opens in a new window. 

![Value realization dashboard](/help/forms/assets/forms-usage-insights.png)

## Overview

The dashboard consists of two main sections:

- **Form & Documents activity over time:** This section provides insights into the usage and evolution of your forms over a selected period.
- **Fragment usage:** This section allows you to monitor the adoption and reuse of form fragments.

## Form & Documents activity over time

This section contains four charts, each tracking a different aspect of form activity. All charts share the same structure:

- **Chart Type:** Line Chart & Bar Chart
- **X-axis:** Date (showing daily activity)
- **Y-axis:** Count (representing the number of occurrences of the tracked activity)
- **Time Period:** Adjustable via a dropdown menu (options: "Last 30 days", "Last 12 months")




### Form Submissions

- **Purpose:** This chart displays the number of times forms have been successfully submitted over the selected time period.

    ![Forms Submissions Chart](/help/forms/assets/forms-submissions-vr-dashboard-form-insights.png)
- **Information to Extract:**
    - **Trend Analysis:** Observe the overall trend of form submissions. Is the number increasing, decreasing, or staying relatively constant?
    - **Peak Periods:** Identify days or periods with unusually high submission rates. Investigate the possible reasons for these spikes (e.g., marketing campaigns, specific events).
    - **Low Activity Periods:** Identify periods with low submission rates and investigate potential causes (e.g., form downtime, usability issues).
    - **Comparative Analysis:** Compare submission rates across different time periods (e.g., the last 30 days versus the previous 30 days) to assess performance changes.

### Document Renditions

- **Purpose:** This chart tracks the number of documents generated as a result of form submissions. This is relevant if your forms trigger the creation of documents (e.g., contracts, reports).

    ![Document Rendetions Chart](/help/forms/assets/document-rendetions-vr-dashboard-form-insights.png)


- **Information to Extract:**
    - **Correlation with Form Submissions:** Compare the trend of document renditions with the trend of form submissions. Ideally, these should correlate closely. Discrepancies may indicate issues with the document generation process.
    - **Volume of Document Generation:** Assess the overall volume of documents being generated to understand the workload on your document generation system.

### Forms Created


- **Purpose:** This chart displays the number of new forms created within the selected time period.

    ![Forms Created Chart](/help/forms/assets/forms-created-vr-dashboard-form-insights.png)

- **Information to Extract:**
    - **Form Creation Rate:** Track the rate at which new forms are being created. This provides insights into the demand for new forms within the organization.
    - **Spikes in Creation:** Identify periods with unusually high form creation activity. This may indicate specific projects or initiatives that require new forms.

### Forms Published

- **Purpose:** This chart tracks the number of forms that have been published (made available for use) within the selected time period.

    ![Forms Published Chart](/help/forms/assets/forms-publish-vr-dashboard-form-insights.png)


- **Information to Extract:**
    - **Form Deployment Rate:** Monitor the rate at which new forms are being deployed to users.
    - **Lag between Creation and Publication:** Analyze the time difference between the "Forms Created" chart and the "Forms Published" chart. A significant delay may indicate bottlenecks in the form approval or deployment process.

## Fragment Usage

This section provides insights into the usage of form fragments, which are reusable components that can be incorporated into multiple forms.

![Forms Published Chart](/help/forms/assets/fragment-usage-vr-dashboard-form-insights.png)

### Number of Form Fragments in Use

- **Chart Type:** Numerical Display (showing a single value)
- **Purpose:** This displays the total number of unique form fragments that are currently being used in active forms.
- **Information to Extract:**
    - **Fragment Adoption:** Assess the overall adoption of form fragments within the organization. A higher number indicates greater use of reusable components.

### Form Fragment Re-use

- **Chart Type:** Numerical Display (showing a single value)
- **Purpose:** This displays the total number of times form fragments have been reused across different forms. This metric indicates how effectively fragments are being leveraged to avoid duplication and maintain consistency.
- **Information to Extract:**
    - **Fragment Reuse Rate:** Monitor the rate at which existing fragments are being reused in new forms. A higher number indicates better leveraging of reusable components and improved efficiency.

## Example Scenarios

- **Scenario:** You notice a sudden drop in "Form Submissions."
    - **Action:** Investigate potential causes such as form downtime, usability issues, or a decline in traffic to the form's landing page.
- **Scenario:** The "Form Fragment Re-use" value is low.
    - **Action:** Promote the benefits of using form fragments to your team, ensure that fragments are well-organized and easy to find, and provide training on how to create and reuse fragments effectively.
- **Scenario:** There's a significant lag between "Forms Created" and "Forms Published."
    - **Action:** Review your form approval and deployment process to identify and eliminate bottlenecks.



## See also

- [Understanding your value realization dashboard](/help/forms/aem-forms-value-realization-dashboard.md)
