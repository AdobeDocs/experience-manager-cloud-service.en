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

## Restrict anonymous access to system properties {#restrict-anonymous-access-to-system-properties}

AEM stores system metadata, such as `jcr:createdBy` and `jcr:lastModifiedBy`, as node properties alongside regular content in the repository. Depending on the configuration and access control setup, rendering these nodes as JSON or XML may expose personally identifiable information (PII).

As with other repository data, access to these properties is controlled by the Oak authorization stack. Restrict access according to the principle of least privilege.

In AEM as a Cloud Service, you can use [Repo Init](/help/implementing/deploying/overview.md#repoinit) to configure a deny access control entry at the repository root, restricting anonymous access to specific system properties.

### Configuration steps {#configuration-steps}

1. In your AEM project, create a configuration file in the following directory:

   `ui.config/src/main/content/jcr_root/apps/<name-of-program>/osgiconfig/config.publish/`

   Use the following file name:

   `org.apache.sling.jcr.repoinit.RepositoryInitializer-anonymousPermissions.config`

1. Add the following configuration to the file:

   ```text
   scripts=["
       set ACL on /
           deny jcr:all for anonymous restriction(rep:itemNames, jcr:createdBy,jcr:lastModifiedBy,cq:lastModifiedBy,cq:lastReplicatedBy,cq:lastRolledoutBy)
       end
   "]
   ```

   The `rep:itemNames` restriction limits the deny entry to the listed names. This configuration restricts anonymous access to the following properties:

   * `jcr:createdBy`
   * `jcr:lastModifiedBy`
   * `cq:lastModifiedBy`
   * `cq:lastReplicatedBy`
   * `cq:lastRolledoutBy`

1. Commit and push the configuration file to your Git repository, then deploy it through a Cloud Manager pipeline. Configuration placed in `config.publish` applies to the Publish environment.

After the configuration takes effect, the targeted properties are no longer visible in JSON or XML output generated using the anonymous user's repository permissions.

>[!NOTE]
>
>Responses cached before the configuration change may still contain the targeted properties. Invalidate the relevant caches as needed.

<!--
Commenting out section for now as requested by Lars

## Anonymous Permission Hardening Package {#anonymous-permission-hardening-package}

For more information on the Anonymous Hardening Package, see [Security Checklist](https://experienceleague.adobe.com/docs/experience-manager-65/administering/security/security-checklist.html#anonymous-permission-hardening-package).
-->
