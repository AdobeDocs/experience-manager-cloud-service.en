---
title: Getting started with HTML5 forms
description: To get started, deploy AEM Forms add-on package and import existing HTML5 forms to AEM.
content-type: reference
topic-tags: hTML5_forms
discoiquuid: f276d150-8936-4bfb-8475-7ca36815b233
feature: HTML5 Forms,Mobile Forms
exl-id: a3245f05-6ea3-4f90-8981-bfa89d2e7335
solution: Experience Manager, Experience Manager Forms
role: Admin, User, Developer
---
# Getting started with HTML5 forms {#getting-started-with-html-forms}

<span class="preview"> The HTML5 Forms capability is offered as part of Early Access Program. To request access, send an email from your official (work) email ID to aem-forms-ea@adobe.com.
</span>

HTML5 forms bring numerous capabilities that are mobile-ready. It helps you expand your current solutions and workflows to tablets or smartphones devices with HTML5 browsers. Some of the capabilities include:

* **HTML5-based rendering of XFA form templates:** In addition to regular PDF forms, you can now render your existing XFA-based forms in HTML5 format. It helps you to expand your client platform to mobile devices (Apple iPad, Android tablet, smartphones, and so on) that supports HTML5 and do not support Adobe Reader with XFA Forms. For more information about HTML5-based rendering capability, see [Introduction to HTML5 forms](/help/forms/introductionhtml5.md).

* **Managing Forms:** In addition, AEM includes new capabilities to simplify the process of organizing and managing forms. You can activate, deactivate, publish, and preview forms.<!--For more information, see [Introduction to managing forms](/help/forms/using/introduction-managing-forms.md).-->

## Configuring your environment for HTML5 forms {#installing-html-forms}

To enable form submissions and proper rendering of HTML5 Forms, perform the following steps:

* **Add dispatcher filters:** Update your `src/conf.dispatcher.d/filters/filters.any` file to allow necessary requests for HTML5 Forms. Add the following filter rules:

  ```
  /0103 { /type "allow" /method '(HEAD|POST)' /url "/content/xfaforms/profiles/default.submit.html" }  # allow POSTs to form selectors under content
  /0104 { /type "allow" /method '(GET|HEAD|POST)' /url "/*.xdp.html" }
  ```

* **Add a package for submission:** In your project, add a package in the `src/main/content/jcr_root/content` folder to support form submission functionality.

* **Import HTML5 Forms:** Import your forms from your local file system to AEM Forms.
