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

The following table illustrates the maintenance tasks that are available.

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
    <td>Customer</td>
    <td>Version purge is currently disabled by default, but the policy can be configured, as described in the <a href="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/maintenance#purge_tasks">Version Purge and Audit Log Purge Maintenance Tasks</a> section.<br/><br/>Purging will soon be enabled by default, with those values overrideable.<br>
   </td>
  </td>
  </tr>
  <tr>
    <td>Audit Log Purge</td>
    <td>Customer</td>
    <td>Audit log purge is currently disabled by default, but the policy can be configured, as described in the <a href="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/maintenance#purge_tasks">Version Purge and Audit Log Purge Maintenance Tasks</a> section.<br/><br/>Purging will soon be enabled by default, with those values overrideable.<br>
   </td>
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
    <p>Enable the maintenance task by adding another node under the node above (name it <code>granite_ProjectPurgeTask</code>) with the appropriate properties. See the list of <a href="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/deploying/configuring-osgi">OSGi Properties</a> for <b>Adobe Projects Purge Configuration</b> .</p>
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

## Version Purge and Audit Log Purge Maintenance Tasks {#purge-tasks}

Purging versions and the audit log reduces the size of the repository, and in some scenarios, can improve performance.

>[!NOTE] 
>
>AEM Guides customers should not configure Version Purge.

### Defaults {#defaults}

Currently, purging is not enabled by default, but this will change in the future. Environments that were created before the default purging is enabled will have a more conservative threshold so that purging does not occur unexpectedly. See the Version Purge and Audit Log Purge sections below for more details about the default purging policy.
<!-- Version purging and audit log purging are on by default, with different default values for environments with ids higher than **TBD** versus those with ids lower than that value. -->

<!-- ### Overriding the default values with a new configuration {#override} -->

The default purge values can be overridden by declaring a configuration file and deploying it as described below.

<!-- The reason for this behavior is to clarify the ambiguity over whether the default purge values would take effect once you remove the declaration. -->

### Applying a configuration {#configure-purge}

Declare a configuration file and deploy it as described in the following steps.

>[!NOTE]
>Once you deploy the version purge node in the configuration file, you must keep it declared and not remove it. The config pipeline will fail if you attempt to do so. 
> 
>Similarly, once you deploy the audit log purge node in the configuration file, you must keep it declared and not remove it.

**1** Create a file named `mt.yaml` or similar.
  
