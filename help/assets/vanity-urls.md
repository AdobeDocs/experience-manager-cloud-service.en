---
title: Create Vanity URLs using Dynamic Media with OpenAPI Capabilities
description: Transform your long asset delivery URLs into short, branded vanity URLs using Dynamic Media OpenAPI capabilities. A vanity URL is a short, clean, easy-to-remember and readable version of your complex delivery URL. You can include your brand name, product names, and relevant keywords in the vanity URL to boost your brand visibility and user engagement
role: Admin
feature: Asset Management, Publishing, Collaboration, Asset Processing
---

# What are Vanity URLs?{#vanity-urls}

Transform your long asset delivery URLs into short, branded vanity URLs using [!DNL Dynamic Media OpenAPI capabilities]. Your asset delivery URLs include system-generated asset UUIDs that make the delivery URL complex, hard to remember and share. Replace these asset UUIDs with Vanity identifiers (Vanity IDs). Use short and simple vanity IDs, to make your delivery URL short, clean, readable, easy-to-remember and share. Use your brand name, product names, and relevant keywords as vanity IDs to boost your brand visibility and user engagement. 

A vanity URL is a short, clean, and readable version of your complex delivery URL. When your user click your vanity URL, Dynamic Media with OpenAPI automatically redirects to the original asset location. DM with OpenAPI maps your vanity IDs to the original asset UUIDs in real time and handles the redirection at the server level. The content loads instantly, while the user continue to see the vanity URL in their address bar. This redirection process is not visible to the user. The redirection process does not impact existing workflows, and asset delivery continues as usual. You can customize the vanity URL in real time without affecting the asset delivery performance.

The following example compares a generic asset delivery URL with its vanity URL:

**Generic URL (including long system-generated UUID)**

`https://delivery-p30902-e145436-cmstg.adobeaemcloud.com/adobe/assets/urn:aaid:aem:43341ab1-4086-44d2-b7ce-ee546c35613b/as/chekc.jpeg`

**Vanity URL (short and branded)**

`https://delivery-p30902-e145436-cmstg.adobeaemcloud.com/adobe/assets/urn:avid:aem:VanityCheck/as/chekc.jpeg`

