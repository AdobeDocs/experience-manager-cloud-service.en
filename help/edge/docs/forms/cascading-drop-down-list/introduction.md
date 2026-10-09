---
title: Cascading Drop Down List
description: Use API Integration to dynamically populate drop down list
feature: Edge Delivery Services
role: User,Developer
exl-id: 3e947bc4-f954-40c3-909f-86285267bc31
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
---
# Use case description

When building forms or applications, it's often useful to guide users through location selection in a structured way. A cascading dropdown list makes this simple and user-friendly — the user first selects a country, which filters the list of available states/provinces, and then a final choice of cities based on the state. This approach not only keeps forms cleaner, but also prevents invalid combinations (like picking a city that doesn't exist in a chosen state).

The following steps are required to accomplish this use case

- Create API Integration
- Create form with fields to capture country/state/city
- Create rule to populate the drop down lists using the API integration
