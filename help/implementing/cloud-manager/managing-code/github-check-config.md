---
title: GitHub Check Configuration for Private Repositories
description: Learn how to control the pipelines that are created automatically to validate each pull request to a private repository.
exl-id: 3ae3c19e-2621-4073-ae17-32663ccf9e7b
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---
# GitHub check configuration for private repositories {#github-check-config}

Learn how to control the pipelines that are created automatically to validate each pull request to a private repository.

## Configuration of GitHub checks {#configuration}

When using [private repositories](private-repositories.md#using), a [full stack code quality pipeline](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md) is created automatically. This pipeline is started at each pull request update.

You can control these checks by creating a `.cloudmanager/pr_pipelines.yml` configuration file in the default branch of the private repository.

```yaml
github:
  shouldDeletePreviousComment: false
  shouldSkipCheckAnnotations: false
pipelines:
  - type: CI_CD
    template:
      programId: 1234
      pipelineId: 456
    namePrefix: Full Stack Code Quality Pipeline for PR
    importantMetricsFailureBehavior: CONTINUE
```

| Parameter | Possible Values | Default | Description |
| --- | --- | --- | --- |
| `shouldDeletePreviousComment` | `true` or `false` | `false` | Whether to keep only the last comment with the code scanning results on this GitHub pull request or keep all. Setting it to `false` (default) means that previous comments are not deleted. |
| `shouldSkipCheckAnnotations` | `true` or `false` | `false` | Whether to have additional annotations present on the GitHub pull request check or not. Setting it to `false` (default) means that check annotations are not skipped and are included in the feedback. |
| `type` |`CI_CD`| n/a | Defines the behavior of CI/CD (Continuous Integration/Continuous Deployment) pipeline configurations. |
| `template.programId` | Integer | No pipeline variables are reused | You can use it to reuse the [pipeline variables](/help/implementing/cloud-manager/configuring-pipelines/pipeline-variables.md) set on an existing pipeline automatically created by each pull request. |
| `template.pipelineId` | Integer| No pipeline variables are reused | You can use it to reuse the [pipeline variables](/help/implementing/cloud-manager/configuring-pipelines/pipeline-variables.md) set on an existing pipeline automatically created by each pull request. |
| `namePrefix` | String | `Full Stack Code Quality Pipeline for PR` | Used to set the prefix for the name of the pipeline that is created automatically. |
| `importantMetricsFailureBehavior` | `CONTINUE` or `FAIL` or `PAUSE` | `CONTINUE` | Sets the important metric behavior of the pipeline<br>`CONTINUE` = If an important metric fails, the pipeline moves forward automatically<br>`FAIL` = The pipeline finishes with a FAILED status if an important metric fails<br>`PAUSE` = The code scanning step receives a WAITING status when an important metric fails and must be manually resumed |




