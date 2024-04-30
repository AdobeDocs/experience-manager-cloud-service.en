---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release X {#release-X}

Summarized below are the continuous improvements for maintenance release X, which was publicly released on April 24, 2024. The previous maintenance release was release 15977.

2024.4.0 Feature Activation provides the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-X}

* **(For AEM Forms only)** After installing AEM Cloud Foundation maintenance release 15977, Adaptive Form fields are rendering in the incorrect order during form authoring and for published forms. If you use AEM Forms, Adobe recommends that you do not upgrade to the 15977 release until the issue is resolved in the upcoming maintenance release. Doing so can help you avoid any inconvenience.

### Fixed Issues {#fixed-issues-X}

None.

### Known Issues {#known-issues-X}

None.

### Deprecated Features and APIs {#deprecated-X}

* [JWT Credentials Deprecation in Adobe Developer Console](/help/security/jwt-credentials-deprecation-in-adobe-developer-console.md)

* Effective May 1, 2024, Adobe Dynamic Media is ending support for the following:

  * SSL (Secure Socket Layer) 2.0
  * SSL 3.0 
  * TLS (Transport Layer Security) 1.0 and 1.1
  * The following weak ciphers in TLS 1.2:
    * `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`
    * `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`
    * `TLS_RSA_WITH_AES_256_GCM_SHA384`
    * `TLS_RSA_WITH_AES_256_CBC_SHA256`
    * `TLS_RSA_WITH_AES_256_CBC_SHA`
    * `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`
    * `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`
    * `TLS_RSA_WITH_AES_128_GCM_SHA256`
    * `TLS_RSA_WITH_AES_128_CBC_SHA256`
    * `TLS_RSA_WITH_AES_128_CBC_SHA`
    * `TLS_RSA_WITH_CAMELLIA_256_CBC_SHA`
    * `TLS_RSA_WITH_CAMELLIA_128_CBC_SHA`
    * `TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA`
    * `TLS_RSA_WITH_SDES_EDE_CBC_SHA`


To know what is deprecated or removed in AEM as a Cloud Service, see [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md).

### Embedded Technologies {#embedded-tech-X}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.62.0|[Oak API 1.62.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.62.0/index.html)| 
|AEM SLING API | 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.24.6|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
