---
title: Configuring Segmentation with ContextHub
description: Learn how to configure segmentation using ContextHub.
---

# Configuring Segmentation with ContextHub{#configuring-segmentation-with-contexthub}

Segmentation is a key consideration when creating a campaign. See [Understanding Segmentation](segmentation.md) for information on how segmentation works and key terms.

Depending on the information you have already collected about your site visitors and the goals you want to achieve, you will need to define the segments and strategies needed for your targeted content.

These segments are then used to provide a visitor with specifically targeted content. [Activities](activities.md) defined here can be included on any page and define which visitor segment the specialized content is applicable for.

AEM allows you to easily personalize your users' experiences. It also allows you to verify the results of your segment definitions.

## Accessing Segments {#accessing-segments}

The [Audiences](audiences.md) console is used to manage segments for ContextHub as well as audiences for your Adobe Target account. This documentation covers managing segments for ContextHub.

To access your segments, in global navigation select **Navigation &gt; Personalization &gt; Audiences**.

![Managing audiences](/help/sites-cloud/authoring/assets/contexthub-segmentation-audiences.png)

## Segment Editor {#segment-editor}

<!--The **Segment Editor** allows you to easily modify a segment. To edit a segment, select a segment in the [list of segments](/help/sites-administering/segmentation.md#accessing-segments) and click the **Edit** button.-->
The **Segment Editor** allows you to easily modify a segment. To edit a segment, select a segment in the list of segments and click the **Edit** button.

![Segment editor](/help/sites-cloud/authoring/assets/contexthub-segment-editor.png)

Using the components browser you can add **AND** and **OR** containers to define the segment logic, then add additional components to compare properties and values or reference scripts and other segments to define the selection criteria (see [Creating a New Segment](#creating-a-new-segment)) to define the exact scenario for selecting the segment.

When the entire statement evaluates to true then the segment has resolved. In the event of multiple segments being applicable, then the **Boost** factor is also used. See [Creating a New Segment](#creating-a-new-segment) for details on the boost factor.

>[!CAUTION]
>
>The segment editor does not check for any circular references. For example, segment A references another segment B, which in turn references segment A. You must ensure that your segments do not contain any circular references.

### Containers {#containers}

The following containers are available out-of-the-box and allow you to group comparisons and references together for boolean evaluation. They can be dragged from the components browser to the editor. See the following section [Using AND and OR Containers](#using-and-and-or-containers) for more information.

|||
|---|---|
|Container AND|The boolean AND operator|
|Container OR|The boolean OR operator|

### Comparisons {#comparisons}

The following segment comparisons are available out-of-the-box to evaluate segment properties. They can be dragged from the components browser to the editor.

|||
|---|---|
|Property-Value|Compares a property of a store to a defined value|
|Property-Property|Compares one property of a store to another property|
|Property-Segment Reference|Compares a property of a store to another referenced segment|
|Property-Script Reference|Compares a property of a store to the results of a script|
|Segment Reference-Script Reference|Compares a referenced segment to the results of a script|

>[!NOTE]
>
>When comparing values, if the data type of the comparison is not set (i.e. set to auto detect), ContextHub's segmentation engine will simply compare the values as javascript would. It does not cast values to their expected types, which can lead to misleading results. For example:
>
>`null < 30 // will return true`
>
>Therefore when [creating a segment](#creating-a-new-segment), you should select a **data type** whenever the types of compared values are known. For example:
>
>When comparing the property `profile/age`, you already know that the compared type will be **number**, so even if `profile/age` is not set, a comparison `profile/age` less-than 30 will return **false**, as you would expect.

### References {#references}

The following references are available out-of-the-box to link directly to a script or another segment. They can be dragged from the components browser to the editor.

|||
|---|---|
|Segment Reference|Evaluate the referenced segment|
|Script Reference|Evaluate the referenced script. See the following section [Using Script References](#using-script-references) for more information.|

## Creating a New Segment {#creating-a-new-segment}

To define your new segment:

1. After [accessing the segments](#accessing-segments), click or tap the Create button and select **Create ContextHub Segment**.

   ![Add segment](/help/sites-cloud/authoring/assets/contexthub-create-segment.png)

1. In the **New ContextHub Segment**, enter a title for the segment as well as a boost value if required and then tap or click **Create**.

   ![New segment](/help/sites-cloud/authoring/assets/contexthub-new-segment.png)

   Each segment has a boost parameter that is used as a weighting factor. A higher number indicates that the segment will be selected in preference to a segment with a lower number in instances where multiple segments are valid.

    * Minimum value: `0`
    * Maximum value: `1000000`

1. From the segments console, edit your newly-created segment to open it in the segment editor.
1. Drag a comparison or reference to the segment editor it will appear in the default AND container.
1. Double-click on or tap the configure option of the new reference or segment to edit the specific parameters. In this example, we are testing for people in Basel.

   ![Testing for people in Basel](/help/sites-cloud/authoring/assets/contexthub-comparing-property-value.png)

   Always set a **Data Type** if possible to ensure that your comparisons are evaluated properly. See [Comparisons](#comparisons) for more information.

1. Click **Done** to save your definition:
1. Add more components as required. You can formulate boolean expressions using the container components for AND and OR comparisons (see [Using AND and Or Containers](#using-and-and-or-containers) below). With the segment editor you can delete components not needed anymore, or drag them to new positions within the statement.

### Using AND and OR Containers {#using-and-and-or-containers}

Using the AND and OR container components, you can construct complex segments in AEM. When doing this, it helps to be aware of a few basic points:

* The top level of the definition is always the AND container that is initially created. This cannot be changed, but does not have an effect on the rest of your segment definition.
* Ensure that the nesting of your container makes sense. The containers can be viewed as the brackets of your boolean expression.

The following example is used to select visitors who are considered in our Swiss target group:

```text
 People in Basel

 OR

 People in Zürich
```

You start by placing an OR container component within the default AND container. Within the OR container you you can add the property or reference components.

![Segment with OR operator](/help/sites-cloud/authoring/assets/contexthub-or-operator.png)

You can nest multiple AND and OR operators as required.

### Using Script References {#using-script-references}

By using the Script Reference component, the evaluation of a segment property can be delegated to an external script. Once the script is configured properly, it can be used as any other component of a segment condition.

#### Defining a Script to Reference {#defining-a-script-to-reference}

1. Add file to `contexthub.segment-engine.scripts` clientlib.
1. Implement a function that returns a value. For example:

   ```javascript
   ContextHub.console.log(ContextHub.Shared.timestamp(), '[loading] contexthub.segment-engine.scripts - script.profile-info.js');

   (function() {
       'use strict';

       /**
        * Sample script returning profile information. Returns user info if data is available, false otherwise.
        *
        * @returns {Boolean}
        */
       var getProfileInfo = function() {
           /* let the SegmentEngine know when script should be re-run */
           this.dependOn(ContextHub.SegmentEngine.Property('profile/age'));
           this.dependOn(ContextHub.SegmentEngine.Property('profile/givenName'));

           /* variables */
           var name = ContextHub.get('profile/givenName');
           var age = ContextHub.get('profile/age');

           return name === 'Joe' && age === 123;
       };

       /* register function */
       ContextHub.SegmentEngine.ScriptManager.register('getProfileInfo', getProfileInfo);

   })();
   ```

1. Register the script with `ContextHub.SegmentEngine.ScriptManager.register`.

If the script depends on additional properties, the script should call `this.dependOn()`. For example if the script depends on `profile/age`:

```javascript
this.dependOn(ContextHub.SegmentEngine.Property('profile/age'));
```

#### Referencing a Script {#referencing-a-script}

1. Create ContextHub segment.
1. Add **Script Reference** component in the desired place of the segment.
1. Open the edit dialog of the **Script Reference** component. If [properly configured](#defining-a-script-to-reference), the script should be available in the **Script name** drop-down.

## Testing the Application of a Segment {#testing-the-application-of-a-segment}

Once the segment has been defined, potential results can be tested with the help of the **[ContextHub](contexthub.md).**

1. Preview a page
1. Click the ContextHub icon to reveal the ContextHub toolbar
1. Select a persona that matches the segment you created
1. The ContextHub will resolve the applicable segments for the selected persona

For example, our simple segment definition to identify users in Basel is based on the location of the user. Loading a specific persona that matches those criteria shows if that the segment is successfully resolved:

![Segment that resolves](/help/sites-cloud/authoring/assets/contexthub-segment-resolve.png)

Or if it is not resolved:

![Segment that doesn't resolve](/help/sites-cloud/authoring/assets/contexthub-segment-doesnt-resolve.png)

>[!NOTE]
>
>All traits are resolved immediately, though most only change on page reload.

Such tests can also be performed on content pages and in combination with targeted content and related **Activities** and **Experiences**.

If you have set up an activity and experience, you can easily test your segment with the activity. For details about setting up an activity, please see the related [documentation on authoring targeted content](targeted-content.md).

1. In editing mode of a page where you have set up targeted content, you can see that the content is targeted via arrow icon on the content.
1. Switch to preview mode and using the context hub, switch to a persona that does not match the segmentation configured for the experience.
1. Switch to a persona that does match the segmentation configured for the experience and see that the experience changes accordingly.

## Using Your Segment {#using-your-segment}

Segments are used to control the actual content seen by specific target audiences. See [Managing Audiences](audiences.md) for more information about audiences and segments and [Authoring Targeted Content](targeted-content.md) about using audiences and segments to target content.
