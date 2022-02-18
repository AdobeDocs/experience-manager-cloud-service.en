---
title: Introduction to Production Programs 
description: Learn what production programs are and suggestions for how to set up yours.
exl-id: bb8d4a5a-b26a-4718-9327-149fedb87e6a
---

# Introduction to Production Programs {#production-programs}

A production program is intended for a user who is familiar with AEM and Cloud Manager and is ready to start writing, building, and testing code with the objective of deploying it to host live traffic.

>[!NOTE]
>
>Production programs can not be deleted.

A program creation wizard guides the user through selections depending on the user’s objective in creating the program.

Based on the unused solution entitlements available to the specific customer or organization, the user has control over how to map available (unused) solution entitlements to Cloud Manager programs. 

## Program Creation Considerations {#program-creation-considerations}

The following table describes common scenarios to consider when creating programs in Cloud Manager.

|Unused Solution Entitlements Available|Create Program Options|What's Included|When to Use|Examples|
|--- |--- |--- |--- |---|
|1 Sites solution |Create 1 Sites only program|1 Production + 1 Stage, 1 Development|N/A|N/A|
|1 Assets solution |Create 1 Assets only program|1 Production + 1 Stage, 1 Development|N/A|N/A|
|1 Sites +1 Assets |Create one Program: 1 Sites &amp; Assets program|1 Production + 1 Stage, 2 Development| When a majority of the digital assets are used to support the sites implementation.<br>In such cases, most of the digital assets are in a finished state, ready to be used for cross-channel experiences via Sites.<br>Typically, a single team is responsible for managing content for both Sites and Assets.|Images that are primarily used for a website.<br>PDFs that will be distributed via an internal portal built in AEM Sites.|
|1 Sites +1 Assets |Create separate programs: 1 Sites only program &amp; 1 Assets only program |1 Production + 1 Stage, 1 Development<br> 1 Production + 1 Stage, 1 Development |When many digital assets do not directly support the sites implementation.<br> In such cases, assets are in various states, including raw file types and works in progress.<br>A dedicated creative team manages digital assets through its own lifecycle and has separate workflows and release cycles than the Sites content management team.|Raw images from a photo shoot are stored in the Assets program and only a select few will be used on the Sites implementation.<br>A large number of Creative Cloud file types, like Photoshop and Illustrator, are managed in AEM Assets and go through their own approval workflow before a finished asset is generated.<br>Consider using [Connected Assets](/help/assets/use-assets-across-connected-assets-instances.md#overview-of-connected-assets) in such cases.|
|1 Sites + 1 Sites |Create separate programs: 1 Sites only program &amp; 1 Sites only program|1 Production + 1 Stage, 1 Development<br>1 Production + 1 Stage, 1 Development|For multi-tenant sites implementations.<br>In such cases, multiple sites with their own release schedule and dedicated development and content teams must be managed.|Two retail brands with dedicated websites and separate development teams|
