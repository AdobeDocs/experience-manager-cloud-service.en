---
title: Content Hub frequently asked questions (FAQs)
description: Get responses to some of the most frequently asked questions (FAQs) for Content Hub.
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 74b5c308-c1d3-4787-9f1f-f64cf09d298a
---
# [!DNL Content Hub] frequently asked questions {#content-hub-frequently-asked-questions}

This page answers the most common questions about [!DNL Content Hub], a centralized workspace for storing, organizing, and reusing digital content across teams and channels. The answers below provide general guidance to help new and experienced users get the most out of the platform.

## What is [!DNL Content Hub]?

**What is [!DNL Content Hub]?**
[!DNL Content Hub] is a centralized repository that stores, organizes, and manages digital assets and content in one place. It serves as a single source of truth so teams can locate approved content, maintain consistency, and reuse materials across multiple projects and channels.

**Why use a [!DNL Content Hub]?**
A [!DNL Content Hub] streamlines content operations and reduces duplicated work. Key benefits include:

- **Centralized access** — all approved content lives in one location, eliminating scattered files and version confusion.
- **Faster reuse** — teams find and repurpose existing assets instead of recreating them.
- **Consistency** — shared, governed content keeps branding and messaging aligned across teams.
- **Improved collaboration** — multiple contributors can work from the same trusted set of materials.

## Getting started

**How do I get started with [!DNL Content Hub]?**
Getting started generally follows a straightforward sequence:

1. Sign in with your account credentials.
2. Locate the [!DNL Content Hub] workspace from the main navigation.
3. Browse existing content or create a new item to add your first asset.
4. Apply relevant tags, categories, or metadata so the content remains easy to find.

![Content Hub frequently asked question](assets/content-hub-faqs.png)

**Who can access [!DNL Content Hub]?**
Access typically depends on the roles and permissions assigned to each user. Administrators grant access levels that determine whether a user can view, edit, publish, or manage content, ensuring the right people work with the right materials.

## Managing and organizing content

**How do I organize content effectively?**
Effective organization relies on consistent structure and metadata. Recommended practices include:

- Applying descriptive tags and categories to every asset.
- Using clear, standardized naming conventions.
- Grouping related items into logical collections or folders.
- Reviewing and archiving outdated content on a regular basis.

Consistent metadata matters because it powers search and filtering, making content faster to retrieve as the library grows.

**Can I edit or update existing content?**
Yes. Users with the appropriate permissions can update existing content, and versioning helps preserve a record of changes so teams can track revisions and, where supported, revert to earlier versions if needed.

## Sharing and collaboration

**How do I share content with my team?**
Content is shared by granting access, distributing a link, or publishing the item to a designated destination. Because assets are centralized, collaborators work from the same approved source rather than passing files back and forth, which reduces version conflicts.

**Can multiple people work in [!DNL Content Hub] at the same time?**
Yes. [!DNL Content Hub] is designed for team collaboration, allowing multiple contributors to access, organize, and work with content simultaneously while permissions govern what each person can change.

## Troubleshooting

**What should I do if I cannot find my content?**
If content does not appear, try the following steps:

1. Confirm you are signed in with the correct account.
2. Check that your permissions include access to the relevant workspace or collection.
3. Search using tags, keywords, or the asset name rather than browsing manually.
4. Verify the content has not been archived, moved, or restricted by an administrator.

**What if I do not have the permissions I need?**
Permission levels are managed by administrators. If you require additional access to view, edit, or publish content, contact your administrator to have your role updated.

For questions not covered here, consult your organization's [!DNL Content Hub] administrator or the platform's help resources for guidance specific to your configuration.

## What is AEM [!DNL Assets] [!DNL Content Hub]? {#what-is-content-hub}

**AEM [!DNL Assets] [!DNL Content Hub]** is a feature of **Adobe Experience Manager (AEM) [!DNL Assets] as a Cloud Service**. It provides an intuitive, cloud-based portal where cross-functional teams across marketing, sales, and partner organizations can discover, access, and adapt approved brand assets on demand. As a native capability of AEM [!DNL Assets], [!DNL Content Hub] extends the reach of the central **Digital Asset Management (DAM)** system beyond specialized creative teams to the wider organization.

