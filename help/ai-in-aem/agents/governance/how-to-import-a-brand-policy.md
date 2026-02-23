---
title: How to Import A Brand Policy
description: Use the Adobe Governance Agent to Import a Brand Policy
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
---

# How to Import a Brand Policy {#how-to-import-a-brand-policy}

## Overview {#overview}

A brand policy defines the rules, standards, and constraints that ensure all content produced or updated by Adobe Experience Manager remains consistent with a company's brand identity. This typically includes tone of voice, terminology, visual guidelines, and editorial rules.

The Governance Agent uses brand policies as a source of truth to analyze existing pages and guide content generation. Customers can provide their own original brand policies, which the Governance Agent automatically converts into AI-readable policy checks. These checks are then used to validate content and to provide the Production Agent with a reliable, enforceable framework to generate or update pages that remain aligned with the brand.

## What is a Brand Policy in the Governance Agent {#what-is-a-brand-policy-in-the-governance-agent}

In the context of the Governance Agent, a brand policy is a structured representation of your brand rules that can be understood and enforced by AI. Rather than requiring customers to rewrite their guidelines in a technical format, the Governance Agent accepts brand policies in their original form (for example, documents, guidelines, or rule descriptions).

Once imported, the policy is transformed into a set of AI policy checks that can:

* Analyze existing pages to detect brand inconsistencies
* Flag deviations from tone, terminology, or mandatory rules
* Provide clear guidance to downstream agents
* Ensure that generated or updated content remains brand-compliant by design

This approach allows teams to reuse their existing brand documentation while benefiting from automated governance and scalable content production.

## How Brand Policies are Used {#how-brand-policies-are-used}

After a brand policy is imported:

* The Governance Agent interprets and normalizes the policy into enforceable AI checks
* Pages can be analyzed against the policy to identify gaps or violations
* The Production Agent uses these checks as constraints when generating or updating content
* Brand compliance becomes consistent, repeatable, and auditable across sites and teams


## Import a Brand Policy {#import-a-brand-policy}

To import a brand into the Governance Agent:

1. Create a brand, by giving a name and a main domain