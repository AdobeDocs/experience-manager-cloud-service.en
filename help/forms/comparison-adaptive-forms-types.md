---
title: Adaptive Forms Core Components vs Edge Delivery Services Forms vs Foundation Components
description: Technical comparison of AEM Forms authoring approaches - Core Components, Edge Delivery Services Forms, and Foundation Components. Architecture, rendering, features, and use cases.
keywords: adaptive forms comparison, core components, foundation components, edge delivery services forms, AEM forms comparison, form builder comparison
role: Architect, Developer, Admin
level: Intermediate
feature: Adaptive Forms, Core Components, Edge Delivery Services
exl-id: adaptive-forms-comparison
---

# Adaptive Forms: Core Components vs Edge Delivery Services Forms vs Foundation Components

Adobe Experience Manager (AEM) Forms provides three distinct approaches for building data capture experiences: Adaptive Forms based on Core Components, Edge Delivery Services Forms, and Adaptive Forms based on Foundation Components. Each approach has a different architecture, rendering model, and target use case. This article provides a technical comparison to help solution architects, developers, and AEM customers select the appropriate approach for their requirements.

## Overview

All three form types serve the purpose of capturing user data and integrating with backend systems. However, they differ in their underlying architecture, where forms are rendered, how they are delivered, and what capabilities they support.

| Approach | Status | Primary Use Case |
|----------|--------|------------------|
| **Core Components** | Recommended for new forms | Modern, scalable forms requiring AEM authoring with flexible publishing options |
| **Edge Delivery Services Forms** | Recommended for performance-critical sites | High-performance forms delivered from the edge with rapid deployment |
| **Foundation Components** | Maintenance mode | Existing forms requiring legacy feature support |

## Adaptive Forms Based on Core Components

### Definition

Adaptive Forms Core Components are a set of 30 open-source, BEM-compliant components built on the foundation of Adobe Experience Manager WCM Core Components. They represent Adobe's recommended approach for creating new Adaptive Forms, providing modern architecture, improved performance, and automatic headless form generation.

### Architecture

Core Components use a standardized, modular component architecture:

