---
title: Maintenance Tasks in AEM as a Cloud Service
seo-title: Maintenance Tasks in AEM as a Cloud Service
description: Maintenance Tasks in AEM as a Cloud Service 
seo-description: Maintenance Tasks in AEM as a Cloud Service 
---

# Maintenance Tasks in AEM as a Cloud Service

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
| Version Purge | Adobe | Fully owned by Adobe, but in the future, it will be shared between Adobe and the customer with the customer being able to configure certain parameters in github. |
| Audit Log Purge  | Adobe | Fully owned by Adobe, but in the future, it will be shared between Adobe and the customer with the customer being able to configure certain parameters in github. |
| Lucene Binaries Cleanup | Removed | N/A - removed |
| Ad-hoc Task Purge | Customer | Must be done in github. <br> Override the Maintenance window configuration node under `/libs` and `/apps` with `/conf/global/settings/granite/operations/maintenance/granite_weekly` or `granite_daily`. See the Maintenance Window table below for additional configuration details. <br> Enable the maintenance task by adding another node under the node above (any name is acceptable, but the convention is `granite_TaskPurgeTask`) with the appropriate properties. <br> Configure the OSGI properties see the (AEM 6.5 Maintenance Task documentation) (link TBD)|
| Workflow Purge | Customer |  Must be done in github. <br> Override the Maintenance window configuration node under `/libs` and `/apps` with `/conf/global/settings/granite/operations/maintenance/granite_weekly` or `granite_daily`. See the Maintenance Window table below for additional configuration details. <br> Enable the maintenance task by adding another node under the node above (any name is acceptable, but the convention is `granite_WorkflowPurgeTask`) with the appropriate properties. <br> Configure the OSGI properties (see AEM 6.5 Maintenance Task documentation) (link TBD) |
| Project Purge | Customer |  Must be done in github. <br> Override the Maintenance window configuration node under `/libs` and `/apps` with `/conf/global/settings/granite/operations/maintenance/granite_weekly` or `granite_daily`. See the Maintenance Window table below for additional configuration details. <br> Enable the maintenance task by adding a node under the node above (any name is acceptable, but the convention is `granite_ProjectPurgeTask`) with the appropriate properties. <br> Configure OSGI properties (see AEM 6.5 Maintenance Task documentation) (link TBD) |

 The table below describes the configuration options of the Maintenance Window node. 

<table>
  <tr>
    <th>Maintenance Window Configuration</th>
    <th>Who owns the configuration</th>
    <th>Configuration Type</th>
    <th>Location</th>
    <th>Example</th>
    <th>Parameters</th>
  </tr>
  <tr>
    <td>Daily</td>
    <td>Customer</td>
    <td>JCR Node Definition</td>
    <td><code>/conf/global/settings/granite/operations/maintenance/granite_daily </code> (which overrides the node in <code>/apps</code> and <code>/libs</code>)</td>
    <td>See code sample 1 below</td>
    <td>
    <ul>
    <li><strong>windowSchedule</strong> = daily (this value should not be changed)</li>
    <li><strong>windowStartTime</strong> = HH:MM using as 24 hour clock. Defines when the Maintenance Tasks associated with the Daily Maintenance Window should begin executing.</li>
    <li><strong>windowEndTime</strong> = HH:MM using as 24 hour clock. Defines when the Maintenance Tasks associated with the Daily Maintenance Window should stop executing if they haven't already completed.</li>
    </ul> </td>
  </tr>
  <tr>
    <td>Weekly</td>
    <td>Customer</td>
    <td>JCR Node Definition</td>
    <td><code>/conf/global/settings/granite/operations/maintenance/granite_weekly</code> (which overrides the node in <code>/apps</code> and <code>/libs</code>)</td>
    <td>See code sample 2 below</td>
    <td></td>
  </tr>
  <tr>
    <td>Monthly</td>
    <td>Customer</td>
    <td>JCR Node Definition</td>
    <td><code>/conf/global/settings/granite/operations/maintenance/granite_monthly</code> (which overrides the node in <code>/apps</code> and <code>/libs</code>)</td>
    <td>See code sample 3 below</td>
    <td></td>
  </tr>
</table>

Code sample 1

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

Code sample 2

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

Code sample 3

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

