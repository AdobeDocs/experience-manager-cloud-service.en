---
title: Create Vanity URLs using Dynamic Media with OpenAPI Capabilities
description: Use Dynamic Media OpenAPI capabilities to transform your long asset delivery URLs into short, branded vanity URLs. A vanity URL is a short, clean, easy-to-remember and readable version of your complex delivery URL. You can include your brand name, product names, and relevant keywords in the vanity URL to boost your brand visibility and user engagement
role: Admin
feature: Asset Management, Publishing, Collaboration, Asset Processing
---

# What are Vanity URLs?{#vanity-urls}

Use [!DNL Dynamic Media OpenAPI capabilities] to transform your long asset delivery URLs into short, branded vanity URLs. Standard asset delivery URLs include system-generated asset UUIDs that make the delivery URL complex, hard to remember and share. Replace these asset UUIDs with vanity identifiers (Vanity IDs) to generate Vanity URL. A vanity URL is a short, clean, and readable version of your complex delivery URL.

See the following URL formats to understand their difference:
* [Standard delivery URL](#standard-urls)
* [Vanity URLs](#vanity-url)

Standard delivery URLs use `aaid` followed by a UUID, while vanity URLs use `vid` followed by a custom identifier (vanity identifier).

Use short and simple vanity IDs, to make your delivery URL short, clean, readable, easy-to-remember and share. Use your brand name, product names, and relevant keywords as vanity IDs to boost your brand visibility and user engagement. 

When your user click your vanity URL, Dynamic Media with OpenAPI automatically redirects to the original asset location. 

Learn to [create Vanity URLs](#create-vanity-urls).

## Standard Delivery URLs{#standard-urls}

The standard Dynamic Media with OpenAPI asset delivery URL includes a unique system-generated identifier and follows the following format.

***Format:*** `https://delivery-<tenant>.adobeaemcloud.com/adobe/assets/urn:aaid:aem:<asset-uuid>/as/seoname.jpg`

***Example:*** `https://delivery-p30902-e145436-cmstg.adobeaemcloud.com/adobe/assets/urn:aaid:aem:43341ab1-4086-44d2-b7ce-ee546c35613b/as/chekc.jpeg`

The standard delivery URL includes `aaid` after `urn:` and a UUID between `urn:aaid:aem:` and `/as/seoname.jpg`, where **aaid** stands for *actual asset identifier*.

In the above example `43341ab1-4086-44d2-b7ce-ee546c35613b` is the UUID.

## Vanity URLs{#vanity-url}

The vanity URLs includes a vanity identifier in place of aaset UUID and follows the following format.

***Format:*** `https://delivery-<tenant>.adobeaemcloud.com/adobe/assets/urn:vid:aem:<vanity-id>/<rendition-path>`

***Example:*** `https://delivery-p30902-e145436-cmstg.adobeaemcloud.com/adobe/assets/urn:avid:aem:VanityCheck/as/chekc.jpeg`

The vanity URL includes `vid` after `urn:` and your vanity ID between `urn:avid:aem:` and `/as/seoname.jpg`, where **vid** stands for *vanity identifier*.

In the above example, `VanityCheck` is the vanity ID that replaced the UUID.

## Explore key capabilities and benefits{#capabilities-and-benefits-of-vanity-urls}

Using meaningful vanity IDs to customize the standard asset delivery URLs, provides several advantages and measurable impact. Some of the key capabilities and benefits of vanity URLs include the following.

**Key capabilities:**

* **URL customization:** Replace long identifiers (asset UUIDs) in the delivery URL with shorter, brand-aligned alternatives to generate a cleaner delivery URL.
* **Real-time redirection:** Vanity URLs redirect to original asset UUIDs at runtime without disrupting workflows. Users see clean URLs in the address bar while the system handles the technical routing.
* **Easy link management:** Customize your vanity URLs at any time without affecting asset delivery performance.

**Key benefits:**

* **Enhances user experience:** Clean and shorter vanity URLs are readable, user-friendly, easy to remember and share.

* **Improves user engagement:** Branded URLs build user confidence and trust. Users are more likely to click professional, branded links, resulting in higher click-through rates.

* **SEO optimization:** URLs that include relevant keywords improve search engine rankings and discoverability.

* **Enhanced brand visibility:** Brand-specific URLs strengthen brand presence across all marketing channels, including email, social media, and advertising campaigns.
Also, consistent use of branded URLs in all communications reinforces brand identity and recognition.

* **Campaign tracking and analytics:** Use unique Vanity URLs for different campaigns and channels to gain detailed insights into traffic sources and conversion performance.

## Prerequisites{#prerequisites-for-creating-vanity-id}

To create the vanity URL, ensure you have already [approved the assets for public delivery](/help/assets/manage-organize-assets-view.md#manage-asset-status).

## Create Vanity URLs{#create-vanity-urls}

Asset delivery URLs includes asset UUIDs. Assets are stored with a unique UUID-based key in the Blob store. Each asset has a metadata JSON doc with asset UUID as key and the asset path as the value. When user hits the delivery URL, the backend resolves the UUID to fetch asset's metadata from key-value store using the UUID and serves the asset. 

Execute the following steps to create vanity URLs:
1. [Configure asset metadata](#configure-asset-metadata)
1. [Create and map Cloud manager environment variable]()
1. [Approve your assets for delivery](/help/assets/manage-organize-assets-view.md#manage-asset-status)
1. [Generate Vanity URLs]()

### Configure asset metadata{#configure-asset-metadata}

Execute the following to set up the vanity ID in your asset's metadata form:
1. Navigate to the details page of the folder holding your assets for Dynamic Media with OpenAPI delivery.
1. [Edit that metadata form](/help/assets/metadata-assets-view.md#edit-metadata-forms) by doing one of the following:
   * Add a new metadata field and specify the required vanity ID as the value of that field.
   * **Update existing field**: Replace an existing metadata property's value with the required vanity ID. Learn the [best practices](#best-practices-for-creating-vanity-IDs) for creating the vanity ID.
   
   [Screenshot placeholder]

   Learn more about [metadata schemas](/help/assets/metadata-schemas.md).
   
   >[!NOTE]
   >
   > A single asset can have multiple vanity IDs.

After configuring your vanity ID in the asset metadata, [map this metadata field to the system's delivery mechanism](#map-cloud-manager-environment-variable).

### Create and map Cloud manager environment variable{#map-cloud-manager-environment-variable}

Execute the following steps to create an environment variable and map it to the metadata field holding the vanity ID:

1. [Navigate to your Cloud Manager environment's configurations page and add a new environment variable with these settings](/help/implementing/cloud-manager/environment-variables.md):
   * **Key**: `ASSET_DELIVERY_VANITY_ID`
   * **Value**: Your metadata field in `dc:<your-metadata-property>` format.
   [Screenshot placeholder]
1. Save your changes to restart the pods in your environment.

### Generate Vanity URLs{generate-vanity-urls}

Make the following replacements to transform your standard delivery URL into vanity URL:

* Replace **UUID** with your **vanity ID**.
* Replace `aaid` with `avid`.

See the [detailed URL format comparison](#standard-urls) above. Learn how to [copy Dynamic Media with OpenAPI delivery URLs](/help/assets/approve-assets.md#copy-delivery-url-for-approved-assets) for your assets.

When your user click the vanity URL, Dynamic Media with OpenAPI automatically redirects to the original asset location. DM with OpenAPI maps your vanity URL to the original asset UUID and handles the redirection at the server level. The content loads instantly, while the user continue to see the vanity URL in their address bar. This redirection process is not visible to the user. The redirection process does not impact existing workflows, and asset delivery continues as usual. You can customize the vanity URL in real time without affecting the asset delivery performance.

### Best Practices for Vanity IDs{#best-practices-for-creating-vanity-IDs}

Follow these best practices for creating vanity IDs:

1. Do not use special characters in vanity IDs, such as spaces, slashes, hyphens and more. The system replaces special characters in vanity IDs using a predefined mapping.
1. Use your brand name, product names, and relevant keywords in vanity ID to boost your brand visibility and user engagement.
1. Use short, descriptive words or strings that convey meaning.
1. Use texts that invite users for clicks.

