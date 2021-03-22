---
title: AEM - Commerce Integration using Commerce Integration Framework FAQ
description: AEM - Commerce Integration using Commerce Integration Framework FAQ
---

# AEM - Commerce Integration using Commerce Integration Framework FAQ


## 1. Is CIF GraphQL only used for commerce or will this be available for querying content authored on AEMs JCR?

Adobe has adopted Magento’s GraphQL APIs as its official commerce API for all commerce related data. Hence, AEM uses GraphQL to exchange commerce data with Magento and with any commerce engine via I/O Runtime. This GraphQL API is independent from AEM's GraphQL API to access Content Fragments.

## 2. How does Adobe I/O come into play? Does AEM talk to Magento directly?

AEM can directly connect to Magento without an I/O Runtime layer. If there is a need to integrate a non-Magento commerce backend (third party solution) with AEM, the I/O Runtime platform can be used to host the mapping layer to connect the Magento GraphQL APIs to any third party solutions APIs. For more details on this, please refer to this [reference implementation](https://github.com/adobe/commerce-cif-graphql-integration-reference). For non-Magento solutions, AEM would be configured to point to the I/O Runtime endpoint.

The I/O Runtime platform can also be used to extend or customize commerce services. For this use-cases you would call the I/O Runtime endpoint that will then host a customized implementation of the respective service. Integration and extension use-cases can be combined.

## 3. Can Product assets (images) be stored and referenced from AEM via Magento admin? How can assets from Dynamic Media be consumed?

There isn't currently an AEM Assets – Magento integration. As a workaround, you can store product assets (images) in AEM Assets but you will have to manually store the asset URLs in Magento. Dynamic Media is now part of AEM Assets and will work the same way.

## 4. Does it matter where the commerce solution is deployed? (On-prem or in the cloud)

It does not matter where your commerce solution is deployed. The integration and the new AEM Venia store front will work regardless of the deployment model. However, if it is deployed based on the approved E2E reference architecture, E2E tests will be run against performance KPIs that were gathered that represent an enterprise customer’s profile. So, this will provide you with additional information that you can use as a benchmark.

## 5. How are catalog pages or product pages created in AEM? How do they persist in AEM?

Catalog pages and product pages are created and cached dynamically in AEM based on generic catalog and product page templates. No Product or Catalog data is imported and stored in AEM.

## 6. When you update product data in your commerce solution, is that a real-time push to AEM? Or is it a batch process?

The CIF add-on used with AEM Cloud Service enables data to flow from the commerce solution to AEM on-demand. Hence, this is not a real-time push or a batch process when there is an update in your commerce solution.

## 7. What catalog size does AEM with CIF support?

As product data and catalog pages get created and cached dynamically, there is no fix size limit. Catalog size is, however, only one aspect you have to consider. Cache ratio, concurrent data requests and page creation may all have an impact on the scalability and performance.

## 8. How does PIM play into this framework?

PIM data gets exposed to AEM and clients via GraphQL requests. Our recommendation is to integrate PIM with the commerce engine (Magento or others) so that PIM data can then be retrieved from the commerce engine.

## 9. Do you also cache pricing and other data via Dispatcher. Does that raise a frequent cache invalidation challenge?

Dynamic data such as price or inventory is not cached on the Dispatcher. Dynamic data is fetched client-side with web components directly via GraphQL APIs. Only static data (such as product or category data) is cached on the Dispatcher. If product data changes, there will be a need for cache invalidation.

## 10. How does cache invalidation for AEM Dispatcher work with AEM and commerce?

We recommend setting up TTL-based cache invalidation for pages cached on the Dispatcher. For dynamic information such as price or stock, we recommend rendering the date client-side. For more information about TTL-based cache invalidation, please refer to [AEM Dispatcher](https://helpx.adobe.com/experience-manager/kb/optimizing-the-dispatcher-cache.html)

## 11. Is there any recommendation on unified search across AEM content with Commerce?

A product search reference implementation is provided but no unified search with content. This feature is usually very customer specific and better solved on a project-specific level.

## 12. How does Search work with AEM and commerce using CIF?

CIF provides Search bar and Search Result components. The Search bar component sends a GraphQL request with the search term to the commerce solution which then returns a product list that includes product name, price, SLUG, etc. The Search Result component then displays the search results in a gallery view on a search result page created in AEM. The Search supports basic full-text search. We use the SLUG/url key to build a reference to the PDP.

## 13. How can product data be used in MSM or translations?

Product data is usually already translated in PIM or in Magento. The AEM – Magento Integration supports the connection to multiple Magento stores & store views. In an MSM setup typically one AEM site is linked to one Magento store view.

## 14. How does CIF work with non-Magento commerce platforms?

Integration with third party solutions such as other commerce solutions (non-Magento) is done via the I/O Runtime platform.  We have built a [reference implementation](https://github.com/adobe/commerce-cif-graphql-integration-reference) to demonstrate how this is done. This enables the reuse of the [AEM CIF Cloud Connector](https://github.com/adobe/commerce-cif-connector) and the [AEM CIF Core Components](https://github.com/adobe/aem-core-cif-components) by exposing the Magento GraphQL API on top of any thirdd-party commerce platform. To offer maximum flexibility and scalability, this integration layer is deployed on the serverless [Adobe I/O Runtime platform](https://www.adobe.io/apis/experienceplatform/runtime.html).

## 15. Is there a way to enhance the product data with commercial text? Where do you do this? In AEM or in the commerce solution?

We recommend to manage marketing related data and content in AEM. Decorate product data from your commerce solution with additional attributes using Content Fragments or create and link Experience Fragments for un-strutured content with your products.

## 16. Does the integration between AEM-Magento change when Adobe I/O Runtime platform is used?

Customers who want to extend commerce services can use the same integration and write action sequences hosted on the I/O Runtime platform to inject business logic and enrich the commerce services.

## 17. Will SPA store front work with AEM SPA editor?

AEM can be used as an authoring tool for any kind of store front. Currently, server- and client-side rendering (hybrid) is used in AEM's storefront. We will release PWA support for headless and headful content authoring later in 2021.


## 18. How can we ensure PCI compliance when using AEM for the entire presentation layer?

We recommend to use abstracted payment methods. This puts the browser client in direct communication with the payment gateway provider so that neither Adobe or the commerce solutions hold or pass cardholder data. This approach requires only a level 3 PCI compliance. However, there are additional things to consider to be fully PCI compliant such as how employees interact with the system and data. For more information about Magento PCI compliance, please refer to https://magento.com/pci-compliance

## 19. If I use AEM and Magento cloud versions, is this joint solution PCI compliant?

Yes, Self-Assessment Questionnaire D and Attestation of Compliance are available on-request.


## 20. How can I request for an I/O Runtime trial license?

You can request for a trial license to use I/O Runtime [here](https://adobeio.typeform.com/to/obqgRm).
