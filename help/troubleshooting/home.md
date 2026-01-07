---
title: Troubleshooting in AEM Assets and Forms
description: Troubleshoot common AEM Assets and Forms issues using the article links for key areas, such as uploads, metadata, search, delivery, form creation, submission, and integration.
hidefromtoc: yes
hide: yes
exl-id: 73ff9249-6f5a-46c1-87fe-7cb50b000927
---
# Troubleshoot AEM Assets and Forms issues {#troubleshoot-aem-assets-forms}

AEM as a Cloud Service offers comprehensive solutions for Digital Asset Management through AEM Assets and powerful form creation capabilities through AEM Forms. Both services provide cloud-native, PaaS solutions with next-generation smart capabilities, such as AI/ML, all within a system that is always current, always available, and always learning.

However, complex enterprise environments can encounter various technical challenges across different areas.

This comprehensive troubleshooting guide provides systematic diagnostic approaches, categorized solutions, and step-by-step resolution paths for both AEM Assets and Forms. Each section includes quick reference guides, detailed troubleshooting methodologies, and extensive resource links to help you efficiently resolve issues and optimize your AEM Cloud Service environment.

## AEM Assets Troubleshooting {#aem-assets-troubleshooting}

AEM Assets streamlines how you manage, organize, and deliver digital assets across experiences. However, issues may arise that affect asset uploads, metadata, integrations, or delivery. This article provides troubleshooting steps to help you diagnose and resolve common AEM Assets issues. By following the guidance here, you can restore workflows efficiently and ensure assets remain accessible, accurate, and ready for use across channels.

### Asset Processing and Renditions {#asset-processing-renditions-issues}

<table>
  <tbody>
  <tr>
    <td><strong>Upload & Processing</strong></td>
    <td><strong>Renditions</strong></td>
    <td><strong>PDF & Text Extraction</strong></td>
  </tr>
  <tr>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26610">Asset processing failed for large MP4 files in AEM as a Cloud Service</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26639">DAM renditions not matching original files</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26785">AEM truncates extracted text from large PDFs after 100K tokens</a></td>
  </tr>
  <tr>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-23916">Tiff file with ZIP compression uploads generate no renditions</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26233">Images not showing thumbnail renditions in AEM as a Cloud Service</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25518">Text extraction limitations for large PDFs in AEM as a Cloud Service</a></td>
  </tr>
  <tr>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-21865">Drag-and-drop of a folder of assets to AEM Assets Web UI fails</a></td>
    <td></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26528">Asset rotation issue makes subsequent rotations invisible</a></td>
  </tr>
  <tr>
  <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26450">Increasing single part asset upload limit for Photoshop Firefly API Integration</a></td>
  <td></td>
  <td></td>
  </tr>
  </tbody>
</table>

### Dynamic Media {#dynamic-media-issues}

<table>
  <tbody>
  <tr>
    <td><strong>Video</strong></td>
    <td><strong>Spin Sets & Smart Crop</strong></td>
    <td><strong>Delivery & Settings</strong></td>
  </tr>
  <tr>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26533">Fix video upload, processing, and rendering issues in AEM</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26715">Spin Sets stuck in processing state</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-17628">Changing Dynamic Media URL for assets</a></td>
  </tr>
  <tr>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26677">Video thumbnail mismatch between Dynamic Media and DAM Card View</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26873">Smart Crop renditions not generated in AEM as a Cloud Service</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26367">Broken image issue with Smart Crop in AEM 6.5</a></td>
  </tr>
  <tr>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26610">Asset processing failure in AEM Dynamic Media</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26637">Background color issue for TIFF renditions</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25294">Dynamic Media General Settings page doesn't open</a></td>
  </tr>
  <tr>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26197">Resolve audio issues in video files with Dynamic Media</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25885">Asset synchronization failure in Dynamic Media</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26461">Resolve asset name discrepancies across environments</a></td>
  </tr>
  <tr>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26871">Dynamic Media video player not functioning in lower environments</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25471">Dynamic Media synchronization user recommendations</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26902">Export assets and metadata from Dynamic Media using API</a></td>
  </tr>
  </tbody>
</table>

### Metadata, Tagging, and Sharing {#metadata-tagging-sharing-issues} 

<table>
  <tbody>
  <tr>
    <td><strong>Metadata</strong></td>
    <td><strong>Smart Tags</strong></td>
    <td><strong>Access & Sharing</strong></td>
  </tr>
  <tr>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25828">Image metadata discrepancy in AEM Assets</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25925">Automatic tagging of newly uploaded assets</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26928">Commenting restricted in Assets View despite read access</a></td>
  </tr>
  <tr>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26655">Resolving metadata schema visibility issues for non-admin users</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25889">Smart Tags not working after JWT to OAuth migration</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25903">Resolve shared link issues in AEM Managed Services</a></td>
  </tr>
  
  </tbody>
</table>