### Key Capabilities

[!DNL Content Hub] delivers two core functions that streamline how organizations distribute and grow their content libraries:

- **Asset discovery and self-service access:** [!DNL Content Hub] enables cross-functional teams to easily discover relevant, approved assets through an intuitive portal and quickly adapt them to their needs. This removes bottlenecks that occur when non-creative users must request files from a central team.
- **Self-serve ingestion:** [!DNL Content Hub] provides an ingestion mechanism that allows users to easily upload assets into the Digital Asset Management (DAM) repository themselves. This distributes the work of populating the DAM across many contributors rather than concentrating it in a single team.

### Business Benefits

[!DNL Content Hub] directly accommodates the need organizations have for higher content creation velocity. By empowering broader teams to both find existing assets and contribute new ones, organizations produce and reuse content faster while reducing dependence on central creative resources.

At the same time, [!DNL Content Hub] preserves brand consistency and compliance through appropriate safeguards. Because only approved assets are surfaced in the portal and ingestion flows can be governed by defined controls, users self-serve without compromising brand standards. This balance means faster content production does not come at the expense of governance, ensuring teams work quickly while staying on-brand and compliant.

<!--

## Why cannot I enable Content Hub on my Cloud Manager program/environment? {#cannot-enable-content-hub}

Content Hub is at this point is only available on AEM Cloud Manager Production programs, which include an Assets license (Assets Cloud Service, Assets Ultimate, Assets Prime). When you click [Content Hub](/help/assets/deploy-content-hub.md#enable-content-hub) to enable it, it is deployed and associated with the author production environment of AEM in that program. See [Deploy Content Hub](/help/assets/deploy-content-hub.md) for details and prerequisites.

-->

## I enabled AEM [!DNL Assets] [!DNL Content Hub] on my production program/environment, can I disable it? {#can-i-disable-content-hub}

**No. Once enabled on a production program, AEM [!DNL Assets] [!DNL Content Hub] cannot be disabled or removed.** Enabling Adobe Experience Manager (AEM) [!DNL Assets] [!DNL Content Hub] on a production program **deploys it as a permanent part of your production infrastructure**. Because AEM Cloud Manager does not allow the removal or disabling of production infrastructure, there is no supported path to reverse the deployment. This restriction exists **specifically to minimize the risk of accidental disruption to production usage caused by human error**.

### How to withhold [!DNL Content Hub] access after deployment

If you do not want to provide [!DNL Content Hub] to your end users after it has been deployed, you can effectively prevent access through user assignment controls in the [!DNL Adobe Admin Console]:

1. Open the **Admin Console**.
2. Locate the **[!DNL Content Hub] product profile**.
3. Do not assign any users to the [!DNL Content Hub] product profile.

Leaving the product profile unassigned means no users receive access, achieving the practical outcome of [!DNL Content Hub] being unavailable to your organization even though the underlying infrastructure remains deployed.

For step-by-step deployment and product profile details, see [Deploy [!DNL Content Hub]](/help/assets/deploy-content-hub.md#content-hub-instance-product-profile).

## How can I evaluate AEM [!DNL Assets] [!DNL Content Hub] in my organization? {#how-can-i-evaluate-content-hub}

**AEM [!DNL Assets] [!DNL Content Hub] is an Adobe-provided and Adobe-maintained feature that contains no custom code**, so it does not require the typical validation through dev/stage/production environments. Access to the feature is **fully controlled by the administrator**. Because access is administrator-controlled, administrators can evaluate the feature without exposing it to all users, and the evaluation does not impact end users or production content managed in **AEM as a Cloud Service [!DNL Assets]**.

The recommended evaluation procedure follows these steps:

1. [Enable [!DNL Content Hub]](/help/assets/deploy-content-hub.md#enable-content-hub) on the **production environment** (Cloud Manager program).
2. [Add an AEM Administrator user](/help/assets/deploy-content-hub.md#onboard-content-hub-administrator) from the production author to the [!DNL Content Hub] product profile.
3. The **AEM Administrator** [configures [!DNL Content Hub]](/help/assets/configure-content-hub-ui-options.md).
4. The **AEM Administrator** or an AEM User on the AEM production author [approves a number of assets for [!DNL Content Hub]](/help/assets/approve-assets-content-hub.md). To avoid changing any production content in **DAM**, create a separate evaluation folder in the AEM author instance, then upload, tag, or copy some assets from DAM into it. This ensures the evaluation stays isolated from live production assets.
5. The **Admin Console administrator** adds [a few selected users](/help/assets/deploy-content-hub.md#onboard-content-hub-users) to the [!DNL Content Hub] product profile so that they can begin the evaluation.
6. After the evaluation is completed, AEM Users in the author instance can remove approval from the test assets and approve production assets for [!DNL Content Hub]. The **Admin Console administrator** then adds all users who need access to [!DNL Content Hub] and the approved content. At this point, your [!DNL Content Hub] is live and available to all authorized users.

An **early access program** for [!DNL Content Hub] is available on **Sandbox programs** and their author production environments. For more information, see [Introduction to Sandbox Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/introduction-sandbox-programs.md). To learn more about the early access program, reach out to your Adobe account team.

## Why do not I see any assets after logging on to AEM [!DNL Assets] [!DNL Content Hub]? {#no-assets-in-content-hub}

If no assets appear after you log on to **[!DNL Content Hub]**, it means those assets have not yet been **approved** in **[!DNL Assets] as a Cloud Service**. Only assets explicitly marked as **approved** in **[!DNL Assets] as a Cloud Service** are automatically made available in [!DNL Content Hub]. As a result, an empty [!DNL Content Hub] view almost always indicates a pending or missing approval step rather than a synchronization failure.

### Cause

[!DNL Content Hub] displays only approved content. Approval acts as the gating mechanism that controls availability, ensuring that end users and downstream teams access only vetted, publish-ready assets. When assets remain unapproved, they stay hidden from [!DNL Content Hub] even though they exist in **[!DNL Assets] as a Cloud Service**.

### Resolution

To make your assets visible in [!DNL Content Hub], complete the following steps:

1. Sign in to the **Adobe Experience Manager (AEM) as a Cloud Service** author environment.
2. Locate the assets you want to surface in [!DNL Content Hub].
3. Mark the selected assets as **approved**.

Once approved, the assets become automatically available in [!DNL Content Hub], so logging back on displays them without additional configuration. For more information, see [Approve assets for [!DNL Content Hub]](/help/assets/approve-assets-content-hub.md).

## Why do not I see my assets that I either upload directly using AEM [!DNL Assets] [!DNL Content Hub] or import them from Dropbox or OneDrive accounts using [!DNL Content Hub]? {#no-assets-uploaded-from-content-hub}

[!DNL Assets] that you upload directly or import from Dropbox or OneDrive accounts through **AEM [!DNL Assets] [!DNL Content Hub]** display only after they pass an approval step. The single factor that determines whether these assets appear is the [**Auto-approval**](/help/assets/configure-content-hub-ui-options.md#configure-import-options-content-hub) toggle on the Configuration user interface. This behavior occurs because the **Auto-approval** setting acts as a moderation gate, controlling whether newly ingested assets become visible immediately or must first be reviewed and approved.

The outcome depends on the state of the **Auto-approval** toggle:

### When Auto-approval is enabled

* If the **Auto-approval** toggle is enabled, assets that you upload or import using [!DNL Content Hub] become **automatically available** for display without any further action.

### When Auto-approval is disabled

* If the **Auto-approval** toggle is disabled, the assets do not display automatically. Instead, they are held in the **`hydrated-assets`** folder of your [!DNL Assets] as a Cloud Service environment. This folder serves as a staging area for assets that are pending approval.
* To make these pending assets visible, navigate to the **`hydrated-assets`** folder and [bulk edit](/help/assets/approve-assets-content-hub.md) their status to **`Approved`**. Once approved, the assets display in [!DNL Content Hub].

## How to quickly find assets uploaded using AEM [!DNL Assets] [!DNL Content Hub] on AEM as a Cloud Service environment? {#find-uploaded-assets-on-aem-cloud}

Locate assets uploaded through AEM [!DNL Assets] [!DNL Content Hub] on AEM as a Cloud Service quickly by following these three steps. Uploaded assets are stored in a dedicated folder, so the process centers on navigating to that folder and filtering the results by status and modification date:

1. Navigate to the **`hydrated-assets`** folder. [!DNL Assets] uploaded through AEM [!DNL Assets] [!DNL Content Hub] are placed in this folder, so it is the correct starting point for locating recent uploads.

2. Click **[!UICONTROL Filters]** and set **[!UICONTROL No Status]** in the **[!UICONTROL Asset Status]** field. Newly uploaded assets have not yet been assigned a status, so filtering by **[!UICONTROL No Status]** isolates them from assets already in review or approved workflows.

3. Sort assets using the **[!UICONTROL Modified Date]** field. Sorting by **[!UICONTROL Modified Date]** surfaces the most recently added or changed assets first, making the latest uploads immediately visible at the top of the list.

## Why do not I see the Edit using [!DNL Adobe Express] option on my asset card to be able to remix assets to create new variations using AEM [!DNL Assets] [!DNL Content Hub]? {#edit-using-express-not-available}

The **Edit using [!DNL Adobe Express]** option appears on the asset card in AEM [!DNL Assets] [!DNL Content Hub] only when specific entitlement and permission requirements are met. If either is missing, the option is hidden, which is the most common reason it does not display. To view the **Edit using [!DNL Adobe Express]** option on the asset card in AEM [!DNL Assets] [!DNL Content Hub], the user must have **[!DNL Adobe Express] Enterprise or Teams entitlement** (see [plans](https://www.adobe.com/express/pricing)) in addition to privileges for [Content Hub users with rights to remix assets to new variations](#onboard-content-hub-users-add-assets).

There are a few configurations of how users are assigned to [!DNL Content Hub] & [!DNL Adobe Express]:

1. **Bundled entitlement (no extra setup):** The organization has [Assets Ultimate](/help/assets/assets-ultimate-overview.md) or [Assets Prime](/help/assets/assets-prime.md) license, and the user is assigned to one of the Experience Manager profiles in Admin console that include **[!DNL Adobe Express] entitlement (Collaborator or Power user)**. The integration works without any additional configuration.

1. **Same Admin Console deployment (no extra setup):** [!DNL Adobe Express] is deployed in the same [!DNL Adobe Admin Console] as [!DNL Experience Manager Assets] with [!DNL Content Hub]. The integration works without any additional configuration.

1. **Separate Admin Console deployment (configuration required):** [!DNL Adobe Express] is deployed in a different [!DNL Adobe Admin Console] than [!DNL Experience Manager Assets] with [!DNL Content Hub]. In this case, the [!DNL Assets] administrator can configure the integration (see [documentation](/help/assets/connect-assets-with-creative-cloud.md)) so that the two separately deployed products recognize the same user and the integration works.

   >[!NOTE]
   >
   >The user assigned to Express and [!DNL Assets] product profiles in two Admin Consoles needs to have the **same email address** and use a business **Enterprise or School** account, and not the **Personal** one. This alignment is required because the integration matches the user across both consoles by identity. The ideal configuration is to have both Admin Consoles set up as **Federated ID** with a trust relationship set up between them, so that the user has a seamless single sign-on experience. Some of the Express plans (for example, Express Teams) does not support Federated ID / single sign-on.

Beyond the right product entitlements, [!DNL Adobe Express] integration in [!DNL Content Hub] requires that the assigned user has at least **[!UICONTROL Can Edit]** permissions on the [!DNL Assets] author environment powering [!DNL Content Hub], on at least the **[#UICONTROL /content/dam/hydrated-assets/]** folder hierarchy. This folder is where [!DNL Content Hub] users save content that they created using Express, so **[!UICONTROL Can Edit]** access on it is essential for the remix workflow to complete successfully. See [Permissions Management](/help/security/touch-ui-principal-view.md) in the Admin view (Touch UI) or a simplified [permissions management in [!DNL Assets] view](https://experienceleague.adobe.com/en/docs/experience-manager-assets-essentials/help/get-started-admins/folder-access/manage-permissions).

## Can I setup AEM [!DNL Assets] [!DNL Content Hub] so that my organization's brand guidelines display as a link on the home page? {#content-hub-setup-brand-guidelines}

Yes. **Adobe Experience Manager (AEM) [!DNL Assets] [!DNL Content Hub]** supports adding **custom links** as separate tabs on the home page, alongside the standard **All [!DNL Assets]**, **Collections**, and **Insights** tabs. This lets you surface your organization's brand guidelines as a dedicated, always-visible tab, giving users one-click access to those guidelines directly from the [!DNL Content Hub] home page rather than requiring them to navigate elsewhere.

To configure a custom link for your organization's brand guidelines, see [Custom Links](/help/assets/configure-content-hub-ui-options.md#configure-custom-links-content-hub).

## Is there any plan on migrating existing Brand Portal customers to AEM [!DNL Assets] [!DNL Content Hub]? {#migration-brand-portal}

Yes. Adobe provides **migration support** for existing **Brand Portal** customers moving to **Adobe Experience Manager (AEM) [!DNL Assets] [!DNL Content Hub]**. This migration path is officially supported, and existing Brand Portal customers can initiate it directly through Adobe's support channels.

To begin the migration from Brand Portal to AEM [!DNL Assets] [!DNL Content Hub]:

1. **Create an Adobe support ticket** requesting migration from Brand Portal to AEM [!DNL Assets] [!DNL Content Hub].
2. **Work with Adobe support** to plan and execute the transition of your assets and configuration.

Creating the support ticket initiates the migration process, allowing Adobe to coordinate the transfer of brand assets and related content into AEM [!DNL Assets] [!DNL Content Hub]. Because [!DNL Content Hub] is designed as the successor experience for distributing approved brand assets, this supported migration path ensures that existing Brand Portal customers can transition without losing access to their managed content.

## Why cannot I see the Product Settings/Configuration option in AEM [!DNL Assets] [!DNL Content Hub]? {#ui-configuration-option-missing}

Accessing the [Configuration User Interface](/help/assets/configure-content-hub-ui-options.md) in AEM [!DNL Assets] [!DNL Content Hub] **requires the user to be a [Content Hub Administrator](/help/assets/deploy-content-hub.md##onboard-content-hub-administrator)**. This administrator-level role is mandatory: without it, the Product Settings/Configuration option does not appear in the [!DNL Content Hub] interface.

If the configuration option is still missing after the correct role assignment, the most common cause is a **renamed AEM Administrators product profile**. AEM matches users to their permissions by the exact product profile name, so any change to that name breaks the mapping and hides the configuration controls.

**Troubleshooting steps to restore the missing configuration option:**

1. **Confirm the required role.** Verify that the user is assigned as a **[!DNL Content Hub] Administrator**, which is the prerequisite for accessing the [Configuration User Interface](/help/assets/configure-content-hub-ui-options.md).
2. **Check the product profile assignment.** If the user is assigned to the **AEM Administrators product profile** on the production author instance in [!DNL Adobe Admin Console] and still cannot see the configuration option, proceed to the next step.
3. **Verify the profile name.** Ensure that the **AEM Administrators product profile is not renamed**. A renamed profile prevents AEM from matching the user to the required administrative permissions, because AEM relies on the exact, default profile name to grant access.

For full details on how profiles map to team permissions, see [AEM as a Cloud Service Team and Product Profiles](/help/onboarding/aem-cs-team-product-profiles.md).

## How AEM [!DNL Assets] [!DNL Content Hub] addresses the limitations of Brand Portal? {#content-hub-brand-portal-comparison}

Adobe Experience Manager (AEM) [!DNL Assets] [!DNL Content Hub] addresses the limitations of Brand Portal by extending distribution, configurability, search, and governance capabilities well beyond what Brand Portal offers. While both solutions distribute approved brand assets from a central Digital Asset Management (DAM) repository, [!DNL Content Hub] delivers a broader set of self-service, branding, and administrative controls. As a result, [!DNL Content Hub] is positioned as the more configurable and extensible distribution experience for teams that need dynamic search, automated synchronization, and richer branding control.

### Key Capabilities Where [!DNL Content Hub] Exceeds Brand Portal

[!DNL Content Hub] introduces several capabilities that Brand Portal does not support, giving administrators and end users significantly greater flexibility:

- **Deeper distribution configuration** — [!DNL Content Hub] lets administrators configure metadata for filters, asset details, and the add-assets page, configure external links from the portal, and set **primary and secondary colors for the user interface (UI)** to match branding requirements. Because these controls are absent in Brand Portal, teams gain more control over both look and function.
- **Automatic asset synchronization** — With [!DNL Content Hub], **approved asset changes are synced automatically** from the DAM, ensuring distributed assets stay current without manual intervention.
- **Dynamic search and filtering** — [!DNL Content Hub] provides **dynamic filters** whose options appear based on the assets currently displayed, along with **search history**, both of which Brand Portal lacks. This makes locating the right asset faster.
- **Richer upload options** — [!DNL Content Hub] allows users to **add configurable metadata while uploading assets**, improving downstream discoverability.
- **Expired-asset governance** — [!DNL Content Hub] can **restrict view and download of expired assets**, reducing the risk of publishing outdated content.
- **Search within collections** — [!DNL Content Hub] supports searching directly within collections, streamlining large-collection navigation.
- **Attribute-based access control** — [!DNL Content Hub] uses **attribute-based access control**, enabling fine-grained, policy-driven permissions.
- **[!DNL Adobe Express] integration** — Users can **edit [!DNL Content Hub] assets in [!DNL Adobe Express] and save back to the DAM**, closing the loop between creation and distribution.
- **Insights dashboard** — [!DNL Content Hub] includes an **Insights dashboard** for reporting on distribution activity.
- **Custom UI extensibility** — [!DNL Content Hub] offers **custom extension points on the asset details page** (limited availability), enabling tailored experiences.

In addition, [!DNL Content Hub] has several **innovations coming soon**, including favourite collections by user, pinned collections by admin, semantic search, and localised search and metadata display — none of which are available in Brand Portal.

### Where Brand Portal Retains a Distinct Capability

Brand Portal continues to support **Access Control List (ACL)-based permissions**, a capability not offered by [!DNL Content Hub], which instead relies on attribute-based access control. Teams whose governance model depends specifically on ACL-based permissions should account for this distinction when comparing the two solutions.

### Capabilities Supported by Both

Both [!DNL Content Hub] and Brand Portal share a common baseline of distribution features, including banner messaging, banner image branding, sharing original approved assets from the DAM, local-drive asset upload, downloading original assets, sharing and downloading static renditions, downloading dynamic renditions (presets and smart crops), link sharing for signed-in users, anonymous link sharing, and both public and private collections.

The table below outlines the key differences between AEM [!DNL Assets] [!DNL Content Hub] and Brand Portal:

| Area | Capability |[!DNL Content Hub]|Brand Portal|
|---|---|----|----|
| Configuring distribution experience | Configure metadata for filters, asset details, and add assets page |&#10003;|&minus;|
|  | Configure external links from portal |&#10003;|&minus;|
|  | Configure banner messaging |&#10003;|&#10003;|
|  | Configure banner image for branding |&#10003;|&#10003;|
|  | Configure primary and secondary colors for UI as per branding requirements |&#10003;|&minus;|
|Sharing assets from the DAM  | Sharing original approved assets from DAM |&#10003;|&#10003;|
|  | Approved asset changes synced automatically |&#10003;|&minus;|
| Search and filters | Dynamic filters (options show dynamically based on assets displayed) |&#10003;|&minus;|
|  | Search history |&#10003;|&minus;|
| Asset upload | Local drive |&#10003;|&#10003;|
|  | Add configurable metadata while uploading assets |&#10003;|&minus;|
| Download and renditions | Download original asset |&#10003;|&#10003;|
|  | Share and download static renditions from DAM |&#10003;|&#10003;|
|  | Download dynamic renditions (preset & smart crops)  |&#10003;|&#10003;|
|  | Ability to restrict view and download of expired assets  |&#10003;|&minus;|
|  Link sharing and Collections| Link share for signed-in users |&#10003;|&#10003;|
|  | Public collections |&#10003;|&#10003;|
|  | Search within collections |&#10003;|&minus;|
|  | Anonymous link share |&#10003;|&#10003;|
|  | Private collections |&#10003;|&#10003;|
|  Permissions| ACL-based permissions |&minus;|&#10003;|
|  | Attribute-based access control |&#10003;|&minus;|
|  Express integration| Edit [!DNL Content Hub] [!DNL Assets] in [!DNL Adobe Express] and save to DAM |&#10003;|&minus;|
|  Dashboards and reports| Insights dashboard |&#10003;|&minus;|
| UI Extensibility| Custom extension points on asset details page |Limited availability|&minus;|
|  Innovations coming soon| Favourite collections by user |&#10003;|&minus;|
|  | Pinned collections by Admin |&#10003;|&minus;|
|  | Semantic search |&#10003;|&minus;|
|  | Localised search and metadata display |&#10003;|&minus;|

## How can I select a repository to view assets only for the selected environment in AEM [!DNL Assets] [!DNL Content Hub]? {#select-repository-multiple-environments}

To view assets only for a selected environment in **Adobe Experience Manager (AEM) [!DNL Assets] [!DNL Content Hub]**, switch the active repository in your [!DNL Content Hub] profile. [!DNL Content Hub] connects to **one specific delivery repository at a time**, so selecting the repository for a given environment determines which assets appear. When you have configured [!DNL Content Hub] for Production and other lower environments within the same Program, you can point [!DNL Content Hub] at the repository for the environment you want to display. Execute the following steps:

1. Click the user icon in the right pane.

1. In the **[!UICONTROL Product Settings]** section, select **[!UICONTROL Select Repository]**.

1. Select the repository from the **[!UICONTROL Repository]** drop-down menu and click **[!UICONTROL OK]** to confirm.

   [!DNL Content Hub] now displays assets for the selected environment, because the interface is pointed at that environment's delivery repository and reads its assets directly.

   >[!NOTE]
   >
   >If assets from a specific environment, for example, **STAGE** are not appearing in [!DNL Content Hub] while assets from another environment, for example, **PRODUCTION** are, check the **[!UICONTROL Select Repository]** setting in your [!DNL Content Hub] profile. [!DNL Content Hub] connects to one specific delivery repository at a time, and the UI can remain pointed at a different environment's repository, for example, still **PRODUCTION** than the one currently being tested. As a result, the expected assets do not surface even though they exist. Switching the repository selection to the correct environment directly resolves this, and it does so without any change to asset approval or Attribute-Based Access Control (ABAC) configuration.

## How can AEM [!DNL Assets] [!DNL Content Hub] display the thumbnail preview for .ZIP file type? {#thumbnail-preview-zip-file}

Adobe Experience Manager (AEM) [!DNL Assets] [!DNL Content Hub] displays a thumbnail preview for file types such as .ZIP when a correctly named rendition is added to the asset. Add a rendition named **`cq5dam.<label>.<width>.<height>.<ext>`** to the root of the path where the .ZIP is available in Adobe Experience Manager (AEM) as a Cloud Service authoring environment. For example, **`cq5dam.preview.500.500.png`**.

### How [!DNL Content Hub] selects the rendition

[!DNL Content Hub] picks the rendition with the **greatest width** among all `cq5dam.*` renditions. This ensures the highest-resolution image is used as the preview. A custom rendition displays as a thumbnail preview only if its encoded width exceeds the existing auto-generated renditions.

### Requirements for the rendition image

The image that you add as a rendition:

* Can be in **JPG, JPEG, or PNG** format.

* Must be **under 50MB**.

When available, [!DNL Content Hub] displays this image as the preview thumbnail for the .ZIP file on [!DNL Content Hub].

>[!NOTE]
>
>A rendition named `cq5dam.preview.png` (without width and height in the filename) is not used as the preview thumbnail. The width and height are required for [!DNL Content Hub] to encode and size the preview correctly, so include the dimensions in the filename — for example, `cq5dam.preview.500.500.png`.

### Automatic thumbnail selection from .ZIP contents

If you do not add a custom rendition, [!DNL Content Hub] determines the thumbnail from the contents of the .ZIP file:

* **If the .ZIP contains one or more images**, [!DNL Content Hub] picks one of them as the thumbnail. When there are multiple images, it selects the first one in **alphanumeric filename order**.

* **If the .ZIP contains only non-image files** (for example, only a PDF, or only a video, with no eligible image inside), no thumbnail is generated. [!DNL Content Hub] does not extract a preview frame from a video and does not render a preview from a PDF inside the .ZIP file.

To guarantee a specific preview, add a custom `cq5dam.<label>.<width>.<height>.<ext>` rendition rather than relying on automatic selection, because automatic selection depends entirely on eligible image files being present inside the .ZIP.

## What Happens When I Approve an Asset for [!DNL Content Hub] versus Delivery? {#approve-an-asset}

Approving an asset with **Delivery** as the Approval Target is required to make the asset reachable through **public link-sharing**, while approving with **[!DNL Content Hub]** as the target only makes the asset visible inside the [!DNL Content Hub] portal. Approval is not a single binary state: the **Approval Target** selected at approval time determines exactly what the approval enables.

### [!DNL Content Hub] Target Versus Delivery Target

* **[!DNL Content Hub] target** — Makes the asset visible inside the [!DNL Content Hub] portal itself, but does **not** make it accessible through a public share link.
* **Delivery target** — Required for the asset to be reachable through **public link-sharing**.

This distinction exists because [!DNL Content Hub] portal visibility and public Delivery are governed by separate approval scopes. Selecting the wrong target therefore restricts where and how the asset can ultimately be accessed.

### Troubleshooting Broken Public Share Links

A **There is no content to display** message or a **404 Error** on a shared public link occurs because the underlying asset was approved with **[!DNL Content Hub]** as the target rather than **Delivery**. To resolve a broken share link, follow these steps:

1. Open the asset and check its **Approval Target**.
2. If the target is set to **[!DNL Content Hub]**, correct it to **Delivery**.
3. Re-test the public share link before investigating any other cause.

Correcting the **Approval Target** to **Delivery** should be the first troubleshooting action, as it is the most frequent cause of inaccessible public links.

### The `dam:roles` Metadata Field

When an asset is approved with **[!DNL Content Hub]** as the target, Adobe Experience Manager (AEM) auto-populates the `dam:roles` metadata field with a system-managed Identity Management System (IMS) group identifier. This is an expected, system-managed security mechanism used to restrict access to authenticated users only.

The presence of this identifier is **not** evidence of a workflow bug. The `dam:roles` value should not be manually edited or removed, and it does **not** conflict with the Attribute-Based Access Control (ABAC) rules. If a metadata schema exposes this field, mark it read-only or hidden so authors do not inadvertently change it. Control access visibility through ABAC and metadata configuration rather than by editing `dam:roles` directly, because manual edits to a system-managed field can disrupt the intended authenticated-access restrictions.

**See also**

* [Translate [!DNL Assets]](/help/assets/translate-assets.md)
* [Assets HTTP API](/help/assets/mac-api-assets.md)
* [Assets supported file formats](/help/assets/file-format-support.md)
* [Search assets](/help/assets/search-assets.md)
* [Connected assets](/help/assets/use-assets-across-connected-assets-instances.md)
* [Asset reports](/help/assets/asset-reports.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Download assets](/help/assets/download-assets-from-aem.md)
* [Manage metadata](/help/assets/manage-metadata.md)
* [Manage Dynamic Media templates](/help/assets/dynamic-media/manage-dynamic-media-templates.md)
* [Manage reports in [!DNL Assets] view](/help/assets/manage-reports-assets-view.md)
* [Search facets](/help/assets/search-facets.md)
* [Manage collections](/help/assets/manage-collections.md)
* [Bulk metadata import](/help/assets/metadata-import-export.md)
* [Publish [!DNL Assets] to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)
