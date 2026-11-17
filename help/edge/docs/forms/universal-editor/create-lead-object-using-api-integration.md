---
title: Create Salesforce Lead object using API Integration
description: Learn how to create a Salesforce Lead object using the API Integration.
feature: Adaptive Forms, Core Components, Edge Delivery Services
role: User, Developer
level: Beginner, Intermediate
keywords: integrating API in rule editor, invoke service enhancements
exl-id: 55835ffe-1b77-449b-b76d-16c0a343cf5c
hide: true
index: false
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: f2d27a5f-0d67-4d85-8a24-86a8d8a3574b
    internal-label: Developer tools
subfeature_v2:
  - id: f88183b7-5ea5-436c-ac46-96b53f0281ea
    internal-label: Edge Delivery Services
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
---
# Create Salesforce Lead object using API Integration

This use case walks through how to create a Lead in Salesforce using the API Integration. By the end of the process, you are able to:

Set up a [Connected App in Salesforce](https://help.salesforce.com/s/articleView?id=platform.ev_relay_create_connected_app.htm&type=5) to enable secure API access.

Configure CORS (Cross-Origin Resource Sharing) to allow code (such as JavaScript) running in a Web browser to communicate with Salesforce from a specific origin, add the origin to the allowed list as shown below

![cors](assets/salesforce-cors.png)

## Connected App Settings

The following settings are used in the connected app. You can assign the OAuth scopes depending on your requirements.
![connected-app-settings](assets/salesforce-connected-app-settings.png)

## Create API Integration

| Name                           | Value |
|--------------------------------|------------------|
| API url |https://`<your-domain>`d.my.salesforce.com/services/data/v32.0/sobjects/Lead             |
| Client ID |Specific to your connected app             |
| Client Secret  | Specific to your connected app             |
| OAuth URL      | https://login.salesforce.com/services/oauth2/authorize             |
| Access Token URL      | https://`<your-domain>`/services/oauth2/token             |
| Refresh Token URL      | https://`<your-domain>`/services/oauth2/token             |
| Authorization Scope      | api chatter_api full id openid refresh_token visualforce web             |
| Authorization Header      | Authorization Bearer             |

![api-integration](assets/salesforce-api-integration-create-lead.png)

## Input and Output parameters

Define the input parameters for the API call and map the output parameters using the following json

```json
{
    "id": "00QKY000001LyJR2A0",
    "success": true
}
```

![input-output](assets/create-lead-api-integration-input-output.png)

## Create a form

Create a simple adaptive form using the Universal Editor to capture the Lead object details as shown below
![lead-object-form](assets/create-lead.png)

Handle the click event on the Create Lead checkbox using the rule editor. Map the input parameters to the values of the appropriate form objects as shown below. Display the ID of the newly created Lead object in the `leadid` TextField object
![rule-editor](assets/create-leade-rule-editor.png)

## Test the integration

- Preview the form
- Enter some meaningful values
- Select the `Create Lead` checkbox to trigger the API call
- The Lead ID of the newly created Lead object is displayed in the `Lead ID` Text Field.
