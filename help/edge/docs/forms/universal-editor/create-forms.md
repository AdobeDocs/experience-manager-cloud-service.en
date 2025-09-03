---
title: Create and Publish Adaptive Forms with Edge Delivery Services
description: Step-by-step instructions for creating, authoring, and publishing Adaptive Forms using Edge Delivery Services templates in AEM, with a focus on technical accuracy and clarity.
keywords: adaptive forms, edge delivery services, universal editor, form creation, AEM forms, form publishing
feature: Edge Delivery Services
role: User, Developer
level: Beginner
exl-id: 1eab3a3d-5726-4ff8-90b9-947026c17e22
---

# Create and Publish Adaptive Forms with Edge Delivery Services

This document provides step-by-step instructions for creating, configuring, and publishing Adaptive Forms using Edge Delivery Services templates in AEM. It covers the complete workflow from form creation to production deployment.

By the end of this guide, you will learn how to:

- Create forms using Edge Delivery Services templates
- Author forms using Universal Editor
- Configure and publish forms to Edge Delivery Services
- Access published forms and verify deployment



## Prerequisites

Ensure the following prerequisites are met before proceeding:


- **AEM Forms as a Cloud Service**: An active author instance with a Forms license.
- **GitHub Account**: Personal or organizational account for repository management.
- **Repository Setup**: Choose one of the following:
  - **New Project**: [Create a new AEM project with Adaptive Forms Block](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#create-a-new-aem-project-pre-configured-with-adaptive-forms-block). The repository is pre-configured for Edge Delivery Services.
  - **Existing Project**: [Add Adaptive Forms Block to an existing repository](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#add-adaptive-forms-block-to-your-existing-aem-project) and update the configuration.

- **AEM-GitHub Connection**: [Establish a connection](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#get-started-with-the-aem-forms-boilerplate-repository-template) between your AEM instance and GitHub repository.
- **Edge Delivery Services**: Ensure the repository is configured for automatic deployment.
- **Permissions**: Verify you have the necessary access rights for form creation and publishing.

- Confirm the GitHub repository contains the Adaptive Forms Block.



## Form Creation and Publishing Workflow

The process consists of three main phases:

- **Phase 1:** [Form Creation](#step-1-form-creation)
- **Phase 2:** [Form Authoring and Design](#step-2-form-authoring-and-design)
- **Phase 3:** [Configuration and Publishing](#step-3-configuration-and-publishing)

Each phase includes validation steps to confirm correct setup.


### Step 1: Form Creation

1. **Access Form Creation**
   - Log in to your AEM Forms as a Cloud Service author instance.
   - Navigate to **Adobe Experience Manager** > **Forms** > **Forms & Documents**.
   - Click **Create** > **Adaptive Forms**.

1. **Select Template**
   - In the **Source** tab, select an **Edge Delivery Services-based template**.
   - The **Create** button becomes enabled.

      ![Create EDS Forms](/help/edge/assets/create-eds-forms.png)

1. **Configure Options (Optional)**
   - **Data Source tab**: Select data integration if required.
   - **Submission tab**: Choose a submit action (can be configured later).
   - **Delivery tab**: Set publishing/unpublishing schedule.

1. **Complete Form Setup**
   - Click **Create** to open the Form Creation wizard.
   - Enter the following:
     - **Name**: Internal identifier (no spaces, use hyphens).
     - **Title**: Display name for your form.
     - **GitHub URL**: Repository URL (e.g., `https://github.com/your-org/your-repo`).

   ![Create Form Wizard](/help/edge/assets/create-form-wizard.png)

1. **Validation**
   - After clicking **Create**, verify:
     - The form opens in Universal Editor.
     - The GitHub URL is correctly linked.
     - The component palette is available.
     - The form canvas is visible.

   ![Universal Editor Interface](/help/edge/assets/author-form.png)

**Outcome:** The form is ready for authoring in the Universal Editor.

### Step 2: Form Authoring and Design


1. **Access Component Library**
   - Open the Content browser in Universal Editor.
   - Navigate to the **Adaptive Form** component in the content tree.

   ![Content Tree Navigation](/help/edge/assets/content-tree.png)

1. **Add Form Fields**
   - Click the **Add** icon to open the component library.
   - Select components from the **Adaptive Form Components** list.
   - Drag and drop components onto the form canvas.

   ![Add Components](/help/edge/assets/add-component.png)

1. **Design the Form**
   - Configure field properties in the properties panel.
   - Set validation rules and behaviors.
   - Adjust styling and layout as needed.

   ![Completed Registration Form](/help/edge/assets/contact-us.png)

#### Validation

- All required fields are present.
- Field properties are correctly configured.
- Layout is responsive and accessible.
- Validation rules function as expected.

#### Next Steps

- [Configure submit actions](/help/edge/docs/forms/universal-editor/submit-action.md) for data handling.
- [Universal Editor guide](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#author-forms-using-wysiwyg) for advanced features.

### Step 3: Configuration and Publishing

Configure Edge Delivery Services and publish your form.

**Configuration:** Automatic (no manual setup required).

- The GitHub repository connection and Edge Delivery Services configuration are created during form creation.
- Publishing endpoints are configured automatically.

**Verification:**

- Confirm the configuration appears in the form's settings.
- Ensure the GitHub URL is correctly linked.

![Automatic EDS Configuration](/help/edge/assets/aem-instance-eds-configuration.png)

#### Publishing the Form

1. In Universal Editor, click the **Publish** button (upper-right corner).
2. Confirm publishing success in the dialog.
3. Note the generated URLs for staged and live versions.

   ![Universal Editor Publish](/help/edge/assets/publish-form.png)

- [Publishing guide](/help/edge/docs/forms/universal-editor/publish-forms.md)

## Form URLs

Published forms are accessible via Edge Delivery Services URLs.

### URL Structure

- **Staged (Preview/Testing):**

  ```
  https://<branch>--<repo>--<owner>.aem.page/content/forms/af/<form_name>
  ```

- **Live (Production):**

  ```
  https://<branch>--<repo>--<owner>.aem.live/content/forms/af/<form_name>
  ```

#### URL Parameters

- `<branch>`: GitHub branch name (e.g., `main`, `develop`)
- `<repo>`: GitHub repository name (e.g., `my-forms-project`)
- `<owner>`: GitHub organization or username (e.g., `company-name`)
- `<form_name>`: Form identifier as defined in AEM (e.g., `contact-us`)

#### Example

Example for form `contact-us` in repository `forms-project` under organization `acme-corp`:

- **Staged:** `https://main--forms-project--acme-corp.aem.page/content/forms/af/contact-us`
- **Live:** `https://main--forms-project--acme-corp.aem.live/content/forms/af/contact-us`

#### Environment Differences

- **Staged (.page):** Latest changes for testing.
- **Live (.live):** Published content for production.

![URL Structure](/help/edge/docs/forms/universal-editor/assets/url-structure.svg)
*Edge Delivery Services form URL structure breakdown*

#### Visual Examples

**Edge Delivery Services Template:**

- Staged: ![Registration form staged version](/help/forms/assets/registration-form-staged-version.png)
- Live: ![Registration form live version](/help/forms/assets/registration-form-live-version.png)

## Troubleshooting 

Below are common issues and solutions for AEM Forms with Edge Delivery Services.

+++Form Not Loading

**Issue:** Form URL returns 404 or blank page.

**Resolution:**

- Remove `.html` extension from URLs.
- Verify the form is published.
- Check the GitHub repository for the Adaptive Forms Block.
- Ensure the form name matches the URL (case-sensitive).

+++

+++Configuration Issues

**Issue:** Edge Delivery Services configuration not working.

**Resolution:**

- Ensure GitHub URL is in `https://github.com/owner/repository` format.
- Use the correct branch name in configuration.
- Verify repository access (public or authenticated).
- Check `fstab.yaml` for correct GitHub details.

+++

+++Publishing Problems

**Issue:** Changes not appearing on the live site.

**Resolution:**

- Wait 2–3 minutes for CDN cache refresh.
- Confirm the publishing workflow completed.
- Test on staged (.page) environment first.
- Ensure the GitHub repository is updated.

+++

+++Universal Editor Issues

**Issue:** Cannot edit form or components not loading.

**Resolution:**

- Use a supported browser (Chrome, Firefox, Safari).
- Clear browser cache and cookies.
- Verify network connectivity.
- Confirm author permissions.

+++

+++Form Submission Errors

**Issue:** Form submissions not working.

**Resolution:**

- Configure the submit action in form properties.
- Test submission endpoints manually.
- Check CORS settings if embedding forms.
- Verify required fields are configured.

+++

+++Performance Issues

**Issue:** Slow form loading or poor performance.

**Resolution:**

- Optimize images.
- Remove unnecessary components.
- Leverage Edge Delivery Services CDN.
- Minimize custom JavaScript/CSS.

+++

+++Getting Help

If issues persist:

1. Check Adobe Experience Cloud service status.
2. Review [Edge Delivery Services documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/edge-delivery/overview.html).
3. Visit [Adobe Experience League Community](https://experienceleaguecommunities.adobe.com/).
4. Contact Adobe Customer Care.

+++

## Next Steps

After completing form creation and publishing, consider the following:

- [Configure Submit Actions](/help/edge/docs/forms/universal-editor/submit-action.md): Set up data handling and integrations.
- [Form Data Models](/help/edge/docs/forms/universal-editor/integrate-forms-with-data-source.md): Connect forms to backend data sources.
- [Edge Delivery Services Best Practices](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/edge-delivery/overview.html): Maximize performance.
- [Form Analytics](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/integrate/services/analytics.html): Track form performance and user behavior.

