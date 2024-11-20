---
title: Work-In-Progress Sites Features for Edge Delivery Services
description: Learn which AEM Sites features and use cases are a work-in-progress and discover alternate solutions when using Edge Delivery Services.
solution: Experience Manager Sites
feature: Edge Delivery Services
role: User
exl-id: 21745f53-a7ef-4eec-9170-b267c2f4314e
---
# Work-In-Progress Sites Features for Edge Delivery Services {#wip-sites-features}

Learn which AEM Sites features and use cases are a work-in-progress and discover alternate solutions when using Edge Delivery Services.

>[!TIP]
>
>Work-in-progress does not mean the end of the road. If you require a feature or use case listed as work-in-progress in this document, please reach out to your Adobe representative. You and Adobe can work together to understand your particular needs and find alternate solutions.

## Work-In-Progress Features {#wip-features}

When using Edge Delivery Services with AEM Sites, most Sites features are available. For example, nearly any action available in the [Sites Console](/help/sites-cloud/authoring/sites-console/introduction.md) is applicable to Edge Delivery Services.

However, some features are a work-in-progress (WIP). WIP features are features of the Sites console which either are not yet available for Edge Delivery Services with AEM Sites or are only partially available. For this reason, WIP features may be presented differently than their Sites counterparts or there may be alternative solutions for the use case.

The following list presents such WIP features and alternate solutions. If your project requires a WIP feature, please review the alternatives suggested below and reach out to Adobe to work together to understand your use case.

|Sites Feature|Status on Edge|Notes|Edge Documentation|
|---|---|---|---|
|[Page Inheritance](/help/sites-cloud/administering/msm-and-translation.md)|Available||[Content Inheritance in the Universal Editor](/help/sites-cloud/authoring/universal-editor/inheritance.md)|
|[Component Inheritance](/help/sites-cloud/administering/msm-and-translation.md)|Partially Available|Components inherit content, but inheritance can only be reverted at the page level|[Content Inheritance in the Universal Editor](/help/sites-cloud/authoring/universal-editor/inheritance.md)|
|[Language Copy](/help/sites-cloud/administering/translation/overview.md)|Partially available|Components inherit content, but inheritance can only be reverted at the page level|[Content Inheritance in the Universal Editor](/help/sites-cloud/authoring/universal-editor/inheritance.md)|
|[Multi Site Management](/help/sites-cloud/administering/msm/overview.md)|Partially available|Components inherit content, but inheritance can only be reverted at the page level|[Content Inheritance in the Universal Editor](/help/sites-cloud/authoring/universal-editor/inheritance.md)|
|[Launches](/help/sites-cloud/authoring/launches/overview.md)|Partially Available|Components inherit content, but inheritance can only be reverted at the page level|[Content Inheritance in the Universal Editor](/help/sites-cloud/authoring/universal-editor/inheritance.md)|
|[Page Templates](/help/sites-cloud/authoring/page-editor/templates.md)|Partially available|Pages created from templates are independent copies of the original template.|[Using Page Templates with the Universal Editor](/help/sites-cloud/authoring/universal-editor/templates.md)|
|[Context Hub and Targeting](/help/sites-cloud/authoring/personalization/overview.md)|Not available|||
|[Timewarp](/help/sites-cloud/authoring/launches/preview.md)|Not available|||
|[Associated Content](/help/sites-cloud/authoring/page-editor/editor-side-panel.md#associated-content-browser)|Not available|||
|[Experience Fragments](/help/sites-cloud/authoring/fragments/experience-fragments.md)|Alternative|Create a page and use a fragment component||

## Work-In-Progress Use Cases {#wip-use-cases}

Because Edge Delivery Services are built on an entirely new and modern technology stack, the following use cases of AEM Sites are not yet fully covered and are a work-in-progress. If your project requires a WIP use case, please reach out to Adobe to work together and to understand your project's needs.

|Sites Use Case|Details|
|---|---|
|Server-side logic to render pages|Using AEM's runtime as app server|
|Dynamic pages|SSI or any dynamic includes technique|
|User management|Using AEM as IdP|
|Authentication|Using AEM for secure content|
|Content permissioning|AEM as secure extranet|
