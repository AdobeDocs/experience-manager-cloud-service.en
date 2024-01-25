---
title: Dynatrace
description: Learn how to use Dynatrace with AEM as a Cloud Service
exl-id: b58c8b82-a098-4d81-bc36-664e890c8f66
---
# Dynatrace {#dynatrace}

Adobe provides the ability to use Dynatrace to monitor AEM as a Cloud Service as a part of enterprise deployment, identify the cause of any potential issues, and take action to remediate them as needed. 

With Dynatrace, you can get seamless observability for all your AEM applications. Dynatrace provides comprehensive visibility into the end-user experience by automatically detecting your AEM applications and visualizing their dependencies from the website to the container to the cloud service. Intertwined with end-to-end traces across every tier and Real User Monitoring, take your AEM content-led experiences to the next level without gaps or blind spots. If any anomalies arise, Dynatrace diagnoses them in realtime, with the Davis AI engine, and pinpoints the root cause down to the broken code before your customers are affected, thereby minimizing the mean time to repair.

To learn more about Dynatrace, see the [Adobe AEM Cloud Service integration](https://www.dynatrace.com/hub/detail/adobe-experience-manager-1/).

![AEM author and publisher performance metrics](/help/implementing/cloud-manager/assets/dynatrace-performance-metrics.png)

## Integrating Dynatrace with AEM as a Cloud Service {#integrating-dynatrace-with-aem-as-a-cloud-service}

Dynatrace customers may monitor their AEM environments by requesting connectivity through a customer support ticket.

The details required for connectivity requests are described below:

| **Field**  | **Description**  |
|---|---|
| Dynatrace Environment URL  | Your Dynatrace environment URL.<br><br>For Dynatrace SaaS customers, the format is `https://<you-environment-id>.live.dynatrace.com`.<br><br>For Dynatrace Managed customers, the format is `https://<your-managed-url>/e/<environmentId>`  |
| Dynatrace Environment ID  | Your Dynatrace environment ID. Please see Get Dynatrace environment information for how to get this. |
| Dynatrace Environment Token  | Your Dynatrace environment token. Please see Get Dynatrace environment information for how to get this.<br><br>This should be considered a secret, so use appropriate security practices. For example, password protect it in a website such as **zerobin.net**, which the customer support ticket can reference, along with the password.  |
| Dynatrace API access token  | The API access token of your Dynatrace environment.  Please see Create a Dynatrace API access token for how to create this.<br><br>This should be considered a secret so use appropriate security practices. For example, password protect it in a website such as **zerobin.net**, which the customer support ticket can reference, along with the password.<br><br>Note: This is only required for Dynatrace Managed.  |
| Dynatrace ActiveGate Port | Your Dynatrace ActiveGate port that the AEM integration should connect to.<br><br>Note: This is only required for Dynatrace Managed.  |
| Dynatrace ActiveGate Network Zone | Your Dynatrace ActiveGate network zone to route AEM monitoring data efficiently across data centers and network regions.<br><br>Note: A Dynatrace ActiveGate network zone is optional.  |
| AEM Environment ID(s)  | The AEM environment id(s) for Dynatrace to monitor. |

## Create a Dynatrace API access token {#create-dynatrace-access-token}

1. Login to your Dynatrace environment.
1. In the Dynatrace menu, go to Manage > Access tokens.
1. Select Generate new token.
1. Define a token name.
 
1. Optional: Set an expiration date. Please make sure to generate a new token before it expires.
1. Set the token scope to PaaS integration - Installer download
1. Select Generate token.
1. Copy the generated access token and store it in a secure place.


## Get Dynatrace environment information {#get-dynatrace-env-info}

1. Execute the following API request to your Dynatrace environment:

```
curl -X GET "<environmentUrl>/api/v1/deployment/installer/agent/connectioninfo" -H "accept: application/json" -H "Authorization: Api-Token <accessToken>"
```
Replace \<environmentUrl\> with your Dynatrace environment URL and with your created API access token.

1. Copy the \<environmentUrl\> and \<environmenToken\> from the response payload and store them in a secured place.
  
```
{
   "tenantUUID": "<environmentId>",
   "tenantToken": "<environmentToken>",
   "communicationEndpoints": [
   ... 
   ],
   "formattedCommunicationEndpoints": "<endpoints>" 
}
```
