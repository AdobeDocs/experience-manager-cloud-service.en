---
title: Customizing Adaptive Form themes using the Theme Editor
description: Learn how to use the Theme Editor to create and customize visual themes for Core Component-based Adaptive Forms in Adobe Experience Manager.
feature: Adaptive Forms, Core Components
role: User, Developer
---

# Customizing Form Themes {#customizing-form-themes}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-advanced-authoring/themes.html)                  |
| AEM as a Cloud Service     | This article        |

The Theme Editor in Adobe Experience Manager (AEM) Forms is a visual interface that lets you create and customize themes for your Adaptive Forms without writing code manually. A theme defines the look and feel of form components and panels, including background colors, font styles, borders, dimensions, and spacing. When you apply a theme, the specified styles reflect on the corresponding components, and you can reuse the same theme across multiple Adaptive Forms.

The Theme Editor eliminates the need for a dedicated developer persona for basic form styling. With just a working knowledge of CSS, you can style forms using the visual sidebar or write advanced CSS overrides directly within the editor.

>[!NOTE]
>
> The Theme Editor is applicable **only** for Core Component-based Adaptive Forms. When selecting a form for preview, ensure that you choose a Core Component-based Adaptive Form.

## Prerequisites {#prerequisites}

* Author-level permissions in Adobe Experience Manager Forms.
* Basic understanding of CSS styling principles. For a complete CSS reference, see the [MDN Web Docs CSS reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference).

## Navigate to the Themes Directory {#navigate-to-themes}

1. Log in to your AEM author instance.
1. Navigate to **[!UICONTROL Adobe Experience Manager]** > **[!UICONTROL Forms]** > **[!UICONTROL Themes]**.

   The Themes directory displays all available themes, including any standard themes provided by AEM Canvas, along with custom themes that you or your organization have created.

### Create a new theme {#create-a-new-theme}

1. In the Themes directory, select the folder where you want to store your new theme.
1. Click **[!UICONTROL Create]** > **[!UICONTROL Theme]**.

   ![Create new Theme](/help/forms/assets/custom-theme-create.png)

1. In the **[!UICONTROL Create Theme]** dialog, specify the following details:
   * **[!UICONTROL Title]**: A descriptive title for the theme.
   * **[!UICONTROL Name]**: The node name for the theme.
   * **[!UICONTROL Adaptive form to preview the theme]**: Select a Core Component-based Adaptive Form to act as the preview canvas for your theme, or click **[!UICONTROL Use default adaptive form]** to use the default form. This form is loaded in the Theme Editor canvas so you can see your styling changes in real time while editing.
   * **[!UICONTROL Description]** *(Optional)*: A brief description of the theme.
   * **[!UICONTROL Configuration Container]** *(Optional)*: The configuration container that holds Adobe Font configuration details.
   * **[!UICONTROL Tags]** *(Optional)*: Tags attached to the theme for identification and search.
1. Click **[!UICONTROL Create]**.

   ![configuring custom theme](/help/forms/assets/custom-theme-name.png)

   The theme is created. You can now click **[!UICONTROL Edit]** to open it in the Theme Editor.

### Edit an existing theme {#edit-an-existing-theme}

1. In the **Themes** directory, select the theme you want to modify.
1. Click **[!UICONTROL Edit]** in the action bar to open the theme in the Theme Editor.

   ![Editing a theme](/help/forms/assets/custom-theme-edit.png)

### Upload a theme {#upload-a-theme}

You can import a theme package (for example, one exported from another environment) into the Themes directory:

1. In the **Themes** directory, click **[!UICONTROL Create]** > **[!UICONTROL File Upload]**.
1. Browse to select the theme package (ZIP file) on your computer, then click **[!UICONTROL Upload]**.

   ![Upload theme - Create menu with File Upload option](/help/forms/assets/custom-theme-upload.png)

The uploaded theme appears in the Themes directory and can be edited like any other theme.

### Download a theme {#download-a-theme}

