---
title: Introduction to Production Programs 
description: Introduction to Production Programs 
---

# Introduction to Production Programs {#production-programs}

A *Production* program is intended for a user who is familiar with AEM and Cloud Manager and is ready to start writing, building and testing code with the objective of deploying it to Production.

>[!NOTE]
>You will not be able to delete a Production program.

A program creation wizard will guide the user to make selections, depending on the user’s objective in creating the program. Based on the unused solution entitlements available to the specific customer or organization, the user has control over how to map available (unused) solution entitlements to Cloud Manager programs. 

## Program Creation Considerations {#program-creation-considerations}

The table below describes common scenarios to be taken into consideration while creating programs in Cloud Manager:

|Unused Solution Entitlements available in the Org|Create Program Options|What's Included|When to Use and other Considerations|
|--- |--- |--- |--- |
|1 Sites solution |Create 1 Sites only program|1 Production + 1 Stage, 1 Development|NA|
|1 Sites + 1 Sites |Create separate programs: 1 Sites only program & 1 Sites only program|1 Production + 1 Stage, 1 Development 1 Production + 1 Stage, 1 Development|Multi-tenant sites implementations. Multiple sites with their own release schedule and dedicated development and content teams. *Common Examples*: Two retail brands with dedicated websites and separate development teams|
|1 Sites +1 Assets |Create one Program: 1 Sites & Assets program|1 Production + 1 Stage, 2 Development| A majority of the digital assets are used to support the sites implementation. Most of the digital assets are in a finished state, ready to be used for cross-channel experiences via Sites.Typically, a single team is responsible for managing content for both Sites and Assets. *Common Examples*:  Images that are primarily used for a website. PDFs that will be distributed via an internal portal built in AEM Sites.|
|1 Sites +1 Assets |Create separate programs: 1 Sites only program & 1 Assets only program |1 Production + 1 Stage, 1 Development 1 Production + 1 Stage, 1 Development |Many digital assets do not directly support the sites implementation. Assets managed are in various states, including raw file types and works in progress. A dedicated creative team manages digital assets through its own lifecycle and have separate workflows and release cycles than the Sites content management team. *Common Examples*: Raw images from a photoshoot are stored in the Assets program and only a select few will be used on the Sites implementation. A large number of Creative Cloud file types, like Photoshop and Illustrator, are managed in AEM Assets and go through their own approval workflow before a finished asset is generated. Features to leverage: [Connected Assets](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/assets/admin/use-assets-across-connected-assets-instances.html?lang=en#overview-of-connected-assets) |
|1 Assets solution |Create 1 Assets only program|1 Production + 1 Stage, 1 Development|NA|


