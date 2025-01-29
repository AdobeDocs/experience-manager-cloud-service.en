---
title: How to connect a database to [!DNL AEM Forms] as a Cloud Service? 
description: Retrieve and save data to RESTful web services, SOAP-based web services, and OData services from an Adaptive Form or an AEM Workflow.
feature: Adaptive Forms, Form Data Model
role: Admin, User
exl-id: 9d146275-de0a-4861-b060-d205ed6305f3
---
# Connect AEM Forms to a database {#aem-forms-data-integration}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/form-data-model/data-integration.html)                |
| AEM as a Cloud Service     | This article        |



 ![Data Integration](do-not-localize/data-integeration.png)

Enterprise infrastructures include disparate back-end systems or data sources like databases, web services, REST services, OData services, and CRM solutions. Put together, they make an information system that serves data to enterprise applications to perform day-to-day business. On the other hand, applications capture data and send it back to update data sources.

When you connect Adaptive Form to a Database, it requires integration with data sources to fetch customer data while rendering forms. There are use cases when data is fetched from data sources based on user inputs in Adaptive Forms. In addition, when you send an Adaptive Form to a database, the submitted Adaptive Form data can be written back to update the respective data sources.

While a distributed, modular system has its own benefits, the challenge lies in integrating and creating data associations across data sources. Data integration is the key to a functional and efficient enterprise infrastructure with disparate data sources connected to applications for exchange of business data.

## Data Integration overview {#data-integration-overview}

![aem-forms-data-integeration](assets/aem-forms-data-integeration.png)

[!DNL AEM Forms] Data Integration allows configuring and connecting disparate data sources with [!DNL AEM Forms]. It provides an intuitive user interface to create a unified data representation schema of business entities and services across connected data sources. The unified representation is known as a form data model (FDM), an extension of JSON schema. The entities in a Form Data Model (FDM) are referred to as data model objects. A Form Data Model (FDM) lets you:

* Access data model objects, properties, and services from connected data sources.
* Create custom data model objects and properties
* Build associations between data model objects within and across data sources.
* Invoke data model object services to query or write data to and from data sources.

Once you have created a form data model (FDM), you can use it to:

* Create Adaptive Forms based on a form data model (FDM)
* Prefill Adaptive Forms from configured data sources
* Invoke data source services/operations using Adaptive Form rules
* Write submitted Adaptive Form data to data sources

## Get started with data integration {#get-started-with-data-integration}

The first step to implement data integration to send Adaptive Form to a database, is to identify and configure data sources that store information you want to use in Adaptive Forms. Next, you create a Form Data Model (FDM) that uses data model objects, properties, and services from one or more data sources. You can create Adaptive Forms based on a Form Data Model (FDM) where Adaptive Form fields are bound to respective data source properties.

[!DNL AEM Forms] also lets you create a Form Data Model (FDM) independent of data sources and associate or bind data model objects and properties in the Form Data Model (FDM) with data source later. It eliminates any dependencies on data sources while you work on a form data model (FDM).

Review the following to get started, understand, and implement data integration:

* [Configure data sources](configure-data-sources.md)
* [Create form data model (FDM)](create-form-data-models.md)
* [Work with form data model (FDM)](work-with-form-data-model.md)
* [Use form data model (FDM)](using-form-data-model.md)

<!--

>[!NOTE]
>
>[!UICONTROL Experience Manager Forms] does not support relational database.

-->