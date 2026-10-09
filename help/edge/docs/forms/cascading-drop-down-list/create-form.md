---
title: Create form using universal editor
description: Create Adaptive Form to test the cascading drop down list using the API Integrations
feature: Edge Delivery Services
role: User
exl-id: 5ed71278-143c-4262-afaa-942e3682795f
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
---
# Create form using universal editor

Create the following form using the universal editor. The form has 3 drop down lists, whose values will be populated using the API integration
![adaptive-form](assets/address-form.png)

## Country of Residence

On initialization, the country of residence drop down will be populated with the results of the API call.
![initialize-event](assets/initialize-event.png) 

## Sucess Handler

The success handler was defined to set the enum and enumNames of the country drop down list with the appropriate values from the geonames array. The geonames array is available under the Event Payload option
![event-payload](assets/event-payload.png)
![success-handler](assets/success-handler.png)

## Fetch Child Values

The state or province drop down list is populated when the user makes a selection in the Country of Residence drop down list. The geonameId associated with the selected country is passed as an input parameter to the GetChildren API integration

![get-children](assets/invoke-service-get-children.png)

The sucees handler was defined to set the enum/enumNames of the StateOrProvince drop down field
![get-children-success-handler](assets/child-success-handler.png)

When the state or province is selected, you can populate the city drop down list by following the above mentioned pattern used for populating state or province drop down list.
