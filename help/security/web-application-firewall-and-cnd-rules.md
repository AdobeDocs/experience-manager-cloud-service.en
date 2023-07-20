---
title: Configuring CDN and Web Application Firewall Rules to Filter Traffic
description: Use the CDN and Web Application Firewall Rules to Filter Malitious Traffic
---

# Configuring CDN and Web Application Firewall Rules to Filter Traffic {#configuring-cdn-and-waf-rules-to-filter-traffic}

>[!NOTE]
>
>This feature is not yet generally available.

Adobe will try to mitigate attacks against customer websites, but itt may be useful to proactively filter requests matching certain patterns so malicious traffic does not reach your application. Possible approaches include:

* Apache layer modules such as `mod_security`+
* Configuring rules that are deployed to the CDN using Cloud Manager's configuration pipeline. 

This article describes the latter approach, which offers two categories of rules:

1. **CDN rules**: block or allow requests based on request properties and request headers, including IP, paths, and user agent. These rules can be configured by all AEM as a Cloud Service customers
1. **WAF** (Web Application Firewall) rules: block requests that matches various patterns known to be associated with malicious traffic. These rules can be configured by customers who license the WAF add-on.

These rules can be deployed to all cloud environment types (RDE, dev, stage, prod) in production (non-sandbox) programs.

## Setup {#setup}

1. First, create the following folder and file structure the top level folder in git:

   ```
   config/
        cdn/
           cdn.yaml
           _config.yaml
   ```

1. `_config.yaml` describes the type of rules, the version, and the environment, as illustrated in the snippet below:

   ```
   kind: "CDN"
   version: "1"
   envType: "dev"
   ```

1. `cdn.yaml` should include a list of CDN rules and WAF rules, as described in sections below
1. In order to match WAF rules, WAF must be enabled in Cloud Manager, as described below for both the new and existing program scenarios. Note that a separate license must be purchased for WAF.

   1. In order to Configure WAF on a new Program, check the **WAF-DDOS Protection** check-box in the **Security** tab as shown below. Continue by following the steps described in [Add Production program](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md) to create your program

   1. In order to Configure WAF on an existing program, select the **Edit program** option by following the steps described in the [Editing Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/editing-programs.md) documentation. Then, in the **Security** tab of the wizard, you can un-check or check the WAF-DDOS option at any time

1. For environment types other than RDE, execute the Cloud Manager configuration pipeline, which can be configured as described below. 

   1. From the pipeline card in your Cloud Manager home page, select **Add Production Pipeline** or **Add Non-Production Pipeline** to launch the add pipeline wizard
   1. Select **Deployment Pipeline** in the configuration tab 

      ![Select the Deployment Pipeline option](/help/security/assets/deployment.png)

   1. Give your pipeline a name and select deployment triggers, then select **Continue** 
   1. In the **Source Code** tab, select **Targeted deployment**, then select **Config**

      ![Selet Targeted deployment](/help/security/assets/target-deployment.png)

   1. Select the repository and branch as needed. Note that if a Config pipeline already exists for the selected environment, this selection will be disabled.

      ![Overview of a Config Pipeline](/help/security/assets/config-pipeline.png)
      
      >[!NOTE]
      >
      >You can configure and run only one Config pipeline per environment.

   1. Select **Save**. Your new pipeline will appear in the pipeline card and can be run when you are ready. 
   1. For RDE, use the command line, as described in the section below.

## Rules Syntax {#rules-syntax}

The format of the rules is described below, followed by some examples in a subsequent section.

| **Property**   | **CND Rules**  | **WAF Rules**  | **Type**  | **Default**  | **Description**  |
|---|---|---|---|---|---|
| name  | X  | X  | String  | -  | Rule name (64 chars long, can only contains alphanumerics and - )  |
| when  | X  | X  | Condition  | -  | The basic structure is:<br><br>`{ <getter>: <value>, <predicate>: <value> }`<br><br>See Condition Structure syntax below, which describes the getters, predicates, and how to combine multiple conditions.  |
| action  | X  | X  | Enum  | log (CDN rules)  | For CDN rules: allow, block, log. Default is log.<br><br>For WAF rules: `enableWafRules`, `disableWafRules`, log. No default.  |
|  rateLimit | X  |   | RateLimit  | not defined  | Rate limiting configuration. Rate limiting is disabled if not defined.<br><br>There is a separate section further below describing the rateLimit syntax, along with examples.  |
| wafRules  |   |  X | `array[Enum]` | -  | List of WAF rules that should be enabled or disabled.<br><br>Examples include SQLI and XSS. See waf Rules list below for a full list.  |

     