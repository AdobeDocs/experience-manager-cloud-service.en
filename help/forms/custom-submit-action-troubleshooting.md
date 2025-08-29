---
title: Troubleshooting 502 Error in Custom Submit Action for Adaptive Forms
description: Learn how to identify and resolve 502 error pages that occur when using custom submit actions in Adaptive Forms (Core Components). This guide explains common causes, such as unhandled exceptions, and provides resolution steps.
feature: Adaptive Forms, Core Components
role: Developer
level: Intermediate
---

# Troubleshooting: 502 Error Page in Custom Submit Action  

When working with Adaptive Forms (Core Components), you may encounter a **502 error page HTML** after submitting a form that uses a custom submit action.  

## Issue  

**Error:** A 502 error page HTML is displayed when a custom submit action service fails.  

**Reason:** This happens if the custom submit action throws an unhandled error, for example, null pointer, invalid API response, or runtime failure. 

## Resolution  

To prevent the 502 error page, wrap submission logic with try-catch blocks to gracefully handle errors.  

For detailed steps, see [Create a custom submit action for Adaptive Forms (Core Components)](/help/forms/custom-submit-action-for-adaptive-forms-based-on-core-components.md).
