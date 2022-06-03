---
title: New Relic One
description: Learn about the New Relic One application performance monitoring (APM) service for AEM as a Cloud Service and how you can access it.
exl-id: 9fa0c5eb-415d-4e56-8136-203d59be927e
---

# New Relic One {#user-access}

Learn about the New Relic One application performance monitoring (APM) service for AEM as a Cloud Service and how you can access it.

## Introduction {#introduction}

Adobe places a great emphasis on the monitoring, availability, and performance of your application. AEM as a Cloud Service provides access to a custom New Relic One monitoring suite as a part of the standard product offering to ensure your teams have the maximum visibility to your AEM as a Cloud Service system and environment performance metrics.

This document describes the New Relic One application performance monitoring (APM) features enabled on your AEM as a Cloud Service environments to help support performance and allow you to get the most out of AEM as a Cloud Service.

When a new Production program is created, the New Relic One sub-account associated with your AEM as a Cloud Service Program is automatically created. 

## Features {#transaction-monitoring}

New Relic One APM for AEM as a Cloud Service has many features.

* Direct access to a dedicated New Relic One account (access managed by Adobe Support)

* Instrumented New Relic One APM agent that shows exact method calls with line numbers, including external dependencies and databases

* Holistic performance optimization by combining key metrics from infrastructure-level monitoring as well as application (Adobe Experience Manager) monitoring

* Exposure of AEM as a Cloud Service JMX Mbeans and health checks directly within New Relic Insights metrics, allowing for deep inspection of application stack performance and health metrics.

## Manage New Relic One Users {#manage-users}

Follow these steps to define the users of your New Relic One sub-account associated with your AEM as a Cloud Service Program.

>[!NOTE]
>
>A user in **Business Owner** or **Deployment Manager** role must be logged in to manage New Relic One users.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Click on the program for which you want to manage your New Relic One users.

1. Switch to the **Environments** from the **Program Overview** page by clicking the **Environments** tab at the top of the screen.

1. On the **Environments** screen, click the ellipsis button at the top of the screen next to the **Add Environment** button.

1. In the ellipsis menu, click **Manage users**.

   ![Manage users](assets/newrelic-manage-users.png)

1. In the **Manage New Relic users** dialog, enter the first and last name of the user you wish to add, and click the **Add** button. Repeat this step for all users you wish to add.

   ![Add users](assets/newrelic-add-users.png)

1. To remove a New Relic One users, click the delete button at the right end of the row representing the user.

1. Click **Save** to create the users.

Once the users are defined, New Relic sends a confirmation email to each user to whom you granted access, so the user can complete the setup process and sign in.

>[!NOTE]
>
>If you are managing the New Relic One users, you must also add yourself as a user in order to also have access. Being the **Business Owner** or **Deployment Manager** does not suffice to have access to New Relic One. You must create yourself as a user as well.

## Accessing New Relic One {#accessing-new-relic}

You can access New Relic One via Cloud Manager or directly.

To access New Relic One via Cloud Manager:

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Click on the program for which you want to access New Relic One.

1. Switch to the **Environments** from the **Program Overview** page by clicking the **Environments** tab at the top of the screen.

1. On the **Environments** screen, click the ellipsis button at the top of the screen next to the **Add Environment** button.

1. In the ellipsis menu, click **Open New Relic**.

1. In the new browser tab that opens, sign in to New Relic One.

To access New Relic One directly:

1. Navigate to New Relic's login page at [`https://login.newrelic.com/login`](https://login.newrelic.com/login)

1. Sign in to New Relic One.

### Verifying Your Email {#verify-email}

If you are asked to verify your email during login to New Relic One, it means your email is associated with multiple accounts. This allows you to choose which account to access.

If you do not verify your email address, New Relic will attempt to log you in with the most recently created user record associated with your email address. To avoid verifying your email during each login, click the **Remember Me** checkbox in the login screen.

For more help, please open a support ticket via the [AEM Support Portal](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).