Learn to [create Vanity URLs](#create-vanity-urls).

## Explore key capabilities and benefits{#capabilities-and-benefits-of-vanity-urls}

Vanity URLs enable customization of generic asset delivery URLs, providing several advantages and measurable impact. Some of the key capabilities and benefits include the following.

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

Fulfill the following requirements for creating the vanity ID:

1. [Approve assets for delivery](/help/assets/manage-organize-assets-view.md#manage-asset-status).

## Create Vanity URLs{#create-vanity-urls}


<!-- 

[!DNL Vanity URLs] let you customize long, complex, hard-to-remember web addresses into shorter, SEO-friendly, easy-to-remember and share URLs. System-generated asset UUIDs makes your asset delivery URL complex. Vanity URLs replaces these UUIDs with short, readable identifiers. Use your brand name, product names, and relevant keywords in the vanity URL to boost brand visibility and user engagement. 

Assets are stored with a unique UUID-based key in the Blob store. Each asset has a metadata JSON doc with asset UUID as key and the asset path as the value. A generic asset delivery URL includes asset UUIDs. When a user hits the delivery URL containing a UUID, the backend resolves the UUID to fetch asset's metadata from key-value store using the UUID  and serves the asset. 

Asset UUID in the asset delivery URL makes the URL long and complex. Replace these asset UUIDs with vanity IDs to make the URL short and readable. An asset can have multiple vanity iDs. Define the vanity IDs of each asset in your custom metadata field. map vanity IDs to asset UUIDs for asset delivery. This Mapping performas this mapping at ingestion time and resolve them properly at delivery time.

---
A generic asset delivery URL includes asset UUIDs. When a user hits the delivery URL containing a UUID, the backend resolves the UUID to fetch asset's metadata from key-value store using the UUID  and serves the asset. Assets are stored with a unique UUID-based key in the Blob store. Each asset has a metadata JSON doc with asset UUID as key and the asset path as the value.

Asset UUID in the asset delivery URL makes the URL long and complex. using [!DNL Dynamic Media OpenAPI capabilities] replace these asset UUIDs with vanity IDs to make the URL short and readable. Vanity IDs are identifiers that makes your delivery URL clean, simple and easy to share. An asset can have multiple vanity IDs. 

Add or edit a metadata property and speify the vanity ID for an asset  as its value, then map the metadta property to the `ASSET_DELIVERY_VANITY_ID` variable in the cloud manager environment. This mapping maps the vanity IDs to asset UUIDs for asset delivery. When your user click your vanity URL, Dynamic Media with OpenAPI automatically redirects to the original asset location. This Mapping helps to map assets at ingestion time and resolve them properly at delivery time. 

Define the vanity IDs of each asset in your custom metadata field, then map vanity IDs to asset UUIDs for asset delivery. This Mapping helps to map assets at ingestion time and resolve them properly at delivery time. When your user click your vanity URL, Dynamic Media with OpenAPI automatically redirects to the original asset location. DM with OpenAPI maps your vanity URL to the original asset UUID and handles the redirection at the server level. The content loads instantly, while the user continue to see the vanity URL in their address bar. This redirection process is not visible to the user. The redirection process does not impact existing workflows, and asset delivery continues as usual. You can customize the vanity URL in real time without affecting the asset delivery performance.

Use vanity ids to replace the asset UUIDs in your asset delivery URLs to customize your long, complex, hard-to-remember delivery urls into shorter, SEO-friendly, easy-to-remember and share URLs. A vanity URL is a short, clean, and readable version of your complex delivery URL. Use your brand name, product names, and relevant keywords in the vanity URL to boost brand visibility and user engagement.

----
-->

Asset delivery URLs includes asset UUIDs. Assets are stored with a unique UUID-based key in the Blob store. Each asset has a metadata JSON doc with asset UUID as key and the asset path as the value. When user hits the delivery URL, the backend resolves the UUID to fetch asset's metadata from key-value store using the UUID and serves the asset. 

To create vanity URLs, map the `ASSET_DELIVERY_VANITY_ID` variable available in your cloud manager environment with the metadata property in your asset's metadata form that includes the vanity ID. Then replace the UUID in your deliver URL with this vanity ID to create the Vanity URL. This mapping maps the vanity IDs to asset UUIDs for asset delivery. This Mapping helps to map assets at ingestion time and resolve them properly at delivery time. When your user click your vanity URL(delivery url with vanity id), Dynamic Media with OpenAPI automatically redirects to the original asset location.

To create vanity ID for an asset, Add or edit a metadata property and specify the vanity ID for an asset  as its value, then map the metadta property to the `ASSET_DELIVERY_VANITY_ID` variable in the cloud manager environment. This mapping maps the vanity IDs to asset UUIDs for asset delivery. This Mapping helps to map assets at ingestion time and resolve them properly at delivery time. When your user click your vanity URL(delivery url with vanity id), Dynamic Media with OpenAPI automatically redirects to the original asset location. 

An asset can have multiple vanity IDs. Define the vanity IDs of each asset in your custom metadata field. map vanity IDs to asset UUIDs for asset delivery. This Mapping performas this mapping at ingestion time and resolve them properly at delivery time.





Execute the following steps to create vanity URLs:

1. Navigate to the details page of your folder storing the assets that needs to be delivered using DM with OpenAPI capabilities and see the metadata form applied to the folder.
1. [Edit the metadata form](/help/assets/metadata-assets-view.md#edit-metadata-forms) to add a new metadata field and specify the vanity ID in its value field.
Alternativey you can also replace the existing value of a metadata property with the required vanity ID. See [metadata scema](/help/assets/metadata-schemas.md) article for more information on metadata forms. Learn the [best practices](/) for creating the vanity ID.
An asset can have multiple vanity IDs.
1. Navigate to the configurations page in your cloud manager environment to add a new `ASSET_DELIVERY_VANITY_ID` variable. Learn to add [environment variables in Cloud Manager](/help/implementing/cloud-manager/environment-variables.md). `ASSET_DELIVERY_VANITY_ID` is the key. In its value field, specify the metadata field containing the vanity ID in `dc:[your maeatadat propery]` format to map `ASSET_DELIVERY_VANITY_ID` with the metadata property.
1. Save the changes to automatically restart the pods in your program environment. 
1. Replace the UUID in DM with OpenAPI delivery URL of your asset with `avid:[your vanity id]` to generate the vanity url for your asset delivery. Learn to copy the [dmwith open api delivery url]() of your assets.

When your user click the vanity URL, Dynamic Media with OpenAPI automatically redirects to the original asset location. DM with OpenAPI maps your vanity URL to the original asset UUID and handles the redirection at the server level. The content loads instantly, while the user continue to see the vanity URL in their address bar. This redirection process is not visible to the user. The redirection process does not impact existing workflows, and asset delivery continues as usual. You can customize the vanity URL in real time without affecting the asset delivery performance.

### Best Practices for Vanity IDs{#best-practices-for-creating-vanity-IDs}

abhd

