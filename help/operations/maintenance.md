---
title: Maintenance Tasks in AEM as a Cloud Service
description: Learn about maintenance tasks in AEM as a Cloud Service and how to configure them.
exl-id: 5b114f94-be6e-4db4-bad3-d832e4e5a412
feature: Operations
role: Admin
---
# Maintenance Tasks in AEM as a Cloud Service {#maintenance-tasks-in-aem-as-a-cloud-service}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_maintenance"
>title="Maintenance Tasks"
>abstract="Maintenance Tasks are processes that run on a schedule to optimize the repository. With AEM as a Cloud Service, the need for customers to configure the operational properties of maintenance tasks is minimal. Customers can focus their resources on application-level concerns, leaving the infrastructure operations to Adobe."

Maintenance Tasks are processes that run on a schedule to optimize the repository. With AEM as a Cloud Service, the need for customers to configure the operational properties of maintenance tasks is minimal. Customers can focus their resources on application-level concerns, leaving the infrastructure operations to Adobe.

## Configuring maintenance tasks {#maintenance-tasks-configuring}

In previous versions of AEM, you could configure maintenance tasks by using the Maintenance Card (Tools > Operations > Maintenance). For AEM as a Cloud Service, the Maintenance Card is no longer available so configurations should be committed to source control and deployed by using the Cloud Manager. Adobe manages those maintenance tasks which have settings that are not configurable by customers (for example, Datastore Garbage Collection). Other maintenance tasks can be configured by customers, as described in the table below.

>[!CAUTION]
>
>Adobe reserves the right to override a customer's maintenance task configuration settings to mitigate issues such as performance degradation.

The following table illustrates the maintenance tasks that are available at the time of release of AEM as a Cloud Service.

<table style="table-layout:auto">
 <tbody>
  <tr>
    <th>Maintenance Task</th>
    <th>Who owns the configuration</th>
    <th>How to configure (optional)</th>
  </tr>  
  <tr>
    <td>Datastore garbage collection</td>
    <td>Adobe</td>
    <td>N/A - fully Adobe owned</td>
  </td> 
  </tr>
  <tr>
    <td>Version Purge</td>
    <td>Adobe</td>
    <td>For existing environments (those created before a yet-to-be-determined date in 2024), purging is disabled and will be enabled in the future with a default of 7 years; customers will be able to configure it with lower, custom values (such as 30 days).<br><br> <!--Alexandru: leave the two line breaks in place, otherwise spacing won't render properly-->New environments (those created starting a yet-to-be-determined date in 2024) will have purging enabled by default with the values below, with customers being able to configure with custom values.
     <ol>
       <li>Versions older than 30 days are removed</li>
       <li>The most recent 5 versions in the last 30 days are kept</li>
       <li>Irrespective of the rules above, the most recent version is preserved.</li>
       <br>It is recommended that customers who have regulatory requirements to render site pages exactly as they appeared on a specific date, integrate with specialized, external services.
     </ol></td>
  </td>
  </tr>
  <tr>
    <td>Audit Log Purge</td>
    <td>Adobe</td>
    <td>For existing environments (those created before a yet-to-be-determined date in 2024), purging is disabled and will be enabled in the future with a default of 7 years; customers will be able to configure it with lower, custom values (such as 30 days).<br><br> <!-- See above for the two line breaks -->New environments (those created starting a yet-to-be-determined date in 2024) will have purging enabled by default under the <code>/content</code> node of the repository according to the following behavior:
     <ol>
       <li>For replication auditing, audit logs older than 3 days are removed</li>
       <li>For DAM (Assets) auditing, audit logs older than 30 days are removed</li>
       <li>For page auditing, logs older than 3 days are removed.</li>
       <br>It is recommended that customers who have regulatory requirements to produce uneditable audit logs, integrate with specialized, external services.
     </ol></td>
   </td>
  </tr>
  <tr>
    <td>Lucene Binaries Cleanup</td>
    <td>Adobe</td>
    <td>Unused and therefore disabled by Adobe.</td>
  </td>
  </tr>
  <tr>
    <td>Ad-hoc Task Purge</td>
    <td>Customer</td>
    <td>
    <p>Must be done in git. Override the out-of-the-box Maintenance window configuration node under <code>/libs</code> by creating properties under the folder <code>/apps/settings/granite/operations/maintenance/granite_weekly</code>, <code>granite_daily</code> or <code>granite_monthly</code>.</p>
    <p>See the Maintenance Window table below for additional configuration details. Enable the maintenance task by adding another node under the node above. Name it <code>granite_TaskPurgeTask</code>, with attribute <code>sling:resourceType</code> set to <code>granite/operations/components/maintenance/task</code> and attribute <code>granite.maintenance.name</code> set to <code>TaskPurge</code>. Configure the OSGI properties, see <code>com.adobe.granite.taskmanagement.impl.purge.TaskPurgeMaintenanceTask</code> for the list of properties.</p>
  </td>
  </tr>
    <tr>
    <td>Workflow Purge</td>
    <td>Customer</td>
    <td>
    <p>Must be done in git. Override the out-of-the-box Maintenance window configuration node under <code>/libs</code> by creating properties under the folder <code>/apps/settings/granite/operations/maintenance/granite_weekly</code>, <code>granite_daily</code> or <code>granite_monthly</code>. See the Maintenance Window table below for additional configuration details.</p>
    <p>Enable the maintenance task by adding another node under the node above (name it <code>granite_WorkflowPurgeTask</code>) with the appropriate properties. Configure the OSGI properties see <a href="https://experienceleague.adobe.com/docs/experience-manager-65/administering/operations/workflows-administering.html#regular-purging-of-workflow-instances">AEM 6.5 Maintenance Task documentation</a>.</p>
  </td>
  </tr>
  <tr>
    <td>Project Purge</td>
    <td>Customer</td>
    <td>
    <p>Must be done in git. Override the out-of-the-box Maintenance window configuration node under <code>/libs</code> by creating properties under the folder <code>/apps/settings/granite/operations/maintenance/granite_weekly</code>, <code>granite_daily</code> or <code>granite_monthly</code>. See the Maintenance Window table below for additional configuration details.</p>
    <p>Enable the maintenance task by adding another node under the node above (name it <code>granite_ProjectPurgeTask</code>) with the appropriate properties. See the list of OSGI properties under "Adobe Projects Purge Configuration".</p>
  </td>
  </tr>
  </tbody>
