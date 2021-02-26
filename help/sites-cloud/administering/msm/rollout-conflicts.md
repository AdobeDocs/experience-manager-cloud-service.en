---
title: Rollout Conflicts
description: Learn how to manage and resolve Multi Site Manager rollout conflicts.
---

# Rollout Conflicts {#msm-rollout-conflicts}

Conflicts can occur if new pages with the same page name are created in both the blueprint branch and a dependent Live Copy branch. Such conflicts need to be handled and resolved upon rollout.

## Conflict Handling {#conflict-handling}

When conflicting pages do exist (in the blueprint and Live Copy branches), MSM allows you to define how (or even if) they should be handled.

To ensure that the rollout is not blocked, possible definitions can include:

* Which page (blueprint or Live Copy) will have priority during rollout
* Which pages will be renamed (and how)
* How this will affect any published content

The default behavior of AEM out-of-the-box is that published content will not be impacted. So if a page that was manually created in the Live Copy branch has been published, that content will still be published after the conflict handling and rollout.

In addition to the standard functionality, customized conflict handlers can be added to implement different rules. These can also allow publishing actions as an individual process.

### Example Scenario {#example-scenario}

In the following sections we use the example of a new page `b`, created in both the blueprint and the Live Copy branch (created manually), to illustrate the various methods of conflict resolution:

* blueprint: `/b`

  A master page with 1 child page, `bp-level-1`

* Live Copy: `/b`

  A page manually created in the Live Copy branch with 1 child page, `lc-level-1`

  * Activated on publish as `/b`, together with the child page

#### Before Rollout {#before-rollout}

||Blueprint Before Rollout|Live Copy Before Rollout|Publish Before Rollout|
|---|---|---|---|
|Value|`b`|`b`|`b`|
|Comment|Created in blueprint branch, ready for rollout|Manually created in Live Copy branch|Contains the content of the page `b` that was manually created in the Live Copy branch|
|Value|`/bp-level-1`|`/lc-level-1`|`/lc-level-1`|
|Comment||Manually created in Live Copy branch|contains the content of the page `child-level-1` that was manually created in the Live Copy branch|

## Rollout Manager and Conflict Handling {#rollout-manager-and-conflict-handling}

The rollout manager allows you to activate or deactivate conflict management.

This is done using [OSGi configuration](/help/sites-deploying/configuring-osgi.md) of **Day CQ WCM Rollout Manager**. Set the value **Handle conflict with manually created Pages** ( `rolloutmgr.conflicthandling.enabled`) to true if the rollout manager should handle conflicts from a page created in the Live Copy with a name that exists in the blueprint.

AEM has [predefined behavior when conflict management has been deactivated.](#behavior-when-conflict-handling-deactivated)

## Conflict Handlers {#conflict-handlers}

AEM uses conflict handlers to resolve any page conflicts that exist when rolling out content from a blueprint to a Live Copy. Renaming pages is the usual (not not only) method of resolving such conflicts. More than one conflict handler can be operational to allow for a selection of different behaviors.

AEM provides:

* The [default conflict handler](#default-conflict-handler):
  * `ResourceNameRolloutConflictHandler`
* The possibility to implement a [customized handler](#customized-handlers)
* The service ranking mechanism that allows you to set the priority of each individual handler
  * The service with the highest ranking is used.

### Default Conflict Handler {#default-conflict-handler}

The default conflict handler is `ResourceNameRolloutConflictHandler`

* With this handler the blueprint page is given precedence.
* The service ranking for this handler is set low, i.e. below the default value for the `service.ranking` property, as the assumption is that customized handlers will need a higher ranking. However, the ranking is not the absolute minimum to ensure flexibility when required.

This conflict handler gives precedence to the blueprint. Fore example, the Live Copy page `/b` is moved within the Live Copy branch to `/b_msm_moved`.

* Live Copy: `/b`

  Is moved within the Live Copy to `/b_msm_moved`. This acts as a backup and ensures that no content is lost.

  * `lc-level-1` is not moved.

* Blueprint: `/b`

  Is rolled out to the Live Copy page `/b`.

  * `bp-level-1` is rolled out to the Live Copy.

#### After Rollout {#after-rollout}

||Blueprint After Rollout|Live Copy After Rollout|Live Copy After Rollout|Publish After Rollout|
|---|---|---|---|---|
|Value|`b`|`b`|`b_msm_moved`|`b`|
|Comment||Has the content of the blueprint page `b` that was rolled out|Has the content of the page `b` that was manually created in the Live Copy branch|No change, contains the content of the original page `b` that was manually created in the Live Copy branch and is now called `b_msm_moved`|
|Value|`/bp-level-1`|`/bp-level-1`|`/lc-level-1`|`/lc-level-1`|
|Comment|||No change|No change|

### Customized Handlers {#customized-handlers}

Customized conflict handlers allow you to implement your own rules. Using the service ranking mechanism you can also define how they interact with other handlers.

Customized conflict handlers can:

* Be named according to your requirements.
* Be developed/configured according to your requirements.
  * For example, you can develop a handler so that the Live Copy page is given precedence.
* Can be designed to be configured using the [OSGi configuration](/help/sites-deploying/configuring-osgi.md). In particular the:
  * **Service Ranking** defines the order related to other conflict handlers ( `service.ranking`).
    * The default value is `0`.

### Behavior When Conflict Handling is Deactivated {#behavior-when-conflict-handling-deactivated}

If you manually [deactivate conflict handling,](#rollout-manager-and-conflict-handling) AEM takes no action on any conflicting pages. Non-conflicting pages are rolled out as expected.

>[!CAUTION]
>
>When conflict handling is deactivated, AEM does not give any indication that conflicts are being ignored. Since in such cases this behavior must be explicitly configured, it is assumed that it is the desired behavior.

In this case the Live Copy effectively takes precedence. The blueprint page `/b` is not copied and the Live Copy page `/b` is left untouched.

* Blueprint: `/b`

  Is not copied at all, but is ignored.

* Live Copy: `/b`

  Stays the same.

#### After Rollout {#after-rollout-no-conflict}

||Blueprint After Rollout|Live Copy After Rollout|Publish After Rollout|
|---|---|---|---|
|Value|`b`|`b`|`b`|
|Comment||No change, has the content of the page `b` that was manually created in the Live Copy branch|No change, contains the content of the page `b` that was manually created in the Live Copy branch|
|Value|`/bp-level-1`|`/lc-level-1`|`/lc-level-1`|
|Comment||No change|No Change|

### Service Rankings {#service-rankings}

The [OSGi](https://www.osgi.org/) service ranking can be used to define the priority of individual conflict handlers.
