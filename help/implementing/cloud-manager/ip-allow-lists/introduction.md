---
title: Introduction to IP Allow Lists
description: Learn how IP allow lists can limit from which addresses users can access your AEM as a Cloud Service domains.
exl-id: 352fae8e-d116-40b0-ba54-d7f001f076e8
---

# Introduction to IP Allow Lists {#introduction}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_ipallowlist"
>title="Manage IP Allow Lists"
>abstract="AEM as a cloud service is accessible via the internet and is secured through user authentication and authorization. Cloud Manager's IP allow lists can be used to limit and control access only to trusted IP addresses. Cloud Manager users with appropriate permissions can create allow lists of trusted IP addresses from which their site's users can access their AEM domains."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/ip-allow-lists/add-ip-allow-lists.html" text="Add an IP Allow List"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/ip-allow-lists/view-update-ip-allow-list.html" text="View & Update an IP Allow List"

AEM as a cloud service is by default accessible via the internet. While security is handled through user authentication and authorization, IP allow-listing is a way to limit access only to trusted IP addresses.

Cloud Manager's IP allow lists can be used to limit and control access only to such trusted IP addresses. Cloud Manager users with appropriate permissions can [create allow lists](/help/implementing/cloud-manager/ip-allow-lists/add-ip-allow-lists.md) of trusted IP addresses from which their site's users can access their AEM domains.

Once added, [IP allow lists can be applied/unapplied](/help/implementing/cloud-manager/ip-allow-lists/apply-allow-list.md) multiple times as a unit or entity to an author and/or publisher service in an environment.

>[!NOTE]
>
>If no IP allow list is applied, by default all IP addresses are allowed. As soon as an IP allow list is applied, no IP addresses are allowed except for those on the IP allow list.

## Limitations {#limitations}

There are a number of limitations to IP allows lists to keep in mind.

* A maximum of 50 IP allow lists can be added in your program
* A maximum of 50 IP/CIDR addresses can be added to each IP allow list.
* IP allow lists names are supported in Cloud Manager for author and/or publish service in an environment.
