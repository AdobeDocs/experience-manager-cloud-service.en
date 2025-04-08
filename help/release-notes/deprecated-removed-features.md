---
title: Deprecated and Removed Features
description: Release notes specific to deprecated and removed features in [!DNL Adobe Experience Manager] as a [!DNL Cloud Service].
exl-id: ef082184-4eb7-49c7-8887-03d925e3da6f
feature: Release Information
role: Admin
---
# Deprecated and Removed Features and APIs {#deprecated-and-removed-features-apis}

>[!CONTEXTUALHELP]
>id="aem_cloud_deprecated_features"
>title="Deprecated and removed features in AEM as a Cloud Service"
>abstract="AEM as a Cloud Service has a cloud-native deployment model. This tab highlights features and capabilities replaced by their cloud-native counterparts." 

Adobe constantly evaluates product capabilities to, over time, reinvent or replace older features with more modern alternatives to improve overall customer value, always under careful consideration of backward compatibility. As [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] uses a cloud-native deployment model, it replaces certain capabilities and features with cloud-native counterparts.

To communicate the impending removal/replacement of [!DNL Experience Manager] capabilities, the following rules apply:

1. Announcement of deprecation comes first. Deprecated capabilities remain available but are not enhanced further.
1. Capabilities announced to be deprecated are removed in the subsequent major release, at the earliest. The actual target date for removal is announced.

This process gives customers at least one release cycle to adapt their implementation to a new version or successor of a deprecated capability, before actual removal.

## Deprecated Features {#deprecated-features}

This section lists features and capabilities that have been marked as deprecated in [!DNL Experience Manager] as a [!DNL Cloud Service]. Typically, features to be removed in a future release are set for deprecation first, with an alternative provided.

Customers are advised to review if they use the feature/capability in their current deployment, and make plans to change their implementation to use the alternative provided.

