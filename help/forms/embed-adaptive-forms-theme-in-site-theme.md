---
title: Embed an Adaptive Forms theme in an AEM Sites theme
description: Learn how to integrate an Adaptive Forms theme (for example, Canvas) into an AEM Sites theme so that Sites pages and embedded Adaptive Forms share one unified theme and deployment.
keywords: adaptive forms theme, site theme, AEM Sites theme, forms theme integration, front-end pipeline, theme embedding
feature: Adaptive Forms, Core Components, AEM Sites
role: Developer
exl-id: a1f8c4d2-3e5b-4a2f-9b7e-2d4f6a8c1b0e
---
# Embed an Adaptive Forms theme in an AEM Sites theme 

You can embed an Adaptive Forms theme (such as the [AEM Forms Canvas theme](https://github.com/adobe/aem-forms-theme-canvas)) into your AEM Sites theme. That way, a single theme drives both your site pages and any Adaptive Forms embedded on those pages, with one build and one deployment via the [AEM Front-End Pipeline](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines.html).

This article is for developers who maintain or customize the standard (or custom) AEM Sites theme and want to include Adaptive Form styling without managing a separate Forms theme deployment.

## Prerequisites {#prerequisites}

Before you start, ensure you have:

* **AEM as a Cloud Service** with the [Front-End Pipeline](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines.html) configured for your site theme.
* **Site theme sources** – for example, the [standard site template theme](https://github.com/adobe/aem-site-template-standard) (the repo that contains `theme/` with `src/theme.scss`, `src/components/`, and so on).
* **Forms theme sources** – the [AEM Forms Canvas theme](https://github.com/adobe/aem-forms-theme-canvas) (or another compatible Adaptive Forms theme) cloned or downloaded locally.
* **Node.js and npm** – to build the site theme (see theme README for supported versions).
* **Maven** – if you build the full site template package (optional for theme-only work).

## Step 1: Create the adaptive form components folder {#step-1-create-folder}

In your **site theme** repository, create the folder where the Forms theme will live:

```text
theme/src/components/adaptiveform/
```

All Forms theme assets will sit under this folder so they stay separate from existing site components.

## Step 2: Copy Forms theme components and images {#step-2-copy-components-and-images}

Using your **Forms theme** (for example, `aem-forms-theme-canvas`) and your **site theme** paths:

1. **Copy component folders**  
   From the Forms theme, copy the entire contents of `src/components/` into the site theme as:

   ```text
   theme/src/components/adaptiveform/
   ```

   So you get paths like:

   ```text
   theme/src/components/adaptiveform/button/
   theme/src/components/adaptiveform/checkbox/
   theme/src/components/adaptiveform/container/
   … (one folder per component)
   ```

2. **Copy images**  
   Copy the Forms theme images into the site theme:

   ```text
   Forms theme:  src/resources/images/*
   Site theme:   theme/src/components/adaptiveform/resources/images/
   ```

   Create `theme/src/components/adaptiveform/resources/images/` if it does not exist, then copy all image assets (for example `question.svg`, `Chevron-Left.svg`, `busy-state.gif`, and so on).

## Step 3: Copy variables and mixins {#step-3-copy-variables-and-mixins}

The Forms theme uses shared variables and mixins under `src/site/`. Copy only these two files into the **root** of `adaptiveform/` (not inside a `site` subfolder):

| Source (Forms theme)       | Destination (site theme)                          |
|---------------------------|---------------------------------------------------|
| `src/site/_variables.scss`| `theme/src/components/adaptiveform/_variables.scss`|
| `src/site/_mixin.scss`    | `theme/src/components/adaptiveform/_mixin.scss`    |

Do **not** copy the rest of the Forms theme’s `src/site/` folder; only these two files are required for the embedded form styles.

## Step 4: Fix image paths in SCSS {#step-4-fix-image-paths}

In the Forms theme, component SCSS files often reference images with paths like `./resources/` or `url(resources/`. After moving into `theme/src/components/adaptiveform/<component>/`, those paths must point up one level to `adaptiveform/resources/`.

**Find and replace** in every `.scss` under `theme/src/components/adaptiveform/`:

| Find | Replace with |
|------|------------------|
| `./resources/` | `../resources/` |
| `url(resources/` | `url(../resources/` |
| `url('resources/` | `url('../resources/` |

**Example** – before (Forms theme):

```scss
.cmp-adaptiveform-button__questionmark {
  background: url(./resources/images/question.svg) center center / cover no-repeat, #969696;
}
```

**After** (site theme):

```scss
.cmp-adaptiveform-button__questionmark {
  background: url(../resources/images/question.svg) center center / cover no-repeat, #969696;
}
```

Repeat for every SCSS file under `adaptiveform/` that references images (button, accordion, wizard, container, scribble, and others). A project-wide find/replace in your IDE over `theme/src/components/adaptiveform/` is recommended.

## Step 5: Create the adaptive form entry-point SCSS {#step-5-create-adaptiveform-scss}

Create **`theme/src/components/adaptiveform/_adaptiveform.scss`** in the site theme. This file must:

1. Import the shared variables and mixins.
2. Import each Adaptive Form component’s main SCSS file.

Use the following as the full entry point (matches the standard integration with all Core Components–based form components):

```scss
//== Adaptive Form components (forms theme integration)
// Variables and mixins for adaptive form components
@import 'variables';
@import 'mixin';

//== Core adaptive form components
@import './button/_button.scss';
@import './checkboxgroup/_checkboxgroup.scss';
@import './container/_container.scss';
@import './datepicker/_datepicker.scss';
@import './dropdown/_dropdown.scss';
@import './fileinput/_fileinput.scss';
@import './footer/_footer.scss';
@import './image/_image.scss';
@import './numberinput/_numberinput.scss';
@import './panelcontainer/_panelcontainer.scss';
@import './radiobutton/_radiobutton.scss';
@import './text/_text.scss';
@import './textinput/_textinput.scss';
@import './accordion/_accordion.scss';
@import './tabsontop/_tabsontop.scss';
@import './pageheader/_pageheader.scss';
@import './wizard/_wizard.scss';
@import './title/_title.scss';
@import './telephoneinput/_telephoneinput.scss';
@import './emailinput/_emailinput.scss';
@import './recaptcha/_recaptcha.scss';
@import './verticaltabs/_verticaltabs.scss';
@import './checkbox/_checkbox.scss';
@import './termsandconditions/_termsandconditions.scss';
@import './switch/_switch.scss';
@import './hcaptcha/_hcaptcha.scss';
@import './turnstile/_turnstile.scss';
@import './review/_review.scss';
@import './scribble/_scribble.scss';
@import './datetime/_datetime.scss';
```

If your Forms theme omits some components (for example, no scribble or captcha), remove or comment out the corresponding `@import` lines to avoid build errors. The list above matches the [Canvas theme](https://github.com/adobe/aem-forms-theme-canvas) structure.

## Step 6: Import the adaptive form theme in the site theme {#step-6-import-in-theme-scss}

In **`theme/src/theme.scss`**, add a single import at the **end** of the file (after other component imports):

```scss
//== Adaptive Form components (forms theme)
@import './components/adaptiveform/_adaptiveform.scss';
```

**Example** – end of `theme.scss`:

```scss
// ... existing site component imports ...
@import './components/embed/_embed.scss';
@import './components/pdfviewer/_pdfviewer.scss';
@import './components/socialmediasharing/_social_media_sharing.scss';

//== Adaptive Form components (forms theme)
@import './components/adaptiveform/_adaptiveform.scss';
```

This is the only change required in the existing site theme structure; all form-specific code stays under `src/components/adaptiveform/`.

## Step 7: Build and verify {#step-7-build-and-verify}

1. **Build the site theme** from the theme root:

   ```bash
   cd theme
   npm install
   npm run build
   ```


2. **Preview locally**:

   ```bash
   npm run live
   ```

   >[!NOTE]
   >
   >* Run `npm run live` to start a local proxy with hot reload that pulls page content from your AEM instance.
   >* Verify that embedded form styles (buttons, fields, panels, wizard, icons) look correct on a Sites page with an embedded Adaptive Form **before** you commit and run the front-end pipeline—this avoids failed pipeline runs and keeps your Git history clean.
   >* Configure `.env` with your AEM URL and proxy port as described in the theme README.

3. **Deploy** via your existing [Front-End Pipeline](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines.html). After deployment, the same theme CSS will apply to both site and embedded Adaptive Forms.

## Troubleshooting {#troubleshooting}

| Issue | What to check |
|-------|-------------------------------|
| Build fails: "file not found" for an image | Put all form images in `theme/src/components/adaptiveform/resources/images/`. In every `.scss` under `adaptiveform/`, use `../resources/` (and `url(../resources/`) for image paths, not `./resources/`. |
| Build fails: "file not found" for `_variables.scss` or `_mixin.scss` | Copy both files from the Forms theme `src/site/` into `theme/src/components/adaptiveform/` (the adaptiveform root), not inside a `site` subfolder. |
| Build fails: "file not found" for a component (e.g. `_scribble.scss`) | Your Forms theme may not include that component. In `theme/src/components/adaptiveform/_adaptiveform.scss`, remove or comment out the `@import` line for that component. |
| Form renders but has no styles | Confirm the page uses the client library that includes the built theme CSS, and that `theme.scss` contains the `@import './components/adaptiveform/_adaptiveform.scss';` line and the theme was rebuilt and deployed. |
| Styles conflict between site and form components | Form component classes are namespaced (e.g. `cmp-adaptiveform-button`). If you see clashes, inspect whether custom site CSS overrides those classes and adjust specificity or order. |

## See also {#see-also}

* [Use themes to style Core Components–based Adaptive Forms](/help/forms/using-themes-in-core-components.md)
* [Develop with Front-End Pipelines](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines.html)