---
title: How to connect a database to [!DNL AEM Forms] as a Cloud Service? 
seo-title: AEM Forms Data Integration
description: You can retrieve and save data to a RESTful web services, SOAP-based web services, and OData services from [!DNL AEM Forms] as a Cloud Service. The service provides a dedicated tool to retrieve, test, validate, and send data to various types of data sources.
exl-id: 9d146275-de0a-4861-b060-d205ed6305f3
---
# Connect your data sources to Cloud Service {#aem-forms-data-integration}

 ![Data Integration](do-not-localize/data-integeration.png)

Enterprise infrastructures include disparate back-end systems or data sources like databases, web services, REST services, OData services, and CRM solutions. Put together, they make an information system that serves data to enterprise applications to perform day-to-day business. On the other hand, applications capture data and send it back to update data sources.

[!DNL AEM Forms] applications like Adaptive Forms and interactive communications require integration with data sources to fetch customer data while rendering forms and creating interactive communications. There are use cases when data is fetched from data sources based on user inputs in Adaptive Forms. In addition, the submitted Adaptive Form data can be written back to update the respective data sources.

While a distributed, modular system has its own benefits, the challenge lies in integrating and creating data associations across data sources. Data integration is the key to a functional and efficient enterprise infrastructure with disparate data sources connected to applications for exchange of business data.

## Data Integration overview {#data-integration-overview}

![aem-forms-data-integeration](assets/aem-forms-data-integeration.png)

[!DNL AEM Forms] Data Integration allows configuring and connecting disparate data sources with [!DNL AEM Forms]. It provides an intuitive user interface to create a unified data representation schema of business entities and services across connected data sources. The unified representation is known as a form data model, an extension of JSON schema. The entities in a Form Data Model are referred to as data model objects. A Form Data Model allows you to:

* Access data model objects, properties, and services from connected data sources.
* Create custom data model objects and properties
* Build associations between data model objects within and across data sources.
* Invoke data model object services to query or write data to and from data sources.

Once you have created a form data model, you can use it in various Adaptive Form and interactive communications workflows, such as:

* Create Adaptive Forms and interactive communications based on form data model
* Prefill Adaptive Forms and interactive communications from configured data sources
* Invoke data source services/operations using Adaptive Form rules
* Write submitted Adaptive Form data to data sources

## Get started with data integration {#get-started-with-data-integration}

The first step to implement data integration is to identify and configure data sources that store information you want to leverage in Adaptive Forms and interactive communications use cases. Next, you create a Form Data Model that uses data model object, properties, and services from one or more data sources. You can create Adaptive Forms and interactive communications based on a Form Data Model where Adaptive Form fields or placeholders in interactive communications are bound to respective data source properties.

[!DNL AEM Forms] also allows you to create a Form Data Model independent of data sources and associate or bind data model objects and properties in the Form Data Model with data source later. It eliminates any dependencies on data sources while you work on a form data model.

Review the following to get started, understand, and implement data integration.

* [Configure data sources](configure-data-sources.md)
* [Create form data model](create-form-data-models.md)
* [Work with form data model](work-with-form-data-model.md)
* [Use form data model](using-form-data-model.md)

>[!NOTE]
>
>[!UICONTROL Experience Manager Forms] does not support relational database.
