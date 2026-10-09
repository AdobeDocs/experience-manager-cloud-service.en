---
title: AEM as a Cloud Service Security Considerations
description: Learn about important security considerations when using AEM as a Cloud Service.
hide: true
exl-id: d2dfde05-ce02-478e-8697-b939fb8740c3
feature: Security
role: Admin
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: b1210526-416b-4ef6-bcc0-1692e99f30e9
    internal-label: Administration and security
subfeature_v2:
  - id: c35bc059-fd80-4a01-91a6-e48da3c76758
    internal-label: Security practices
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---
# AEM as a Cloud Service Security Considerations {#security-considerations}

## AEM Trust Store {#aem-trust-store}

To support asymmetric, cryptographic operations, AEM stores certificates inside the content repository, in a global trust-store. Its contents are public and, by default, are anonymously accessible by everyone on publisher instances.

### Characteristics of the Trust Store {#truststore-characteristics}

* The trust-store is located below `/etc/truststore` and consists of a Java&trade; keystore file, the keystore password, and repository metadata. Both the password and the keystore are encrypted for technical reasons, even though the contained certificates are accessible to everyone by default through the API
* Out of the box the certificates are used for HTTPS and SAML support only, and the store must be manually created first
* Customers can use it in their own code through the [keystore API](https://experienceleague.adobe.com/en/tools/aem-api-documentation/6-5/javadoc/com/adobe/granite/keystore/KeyStoreService.html#getTrustStore-org.apache.sling.api.resource.ResourceResolver-)
* The trust-store can be managed through the UI at **Tools** - **Security** - **Trust Store** or by accessing *`https://serveraddress:serverport/libs/granite/security/content/truststore.html`*, as shown below:

  ![Trust Store Management](/help/security/assets/global-trust-store-modified.png)

* Access to the trust-store can be further restricted by repository access control depending on the use-case.

>[!NOTE]
>
>Adobe recommends that the default access controls be used for the Trust Store, which means that it remains publicly accessible. For the most secure configuration, you can use a policy of deny `jcr:all` for everyone.

<!--
Commenting out section for now as requested by Lars

## Anonymous Permission Hardening Package {#anonymous-permission-hardening-package}

For more information on the Anonymous Hardening Package, see [Security Checklist](https://experienceleague.adobe.com/docs/experience-manager-65/administering/security/security-checklist.html#anonymous-permission-hardening-package).
-->