## Troubleshooting New Relic One Access {#troubleshooting}

If the user cannot locate the original account confirmation email follow these steps.

1. Navigate to New Relic's login page at [`login.newrelic.com/login`](https://login.newrelic.com/login).

1. Select **Forgot your password?**.

   ![New Relic login](/help/implementing/cloud-manager/assets/new-relic/newrelic-1.png)

1. Type the account email address, and select **Send my reset link**.

   ![Enter email address](/help/implementing/cloud-manager/assets/new-relic/newrelic-2.png)

1. New Relic will send the user an email containing a link to confirm the account.

If you complete the sign up process and are unable to log in to your account due to email or password error messages, please log a support ticket via the [Admin Console](https://adminconsole.adobe.com/).

If you don't receive an email from New Relic:

* Check your [spam filters](https://docs.newrelic.com/docs/accounts/accounts-billing/account-setup/create-your-new-relic-account/).
* If applicable, [add New Relic to your email allow list](https://docs.newrelic.com/docs/accounts/accounts/account-maintenance/account-email-settings/#email-whitelist).
* If neither suggestion help, please provide feedback on the support ticket and Adobe Support team will help you further.

## Limitations {#limitations}

The following limitations apply to adding users to New Relic One:

* A maximum of 25 users can be added. If the maximum number of users has been reached, remove users in order to be able to add new users.
* Users added to New Relic will be of the type **Restricted** refer to [the New Relic documentation for details.](https://docs.newrelic.com/docs/accounts/original-accounts-billing/original-users-roles/users-roles-original-user-model/#:~:text=In%20general%2C%20Admins%20take%20responsibility,Restricted%20Users%20can%20use%20them.&text=One%20or%20more%20individuals%20who,change)%20any%20New%20Relic%20features.)
* AEM as a Cloud Service only offers the New Relic One APM solution and does not provide support for alerting, logging, or API integrations.

For more help or additional guidance on New Relic One offerings for your AEM as a Cloud Service Program, please open a support ticket via the [AEM Support Portal](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).

## Frequently Asked Questions for New Relic Account {#faqs}

### What does Adobe monitor with New Relic One? {#adobe-monitor}

Adobe monitors the AEM as a Cloud Service author, publish and preview (where available) services via New Relic One's Java plug-in. Adobe enables custom New Relic One APM telemetry and monitoring across non-production and production AEM as a Cloud Service environments. 

Your New Relic One account is attached to a primary Adobe-maintained account and has multiple applications reporting into it: three per AEM as a Cloud Service Environment. 

* One application for the author service per environment
* One application for the publish service per environment (including Golden Publish)
* One application for the preview service per environment

Please note:

* Each application uses one license key.
* AEM as a Cloud Service environments report to only one New Relic One account.
* Full monitoring metrics and events for both New Relic One are retained for seven days.

### Who can access the New Relic One cloud service data? {#access-new-relic-cloud}

Full read access will be granted for up to 10 members of your team. Read access will include all APM metrics collected by the New Relic One agent.

### Is custom SSO configuration supported? {#custom-sso}

Custom SSO configuration is not supported for the New Relic One account provisioned by Adobe.

### What if I already have an on-premises New Relic subscription? {#new-relic-subscription}

New Relic One is the new observability platform from New Relic and it enables Adobe support and your teams to observe, monitor, and view metrics and events, all in one place.

New Relic One provides users the ability to search across all accounts where they have access and visualize the data from all services and hosts in one view.

While Adobe support will monitor the AEM as a Cloud Service application using New Relic One and other in-house tools as part of your service, your teams can continue to leverage New Relic for on-premises hosted services and infrastructure. They will be able to visualize the data from both Adobe New Relic One account and customer-managed New Relic accounts.

>[!NOTE]
>
>To view both data sets within New Relic One, a user must have the right permissions and use the same login methodology for both accounts (Adobe New Relic One and the customer-managed New Relic accounts).