You can export a theme as a package (ZIP file) to reuse in another AEM Forms environment or to back it up:

1. In the **Themes** directory, select one or more themes (use the checkboxes on the theme cards).
1. Click **[!UICONTROL Download]** in the action bar. A dialog may appear with details of the selected theme(s).
1. Confirm or click **[!UICONTROL Download]** in the dialog. The theme package is downloaded as a ZIP file to your computer.

   ![Download theme - select theme and click Download](/help/forms/assets/custom-theme-download.png)

You can upload this ZIP later using [Upload a theme](#upload-a-theme) in the same or another environment.

## Understand the Theme Editor interface {#understand-the-theme-editor}

When you open a theme in the Theme Editor, you see two main areas:

* **Canvas** (right side): Displays a preview of the Adaptive Form linked to the theme. All styling changes reflect here instantly, so you can see the impact of your edits in real time.
* **Sidebar** (left side): Contains the **Selectors** panel that lists all stylable form components in a tree structure, such as Page, Form, Field, Button, Panel, Image, hCaptcha, and reCaptcha.

![Theme Editor](/help/forms/assets/custom-theme-editor.png)

### Canvas toolbar and Theme Options {#canvas-toolbar}

The Theme Editor gives you controls in two places: the **toolbar above the canvas** (for view and theme-level actions) and the **bottom of the left sidebar** (for previewing states). Use them in this order as you work.

**1. Toolbar above the canvas**

From left to right, the toolbar provides:

* **Toggle Side Panel**: Show or hide the Selectors sidebar. Use this to maximize the form preview area when you want to focus on the canvas, or show the sidebar again when you need to select or style components.
* **Emulator**: Select a device or breakpoint (for example, Desktop, Tablet, or Mobile) to preview the form at that screen size. The form preview resizes to match the selected breakpoint. Any styles you set while a breakpoint is selected apply only to that breakpoint, so you can define responsive styles. For details, see [Styling for different screen sizes](#styling-for-different-screen-sizes).
* **Undo / Redo**: Revert or reapply your last styling changes. Useful if you try a style and want to step back without losing other edits.
* **Theme Options** (dropdown): Opens a menu with four options. Click it when you need to change the preview form, view CSS, manage saved styles, or get in-editor help.

   ![Theme Editor canvas toolbar with Toggle Side Panel, Emulator, Undo, Redo, and Theme Options](/help/forms/assets/custom-theme-toolbar-utilities.png)

**2. Theme Options menu (four options)**

When you open the Theme Options dropdown, you see:

![The Theme Options dropdown showing Configure, View Theme CSS, Manage Styles, and Help](/help/forms/assets/custom-theme-configure.png)

* **[!UICONTROL Configure]**: Switch the form shown in the canvas to a different Adaptive Form. Use this to check how your theme looks on another form without leaving the editor.
   ![Configure Adaptive Form for theme Preview](/help/forms/assets/custom-theme-switch-af.png)
* **[!UICONTROL View Theme CSS]**: Open a dialog with the full compiled CSS for the theme. To see CSS for only the currently selected component, use **[!UICONTROL View CSS]** in the sidebar instead (handy for debugging or copying rules).
   ![View Final CSS](/help/forms/assets/custom-theme-view-css.png)
* **[!UICONTROL Manage Styles]**: Open the dialog to save, name, and reuse text and image styles. Saved styles can be applied to other components; recently used styles may also appear for quick reuse.
* **[!UICONTROL Help]**: Start the image-guided tour of the Theme Editor.

**3. Bottom of the sidebar: Simulate Error and Simulate Success**

When you style components by state (for example, Error or Success), you can preview that look without submitting the form. In AEM Forms as a Cloud Service, **Simulate Error** and **Simulate Success** are available at the **bottom of the left sidebar**. Scroll down in the sidebar if you don’t see them; they appear when you have a component selected and let you toggle the preview to match the Error or Success state.

* **Simulate Error**: Show the form as if a field failed validation, so you can see your **[!UICONTROL Error]** state styling.
* **Simulate Success**: Show the form as if validation passed, so you can see your **[!UICONTROL Success]** state styling.

Toggle these on or off as you adjust styles for each state. For more on styling by state, see [Style by component state](#style-by-state).

### Style a Component

You can select a component to style in two ways:
* **From the Canvas**: Click directly on a component in the form preview (for example, a text field, button, or drop-down). The selected element is highlighted with a border, and a component label (for example, "Text Input Widget") appears above it. The styling options for that component appear in the sidebar.

   ![Edit theme from canvas](/help/forms/assets/custom-theme-field-level.png)

* **From the Selectors panel**: Use the tree structure in the left sidebar to drill down into specific components. For example, expand **[!UICONTROL Field]** > **[!UICONTROL Widget]** > **[!UICONTROL Text Input]** to target the textbox widget specifically.

   ![Edit Theme from the Selector panel](/help/forms/assets/custom-theme-selector.png)

#### Apply styles to a component {#apply-styles-to-a-component}

Once a component is selected, the sidebar displays the available styling properties organized into the following categories:

* **[!UICONTROL Dimensions & Position]**: Control alignment, size, padding, margin, width, height, and Z-index.
* **[!UICONTROL Text]**: Configure font family, weight, color, size, line height, alignment, letter spacing, text decoration, and transform. For a complete list of supported CSS text properties, see the [MDN CSS Text documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_text).
* **[!UICONTROL Background]**: Set a background color, image, or gradient. See [MDN CSS Backgrounds documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_backgrounds_and_borders).
* **[!UICONTROL Border]**: Define border width, style, radius, and color.
* **[!UICONTROL Effects]**: Add opacity, blend modes, and shadows.

To apply a style:

1. Select the component from the canvas or the Selectors panel.
1. Set the desired visual properties in the sidebar. For example, choose a **[!UICONTROL Background Color]** and adjust the **[!UICONTROL Font Color]**.
1. Click the checkmark icon **[!UICONTROL OK]** to confirm the property change.

   ![Applying style](/help/forms/assets/custom-theme-applying-style.png)

#### Style by component state {#style-by-state}

Components can have different visual states (for example, default, focus, hover, disabled, error, success). You can style each state separately so the form looks correct during user interaction and validation.

1. Select the component from the canvas or the Selectors panel.
1. In the sidebar, use the **[!UICONTROL State]** dropdown to choose the state you want to style (for example, **[!UICONTROL Default]**, **[!UICONTROL Focus]**, **[!UICONTROL Hover]**, **[!UICONTROL Disabled]**, **[!UICONTROL Error]**, or **[!UICONTROL Success]**).
1. Set the styling properties (Background, Border, Text, and so on) for that state.
1. Click **[!UICONTROL OK]** to confirm.

   ![State dropdown in sidebar for styling Default, Focus, Error, Success, and other states](/help/forms/assets/custom-theme-state-dropdown.png)

The styles you define apply only when the component is in the selected state. For example, if you set a red border and red background for the **[!UICONTROL Error]** state, the field shows that styling when validation fails. If your environment supports it, use **Simulate Error** or **Simulate Success** at the bottom of the sidebar to preview how the component looks in those states without submitting the form.

#### Styling for different screen sizes {#styling-for-different-screen-sizes}

You can define different styles for different device breakpoints (for example, desktop, tablet, mobile) so your theme is responsive.

1. In the canvas toolbar, use the device/emulator icons or the breakpoint selector to choose a breakpoint (for example, Desktop, Tablet, or Mobile).
1. With that breakpoint selected, use the sidebar to set or adjust styles. The styles apply only for the selected breakpoint.
1. Switch to another breakpoint and define styles for it as needed.
1. Click **[!UICONTROL OK]** and save the theme when finished.

   ![Device breakpoint selector and emulator in Theme Editor](/help/forms/assets/custom-theme-breakpoints.png)

The same theme can therefore have different spacing, font sizes, or layout-related styles per breakpoint, matching the [AEM 6.5 Theme Editor behavior](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-advanced-authoring/themes.html) for responsive styling.

### Form-level styling {#form-level-styling}

Form-level styling applies a style broadly to all components of the same type. For example, if you select **[!UICONTROL Field]** in the **Selectors** panel and set a background color to blue, every field in the form (text boxes, numeric boxes, date pickers, and drop-downs) inherits that blue background.

**Example:** To set a uniform background color on all fields in the form:

1. In the **Selectors** panel, select **[!UICONTROL Field]**.
1. In the sidebar, set the **[!UICONTROL Background Color]** to blue.
1. Click **[!UICONTROL OK]**.

   ![Form Level Styling](/help/forms/assets/custom-theme-form-level-styling.png)

All field components in the form now display a blue background.

### Component-level styling {#component-level-styling}

Component-level styling targets a specific component type, overriding any broader form-level style. For example, if you want only the Textbox widget to have a different background color while all other fields remain blue, you target the textbox widget specifically.

**Example:** To set a green background and purple font on only the textbox widget:

1. In the Selectors panel, expand **[!UICONTROL Field]** > **[!UICONTROL Widget]** > **[!UICONTROL Text Input]**.
1. Set the **[!UICONTROL Font Color]** to purple.
   ![Field level Styling](/help/forms/assets/custom-theme-field-level-styling1.png)
1. Set the **[!UICONTROL Background Color]** to green.
   ![Field level Styling](/help/forms/assets/custom-theme-field-level-styling2.png)
1. Click **[!UICONTROL OK]**.

The Textbox widget now displays a green background with purple text, while all other fields remain blue from the form-level style.

>[!NOTE]
>
> **Component-level styling always takes priority over form-level styling.** When a style is defined at both levels, the more specific component-level selector overrides the broader form-level selector. This follows standard [CSS specificity rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity). For example, if you set a blue background on all Fields (form-level) and a green background on the textbox widget (component-level), the textbox displays a green background.

## Use advanced CSS overrides {#use-advanced-css-overrides}

For styles that are not available through the visual sidebar, you can write custom CSS directly in the editor.

1. Select the component.
1. In the sidebar, expand the **[!UICONTROL Advanced]** section.
1. Write your custom CSS rules in the **[!UICONTROL CSS Override]** area. These rules override any properties set through the visual controls if there is a conflict.

For a complete CSS property reference, see the [MDN Web Docs CSS reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference).

### Add CSS pseudo-elements {#add-css-pseudo-elements}

The **[!UICONTROL Advanced]** section also supports CSS pseudo-elements such as `::before` and `::after`. These let you inject content or decorative styling around a component without modifying the form structure. For example, to add a visual indicator before a textbox component:

1. Select the component (for example, `CMP Textbox`).
1. Expand the **[!UICONTROL Advanced]** section.
1. In the `::before` pseudo-element fields, add CSS properties such as:

   ```css
   color: #B10DC9;
   ```

   ![Before CSS](/help/forms/assets/custom-theme-before-css.png)

1. In the `::after` pseudo-element fields, add CSS properties such as:

   ```css
   color: #006400;
   ```

    ![After CSS](/help/forms/assets/custom-theme-after-css.png)


These pseudo-elements follow standard CSS behavior. For a full reference, see [MDN CSS Pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements).

## Best practices {#best-practices}

* **Use the Selectors panel for precise targeting**: When styling nested elements such as a field label or a long description, use the Selectors panel on the left rather than clicking the canvas. This ensures that the correct CSS selector is generated with proper specificity.
* **Avoid assets from other themes**: When editing a theme, do not browse and add assets (such as images) from other themes. If the source theme is moved or deleted, your current theme breaks.
* **Do not change container panel layout width**: Specifying a fixed width on container panels makes them static and prevents them from adapting to different screen sizes.

## See Also {#see-also}

{{see-also}}