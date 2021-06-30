---
title: OSGi Configuration API
description: Description of the AEM as a Cloud Service OSGi configuration surface
feature: Deploying
---

# OSGi Configuration API

The two tables below reflect the AEM as a Cloud Service OSGi configuration surface, describing customers can configure.

1. A list of OSGi configurations that must not be configured by customer code
1. A list of OSGi configurations whose properties may be configured, but must abide by validation rules of each row. These rules include whether declaration of the property is required, its type, and in some cases, its allowed range of values.

If an OSGI configuration is not listed, it may be configured by customer code.

These rules are validated during the Cloud Manager build process. Additional rules may be added over time and the expected enforcement date is noted in the table. Customers are expected to abide by these rules by the target enforcement date. Not abiding by the rules after the removal date will generate errors in the Cloud Manager build process. Maven project's should include the [AEM as a Cloud Service SDK Build Analyzer Maven Plugin](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/build-analyzer-maven-plugin.html) to flag OSGI configuration errors during local SDK development.

Additional information about OSGI configuration can be found at [this location](/help/implementing/deploying/configuring-osgi.md).

## OSGi Configurations that Cannot be Configured {#osgi-configurations-that-cannot-be-configured}

| OSGi Configurations  | Announcement Date  | Target Enforcement Date  |
|---|---|---|
| org.apache.felix.webconsole.internal.servlet.OsgiManager  | 4/30/2021  | 7/31/2021  |
| com.day.cq.auth.impl.cug.CugSupportImpl |   |   |
| com.day.cq.jcrclustersupport.ClusterStartLevelController |   |   |
| org.apache.felix.http (Factory)  |   |   |

## OSGi Configurations Subject to Build Validation Rules {#osgi-configurations-subject-to-build-validation-rules}

<table>
<thead>
  <tr>
    <th>OSGi Confiturations and Properties</th>
    <th>Is Required</th>
    <th>Type</th>
    <th>Required Range</th>
    <th>Announcement Date</th>
    <th>Target Enforcement Date</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Configuration org.apache.felix.eventadmin.impl.EventAdmin</b></td>
    <td></td>
    <td></td>
    <td></td>
    <td>4/30/2021</td>
    <td>7/31/2021</td>
  </tr>
  <tr>
    <td>org.apache.felix.eventadmin.ThreadPoolSize</td>
    <td></td>
    <td>Integer</td>
    <td>2-100</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.eventadmin.AsyncToSyncThreadRatio</td>
    <td></td>
    <td>Double</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.eventadmin.Timeout</td>
    <td></td>
    <td>Integer</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.eventadmin.RequireTopic</td>
    <td></td>
    <td>Boolean</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.eventadmin.IgnoreTimeout</td>
    <td>Yes</td>
    <td>Array of strings</td>
    <td>must include at least all of:<br>org.apache.felix*,<br>org.apache.sling*<br>come.day*<br>com.adobe*</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.eventadmin.IgnoreTopic</td>
    <td></td>
    <td>Array of strings</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td><b>Configuration org.apache.felix.http</b></td>
    <td></td>
    <td></td>
    <td></td>
    <td>4/30/2021</td>
    <td>7/31/2021</td>
  </tr>
  <tr>
    <td>org.apache.felix.http.timeout</td>
    <td></td>
    <td>Integer</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.http.session.timeout</td>
    <td></td>
    <td>Integer</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.http.jetty.threadpool.max</td>
    <td></td>
    <td>Integer</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.http.jetty.headerBufferSize</td>
    <td></td>
    <td>Integer</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.http.jetty.requestBufferSize</td>
    <td></td>
    <td>Integer</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.http.jetty.responseBufferSize</td>
    <td></td>
    <td>Integer</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.http.jetty.maxFormSize</td>
    <td></td>
    <td>Integer</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.https.jetty.session.cookie.httpOnly</td>
    <td></td>
    <td>Boolean</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.https.jetty.session.cookie.secure</td>
    <td></td>
    <td>Boolean</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.eclipse.jetty.servlet.SessionIdPathParameterName</td>
    <td></td>
    <td>String</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.eclipse.jetty.servlet.CheckingRemoteSessionIdEncoding</td>
    <td></td>
    <td>Boolean</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.eclipse.jetty.servlet.SessionCookie</td>
    <td></td>
    <td>String</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.eclipse.jetty.servlet.SessionDomain</td>
    <td></td>
    <td>String</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.eclipse.jetty.servlet.SessionPath</td>
    <td></td>
    <td>String</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.eclipse.jetty.servlet.MaxAge</td>
    <td></td>
    <td>Integer</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.eclipse.jetty.servlet.SessionScavengingInterval</td>
    <td></td>
    <td>Integer</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.jetty.gziphandler.enable</td>
    <td></td>
    <td>Boolean</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.jetty.gzip.minGzipSize</td>
    <td></td>
    <td>Integer</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.jetty.gzip.compressionLevel</td>
    <td></td>
    <td>Integer</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.jetty.gzip.inflateBufferSize</td>
    <td></td>
    <td>Integer</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.jetty.gzip.syncFlush</td>
    <td></td>
    <td>Boolean</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.jetty.gzip.excludedUserAgents</td>
    <td></td>
    <td>String</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.jetty.gzip.includedMethods</td>
    <td></td>
    <td>Array of strings</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.jetty.gzip.excludedMethods</td>
    <td></td>
    <td>Array of strings</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.jetty.gzip.includedPaths</td>
    <td></td>
    <td>Array of strings</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.jetty.gzip.excludedPaths</td>
    <td></td>
    <td>Array of strings</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.jetty.gzip.includedMimeTypes</td>
    <td></td>
    <td>Array of strings</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.jetty.gzip.excludedMimeTypes</td>
    <td></td>
    <td>Array of strings</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.http.session.invalidate</td>
    <td></td>
    <td>Boolean</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.http.session.container.attribute</td>
    <td></td>
    <td>Array of strings</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.felix.http.session.uniqueid</td>
    <td></td>
    <td>Boolean</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td><b>Configuration org.apache.sling.scripting.cache</b></td>
    <td></td>
    <td></td>
    <td></td>
    <td>4/30/2021</td>
    <td>7/31/2021</td>
  </tr>
  <tr>
    <td>org.apache.sling.scripting.cache.size</td>
    <td></td>
    <td>Integer</td>
    <td>>= 2048</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>org.apache.sling.scripting.cache.additional_extensions</td>
    <td>Yes</td>
    <td>Array of strings</td>
    <td>Must include js</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td><b>Configuration com.day.cq.mailer.DefaultMailService</b></td>
    <td></td>
    <td></td>
    <td></td>
    <td>4/30/2021</td>
    <td>7/31/2021</td>
  </tr>
  <tr>
    <td>smtp.host</td>
    <td></td>
    <td>String</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>smtp.port</td>
    <td></td>
    <td>Integer</td>
    <td>Either 465, 587, or 25</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>smtp.user</td>
    <td></td>
    <td>String</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>smtp.password</td>
    <td></td>
    <td>String</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>from.address</td>
    <td></td>
    <td>String</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>smtp.ssl</td>
    <td></td>
    <td>String</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>smtp.starttls</td>
    <td></td>
    <td>Boolean</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>smtp.requiretls</td>
    <td></td>
    <td>Boolean</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>debug.email</td>
    <td></td>
    <td>Boolean</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>oauth.flow</td>
    <td></td>
    <td>Boolean</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>