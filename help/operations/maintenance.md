---
title: Maintenance Tasks in AEM as a Cloud Service
description: Maintenance Tasks in AEM as a Cloud Service
exl-id: 5b114f94-be6e-4db4-bad3-d832e4e5a412
---
# Maintenance Tasks in AEM as a Cloud Service

>[!CONTEXTUALHELP]
>id="aemcloud_golive_maintenance"
>title="Maintenance Tasks"
>abstract="Maintenance Tasks are processes that run on a schedule in order to optimize the repository. With AEM as a Cloud Service, the need for customers to configure the operational properties of maintenance tasks is minimal. Customers can focus their resources on application-level concerns, leaving the infrastructure operations to Adobe."
>additional-url="https://helpx.adobe.com/experience-manager/kb/AEM6-Maintenance-Guide.html" text="AEM Maintenance Guide"
>additional-url="https://helpx.adobe.com/experience-manager/6-5/sites/administering/using/operations-dashboard.html#AutomatedMaintenanceTasks" text="Operations Dashboard Maintenance Tasks"

Maintenance Tasks are processes that run on a schedule in order to optimize the repository. With AEM as a Cloud Service, the need for customers to configure the operational properties of maintenance tasks is minimal. Customers can focus their resources on application-level concerns, leaving the infrastructure operations to Adobe.

For additional information about maintenance tasks, see the following pages:

