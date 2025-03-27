---
title: Link Checker
description: Learn how the Link Checker helps authors by validating links as they are added to content and what configuration options it offers.
feature: Operations
role: Admin
---

# Link Checker {#link-checker}

Learn how the Link Checker helps authors by validating links as they are added to content and what configuration options it offers.

## Overview {#overview}

Content authors should not have to concern themselves with validating every link that they include in their content.

The Link Checker runs automatically to assist content authors with their links including:

* Validating links as they are added to content
* Performing link transformations

The Link Checker has several [configuration options](#configuring) such as defining the validation internal, allowing certain links or link patters to be omitted from validation, and defining link rewriting rules.

The Link Checker validates both internal links and external links.

>[!NOTE]
>
>Because the Link Checker checks every content page’s links, the Link Checker can impact performance on large repositories. In such cases, you may need to [configure how often the Link Checker runs](#configuring) or [disable it.](#disabling)