### Integrations and Access {#integrations-access}

<table>
  <tbody>
    <tr>
      <td><strong>Asset Link</strong></td>
      <td><strong>Licensing and Customizations</strong></td>
    </tr>
    <tr>
      <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26922">Adobe Asset Link leaves links inaccessible in InDesign</a></td>
      <td>
        <a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26616">Content fragments not included in AEM Assets license</a><br>
        </td>
    </tr>
    <tr>
      <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25562">Resolving AEM Asset Link connection issues in InDesign</a></td>
      <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25525">Resolving asset processing issues in AEM as a Cloud Service</a></td>
    </tr>
    <tr>
      <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25506">Adobe Asset Link Plug-In Network Error: Server unreachable</a></td>
      <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25829">Updating custom thumbnails for video assets in AEM as a Cloud Service</a>
      </td>
    </tr>
  </tbody>
</table>




## AEM Forms Troubleshooting {#aem-forms-troubleshooting}

AEM Forms as a Cloud Service provides powerful form creation and management capabilities. However, you may encounter issues during installation, configuration, form creation, or submission processes. This section provides comprehensive troubleshooting guidance for common AEM Forms issues.

### Installation and Configuration Issues

<table>
  <tbody>
  <tr>
    <td><strong>Setup & Configuration</strong></td>
    <td><strong>Form Creation Issues</strong></td>
    <td><strong>Performance & Caching</strong></td>
  </tr>
  <tr>
    <td><a href="/help/forms/troubleshooting-installation-and-configuration.md">Forms option unavailable in Navigation</a></td>
    <td><a href="/help/forms/form-creation-failing.md">Form creation fails after template publishing</a></td>
    <td><a href="/help/forms/troubleshooting-caching-performance.md">Adaptive Forms caching issues</a></td>
  </tr>
  <tr>
    <td><a href="/help/forms/troubleshooting-installation-and-configuration.md#build-pipeline-fails">Build pipeline failures</a></td>
    <td><a href="/help/forms/form-creation-failing.md#cause-form-creation-fails">Template publishing sequence issues</a></td>
    <td><a href="/help/forms/troubleshooting-caching-performance.md#images-videos-not-invalidated">Dispatcher cache invalidation problems</a></td>
  </tr>
  <tr>
    <td><a href="/help/forms/troubleshooting-installation-and-configuration.md#bundles-inactive-state">Bundle activation issues</a></td>
    <td><a href="/help/forms/known-issues.md">Known form creation limitations</a></td>
    <td><a href="/help/forms/troubleshooting-caching-performance.md#cdn-caching-stops-working-after-300-seconds">CDN caching failures</a></td>
  </tr>
  </tbody>
</table>

### Form Submission and Integration Issues

<table>
  <tbody>
  <tr>
    <td><strong>Edge Delivery Services</strong></td>
    <td><strong>Custom Submit Actions</strong></td>
    <td><strong>Integration Problems</strong></td>
  </tr>
  <tr>
    <td><a href="/help/forms/troubleshooting-403-forbidden-edge-delivery-form-submission.md">403 Forbidden errors in form submission</a></td>
    <td><a href="/help/forms/custom-submit-action-troubleshooting.md">502 errors in custom submit actions</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-27434">DRM-SAML redirect failures</a></td>
  </tr>
  <tr>
    <td><a href="/help/forms/troubleshooting-403-forbidden-edge-delivery-form-submission.md#cors-issues">CORS configuration issues</a></td>
    <td><a href="/help/forms/custom-submit-action-troubleshooting.md#resolution">Unhandled exception handling</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-27075">Submit button disabled on AEM Sites</a></td>
  </tr>
  <tr>
    <td><a href="/help/forms/troubleshooting-403-forbidden-edge-delivery-form-submission.md#referrer-filter-issues">Referrer Filter configuration</a></td>
    <td><a href="/help/forms/custom-submit-action-for-adaptive-forms-based-on-core-components.md">Best practices for custom actions</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26532">Hidden fields visibility after upgrades</a></td>
  </tr>
  </tbody>
</table>

### Designer and Development Issues

<table>
  <tbody>
  <tr>
    <td><strong>AEM Forms Designer</strong></td>
    <td><strong>Development Environment</strong></td>
    <td><strong>Version and Compatibility</strong></td>
  </tr>
  <tr>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26558">Designer 6.5 not opening after upgrade</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-27089">Locators fail to start with JDK 8/11</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26862">AEM Forms (AEMFD) package version display issues</a></td>
  </tr>
  <tr>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-21018">PDF Generator JPEG 2000 errors</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-22689">JBoss log path configuration</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26846">Incorrect version numbers in Windows</a></td>
  </tr>
  <tr>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-27406">Button missing in PDF output</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-18084">Configuration Manager upgrade errors</a></td>
    <td><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-17339">Index corruption workarounds</a></td>
  </tr>
  </tbody>
</table>
