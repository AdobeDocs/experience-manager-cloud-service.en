---
title: Configure thank you page for EDS Forms
description: Configure thank you page for EDS Forms
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
---

# Configure Form block redirects

You have the option to configure the form block to redirect to a different page on your website instead of the default "thankyou" page,. To set up another page as the redirect destination

1. Open the `[EDS Project]/blocks/form/form.js` file for editing.

    ![code for thank you node](/help/edge/assets/change-thankyou-node.png)

1. Change the `thankyou` node in the following line to node of your choice:

    ```JavaScript

    window.location.href = form.dataset?.redirect || 'thankyou';


    ```

    For example,

    ```JavaScript

    window.location.href = form.dataset?.redirect || 'home';
        
    ```
    
    >[!NOTE]
    >
    > Ensure that a document page with the same name is created in your Edge Delivery Service project folder on either Microsoft SharePoint or Google Sheets, if it hasn't been created already.
 

1. Proceed to check-in the updated 'form.js' folder and its underlying files to your Edge Delivery Service project on GitHub. This update ensures that the form now redirects to the updated node as specified.
