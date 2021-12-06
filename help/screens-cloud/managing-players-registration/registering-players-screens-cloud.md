---
title: Registering Players in Screens as a Cloud Service
description: This page describes how to register players in Screens as a Cloud Service.
exl-id: 1a0d6b22-71b1-4f3c-acaa-82d8d9c0f81a
---
# Registering Players in Screens as a Cloud Service {#registering-players-screens-cloud}

Once you have installed and configured players for Screens as a Cloud Service, you must register the players.

## Objective {#objective}

This document helps you understand registering players in Screens Services Provider. After reading you should be able to:

* understand how to register players
* how to complete the registration process from Screens Services Provider

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

   >[!IMPORTANT]
   >**Security Best Practices Recommendation while using Registration Code**
   >As a best practice, you can limit the registration code usage. If a registration code is compromised, but has a limit of 100 registrations, then the attacker can register only up to that number, but not more. You can always update the usage limit after the registration code is created and some of the customer's players have already been registered. If the customer observes unusual registration activity for a specific registration code, they can lower the limit in real-time while they investigate and can increase the number back if it was a false alarm, without impacting the already registered players.


## What's Next {#whats-next}

Now, that you have installed and configured the player to Cloud mode, you should continue your Screens as a Cloud Service journey by next reviewing the document, [Assigning Player to a Display in Screens as a Cloud Service](/help/screens-cloud/managing-players-registration/assigning-player-display.md) from Screens Services Provider.
