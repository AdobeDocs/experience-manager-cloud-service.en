---
title: Cloud Manager Environment Variables
description: Standard environment variables can be configured and managed via Cloud Manager and be provided to the run time environment, to be used in OSGi configuration.
---

# Cloud Manager Environment Variables {#environment-variables}

Standard environment variables can be configured and managed via Cloud Manager. They are provided to the run time environment and can be used in OSGi configurations. Environment variables can be either environment-specific values or environment secrets, based on what is being changed.

## Overview {#overview}

Environment variables offer a host of benefits to users of AEM as a Cloud Service:

* They allow the behavior of your code and application to vary based on context and environment. For example, they can used to enable different configuration on the development environment vs. the production or stage environments to avoid costly mistakes.
* They only need to be configured and setup once and can be updated and deleted  when necessary.
* The values of the variables can be updated at any point of time without the need for any code changes or deployments to take effect.
* They enable you to separate code from configuration and avoid including sensitive information in your version control.
* The security of the AEM as a Cloud Service application is improved since these configurations live outside the code.

Typical use cases for using environment variables include connecting your AEM application with different external endpoints, using a reference when storing passwords instead of directly in the code base, and when multiple development environments exist in a program and some configuration differs from one environment to the next.

## Add Environment Variables {#add-variables}

1. Log into Adobe Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/).
1. Cloud Manager lists the various programs available. Tap or click the one you wish to manage.
1. Select the **Environments** tab for the chosen program then select the environment for which you want to create an environment variable in the left navigation panel.
1. Within the detail of the environment, select the **Configuration** tab then tap or click **Add**. 
   * If you're adding an environment variable for the first time, you will see an **Add Configuration** button. in the center of the page. Use this to launch the **Environment Configuration** dialog.
1. Enter the variable name, value, the service you wish to apply it to (Author/Publish/Preview), and if the type is variable or secret.
1. After you enter your new variables, you must select **Add** in the last column of the row containing the new variable.
  * You can enter multiple variables at once by entering a new line and tapping or clicking **Add**.
1. Tap or click **Save** to persist your variables.

You will see a status of **Updating** to indicate that the environment is being updated with your configuration. Once complete, your environment variable will be visible in the table.
Select Cancel if you wish to lose all your changes.


>[!TIP]
>
>If you wish to add multiple variables, it is recommended to add the first variable or secret, then use the **Add** button in the **Environment Configuration** dialog to add the additional variables. This way you can add them with one update to the environment.

## Update Environment Variables {#update-variables}

After you have created environment variables, you can update them using the **Add/Update** button to launch the **Environment Configuration** dialog.

1. Log into Adobe Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/).
1. Cloud Manager lists the various programs available. Tap or click the one you wish to manage.
1. Select the **Environments** tab for the chosen program then select the environment for which you want to create an environment variable in the left navigation panel.
1. Within the detail of the environment, select the **Configuration** tab then tap or click **Add/update** in the top right to open the **Environment Configuration** dialog.
1. Using the ellipsis button in the last column of the row of the variable you wish to modify, select **Edit** or **Delete**. 
1. Edit the environment variable as necessary.
  * When editing, the ellipsis button will change to options to revert back to the original value or confirm your change.
  * When editing secrets, the values can only be updated, not viewed.
1. Once you've made all of the required configuration changes, tap or click **Save**.

You will see a status of **Updating** to indicate that the environment is being updated with your configuration. Once complete, your environment variable will be visible in the table.
Select Cancel if you wish to lose all your changes.

>[!TIP]
>
>If you wish to update multiple variables, it is recommended to use the **Environment Configuration** dialog to update all of the necessary variables at once before tapping or clicking **Save**. This way you can add them with one update to the environment.
