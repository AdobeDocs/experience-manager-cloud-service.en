---
title: How to publish or unpublish forms on preview or publish instances?
description: Learn publishing or unpublishing forms from the AEM author environment to preview or publish instances. Whether you are testing your forms on a staging environment or deploying them live for end-users, AEM provides streamlined tools to manage this process efficiently.
Keywords: 6.5 forms to cloud service, 6.5 forms to cs, manage publication, , AEM Forms 6.5 to Cloud Service, AEM form migration to cloud service, Forms Manage publication, AF Manage publication, Adaptive Forms Manage publication, Cloud Manage publication
contentOwner: khsingh
feature: Adaptive Forms
feature-set: Experience Manager Assets,Experience Manager Sites,Experience Manager, Experience Manager Forms, Experience Manager Cloud Manager
role: User, Developer
level: Intermediate
---

# ​Manage publication in Experience Manager Forms

As an Adobe Experience Manager Forms administrator, you can publish forms from your author instance to Experience Manager Forms. You can schedule to publish a form or folder at a later date or time. Once published, the users can access and fill the forms. 

You can publish or unpublish form using either Publish or Manage Publication option available in the Experience Manager Forms interface. If you make subsequent modifications to the original forms or folder in Experience Manager Forms, the changes are not reflected in the publish instance until you republish from Experience Manager Forms. It ensures that work-in-progress changes are not available in the publish instance. Only changes that are published by an administrator are available in the publish instance.

## Publish forms using Publish option 
 
The publish option lets you immediately publish a form. From the Experience Manager Forms console, navigate to the parent folder and select a form that you want to publish. Click Publish option from the toolbar, take a look at all the reference assets that would be published with form and click Publish. 

A screenshot of a computer

Description automatically generated

## Publish or Unpublish forms using Manage Publication 


Manage publication lets you publish or unpublish content to and from the selected destination, add content to the publishing list from across the forms & documents folder, select references to publish, and schedule publishing to a later date or time. 


From the Experience Manager Forms console, navigate to the parent folder and select a form that you want to publish. Click Manage Publication option from the toolbar.  


A screenshot of a computer

Description automatically generated 

 

The following options are available in the Manage Publication interface: 

* Actions 

    * Publish: Publish forms to the selected destination 
    * Unpublish: Unpublish forms from the destination 

* Destination 

    * Publish: Publish forms to Experience Manager Forms (AEM) Publish instance.  
    * Preview: Publish forms to Experience Manager Forms (AEM) preview instance. 

* Scheduling 

    * Now: Publish forms immediately 
    * Later: Publish forms based on the Activation date or time 

 

To continue, click **Next**. In the Scope tab use the Add Content options to add more content for publishing. For example, you can add more Forms or Document of Record files. 

### Add Content 

Publishing to Experience Manager Forms lets you further add more content (forms, assets and folders) to the publishing list. You can add more forms, assets or folders to the list from the formsanddocuments folder. But you cannot add assets from multiple folders at a time.

A screenshot of a computer

Description automatically generated  

Click **Add Content** button to add more content. You can add multiple assets from a folder or add multiple folders at a time. But you cannot add assets from multiple folders at a time. 

To configure the references to publish or not publish for a form or other assets, select the form or the asset and click Published References.  

A screenshot of a computer

Description automatically generated 

In the Published References dialog box, uncheck the assets you plan to not-publish and click done. 


A screenshot of a computer

Description automatically generated


## Publish or unpublish a form later 

 
Along with allowing you to publish or unpublish forms at a later date and time, the publish or unpublish later option also allows to configure a workflow. The forms are published or unoublished after completion of the workflow. To schedule a form for publishing or unpublishing: 

1. From the Experience Manager Forms console, navigate to the parent folder and select the form that you want to schedule for publishing. 
1. Click Manage Publication option from the toolbar. 
1. Click Publish or Unpublish from Action, and then select the Destination where you want to publish or unpublish the content.  

    * Preview: Use the Preview option to publish or unpublish to an Experience Manager Forms preview environment. The Experience Manager Forms preview environments are used to test under development forms.  
    * Publish: Use the Experience Manager Forms Publish option to send the form to Experience Manager Forms publish environment after the form is ready to use in a production environment.  
 

1. Select Later from Scheduling. 

1. Select an Activation date and specify the date and time. Click Next. 

    A screenshot of a computer

    Description automatically generated 

1. In the Scope tab, Add Content (if necessary). Click Next. 

    A screenshot of a computer

    Description automatically generated 

1, (Optional) In the Workflows tab, specify a Workflow title. Click Publish Later. 

A screenshot of a computer

Description automatically generated 

## Determining Publication Status 

There are multiple ways to determine the publishing status: 

* Log in to the destination instance to verify the published forms and other assets (depending upon the scheduled date or time). 

* Use the timeline view to determine the publication status. 

* Use the page information menu in Adaptive Forms editor.  