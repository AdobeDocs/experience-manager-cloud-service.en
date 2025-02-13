---
title: How to add Footnote to an adaptive form?
description: Use Rich Text editor (RTE) for footnotes in an Adaptive Form.
feature: Adaptive Forms, Foundation Components
exl-id: f04dae84-daab-42f8-876f-02fe426f62be
role: User, Developer
---
# Footnote Component {#footnotecomponent}

>[!NOTE]
>
> Adobe recommends using the modern and extensible data capture [Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html) for [creating new Adaptive Forms](/help/forms/creating-adaptive-form-core-components.md) or [adding Adaptive Forms to AEM Sites pages](/help/forms/create-or-add-an-adaptive-form-to-aem-sites-page.md). These components represent a significant advancement in Adaptive Forms creation, ensuring impressive user experiences. This article describes older approach to author Adaptive Forms using foundation components.

**[!UICONTROL Footnote]** is the extra bit of information or notes which appear at the end of the page. [!UICONTROL Footnote] comprises the notes that are indicated in your text with numbers as a superscript.

Footnotes are numbered sequentially in the order that they appear on the page. Each footnote has a unique number as a superscript which corresponds to the number which is placed at the bottom of the page. Next to the number appears the supplementary information as a footnote description.

![Footnote Description](/help/forms/assets/footnote_description.png)


## Usage of Footnote {#usesoffootnotes}

* Helps in providing citations. 
* Provides extra information that can interrupt the normal flow of the main information.
* Provides parenthetical information or copyright permissions.

In Adaptive Forms, [!UICONTROL footnote] is used to display the information on how to complete or use the form. For information on how to create an Adaptive Forms, see [Creating an Adaptive Form](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/create-an-adaptive-form/create-an-adaptive-form-on-forms-cs/creating-adaptive-form.html).

## Footnote in Adaptive Forms {#using-footnote-adaptiveforms}

To add footnote in Adaptive Forms, perform the following steps:
1. Open an Adaptive Form in **Edit** mode.
1. From the component browser, drag-drop the **[!UICONTROL Text]** component onto the Adaptive Form. 
1. Select the **[!UICONTROL Text]** component that you added and select ![cmppr](assets/configure-icon.svg) to edit its properties.

    ![Footnote in Adaptive Forms](/help/forms/assets/footnote_rte.png)

1. Select the text for which you want to add a footnote description  and click  ![star](/help/forms/assets/asterisk.svg) button to style the **[!UICONTROL Footnote]** component.

1. Click ![check](/help/forms/assets/save_icon.svg) to save the changes and styles.

    >[!NOTE]
    >
    >* Footnotes are numbered automatically and appear in a manner they are created on the Adaptive Form.
    >* If there are duplicate footnotes, then numeration is same for all the duplicate footnotes. 

1. From the component browser, drag-drop the **[!UICONTROL Footnote Placeholder]** component onto the Adaptive Form.
    >[!NOTE]
    >
    >* At the publish instance, footnotes are displayed at the position where **[!UICONTROL Footnote Placeholder]** component is placed onto the Adaptive Form.  
    >* When you navigate between different panels, only visible footnotes appear in the **[!UICONTROL Footnote Placeholder]** that are present within the navigated panel.

1. Save the properties.

At runtime, number appears on the text as a superscript and its corresponding description appears in the **[!UICONTROL Footnote]** component at the position where [!UICONTROL Footnote Placeholder] is placed on the Adaptive Form. You can directly navigate to the footnote description by clicking its corresponding number on the [!UICONTROL Footnote].


## See Also {#see-also}

{{see-also}}