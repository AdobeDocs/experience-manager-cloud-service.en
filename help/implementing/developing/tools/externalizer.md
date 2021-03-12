---
title: Externalizing URLs
description: The Externalizer is an OSGi service that allows you to programmatically transform a resource path into an external and absolute URL.
---

# Externalizing URLs {#externalizing-urls}

In AEM, the **Externalizer** is an OSGi service that allows you to programmatically transform a resource path (e.g. `/path/to/my/page`) into an external and absolute URL (for example, `https://www.mycompany.com/path/to/my/page`) by prefixing the path with a pre-configured DNS.

Because an AEM as a Cloud Service instance cannot know its externally visible URL and because sometimes a link has to be created outside of the request scope, this service provides a central place to configure those external URLs and build them.

This article explains how to configure the Externalizer service and how to use it. For technical details of the service, please refer to the [Javadocs](https://docs.adobe.com/content/help/en/experience-manager-cloud-service-javadoc/com/day/cq/commons/Externalizer.html).

## Default Values for AEM as a Cloud Service {#default-values}

By default, the Externalizer service will have values such as `author-p12345-e6789.adobeaemcloud.com` and `publish-p12345-e6789.adobeaemcloud.com`.

To override such values, use Cloud Manager environment variables as described in the article [Configuring OSGi for AEM as a Cloud Service](/help/implementing/deploying/configuring-osgi.md#cloud-manager-api-format-for-setting-properties) and setting the predefined `AEM_CDN_DOMAIN_AUTHOR` and `AEM_CDN_DOMAIN_PUBLISH` variables.

## Configuring the Externalizer Service {#configuring-the-externalizer-service}

The Externalizer service allows you to centrally define the domain that can be used to programmatically prefix resource paths. The Externalizer service should only be used for applications with a single domain.

>[!NOTE]
>
>As when applying any [OSGi configurations for AEM as a Cloud Service,](/help/implementing/deploying/overview.md#osgi-configuration) the following steps should be performed on a local developer instance and then committed to your project code for deployment.

To define a domain mapping for the Externalizer service:

1. Navigate to the Configuration Manager via:

   `https://<host>:<port>/system/console/configMgr`

1. Click **Day CQ Link Externalizer** to open the configuration dialog box.

   ![The Externalizer OSGi configuration](./assets/externalizer-osgi.png)

   >[!NOTE]
   >
   >The direct link to the configuration is `https://<host>:<port>/system/console/configMgr/com.day.cq.commons.impl.ExternalizerImpl`

1. Define a **Domains** mapping. A mapping consists of a unique name that can be used in the code to reference the domain, a space, and the domain:

   `<unique-name> [scheme://]server[:port][/contextpath]`

   Where:

    * **`scheme`** is usually http or https, but can be another protocol.

        * It is recommended to use https to enforce https links.
        * It will be used if the client code does not override the scheme when asking for externalization of a URL.

    * **`server`** is the host name (either a domain name or ip address).
    * **`port`** (optional) is the port number.
    * **`contextpath`** (optional) is only set if AEM is installed as a webapp under a different context path.

   For example: `production https://my.production.instance`

   The following mapping names are predefined and must always be set as AEM relies on them:

    * `local` - the local instance
    * `author` - the authoring system DNS
    * `publish` - the public facing website DNS

   >[!NOTE]
   >
   >A custom configuration allows you to add a new category, such as `production`, `staging` or even external non-AEM systems such as `my-internal-webservice`. It is useful to avoid hard coding such URLs across different places in a project's codebase.

1. Click **Save** to save your changes.

### Using the Externalizer service {#using-the-externalizer-service}

This section shows a few examples of how the Externalizer service can be used:

1. **To get the Externalizer service in a JSP:**

   ```java
   Externalizer externalizer = resourceResolver.adaptTo(Externalizer.class);
   ```

1. **To externalize a path with the 'publish' domain:**

   ```java
   String myExternalizedUrl = externalizer.publishLink(resolver, "/my/page") + ".html";
   ```

   Assuming the domain mapping:

    * `publish https://www.website.com`

   `myExternalizedUrl` ends up with the value:

    * `https://www.website.com/contextpath/my/page.html`

1. **To externalize a path with the 'author' domain:**

   ```java
   String myExternalizedUrl = externalizer.authorLink(resolver, "/my/page") + ".html";
   ```

   Assuming the domain mapping:

    * `author https://author.website.com`

   `myExternalizedUrl` ends up with the value:

    * `https://author.website.com/contextpath/my/page.html`

1. **To externalize a path with the 'local' domain:**

   ```java
   String myExternalizedUrl = externalizer.externalLink(resolver, Externalizer.LOCAL, "/my/page") + ".html";
   ```

   Assuming the domain mapping:

    * `local https://publish-3.internal`

   `myExternalizedUrl` ends up with the value:

    * `https://publish-3.internal/contextpath/my/page.html`

1. You can find more examples in the [Javadocs](https://docs.adobe.com/content/help/en/experience-manager-cloud-service-javadoc/com/day/cq/commons/Externalizer.html).
