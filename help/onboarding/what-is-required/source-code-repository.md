---
title: Source Code Repository - Cloud Services
seo-title: Source Code Repository - Cloud Services
description: Source Code Repository - Cloud Services
seo-description: Source Code Repository - Cloud Services 
---

# Source Code Repository {#source-code-repository} 

In order for a user to access the Cloud Manager git repository, they will need to use a Git client. 
This could be a command-line tool, a standalone visual Git client, or the user's IDE such as Eclipse, IntelliJ, NetBeans.

Once a Git client is set up, the user can select the **Manage Git** button to get the information necessary to access Cloud Manager Git repository.

The important considerations to manage your git in Cloud Manager are:

* The repository URL is the value in the **URL** field
* The user name is the value in the **Username** field
* The password is the value in the **Password** field shown when the **Generate Password** button is pressed.

To begin developing the AEM Cloud application, a local copy of the application code must be made by checking it out from the Cloud Manager repository to a location on their local computer where they wish to create their repository.
```
java
$ git clone {URL}
```
> Note:
> A user can check out a copy of their code, and make changes in the local code repository. When ready, the user can commit their code changes back to the remote code repository in Cloud Manager.