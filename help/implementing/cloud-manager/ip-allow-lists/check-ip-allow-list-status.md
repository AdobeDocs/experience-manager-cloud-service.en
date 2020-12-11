---
title: Checking IP Allow List Status
description: Checking IP Allow List Status
---

# Checking IP Allow List Status {#check-allow-list-status}

Follow the steps below to determine the status of updates to your IP Allow List:

1. Click on the Status icon for the IP Allow List from the table from the **Environments** screen and select **IP Allow Lists** page.

1. Cloud Manager will display one of the following statuses, as mentioned in the section below.

## Status of an IP Allow List {#status}

The following are the definitions of status that will appears in an IP Allow List:

* **Applied**: IP Allow List is successfully applied on environments.  The environments and service can be seen as shown in the image below.

* **Updating**: An update to the IP Allow List which may include one or more apply or unapply is in process. Each Apply and Unapply will be  listed along with Not Started/In Progress/Complete or Failed.

* **Failed**: One or more apply or unapply process in an Update failed. Each Apply and Unapply will be  listed along with Complete or Failed.
   * The status will be Failed, even if one apply/unapply in the update fails. 
   * The status will remain Failed until all failures are cleared. User must select the retry icon next to the status to clear the failure.
   * User will not be able to Update or Delete IP Allow List while the status is Failed.

* **Deleting**: Delete request is in progress. This involves unapply of all services. Each Unapply will be  listed along with Not Started/In Progress/Complete or Failed.
Once Delete operation is completed, the IP Allow List will:
   * No longer appear in the IP Allow List table.
   * No longer be applied on any service in the program in Cloud Manager.

* **Delete Failed**: One or more unapply process in a Delete operation failed. Each Unapply will be  listed along with Complete or Failed.

   * The status will be Delete Failed, even if one unapply fails. 
   * The status will remain Delete Failed until all failures are cleared. User must select Delete from the **...** menu at the far right of the row in the table to clear any failure. 
   * User will not be Allow to Update IP Allow List while the status is Failed.