**2** Place the file somewhere under a top level folder named `config` or similar, as described under [Using Config Pipelines](/help/operations/config-pipeline.md#folder-structure).

**3** - Declare properties in the configuration file, which include:

* a few properties above the data node -- see [Using Config Pipelines](/help/operations/config-pipeline.md#common-syntax) for a description. The `kind` property value should be *MaintenanceTasks* and the version should be set to *1*.

* a data object with both `versionPurge` and `auditLogPurge` objects.

See the definitions and syntax of the `versionPurge` and `auditLogPurge` objects below.

Structure the configuration similar to the following example:

```

kind: "MaintenanceTasks"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  versionPurge:
    maximumVersions: 15
    maximumAgeDays: 20
    paths: ["/content"]
    minimumVersions: 1
    retainLabelledVersions: false
  auditLogPurge:
    rules:
      - replication:
          maximumAgeDays: 15
          contentPath: "/content"
          types: ["Activate", "Deactivate", "Delete", "Test", "Reverse", "Internal Poll"]
      - pages:
          maximumAgeDays: 15
          contentPath: "/content"
          types: ["PageCreated", "PageModified", "PageMoved", "PageDeleted", "VersionCreated", "PageRestored", "PageValid", "PageInvalid"]
      - dam:
          maximumAgeDays: 15
          contentPath: "/content"
          types: ["ASSET_EXPIRING", "METADATA_UPDATED", "ASSET_EXPIRED", "ASSET_REMOVED", "RESTORED", "ASSET_MOVED", "ASSET_VIEWED", "PROJECT_VIEWED", "PUBLISHED_EXTERNAL", "COLLECTION_VIEWED", "VERSIONED", "ADDED_COMMENT", "RENDITION_UPDATED", "ACCEPTED", "DOWNLOADED", "SUBASSET_UPDATED", "SUBASSET_REMOVED", "ASSET_CREATED", "ASSET_SHARED", "RENDITION_REMOVED", "ASSET_PUBLISHED", "ORIGINAL_UPDATED", "RENDITION_DOWNLOADED", "REJECTED"]

```

Keep in mind that in order for the configuration to be valid:

* all properties must be defined. There are no inherited defaults.
* the types (integers, strings, booleans, etc) in the property tables below must be respected.

**4** - Create a config pipeline in Cloud Manager, as described in the [config pipeline article](/help/operations/config-pipeline.md#managing-in-cloud-manager).  

### Version Purge {#version-purge}

>[!NOTE]
>
>AEM Guides customers should not configure Version Purge.

#### Version Purge Defaults {#version-purge-defaults}

<!-- For version purging, environments with an id higher than **TBD** have the following default values: -->

Currently, purging is not enabled by default, but this will change in the future.

Environments that were created after the default purging is enabled will have the following default values: 

* Versions older than 30 days are removed.
* The most recent five versions in the last 30 days are kept.
* Irrespective of the rules above, the most recent version (in addition to the current file) is preserved.

<!-- Environments with an id equal or lower than **TBD** will have the following default values: -->

Environments that were created before the default purging is enabled will have the default values listed below, however it is recommended to lower those values in order to optimize performance.

* Versions older than 7 years are removed.
* All versions in the last 7 years are kept.
* After 7 years, versions other than the most recent version (in addition to the current file) are removed.

#### Version Purge Properties {#version-purge-properties}

The allowed properties are listed below. 

The columns indicating *default* indicate the default values in the future, when defaults are applied; *TBD* reflects an environment id that is still not determined.

| Properties | future default for envs>TBD  | future default for envs<=TBD  | required   | type    | Values   |
|-----------|--------------------------|-------------|-----------|---------------------|-------------|
| paths | ["/content"] | ["/content"] | Yes | array of strings | Specifies under which paths to purge versions when new versions are created.  Customers must declare this property, but the only allowable value is "/content". |
| maximumAgeDays | 30 | 2557 (7 years + 2 leap days) | Yes | Integer | Any version older than the configured value is removed. If the value is 0, purging is not performed based on the age of the version. |
| maximumVersions | 5 | 0 (no limit) | Yes | Integer | Any version older than the n-th newest version is removed. If the value is 0, purging is not performed based on the number of versions.|
| minimumVersions | 1 | 1 | Yes | Integer | The minimum number of versions that are kept regardless of the age. Note that at least 1 version is always kept; its value must be 1 or higher. |
| retainLabelledVersioned | false | false | Yes | boolean | Determines whether explicitly labelled versions will be excluded from the purge. For better repository optimization, it is recommended to set this value to false. |


**Property interactions**

The following examples illustrate how properties interact when combined.

Example:

```

maximumAgeDays = 30
maximumVersions = 10
minimumVersions = 2

```

If there are 11 versions on day 23, the oldest version will be purged next time the purge maintenance task runs, since the `maximumVersions` property is set to 10.

If there are 5 versions on day 31, only 3 will be purged since the `minimumVersions` property is set to 2.

Example:

```

maximumAgeDays = 30
maximumVersions = 0
minimumVersions = 1

```

No versions newer than 30 days will be purged since the `maximumVersions` property is set to 0.

One version older than 30 days will be kept.

### Audit Log Purge {#audit-purge}

#### Audit Log Purge Defaults {#audit-purge-defaults}

<!-- For audit log purging, environments with an id higher than **TBD** have the following default values: -->

Currently, purging is not enabled by default, but this will change in the future.

Environments that were created after the default purging is enabled will have the following default values: 

* Replication, DAM, and page audit logs older than 7 days are removed.
* All possible events are logged.

<!-- Environments with an id equal or lower than **TBD** will have the following default values: -->

Environments that were created before the default purging is enabled will have the default values listed below, however it is recommended to lower those values in order to optimize performance.

* Replication, DAM, and page audit logs older than 7 years are removed.
* All possible events are logged.

>[!NOTE]
>It is recommended that customers, who have regulatory requirements to produce uneditable audit logs, integrate with specialized, external services.

#### Audit Log Purge Properties {#audit-purge-properties}

The allowed properties are listed below. 

The columns indicating *default* indicate the default values in the future, when defaults are applied; *TBD* reflects an environment id that is still not determined.


| Properties | future default for envs>TBD  | future default for envs<=TBD  | required   | type    | Values   |
|-----------|--------------------------|-------------|-----------|---------------------|-------------|
| rules | - | - | Yes | Object | One or more of the following nodes: replication, pages, dam. Each of these nodes defines rules, with the properties below. All properties must be declared.|
| maximumAgeDays | 7 days| for all, 2557 (7 years + 2 leap days) | Yes | integer | For either replication, pages, or dam: the number of days the audit logs are kept. Audit logs older than the configured value are purged. |
| contentPath | "/content" | "/content" | Yes | String | The path under which the audit logs will be purged, for the related type. Must be set to "/content". |
| types | all values | all values | Yes | Array of enumeration | For **replication**, the enumerated values are: Activate, Deactivate, Delete, Test, Reverse, Internal Poll. For **pages**, the enumerated values are: PageCreated, PageModified, PageMoved, PageDeleted, VersionCreated, PageRestored, PageRolled Out, PageValid, PageInvalid. For **dam**, the enumerated values are: ASSET_EXPIRING, METADATA_UPDATED, ASSET_EXPIRED, ASSET_REMOVED, RESTORED, ASSET_MOVED, ASSET_VIEWED, PROJECT_VIEWED, PUBLISHED_EXTERNAL, COLLECTION_VIEWED, VERSIONED, ADDED_COMMENT, RENDITION_UPDATED, ACCEPTED, DOWNLOADED, SUBASSET_UPDATED, SUBASSET_REMOVED, ASSET_CREATED, ASSET_SHARED, RENDITION_REMOVED, ASSET_PUBLISHED, ORIGINAL_UPDATED, RENDITION_DOWNLOADED, REJECTED. |