* [AEM Maintenance Guide](https://helpx.adobe.com/experience-manager/kb/AEM6-Maintenance-Guide.html)
* [Operations Dashboard Maintenance Tasks](https://helpx.adobe.com/experience-manager/6-5/sites/administering/using/operations-dashboard.html#AutomatedMaintenanceTasks)

## Configuring maintenance tasks

In previous versions of AEM, you could configure maintenance tasks by using the Maintenance Card (Tools > Operations > Maintenance). For AEM as a Cloud Service, the Maintenance Card is no longer available so configurations should be committed to source control and deployed by using the Cloud Manager. Adobe will manage maintenance tasks that do not require customer decisions (for example, Datastore Garbage Collection) while other maintenance task can be configured by the customer (see the table below). 

>[!CAUTION]
>
>Adobe reserves the right to override a customer's maintenance task configuration settings in order to mitigate issues such as performance degradation.

The following table illustrates the maintenance tasks that are available at the time of release of AEM as a Cloud Service.

| Maintenance Task | Who owns the configuration | How to configure (optional)  |
|---|---|---|
| Datastore garbage collection | Adobe | N/A - fully Adobe owned |
| Version Purge | Adobe | Fully owned by Adobe, but in the future, customers will be able to configure certain parameters. |
| Audit Log Purge  | Adobe | Fully owned by Adobe, but in the future, customers will be able to configure certain parameters. |
| Lucene Binaries Cleanup | Adobe | Unused and therefore disabled by Adobe. |
| Ad-hoc Task Purge | Customer | Must be done in github. <br> Override the out-of-the-box Maintenance window configuration node under `/libs` by creating properties under the the folder `/apps/settings/granite/operations/maintenance/granite_weekly` or `granite_daily`. See the Maintenance Window table below for additional configuration details. <br> Enable the maintenance task by adding another node under the node above (name it `granite_TaskPurgeTask`) with the appropriate properties. <br> Configure the OSGI properties see the [AEM 6.5 Maintenance Task documentation](https://helpx.adobe.com/experience-manager/kb/AEM6-Maintenance-Guide.html)|
| Workflow Purge | Customer |  Must be done in github. <br> Override the out-of-the-box Maintenance window configuration node under `/libs` by creating properties under the the folder`/apps/settings/granite/operations/maintenance/granite_weekly` or `granite_daily`. See the Maintenance Window table below for additional configuration details. <br> Enable the maintenance task by adding another node under the node above (name it `granite_WorkflowPurgeTask`) with the appropriate properties. <br> Configure the OSGI properties see [AEM 6.5 Maintenance Task documentation](https://helpx.adobe.com/experience-manager/kb/AEM6-Maintenance-Guide.html) |
| Project Purge | Customer |  Must be done in github. <br> Override the out-of-the-box Maintenance window configuration node under `/libs` by creating properties under the the folder `/apps/settings/granite/operations/maintenance/granite_weekly` or `granite_daily`. See the Maintenance Window table below for additional configuration details. <br> Enable the maintenance task by adding a node under the node above (name it `granite_ProjectPurgeTask`) with the appropriate properties. <br> Configure OSGI properties see [AEM 6.5 Maintenance Task documentation](https://helpx.adobe.com/experience-manager/kb/AEM6-Maintenance-Guide.html) |

Customers can schedule each of the Workflow Purge, Ad-hoc Task Purge and Project Purge Maintenance tasks to be executed during the daily, weekly, or monthly maintenance windows. These configurations should be edited directly in source control. The table below describes the configuration parameters available for each of the window. Also, see the locations and code samples provided after the table.

<table>
 <tbody>
  <tr>
    <th>Maintenance Window Configuration</th>
    <th>Who owns the configuration</th>
    <th>Configuration Type</th>
    <th>Parameters</th>
  </tr>
  <tr>
    <td>Daily</td>
    <td>Customer</td>
    <td>JCR Node Definition</td>
  <td>
  <p><strong>windowSchedule=daily</strong> (this value should not be changed)</p>
  <p><strong>windowStartTime=HH:MM</strong> using as 24 hour clock. Defines when the Maintenance Tasks associated with the Daily Maintenance Window should begin executing.</p>
  <p><strong>windowEndTime=HH:MM</strong> using as 24 hour clock. Defines when the Maintenance Tasks associated with the Daily Maintenance Window should stop executing if they haven't already completed.</p>
  </td> 
  </tr>
  <tr>
    <td>Weekly</td>
    <td>Customer</td>
    <td>JCR Node Definition</td>
    <td>
    <p><strong>windowSchedule=weekly</strong> (this value should not be changed)</p>
    <p><strong>windowStartTime=HH:MM</strong> using as 24 hour clock. Defines when the Maintenance Tasks associated with the weekly Maintenance Window should begin executing.</p>
    <p><strong>windowEndTime=HH:MM</strong> using as 24 hour clock. Defines when the Maintenance Tasks associated with the Weekly Maintenance Window should stop executing if they haven't already completed.</p>
    <p><strong>windowScheduleWeekdays= Array of 2 values from 1-7 (e.g. [5,5])</strong> The first value of the array is the start day when the job is scheduled and the second value is the end day when the job would be stopped. The exact time of the start and the end is governed by windowStartTime and windowEndTime respectively.</p>
    </td>
  </tr>
  <tr>
    <td>Monthly</td>
    <td>Customer</td>
    <td>JCR Node Definition</td>
    <td>
    <p><strong>windowSchedule=daily</strong> (this value should not be changed)</p>
    <p><strong>windowStartTime=HH:MM</strong> using as 24 hour clock. Defines when the Maintenance Tasks associated with the Monthly Maintenance Window should begin executing.</p>
    <p><strong>windowEndTime=HH:MM</strong> using as 24 hour clock. Defines when the Maintenance Tasks associated with the Monthly Maintenance Window should stop executing if they haven't already completed.</p>
    <p><strong>windowScheduleWeekdays=Array of 2 values from 1-7 (e.g. [5,5])</strong> The first value of the array is the start day when the job is scheduled and the second value is the end day when the job would be stopped. The exact time of the start and the end is governed by windowStartTime and windowEndTime respectively.</p>
    <p><strong>windowFirstLastStartDay= 0/1</strong> 0 to schedule on the first week of the month or 1 to schedule on the last week of the month. The absence of a value would effectively schedule jobs every day as governed by windowScheduleWeekdays every month.</p>
    </td> 
    </tr>
    </tbody>
</table>

**Locations**:

* Daily - /apps/settings/granite/operations/maintenance/granite_daily
* Weekly - /apps/settings/granite/operations/maintenance/granite_weekly
* Monthly - /apps/settings/granite/operations/maintenance/granite_monthly

**Code samples**:

Code sample 1 (daily)

```xml

<?xml version="1.0" encoding="UTF-8"?>
<jcr:root xmlns:sling="http://sling.apache.org/jcr/sling/1.0" 
  xmlns:jcr="http://www.jcp.org/jcr/1.0" 
  jcr:primaryType="sling:Folder"
  sling:configCollectionInherit="true"
  sling:configPropertyInherit="true"
  windowSchedule="daily"
  windowStartTime="03:00"
  windowEndTime="05:00"
 />
```

Code sample 2 (weekly)

```xml

<?xml version="1.0" encoding="UTF-8"?>
<jcr:root xmlns:sling="http://sling.apache.org/jcr/sling/1.0" 
   xmlns:jcr="http://www.jcp.org/jcr/1.0"
   jcr:primaryType="sling:Folder"
   sling:configCollectionInherit="true"
   sling:configPropertyInherit="true"
   windowEndTime="15:30"
   windowSchedule="weekly"
   windowScheduleWeekdays="[5,5]"
   windowStartTime="14:30"/>
```

Code sample 3 (monthly)

```xml

<?xml version="1.0" encoding="UTF-8"?>
<jcr:root xmlns:sling="http://sling.apache.org/jcr/sling/1.0" 
   xmlns:jcr="http://www.jcp.org/jcr/1.0"
   jcr:primaryType="sling:Folder"
   sling:configCollectionInherit="true"
   sling:configPropertyInherit="true"
   windowEndTime="15:30"
   windowSchedule="monthly"
   windowFirstLastStartDay=0
   windowScheduleWeekdays="[5,5]"
   windowStartTime="14:30"/>
```