</table>

<table style="table-layout:auto">
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
  <p>A maintenance task cannot be executed more than once during this timeframe.</p>
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
    <p>A maintenance task cannot be executed more than once during this timeframe.</p>
    <p><strong>windowScheduleWeekdays= Array of two values from 1&ndash;7 (for example, [5,5])</strong> The first value of the array is the start day when the job is scheduled and the second value is the end day when the job would be stopped. The exact time of the start and the end is governed by windowStartTime and windowEndTime respectively.</p>
    </td>
  </tr>
  <tr>
    <td>Monthly</td>
    <td>Customer</td>
    <td>JCR Node Definition</td>
    <td>
    <p><strong>windowSchedule=monthly</strong> (this value should not be changed)</p>
    <p><strong>windowStartTime=HH:MM</strong> using as 24 hour clock. Defines when the Maintenance Tasks associated with the Monthly Maintenance Window should begin executing.</p>
    <p><strong>windowEndTime=HH:MM</strong> using as 24 hour clock. Defines when the Maintenance Tasks associated with the Monthly Maintenance Window should stop executing if they haven't already completed.</p>
    <p>A maintenance task cannot be executed more than once during this timeframe.</p>
    <p><strong>windowScheduleWeekdays=Array of two values from 1&ndash;7 (for example, [5,5])</strong> The first value of the array is the start day when the job is scheduled and the second value is the end day when the job would be stopped. The exact time of the start and the end is governed by windowStartTime and windowEndTime respectively.</p>
    <p><strong>windowFirstLastStartDay= 0/1</strong> 0 to schedule on the first week of the month or 1 to schedule on the last week of the month. The absence of a value would effectively schedule jobs on the day governed by windowScheduleWeekdays (every month).</p>
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
