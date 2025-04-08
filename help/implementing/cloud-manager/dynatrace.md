---
title: Dynatrace
description: Learn how to use Dynatrace with AEM as a Cloud Service
exl-id: b58c8b82-a098-4d81-bc36-664e890c8f66
solution: Experience Manager
feature: Log Files, Developing
role: Admin, Architect, Developer
---
# Dynatrace {#dynatrace}

Adobe provides the ability to use Dynatrace to monitor AEM as a Cloud Service as a part of enterprise deployment, identify the cause of any potential issues, and take action to remediate them as needed. 

With Dynatrace, you can get seamless observability for all your AEM applications. Dynatrace provides comprehensive visibility into the end-user experience by automatically detecting your AEM applications and visualizing their dependencies from the website to the container to the cloud service. Intertwined with end-to-end traces across every tier and Real Use Monitoring, take your AEM content-led experiences to the next level without gaps or blind spots. If any anomalies arise, Dynatrace diagnoses them in realtime, with the Davis AI engine, and pinpoints the root cause down to the broken code before your customers are affected, thereby minimizing the mean time to repair.

To learn more about Dynatrace, see the [Adobe AEM Cloud Service integration](https://www.dynatrace.com/hub/detail/adobe-experience-manager-1/).

![AEM author and publisher performance metrics](/help/implementing/cloud-manager/assets/dynatrace-performance-metrics.png)

## Integrating Dynatrace with AEM as a Cloud Service {#integrating-dynatrace-with-aem-as-a-cloud-service}

Dynatrace customers may monitor their AEM environments by requesting connectivity through a customer support ticket.

The details required for connectivity requests are described below:

| **Field**  | **Description**  |
|---|---|
| [!DNL Dynatrace Environment URL]  | Your Dynatrace environment URL.<br><br>For Dynatrace SaaS customers, the format is `https://<your-environment-id>.live.dynatrace.com`.<br><br>For Dynatrace Managed customers, the format is `https://<your-managed-url>/e/<environmentId>`  |
| [!DNL Dynatrace Environment ID]  | Your Dynatrace environment ID. See [How do I get my Dynatrace Connection Details?](#how-do-i-get-my-dynatrace-connection-details) for how to get this. |
| [!DNL Dynatrace Environment Token]  | Your Dynatrace environment token. See [How do I get my Dynatrace Connection Details?](#how-do-i-get-my-dynatrace-connection-details) for how to get this.<br><br>This should be considered a secret, so use appropriate security practices. For example, password protect it in a website such as **zerobin.net**, which the customer support ticket can reference, along with the password.  |
| [!DNL Dynatrace API access token]  | The API access token of your Dynatrace environment. See [Create a Dynatrace API access token](#create-dynatrace-access-token) for how to create this.<br><br>This should be considered a secret so use appropriate security practices. For example, password protect it in a website such as **zerobin.net**, which the customer support ticket can reference, along with the password.<br><br>Note: This is only required for Dynatrace Managed.  |
| [!DNL Dynatrace ActiveGate Port] | Your Dynatrace ActiveGate port that the AEM integration should connect to.<br><br>Note: This is only required for Dynatrace Managed.  |
| [!DNL Dynatrace ActiveGate Network Zone] | Your [Dynatrace ActiveGate network zone](https://docs.dynatrace.com/docs/manage/network-zones) to route AEM monitoring data efficiently across data centers and network regions.<br><br>Note: A Dynatrace ActiveGate network zone is optional.  |
| [!DNL AEM Environment ID(s)]  | The AEM environment ID(s) for Dynatrace to monitor. |

>[!NOTE]
>
>Once Dynatrace is integrated, data will no longer flow to other APM tools such as New Relic, if it was previously enabled.

## FAQ {#faq}

### Which license do I need for Dynatrace AEM Monitoring? {#which-license-do-i-need-for-AEM-monitoring}

Dynatrace AEM monitoring requires a Dynatrace license. Dynatrace AEM licensing is based on [full-stack monitoring for Kubernetes containers](https://docs.dynatrace.com/docs/shortlink/dps-hosts#gib-hour-calculation-for-containers-and-application-only-monitoring). The memory sizes of monitored AEM containers (author and publisher services) are automatically detected.

The Adobe deployment specifications per AEM environment are:

* Production: On average, 4 containers, 16 GB of memory each
* Non-production: On average, 4 containers, 8 GB of memory each

To learn more about Dynatrace licensing, see the [Dynatrace Platform Subscription](https://docs.dynatrace.com/docs/shortlink/dynatrace-platform-subscription).

### How do I get my Dynatrace Connection Details? {#how-do-i-get-my-dynatrace-connection-details}

1. Execute the following API request to your Dynatrace environment:  

   ```
   curl -X GET "<environmentUrl>/api/v1/deployment/installer/agent/connectioninfo" -H "accept: application/json" -H "Authorization: Api-Token <accessToken>"
   ```


   Replace `<environmentUrl>` with your Dynatrace environment URL and `<accessToken>` with your created API access token.  

1. Copy the `<environmentId>` and `<environmentToken>` from the response payload and store them in a secured place.
      
   ```
   {
      "tenantUUID": "<environmentId>",
      "tenantToken": "<environmentToken>",
      "communicationEndpoints": [...]
   }
   ```

### Create a Dynatrace API access token {#create-dynatrace-access-token}

1. Login to your Dynatrace environment.
1. Go to **[!DNL Access tokens]** and select **[!DNL Generate new token]**.
1. Define a [!DNL token name].
1. Set the token scope to **[!DNL PaaS integration - Installer download]**.
1. Select **[!DNL Generate token]**.
1. Copy the generated access token and store it in a secure place.





