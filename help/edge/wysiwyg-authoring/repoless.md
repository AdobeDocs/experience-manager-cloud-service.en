---
title: Reusing Code Across Sites
description: If you have many similar sites that mostly look and behave the same, but have different content, learn how you can share code across multiple sites in a repo-less model.
feature: Edge Delivery Services
role: Admin, Architect, Developer
---

# Reusing Code Across Sites {#repoless}

If you have many similar sites that mostly look and behave the same, but have different content, learn how you can share code across multiple sites in a repo-less model.

## One Codebase for Multiple Sites {#one-codebase}

By default, AEM is tightly bound to your code repository, which meets the majority of use cases. However you may have multiple sites that differ mostly in their content, but could leverage the same code base.

Rather than creating multiple GitHub repositories and running each site off a dedicated GitHub repository while keeping them in sync, AEM supports running multiple sites from the same codebase.

This simplified setup, which eliminates the need for code replication is also known as "repoless", because all but your first site don't need a GitHub repository of their own.

If your project requires the repoless flexibility of code reuse across sites, you can activate the feature.

