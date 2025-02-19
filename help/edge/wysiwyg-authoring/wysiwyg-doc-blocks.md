---
title: Blocks for WYSIWYG and Document-Based Authoring
description: Learn how you can create blocks that can be used for both WYSIWYG authoring and document-based authoring.
feature: Edge Delivery Services
role: User
exl-id: f039c70a-e1a0-4fcc-8f42-dfa0f8bb3764
---
# Blocks for WYSIWYG and Document-Based Authoring {#wysiwyg-and-doc-blocks}

Learn how you can create blocks that can be used for both WYSIWYG authoring and document-based authoring.

## Overview {#overview}

On certain projects, you may want to support both [WYSIWYG authoring using the Universal Editor](/help/edge/wysiwyg-authoring/authoring.md) as well as [document-based authoring](/help/edge/docs/authoring.md). To minimize development time and ensure the same site experience, you can create one set of blocks to support both use cases.

To do this, you must use the same content modeling approach for both your WYSIWYG authoring setup as well as your document-based authoring setup.

## Approach {#approach}

In WYSIWYG authoring in AEM, you [declare a model](/help/edge/wysiwyg-authoring/content-modeling.md) and provide naming conventions. Data is then rendered in table-like block structures using Edge Delivery in the same way as if the table would have been created manually using document-based authoring.

To achieve this, certain assumptions are made such as for a simple block like a teaser that all properties and groups of properties are rendered in 1..n rows with a single column each. For blocks that have 1..n items (such as carousel and cards) the items are appended after these rows with one row each and a column for each property/group of properties.

If you follow the same approach for document-based authoring you can reuse your WYSIWYG blocks.
