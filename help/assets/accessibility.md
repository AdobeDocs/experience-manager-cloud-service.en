---
title: Accessibility in [!DNL Experience Manager Assets].
description: Know how accessibility features in [!DNL Adobe Experience Manager] as a Cloud Service help disabled users.
contentOwner: AG
---

<!--
Original scope of this article for Core Assets for all a11y topics is around the following topics. This has changed since then but keeping this list of topics for posterity's sake.

* Convert the absolute doc links to relative links.
* Add an overview
* Compile a list of enhancements done in the last ~1 year.
* Top-level actions supported, such as clickable UI elements, keyboard shortcuts, popup dialogs, etc.)
* Specific user tasks supported, such as, download assets, datepicker, editing metadata, etc.
* Support matrix of user tasks with browsers and screen readers + OSes combinations
* Exceptions that users should be aware of.
* CTA – what is next and more info from AEM team
  * Link to ACRs on a.com.
  * Generic a11y info by Adobe to begin with.
  * Examples of other a11y DX Docs from Elle.
  * Link to a11y-specific channels to report issues, seek support, or request enhancements, if any. Available info from Elle.
-->

# Accessibility in [!DNL Adobe Experience Manager Assets] as a Cloud Service {#accessibility-in-aem-assets}

Adobe is committed to make products for all users, including people with disabilities. [!DNL Adobe Experience Manager] is continuously enhanced to meet the needs of all types of users. [!DNL Experience Manager] publishes conformance information that details standards it adheres to, outlines the accessibility features in the product, and describes the level of compliance. It helps users understand the extent of the adherence.

[!DNL Adobe Experience Manager] provides varying levels of support for the following standards:

