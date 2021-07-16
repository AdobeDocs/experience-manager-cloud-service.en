---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
mini-toc-levels: 1
exl-id: a2d56721-502c-4f4e-9b72-5ca790df75c5
mini-toc-levels: 1
---

# Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for the current (latest) version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions; for example, for those in 2020, 2021 and so on.

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2021.7.0 is July 29, 2021.
The following release (2021.7.0) will be on August26 , 2021.

## Release Video {#release-video}

Have a look at the [June 2021 Release Overview](https://video.tv.adobe.com/v/334296) video for a summary of the features added.

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}
 
### New features in [!DNL Sites] {#ga-features-sites}
 
* 
* 
 
### New features available in the [!DNL Sites] prerelease channel {#beta-features-sites}
 
* 
* 
 
#### Bugs fixed in [!DNL Sites] {#bugs-fixed-sites}
 
* 
* 

## [!DNL Adobe Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### What is new in [!DNL Forms] {#what-is-new-forms}

* You can now use Automated Forms Conversion service to convert PDF Forms in French, German, and Spanish language to adaptive forms. 
* Added a separate panel to template editor to display errors related to adaptive form components. It helps consolidate all adaptive form errors at one location and reduce resolution time.

### New features available in [!DNL Forms] prerelease channel {#beta-features-assets}

* **[!DNL AEM Forms as a Cloud Service - Communications]**: Communication APIs helps you combine XDP templates and XML data to generate print documents in various formats. The service allows you to generate documents in synchronous mode. The APIs enables you to create applications that let you:
  * Generate documents by populating template files with XML data.
  * Generate output forms in various formats, including non-interactive PDF print streams.
  * Generate print PDFs from an XFA form PDF and Adobe Acrobat Form.

* **Variable Data Externalizer**: You can save data of AEM Workflow variables on an external storage system managed by your organization.

* **Acroform-based Document of Record**: You can also use Adobe Acrobat Form PDF (Acroform PDF) as a template for Document of Record besides XFA-based form template.

* **Form Data Model**: You can now connect Form Data Model to Microsoft Azure Storage. It allows you to store and retrieve adaptive form data to Microsoft Azure Storage as a BLOB.  


### Bugs fixed in [!DNL Forms] {#forms-bugs-fixed}

* When a field is validated before submitting data to backend service via Form Data Model (FDM), validations succeed but the Form Data Model service fail to invoke post validation.
* When you submit a form containing a standard HTML upload field from an Apple iOS device, sometimes, the content of the file is not sent and a 0-byte file is received at the other end. This is a known issue in Apple iOS. [FB9117687](https://feedbackassistant.apple.com/feedback/9117687)
