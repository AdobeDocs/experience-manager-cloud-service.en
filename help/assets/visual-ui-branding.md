Customize your [!DNL Content Hub] UI as per your brand's theme. To do the customization, navigate to your [!DNL Content Hub] home page, select the user icon in the top right corner, click **[!UICONTROL Configurations]** and select ![Branding](/help/assets/assets/ColorPalette.svg) **[!UICONTROL Branding]** on the **[!UICONTROL Configuration]** page to display **[!UICONTROL Banner]**, **[!UICONTROL Colors]** and **[!UICONTROL Banner image]** sections on the Page. Execute the following customizations from these section: 
1. [Change the banner image from [!UICONTROL Banner image] section](#Change-the-banner-image)
1. [Update the title and body text on the banner and change the text color from the [!UICONTROL Banner] section](#Add-title-and-body-text-to-your-banner-and-change-the-text-color)
1. [Change the primary and secondary color from the [!UICONTROL Colors] section](#Change-the-primary-and-secondary-color)

Select **[!UICONTROL Reset Defaults]** option to revert your changes and restore the default theme.

# Change the banner image{#Change-the-banner-image}

On the ![Branding](/help/assets/assets/ColorPalette.svg) **[!UICONTROL Branding]** page, execute the following steps to change the banner image of your [!DNL Content Hub]:

1. Click ![](/help/assets/assets/Browse.svg) **[!UICONTROL Select from gallery]** to select a banner image from the asset selector dialog box.
1. Select the image and click **[!UICONTROL Select]** to make it the header banner of your [!DNL Content Hub].

# Add title and body text to your banner and change the text color{#Add-title-and-body-text-to-your-banner-and-change-the-text-color}

Add title and body texts to your banner using the respective fields in the **[!UICONTROL Banner]** section available on the ![Branding](/help/assets/assets/ColorPalette.svg) **[!UICONTROL Branding]** page. 
Click the square box next to the **[!UICONTROL Banner text color]** to select a text color from the color picker for your banner text or specify the color's hex code in the field next to the color picker square box.

# Change the primary and secondary color{#Change-the-primary-and-secondary-color}

On the ![Branding](/help/assets/assets/ColorPalette.svg) **[!UICONTROL Branding]** page, use the **[!UICONTROL Colors]** section to set primary and secondary colors. These colors customize the background, text, and icon colors of UI elements in your [!DNL Content Hub]. The selected colors also highlight certain elements when selected.

```mermaid
graph TD
    A[Content Hub Interface] --> B[Content Hub home page]
    A --> C[Configuration Page]
    
    %% Making boxes on 3rd layer same width
    B --> D[Primary color elements                    ]
    B --> E[Secondary color elements                  ]
    
    C --> F[Primary color elements                    ]
    C --> G[Secondary color elements                  ]
    
    %% Standardizing bottom boxes with original content
    D ---->|Search &<br>Selection| H[Search bar,<br>Checkboxes,<br>Toggle switches &<br>Pane displaying asset count on selecting asset card<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]
    D ---->|Asset<br>Management| I[Add assets option on All Assets page &<br>Create collection option on Collections page<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]
    D ---->|Actions| J[Upload option,<br>Asset card selection &<br>Rendition selection<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]
    
    E ---->|Dialog<br>Elements| K[Input fields<br>Download options<br>Share options<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]
    
    F ---->|Interactive<br>Elements| L[Selected table rows<br>Toggle switches<br>Confirm options<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]
    
    G ---->|Configuration<br>Options| M[Import, Filters, Search,<br>Asset details, Branding<br>Input fields in dialog boxes<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]

    style A fill:#4682B4,color:#fff
    style B fill:#E6EEF4,color:#000
    style C fill:#E6EEF4,color:#000
    style D fill:#B0C4DE,color:#000
    style E fill:#DEB887,color:#000
    style F fill:#B0C4DE,color:#000
    style G fill:#DEB887,color:#000
    style H fill:#F0F8FF,color:#000
    style I fill:#F0F8FF,color:#000
    style J fill:#F0F8FF,color:#000
    style K fill:#FFF8DC,color:#000
    style L fill:#F0F8FF,color:#000
    style M fill:#FFF8DC,color:#000

    %% Styling for better alignment
    linkStyle default stroke-width:2px,fill:none,stroke:gray,curve
    classDef default rx:10,ry:10
```

See the following table for information on where both these colors apply:

<table style="border-collapse: separate; border-spacing: 0; width: 100%; border-radius: 8px; overflow: hidden;">
  <tr style="background-color: #4682B4;">
    <th style="padding: 12px; color: white; font-weight: bold; text-align: left;">Location</th>
    <th style="padding: 12px; color: white; font-weight: bold; text-align: left;">Color</th>
    <th style="padding: 12px; color: white; font-weight: bold; text-align: left;">UI Element</th>
    <th style="padding: 12px; color: white; font-weight: bold; text-align: left;">Navigation Path</th>
  </tr>
  <tr>
    <td rowspan="13" style="padding: 12px; border: 1px solid #d0d0d0; background-color: #E6EEF4; font-weight: bold;">[!DNL Content Hub] home page</td>
    <td rowspan="11" style="padding: 12px; border: 1px solid #d0d0d0; background-color: #B0C4DE;">Primary</td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F0F8FF;">
       <img alt="Magnifying glass icon" src="/help/assets/assets/Magnify.svg" /> Magnifying glass icon in search bar
    </td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">Across [!DNL Content Hub] home page</td>
  </tr>
  <tr>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F0F8FF;">Border color of the search bar when selected</td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">Across [!DNL Content Hub] home page</td>
  </tr>
  <tr>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F0F8FF;">
       <img alt="Selection checkboxes" src="/help/assets/assets/SelectBox.svg" /> Selection checkboxes after selection
    </td> 
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">Across [!DNL Content Hub] home page</td>
  </tr>
  <tr>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F0F8FF;">
       <img alt="Toggle switches" src="/help/assets/assets/toogle.svg" /> Toggle switches and date input fields
    </td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">[!DNL Content Hub] home page > Filters or relevant places</td>
  </tr>
  <tr>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F0F8FF;">
       <img alt="Add assets" src="/help/assets/assets/add-image.svg" /> <b>[!UICONTROL Add assets]</b> option
    </td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">[!DNL Content Hub] home page > <b>[!UICONTROL All Assets]</b></td>
  </tr>
  <tr>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F0F8FF;">
       <img alt="Create collection" src="/help/assets/assets/CollectionAdd.svg" /> <b>[!UICONTROL Create collection]</b> option
    </td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">[!DNL Content Hub] home page > <b>[!UICONTROL Collections]</b></td>
  </tr>
  <tr>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F0F8FF;">Selected asset cards</td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">[!DNL Content Hub] home page > <b>[!UICONTROL All Assets]</b>  > Select asset card</td>
  </tr>
  <tr>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F0F8FF;">Selected collection tiles</td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">[!DNL Content Hub] home page > Select <img alt="Add to collection" src="/help/assets/assets/add-circle.svg" /> available on the asset card or select <img alt="Add to collection" src="/help/assets/assets/add-circle.svg" /><b>[!UICONTROL Add to collection]</b> after selecting one or more asset cards > select the collection tile from <b>[!UICONTROL Add asset to collection]</b> dialog box. You can also click asset thumbnail > Select <img alt="Add to collection" src="/help/assets/assets/add-circle.svg" /> > select the collection tile from the panel.</td>
  </tr>
  <tr>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F0F8FF;"><b>[!UICONTROL Upload]</b> option</td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">[!DNL Content Hub] home page > <img alt="Add assets" src="/help/assets/assets/add-image.svg" /> <b>[!UICONTROL Add assets]</b> > select <b>[!UICONTROL Upload]</b> from <b>[!UICONTROL Add approved assets]</b> dialog box.</td>
  </tr>
  <tr>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F0F8FF;">Selected assets count pane</td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">[!DNL Content Hub] home page > Select asset card from <b>[!UICONTROL All Assets]</b> page or <b>[!UICONTROL Collections]</b> page.</td>
  </tr>
  <tr>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F0F8FF;"> Hovering or selecting renditions
    </td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">[!DNL Content Hub] home page > click asset thumbnail > select <img alt="Download icon" src="/help/assets/assets/download-icon.svg" />.</td>
  </tr>
  <tr>
    <td rowspan="2" style="padding: 12px; border: 1px solid #d0d0d0; background-color: #DEB887;">Secondary</td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #FFF8DC;">Input fields in dialog boxes, excluding those in the <b>[!UICONTROL Add approved assets]</b> dialog box.</td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">[!DNL Content Hub] home page > Any dialog box</td>
  </tr>
  <tr>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #FFF8DC;">Options such as, <b>[!UICONTROL Download]</b>, <b>[!UICONTROL Generate share link]</b>, 
       <img alt="Add to collection" src="/help/assets/assets/add-circle.svg" /> <b>[!UICONTROL Add to collection]</b> available in various dialog boxes.
    </td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">[!DNL Content Hub] home page > Dialog options</td>
  </tr>
  <tr>
    <td rowspan="6" style="padding: 12px; border: 1px solid #d0d0d0; background-color: #E6EEF4; font-weight: bold;">[!DNL Content Hub] [!UICONTROL configuration] page</td>
    <td rowspan="3" style="padding: 12px; border: 1px solid #d0d0d0; background-color: #B0C4DE;">Primary</td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F0F8FF;">Selected table rows</td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">[!DNL Content Hub]<b> [!UICONTROL Configuration] page</b> > Select configuration option > select row</td>
  </tr>
  <tr>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F0F8FF;">
       <img alt="Toggle switch" src="/help/assets/assets/toogle.svg" /> Toggle switches
    </td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">[!DNL Content Hub] > <b>[!UICONTROL Configuration]</b> > Toggle switches across all configuration pages.</td>
  </tr>
  <tr>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F0F8FF;"><b>[!UICONTROL Confirm]</b> option</td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">[!DNL Content Hub] > <b>[!UICONTROL Configuration]</b> > Edit dialog box on all configuration pages.</td>
  </tr>
  <tr>
    <td rowspan="3" style="padding: 12px; border: 1px solid #d0d0d0; background-color: #DEB887;">Secondary</td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #FFF8DC;">
       <img alt="Import" src="/help/assets/assets/import.svg" /> <b>[!UICONTROL Import]</b>, 
       <img alt="Filters" src="/help/assets/assets/filter.svg" /> <b>[!UICONTROL Filters]</b>, 
       <img alt="Asset details" src="/help/assets/assets/info-icon.svg" /> <b>[!UICONTROL Asset details]</b>,
       <img alt="Asset card" src="/help/assets/assets/asset-card.svg" /> <b>[!UICONTROL Asset Card]</b>,
       <img alt="Search" src="/help/assets/assets/Magnify.svg" /> <b>[!UICONTROL Search]</b>,
       <img alt="Branding" src="/help/assets/assets/ColorPalette.svg" /> <b>[!UICONTROL Branding]</b>,
       <img alt="Expired Assets" src="/help/assets/assets/expired-assets.svg" /> <b>[!UICONTROL Expired Assets]</b>,
       <b>[!UICONTROL Renditions]</b>, and
       <img alt="Custom Links" src="/help/assets/assets/link.svg" /> <b>[!UICONTROL Custom Links]</b>
    </td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">[!DNL Content Hub] > <b>[!UICONTROL Configuration]</b></td>
  </tr>
  <tr>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #FFF8DC;"><b>[!UICONTROL Add filters]</b> on 
       <img alt="Filters" src="/help/assets/assets/filter.svg" /> <b>[!UICONTROL Filters]</b> page, <b>[!UICONTROL Add link]</b> on 
       <img alt="Custom Links" src="/help/assets/assets/link.svg" /> <b>[!UICONTROL Custom Links]</b> page and <b>[!UICONTROL Add metadata]</b> on 
       <img alt="Import" src="/help/assets/assets/import.svg" /> <b>[!UICONTROL Import]</b>, <img alt="Asset details" src="/help/assets/assets/info-icon.svg" /> <b>[!UICONTROL Asset details]</b>, <img alt="Asset card" src="/help/assets/assets/asset-card.svg" /> <b>[!UICONTROL Asset Card]</b>, and <img alt="Search" src="/help/assets/assets/Magnify.svg" /> <b>[!UICONTROL Search]</b> pages
    </td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">[!DNL Content Hub] > <b>[!UICONTROL Configuration]</b> > Respective pages</td>
  </tr>
  <tr>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #FFF8DC;">Input fields in <b>[!UICONTROL Add metadata]</b>, <b>[!UICONTROL Add link]</b> and <b>[!UICONTROL Add filters]</b> dialog boxes.</td>
    <td style="padding: 12px; border: 1px solid #d0d0d0; background-color: #F5F5F5;">[!DNL Content Hub] > <b>[!UICONTROL Configuration]</b> > <b>[!UICONTROL Dialog boxes]</b></td>
  </tr>
</table>

See [Detailed color application guide](#primary-and-secondary-color-on-the-content-hub-home-page) for a detailed breakdown of where these colors are applied across different pages and UI elements:

<details>
<summary><strong>Detailed color application guide</strong></summary>

See the following sections to know the places on the [[!DNL Content Hub] home page](#primary-and-secondary-color-on-the-content-hub-home-page) and [[!UICONTROL Configuration]](#primary-and-secondary-color-on-the-content-hub-configuration-page) page where both these colors apply:

## Apply primary and secondary color on the [!DNL Content Hub] home page{#primary-and-secondary-color-on-the-content-hub-home-page}

Primary color apply to the following places on the [!DNL Content Hub] home page: 

* Magnifying glass ![](/help/assets/assets/Magnify.svg) inside the search bar.
* Border color of the search bar when selected.
* Selection checkboxes ![](/help/assets/assets/SelectBox.svg) after selection.
* Toggle switches ![](/help/assets/assets/toogle.svg) and date input fields.
* UI options such as ![](/help/assets/assets/add-image.svg) **[!UICONTROL Add assets]** on the **[!UICONTROL All Assets]** page and ![](/help/assets/assets/CollectionAdd.svg) **[!UICONTROL Create collection]** on the ![](/help/assets/assets/Collection.svg) **[!UICONTROL Collections]** page.
* selecting Asset cards from the **[!UICONTROL All Assets]** page. 
* Selecting collection tiles from the **[!UICONTROL Add aaset to collection]** dialog box or **[!UICONTROL Add to collection]** panel. **[!UICONTROL Add aaset to collection]** dialog box displays when you select ![](/help/assets/assets/add-circle.svg) available on the asset card or select ![](/help/assets/assets/add-circle.svg) **[!UICONTROL Add to collection]** after selecting one or more asset cards. **[!UICONTROL Add to collection]** panel displays when you click asset thumbnail on an asset card and select ![](/help/assets/assets/add-circle.svg) from the menu options in the right pane.
* The **[!UICONTROL Upload]** option in the **[!UICONTROL Add approved assets]** dialog box. **[!UICONTROL Add approved assets]** dialog box displays when you select ![](/help/assets/assets/add-image.svg) **[!UICONTROL Add assets]** available on the **[!UICONTROL All Assets]** page.
* The pane displaying the count of selected assets after selecting an asset card from the **[!UICONTROL All Assets]** or ![](/help/assets/assets/Collection.svg) **[!UICONTROL Collections]** page.
* Hovering over or selecting a rendition from the **[!UICONTROL Download]** panel. **[!UICONTROL Download]** panel displays when you click asset thumbnail on an asset card and select ![](/help/assets/assets/download-icon.svg) from the menu options in the right pane. 

Secondary color apply to the following places on the [!DNL Content Hub] home page: 

* Input fields in dialog boxes, excluding those in the **[!UICONTROL Add approved assets]** dialog box. **[!UICONTROL Add approved assets]** dialog box displays on clicking ![](/help/assets/assets/add-image.svg) **[!UICONTROL Add assets]** available on the **[!UICONTROL All Assets]** page.
* Options such as **[!UICONTROL Download]**, **[!UICONTROL Generate share link]**, and ![](/help/assets/assets/add-circle.svg) **[!UICONTROL Add to collection]** available in various dialog boxes, excluding the **[!UICONTROL Upload]** option in the **[!UICONTROL Add approved assets]** dialog box.

## Apply primary and secondary color on the [!DNL Content Hub] [!UICONTROL configuration] page{#primary-and-secondary-color-on-the-content-hub-configuration-page}

Secondary color apply to the following places on the [!DNL Content Hub] **[!UICONTROL configuration]** page:

* All configuration options including ![](/help/assets/assets/import.svg) **[!UICONTROL Import]**, ![](/help/assets/assets/filter.svg) **[!UICONTROL Filters]**, ![](/help/assets/assets/info-icon.svg) **[!UICONTROL Asset details]**, ![](/help/assets/assets/asset-card.svg) **[!UICONTROL Asset Card]**, ![](/help/assets/assets/Magnify.svg) **[!UICONTROL Search]**, ![](/help/assets/assets/ColorPalette.svg) **[!UICONTROL Branding]**, ![](/help/assets/assets/expired-assets.svg) **[!UICONTROL Expired Assets]**, **[!UICONTROL Renditions]** and ![](/help/assets/assets/link.svg) **[!UICONTROL Custom Links ]** available on the configuration page.
* Options including **[!UICONTROL Add filters]** on![](/help/assets/assets/filter.svg) **[!UICONTROL Filters]** page, **[!UICONTROL Add link]** on ![](/help/assets/assets/link.svg) **[!UICONTROL Custom Links]** page and **[!UICONTROL Add metadata]** on ![](/help/assets/assets/import.svg) **[!UICONTROL Import]**, ![](/help/assets/assets/info-icon.svg) **[!UICONTROL Asset details]**, ![](/help/assets/assets/asset-card.svg) **[!UICONTROL Asset Card]** and ![](/help/assets/assets/Magnify.svg) **[!UICONTROL Search]** pages.  
* Input fields in the **[!UICONTROL Add metadata]**, **[!UICONTROL Add link]** and **[!UICONTROL Add filters]** dialog boxes.

Primary color apply to the following places on the [!DNL Content Hub] [!UICONTROL configuration] page:

* Selecting a row from the table on the configuration pages.
* Toggle color across all configuration pages.
* The **[!UICONTROL Confirm]** option in the Edit dialog boxes on all configuration pages.

</details>