| Capabilities | Deprecated feature | Replacement |
| ------------ | ------------------ | ----------- |
|Sites|[PWA Features](/help/sites-cloud/authoring/sites-console/enable-pwa.md)|None|
|Sites|[SPA Editor](/help/implementing/developing/hybrid/introduction.md)|The preferred editors for managing headless content in AEM are:<br>- [The Universal Editor](/help/edge/wysiwyg-authoring/authoring.md) for visual editing.<br>- [The Content Fragment Editor](/help/assets/content-fragments/content-fragments-managing.md) for form-based editing.|
|[!DNL Sites]|[JavaScript Use API](https://github.com/adobe/htl-spec/blob/master/SPECIFICATION.md#42-javascript-use-api)|[Java Use API](https://experienceleague.adobe.com/en/docs/experience-manager-htl/content/java-use-api)|
| [!DNL Sites]       | Experience Fragments properties for **Social Media Status**. | The feature is planned for removal soon. |
| [!DNL Sites]       | Template-based simple content fragments. | [Model-based structured content fragments](/help/assets/content-fragments/content-fragments-models.md) now. |
| [!DNL Assets]       | `DAM Asset Update` workflow to process ingested images. | Asset ingestion uses [asset microservices](/help/assets/asset-microservices-overview.md) now. |
| [!DNL Assets]       | Upload assets directly to [!DNL Experience Manager]. See [deprecated asset upload APIs](/help/assets/developer-reference-material-apis.md#deprecated-asset-upload-api). | Use [Direct binary upload](/help/assets/add-assets.md). For technical details, see [direct upload APIs](/help/assets/developer-reference-material-apis.md#upload-binary). |
| [!DNL Assets]       | [Certain workflow steps](/help/assets/developer-reference-material-apis.md#post-processing-workflows-steps) in `DAM Asset Update` workflow are not supported, including calling command-line tools like [!DNL ImageMagick]. | [Asset microservices](/help/assets/asset-microservices-overview.md) provide a replacement for many workflows. For custom processing, use [post-processing workflows](/help/assets/asset-microservices-configure-and-use.md#post-processing-workflows). |
| [!DNL Assets]       | FFmpeg transcoding of videos. | For FFmpeg thumbnail generation, use [Asset microservices](/help/assets/asset-microservices-overview.md). For FFmpeg transcoding, use [Dynamic Media](/help/assets/manage-video-assets.md). |
| [!DNL Foundation]       | Tree replication UI under the replication agents "Distribute" tab (removal after September 30, 2021) | [Manage publication](/help/operations/replication.md#manage-publication) or [Tree Activation Workflow Step](/help/operations/replication.md#tree-activation) approaches. |
| [!DNL Foundation]       | The replication agent admin screen's Distribute tab and the Replication API cannot replicate content packages larger than 10MB. | [Manage publication](/help/operations/replication.md#manage-publication) or [Tree Activation Workflow Step](/help/operations/replication.md#tree-activation) |
| [!DNL Foundation]       | Integrations using credentials generated from Adobe Developer Console projects are gradually losing support for Service Account (JWT) credentials. As of May 1, 2024, new Service Account (JWT) credentials cannot be created in Adobe Developer Console. Existing Service Account (JWT) credentials remain usable for configured integrations until January 1, 2025, after which they stop working, requiring customers to migrate to OAuth Server-to-Server credentials. [Learn more](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/jwt-credentials-deprecation-in-adobe-developer-console).| [Migrate](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/migration/#migration-overview) to OAuth Server-to-Server credentials. |
| [!DNL Foundation]       | Publish Content Tree Workflow and the related Publish Content Tree Workflow Step, which was used for replications of hierarchies of content. | Use [Tree Activation Workflow Step](/help/operations/replication.md#tree-activation), which is more performant. |


## Removed Features {#removed-features}

This section lists features and capabilities that have been removed from [!DNL Experience Manager] with [!DNL Experience Manager] as a [!DNL Cloud Service].

| Area         | Feature            | Replacement | Target Removal Date |
| ------------ | ------------------ | ----------- | ------------------- |
| User Interface  | Classic UI is removed from the product user interface. A few Classic UI dialogs are available for a few select capabilities, such as Link Checker, Version Purge, and some Cloud Service configurations. Upcoming [product updates](/help/release-notes/home.md) may further remove Classic UI availability. | Standard UI  | Removed |
| [!DNL Dynamic Media] | Previous integrations with [Dynamic Media Classic](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/sites/administering/integration/scene7#integration) and [Dynamic Media Hybrid mode](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/assets/dynamic/config-dynamic#dynamic) are not available in [!DNL Experience Manager] as a [!DNL Cloud Service]. | Use [Dynamic Media](/help/assets/dynamic-media/dynamic-media.md) provided with [!DNL Experience Manager] as a [!DNL Cloud Service]. | Removed |
| [!DNL Sites] | Portal Director and Portlet Component | These capabilities were deprecated in [!DNL Experience Manager] 6.4 and have now been removed from [!DNL Experience Manager].| Removed |
| [!DNL Sites] | Design Importer | This capability has been removed as immutable sections of the [!DNL Experience Manager] repository are not accessible at runtime. | Removed |
| [!DNL Assets] | [!DNL Assets] sharing with Assets Core Service and Creative Cloud services is not available. | For integration with [!DNL Adobe Creative Cloud], use [Adobe Asset Link](https://helpx.adobe.com/enterprise/using/adobe-asset-link.html). | Removed |
| [!DNL Foundation]       | Support for Apache Sling datasources (OSGi bundle org.apache.sling.datasource) | N/A | Removed |
| [!DNL Foundation]       | Support for JST scripting templates (OSGi bundle org.apache.sling.scripting.jst) | N/A | Removed |
| [!DNL Foundation]       | Support for the Apache Felix Http Whiteboard | OSGi Http Whiteboard | March 2022 |
| [!DNL Foundation]       | Support for com.adobe.granite.oauth.server | Adobe IMS Integration | March 2023 |
| [!DNL Foundation]       | Support for org.apache.sling.serviceusermapping feature to [get the service user id](https://sling.apache.org/apidocs/sling12/org/apache/sling/serviceusermapping/ServiceUserMapper.html#getServiceUserID-org.osgi.framework.Bundle-java.lang.String-) | N/A | 8/30/24 |


## AEM APIs {#aem-apis}

Below is an extensive list of deprecated AEM APIs and their expected removal date. Customers are expected to remove the APIs by the target removal date from their code. Any usage of the API past the removal date can generate errors in the local SDK/Development Environment and the Cloud Manager build process.

<details>
  <summary>Expand to see the list of deprecated APIs.</summary>
<table style="table-layout:auto">
  <tr>
    <th>Package/Class</th>
    <th>Comments</th>
    <th>Deprecation Date</th>
    <th>Target Removal Date</th>
  </tr>
<tbody>
  <tr>
    <td>org.apache.sling.commons.auth<br>org.apache.sling.commons.auth.spi</td>
    <td>Use Sling's Auth Core/Auth Core SPI interfaces as an alternative. <a href="#org.apache.sling.commons.auth">See removal notes below.</a></td>
    <td>2015</td>
    <td>7/30/21</td>
  </tr>
  <tr>
    <td>org.apache.sling.runmode</td>
    <td></td>
    <td>2015</td>
    <td>7/30/21</td>
  </tr>
  <tr>
    <td>com.day.cq.jcrclustersupport</td>
    <td>Use Sling's Discovery API as an alternative</td>
    <td>2015</td>
    <td>removed</td>
  </tr>
  <tr>
    <td>org.apache.fop.apps</td>
    <td></td>
    <td>3/1/21</td>
    <td>removed</td>
  </tr>
  <tr>
    <td>org.apache.jackrabbit.vault.util.xml.xerces.dom<br>org.apache.jackrabbit.vault.util.xml.xerces.util<br>org.apache.jackrabbit.vault.util.xml.xerces.xni<br>org.apache.jackrabbit.vault.util.xml.xerces.xni.parser</td>
    <td></td>
    <td>3/5/21</td>
    <td>removed</td>
  </tr>
  <tr>
    <td>org.json</td>
    <td>The Apache Johnzon implementation of <a href="https://johnzon.apache.org/index.html">javax.json</a> is recommended and should be used. </td>
    <td>4/30/21</td>
    <td>12/31/21</td>
  </tr>
  <tr>
    <td>org.apache.felix.cm<br>org.apache.felix.cm.file</td>
    <td>Custom persistence managers are not supported in AEM as a Cloud Service.</td>
    <td>4/30/21</td>
    <td>removed</td>
  </tr>
  <tr>
    <td>org.apache.commons.lang<br>org.apache.commons.lang.enums<br>org.apache.commons.lang.builder<br>org.apache.commons.lang.exception<br>org.apache.commons.lang.math<br>org.apache.commons.lang.mutable<br>org.apache.commons.lang.reflect<br>org.apache.commons.lang.text<br>org.apache.commons.lang.time</td>
    <td>Commons Lang 2 is in maintenance mode. Commons Lang 3 should be used instead.</td>
    <td>4/30/21</td>
    <td>12/31/21</td>
  </tr>
  <tr>
    <td>org.apache.commons.collections<br>org.apache.commons.collections.bag<br>org.apache.commons.collections.bidimap<br>org.apache.commons.collections.buffer<br>org.apache.commons.collections.collection<br>org.apache.commons.collections.comparators<br>org.apache.commons.collections.functors<br>org.apache.commons.collections.iterators<br>org.apache.commons.collections.keyvalue<br>org.apache.commons.collections.list<br>org.apache.commons.collections.map<br>org.apache.commons.collections.set</td>
    <td>Commons Collections 3 is in maintenance mode. Commons Collections 4 should be used instead.</td>
    <td>4/30/21</td>
    <td>12/31/21</td>
  </tr>
  <tr>
    <td>org.apache.felix.systemready</td>
    <td>It is recommended you use the Apache Felix HealthCheck API instead</td>
    <td>4/30/21</td>
    <td>removed</td>
  </tr>
  <tr>
    <td>org.apache.felix.webconsole<br>org.apache.felix.webconsole.bundleinfo<br>org.apache.felix.webconsole.i18n</td>
    <td>The Felix web console is not supported in Cloud environments</td>
    <td>4/30/21</td>
    <td>7/30/21</td>
  </tr>
  <tr> <td>org.apache.felix.http.jetty<br>org.eclipse.jetty.client.jmx<br>org.eclipse.jetty.jmx<br>org.eclipse.jetty.server.handler.jmx<br>org.eclipse.jetty.server.nio<br>org.eclipse.jetty.server.jmx<br>org.eclipse.jetty.servlet.jmx<br>org.eclipse.jetty.util.preventers<br>org.eclipse.jetty.util.thread.strategy<br>org.eclipse.jetty.webapp<br>org.eclipse.jetty.websocket.api<br>org.eclipse.jetty.websocket.api.annotations<br>org.eclipse.jetty.websocket.api.extensions<br>org.eclipse.jetty.websocket.api.util<br>org.eclipse.jetty.websocket.client<br>org.eclipse.jetty.websocket.client.io<br>org.eclipse.jetty.websocket.client.masks<br>org.eclipse.jetty.websocket.common<br>org.eclipse.jetty.websocket.common.events<br>org.eclipse.jetty.websocket.common.events.annotated<br>org.eclipse.jetty.websocket.common.extensions<br>org.eclipse.jetty.websocket.common.extensions.compress<br>org.eclipse.jetty.websocket.common.extensions.fragment<br>org.eclipse.jetty.websocket.common.extensions.identity<br>org.eclipse.jetty.websocket.common.frames<br>org.eclipse.jetty.websocket.common.io<br>org.eclipse.jetty.websocket.common.io.http<br>org.eclipse.jetty.websocket.common.io.payload<br>org.eclipse.jetty.websocket.common.message<br>org.eclipse.jetty.websocket.common.scopes<br>org.eclipse.jetty.websocket.common.util<br>org.eclipse.jetty.websocket.server<br>org.eclipse.jetty.websocket.server.pathmap<br>org.eclipse.jetty.websocket.servlet<br>org.eclipse.jetty.xml</td>
    <td>The Eclipse Jetty and Felix Http Jetty packages are no longer supported. <a href="#org.eclipse.jetty">See removal notes below.</a></td>
    <td>5/27/21</td>
    <td>8/26/21</td>
  </tr>
  <tr> <td>org.eclipse.jetty.client<br>org.eclipse.jetty.client.api<br>org.eclipse.jetty.client.http<br>org.eclipse.jetty.client.util<br>org.eclipse.jetty.http<br>org.eclipse.jetty.http.pathmap<br>org.eclipse.jetty.io<br>org.eclipse.jetty.io.ssl<br>org.eclipse.jetty.security<br>org.eclipse.jetty.server<br>org.eclipse.jetty.server.handler<br>org.eclipse.jetty.server.handler.gzip<br>org.eclipse.jetty.server.session<br>org.eclipse.jetty.servlet<br>org.eclipse.jetty.servlet.listener<br>org.eclipse.jetty.util<br>org.eclipse.jetty.util.annotation<br>org.eclipse.jetty.util.component<br>org.eclipse.jetty.util.log<br>org.eclipse.jetty.util.resource<br>org.eclipse.jetty.util.security<br>org.eclipse.jetty.util.ssl<br>org.eclipse.jetty.util.statistic<br>org.eclipse.jetty.util.thread
</td>
    <td>The Eclipse Jetty and Felix Http Jetty packages are no longer supported.</td>
    <td>5/27/21</td>
    <td>8/26/21</td>
  </tr>  
  <tr>     <td>com.mongodb<br>com.mongodb.annotations<br>com.mongodb.assertions<br>com.mongodb.async<br>com.mongodb.binding<br>com.mongodb.bulk<br>com.mongodb.client<br>com.mongodb.client.gridfs<br>com.mongodb.client.gridfs.codecs<br>com.mongodb.client.gridfs.model<br>com.mongodb.client.jndi<br>com.mongodb.client.model<br>com.mongodb.client.model.changestream<br>com.mongodb.client.model.geojson<br>com.mongodb.client.model.geojson.codecs<br>com.mongodb.client.result<br>com.mongodb.connection<br>com.mongodb.connection.netty<br>com.mongodb.diagnostics.logging<br>com.mongodb.event<br>com.mongodb.gridfs<br>com.mongodb.internal<br>com.mongodb.internal.async<br>com.mongodb.internal.authentication<br>com.mongodb.internal.connection<br>com.mongodb.internal.dns<br>com.mongodb.internal.event<br>com.mongodb.internal.management.jmx<br>com.mongodb.internal.session<br>com.mongodb.internal.thread<br>com.mongodb.internal.validator<br>com.mongodb.management<br>com.mongodb.operation<br>com.mongodb.selector<br>com.mongodb.session<br>com.mongodb.util</td>
    <td>Usage of this API is not supported in AEM as a Cloud Service. <a href="#com.mongodb">See removal notes below.</a></td>
    <td>5/27/21</td>
    <td>7/30/21</td>
  </tr>
  <tr>
    <td>org.apache.felix.metatype<br>org.apache.felix.scr<br>org.apache.felix.scr.info<br>org.apache.felix.scr.component</td>
    <td>The Apache Felix metatype and SCR APIs are deprecated.  Use the OSGi metatype and Declarative Service APIs instead.</td>
    <td>5/27/21</td>
    <td>removed</td>
  </tr>
  <tr>
    <td>org.slf4j.impl</td>
    <td>Log implementation classes are not compatible with AEM as a Cloud Service.</td>
    <td>7/4/21</td>
    <td>removed</td>
  </tr>
  <tr>
    <td>org.apache.abdera<br>org.apache.abdera.model<br>org.apache.abdera.factory<br>org.apache.abdera.ext.media<br>org.apache.abdera.util<br>org.apache.abdera.i18n.iri<br>org.apache.abdera.writer<br>org.apache.abdera.i18n.rfc4646<br>org.apache.abdera.i18n.rfc4646.enums<br>org.apache.abdera.i18n.text<br>org.apache.abdera.filter<br>org.apache.abdera.xpath<br>org.apache.abdera.i18n.text.io<br>org.apache.abdera.i18n.text.data<br>org.apache.abdera.parser</td>
    <td>This API is deprecated as Apache Abdera is a retired project since 2017. <a href="#org.apache.abdera_or_org.apache.sling.atom.taglib">See removal notes below.</a></td>
    <td>7/29/21</td>
    <td>09/29/21</td>
  </tr>
  <tr>
    <td>org.apache.abdera.ext.opensearch<br>org.apache.abdera.ext.opensearch.model<br>org.apache.abdera.ext.opensearch.server<br>org.apache.abdera.ext.opensearch.server.impl<br>org.apache.abdera.ext.opensearch.server.processors<br>org.apache.abdera.i18n.iri.data<br>org.apache.abdera.i18n.lang<br>org.apache.abdera.i18n.templates<br>org.apache.abdera.i18n.unicode.data<br>org.apache.abdera.parser.stax<br>org.apache.abdera.parser.stax.util<br>org.apache.abdera.protocol<br>org.apache.abdera.protocol.client<br>org.apache.abdera.protocol.client.cache<br>org.apache.abdera.protocol.client.util<br>org.apache.abdera.protocol.error<br>org.apache.abdera.protocol.server<br>org.apache.abdera.protocol.server.context<br>org.apache.abdera.protocol.server.filters<br>org.apache.abdera.protocol.server.impl<br>org.apache.abdera.protocol.server.multipart<br>org.apache.abdera.protocol.server.processors<br>org.apache.abdera.protocol.server.provider.basic<br>org.apache.abdera.protocol.server.provider.managed<br>org.apache.abdera.protocol.server.servlet<br>org.apache.abdera.protocol.util<br>org.apache.abdera.util.filter</td>
    <td>This API is deprecated as Apache Abdera is a retired project since 2017.</td>
    <td>4/8/19</td>
    <td>09/29/21</td>
  </tr>
  <tr>
    <td>org.apache.sling.startupfilter<br>com.adobe.granite.crypto.spi<br>com.adobe.granite.crpyto.spi.base<br>com.adobe.agl.impl.data.icudt40b<br>com.adobe.agl.impl.data.icudt40b.brkitr<br>com.adobe.agl.impl.data.icudt40b.coll<br>com.adobe.agl.impl.data.icudt40b.rbnf<br>com.<br>adobe.agl.impl.data.icudt40b.translit<br>com.adobe.internal.pdf.tika<br>com.adobe.internal.pdftoolkit.color<br>com.adobe.internal.pdftoolkit.core.encryption<br>com.adobe.internal.pdftoolkit.core.encryption.impl<br>com.adobe.internal.pdftoolkit.core.traverser<br>com.adobe.internal.pdftoolkit.graphicsDOM<br>com.adobe.internal.pdftoolkit.graphicsDOM.shading<br>com.adobe.internal.pdftoolkit.graphicsDOM.utils<br>com.adobe.internal.pdftoolkit.image<br>com.adobe.internal.pdftoolkit.pdf.content<br>com.adobe.internal.pdftoolkit.pdf.content.processor<br>com.adobe.internal.pdftoolkit.pdf.content.processor.base14fontwidths<br>com.adobe.internal.pdftoolkit.pdf.contentmodify<br>com.adobe.internal.pdftoolkit.pdf.contentmodify.impl<br>com.adobe.internal.pdftoolkit.pdf.digsig<br>com.adobe.internal.pdftoolkit.pdf.document<br>com.adobe.internal.pdftoolkit.pdf.document.listener<br>com.adobe.internal.pdftoolkit.pdf.document.permissionhandlers<br>com.adobe.internal.pdftoolkit.pdf.filters<br>com.adobe.internal.pdftoolkit.pdf.graphics<br>com.adobe.internal.pdftoolkit.pdf.graphics.colorspaces<br>com.adobe.internal.pdftoolkit.pdf.graphics.colorspaces.cmykresources<br>com.adobe.internal.pdftoolkit.pdf.graphics.font<br>com.adobe.internal.pdftoolkit.pdf.graphics.font.encodings<br>com.adobe.internal.pdftoolkit.pdf.graphics.font.impl<br>com.adobe.internal.pdftoolkit.pdf.graphics.impl<br>com.adobe.internal.pdftoolkit.pdf.graphics.optionalcontent<br>com.adobe.internal.pdftoolkit.pdf.graphics.patterns<br>com.adobe.internal.pdftoolkit.pdf.graphics.shading<br>com.adobe.internal.pdftoolkit.pdf.graphics.xobject<br>com.adobe.internal.pdftoolkit.pdf.impl<br>com.adobe.internal.pdftoolkit.pdf.inlineimage<br>com.adobe.internal.pdftoolkit.pdf.interactive<br>com.adobe.internal.pdftoolkit.pdf.interactive.action<br>com.adobe.internal.pdftoolkit.pdf.interactive.annotation<br>com.adobe.internal.pdftoolkit.pdf.interactive.forms<br>com.adobe.internal.pdftoolkit.pdf.interactive.forms.impl<br>com.adobe.internal.pdftoolkit.pdf.interactive.geospatial<br>com.adobe.internal.pdftoolkit.pdf.interactive.markedcontent<br>com.adobe.internal.pdftoolkit.pdf.interactive.navigation<br>com.adobe.internal.pdftoolkit.pdf.interactive.navigation.collection<br>com.adobe.internal.pdftoolkit.pdf.interactive.readerrequirements<br>com.adobe.internal.pdftoolkit.pdf.interactive.requirement<br>com.adobe.internal.pdftoolkit.pdf.interchange<br>com.adobe.internal.pdftoolkit.pdf.interchange.documentparts<br>com.adobe.internal.pdftoolkit.pdf.interchange.metadata<br>com.adobe.internal.pdftoolkit.pdf.interchange.prepress<br>com.adobe.internal.pdftoolkit.pdf.interchange.structure<br>com.adobe.internal.pdftoolkit.pdf.multimedia<br>com.adobe.internal.pdftoolkit.pdf.page<br>com.adobe.internal.pdftoolkit.pdf.rendering<br>com.adobe.internal.pdftoolkit.pdf.transparency<br>com.adobe.internal.pdftoolkit.pdf.utils<br>com.adobe.internal.pdftoolkit.services.Jpeg2000<br>com.adobe.internal.pdftoolkit.services.fontresources<br>com.adobe.internal.pdftoolkit.services.fontresources.subsetting<br>com.adobe.internal.pdftoolkit.services.interchange.structure<br>com.adobe.internal.pdftoolkit.services.optionalcontent<br>com.adobe.internal.pdftoolkit.services.optionalcontent.impl<br>com.adobe.internal.pdftoolkit.services.pdfParser<br>com.adobe.internal.pdftoolkit.services.permissions<br>com.adobe.internal.pdftoolkit.services.rasterizer<br>com.adobe.internal.pdftoolkit.services.readingorder<br>com.adobe.internal.pdftoolkit.services.security<br>com.adobe.internal.pdftoolkit.services.swf<br>com.adobe.internal.pdftoolkit.services.textextraction<br>com.adobe.internal.pdftoolkit.services.textextraction.impl<br>com.adobe.internal.pdftoolkit.services.xmp<br>com.adobe.internal.util.base64<br>com.adobe.internal.xmp.utils<br>com.day.crx.core.cluster<br>com.day.crx.packaging<br>com.day.crx.packaging.gfx<br>com.day.crx.query<br>com.day.crx.sling.server.jmx<br>com.day.durbo<br>com.day.durbo.io<br>com.day.imageio.plugins<br>org.apache.aries.jmx.codec<br>org.h2.mvstore<br>org.h2.mvstore.rtree<br>org.h2.mvstore.type<br>org.openxmlformats.schemas.drawingml.x2006.chart.impl<br>org.openxmlformats.schemas.drawingml.x2006.main.impl<br>org.openxmlformats.schemas.drawingml.x2006.picture.impl<br>org.openxmlformats.schemas.drawingml.x2006.spreadsheetDrawing.impl<br>org.openxmlformats.schemas.drawingml.x2006.wordprocessingDrawing.impl<br>org.openxmlformats.schemas.officeDocument.x2006.customProperties.impl<br>org.openxmlformats.schemas.officeDocument.x2006.docPropsVTypes.impl<br>org.openxmlformats.schemas.officeDocument.x2006.extendedProperties.impl<br>org.openxmlformats.schemas.officeDocument.x2006.relationships.impl<br>org.openxmlformats.schemas.presentationml.x2006.main.impl<br>org.openxmlformats.schemas.spreadsheetml.x2006.main.impl<br>org.openxmlformats.schemas.wordprocessingml.x2006.main.impl<br>org.openxmlformats.schemas.xpackage.x2006.contentTypes<br>org.openxmlformats.schemas.xpackage.x2006.contentTypes.impl<br>org.openxmlformats.schemas.xpackage.x2006.digitalSignature<br>org.openxmlformats.schemas.xpackage.x2006.digitalSignature.impl<br>org.openxmlformats.schemas.xpackage.x2006.metadata.coreProperties<br>org.openxmlformats.schemas.xpackage.x2006.metadata.coreProperties.impl<br>org.openxmlformats.schemas.xpackage.x2006.relationships<br>org.openxmlformats.schemas.xpackage.x2006.relationships.impl<br>com.adobe.internal.afml<br>com.adobe.internal.agm<br>com.adobe.internal.pdftoolkit.legacy.services.ap.es2<br>com.adobe.internal.pdftoolkit.legacy.services.ap.es3<br>com.adobe.internal.pdftoolkit.pdf.pieceinfo.compoundtype<br>com.adobe.internal.pdftoolkit.pdf.pieceinfo.editablepdf<br>com.adobe.internal.pdftoolkit.services.ap<br>com.adobe.internal.pdftoolkit.services.ap.annot<br>com.adobe.internal.pdftoolkit.services.ap.extension<br>com.adobe.internal.pdftoolkit.services.ap.impl<br>com.adobe.internal.pdftoolkit.services.ap.spi<br>com.adobe.internal.pdftoolkit.services.digsig<br>com.adobe.internal.pdftoolkit.services.digsig.cryptoprovider<br>com.adobe.internal.pdftoolkit.services.digsig.docmodanalysis<br>com.adobe.internal.pdftoolkit.services.digsig.spi<br>com.adobe.internal.pdftoolkit.services.fdf<br>com.adobe.internal.pdftoolkit.services.formflattener<br>com.adobe.internal.pdftoolkit.services.forms<br>com.adobe.internal.pdftoolkit.services.imageconversion<br>com.adobe.internal.pdftoolkit.services.javascript<br>com.adobe.internal.pdftoolkit.services.javascript.extension<br>com.adobe.internal.pdftoolkit.services.manipulations<br>com.adobe.internal.pdftoolkit.services.manipulations.impl<br>com.adobe.internal.pdftoolkit.services.optimizer<br>com.adobe.internal.pdftoolkit.services.pdfa<br>com.adobe.internal.pdftoolkit.services.pdfa.error<br>com.adobe.internal.pdftoolkit.services.pdfa2<br>com.adobe.internal.pdftoolkit.services.pdfa2.error<br>com.adobe.internal.pdftoolkit.services.pdfa2.error.codes<br>com.adobe.internal.pdftoolkit.services.pdfa3<br>com.adobe.internal.pdftoolkit.services.pdfport<br>com.adobe.internal.pdftoolkit.services.portfolio<br>com.adobe.internal.pdftoolkit.services.rcg<br>com.adobe.internal.pdftoolkit.services.rcg.impl<br>com.adobe.internal.pdftoolkit.services.redaction<br>com.adobe.internal.pdftoolkit.services.redaction.handler<br>com.adobe.internal.pdftoolkit.services.sanitization<br>com.adobe.internal.pdftoolkit.services.xbm<br>com.adobe.internal.pdftoolkit.services.xdp<br>com.adobe.internal.pdftoolkit.services.xfa<br>com.adobe.internal.pdftoolkit.services.xfa.form<br>com.adobe.internal.pdftoolkit.services.xfatext<br>com.adobe.internal.pdftoolkit.services.xfdf<br>com.adobe.internal.pdftoolkit.services.xobjhandler<br>com.adobe.internal.pdftoolkit.xml<br>com.adobe.octopus.extract<br>opennlp.tools.doccat<br>opennlp.tools.entitylinker<br>opennlp.tools.formats<br>opennlp.tools.formats.ad<br>opennlp.tools.formats.brat<br>opennlp.tools.formats.convert<br>opennlp.tools.formats.frenchtreebank<br>opennlp.tools.formats.muc<br>opennlp.tools.formats.ontonotes<br>opennlp.tools.lemmatizer<br>opennlp.tools.parser<br>opennlp.tools.parser.chunking<br>opennlp.tools.parser.lang.en<br>opennlp.tools.parser.lang.es<br>opennlp.tools.parser.treeinsert<br>opennlp.tools.sentdetect<br>opennlp.tools.sentdetect.lang<br>opennlp.tools.sentdetect.lang.th<br>opennlp.tools.stemmer<br>opennlp.tools.stemmer.snowball<br>opennlp.tools.tokenize.lang.en<br>org.apache.commons.imaging.color<br>org.apache.commons.imaging.common<br>org.apache.commons.imaging.common.itu_t4<br>org.apache.commons.imaging.common.mylzw<br>org.apache.commons.imaging.formats.bmp<br>org.apache.commons.imaging.formats.dcx<br>org.apache.commons.imaging.formats.gif<br>org.apache.commons.imaging.formats.icns<br>org.apache.commons.imaging.formats.ico<br>org.apache.commons.imaging.formats.jpeg<br>org.apache.commons.imaging.formats.jpeg.decoder<br>org.apache.commons.imaging.formats.jpeg.exif<br>org.apache.commons.imaging.formats.jpeg.iptc<br>org.apache.commons.imaging.formats.jpeg.segments<br>org.apache.commons.imaging.formats.jpeg.xmp<br>org.apache.commons.imaging.formats.pcx<br>org.apache.commons.imaging.formats.png<br>org.apache.commons.imaging.formats.png.chunks<br>org.apache.commons.imaging.formats.png.scanlinefilters<br>org.apache.commons.imaging.formats.png.transparencyfilters<br>org.apache.commons.imaging.formats.pnm<br>org.apache.commons.imaging.formats.psd<br>org.apache.commons.imaging.formats.psd.dataparsers<br>org.apache.commons.imaging.formats.psd.datareaders<br>org.apache.commons.imaging.formats.rgbe<br>org.apache.commons.imaging.formats.tiff<br>org.apache.commons.imaging.formats.tiff.constants<br>org.apache.commons.imaging.formats.tiff.datareaders<br>org.apache.commons.imaging.formats.tiff.fieldtypes<br>org.apache.commons.imaging.formats.tiff.photometricinterpreters<br>org.apache.commons.imaging.formats.tiff.taginfos<br>org.apache.commons.imaging.formats.tiff.write<br>org.apache.commons.imaging.formats.wbmp<br>org.apache.commons.imaging.formats.xbm<br>org.apache.commons.imaging.formats.xpm<br>org.apache.commons.imaging.icc<br>org.apache.commons.imaging.palette<br>org.apache.commons.imaging.util<br>com.adobe.dam.print.ids.utils<br>com.day.cq.dam.api.reporting<br>com.day.cq.dam.entitlement.api<br>com.day.cq.dam.handler.standard.epub<br>com.day.cq.dam.handler.standard.keynote<br>com.day.cq.dam.handler.standard.mp3<br>com.day.cq.dam.handler.standard.msoffice<br>com.day.cq.dam.handler.standard.msoffice.wmf<br>com.day.cq.dam.handler.standard.ooxml<br>com.day.cq.dam.handler.standard.pdf<br>com.day.cq.dam.handler.standard.pict<br>com.day.cq.dam.handler.standard.ps<br>com.day.cq.dam.handler.standard.psd<br>com.day.cq.dam.handler.standard.zip<br>com.day.cq.dam.word.extraction<br>com.day.cq.dam.word.process<br>com.adobe.xmp.worker.files<br>com.adobe.cq.address.api<br>com.adobe.cq.address.api.location<br>com.day.cq.mcm.emailprovider.impl.types<br>com.day.io<br>com.day.io.disk<br>com.day.io.file<br>org.apache.commons.exec.environment<br>org.apache.commons.exec.launcher<br>org.apache.commons.exec.util<br>com.google.zxing<br>com.google.zxing.common<br>com.google.zxing.common.reedsolomon<br>com.google.zxing.qrcode.decoder<br>com.google.zxing.qrcode.encoder<br>com.adobe.cq.dam.dm.internalapi.image_server<br>com.day.cq.dam.api.s7dam.jobs<br>com.day.cq.dam.api.s7dam.omnisearch<br>com.day.cq.dam.api.s7dam.scene7<br>com.day.cq.dam.scene7<br>com.day.cq.dam.scene7.api.net<br>com.day.cq.analytics.sitecatalyst.rsmerger<br>com.day.cq.searchpromote<br>com.day.cq.searchpromote.xml<br>com.day.cq.searchpromote.xml.form<br>com.day.cq.searchpromote.xml.result></td>
    <td>Legacy AEM 6.x API.</td>
    <td>4/8/19</td>
    <td>removed</td>
  </tr>
  <tr>
    <td>org.apache.sling.discovery.commons<br>org.apache.sling.discovery.commons.providers<br>org.apache.sling.discovery.commons.providers.base<br>org.apache.sling.discovery.commons.providers.spi<br>org.apache.sling.discovery.commons.providers.spi.base<br>org.apache.sling.discovery.commons.providers.util</td>
    <td>This API is not supported in Cloud Service.</td>
    <td>9/30/21</td>
    <td>removed</td>
  </tr>
  <tr>
    <td>org.apache.jackrabbit.vault.util.xml<br>org.apache.jackrabbit.vault.util.xml.serialize</td>
    <td>Util Classes related to Apache Xerces are removed in subsequent releases causing a major version change. Because these utils are for internal use in File vault, the API is getting deprecated from the public API surface.</td>
    <td>9/1/21</td>
    <td>removed</td>
  <tr>
    <td>org.apache.sling.atom.taglib<br>org.apache.sling.atom.taglib.media</td>
    <td>Legacy AEM 6.x API. <a href="#org.apache.abdera_or_org.apache.sling.atom.taglib">See removal notes below.</a></td>
    <td>4/8/19</td>
    <td>9/29/21</td>
  </tr>
  <tr>
    <td>org.apache.felix.http.whiteboard</td>
    <td>The Apache Felix Http Whiteboard is not supported anymore. Migrate your code to the OSGi Http Whiteboard. <a href="#org.apache.felix.http.whiteboard">See removal notes below.</a></td>
    <td>1/27/2022</td>
    <td>3/24/2022</td>
  </tr>
  <tr>
    <td>org.apache.cocoon.xml.dom<br>org.apache.cocoon.xml.sax</td>
    <td>This API is deprecated. Migrate your code to the XML APIs provided by the JDK.</td>
    <td>1/27/2022</td>
    <td>3/24/2022</td>
  </tr>
  <tr>
    <td>ch.qos.logback.classic<br>ch.qos.logback.classic.boolex<br>ch.qos.logback.classic.db.names<br>ch.qos.logback.classic.db.script<br>ch.qos.logback.classic.encoder<br>ch.qos.logback.classic.filter<br>ch.qos.logback.classic.helpers<br>ch.qos.logback.classic.html<br>ch.qos.logback.classic.jmx<br>ch.qos.logback.classic.joran<br>ch.qos.logback.classic.joran.action<br>ch.qos.logback.classic.jul<br>ch.qos.logback.classic.layout<br>ch.qos.logback.classic.log4j<br>ch.qos.logback.classic.net<br>ch.qos.logback.classic.net.server<br>ch.qos.logback.classic.pattern<br>ch.qos.logback.classic.pattern.color<br>ch.qos.logback.classic.selector<br>ch.qos.logback.classic.selector.servlet<br>ch.qos.logback.classic.servlet<br>ch.qos.logback.classic.sift<br>ch.qos.logback.classic.spi<br>ch.qos.logback.classic.turbo<br>ch.qos.logback.classic.util<br>ch.qos.logback.core<br>ch.qos.logback.core.boolex<br>ch.qos.logback.core.encoder<br>ch.qos.logback.core.filter<br>ch.qos.logback.core.helpers<br>ch.qos.logback.core.hook<br>ch.qos.logback.core.html<br>ch.qos.logback.core.joran<br>ch.qos.logback.core.joran.action<br>ch.qos.logback.core.joran.conditional<br>ch.qos.logback.core.joran.event<br>ch.qos.logback.core.joran.event.stax<br>ch.qos.logback.core.joran.node<br>ch.qos.logback.core.joran.spi<br>ch.qos.logback.core.joran.util<br>ch.qos.logback.core.joran.util.beans<br>ch.qos.logback.core.layout<br>ch.qos.logback.core.net<br>ch.qos.logback.core.net.server<br>ch.qos.logback.core.net.ssl<br>ch.qos.logback.core.pattern<br>ch.qos.logback.core.pattern.color<br>ch.qos.logback.core.pattern.parser<br>ch.qos.logback.core.pattern.util<br>ch.qos.logback.core.property<br>ch.qos.logback.core.read<br>ch.qos.logback.core.recovery<br>ch.qos.logback.core.rolling<br>ch.qos.logback.core.rolling.helper<br>ch.qos.logback.core.sift<br>ch.qos.logback.core.spi<br>ch.qos.logback.core.status<br>ch.qos.logback.core.subst<br>ch.qos.logback.core.util</td>
    <td>AEM as a Cloud Service does not support this internal log back API.</td>
    <td>1/27/2022</td>
    <td>3/24/2022</td>
  </tr>
  <tr>
    <td>org.slf4j.spi</td>
    <td>AEM as a Cloud Service does not support this internal log4j API.</td>
    <td>1/27/2022</td>
    <td>3/24/2022</td>
  </tr>
  <tr>
    <td>org.apache.log4j<br>org.apache.log4j.helpers<br>org.apache.log4j.spi<br>org.apache.log4j.xml</td>
    <td>Apache Log4j 1 has reached its end of life in 2015 and is no longer supported.</td>
    <td>1/27/2022</td>
    <td>3/24/2022</td>
  </tr>
  <tr>
    <td>org.apache.sling.commons.log.logback<br>org.apache.sling.commons.log.logback.webconsole</td>
    <td>AEM as a Cloud Service does not support this internal log back API.</td>
    <td>1/27/2022</td>
    <td>removed</td>
  </tr>
  <tr>
    <td>com.github.jknack.handlebars.js</td>
    <td>Handlebars upgrade required from 4.0.5 to 4.3.0 due to a security vulnerability. This package is no longer present in the upgraded handlebars.</td>
    <td>5/5/2022</td>
    <td>8/5/2022</td>
  </tr>
  <tr>
    <td>com.adobe.granite.resourceresolverhelper</td>
    <td>This API is not supported anymore. Use org.apache.sling.api.resource.ResourceResolverFactory instead.</td>
    <td>9/29/2022</td>
    <td>11/24/2022</td>
  </tr>
  <tr>
    <td>com.day.cq.contentsync.handler.util</td>
    <td>This API is deprecated. Use Apache Sling's Builders instead.</td>
    <td>10/31/2022</td>
    <td>1/01/2023</td>
  </tr>
  <tr><td>org.apache.sling.commons.json<br>org.apache.sling.commons.json.http<br>org.apache.sling.commons.json.io<br>org.apache.sling.commons.json.jcr<br>org.apache.sling.commons.json.sling<br>org.apache.sling.commons.json.util<br>org.apache.sling.commons.json.xml</td>
    <td>AEM as a Cloud Service does not support this API.</td>
    <td>5/15/2023</td>
    <td>6/15/2023</td>
  </tr><td>com.google.common.annotations<br>com.google.common.base<br>com.google.common.cache<br>com.google.common.collect<br>com.google.common.escape<br>com.google.common.eventbus<br>com.google.common.hash<br>com.google.common.html<br>com.google.common.io<br>com.google.common.math<br>com.google.common.net<br>com.google.common.primitives<br>com.google.common.reflect<br>com.google.common.util.concurrent<br>com.google.common.xml</td>
    <td>The Google Guava Core Libraries are deprecated.</td>
    <td>5/15/2023</td>
    <td>6/15/2023</td>
  </tr>
  <tr>
    <td>org.slf4j.event    </td>
    <td>AEM as a Cloud Service does not support this internal slf4j API.</td>
    <td>4/11/2022</td>
    <td>8/30/2024</td>
  </tr>
  <tr>
    <td>org.apache.sling.repoinit.jcr<br>org.apache.sling.repoinit.parser.operations</td>
    <td>Usage of this API is not supported in AEM as a Cloud Service.</td>
    <td>5/17/2024</td>
    <td>6/30/2024</td>
  </tr>
  <tr>
    <td>com.day.cq.xss<br>com.day.cq.xss.taglib<br>com.day.cq.xss.impl</td>
    <td>Use org.apache.sling.xss instead.</td>
    <td>12/12/2023</td>
    <td>6/30/2024</td>
  </tr>
  <tr>
    <td>com.adobe.granite.xss<br>com.adobe.granite.xss.impl</td>
    <td>Use org.apache.sling.xss instead.</td>
    <td>12/12/2023</td>
    <td>6/30/2024</td>
  </tr>  
  <tr>
    <td>com.drew.*</td>
    <td>Extracting metadata from images and videos should be done via Asset Compute in Cloud Service, or via Apache POI or Apache Tika.</td>
    <td>9/17/2024</td>
    <td>12/17/2024</td>
  </tr>
  <tr>
    <td>org.apache.jackrabbit.oak.plugins.blob.*</td>
    <td></td>
    <td>9/23/2024</td>
    <td>12/23/2024</td>
  </tr>       
</tbody>
</table>
</details>

### Removal of `org.apache.sling.commons.auth*` {#org.apache.sling.commons.auth}

If you are using `org.apache.sling.commons.auth`, or `org.apache.sling.commons.auth.spi`, or both, the usage can be replaced by migrating the code to `org.apache.sling.auth` resp. `org.apache.sling.auth.spi`. If you are using an old version of [ACS AEM Commons](https://adobe-consulting-services.github.io/acs-aem-commons/), make sure to update to the latest version.

Action list:

* Update ACS AEM Commons to latest version
* Migrate from `org.apache.sling.commons.auth` and/or `org.apache.sling.commons.auth.spi` to `org.apache.sling.auth` resp. `org.apache.sling.auth.spi`.

### Removal of `org.eclipse.jetty*` {#org.eclipse.jetty}

If you use anything from the package `org.eclipse.jetty` or one of its sub packages, you might want to migrate to other third-party libraries with a similar functionality. If migration is not feasible, add the required bundles from the below list to your project.

Action list:

* Replace usage of `org.eclipse.jetty` packages with other third-party libraries/own code or
* Select the required bundles from this list and add them to your project:
  * `org.eclipse.jetty:jetty-client:9.4.54.v20240208`
  * `org.eclipse.jetty:jetty-http:9.4.54.v20240208`
  * `org.eclipse.jetty:jetty-io:9.4.54.v20240208`
  * `org.eclipse.jetty:jetty-security:9.4.54.v20240208`
  * `org.eclipse.jetty:jetty-servlet:9.4.54.v20240208`
  * `org.eclipse.jetty:jetty-server:9.4.54.v20240208`
  * `org.eclipse.jetty:jetty-util:9.4.54.v20240208`
  * `org.eclipse.jetty:jetty-util-ajax:9.4.54.v20240208`

### Removal of `com.mongodb` {#com.mongodb}

Add the Mongo client API to your project.

Action list:

* Add this bundle to your project
  * `org.mongodb:mongo-java-driver:3.12.7`

### Usage of `org.apache.abdera*` and `org.apache.sling.atom.taglib` {#org.apache.abdera_or_org.apache.sling.atom.taglib}

Replace the usage of any package from `org.apache.abdera` and `org.apache.sling.atom.taglib` with a third-party library providing similar functionality or your own code.

Action list:

* Replace usage of packages from `org.apache.abdera` and `org.apache.sling.atom.taglib` with other third-party libraries/own code.

### Usage of `org.apache.felix.http.whiteboard` {#org.apache.felix.http.whiteboard}

Replace the usage of `org.apache.felix.http.whiteboard` with the [OSGi Http Whiteboard](https://docs.osgi.org/specification/osgi.cmpn/7.0.0/service.http.whiteboard.html). The official OSGi API has similar capabilities and replacing most often only requires to change the service registration properties.

Action list:

* Replace the usage of `org.apache.felix.http.whiteboard` with [OSGi Http Whiteboard](https://docs.osgi.org/specification/osgi.cmpn/7.0.0/service.http.whiteboard.html)

## OSGI Configuration {#osgi-configuration}

The two lists below reflect the AEM as a Cloud Service OSGi configuration surface, describing what customers can configure.

1. Customer code must not configure the listed OSGi configurations.
1. A list of OSGi configurations whose properties may be configured, but must abide by the indicated validation rules. These rules include whether declaration of the property is required, its type, and in some cases, its allowed range of values.

Customer code may configure any OSGi configuration not listed.

These rules are validated during the Cloud Manager build process. Additional rules may be added over time and the expected enforcement date is noted in the table. Customers are expected to abide by these rules by the target enforcement date. Not abiding by the rules after the removal date generates errors in the Cloud Manager build process. Maven projects should include the [AEM as a Cloud Service SDK Build Analyzer Maven Plugin](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/developing/archetype/build-analyzer-maven-plugin) to flag OSGI configuration errors during local SDK development.

Additional information about OSGI configuration can be found at [this location](/help/implementing/deploying/configuring-osgi.md).

+++OSGi configurations that cannot be modified.

  * **`org.apache.felix.webconsole.internal.servlet.OsgiManager`** (Announcement Date: 4/30/2021, Enforcement Date: 7/31/2021)
  * **`com.day.cq.auth.impl.cug.CugSupportImpl`** (Announcement Date: 4/30/2021, Enforcement Date: 7/31/2021)
  * **`com.day.cq.jcrclustersupport.ClusterStartLevelController`** (Announcement Date: 4/30/2021, Enforcement Date: 7/31/2021)
  * **`org.apache.felix.http (Factory)`** (Announcement Date: 4/30/2021, Enforcement Date: 7/31/2021)
  * **`org.apache.sling.jcr.davex.impl.servlets.SlingDavExServlet`** (Announcement Date: 8/25/2021, Enforcement Date: 11/26/2021)
+++

+++OSGi configurations subject to build validation rules.

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
+++

## Java runtime update to version 21 {#java-runtime-update-21}

Adobe Experience Manager as a Cloud Service is transitioning to the Java 21 runtime. To ensure compatibility, updating library versions as outlined in [Runtime requirements](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#runtime-requirements) is essential.

<!-- (OLD Removed from here to end of topic 1/16/25 as per instruction in https://wiki.corp.adobe.com/pages/viewpage.action?pageId=3359689801) AEM as a Cloud Service will be moving to Java 21 runtime. In order to ensure compatibility, it is essential to make the following adjustments:

### Runtime Requirements

These adjustments are required to ensure compatibility with the Java 21 runtime. The libraries can be updated at any time as they are compatible with older versions of Java.

#### Minimum version of org.objectweb.asm {#org.objectweb.asm}

Update the usage of org.objectweb.asm to version 9.5 or higher to ensure support for newer JVM runtimes.

#### Minimum version of org.apache.groovy {#org.apache.groovy}

Update the usage of org.apache.groovy to version 4.0.22 or higher to ensure support for newer JVM runtimes.

This bundle can be indirectly included by adding third party dependencies such as the AEM Groovy Console.

### Build-time Requirements

These adjustments are required to allow building the project with newer versions of Java but not required for runtime compatibility. The Maven plug-ins can be updated at any time as they are compatible with older versions of Java.

#### Minimum version of bnd-maven-plugin {#bnd-maven-plugin}

Update the usage of bnd-maven-plugin to version 6.4.0 to ensure support for newer JVM runtimes. Versions 7 or higher are not compatible with Java 11 or lower so an upgrade to that version is not recommended at this time.

#### Minimum version of aemanalyser-maven-plugin {#aemanalyser-maven-plugin}

Update the usage of aemanalyser-maven-plugin to version 1.6.6 or higher to ensure support for newer JVM runtimes.

#### Minimum version of maven-bundle-plugin  {#maven-bundle-plugin}

Update the usage of maven-bundle-plugin to version 5.1.5 or higher to ensure support for newer JVM runtimes.

#### Update dependencies in maven-scr-plugin  {#maven-scr-plugin}

The `maven-scr-plugin` is not directly compatible with Java 17 and 21. However, it is possible to generate the descriptor files by updating the ASM dependency version within the plugin configuration, similar to the snippet below: 

```
[source,xml]
 <project>
   ...
   <build>
     ...
     <plugins>
       ...
       <plugin>
         <groupId>org.apache.felix</groupId>
         <artifactId>maven-scr-plugin</artifactId>
         <version>1.26.4</version>
         <executions>
           <execution>
             <id>generate-scr-scrdescriptor</id>
             <goals>
               <goal>scr</goal>
             </goals>
           </execution>
         </executions>
         <dependencies>
           <dependency>
             <groupId>org.ow2.asm</groupId>
             <artifactId>asm-analysis</artifactId>
             <version>9.7.1</version>
             <scope>compile</scope>
           </dependency>
         </dependencies>
       </plugin>
       ...
     </plugins>
     ...
   </build>
   ...
 </project>
```
-->
