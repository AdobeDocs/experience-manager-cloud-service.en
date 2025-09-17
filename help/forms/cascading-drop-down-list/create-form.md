---
title: Create form using universal editor
description: Use Adaptive Forms expressions to add automatic validation, calculation, and turn visibility of a section on or off.
feature: Adaptive Forms, Foundation Components
role: User
hide: yes
hidefromtoc: yes
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