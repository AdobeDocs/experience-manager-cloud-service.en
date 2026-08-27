---

title: "Form builder: Choose your approach"
description: Compare form builders and find the right approach for creating adaptive forms. Whether you're a form creator needing templates or building complex forms, choose the best form builder for your needs.
keywords: form builder, AEM forms, form creator, create forms, form maker, adaptive forms, core components, foundation components, edge delivery services, build forms
feature: Adaptive Forms, Core Components, Edge Delivery Services
role: User, Developer, Admin
level: Beginner
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: choose-form-builder-guide

---

# Form builder: Choose your approach {#choose-your-form-builder}

Adobe Experience Manager (AEM) Forms provides three powerful form building approaches, each designed for different use cases, technical requirements, and publishing destinations. Whether you're a form creator looking for templates or a developer building complex forms, this guide helps you choose the right form builder for your project.

## Quick decision guide

Use this quick reference to identify the best form builder for your needs:

| **If you need...** | **Choose** |
|-------------------|------------|
| **Modern, scalable forms with latest features** | Core Components |
| **Lightning-fast forms for high-traffic websites** | Universal Editor |
| **Maintain existing forms or legacy integrations** | Foundation Components |
| **Visual drag-and-drop authoring** | Core Components or Universal Editor |
| **Spreadsheet-based form creation** | Document-Based Authoring |
| **Omnichannel delivery (web, mobile, kiosks)** | Core Components (with headless APIs) |
| **Custom frontend applications (React, Angular)** | Core Components (with headless APIs) |
| **Full control over form rendering** | Core Components (with headless APIs) |

## Understanding your form builder options

AEM Forms offers three main form building approaches, each designed for different types of form creators and use cases. Whether you need a simple form maker for quick tasks or advanced form builder capabilities for complex projects, there's an approach that fits your needs:

### Foundation component form builder

Foundation Components represent the classic AEM Forms authoring experience. While still supported, they're primarily recommended for maintaining existing forms rather than creating new ones.

**Key characteristics:**

- Traditional AEM authoring interface
- Proven stability for existing workflows
- Limited to AEM-only publishing
- Basic component library

### Core component form builder

Core Components provide the latest AEM Forms capabilities with improved performance, accessibility, and flexibility. This form builder is ideal for form creators who need professional results with modern features. It supports both AEM and Edge Delivery Services publishing, and automatically produces headless forms for API-driven delivery across multiple platforms.

**Key characteristics:**

- Modern, standardized components
- Enhanced performance and accessibility
- Flexible publishing options (AEM + Edge Delivery)
- Advanced customization capabilities
- Future-proof architecture
- Automatic headless form generation for omnichannel delivery

### Universal editor (Edge Delivery Services)

Universal Editor provides two powerful authoring approaches for Edge Delivery Services: WYSIWYG visual authoring and document-based authoring using spreadsheets. This form maker approach is perfect for users who want to create forms quickly with exceptional performance.

**Key characteristics:**

- Exceptional performance (high Lighthouse scores)
- Two authoring methods: WYSIWYG and document-based
- Optimized for Edge Delivery Services
- Exceptional performance and SEO
- Rapid development and deployment


## Detailed comparison

### Technical capabilities

| **Capability** | **Foundation** | **Core** | **Universal Editor** | **Document-Based** |
|----------------|----------------|----------|---------------------|-------------------|
| **Form complexity** | Basic | Advanced | Advanced | Simple to moderate |
| **Rules engine** | Advanced | Advanced | Advanced | Limited |
| **Custom components** | ✅ | ✅ | ✅ | ✅ |
| **Themes** | ✅ | ✅ | Project-level | Project-level |
| **Templates** | ✅ | ✅ | Initial content only |  |
| **Fragments** | ✅ | ✅ | ✅ | ✅ |
| **Localization** | ✅ | ✅ | Via AEM Sites | Manual/Functions |

### Integration and submission

