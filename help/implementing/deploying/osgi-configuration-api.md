---
title: OSGi Configuration API
description: Description of the AEM as a Cloud Service OSGi configuration surface
feature: Deploying
exl-id: 94d3df65-71d7-4442-8412-fe2cca7e79ff
---
# OSGi Configuration API

The two lists below reflect the AEM as a Cloud Service OSGi configuration surface, describing what customers can configure.

1. A list of OSGi configurations that must not be configured by customer code
1. A list of OSGi configurations whose properties may be configured, but must abide by the indicated validation rules. These rules include whether declaration of the property is required, its type, and in some cases, its allowed range of values.

If an OSGI configuration is not listed, it may be configured by customer code.

These rules are validated during the Cloud Manager build process. Additional rules may be added over time and the expected enforcement date is noted in the table. Customers are expected to abide by these rules by the target enforcement date. Not abiding by the rules after the removal date will generate errors in the Cloud Manager build process. Maven projects should include the [AEM as a Cloud Service SDK Build Analyzer Maven Plugin](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/build-analyzer-maven-plugin.html) to flag OSGI configuration errors during local SDK development.

Additional information about OSGI configuration can be found at [this location](/help/implementing/deploying/configuring-osgi.md).

## OSGi Configurations that Cannot be Modified {#osgi-configurations-that-cannot-be-modified}

* **`org.apache.felix.webconsole.internal.servlet.OsgiManager`** (Announcement Date: 4/30/2021, Enforcement Date: 7/31/2021)
* **`com.day.cq.auth.impl.cug.CugSupportImpl`** (Announcement Date: 4/30/2021, Enforcement Date: 7/31/2021)
* **`com.day.cq.jcrclustersupport.ClusterStartLevelController`** (Announcement Date: 4/30/2021, Enforcement Date: 7/31/2021)
* **`org.apache.felix.http (Factory)`** (Announcement Date: 4/30/2021, Enforcement Date: 7/31/2021)
* **`org.apache.sling.jcr.davex.impl.servlets.SlingDavExServlet`** (Announcement Date: 8/25/2021, Enforcement Date: 11/26/2021)

## OSGi Configurations Subject to Build Validation Rules {#osgi-configurations-subject-to-build-validation-rules}

* **`org.apache.felix.eventadmin.impl.EventAdmin`** (Announcement Date: 4/30/2021, Enforcement Date: 7/31/2021)
  * `org.apache.felix.eventadmin.ThreadPoolSize` 
    * Type: integer
    * Required Range: 2-100
  * `org.apache.felix.eventadmin.AsyncToSyncThreadRatio`
    * Type: double
  * `org.apache.felix.eventadmin.Timeout`
    * Type: integer
  * `org.apache.felix.eventadmin.RequireTopic`
    * Type: boolean
  * `org.apache.felix.eventadmin.IgnoreTimeout`
    * Required
    * Type: array of strings
    * Required Range: Must include at least all of `org.apache.felix*`, `org.apache.sling*`, `come.day*`, `com.adobe*`
  * `org.apache.felix.eventadmin.IgnoreTopic`
    * Type: array of strings
* **`org.apache.felix.http`** (Announcement Date: 4/30/2021, Enforcement Date: 7/31/2021)
  * `org.apache.felix.http.timeout`
    * Type: integer
  * `org.apache.felix.http.session.timeout`
    * Type: integer
  * `org.apache.felix.http.jetty.threadpool.max`
    * Type: integer
  * `org.apache.felix.http.jetty.headerBufferSize`
    * Type: integer
  * `org.apache.felix.http.jetty.requestBufferSize`
    * Type: integer
  * `org.apache.felix.http.jetty.responseBufferSize`
    * Type: integer
  * `org.apache.felix.http.jetty.maxFormSize`
    * Type: integer
  * `org.apache.felix.https.jetty.session.cookie.httpOnly`
    * Type: boolean
  * `org.apache.felix.https.jetty.session.cookie.secure`
    * Type: boolean
  * `org.eclipse.jetty.servlet.SessionIdPathParameterName`
    * Type: string
  * `org.eclipse.jetty.servlet.CheckingRemoteSessionIdEncoding`
    * Type: boolean
  * `org.eclipse.jetty.servlet.SessionCookie`
    * Type: string
  * `org.eclipse.jetty.servlet.SessionDomain`
    * Type: string
  * `org.eclipse.jetty.servlet.SessionPath`
    * Type: string
  * `org.eclipse.jetty.servlet.MaxAge`
    * Type: integer
  * `org.eclipse.jetty.servlet.SessionScavengingInterval`
    * Type: integer
  * `org.apache.felix.jetty.gziphandler.enable`
    * Type: boolean
  * `org.apache.felix.jetty.gzip.minGzipSize`
    * Type: integer
  * `org.apache.felix.jetty.gzip.compressionLevel`
    * Type: integer
  * `org.apache.felix.jetty.gzip.inflateBufferSize`
    * Type: integer
  * `org.apache.felix.jetty.gzip.syncFlush`
    * Type: boolean
  * `org.apache.felix.jetty.gzip.excludedUserAgents`
    * Type: string
  * `org.apache.felix.jetty.gzip.includedMethods`
    * Type: array of strings
  * `org.apache.felix.jetty.gzip.excludedMethods`
    * Type: array of strings
  * `org.apache.felix.jetty.gzip.includedPaths`
    * Type: array of strings
  * `org.apache.felix.jetty.gzip.excludedPaths`
    * Type: array of strings
  * `org.apache.felix.jetty.gzip.includedMimeTypes`
    * Type: array of strings
  * `org.apache.felix.jetty.gzip.excludedMimeTypes`
    * Type: array of strings
  * `org.apache.felix.http.session.invalidate`
    * Type: boolean
  * `org.apache.felix.http.session.container.attribute`
    * Type: array of strings
  * `org.apache.felix.http.session.uniqueid`
    * Type: boolean
* **`org.apache.sling.scripting.cache`** (Announcement Date: 4/30/2021, Enforcement Date: 7/31/2021)
  * `org.apache.sling.scripting.cache.size`
    * Type: integer
    * Required Range: >= 2048
  * `org.apache.sling.scripting.cache.additional_extensions`
    * Required
    * Type: array of strings
    * Required Range: must include js
* **`com.day.cq.mailer.DefaultMailService`** (Announcement Date: 4/30/2021, Enforcement Date: 7/31/2021)
  * `smtp.host`
    * Type: string
  * `smtp.port`
    * Type: integer
    * Required Range: 465, 587, or 25
  * `smtp.user`
    * Type: string
  * `smtp.password`
    * Type: string
  * `from.address`
    * Type: string
  * `smtp.ssl`
    * Type: string
  * `smtp.starttls`
    * Type: boolean
  * `smtp.requiretls`
    * Type: boolean
  * `debug.email`
    * Type: boolean
  * `oauth.flow`
    * Type: boolean
* **`org.apache.sling.commons.log.LogManager.factory.config`** (Announcement Date: 11/16/21, Enforcement Date: 2/16/21)
  * `org.apache.sling.commons.log.level`
    * Type: enumeration
    * Required Range: INFO, DEBUG, or TRACE
  * `org.apache.sling.commons.log.names`
    * Type: string
  * `org.apache.sling.commons.log.file`
    * Type: string
  * `org.apache.sling.commons.log.additiv`
    * Type: boolean