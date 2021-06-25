---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: a2d56721-502c-4f4e-9b72-5ca790df75c5
---

# Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for the current (latest) version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>From here, you can navigate to release notes of previous versions; for example, for those in 2020, 2021 and so on.

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2021.6.0 is June 24, 2021.
The following release (2021.7.0) will be on July 29, 2021.


## [!DNL Adobe Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### What is new in [!DNL Forms] {#what-is-new-forms}

* Added ability to filter custom columns in AEM Inbox.
* Added ability to use the theme editor and style layer of adaptive form editor to style the captcha component. 
* Improved speed and accuracy for automatically detecting logical sections in the source PDF forms and converting those into corresponding adaptive form panels. 
* Added move action to move a PDF or XDP file from one folder to another.

### Beta feature of [!DNL Forms]  {#what-is-new-forms-prerelease}

* **AEM Forms as a Cloud Service - Communications**: Communication APIs helps you combine XDP templates and XML data to generate print documents in various formats. The service allows you to generate documents in synchronous mode. The APIs enables you to create applications that let you:
  * Generate final form documents by populating template files with XML data.
  * Generate output forms in various formats, including non-interactive PDF print streams.
  * Generate print PDFs from an XFA form PDF and Acrobat Form (AcroForm)

* **Variable Data Externalizer**: You can save data of AEM Workflow variables on an external storage system managed by your organization. 

You can write to [!DNL formscsbeta@adobe.com] to sign up for the beta program.

### Bugs fixed in [!DNL Forms] {#forms-bugs-fixed}

* When a field is validated before submitting data to backend service via Form Data Model (FDM), validations succeed but the Form Data Model service fail to invoke post validation.
* When you submit a form containing a standard HTML upload field from an Apple iOS device, sometimes, the content of the file is not sent and a 0-byte file is received at the other end. This is a known issue in Apple iOS. [FB9117687](https://feedbackassistant.apple.com/feedback/9117687)