* [Web Content Accessibility Guidelines (WCAG) 2.1](https://www.w3.org/TR/WCAG/).
* [Revised Section 508](https://www.access-board.gov/guidelines-and-standards/communications-and-it/about-the-ict-refresh/final-rule/text-of-the-standards-and-guidelines).
* [WAI-ARIA](https://www.w3.org/WAI/standards-guidelines/aria/).
* [EN 301 549](https://en.wikipedia.org/wiki/EN_301_549).

To access the report detailing the levels of compliance, see [Accessibility conformance reports ](https://www.adobe.com/accessibility/compliance.html) (ACR) page for all Adobe solutions.

## Assistive technologies to use {#at-support}

Users with disabilities frequently rely on hardware and software to access web content. These tools are known as assistive technologies. [!DNL Adobe Experience Manager Assets] work with the following assistive technologies to let users use the core functionalities:

* Screen readers.
* Speech recognition software.
* Keyboard usage – navigation and shortcuts.
* UI magnifying tools.

## [!DNL Experience Manager Assets] use cases that are accessible {#accessible-assets-use-cases}

In [!DNL Experience Manager], the accessibility features address two key requirements of [!DNL Experience Manager] users and their customers.

For content designers and creators, there are features to create and publish accessible content that is used in turn by their customers and website visitors. The content can be used by individuals with disabilities with the help of assistive technologies. For details, see [web accessibility guidelines](/help/onboarding/accessibility/web-accessibility.md).

Also, [!DNL Experience Manager] lets its users and administrators with disabilities access user interface and controls to create and manage content. The individual with disabilities can use assistive technologies to navigate, use, and manage the [!DNL Assets] capability.

The core features in [!DNL Assets] are more accessible than before and are regularly updated to improve compliance with global standards. The CRUD operations in Assets have some degree of accessibility built into those. DAM workflows like adding, managing, searching, and distributing assets are accessible with the help of keyboard shortcuts, screen reader text, color contrast, and so on.

## Support for use of keyboard {#keyboard-use}

Many user interface elements that are clickable or actionable with a pointer can also be engaged with using keyboard. Using a keyboard, users can focus upon UI elements and take an appropriate action. Users can directly use keyboard shortcuts to trigger a command or an action without having to focus on UI elements and trigger it using keyboard. For example, users can open the timeline of an asset in the left side by browsing to the UI control using a keyboard and pressing Return and by pressing `alt + 2` keyboard shortcut.

<!-- TBD items:

* The button/menu to toggle between list view and card view exposes relevant info to the screen readers. What about column view option? This info can go into ‘basic handling’ info aka article to ‘understand and use the workspace’.
* How to open and browse through the profile popup dialog in [!DNL Experience Manager] UI using a keyboard? The navigation does not match the order of visual display of options on the UI. This info can go into ‘basic handling’ info aka article to ‘understand and use the workspace’. What about setting preferences and impersonating a user?
* Using the [!DNL Experience Manager] tag browser and operating the buttons like delete tag? This info can go into ‘basic handling’ info aka article to ‘understand and use the workspace’.
* Read-only form fields can be focused with the keyboard. Can users tab to these fields to understand the contents and are they able to copy text from the fields?
-->

### Keyboard shortcuts in Assets {#keyboard-shortcuts}

<!-- TBD: Add here only those keyboard shortcuts that work for/with Assets. Do with Oct release. File Jira.
-->

Most keyboard shortcuts that apply to [!DNL Experience Manager] consoles also apply to Assets. See [Keyboard Shortcuts for Consoles](https://docs.adobe.com/content/help/en/experience-manager-65/authoring/essentials/keyboard-shortcuts.html). See [enable or disable the keyboard shortcuts](/help/sites-cloud/authoring/getting-started/keyboard-shortcuts.md).

## Sign in and navigate [!DNL Assets] user interface {#login}

Users can use keyboard to navigate to and fill in the sign in field to log in. After logging in, DAM users can navigate to [!DNL Assets] user interface using keyboard.


## Browse existing assets and view related information {#browse}

In the [!DNL Assets] user interface, users can use keyboard to browse through the list of existing digital assets in DAM repository.

* Preview the asset itself.
* List view and card view.
* Insights view.
* See the generated renditions.
* See timeline and versions.
* See comments on an asset.
* View metadata.

When browsing the assets repository, the following functionality improves accessibility:

* Users can access and focus the interactive user interface options in References list of assets using keyboard keys.
* The elements in each row in list view are announced as the elements of the same row by screen readers.
* User focus when navigating using `Tab` key can move to the close option in version preview.


Initiate asset [search](#search).


## Add and upload digital assets {#upload}

## Configure and administer Assets {#config-admin}

<!-- 
* List the a11y fixes in workflows to configure and administer [!DNL Experience Manager Assets]?
* Some enhancements in Processing profiles creation or application to a folder?
* Some enhancements to metadata properties UI?
-->

## Manage digital assets {#manage-assets}

* Download an asset.
* Add metadata.
* Collections related.
* Date picker popup dialog can be used using a keyboard. Datepicker is used to set on-times and off-times.
* To manage metadata, can users browse through all the options on the Properties page?
* Other metadata-related enhancements?

For metadata operations, the following product behavior improves accessibility:

* Screen readers now announce the options to delete the selected tags in Basic tab of asset Properties buttons to delete the selected tags.

## Search digital assets {#search}

Being able to quickly search the relevant assets, boosts the content velocity. The content velocity use cases are are part of core [!DNL Assets] functionality. Search use case is accessible in the following ways:

* Users search for assets from within the Omnisearch bar. Use either the keyboard keys or the keyboard shortcut `/` to access Omnisearch bar.
* Start typing the search keyword and use keyboard to select the auto-suggestions. Press the Return key to accept an auto-suggested string and search assets for it.
* Screen readers can identify and announce the mixed state checkboxes (in which unless you select all the nested predicates the first-level checkboxes are not selected and are stricken through) in Filters panel when filtering search results.

When filtering search results:

* Search result page has an informative titles for better understanding of screen reader users.
* A screen reader announces the options in search filter as expandable accordions.
* Predicates that have mixed-state buttons are announced by screen readers.

* User focus now correctly moves to search icon after Omnisearch is closed.

## Accessible documentation {#accessible-docs}

[!DNL Experience Manager] provides accessible documentation that can be consumed by people with disabilities. The following helps make the content offering accessible right now, while Adobe continues to improve the platform and the content:

* Screen readers can read the text.
* Images and illustrations have alt text available.
* Keyboard navigation is possible.
* Contrast ratios help highlight some parts of the documentation website.

<!-- 
## More resources for accessibility {#a11y-resources}

TBD: If anyone is aware of AEM-specific resources that help users leverage any accessibility features or use any assistive technology with AEM, please share or leave a link here.
-->

## Enhancements in Experience Manager Assets releases {#rn-fixes}

For a list of enhancements done in each release, see the [release notes](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/release-notes/home.html) of the individual releases.

>[!MORELIKETHIS]
>
>* [AEM accessibility guidance](/help/onboarding/accessibility/web-accessibility.md)
>* [Conformance reports for Adobe solutions](https://www.adobe.com/accessibility/compliance.html)
>* []().

<!-- <!-- TBD: Just listing the RN enhancements here too for the sake of collating in this article. Remove this section later.


•	Search page and search result page now have more informative titles for better understanding of screen reader users (NPR-34093). 
•	Screen readers now announce the options to delete the selected tags in Basic tab of asset Properties buttons to delete the selected tags (NPR-33972). 
•	The elements in each row in list view are now correctly announced as the elements of the same row by screen readers (NPR-33932). 
•	User focus when navigating using Tab key now correctly moves to the close option in version preview (NPR-33863). 
•	User focus now correctly moves to search icon after Omnisearch is closed (NPR-33705). 
•	The actionable user interface options now have more prominent visual focus with enhanced contrast when focused using keyboard keys. Therefore, sighted keyboard users can now differentiate the focused areas (NPR-33542). 
•	The drag functionality using keyboard now correctly functions in Metadata Schema Editor in browse mode of screen reader (CQ-4296326). 
•	In the link sharing dialog, when navigating in browse mode, the screen readers, 
o	now do not narrate the table information as soon as the dialog is loaded. 
o	can navigate to all the listed auto-suggestions. 
o	now narrate the displayed auto-suggestions for the Add Email Address/Search (CQ-4294232). 
•	Use of the Esc key to remove the quick action icons from thumbnail view no longer removes keyboard focus from the last focused item (CQ-4293554). 
•	Screen reader now announces text alternatives, which depict their functionality, for icons (such as chevrons) instead of their literal names (CQ-4272943). 
•	Keyboard focus now successfully moves to Flyout, InlineZoom, Shoppable_Banner, Zoom_dark, Zoom_light, ZoomVertical_dark, and ZoomVertical_light options when navigating using keyboard Tab key in asset details Viewers in Dynamic Media (CQ-4290605). 
•	Save & Close option on asset Properties page can now be accessed using keyboard keys (NPR-34107). 
•	Error messages due to incorrect username and password combinations on login page are now announced by screen readers each time the error occurs (NPR-33722). 
•	In Experience Manager header section, when navigating in browse mode, screen reader now announces, 
o	auto edited suggestions in Type to search in Omnisearch. 
o	the state as expanded or collapsed for Solutions, Help, Inbox and User options. 
o	the Searching Help status message that is displayed when user enters a search string in Search for Help field under Help option
o	the error message if incorrect value is entered in Impersonate as field under User option and focus correctly moves to the text field (NPR-33804).

•	User can now move focus using keyboard keys within: 
o	Search/Add Email Address field in Link Sharing dialog. 
o	Add User or Group field under Closed User Group in Permissions tab of folder Properties (NPR-34452). 

•	GRANITE-28726 - This was a keyboard accessibility issue where if user quits omnisearch focus wasn't moving to the search button again.
•	CQ-4300021 - Having selected an asset in Assets UI, pressing `alt + 4` (existing shortcut combination) opens References in the left panel. Tabbing through, navigates through the none zero reference entries, across assets, sites, forms, livecopies, etc.
•	CQ-4294530 - This was platform issue which assets team fixed. Updated search result page title(<title>) to "Location: Assets | AEM Search". The word 'Assets' in the title can be Sites, Experience Fragments etc. based on search location.
•	CQ-4293591 - Not a bug.
•	CQ-4293383 - The bug was no longer applicable when we moved the userpicker in link share dialog to use foundation-autocomplete. Unlike foundation-userpicker, foundation-autocomplete does not have a down chevron icon.
•	CQ-4293363 - 
•	On any page in AEM, navigate to the icons on the shell menubar in the browse mode of NVDA -
1. While navigating through the items in the menu bar, each item should be properly announced by NVDA.
2. Press enter on Search icon. NVDA should announce ""type to search"" so that user knows they are in the search field and can start typing string(s) to search.
3. All the shell menubar items should correctly announce their state when they are expanded by pressing enter key and collapsed by pressing escape key.
4. When inside Help menu in shell menubar, typing any string to search reveals a spinner until the search results are fetched. The users should be indicated that search is in progress by announcing "Searching help".
5. Pressing enter on User button in shell menubar opens the dialog where users can impersonate the logged in user. However, pressing Ok button without selecting any user to impersonate shows an error message asking user to type in a userID to impersonate. This error message should be correctly announced for screen reader users."
•	CQ-4282133 - Close button in a coral-dialog wasn't accessible through keyboard, due to which user cannot trigger close button through keyboard press in version preview dialog. After fix, user can close dialog through close button using keyboard.
•	CQ-4281109 - No documentation update required
•	CQ-4281110 - Screen reader not interpreting 'Enter path', 'Select tag(s)' edit field and the 'Open Selection Dialog' button correctly
•	Combobox has now implemented the 1.2 of the WAI-ARIA ComboBox design pattern.
•	CQ-4273122 - Assets of video/audio type will have aria-label in format "Multimedia player: <Title>" so users relying on screen-reader will get to know that they are video/audio assets.
•	CQ-4273120 - No documentation update required as there is no effect on the UI. It was more like a "best practice" issue.
•	CQ-4273103 - No effect on UI. This issue was to improve screenreader accessibility of coral-accordion component.
•	CQ-4273029 - No effect on UI. This issue was to fix screenreader accessibility of "Save" , "Save and Close" button metadata editor page. We have fixed role and other accessibility attribute such as aria-label etc.
•	CQ-4273028 - No update required
•	CQ-4273025 - No documentation update required
•	CQ-4273015 - 
•	Changes roles for steplist in accordance to accessibility standards. This was changed in coral component, changes will be visible across platform areas wherever steplist component is used
•	Voice over will announce the state of the steps (i.e completed , current , not complete).
•	Each coral-step should have role="listitem", with aria-setsize set to the total number of coral-steps in the coral-steplist, and aria-posinset set to the index position of each coral-step within the coral-steplist. These list items are not interactive and should not have a tabindex attribute.
•	Each coral-step should have as its child an a[href] or an element with [role="link"][tabindex="0"] that will receive focus and display the focused style.
•	No documentation update required"
•	CQ-4272954 - On AEM login page, previously "Incorrect username/password" error is announced only once. With the fix this error is announced on each invalid login attempt.
•	CQ-4272943 - Adds appropriate role and text to previous and next buttons in case of Asset details page, Adds role and text option to inbox icon present at top of page, adds role and text option to insight elements including usage count, click count, impression count.
•	CQ-4271825 - This is a feature enhancement to introduce 'row headers' for coral-table rows. In list view, Name column of asset is treated as row headers. When user is navigating to different cells in list view through keyboard, row header(asset name) is announced along with cell value to indicate row/asset correspondence.
•	CQ-4271712 - 
•	Start workflow and Save as version actions visible in Assets UI, when an asset is selected, is now accessible by keyboard, tabbing through the form elements.
•	Comments in the asset timeline are now accessible by keyboard, by tabbing through them
•	View Settings in Assets UI is now accessible by keyboard. User can navigate through the available card sizes using arrow keys, and select and tab through to navigate through and set other elements in the existing View Settings view."

-->
