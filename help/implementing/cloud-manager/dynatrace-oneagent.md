---
title: Dynatrace OneAgent
description: Learn how to use Dynatrace's OneAgent with AEM as a Cloud Service
---

# Dynatrace OneAgent {#dynatrace-oneagent}

>[!INFO]
>
>This feature is part of the AEM adopter program.

Adobe provides the ability to use Dynatrace's OneAgent to monitor AEM as a Cloud Service as a part of an enterprise deployment, identify the cause of any potential issues, and take action to remediate them as needed.

## Integrating OneAgent with AEM as a Cloud Service {#integrating-oneagent-with-aem-as-a-cloud-service}

Dynatrace OneAgent customers may monitor their AEM usage by requesting connectivity through a customer support ticket.

The details required for connectivity requests are described below:

| **Field**  | **Description**  |
|---|---|
| Environment URL  | Your Dynatrace environment URL.<br><br>For Dynatrace SaaS customers, the format is `https://<environment>.live.dynatrace.com`.<br><br>For Dynatrace Managed customers, the format is `https://<your-managed-url>/e/<environmentId>`  |
| Environment ID  | Your Dynatrace environment ID, which can be found in the Environment URL  |
| Environment Token  | Your OneAgent environment token. Please consult Dynatrace documentation for how to create this.<br><br>This should be considered a secret, so use appropriate security practices. For example, password protect it in a website such as **zerobin.net**, which the customer support ticket can reference, along with the password.  |
| API access token  | The API access token of your Dynatrace environment. Please consult Dynatrace documentation for how to create this.<br><br>This should be considered a secret so use appropriate security practices. For example, password protect it in a website such as **zerobin.net**, which the customer support ticket can reference, along with the password.<br><br>Note: This is only required for Dynatrace Managed.  |

