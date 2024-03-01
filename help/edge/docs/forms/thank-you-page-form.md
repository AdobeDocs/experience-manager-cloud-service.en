---
title: Configure thank you page for EDS Forms
description: Learn how to configure thank you pages and redirection for EDS Forms to optimize user experience and streamline user journeys.
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
---

# Configuring Thank You Pages and Redirection in Adaptive Forms Blocks

Thank you pages and redirection are vital aspects of user experience enhancement, providing users with confirmation, clear communication, and smooth navigation after form submission.

## Configuring Thank You Pages

Thank you pages serve as a reassuring acknowledgment to users and enable organizations to communicate essential information while reinforcing brand identity. Follow these steps to configure a thank you page for EDS Forms:

1. Access your AEM Edge Delivery project folder on Microsoft SharePoint or Google Workspace.
1. Create a Microsoft Word or Google Docs file named "thankyou" within your project directory.
1. Add your thank you message to the "thankyou" file.
    ![Example thank you page](/help/edge/assets/sample-thankyou-page.png) 
1. Utilize AEM Sidekick to preview and publish the "thankyou" file.

## Redirecting Users After Submission

Redirection facilitates seamless user journeys by guiding users to relevant destinations, optimizing engagement, and increasing conversion rates. 

By default, the Adaptive Forms block redirects the users to the "thankyou" page. To redirect users to a page other than the default "thankyou" page, you have two options: 

* either replace the existing "thank you" page with a different page, or 
* redirect the "thankyou" page to another page of your choice.

### Replace the Existing "thankyou" Page

1. Open the "[EDS Project]/blocks/form/form.js" file for editing.
1. Change the `thankyou` page in the following line to page of your choice:

    ```JavaScript

    window.location.href = form.dataset?.redirect || 'thankyou';


    ```

    For example,

    ```JavaScript

    window.location.href = form.dataset?.redirect || 'payment';
        
    ```
    
    >[!NOTE]
    >
    > Ensure that a page with the same name exists in your Edge Delivery Service project folder on either Microsoft SharePoint or Google Workspace. If the page does not exist, proceed to create and publish it.  

1. Proceed to check in the updated 'form.js' folder and its underlying files to your Edge Delivery Service project on GitHub. This update ensures that the form now redirects to the updated page as specified.

1. Ensure that the page exists in your EDS project folder and publish it.


### Use Website Redirects

Configure a website redirect to direct the "thankyou" page to a different page. Refer to the [Redirects documentation](https://www.aem.live/docs/redirects) for detailed instructions.


