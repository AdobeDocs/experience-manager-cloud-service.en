---
title: Readiness Phase in Cloud Acceleration Manager
description: This page provides an overview on the Readiness phase in Cloud Acceleration Manager.
exl-id: 2583985b-0358-433c-9d31-38e2c60dc3dc
feature: Migration
role: Admin
---
# Readiness Phase in Cloud Acceleration Manager {#readiness-phase-cam}

Once you have created a project in Cloud Acceleration Manager (CAM), you can now start the assessment of your current Adobe Experience Manager (AEM) implementation in the Readiness phase.

The Readiness Phase includes:

* [Best Practices Analysis](#best-practices-analysis)
* [Planning and Setup](#planning-setup) 

Follow the steps below to navigate to the Readiness Phase:

1. Click your project card.

   ![Project card](/help/journey-migration/cloud-acceleration-manager/assets/cam-landing1.png)

1. On the project landing page, navigate to the **Readiness** section, as shown in the figure below.

   ![Readiness](/help/journey-migration/cloud-acceleration-manager/assets/readiness-1.png)

   >[!NOTE]
   >See Creating and Managing a Project in Cloud Acceleration Manager to learn more.

## Using Best Practices Analysis Card {#best-practices-analysis}

>[!CONTEXTUALHELP]
>id="aemcloud_cam_bpa"
>title="Best Practices Analysis report"
>abstract="The BPA report can be uploaded to CAM to provide an analysis of it with respect to migration to AEM as a Cloud Service."
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/best-practices-analyzer/using-best-practices-analyzer" text="Using Best Practices Analyzer"

1. Click **Review** from the **Best Practices Analysis** card. 

   ![Best Practices Analysis - Review](/help/journey-migration/cloud-acceleration-manager/assets/readiness-2.png)

1. Download Best Practices Analyzer (BPA).

   >[!NOTE]
   >To avoid an impact on business critical instances, Adobe recommends that you run BPA on an Author environment. The environment should be as close as possible to the Production environment in the areas of customizations, configurations, content, and user applications. Alternatively, it can be run on a clone of the production Author environment.

   1. Navigate to the [Software Distribution](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html?fulltext=best*) portal and download the Best Practices Analyzer as a zip file.

      >[!NOTE]
      >Review [Using Best Practices Analyzer](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/best-practices-analyzer/using-best-practices-analyzer.html#imp-considerations) to learn how to run BPA.

1. In CAM, click **Get upload key**, so you can get the key used to configure your system to automatically upload BPA reports directly to CAM.

   ![Get upload key](/help/journey-migration/cloud-acceleration-manager/assets/readiness-3b.png)
   
   >[!IMPORTANT]
   >The report can still be uploaded manually, but using the Upload Key streamlines the operation. Note that the report cannot be uploaded manually if its size is approximately 200MB or greater. The report also can not be uploaded using the browser's Incognito mode.

1. After a new report has been uploaded, you can see the Best Practices Analysis report in CAM.

   ![Best Practices Analysis report](/help/journey-migration/cloud-acceleration-manager/assets/cam-bpareport.png)

   >[!NOTE]
   >If multiple, different reports are uploaded, the report that is displayed in detail is always the one that has the most recent creation date (not upload date).

1. Review and explore the Best Practices Analysis dashboard in CAM. See [Reviewing Best Practices Analysis Report](#analysis-report) for more details.

   >[!NOTE]
   >Uploading a new report resets all the assessments if it is newer than the previously loaded report.

### Using Print Preview {#print-preview-cam}

You can select the print preview option in Cloud Acceleration Manager for a printable preview of the reports or to print the report to a PDF format for easy shareability.

Follow the steps below:

1. Click the **Print Preview** action.

   ![Print Preview](/help/journey-migration/best-practices-analyzer/assets/bpa-printpreview1b.png)

1. On the new tab with the report displayed in a printable preview, click **Print** to print the report to a PDF format.

   >[!IMPORTANT]
   >
   >* The option **Save as PDF** is recommended and supported for the above functionality.
   >* If the browser's print button is used, it prints only one page. 

   ![Print](/help/journey-migration/best-practices-analyzer/assets/bpa-printpreview2.png)

### Using View Trendline {#trendline-view-cam}

When you upload more than one distinct Best Practices Analyzer (BPA) report in a Project, you can select the **View Trendline** option to view and compare results from the historical BPA reports.

Follow the steps below to view reports from the trendline option:

>[!NOTE]
>When you upload more than one distinct BPA report in a Project, you see the **...** icon. Reports are considered the same (not distinct) if their host and creation time are the same.

1. Navigate to your project and click **Review** from the **Best Practices Analysis** card in the **Readiness** phase.

   ![Best Practices Analysis - Review](/help/journey-migration/cloud-acceleration-manager/assets/trendline-view1a.png)

1. From the **View** drop-down list, click **Trendline Report**, as shown in the figure below.

   ![Trendline Report](/help/journey-migration/cloud-acceleration-manager/assets/trendline-view1b.png)

1. Clicking **Trendline Report** opens the trendline view of the report.

   ![Trendline View](/help/journey-migration/cloud-acceleration-manager/assets/trendline-view3a.png)


   >[!NOTE]
   >The Trendline Report displays the results from the historical BPA reports in a graphical representation. 
   >
   >You see two graphs displaying the trend of the:
   > 
   >1. **Report Findings Trend**
   >1. **Custom Components and Template Trend**
   >
   >You can add or change the graphical view by way of the drop-down, as shown in the figure below:
   >![Select the graphical view](/help/journey-migration/cloud-acceleration-manager/assets/reports-bpa1.png)


### Reviewing Best Practices Analysis Report {#analysis-report}

Explore the following cards available in the Best Practices Analysis Report page:

![Best Practices Analysis Report](/help/journey-migration/cloud-acceleration-manager/assets/cam-bpareport.png)

>[!NOTE]
> With each card, you can:
>
>* open its associated tab
>* bookmark all report tabs (including filtering) for sharing or future retrieval
>* use the details icon to view the details of each report finding

#### Report Properties {#report-properties}

The **Report Properties** card provides information about report properties such as report date, duration, filters, upload date, and Adobe Experience Manager (AEM) details.

![Report Properties](/help/journey-migration/cloud-acceleration-manager/assets/report-properties.png)

#### Report Overview {#report-overview}

This **Report Overview** card provides the report findings and severity levels that apply when assessing the readiness to move to AEM as a Cloud Service, as shown in the figure below.

![Report Overview](/help/journey-migration/cloud-acceleration-manager/assets/report-overview.png)

Clicking this report opens the **Report** tab.

![Report tab](/help/journey-migration/cloud-acceleration-manager/assets/report-overview2.png)

You can filter the report based on importance, subtype, or count.

![Report filters](/help/journey-migration/cloud-acceleration-manager/assets/report-overview3.png)

>[!NOTE]
>See [Interpreting the Best Practices Analyzer Report](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/best-practices-analyzer/using-best-practices-analyzer.html) to learn about findings categories and importance levels.

#### Best Practices Assessment {#best-practices-assessment}

The Best Practices Assessment option provides an assessment of your current AEM instance and provides guidance on next steps to adopt AEM best practices. You can review the following information from this tab:

* AEM Instance Overview
* Custom Components and Templates
* Additional Findings
* Slow Queries
* Maintenance Tasks

#### Migration Complexity Assessment {#migration-complexity-assessment}

The Migration Complexity Assessment option provides an assessment of the complexity to migrate the existing AEM implementation to AEM as a Cloud Service. 

You can review the following information from this tab:

* AEM Instance Overview
* Assessment
* Content Migration Considerations

   ![Migration Complexity Assessment](/help/journey-migration/cloud-acceleration-manager/assets/migration-complexity-1.png)

## Using Planning and Setup Card {#planning-setup}

1. Click **View** from the **Planning And Setup** card. This card provides all the relevant content that helps you plan and set up your AEM migration.

   ![Planning And Setup - View](/help/journey-migration/cloud-acceleration-manager/assets/readiness-view.png)

1. A content carousel displays all the relevant information for this phase of the migration journey.

   ![Planning And Setup carousel](/help/journey-migration/cloud-acceleration-manager/assets/readiness-5-planning.png)

### Deleting a Best Practices Analysis Report from the Trendline view {#delete-trendline}

>[!IMPORTANT]
>A report can be deleted only when more than one report has been uploaded in a project. 

1. Navigate to your project and click **Review** from the **Best Practices Analysis** card in the **Readiness** phase.

   ![Best Practices Analysis - Review](/help/journey-migration/cloud-acceleration-manager/assets/trendline-view1a.png)

1. Click **...**.

   ![Ellipse](/help/journey-migration/cloud-acceleration-manager/assets/trendline-view1.png)

1. In the drop-down list, click **View Trendline**, as shown in the figure below.

   ![View Trendline](/help/journey-migration/cloud-acceleration-manager/assets/trendline-view1b.png)

1. Click the delete icon from the **Trendline Report** screen.

   ![Trendline Report - Delete](/help/journey-migration/cloud-acceleration-manager/assets/trendline-view5a.png)

1. Click **Delete** to confirm the deletion.

   ![Delete](/help/journey-migration/cloud-acceleration-manager/assets/trendline-view6a.png)

## What's Next {#whats-next}

Once you have learned how to log into Cloud Acceleration Manager and how to create a project, you are now ready to move on to reviewing the next step in the [Implementation Phase](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-acceleration-manager/using-cam/cam-implementation-phase.html).
