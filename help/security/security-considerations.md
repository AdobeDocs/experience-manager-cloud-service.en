---
title: AEM as a Cloud Service Security Considerations
description: Learn about important security considerations when using AEM as a Cloud Service
hidefromtoc: yes
hide: yes
---

# AEM as a Cloud Service Security Considerations {#security-considerations}

## Anonymous Permission Hardening Package {#anonymous-permission-hardening-package}

By default, AEM stores system metadata, such as `jcr:createdBy` or `jcr:lastModifiedBy` as node properties, next to regular content, in the repository. Depending on the configuration and the access control setup, in some cases this could lead to exposure of personally identifiable information (PII), for example when such nodes are rendered as raw JSON or XML. 

Like all repository data, these properties are mediated by the Oak authorization stack. Access  to them should be restricted in accordance with the principle of least privilege.

To support this, Adobe provides a permission hardening package as a basis for customers to build upon. It works by installing a "deny" access control entry at the repository root, restricting anonymous access to commonly used system properties. The package is available for download [here](https://experience.adobe.com/#/downloads/content/software-distribution/en/aem.html?package=/content/software-distribution/en/details.html/content/dam/aem/public/adobe/packages/helper/anonymous-permissions-pkg-0.1.2.zip) and can be installed on all supported versions of AEM. Please see the release notes for more information.

## AEM Trust Store {#aem-trust-store}

In order to support asymmetric, cryptographic operations, AEM stores certificates inside the content repository, in a global trust-store. Its contents are public and, by default, are anonymously accessible by everyone on publisher instances.

### Characteristics of the Trust Store {#truststore-characteristics}

* The trust-store is located below `/etc/truststore` and consists of a Java keystore file, the keystore password and repository metadata. Note that both the password and the keystore itself are encrypted for technical reasons, even though the contained certificates are accessible to everyone by default through the API
* Out of the box the certificates are used for HTTPS and SAML support only, and the store must be manually created first
* Customers can use it in their own code through the [keystore API](https://developer.adobe.com/experience-manager/reference-materials/6-5/javadoc/com/adobe/granite/keystore/KeyStoreService.html#getTrustStore-org.apache.sling.api.resource.ResourceResolver-)
* The trust-store can be managed through the UI at **Tools** - **Security** - **Trust Store** or by accessing *`https://serveraddress:serverport/libs/granite/security/content/truststore.html`*
* Access to the trust-store can be further restricted by repository access control depending on the use-case.