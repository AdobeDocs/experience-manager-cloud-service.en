---
title: Cascading Drop Down List
description: Use API Integration to dynamically populate drop down list
feature: Edge Delivery Services
role: User,Developer

---
# Use case description

When building forms or applications, it's often useful to guide users through location selection in a structured way. A cascading dropdown list makes this simple and user-friendly — the user first selects a country, which filters the list of available states/provinces, and then a final choice of cities based on the state. This approach not only keeps forms cleaner, but also prevents invalid combinations (like picking a city that doesn't exist in a chosen state).

The following steps are required to accomplish this use case

- Create API Integration
- Create form with fields to capture country/state/city
- Create rule to populate the drop down lists using the API integration