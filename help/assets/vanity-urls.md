---
title: Create Vanity URLs using Dynamic Media with OpenAPI Capabilities
description: Use Dynamic Media OpenAPI capabilities to transform your long asset delivery URLs into short, branded vanity URLs. A vanity URL is a short, clean, easy-to-remember and readable version of your complex delivery URL. You can include your brand name, product names, and relevant keywords in the vanity URL to boost your brand visibility and user engagement
role: Admin
feature: Asset Management, Publishing, Collaboration, Asset Processing
---

# Use vanity URLs?{#vanity-urls}

Use [!DNL Dynamic Media OpenAPI capabilities] to transform your long asset delivery URLs into short, branded vanity URLs. Standard asset delivery URLs include system-generated asset UUIDs that make the delivery URL complex, hard to remember and share. Replace these asset UUIDs with simple identifiers (Vanity IDs) to generate a vanity URL. A vanity URL is a short, clean, and readable version of your complex delivery URL.

See the following URL formats to understand their difference:
* [Standard delivery URL](#standard-urls)
* [Vanity URLs](#vanity-url)

Standard delivery URLs use `aaid` followed by a UUID, while vanity URLs use `avid` followed by a custom identifier (vanity identifier).

Use short and simple vanity identifiers, to make your delivery URL short, clean, readable, easy-to-remember and share. Use your brand name, product names, and relevant keywords as vanity IDs to boost your brand visibility and user engagement. 

When your user clicks your vanity URL, [!DNL Dynamic Media with OpenAPI] automatically maps to the original asset location at ingestion time and resolve them properly at delivery time to server the asset to the user. 

Learn to [create Vanity URLs](#create-vanity-urls).

## Standard Delivery URLs{#standard-urls}

The standard [!DNL Dynamic Media with OpenAPI] asset delivery URL includes a unique system-generated identifier and follows the following format.

***Format:*** `https://delivery-<tenant>.adobeaemcloud.com/adobe/assets/urn:aaid:aem:<asset-uuid>/as/<seoname>.<format>`

The standard delivery URL includes `aaid` (*actual asset identifier*) after `urn:` and a UUID between `urn:aaid:aem:` and `/as/<seoname>.<format>`.

***Example:*** `https://delivery-p30902-e145436.adobeaemcloud.com/adobe/assets/urn:aaid:aem:43341ab1-4086-44d2-b7ce-ee546c35613b/as/check.jpeg`

In the above example, `43341ab1-4086-44d2-b7ce-ee546c35613b` is the UUID.

## Vanity URLs{#vanity-url}

The vanity URLs includes a vanity identifier in place of asset UUID and follows the following format.

***Format:*** `https://delivery-<tenant>.adobeaemcloud.com/adobe/assets/urn:avid:aem:<vanity-id>/<seoname>.<format>`

The vanity URL includes `avid` (*actual vanity identifier*) after `urn:` and your vanity ID between `urn:avid:aem:` and `/<seoname>.<format>`.

***Example:*** `https://delivery-p30902-e145436.adobeaemcloud.com/adobe/assets/urn:avid:aem:VanityCheck/as/check.jpeg`

In the above example, `VanityCheck` is the vanity ID that replaced the UUID.

## Explore key capabilities and benefits{#capabilities-and-benefits-of-vanity-urls}

Using meaningful vanity IDs to customize the standard asset delivery URLs provides several advantages and measurable impact. Some of the key capabilities and benefits of vanity URLs include the following.

### Key capabilities{#key-capabilities}

* **URL customization:** Replace long identifiers (asset UUIDs) in the delivery URL with shorter, brand-aligned alternatives to generate a cleaner delivery URL.
* **Real-time redirection:** Vanity URLs redirect to original asset UUIDs at runtime without disrupting workflows. Users see clean URLs in the address bar while the system handles the technical routing.
* **Easy link management:** Customize your vanity URLs at any time without affecting asset delivery performance.

### Key benefits{#key-benefits}

* **Enhances user experience:** Clean and shorter vanity URLs are readable, user-friendly, easy to remember and share.

* **Improves user engagement:** Branded URLs build user confidence and trust. Users are more likely to click professional, branded links, resulting in higher click-through rates.

* **SEO optimization:** URLs that include relevant keywords improve search engine rankings and discoverability.

* **Enhanced brand visibility:** Brand-specific URLs strengthen brand presence across all marketing channels, including email, social media, and advertising campaigns.
Also, consistent use of branded URLs in all communications reinforces brand identity and recognition.

* **Campaign tracking and analytics:** Use unique vanity URLs for different campaigns and channels to gain detailed insights into traffic sources and conversion performance.

## Prerequisites{#prerequisites-for-creating-vanity-id}

To create the vanity URL, ensure you have already [approved the assets for public delivery](/help/assets/manage-organize-assets-view.md#manage-asset-status).

## Create Vanity URLs{#create-vanity-urls}

Execute the following steps to create vanity URLs:
1. [Set up asset metadata](#set-up-asset-metadata)
1. [Create and map Cloud manager environment variable](#map-cloud-manager-environment-variable)
1. [Approve the assets requiring vanity URL for delivery](/help/assets/manage-organize-assets-view.md#manage-asset-status)
1. [Generate vanity URLs](#generate-vanity-urls)

### Set up asset metadata{#set-up-asset-metadata}

Execute the following to set up the vanity ID in your asset's metadata form:
1. Navigate to the details page of the folder holding your assets for [!DNL Dynamic Media with OpenAPI] delivery.
1. [Edit that metadata form](/help/assets/metadata-assets-view.md#edit-metadata-forms) by doing one of the following:
   * Add a new metadata field and specify the required vanity ID as the value of that field.
   * Update existing field by replacing an existing metadata property's value with the required vanity ID. Learn the [best practices](#best-practices) for creating the vanity ID.
   ![vanity ID](/help/assets/assets/vanity-id-metadata.png)
   Learn more about [metadata schemas](/help/assets/metadata-schemas.md).
   
     >[!NOTE]
     >
     > * Use unique vanity IDs for each asset. Always verify that assets sharing the same metadata form have unique vanity IDs for DM with OpenAPI delivery through vanity URLs. If two assets share the same vanity ID, DM with OpenAPI delivers the asset that most recently received that ID, overriding the previous entitlement of the ID to another asset.
     >
     > * A single asset can have multiple vanity IDs. [Contact Adobe support](https://helpx.adobe.com/in/contact.html) and raise a request for generating the required vanity IDs.

After setting up your vanity ID in the asset metadata form, [map this metadata field to the system's delivery mechanism](#map-cloud-manager-environment-variable).

### Create and map Cloud manager environment variable{#map-cloud-manager-environment-variable}

Execute the following steps to create an environment variable and map it to the metadata field holding the vanity ID:

1. [Navigate to the configurations page of your Cloud Manager environment](/help/implementing/cloud-manager/environment-variables.md) and do the following:
   1. Add `ASSET_DELIVERY_VANITY_ID` variable. This is the key.
   1. Use the value field to map to the metadata property that holds the vanity ID. The mapping follows the `dc:<your-metadata-property>` format, where the metadata mapping prefix (such as dc:) varies based on your metadata configuration property.
   ![ASSET_DELIVERY_VANITY_ID variable](/help/assets/assets/environment-config.png)
1. Save your changes to restart the pods in your environment.

### Approve the assets for delivery{#approve-assets-for-delivery}

After mapping the `ASSET_DELIVERY_VANITY_ID` variable in your Cloud Manager environment to the asset metadata property that holds the vanity ID, [approve your assets that require vanity URL for delivery](/help/assets/manage-organize-assets-view.md#manage-asset-status).

### Generate Vanity URLs{#generate-vanity-urls}

Make the following replacements in your standard delivery URL to transform it into a vanity URL:

* Replace **UUID** with your **vanity ID**.
* Replace `aaid` with `avid`.

See the [URL transformation from standard to vanity URL](#standard-urls) above.
Learn how to [copy Dynamic Media with OpenAPI delivery URLs](/help/assets/approve-assets.md#copy-delivery-url-for-approved-assets) for your assets.

When your user clicks the vanity URL, [!DNL Dynamic Media with OpenAPI] automatically maps the vanity ID to the original asset UUID at ingestion time and resolves them properly at delivery time to serve the asset to the user without any delay. You can customize the vanity URL in real time without affecting the asset delivery performance.

[Enhance the impact of your vanity URLs using the advanced customization capabilities of AEM Cloud Service.](#scale-using-vanity-url)

## Scale using vanity URLs{#scale-using-vanity-url}

AEM as a Cloud Service enables you to [customize the DNS and CDN names](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/custom-domain-names/introduction) within your web addresses. Use these AEMCS capabilities with your vanity URLs to transforms them into unique web-addresses that are clean, descriptive, branded, intuitive and provide the [above-mentioned benefits](#key-benefits).

See the following vanity URL and its customizable components:

**Vanity URL format:**

`https://delivery-<tenant>.adobeaemcloud.com/adobe/assets/urn:avid:aem:<vanity-id>/<seoname>.<format>`

<table style="border-collapse:collapse; table-layout:auto; width:auto;">
<tr valign="top">
<td style="padding:0 4px; white-space:nowrap; text-align:center;">
<div style="text-align:left;"><code>https://delivery&#8209;&lt;tenant&gt;.adobeaemcloud.com</code></div>
<div style="text-align:center;">↓</div>
<div style="text-align:center;"><a href="#customize-dns">Customize this DNS</a></div>
</td>
<td style="padding:0 6px; white-space:nowrap; text-align:center;">/</td>
<td style="padding:0 4px; white-space:nowrap; text-align:center;">
<div style="text-align:left;"><code>adobe/assets/urn:avid:aem:</code></div>
<div style="text-align:center;">↓</div>
<div style="text-align:center;"><a href="#rewrite-cdn-rules">Customize URL with rewrite rules</a></div>
</td>
<td style="padding:0 4px; white-space:nowrap; text-align:center;">
<div style="text-align:left;"><code>&lt;vanity-id&gt;</code></div>
<div style="text-align:center;">↓</div>
<div style="text-align:center;"><a href="#create-vanity-urls">Create vanity ID</a></div>
</td>
<td style="padding:0 4px; white-space:nowrap; text-align:left; width:1%;">
<code>/&lt;seoname&gt;.&lt;format&gt;</code>
</td>
</tr>
</table>.

**Vanity URL format with customized DNS and CDN names:**

`https://<custom-dns>` `/` `dam/assets/` `<vanity-id>` `/<seoname>.<format>`

**Customizable URL Components**

* ***[DNS name (hostname):](#customize-DNS)*** `https://delivery-<tenant>.adobeaemcloud.com` is the server domain that hosts your assets. [Customize DNS to change the hostname](#customize-DNS).
* ***[CDN rewrite rules:](#rewrite-cdn-rules)*** `adobe/assets/urn:avid:aem:` is the path structure that identifies asset types and delivery methods. [Rewrite CDN rules](#rewrite-cdn-rules) to modify the domain path.

### Customize DNS{#customize-dns}

[Raise a request to Adobe support](https://helpx.adobe.com/in/contact.html) to generate the required custom DNS for your delivery tier. Follow these [best practices](#best-practices) for creating custom DNS names.

### Rewrite CDN rules{#rewrite-cdn-rules}

Execute the following steps to rewrite the CDN rules for delivery:

1. Navigate to your AEM repository to create a YAML configuration file.
2. Execute the steps in [setup](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/cdn-error-pages#setup) section to configure CDN rules and deploy the configuration through your Cloud Manager configuration pipeline. 
Follow these [best practices](#best-practices) for creating your domain path.
[Learn more about CDN rewriting rules](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/cdn-configuring-traffic#request-transformations).

The following are examples of rewrite rules for appending file names with extensions in vanity URLs. Customize these rewrite rules according to your specific requirements. [Contact Adobe support](https://helpx.adobe.com/in/contact.html) for further assistance:

```- name: cdn-rewrite-rule
  when:
    allOf:
      - reqProperty: tier
        equals: delivery
```

#### For SVG, GIF, and PDF {#svg-gif-pdf}

```
    type: transform
      reqProperty: path
      op: replace
      match: ^/dam/assets/([^/]+\.(?:svg|gif|pdf|docx|xlsx))(\?.*)?$
      replacement: /adobe/assets/urn:avid:aem:\1/original/as/\1\2
```

#### For video{#video}

For videos including MP4, MOV, AVI and MKV

``` 
type: transform
      reqProperty: path
      op: replace
      match: ^/dam/assets/([^/]+\.(?:mp4|mov|avi|mkv))(\?.*)?$
      replacement: /adobe/assets/urn:avid:aem:\1/play\2
```

#### For image{#image}

For all image types, excluding SVG.

```
type: transform
      reqProperty: path
      op: replace
      match: ^/dam/assets/([^/]+\.[^/]+)(\?.*)?$
      replacement: /adobe/assets/urn:avid:aem:\1/as/\1\2
```

## Follow the best practices for creating clean vanity URLs{#best-practices}

Follow these best practices for creating vanity IDs, custom DNS and domain names:

1. Do not use special characters in vanity IDs, such as spaces, slashes, hyphens and more. The system replaces special characters in vanity IDs using a predefined mapping.
1. Use your brand name, product names, and relevant keywords in your vanity IDs, custom DNS and domain names to boost your brand visibility and user engagement.
1. Use short, descriptive words or strings that convey meaning.
1. Use texts that invite users for clicks.
