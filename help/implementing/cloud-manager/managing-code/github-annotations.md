---
title: GitHub Check Annotations
description: Learn how GitHub checks annotate PRs for your private repositories to provide you will helpful feedback.
exl-id: 15178de8-8a8a-4300-8510-88875ad0fc8c
feature: Cloud Manager, Developing
role: Admin, Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: a01bfd36-4ab8-4bf8-9dc0-5b45b890552e
    internal-label: APIs
subfeature_v2:
  - id: d9eb3b3e-9447-4ed4-bf4a-96c7b245cb27
    internal-label: Cloud Manager APIs
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---

# GitHub Check Annotations {#github-annotations}

Learn how GitHub checks annotate PRs for your private repositories to provide you with helpful feedback.

## Overview {#overview}

If you are using [private repositories](private-repositories.md) for your Cloud Manager program, checks in GitHub are automatically run for every pull request. These PRs are annotated with useful information to help you understand any issues with your code as soon as possible.

![Example of GitHub check annotations](assets/github-check-annotations.png)

[Code quality](/help/implementing/cloud-manager/code-quality-testing.md) issues detected by [SonarQube](/help/implementing/cloud-manager/custom-code-quality-rules.md) are clearly listed. 

![Example of code issue annotation](assets/github-check-annotations-example.png)

The exact line of code with the issue is provided and you can select it to display the relevant code. These annotations cover code issues, not just those in the pull request.

![Example of code issue annotation](assets/github-check-annotations-example-code.png)

All annotated lines are aggregated on the **Files Changed** tab on the GitHub pull request. Annotations for unchanged pull request files appear in their own section.

![Example of annotations on files changed tab](assets/github-check-annotations-files-changed.png)

## Code Quality Pipelines {#code-quality-pipelines}

The [code quality](/help/implementing/cloud-manager/code-quality-testing.md) results are also visible in the pipeline that Cloud Manager automatically triggers at the bottom of the **Checks** tab. It is also accessible from the **Details** of the pull request check.

![Example of annotations](assets/github-check-annotations-code-quality.png)

![Example of annotations](assets/github-check-annotations-code-quality-2.png)

You can also visualize the issues in the form of a CSV. You can retrieve this CSV by [viewing the details of the pipeline execution in Cloud Manager](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md#view-details).
