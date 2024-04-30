---
title: AEM as a Cloud Service Security Considerations
description: Learn about important security considerations when using AEM as a Cloud Service.
hidefromtoc: yes
hide: yes
exl-id: d2dfde05-ce02-478e-8697-b939fb8740c3
---
# AEM as a Cloud Service Security Considerations {#security-considerations}

## AEM Trust Store {#aem-trust-store}

To support asymmetric, cryptographic operations, AEM stores certificates inside the content repository, in a global trust-store. Its contents are public and, by default, are anonymously accessible by everyone on publisher instances.

### Characteristics of the Trust Store {#truststore-characteristics}

* The trust-store is located below `/etc/truststore` and consists of a Java&trade; keystore file, the keystore password, and repository metadata. Both the password and the keystore are encrypted for technical reasons, even though the contained certificates are accessible to everyone by default through the API
* Out of the box the certificates are used for HTTPS and SAML support only, and the store must be manually created first
* Customers can use it in their own code through the [keystore API](https://developer.adobe.com/experience-manager/reference-materials/6-5/javadoc/com/adobe/granite/keystore/KeyStoreService.html#getTrustStore-org.apache.sling.api.resource.ResourceResolver-)
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