| **Feature** | **Foundation** | **Core** | **Universal Editor** | **Document-Based** |
|-------------|----------------|----------|---------------------|-------------------|
| **Data models** | FDM, Custom | FDM, Custom | FDM, Custom | Custom |
| **Submit actions** | Multiple options | Multiple options | Multiple options | Spreadsheet only |
| **Pre-fill** | ✅ | ✅ | Via Wizard | ✅ |
| **CAPTCHA** | Multiple types | reCAPTCHA, hCaptcha | reCAPTCHA Enterprise | reCAPTCHA Enterprise |
| **Attachments** | ✅ | ✅ | ✅ | Early Access |
| **Digital signatures** | ✅ |  |  |  |

### Publishing and performance

| **Aspect** | **Foundation** | **Core** | **Universal Editor** | **Document-Based** |
|------------|----------------|----------|---------------------|-------------------|
| **Publishing** | AEM only | AEM + Edge Delivery + Headless APIs | Edge Delivery | Edge Delivery |
| **Performance** | Standard | Improved | High Lighthouse scores | High Lighthouse scores |
| **SEO optimization** | Basic | Good | Excellent | Excellent |
| **Mobile responsiveness** | Good | Excellent | Excellent | Excellent |

## Choosing the right builder

### Choose foundation components if:

- You're maintaining existing Foundation-based forms
- You need digital signature integration
- Your workflow depends on established Foundation features
- You're working within AEM-only publishing requirements

**Ideal for:** Form maintenance, legacy system integration, established workflows

### Choose core components if:

- You're building new, modern forms
- You need flexibility to publish on AEM or Edge Delivery Services
- You want the latest features
- You need advanced customization and theming
- Accessibility and performance are priorities
- You want future-proof technology

**Ideal for:** New projects, scalable solutions, modern web experiences

### Choose universal editor if:

- You need exceptional performance and SEO
- You're building for Edge Delivery Services sites
- You need complex forms with custom actions
- Integration with external systems is required

**Ideal for:** High-performance sites, Edge Delivery Services, visual authoring workflows

### Choose document-based authoring if:

- Business users prefer spreadsheet-based authoring
- You need rapid prototyping and deployment
- Forms are relatively simple (surveys, registrations, feedback)
- Data collection in spreadsheets meets your needs
- No advanced submission workflows required

**Ideal for:** Quick deployment, business user authoring, simple data collection


## Migration considerations

### From foundation to core components

- **Recommended approach:** Use the [migration utility tool](/help/forms/migration-utility-tool-for-af-core-components.md)
- **Benefits:** Modern features, better performance, dual publishing capability
- **Effort:** Moderate to high, depending on form complexity

### From traditional to universal editor

- **Approach:** Rebuild forms using WYSIWYG or Document-Based authoring in Universal Editor
- **Benefits:** Exceptional performance, modern development experience, high SEO scores
- **Effort:** High for complex forms, low for simple forms

## Getting started

Once you've chosen your form builder:

### Foundation components

1. [Create an Adaptive Form (Foundation Components)](/help/forms/creating-adaptive-form.md)
2. [Foundation Components authoring guide](/help/forms/introduction-forms-authoring.md)

### Core components

1. [Create an Adaptive Form (Core Components)](/help/forms/creating-adaptive-form-core-components.md)
2. [Core Components feature overview](/help/forms/adaptive-form-core-components-json-schema-form-model.md)

### Universal editor (Edge Delivery Services)

1. **WYSIWYG Authoring:** [Getting started with Universal Editor](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md)
2. **Document-Based Authoring:** [Build your first form with spreadsheets](/help/edge/docs/forms/tutorial.md)


## Need help deciding?

Still unsure which form builder to choose? Consider these factors:

- **Team expertise:** What's your team's technical skill level?
- **Project timeline:** How quickly do you need to deploy?
- **Performance requirements:** Are speed and SEO critical?
- **Future scalability:** Will you need to expand or modify forms frequently?
- **Publishing destination:** Where will your forms be published?

For personalized guidance, consult with your AEM Forms implementation team or Adobe support.

## Related articles

- [Detailed form authoring comparison](/help/edge/docs/forms/authoring-a-form.md)
- [AEM Forms Core Components overview](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html)
- [Edge Delivery Services for Forms overview](/help/edge/docs/forms/overview.md)
- [Headless Adaptive Forms with Core Components](https://experienceleague.adobe.com/en/docs/experience-manager-headless-adaptive-forms/using/tutorial/build-engaging-forms-using-core-components-and-headless-adaptive-forms-aem-forms-cloud-service)
