---
title: Contributor guide for Adobe documentation
seo-title: Contributor guide overview for [!UICONTROL Adobe Experience Cloud] technical documentation
description: The guide describes how you can contribute suggestions and additions to the Adobe documentation site.
seo-description: The guide describes how you can contribute to the [!UICONTROL Adobe Experience Cloud] technical documentation.
---

# Contributor Guide Overview for Documentation

<!---
<https://docs.microsoft.com/en-us/contribute/>
-->

## Working with Collaborative Documentation

The documentation for [!UICONTROL Adobe Experience Cloud] is transitioning to an open source model, utilizing Github, Markdown and [!UICONTROL Adobe Experience Manager]. As a user of this material - regardless of if you are an employee, partner, customer or even prospective customers - you can contribute to this documentation in several simple ways; everything from making quick edits to existing documents to submitting entire articles, complete with assets and code samples. This open source model improves communication between the product teams, the documentation teams, and customers. 
 
<!--
> [!IMPORTANT]
> All repositories that publish to docs.adobe.com have adopted the [Adobe Open Source Code of Conduct](../code-of-conduct.md) or the [.NET Foundation Code of Conduct](https://dotnetfoundation.org/code-of-conduct). For more information, see the [Contributing](../contributing.md) article.
>
> Minor corrections or clarifications to documentation and code examples in public repositories are covered by the [Adobe Documentation Terms of Use](https://www.adobe.com/legal/terms.html). New or significant changes generate a comment in the pull request, asking you to submit an online Contribution License Agreement (CLA) if you are not an employee of Adobe. We need you to complete the online form before we can review or accept your pull request.
--->
    
## Make quick edits to existing documents

Making quick edits is a good way to fix small errors and omissions in documents. If an article displays an edit button as shown below, you can make a quick fix yourself. When you edit the document, you submit a pull request (PR) to submit the fix/suggestion to us, and we can vet, approve and publish the suggestion.

1. Click `Edit this page` on the right column to go to the markdown source file on GitHub.

   <!---![Location of the Edit link](assets/edit-article.png)-->

1. Click the `pencil icon` to edit the article.  
   > [!NOTE]
   > If the pencil icon is grayed out, you need to login to your GitHub account, or create a new account.  

   ![Location of the pencil icon](assets/edit-icon.png)

1. Make your changes in the web editor. You can click the **Preview changes** tab to check formatting of your change.
1. Once you have made your change(s), scroll to the bottom of the page. Enter a title and description for your PR and click **Propose file change** as shown in the following figure:  
   ![proposing your change](assets/submit-pull-request.png)

That's all there is to it. Thank you! Documentation team members will review and merge your pull request.

## Log an Issue

Another easy way to let us know about a problem with a piece of content is to 'Log an Issue'.

1. If you see a problem with a piece of content, click the `Log an Issue` link in the lower right of any page. See figure below:

   ![](assets/git_log_issue.png)
   
   > [!NOTE]
   > You will need to login to your GitHub account, or create a new account, to log an issue. 
   
   Clicking this link will allow you to log a quick ticket with us, using the Github Issue interface.
   
1. The URL of the page with the issue will automatically populate in the description field. Fill in the title, write a short description of the issue, and then click *Submit new issue*.

   ![](assets/git_issue_example.png)

This will directly notify the content team for this page who will be able to take action. When we have updated the content, we'll let you know in the Github Issues interface, and it will notify you by email when updated or closed.

## Understand GitHub permissions

The GitHub editing UI adapts to your repository permissions. The preceding images are accurate for contributors that do not have write permissions to the target repository. GitHub automatically creates a fork of the target repository in your account. If you have write access to the target repository, GitHub creates a new branch in the target repo.

Adobe uses pull requests for all changes, even for contributors that have write access. Most repositories have the `master` branch protected so that updates must be submitted as pull requests.

The in-browser editing experience is best for minor or infrequent changes. If you make large contributions, or use advanced Git features, we recommend that you [fork the repo and work locally](setup/full-workflow.md).

## Provide feedback

With a solution set as large as Adobe's, the documentation is always a work in progress. If you spot errors, log an issue, if you have suggestions on material please let us know. Tell us what information you were looking for. Let us know if you couldn't find what you needed, or if you had difficulty completing your task, please let us know how we can help you learn our solutions.

Thanks from the Collaborative Documentation team and all the writers and content producers in the [!UICONTROL Adobe Experience Cloud].
