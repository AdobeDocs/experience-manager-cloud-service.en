---
title: Add a Specialized Testing Environment
description: Learn how Specialized Testing Environments in Cloud Manager provide a dedicated space to validate features under near-production conditions, ideal for stress testing and advanced pre-deployment checks.
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
badge: label="Early Adopter" type="Positive" url="/help/implementing/cloud-manager/release-notes/current.md#gitlab-bitbucket" 


---
# Add a Specialized Testing Environment{#add-special-test-enviro}

>[!NOTE]
>
>>The feature described in this article is only available through the early adoption program. To sign up as an early adopter, see [Specialized Testing Environment](/help/implementing/cloud-manager/release-notes/current.md#specialized-test-environment).

Cloud Manager now supports a new environment type called Specialized Testing Environment, designed to help teams validate features under near-production conditions before going live. This environment type is distinct from traditional Development, Rapid Development, or Production environments and offers a focused space for executing advanced validation scenarios.

Specialized Testing Environments allow you to simulate real-world user conditions with greater control, making them ideal for stress testing, configuration validation, and feature rollout checks. These environments can be selected at the time of creation through the Cloud Manager UI. Once created, the primary region of the environment (e.g., "United States (West US)") is locked and cannot be changed.

This environment type shares the same base provisioning infrastructure as other non-production environments but is configured for more rigorous test conditions. It can be integrated into complex CI/CD workflows or used for isolated validation without disrupting ongoing development.

For organizations requiring robust pre-deployment testing workflows, this addition provides a high-fidelity testing layer between Development and Production environments.

See also [Manage Environments](/help/implementing/cloud-manager/manage-environments.md)

## Add a Specialized Testing Environment {#add-specialize-testing-environment}

To add or edit an environment, a user must be a member of the **Business Owner** role.

**To add a Specialized Testing Eenvironment:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, click the program for which you want to add an environment.

1. Do one of the following: 

   If the **Add Environment** option is dimmed (disabled), it may be due to a lack of permissions or dependent on the licensed resources. 

   * On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, on the **Environments** card, click **Add Environment**.

   ![Environments card](assets/no-environments.png)

   * On the left side panel, click ![Data icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Data_18_N.svg) **Environments**, then on the Environments page, near the upper-right corner, click **Add Environment**.

     ![Environments tab](assets/environments-tab.png)
   
1. In the **Add environment** dialog box, do the following:
   
   * Select an [**environment type**](#environment-types). The number of available/used environments is displayed in parentheses behind the environment type name.
   * Provide an environment **Name**. The environment name cannot be changed after the environment is created.
   * Provide an optional **Description** for the environment.
   * If you are adding a **Production + Stage** environment, you must provide an environment name and description for both your production and staging environments.
   * Select a **Primary region** from the drop-down. The primary region cannot be changed after creation. Also, depending on your available entitlements, you may be able to configure [multiple regions](#multiple-regions).
  
   ![Add environment dialog box with Specialized Testing Environment radio button selected](assets/specialized-test-environment.png)

1. Click **Save**.

The **Overview** page now displays your new environment in the **Environments** card. You can now set up pipelines for your new environment.

