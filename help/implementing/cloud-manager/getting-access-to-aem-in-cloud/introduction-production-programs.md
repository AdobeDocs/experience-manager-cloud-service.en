---
title: Introduction to Production Programs 
description: Learn what production programs are and suggestions for how to set up yours.
exl-id: bb8d4a5a-b26a-4718-9327-149fedb87e6a
---

# Introduction to Production Programs {#production-programs}

A production program is intended for a team that is ready to start writing, building, and testing code with the objective of deploying it to host live traffic. 

After you [create your production program,](creating-production-programs.md) a [program creation wizard](using-the-wizard.md) guides the user through selections depending on the user’s objective in creating the program.

## Program Creation Options {#program-creation-options}

Your contractual agreement with Adobe defines the number and types of solutions available to your specific organization when creating production programs. You have control over how to map the available solutions to Cloud Manager programs. 

The following table describes common scenarios of available solutions and the typical production programs created based on them.

|Available Solutions|Program Options|What's Included|When to Use|Examples|
|--- |--- |--- |--- |---|
|1 Sites solution |Create 1 Sites-only program|1 Production + 1 Stage, 1 Development|N/A|N/A|
|1 Assets solution |Create 1 Assets-only program|1 Production + 1 Stage, 1 Development|N/A|N/A|
|1 Sites +1 Assets |Create one program: <br>1 Sites &amp; Assets program|1 Production + 1 Stage, 2 Development| When a majority of the digital assets are used to support the sites implementation.<br>In such cases, most of the digital assets are in a finished state, ready to be used for cross-channel experiences via Sites.<br>Typically, a single team is responsible for managing content for both Sites and Assets.|Images that are primarily used for a website.<br>PDFs that will be distributed via an internal portal built in AEM Sites.|
|1 Sites +1 Assets |Create separate programs:<br>1 Sites only program &amp; 1 Assets only program |1 Production + 1 Stage, 1 Development<br> 1 Production + 1 Stage, 1 Development |When many digital assets do not directly support the sites implementation.<br> In such cases, assets are in various states, including raw file types and works in progress.<br>A dedicated creative team manages digital assets through its own lifecycle and has separate workflows and release cycles than the Sites content management team.|Raw images from a photo shoot are stored in the Assets program and only a select few will be used on the Sites implementation.<br>A large number of Creative Cloud file types, like Photoshop and Illustrator, are managed in AEM Assets and go through their own approval workflow before a finished asset is generated.<br>Consider using [Connected Assets](/help/assets/use-assets-across-connected-assets-instances.md#overview-of-connected-assets) in such cases.|
|1 Sites + 1 Sites |Create separate programs:<br>1 Sites only program &amp; 1 Sites only program|1 Production + 1 Stage, 1 Development<br>1 Production + 1 Stage, 1 Development|For multi-tenant sites implementations.<br>In such cases, multiple sites with their own release schedule and dedicated development and content teams must be managed.|Two retail brands with dedicated websites and separate development teams|

>[!NOTE]
>
>Production programs [can be edited not be deleted.](editing-programs.md)
