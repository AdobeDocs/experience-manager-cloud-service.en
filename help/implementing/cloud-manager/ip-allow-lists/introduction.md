---
title: Introduction to IP Allow Lists
description: Learn how IP allowlists can limit from which addresses users can access domains on AEM as a Cloud Service.
exl-id: 352fae8e-d116-40b0-ba54-d7f001f076e8
solution: Experience Manager
feature: "Cloud Manager, Developing"
role: "Admin, Architect, Developer"
---

# Introduction to IP Allow Lists {#introduction}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_ipallowlist"
>title="Manage IP allowlists"
>abstract="AEM as a cloud service is accessible by way of the internet and is secured through user authentication and authorization. Cloud Manager's IP allowlists can be used to limit and control access only to trusted IP addresses. Cloud Manager users with appropriate permissions can create allowlists of trusted IP addresses from which their site's users can access their AEM domains."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/ip-allow-lists/add-ip-allow-lists.html" text="Add an IP Allow List"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/ip-allow-lists/managing-ip-allow-lists.html" text="View & Update an IP Allow List"

AEM as a cloud service is by default accessible via the internet. While security is handled through user authentication and authorization, IP allow-listing is a way to limit access only to trusted IP addresses.

Cloud Manager's IP allowlists can be used to limit and control access only to such trusted IP addresses. Cloud Manager users with appropriate permissions can [create allowlists](/help/implementing/cloud-manager/ip-allow-lists/add-ip-allow-lists.md) of trusted IP addresses from which their site's users can access their AEM domains.

After adding, [IP allowlists can be applied/unapplied](/help/implementing/cloud-manager/ip-allow-lists/apply-allow-list.md) multiple times as a unit or entity to an author and/or publisher service in an environment.

>[!NOTE]
>
>If no IP allowlist is applied, by default all IP addresses are allowed. When an IP allowlist is applied, no IP addresses are allowed except for addresses on the IP allowlist.

## Limitations {#limitations}

There are several limitations to IP allowlists to keep in mind.

* A maximum of 50 IP allowlists can be added in your program
* A maximum of 50 IP/CIDR addresses can be added to each IP allowlist.
* IP allowlists names are supported in Cloud Manager for author, or publish service, or both, in an environment.
