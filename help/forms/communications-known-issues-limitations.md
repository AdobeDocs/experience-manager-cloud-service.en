---
title: Known issues 
seo-title: Communications best practices, known issues, and limitations
description: 
---

# Frequently asked questions, best practices, known issues, and limitations {#best-practices-known-issues-and-limitations}

Before you begin using Communication APIs, frequently asked questions, review the following known issues and limitations:

## Known issues

- You can use a specific render type (PDF, PRINT) only once in the print options list. For example, you cannot have two PRINT options each specifying a PCL render type.

- For a batch configuration, only one instance of combination of values of OutputType(PDF, PRINT) and RenderType(PostScript, PCL, IPL, ZPL, etc.) is allowed.

## Best Practices

- Adobe recommends to host data files blob container store in the cloud region used by AEM Cloud Service.

## Frequently asked questions {#faq}

**Can I use a watched folder or other storage mechanisms to store input and output?**

At the moment, you can use Microsoft Azure Storage to save input data and generated documents. Microsoft Azure storage provides various options to [automate data movement operations](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10).

**Is a Microsoft Azure Storage account included with Experience Manager Forms Cloud Service license?**

Microsoft Azure Storage account is independent of Experience Manager Forms Cloud Service license.

**Does Communication APIs store data on Experience Manager Forms Cloud Service servers?**

Input and output data is saved only on Microsoft Azure Storage.

**Are Communication APIs available only for Experience Manager Forms Cloud Service? Can I get similar functionality on on-premise environment?**

You can use AEM Forms Output service to combine a template (XFA or PDF) with customer data to generate documents in PDF, PS, PCL, and ZPL formats.

In comparison to on-premise environment,  the Cloud Service provides additional benefits of auto-scaling and cost effectiveness.

<!--**Where is data processed?**

**Who has access to data?**

**Is data encrypted?**

**Where is data hosted?** -->

**Can I run multiple batch operations simultaneously?**
Yes, you can run multiple batch operations simuntabously. Always use different source and destination folders for every operation to avoid any conflicts.
