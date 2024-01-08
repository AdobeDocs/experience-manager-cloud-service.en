---
title: Dynatrace OneAgent
description: Learn how to use Dynatrace's OneAgent with AEM as a Cloud Service
---

# Dynatrace OneAgent {#dynatrace-oneagent}

Adobe provides the ability to use Dynatrace's OneAgent to monitor AEM as a Cloud Service as a part of an enterprise deployment, identify the cause of any potential issues, and take action to remediate them as needed. <!-- When GA, add: Read this [Dynatrace article](https://www.dynatrace.com/hub/detail/adobe-experience-manager/) about AEM monitoring to learn more. -->

## Integrating OneAgent with AEM as a Cloud Service {#integrating-oneagent-with-aem-as-a-cloud-service}

Dynatrace OneAgent customers may monitor their AEM usage by requesting connectivity through a customer support ticket.

The details required for connectivity requests are described below:

| **Field**  | **Description**  |
|---|---|
| Dynatrace Environment URL  | Your Dynatrace environment URL.<br><br>For Dynatrace SaaS customers, the format is `https://<you-environment-id>.live.dynatrace.com`.<br><br>For Dynatrace Managed customers, the format is `https://<your-managed-url>/e/<environmentId>`  |
| Dynatrace Environment ID  | Your Dynatrace environment ID, which can be found in the Environment URL  |
| Dynatrace Environment Token  | Your OneAgent environment token. Please consult Dynatrace documentation for how to create this.<br><br>This should be considered a secret, so use appropriate security practices. For example, password protect it in a website such as **zerobin.net**, which the customer support ticket can reference, along with the password.  |
| Dynatrace API access token  | The API access token of your Dynatrace environment. Please consult Dynatrace documentation for how to create this.<br><br>This should be considered a secret so use appropriate security practices. For example, password protect it in a website such as **zerobin.net**, which the customer support ticket can reference, along with the password.<br><br>Note: This is only required for Dynatrace Managed.  |
| Dynatrace ActiveGate Port | Your Dynatrace ActiveGate port that OneAgent should connect to.<br><br>Note: This is only required for Dynatrace Managed.  |
| AEM Environment ID(s)  | The AEM environment id(s) for Dynatrace to monitor. |


