---
title: Screens Notification Service in Screens as a Cloud Service
description: This page describes how to configure Notification Service in Screens as a Cloud Service.
index: true
exl-id: 74215a70-45c8-4b7f-ba30-60c332de07e9
feature: Developing Screens
role: Admin, Developer, User
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
---
# Screens Notification Service {#notification-service}

## Introduction {#introduction}

### Overview

AEM Screens Notifications Service allows administrators to receive a report with a list of all the AEM Screens players which did not ping for a configurable period of time on an email.

### How to configure

On AEM Screens Cloud, customers can request a report on device inactivity status by creating a support ticket with following information:

* Customer Name
* IMS OrgID
* Schedule Frequency: Specify a time or frequency in hours (for example, 1) at which this monitor should send emails.
* Ping Timeout: Specifies the interval in minutes after which a device should be considered not reachable.
* Email ID(s) : Email id(s) where the report will be sent

>[!NOTE]
>Emails will have the player reported only if the  device that has not pinged for the given ping timeout at the time of generating the email.

### Example Use Case

If you set the report time as 5 am and the ping timeout as 1 hour, then if your Screens device does not ping between 4:00 am - 5:00 am, you will receive an email notification confirming device inactivity.
