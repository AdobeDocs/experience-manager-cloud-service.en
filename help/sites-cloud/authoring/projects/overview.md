---
title: Projects
description: Projects let you group resources into one entity whose common, shared environment makes it easy to manage your projects
exl-id: c5f3331e-637f-4816-be83-faf2df59bd5f
solution: Experience Manager Sites
feature: Authoring
role: User
---
# Projects {#projects}

Projects let you group resources into one entity. A common, shared environment makes it easy to manage your projects. The types of resources you can associate with a project are referred to in AEM as Tiles. Tiles may include project and team information, assets, workflows, and other types of information, as described in detail in [Project Tiles](#project-tiles).

>[!CAUTION]
>
>For users in projects to see other users/groups while using Projects functionality like creating projects, creating tasks/workflows, seeing and managing the team, those users need to have read access on `/home/users` and `/home/groups`. The easiest way to implement this is to give the **projects-users** group read access to `/home/users` and `/home/groups`.

As a user, you can do the following:

* Create projects
* Associate content and asset folders to a project
* Delete projects
* Remove content links from project

See the following additional topics:

* [Managing Projects](/help/sites-cloud/authoring/projects/managing.md)
* [Working with Tasks](/help/sites-cloud/authoring/projects/tasks.md)
* [Working with Project Workflows](/help/sites-cloud/authoring/projects/workflows.md)

## Projects Console {#projects-console}

The projects console is where you access and manage your projects within AEM.

![The Projects console](/help/sites-cloud/authoring/assets/projects-console.png)

* Select **Timeline** and then a project to view its timeline.
* Select **Select** to enter selection mode.
* Click **Create** to add projects.
* **Toggle Active Projects** lets you switch between all projects and only those that are active.
* **Show Statistics View** lets you see project statistics concerning task completions.

## Project Tiles {#project-tiles}

With Projects, you associate different types of information with your projects. These are called **Tiles**. Each of the tiles and what kind of information they contain is described in this section.

You can have the following tiles associated with your project. Each is described in the sections that follow:

* Assets and asset collections
* Experiences
* Links
* Project Information
* Team
* Landing Pages
* Emails
* Workflows
* Launches
* Tasks

### Assets {#assets}

In the **Assets** tile, you can gather all assets that you use for a particular project.

![Assets tile](/help/sites-cloud/authoring/assets/projects-assets-tile.png)

You upload assets directly in the tile. In addition you can create Image Sets, Spin Sets, or Mixed Media Sets if you have the Dynamic Media add-on.

![Image set](/help/sites-cloud/authoring/assets/projects-image-sets.png)

### Asset Collections {#asset-collections}

Similar to assets, you can add [asset collections](/help/assets/manage-collections.md) directly to your project. You define collections in Assets.

![Asset collection](/help/sites-cloud/authoring/assets/projects-asset-collections.png)

Add a collection by clicking **Add Collection** and selecting the appropriate collection from the list.

### Experiences {#experiences}

The **Experiences** tile lets you add a Mobile app, web site, or publication to the project.

![Experiences](/help/sites-cloud/authoring/assets/project-experiences.png)

The icons indicate which kind of experience is represented: web site, mobile application or a publication. Add experiences by tapping or clicking the down chevron and tapping **Add Experience** and selecting the type of experience.

![Add an experience](/help/sites-cloud/authoring/assets/projects-add-experience.png)

Select the path for the thumbnails and if applicable, change the thumbnail for the experience. Experiences are grouped together in the **Experiences** tile.

### Links {#links}

The Links tile lets you associate external links with your project.

![Links](/help/sites-cloud/authoring/assets/project-links.png)

You can name the link with an easy-to-recognize name and change the thumbnail.

![Add link](/help/sites-cloud/authoring/assets/projects-add-link.png)

### Project Info {#project-info}

The Project Information tile provides general information on the project including a description, project status (inactive or active), a due date, and members. In addition, you can add a project thumbnail, which is displayed on the main Projects page.

![Project info](/help/sites-cloud/authoring/assets/project-info.png)

Team members can be assigned and deleted from this tile (or have their roles changed) and the Team tile.

![Add team members to project](/help/sites-cloud/authoring/assets/projects-add-team.png)

### Translation Job {#translation-job}

The Translation Job tile is where you start a translation and also where you see the status of your translations. To set up your translation, see [Creating Translation Projects](/help/assets/translate-assets.md).

![Translation job](/help/sites-cloud/authoring/assets/projects-translation-job.png)

Click the ellipsis at the bottom of the **Translation Job** card to view the assets in the translation workflow. The translation job list also displays entries for asset metadata and tags. These entries indicate that the metadata and tags for the assets are also translated.

![Translation job detail](/help/sites-cloud/authoring/assets/projects-translation-job-detail.png)

### Team {#team}

In this tile, you can specify the members of the project team. When editing, you can enter the name of the team member and assign the user role.

![Team tile](/help/sites-cloud/authoring/assets/projects-team-tile.png)

You can add and delete team members from the team. In addition, you can edit the [user role](#user-roles-in-a-project) assigned to the team member.

![Add team from list](/help/sites-cloud/authoring/assets/projects-add-team-list.png)

### Workflows {#workflows}

You can assign your project to follow certain workflows. If any workflows are running, their status displays in the **Workflows** tile in Projects.

![Workflows](/help/sites-cloud/authoring/assets/project-workflows.png)

You can assign your project to follow certain workflows. Depending on which project you choose you have different workflows available.

These are described in [Working with Project Workflows](/help/sites-cloud/authoring/projects/workflows.md).

### Launches {#launches}

The Launches tile shows any launches that have been requested with a [Request Launch workflow](/help/sites-cloud/authoring/projects/workflows.md).

![Launches](/help/sites-cloud/authoring/assets/project-launches.png)

### Tasks {#tasks}

Tasks let you monitor the status of any project-related tasks, including workflows. Tasks are covered in detail at [Working with Tasks](/help/sites-cloud/authoring/projects/tasks.md).

![Tasks](/help/sites-cloud/authoring/assets/projects-tasks.png)

## Project Templates {#project-templates}

AEM ships with three different templates out of the box:

* A simple project - A reference sample for any projects that do not fit into other categories (a catch-all). It includes three basic roles (Owners, Editors, and Observers) and four workflows (Project Approval, Request Launch, Request Landing Page and Request Email).
* A media project - A reference sample project for media-related activities. It includes several media related project roles (Photographers, Editors, Copywriters, Designers, Owners and Observers). It also Request Copy workflow to request and review text.
* A [translation project](/help/sites-cloud/administering/translation/overview.md) - A reference sample for managing translation related activities. It includes three basic roles (Owners, Editors, and Observers). It includes two workflows that are accessed in the Workflows user interface.

Based on the template you select, you have different options available to you particularly around user roles and workflows.

## User Roles in a Project {#user-roles-in-a-project}

The different user roles are set in a Project template and are used for two primary reasons:

1. Permissions. The user roles fall into one of the three categories listed: Observer, Editor, Owner. For example, a Photographer or Copywriter will have the same privileges as an Editor. The permissions determine what a user can do to content in a project.
1. Workflows. The workflows determine who is assigned tasks in a project. The tasks can be associated with a project role. For example, a task can be assigned to Photographers so all team members that have the Photographer role will get the task.

All projects support the following default roles to let you administer security and control permissions:

|Role|Description|Permissions|Group Membership|
|---|---|---|---|
|Observer|A user in this role can view project details, including the project status.|Read-only permissions on a project|`workflow-users` group|
|Editor|A user in this role can upload and edit the contents of a project.|Read and Write access on a project, associated metadata, and related assets; privileges to upload a shot list, and review and approve assets; write permission on /etc/commerce; modify permission on a specific project|workflow-users group|
|Owner|A user in this role can initiate a project. An owner can create a project, initiate work in a project, and also move approved assets to the Production folder. Although all other tasks in the project can also be viewed and performed by the owner.|Write permission on `/etc/commerce`|`dam-users` group (to be able to create a project) project-administrators group (to be able to create a project and move assets)|

>[!NOTE]
>
>When you create the project and add users to the various roles, groups associated with the project are automatically created to manage associated permissions. For example, a project called Myproject would have three groups **Myproject Owners**, **Myproject Editors**, **Myproject Observers**. However, if the project is deleted, those groups are not automatically deleted. An administrator must manually delete the groups in **Tools** &gt; **Security** &gt; **Groups**.
