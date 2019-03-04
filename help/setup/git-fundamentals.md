---
title: Git and GitHub documentation essentials
seo-title: Git and GitHub documentation essentials
description: This article explains an overview of Git, GitHub repository, and how content is organized, and naming conventions used for Adobe documentation.
seo-description: this article explains an overview of git,  github repository, and how content is organized, and naming conventions used for adobe documentation.
index: no
---
# Git and GitHub documentation essentials

## Overview

If you just need to make minor, text-only changes to articles, you do not need to understand the details of this article. This article describes the workflow for making major edits, such as creating new articles, adding images, or making ongoing edits to Adobe documentation. 

As a contributor to Adobe documentation content, you can interact with multiple tools and processes. You can work in parallel with other contributors on the same project, potentially the exact same content, even at the same time. This is all enabled through Git and GitHub software.

Git is an open-source version control system that allows collaboration. Multiple contributors can work on files that live in *repositories*. 

GitHub is a web-based hosting service for Git repositories, such as those used to store [docs.adobe.com](https://docs.adobe.com) content. For any project, GitHub hosts the main repository, from which contributors can make copies for their own work.

## Git

Git has a unique contribution workflow and terminology to support its distributed model. For instance, there is no file locking that is normally associated with check-out/check-in operations. Git allows changes to be resolved at an even finer level, comparing files byte by byte.

Git also uses a tiered structure to store and manage content for a project:

- *Repository*: Also known as a *repo*, this is the highest unit of storage. A repository contains one or more branches.
- *Branch*: All repositories contain a default branch (typically named "master") and one or more branches that are destined to be merged back into the master branch. The master branch serves as the current version and source from which content is published. It's the parent from which all other branches in the repository are created.

Contributors interact with Git to update and manipulate repositories at both the local and GitHub levels:

- Locally through tools such as the GitHub Desktop.
- Via [www.github.com](https://www.github.com), which integrates Git to manage the reconciliation of contributions that flow back into the main repository.

## GitHub

All workflows begin and end at the GitHub level, where the main repository for any Adobe documentation project is stored. The copies that contributors create for their own use are distributed across multiple computers. These copies are eventually reconciled back into the project's main GitHub repository.

### Directory organization

A project's default/master branch serves as the current version of content for the project. The content in the master branch--and branches created from it--aligns with the organization of the article topics. Subdirectories are used for organizing content and image assets.

You can typically find a main `help` directory off the root of the repository. The articles directory contains a set of subdirectories. Articles in the subdirectories are formatted as Markdown files that use an *.md* extension.

Within the root of this directory, you can find general articles that relate to the overall service or product. And typically, you can then find another series of subdirectories that match the features/services or common scenarios. 

### Assets directory

User guide directories contain `/assets` subdirectories for image files that are referenced within a directory.

<!---
### Markdown file template

For convenience, the root directory of each repository typically contains a Markdown template file named `template.md`. You can use this template file as a "starter file" if you need to create a new article for submission to the repository. The file contains:

- A **metadata header** at the top of the file, delineated by two, 3-hyphen lines. It contains the various tags used for tracking information related to the article. It also includes SEO optimizations and reporting processes that Adobe uses to evaluate the performance of the content. So the metadata is important!
- Various **examples of using Markdown** to format the elements of an article.
- General **instructions on the use of Markdown extensions**, which you can use for various types of alerts.
- Examples of **embedding video** by using an iframe.
- General **instructions on the use of docs.adobe.com extensions**, which you can use for special controls such as buttons and selectors.
-->

## Pull requests

A *pull request* provides a convenient way for a contributor to propose a set of changes that will be applied to the default branch. The changes (also known as *commits*) are stored in a contributor's branch, so GitHub can first model the impact of *merging* them into the default branch. A pull request also serves as a mechanism to provide the contributor with feedback from a build/validation process, the pull request reviewer, to resolve potential issues or questions before the changes are merged into the default branch.

There are two ways to contribute by pull request, depending on the size of changes that you want to propose. We will cover this in detail later, in the [GitHub workflow](local-repo.md) section of this guide.