- **Component Foundation**: Built on AEM WCM Core Components
- **Styling Methodology**: BEM (Block Element Modifier) CSS conventions
- **Content Storage**: JCR repository with structured content nodes
- **Rendering**: Server-side rendering in AEM with optional client-side headless rendering
- **Source**: Open-source (available on [GitHub](https://github.com/adobe/aem-core-forms-components))

### Rendering Model

Core Components support multiple rendering models:

1. **Server-Side Rendering (SSR)**: Forms render on the AEM server and deliver complete HTML to the browser
2. **Headless Rendering**: Forms expose JSON representations via APIs for client-side rendering in React, Angular, or other frameworks
3. **Hybrid Rendering**: Combination of server and client rendering for optimal performance

### Publishing Options

- AEM Publish instances
- Edge Delivery Services (when configured)
- Headless APIs for custom frontend applications

### Key Features

| Category | Capabilities |
|----------|-------------|
| **Components** | 30 standardized components including Text Box, Numeric Box, Date Picker, Drop-down, Checkbox Group, Radio Button, File Attachment, Wizard, Accordion, Horizontal/Vertical Tabs |
| **Form Models** | JSON Schema (v4 and 2020-12), Form Data Model (FDM), XDP/XFA templates (limited) |
| **Rules Engine** | Visual rule editor with conditional logic, validation, service invocation, custom functions |
| **Submit Actions** | REST endpoint, Email, AEM Workflow, SharePoint, OneDrive, Azure Blob Storage, Power Automate, Workfront Fusion, Form Data Model |
| **Pre-fill** | Form Data Model Prefill Service, custom prefill services |
| **CAPTCHA** | reCAPTCHA, hCaptcha, Turnstile |
| **Document of Record** | PDF generation with custom or OOTB templates |
| **Accessibility** | WCAG compliant, ARIA labels, keyboard navigation, screen reader support |
| **Localization** | Multi-language support via AEM translation workflow |
| **Versioning** | Content versioning inherited from AEM Sites |

### Prerequisites

- **AEM Forms as a Cloud Service**: Core Components enabled by default
- **AEM 6.5 Forms**: Requires enabling via AEM Archetype
- **User Permissions**: User must be in `forms-users` group
- **Template**: Adaptive Form (Core Component) template required
- **Theme**: Canvas theme (OOTB) or custom theme

### Limitations

- **JSON Schema Constraints**: Null type, union types (any), OneOf/AnyOf/AllOf/NOT constructs not supported
- **Component Gaps**: Adobe Sign Block, Scribble Signature, Chart, Image Choice not available (available in Foundation Components)
- **Custom Functions**: Generator functions, async/await, class methods not supported
- **Digital Signatures**: Not available natively (unlike Foundation Components)

### When to Use

**Recommended for:**

- New form development projects
- Organizations requiring modern, maintainable architecture
- Projects requiring flexible publishing (AEM + Edge Delivery + Headless)
- Custom frontend applications (React, Angular) via headless APIs
- Projects prioritizing performance and accessibility
- Omnichannel delivery requirements (web, mobile, kiosks)

**Not recommended for:**

- Forms requiring Adobe Sign integration (use Foundation Components)
- Simple forms where Edge Delivery Services performance is critical
- Existing Foundation Component-based forms (maintain in Foundation unless migrating)

## Edge Delivery Services Forms

### Definition

Edge Delivery Services (EDS) Forms are a composable set of services for creating and delivering forms through Adobe Experience Manager Edge Delivery Services. They enable rapid form development with exceptional performance through edge-based delivery, client-side rendering, and multiple authoring methods.

### Architecture

EDS Forms use a decoupled, edge-first architecture:

- **Content Sources**: Microsoft SharePoint, Google Drive (Document-Based), or Universal Editor (WYSIWYG)
- **Code Repository**: GitHub
- **Content Delivery**: Edge Delivery Services CDN
- **Rendering**: Client-side rendering using vanilla JavaScript
- **Form Block**: Adaptive Forms Block processes form definitions and generates HTML

### Rendering Model

EDS Forms use client-side rendering exclusively:

1. Form definition stored as JSON (converted from spreadsheet or authored in Universal Editor)
2. JSON fetched from edge: `https://<branch>--<repo>--<owner>.aem.live/<form>.json`
3. Adaptive Forms Block JavaScript processes JSON
4. HTML structure generated dynamically in the browser
5. CSS applied for styling

**HTML Structure Pattern:**

```html
<div class="{Type}-wrapper field-{Name} field-wrapper" data-required="{Required}">
   <label for="{FieldId}" class="field-label">Label</label>
   <input type="{Type}" id="{FieldId}" name="{Name}">
   <div class="field-description" id="{FieldId}-description">Help text</div>
</div>
```

### Authoring Methods

EDS Forms support two authoring approaches:

#### Universal Editor (WYSIWYG)

- Visual drag-and-drop interface
- Real-time preview with device simulation
- Advanced rule editor for conditional logic
- Form Data Model (FDM) integration
- AEM Workflows integration
- Custom component support
- Template-based creation

#### Document-Based Authoring

- Microsoft Excel or Google Sheets authoring
- Spreadsheet-based form definition
- Instant publishing (changes reflect immediately)
- Suitable for simple to moderate complexity forms

### Submission Options

**Forms Submission Service (FSS):**

- Submit to Google Sheets
- Submit to Microsoft Excel (OneDrive/SharePoint)
- Email notifications

**AEM Publish Submit Actions:**

- REST endpoint
- AEM mail services
- Form Data Model
- AEM Workflow
- SharePoint/OneDrive
- Azure Blob Storage
- Microsoft Power Automate
- Adobe Workfront Fusion
- Adobe Marketo Engage

### Key Features

| Category | Capabilities |
|----------|-------------|
| **Components** | All HTML5 input types, Checkbox groups, Radio groups, Dropdown, Panels, Repeatable sections, File attachment, Accordion, Wizard, Modal |
| **Validation** | Field-level validation (required, min/max, pattern), custom validation messages |
| **Rules** | Conditional visibility, value expressions, event-driven rules |
| **Integrations** | Adobe Sign, Salesforce, Microsoft Dynamics, A/B testing |
| **Security** | reCAPTCHA Enterprise, hCaptcha, CORS configuration |
| **Analytics** | Adobe Experience Platform Web SDK, form views and submission tracking |

### Prerequisites

**For Document-Based Authoring:**

- GitHub account
- Google Drive or Microsoft SharePoint account
- Node/npm for local development
- AEM project with Adaptive Forms Block configured
- Share folder with `forms@adobe.com` (edit permissions)

**For Universal Editor:**

- AEM Forms as a Cloud Service instance
- Edge Delivery Services project configured
- Required permissions for target destinations

**For AEM Publish Submission:**

- AEM Cloud Service instance URL configured
- OSGi Referrer Filter configuration
- CORS configuration for Edge Delivery site domains

### Limitations

**Document-Based Authoring:**

- Sheet naming restricted to `helix-default` and `shared-aem`
- Best suited for low-complexity forms
- Limited rules capabilities
- No AEM Workflows (without AEM Publish submission)
- No Form Data Model integration

**Universal Editor:**

- Static/dynamic imports not supported in custom functions
- Form fragments can only be edited standalone
- Form embedding functionality in development

**General:**

- `shared-aem` sheets should not contain PII (publicly accessible)
- Requires CORS configuration for cross-origin submissions
- OSGi Referrer Filter required for AEM Publish submissions

### When to Use

**Recommended for:**

- Performance-critical websites requiring high Lighthouse scores
- Sites already using Edge Delivery Services
- Rapid form development and deployment
- Simple to moderate complexity data capture
- Teams preferring spreadsheet-based authoring (Document-Based)
- Projects requiring fast time-to-market

**Not recommended for:**

- Forms requiring extensive server-side processing
- Deep integration with legacy systems lacking REST APIs
- Offline form requirements
- Organizations requiring specific JavaScript frameworks (React, Angular) with full control

## Adaptive Forms Based on Foundation Components

### Definition

Foundation Components represent the classic AEM Forms authoring approach. They are the original Adaptive Forms components that have been available in AEM Forms for many years. While still supported, Adobe recommends Foundation Components primarily for maintaining existing forms rather than creating new ones.

### Architecture

Foundation Components use traditional AEM architecture:

- **Content Model**: WCM `cq:Page` component with JCR content structure
- **Root Structure**: `guideContainer` (root) → `rootPanel` → `items` (form fields)
- **Rendering**: Server-side rendering with client-side JavaScript
- **SOM Expressions**: Scripting Object Model for referencing form objects

### Rendering Model

Foundation Components use server-side rendering:

1. Form content stored in JCR repository
2. AEM server processes form structure
3. Complete HTML rendered and sent to browser
4. Client-side JavaScript handles interactivity and validation

### Key Features

| Category | Capabilities |
|----------|-------------|
| **Components** | 40+ components including all Core Component equivalents plus: Adobe Sign Block, Chart, Scribble Signature, Image Choice, Summary Step, File Attachment Listing |
| **Form Models** | Form Data Model (FDM), XDP/XFA templates, XML Schema (XSD), JSON Schema |
| **Rules Engine** | Visual editor + code editor (for forms-power-users group) |
| **Digital Signatures** | Adobe Sign integration, Scribble Signature |
| **Submit Actions** | Multiple OOTB actions similar to Core Components |

### Components Exclusive to Foundation

The following components are **only available** in Foundation Components:

- Adobe Sign Block
- Chart
- File Attachment Listing
- Footnote Placeholder
- Image Choice
- Scribble Signature
- Summary Step
- Turnstile Captcha

### Prerequisites

- AEM Forms as a Cloud Service or AEM 6.5 Forms
- Adaptive Form template (Foundation)
- User in `forms-users` group

### Limitations

- **Publishing**: AEM-only (no Edge Delivery Services or Headless APIs)
- **Performance**: Standard performance (not optimized for Lighthouse scores)
- **Architecture**: Legacy architecture without BEM compliance
- **Open Source**: Not open-source
- **Future Development**: Maintenance mode; new features primarily added to Core Components

### When to Use

**Recommended for:**

- Maintaining existing Foundation-based forms
- Forms requiring Adobe Sign or Scribble Signature integration
- Workflows dependent on established Foundation features
- Projects with AEM-only publishing requirements
- Forms requiring Foundation-exclusive components (Chart, Image Choice)

**Not recommended for:**

- New form development (use Core Components)
- Projects requiring Edge Delivery Services publishing
- Headless form APIs
- Performance-critical implementations
- Projects prioritizing future-proof architecture

## Comparison Table

| Parameter | Core Components | Edge Delivery Services Forms | Foundation Components |
|-----------|-----------------|-----------------------------|-----------------------|
| **Status** | Recommended for new forms | Recommended for high-performance sites | Maintenance mode |
| **Architecture** | Modular, BEM-compliant | Edge-first, decoupled | Traditional WCM |
| **Rendering** | Server-side + Headless | Client-side only | Server-side |
| **Publishing** | AEM + Edge Delivery + Headless APIs | Edge Delivery Services only | AEM only |
| **Authoring** | AEM Forms Editor | Universal Editor or Spreadsheets | AEM Forms Editor |
| **Performance** | Good (improved over Foundation) | Excellent (high Lighthouse scores) | Standard |
| **Component Count** | 30 | 20+ (all HTML5 input types) | 40+ |
| **Open Source** | Yes (GitHub) | Yes | No |
| **Form Data Model** | ✅ | ✅ (Universal Editor only) | ✅ |
| **JSON Schema** | ✅ | Limited | ✅ |
| **XDP/XFA Support** | Limited | ❌ | ✅ |
| **XML Schema** | ❌ | ❌ | ✅ |
| **Rules Engine** | Advanced visual editor | Advanced (Universal Editor) / Limited (Document-Based) | Advanced visual + code editor |
| **Digital Signatures** | ❌ | ❌ | ✅ |
| **Adobe Sign** | ❌ | Via integration | ✅ (Native block) |
| **Document of Record** | ✅ | ✅ | ✅ |
| **CAPTCHA Options** | reCAPTCHA, hCaptcha | reCAPTCHA Enterprise, hCaptcha | reCAPTCHA, hCaptcha, Turnstile |
| **AEM Workflow** | ✅ | ✅ (via AEM Publish) | ✅ |
| **Headless APIs** | ✅ (automatic) | ❌ | ❌ |
| **Accessibility** | WCAG compliant | WCAG compliant | Basic |
| **Deployment Speed** | Pipeline-based | Instant (commit to live) | Pipeline-based |
| **Styling** | BEM CSS, Themes | CSS, Project-level themes | CSS, Themes |
| **Versioning** | ✅ (inherited from Sites) | Git-based | ✅ |
| **Localization** | AEM translation workflow | Manual / AEM Sites workflow | AEM translation workflow |

## Decision Matrix

| Requirement | Recommended Approach |
|-------------|---------------------|
| New form development | Core Components |
| Maintaining existing forms | Foundation Components (until migration) |
| Performance-critical (high Lighthouse scores) | Edge Delivery Services Forms |
| Headless / omnichannel delivery | Core Components |
| Adobe Sign integration | Foundation Components |
| Spreadsheet-based authoring | Edge Delivery Services (Document-Based) |
| Visual WYSIWYG authoring with edge delivery | Edge Delivery Services (Universal Editor) |
| Complex enterprise integrations | Core Components or Foundation Components |
| Rapid prototyping | Edge Delivery Services (Document-Based) |
| XFA/XDP template support | Foundation Components |
| Custom React/Angular frontend | Core Components (Headless APIs) |

## Migration Considerations

### Foundation Components to Core Components

- **Tool**: AEM Modernize Tools (Forms Conversion Utility)
- **Effort**: Moderate to high depending on form complexity
- **Considerations**:
  - Rules require manual recreation
  - Foundation-exclusive components (Adobe Sign Block, Scribble Signature, Chart) are deleted during migration
  - Translation settings not carried over
  - Custom functions require rewriting

### Traditional to Edge Delivery Services

- **Approach**: Rebuild forms using Universal Editor or Document-Based authoring
- **Effort**: High for complex forms, low for simple forms
- **Benefits**: Significant performance improvement, modern development experience

## Documentation Gaps and Ambiguities

The following areas have incomplete or ambiguous documentation:

1. **Core Components XDP/XFA Support**: Documentation indicates "limited" support but does not specify exact limitations
2. **Edge Delivery Services Form Embedding**: Marked as "Coming Soon" in documentation; current status unclear
3. **Foundation Components Future**: No explicit deprecation timeline; described as "maintenance mode"
4. **Headless API Coverage**: Exact feature parity between server-rendered and headless forms not documented
5. **Performance Benchmarks**: Specific Lighthouse score comparisons between approaches not provided

## Related Resources

- [Create an Adaptive Form (Core Components)](/help/forms/creating-adaptive-form-core-components.md)
- [Create an Adaptive Form (Foundation Components)](/help/forms/creating-adaptive-form.md)
- [Edge Delivery Services Forms Overview](/help/edge/docs/forms/overview.md)
- [Universal Editor Getting Started](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md)
- [Document-Based Authoring Tutorial](/help/edge/docs/forms/tutorial.md)
- [Migration Utility Tool](/help/forms/migration-utility-tool-for-af-core-components.md)
- [AEM Forms Core Components on GitHub](https://github.com/adobe/aem-core-forms-components)
