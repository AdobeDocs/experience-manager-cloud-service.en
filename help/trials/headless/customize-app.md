---
title: Customize Content in a Sample React App
description: Use a sample React app to learn how to customize content using the headless feature set in AEM as a Cloud Service.
hidefromtoc: yes
index: no
exl-id: 32290ad4-d915-41b7-a073-2637eb38e978
---

# Customize Content in a Sample React App {#customize-app}

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_react_app"
>title="Customize content in a sample React app"
>abstract="Your AEM headless trial comes integrated with a sample React app, which you can customize."

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_react_app_guide"
>title="Launch the Content Fragment editor"
>abstract="Your AEM headless trial comes integrated with a sample React app, so you can see how easy it is for anyone to independently manage content without development time.<br><br>Launch this module in a new tab by clicking below, then follow this guide."
>additional-url="https://video.tv.adobe.com/v/328618" text="Customize app intro video"

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_react_app_guide_footer"
>title="In this module, you learned how to customize a sample React app.<br><br>Time to market: Accelerated!<br>Development cycles: Reduced!<br><br>Now you understand how easy managing headless content is for websites and apps that are powered by AEM's headless capabilities."
>abstract=""

## Preview the App {#preview}

Clicking the **Launch the Content Fragment editor** button above opens the Content Fragment editor in a new tab.

![Content Fragment editor](assets/customize-app/content-fragment-editor.png)

The sample app provided with your AEM headless trial is powered by Content Fragments delivered via GraphQL. Use the Content Fragment editor to get familiar with the content by previewing the sample.

1. Tap or click the **Preview** button at the top-right of the editor screen.

1. The demo app opens in a new tab. The app is for the fictional WKND outdoor lifestyle brand. Click around to navigate the sample content.

   ![Demo app preview](assets/customize-app/preview-demo-app.png)

1. Return to the browser tab of the Content Fragment editor to continue.

## Edit a header in the App {#edit-app}

The Content Fragment editor displays the basic layout of the app as a page Content Fragment. The **Panels** represent different pages of the app, each of which is its own Content Fragment. By modifying these fragments, you can change the content of the app.

1. Tap or click **Mtn Biker in Canyon** in the **Panels** section.

   ![Tap Mtn Biker in Canyon fragment](assets/customize-app/mtn-biker-in-canyon.png)

1. The editor opens up the header panel of the app for the mountain biker. Each panel is made up of layers, representing different images and text that compose the experience.

   ![Panels](assets/customize-app/panels.png)

1. Select the text layer **Mtn Biker in Canyon Text Layer**. This opens the detail of the layer in the editor. The layer is made up of multiple Content Fragments that control the text that is displayed in this panel of the app.

   ![Select the Mtn Biker in Canyon Title](assets/customize-app/mtn-biker-in-canyon-text-layer.png)

1. Select the **Mtn Biker in Canyon Title** text item. This opens the Content Fragment editor.

   ![Select the Mtn Biker in Canyon Title text item](assets/customize-app/mtn-biker-in-canyon-title.png)

1. Change the text from `Your next great adventure is calling` to `Choose your own adventure`. The change is saved automatically by the editor.

1. Tap or click **Preview** at the top-right of the window to see your changes. The preview of the demo app opens in a new tab.

   ![Demo app preview](assets/customize-app/preview-demo-app-text.png)

That's how easy it is to update content within a React app when integrated into AEM headless CMS.

## Swap an image in the app {#change-image}

Now that you modified a headline in the app, try changing an image.

1. Return to the browser tab of the Content Fragment editor.

1. You need to return to the correct place in the Content Fragment editor. The breadcrumbs at the top-left of the editor show where you are in your content hierarchy. Tap or Click **Mtn Biker in Canyon** in the breadcrumbs to return to that page.

   ![Breadcrumbs](assets/customize-app/breadcrumbs.png)

1. Select the **Mtn Biking - Biker** image layer. This opens the Content Fragment editor

   ![Edit image fragment](assets/customize-app/mtn-biking-biker.png)

1. Tap or click the **X** to remove the biker image. The image disappears and the editor shows an error since the image is required data for this Content Fragment model.

   ![Image removed from fragment](assets/customize-app/mtn-biking-biker-no-image.png)

1. Tap or click **Add asset**.

1. The **Select Asset** dialog opens and the path **sample-wknd-app** &gt; **en** &gt; **image-files** is automatically selected for you.

1. Select the image `biker-yellow.png` and then tap or click **Select**.

   ![Select asset](assets/customize-app/select-asset.png)

1. The image of the biker is replaced with the selected image. The editor automatically saves the changes.

   ![Edited fragment of biker image](assets/customize-app/mtn-biking-biker-edited.png)

1. Tap or click **Preview** at the top-right of the window to see your changes. The preview of the demo app opens in a new tab. Click refresh on the browser and you should see your new biker image with yellow shorts in the app.

It's that easy to update images and assets in your apps with AEM headless CMS.

## Add a reference to a new Content Fragment in the app {#create-moment}

Now that you updated the image of the biker, let's walk through how to add new content to an app by creating and reference a new Content Fragment. You will add a product call-out managed by a "shoppable moment" Content Fragment to the second panel of the app.

![Example of a shoppable moment](assets/customize-app/example-shoppable-moment.png)

1. Return to the browser tab of the Content Fragment editor.

1. You need to return to the correct place in the Content Fragment editor. The breadcrumbs at the top-left of the editor show where you are in your content hierarchy. Tap or click **WKND Home** in the breadcrumbs to return to that page.

   ![Navigate back to the layout screen](assets/customize-app/breadcrumbs-2.png)

1. Select the **Mtn Biker on WKND Yellow** panel.

   ![Create a shoppable moment](assets/customize-app/mtn-biker-on-wknd-yellow.png)

1. Select the **Mtn Biking - Shoppable** layer.

   ![Select shoppable moment layer](assets/customize-app/mtn-biking-shoppable.png)

1. In order to create a new call-out on this panel, you must create a new shoppable moment Content Fragment. Tap or click the **+ Create new fragment** button.

   ![Add a shoppable moment](assets/customize-app/create-new-fragment.png)

1. You must first choose a model on which to base the new Content Fragment. Select the **Shoppable Moment Item** model from the **Content Fragment model** drop-down.

1. Give the Content Fragment a name. For example, enter `Shorts` into the **Name** field.

   ![Name the shoppable moment](assets/customize-app/new-content-fragment.png)

1. Tap or click **Create and open**.

1. The editor opens for your new Content Fragment.

1. Give the shoppable moment a name in the **Text** field such as `Yellow shorts`.

1. Set values for **X** and **Y**. This is where this call-out should be overlaid on the panel. Changes to the fragment are automatically saved by the editor
   * **X**: `-18`
   * **Y**: `-28`

   ![Edit the shoppable moment](assets/customize-app/edit-shoppable-moment.png)

1. Tap or click **Preview** at the top-right of the window to see your changes. The preview of the demo app opens in a new tab. Click refresh on the browser to test the positioning and make adjustments as needed in the editor.

Now you understand how creating new content and referencing it as a Content Fragment in your app can be completed without any development cycles.
