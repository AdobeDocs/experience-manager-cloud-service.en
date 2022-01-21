---
title: Accessibility in Dynamic Media
description: Learn how to work with video in Dynamic Media such as best practices for encoding videos, publishing videos to YouTube, and viewing video reports. Also learn how to add closed captioning, subtitles, or chapter markers to videos.
contentOwner: Rick Brough
topic-tags: introduction
content-type: reference
feature: Accessibility
role: Admin,User
exl-id: f8d2dcbf-f61a-4b27-a3fc-406e3662adcb
---
# Accessibility in Dynamic Media {#accessibility-in-dm}

Dynamic Media supports keyboard control and assistive technologies, such as JAWS and NVDA screen readers, across the authoring user interface.

## Keyboard accessibility support in Dynamic Media {#keyboard-support-in-dm}

Because Dynamic Media is a plug-in to [!DNL Experience Manager Assets], most of the keyboard control behavior is the same as in [!DNL Experience Manager Assets]. For example, the `Cancel` button in Dynamic Media has the same focus highlight as in [!DNL Experience Manager Assets]. It also reacts to the `Spacebar` key as in [!DNL Experience Manager Assets]. See [keyboard shortcuts in Assets](/help/assets/accessibility.md#keyboard-shortcuts).

Keystrokes supported by Individual user interface elements in Dynamic Media are-in most cases-obvious and easy to find. Keyboard control in Dynamic Media is about the following:

* Ability to use `Tab` and `Shift+Tab` keystrokes to navigate between interactive elements on the page.
Using `Tab` advances input focus to the next user interface element in the tabbing order; using `Shift+Tab` brings input focus back to the previous user interface element. 
The focus traversal follows the natural user interface element location on the screen and moves in a left-to-right, then top-to-bottom order. In addition, if any field has an error, you can press `Tab` to move the focus to it.
* Ability to use the `Spacebar` and `Enter` key to activate standard user interface elements, such as buttons and drop-down lists.
* Ability to see the keyboard focus highlight on the active element. The user interface element that has input focus received a visual focus indication as a border rendered around the user interface element.
* In the Hotspot editor, you can use some custom keystrokes, such as arrow keys, to interact with complex user interface elements to reposition hotspots. 
* In the Interactive Video editor, you can use the `Spacebar` to select an image and add it to a segment. In addition, you can use the `Backspace` key to delete the selected item from the **[!UICONTROL Content]** tab. Also, pressing `Tab` functions as desired to navigate between interactive elements on the page.
* In the Image Crop/Smart Crop editor, you can do the following:
  * Use arrow keys to crop the frame size, or reposition the image, or both.
  * The first `Tab` stop highlights the entire image frame. You can then use arrow keys on the keyboard to reposition the frame.
  * The next four `Tab` stops are the frame's four corners. When focus is placed on a frame corner, the corner is highlight. Again, you can use arrow keys on the keyboard to move the focused corner.
  See [Editing the smart crop or smart swatch of a single image](/help/assets/dynamic-media/image-profiles.md#editing-the-smart-crop-or-smart-swatch-of-a-single-image)

<!-- Keyboarding is the same because Dynamic Media is using the same UI library (Coral 3 (Experience Manager 6.5) or Coral Spectrum (in Skyline)) as entire Experience Manager Assets.  -->

<!-- In the Hotspot editor, Dynamic Media lets you use arrow keys to control the position of a hot spot. See [Carousel Banners](/help/assets/dynamic-media/carousel-banners.md##adding-hotspots-or-image-maps-to-an-image-banner) or [Interactive Images](/help/assets/dynamic-media/interactive-images.md#adding-hotspots-to-an-image-banner)  --> 

 <!-- I think we should definitely mention this in the DM-specific area of documentation for keyboard support. -->

<!-- I would not get into much of details of specific keyboard support logic of these editors. One of the reasons - chances are that accessibility support will receive Phase2-like attention, with more holistic approach. -->

## Assistive technology support in Dynamic Media {#assistive-technology=support-for-dm}

Dynamic Media user interface elements work with assistive technologies such as screen readers. For example, it recognizes landmarks on a page when you navigate landmarks using keyboard shortcut `D` or regions using keyboard shortcut `R`. It also narrates the heading when navigating using the heading keyboard shortcut `H`.

## Keyboard accessibility support in Dynamic Media viewers {#keyboard-accessibility-for-dm-viewers}

All out-of-the-box Dynamic Media viewers components support keyboard accessibility for your customers.

See [Keyboard accessibility and navigation](https://experienceleague.adobe.com/docs/dynamic-media-developer-resources/library/c-keyboard-accessibility.html) in the Dynamic Media Viewers Reference Guide.

## Assistive technology support in Dynamic Media viewers {#assistive-technology=support-for-dm-viewers}

All Dynamic Media viewer components support ARIA (Accessible Rich Internet Applications) roles and attributes to improve integration with assistive technologies such as screen readers.
See the **Assistive technology support** Help topic in any customizing viewer topic in the Dynamic Media Viewers Reference Guide. For example, see [Assistive technology support](https://experienceleague.adobe.com/docs/dynamic-media-developer-resources/library/viewers-aem-assets-dmc/video/r-html5-video-viewer-20-assistive.html) for the Video viewer, or [Assistive technology support](https://experienceleague.adobe.com/docs/dynamic-media-developer-resources/library/viewers-for-aem-assets-only/interactive-images/c-html5-aem-interactive-image-assistive.html#viewers-for-aem-assets-only) for the Interactive Image viewer.

## Closed caption support in [!DNL Dynamic Media] {#closed-caption-support}

Dynamic Media supports the delivery of videos and adaptive video sets with closed captioning. The captions must be displayed on top of the video content.

See [Video in Dynamic Media - Add closed captions or subtitles to video](/help/assets/dynamic-media/video.md#adding-captions-to-video).


>[!MORELIKETHIS]
>
>* [Accessibility for Adobe solutions](https://www.adobe.com/accessibility.html)
>* [Accessibility in Experience Manager Assets](/help/assets/dynamic-media/accessibility-dm.md)
