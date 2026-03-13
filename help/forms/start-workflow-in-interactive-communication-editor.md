# Start Workflow in Interactive Communication Editor

## Overview

The Interactive Communication Authoring Workflow feature allows authors to apply predefined workflows to an Interactive Communication. Workflows help automate the review and approval process by routing the IC through a sequence of tasks assigned to different users.

By using workflows, teams can ensure that IC content is reviewed, validated, and approved before it is finalized or published.

## How Workflows Work with Interactive Communications

In AEM Forms, workflows automate a series of steps performed on an Interactive Communication. Once a workflow is applied, the IC moves through different stages where assigned users complete specific tasks.

A typical workflow process includes the following steps:

1. **Author applies the workflow**
   The author selects and applies a workflow to the Interactive Communication. This action initiates the workflow process.

2. **Workflow task assignment**
   The workflow engine creates a **work item** and assigns it to the designated user or group (for example, an editor or reviewer).

3. **Editor reviews the IC**
   The assigned editor receives a notification or work item indicating that the IC requires review. The editor opens the IC, reviews the content, and makes necessary updates or comments.

4. **Task completion**
   After completing the review, the editor marks the work item as **complete**, which moves the workflow to the next step or finalizes the process depending on the workflow configuration.

## Applying a Workflow to an Interactive Communication

Follow these steps to apply a workflow to an IC:

1. Navigate to **AEM Forms > Communications**.
2. Select the **Interactive Communication** you want to process.
3. From the toolbar, select **Start Workflow**.
4. Choose the required **workflow model** from the available list.
5. Provide any required details such as workflow title, description, or assignee.
6. Click **Start** to initiate the workflow.

Once started, the IC enters the workflow process and assigned users receive their respective work items.

### Benefits of Using IC Authoring Workflows

* Automates review and approval processes
* Ensures content quality and compliance
* Improves collaboration between authors and editors
* Tracks workflow progress and task completion

The **IC Authoring Workflow** feature enables organizations to streamline the content lifecycle for Interactive Communications. By applying workflows, authors can automate review processes, assign tasks to editors or reviewers, and ensure that the IC is properly reviewed before completion. This structured approach improves efficiency, collaboration, and governance in IC content management.
