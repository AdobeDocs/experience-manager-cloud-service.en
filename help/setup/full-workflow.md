---
lastModified: 2018-06-28
title: GitHub contribution workflow for major changes
seo-title: GitHub contribution workflow for major changes to Adobe documentation
description: this article shows you how to use the "major" contributor workflow to make contributions to adobe documentation.
seo-description: this article shows you how to use the "major" contributor workflow to make contributions to adobe documentation.
---

# GitHub contribution workflow for major changes

<!--
> [!IMPORTANT]
> All repositories that publish to docs.adobe.com have adopted the [Adobe Open Source Code of Conduct](../../code-of-conduct.md) or the [.NET Foundation Code of Conduct](https://dotnetfoundation.org/code-of-conduct). For more information, see the [Contributing](../../contributing.md) article.
>
> Minor corrections or clarifications to documentation and code examples in public repositories are covered by the [Adobe Documentation Terms of Use](https://www.adobe.com/legal/terms.html). New or significant changes generate a comment in the pull request, asking you to submit an online Contribution License Agreement (CLA) if you are not an employee of Adobe. We need you to complete the online form before we can review or accept your pull request.
--->

## Overview

This workflow is suitable for a contributor who needs to make a major change or will be a frequent contributor to a repository. Frequent contributors typically have ongoing (long-running) changes, which go through multiple build/validation/staging cycles or span multiple days before pull request sign-off and merge.

### Terminology

Before you start, let's review some of the Git/GitHub terms used in this workflow. 

| Name | Description |
|-----------|-------------|
|fork|Normally used as a noun, when referring to a copy of a main GitHub repository. In practice, a fork is just another repository. But it's special in the sense that GitHub maintains a two-way connection back to the main/parent repository. It's sometimes used as a verb, as in "You must fork the repository first."|
|remote|A named connection to a remote repository, such as the "origin" or "upstream" remote. Git refers to these as remotes because they are used to reference a repository that's hosted on another computer. In this workflow, a remote is always a GitHub repository.|
|origin|The name assigned to the connection between your local repository and the repository from which it was cloned. In this workflow, origin represents the connection to your fork. It's sometimes used as a moniker for the origin repository itself, as in "Remember to push your changes to origin."|
|upstream|Like the origin remote, upstream is a named connection to another repository. In this workflow, upstream represents the connection between your local repository and the main repository, from which your fork was created. It's sometimes used as a moniker for the upstream repository itself, as in "Remember to pull the changes from upstream."|

If you are unfamiliar with Git and GitHub concepts such as a repository or branch, please first review [Git and GitHub fundamentals](git-fundamentals.md).

## Workflow

>[!IMPORTANT]
> If you haven't already, you must complete the steps in the [Setup](sign-up.md) section. 

In this workflow, changes flow in a repetitive cycle. Starting from your device's local repository, they flow back up to your GitHub fork, into the main GitHub repository, and back down locally again as you incorporate changes from other contributors.

### Use GitHub flow

Recall from [Git and GitHub fundamentals](git-fundamentals.md) that a Git repository contains a master branch, plus any additional work-in-progress branches that have not been integrated into master. Whenever you introduce a set of logically related changes, it’s a best practice to create a *working branch* to manage your changes through the workflow. We refer to it here as a working branch because it's a workspace to iterate/refine changes, until they can be integrated back into the master branch.

Isolating related changes to a specific branch allows you to control and introduce those changes independently, targeting them to a specific release time in the publishing cycle. In reality, depending on the type of work you do, you can easily end up with several working branches in your repository. It's not uncommon to be working on multiple branches at the same time, each representing a different project.

>[!NOTE]
>Making your changes in the master branch *is not a good practice*. Imagine that you use the master branch to introduce a set of changes for a timed feature release. You finish the changes and are waiting to release them. Then in the interim, you have an urgent request to fix something, so you make the change to a file in the master branch and then publish the change. In this example, you inadvertently publish both the fix *and* the changes that you were holding for release on a specific date.

The next step is to create a new working branch in your local repository, to capture your proposed changes. Each git client is different, so consult the help for your preferred client. You can see an overview of the process in the GitHub Guide on [GitHub flow](https://guides.github.com/introduction/flow/).

## Pull request processing

You submit proposed changes by bundling them in a new pull request (PR) that is added to the destination repository's PR queue. A pull request enables GitHub's collaboration model, by asking for the changes from your working branch to be pulled and merged into another branch. In most cases, that other branch is the default/master branch in the main repository.

### Validation

Before your pull request can be merged into its destination branch, it might be required to pass through one or more PR validation processes. Validation processes can vary depending on the scope of proposed changes and the rules of the destination repository. After your pull request is submitted, you can expect the content to be reviewed and, if and when appropriate, merged into the main repository.

### Review and sign-off

After all PR processing is completed, you should review the results (PR comments, preview URLs, etc.) to determine if additional changes to its files are required before you sign off for merging. If a PR reviewer has reviewed your pull request, they can also provide feedback via comments if there are outstanding issues/questions to be resolved prior to merge.

When the pull request is issue-free and signed off, your changes are merged back into the parent branch and the pull request is closed.

### Publishing

Remember, your pull request has to be merged by a PR reviewer before the changes can be included in the next scheduled publishing run. Pull requests are normally reviewed/merged in the order of submission. If your pull request requires merging for a specific publishing run, you will need to work with your PR reviewer ahead of time to ensure that merging happens prior to publishing.

After your contributions are approved and merged, the docs.microsoft.com publishing process picks them up. Depending on the team that manages the repository you are contributing to, publishing times can vary.
