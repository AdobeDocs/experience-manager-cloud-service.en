---
title: Registering Players in Screens as a Cloud Service
description: This page describes how to register players in Screens as a Cloud Service.
hide: yes
hidefromtoc: yes
index: no
---

# Registering Players in Screens as a Cloud Service {#registering-players-screens-cloud}

Once you have installed and configured players for Screens as a Cloud Service, you must register the players.

## Objective {#objective}

This document helps you understand registering players in Screens Services Provider. After reading you should:

* Understand how to register players.
* Be able to manage your channels in an AEM Screens project, in terms of scope.

## Steps to Register a Screens Player {#register-players}

Once you have installed your player to Screens as a Cloud Service, you are ready to register your player from Screens Services Provider.

Follow the steps below to register your player:

1. Login to Screens Services Provider.

1. Navigate to **Registration Codes** under **Players management** from the left navigation panel and click on **Create code**. 

   >[!NOTE]
   >If no valid/unexpired codes exist, click create code and enter a name for the code and choose expiry settings as per your requirements.

   ![image](/help/screens-cloud/assets/player/register-player1.png)

1. Populate the following fields in **Create a registration code** dialog box:

   ![image](/help/screens-cloud/assets/player/register-player2.png)

   1. **Registration Code Name**: Name for your registration code
   1. **Registration Code Expiry**: Date of expiry for your registration code
   1. **Limit Usage**: Toggle the button to switch off the usage limit of your registration code. By default, the Limit Usage option is off by default. 
   1. **Usage Limit**: Choose the number for your usage limit

1. Click on **Create** to create the registration code. You will see your player with the registration code in the list.

   ![image](/help/screens-cloud/assets/player/register-player3.png)

1. Click on the value under the column **REGISTRATION CODE**  to copy the value to the clipboard.

1. Paste this value in the **Enter code** field in the **Player Registration** tab from the Admin UI of the AEM Screens player and click on **Register**.
 
   ![image](/help/screens-cloud/assets/player/register-player4.png)


1. Once you have added the code, you will see the player is now registered from the Admin UI of the player.

   ![image](/help/screens-cloud/assets/player/register-player5.png)

1. You should see this player now show up in **Players** from the left navigation panel. The code that displays in Screens Services Provider matches the **System Information** panel from the Admin UI under Player Code.

   ![image](/help/screens-cloud/assets/player/register-player6.png)

