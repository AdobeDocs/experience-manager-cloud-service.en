---
title: How do I add support for new locales to an Adaptive Form based on core components?
description: Learn to add new locales for an Adaptive Form.
feature: Adaptive Forms, Core Components
Role: Developer, Author
exl-id: bc06542b-84c8-4c6a-a305-effbd16d5630
role: User, Developer
---
# Add a locale for Adaptive Forms based on Core Components {#supporting-new-locales-for-adaptive-forms-localization}

| Version | Article link |
| -------- | ---------------------------- |
| Foundation Components  |    [Click here](supporting-new-language-localization.md)                  |
| Core Components     | This article         |

<span class="preview"> The Right-to-Left language support feature is available under the early adopter program. You can write to aem-forms-ea@adobe.com from your official email id to join the early adopter program and request access to the capability. </span>

AEM Forms provide out of the box support for English (en), Spanish (es), French (fr), Italian (it), German (de), Japanese (ja), Portuguese-Brazilian (pt-BR), Chinese (zh-CN), Chinese-Taiwan (zh-TW), and Korean (ko-KR) locales. You can add support for more locales also, like Hindi(hi_IN). You can also present Adaptive Forms in a Right-to-Left (RTL) language like Arabic, Persian, and Urdu by adding these locales.  

>[!VIDEO](https://video.tv.adobe.com/v/3433132/adaptive-forms-rtl--arabic-hebrew-farsi)

## How Does AEM Forms determine the locale for an Adaptive Form?

Understanding how AEM Forms selects the locale for rendering an Adaptive Form is crucial for proper localization. Here's a breakdown of the selection process:

### Priority-based locale selection

AEM Forms prioritizes the following methods to determine the locale for an Adaptive Form:

1. **URL Locale Selector ([locale])**:

    The system prioritizes the locale specified within the URL using the [locale] selector. This format allows caching for better performance.

    Format: The URL follows this format: http:/[AEM Forms Server URL]/content/forms/af/[afName].[locale].html?wcmmode=disabled.
    
    Example: https://[server]/content/forms/af/contact-us.hi.html renders the form in Hindi.


1. **afAcceptLang Request Parameter**:

    To override the user's browser locale, you can use the `afAcceptLang` parameter in the URL.
    
    Example: https://[server]/forms/af/survey.ca-fr.html?afAcceptLang=ca-fr forces the form to render in Canadian French.

1. **User's Browser Locale (Accept-Language Header)**:

    If no other locale is specified, AEM Forms considers the user's browser locale sent using the `Accept-Language` header.


### Fallback Mechanism:


* If a client library (process to add a new locale, explained later in this document) for the requested locale is unavailable, AEM Forms checks for a library based on the language code within the locale. 

    Example: If en_ZA (South African English) is requested and there's no en_ZA library, it uses en (English) if available.
    
    If no suitable client library is found, the default dictionary (mostly `en`) for the form's authoring language is used.

    In the absence of any locale information, the Adaptive Form displays in its original language used during development.


## Prerequisites for adding a locale

Before you begin adding a new locale for your Adaptive Forms, ensure you have the following:

**Software:**

* Plain Text Editor (IDE): While any plain text editor can work, an Integrated Development Environment (IDE) like [Microsoft Visual Studio Code](https://code.visualstudio.com/download) offers advanced features for easier editing.

* Git: This version control system is required for managing code changes. If you don't have it installed, download it from [https://git-scm.com](https://git-scm.com).


**Code Repository:**

Clone the Adaptive Forms Core Components Repository: You need a client library from this repository for adding a locale. To clone the repository:

1. Open your command line or terminal window.

1. Navigate to the desired location on your machine where you want to store the repository (for example, /adaptive-forms-core-components).

1. Run the following command to clone the repository:

    ```
    git clone https://github.com/adobe/aem-core-forms-components.git

    ```

    This command downloads the repository and create a folder named `aem-core-forms-components` on your machine. Throughout this guide, we refer to this folder as the `[Adaptive Forms Core Components repository]`. 


## Add a locale {#add-localization-support-for-non-supported-locales}

To add support for new locales to an adaptive form based on core components, follow these steps:

### Clone your AEM as a Cloud Service Git repository

1. Open the command line and choose a directory to store your AEM as a Cloud Service repository, such as `/cloud-service-repository/`.

1. Run the below command to clone the repository:

    ```SHELL

    git clone https://git.cloudmanager.adobe.com/<organization-name>/<program id>/

    ```

    To clone your Git repository, you need some information:

    * **Organization name**: This identifies your team or project within Adobe Experience Manager as a Cloud Service (AEM as a Cloud Service).

    * **Program ID**: This specifies the program associated with your repository.

    * **Credentials**: You need a username and password (or a personal access token) to access the repository securely.

    **Where to find this information?**

    For step-by-step instructions on locating these details, refer to the Adobe Experience League article "[Accessing Git](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#accessing-git)".

    **Your project is ready!**

    When the command completes successfully, you see a new folder created in your local directory. This folder is named after your program (for example, program-id). This folder contains all the files and code downloaded from your AEM as a Cloud Service Git repository.

    Throughout this guide, we refer to this folder as the `[AEMaaCS project directory]`.


### Add the new locale to the Guide Localization Service

1. Open the repository folder in an editor. 

    ![Repository folder in an editor](/help/forms/assets/repository-folder-in-an-editor.png)

1. Locate the `Guide Localization Service.cfg.json` file. This file controls the locales supported by your AEM Forms application. You can edit this file to add a new locale.

    * **Existing file**: If the file already exists, locate it within your AEM Forms project directory. The typical location is:

        ```Shell

        [AEMaaCS project directory]/ui.config/src/main/content/jcr_root/apps/<appid>/osgiconfig/config`. 

        ```

        Replace `<appid>` with your project specific app ID. You can find `<appid>` for your AEM Project in the `archetype.properties` file. 

        ![Archetype Properties](/help/forms/assets/archetype-properties.png)

    * **New file**: If the file doesn't exist, you need to create it in the same location mentioned above. Do not copy paste the name of the file from this document, rather manually type the name. The file name `Guide Localization Service.cfg.json` includes spaces. This is intentional and not a typo in the documentation.

        A sample file with the list of OOTB supported locales is:

        ```

            {
                "supportedLocales":[
                "en",
                "fr",
                "de",
                "ja",
                "pt-br",
                "zh-cn",
                "zh-tw",
                "ko-kr",
                "it",
                "es"
                ]
            }

        ```

1. Add the locale code for your desired language to the file. 
    1. Use the [List of ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) to find the two-letter code representing your desired language.

    1. Include the locale code to the `Guide Localization Service.cfg.json` file. Here are some examples:

        * Left-to-Right Languages:
            * English (United States): en-US
            * Spanish (Spain): es-ES
            * French (France): fr-FR
        * Right-to-Left Languages:
            * Arabic (United Arab Emirates): ar-ae
            * Hebrew: he (or iw for historical reference)
            * Farsi: fa

1. After making changes, ensure the `Guide Localization Service.cfg.json` file is formatted correctly as a valid JSON file. Errors in JSON formatting can prevent it from functioning properly. Save the file. 



### Leverage the sample client library for easy locale addition

AEM Forms provides a helpful sample client library, `clientlib-it-custom-locale`, to simplify adding new locales. This library is part of the [Adaptive Forms Core Components repository](https://github.com/adobe/aem-core-forms-components), available on GitHub.


Before we begin, ensure you have a local copy of the [Adaptive Forms Core Components repository]. If not, you can easily clone it using Git with the following command:

```SHELL

git clone https://github.com/adobe/aem-core-forms-components.git

```

This command downloads the entire repository, including the clientlib-it-custom-locale library, to a directory named aem-core-forms-components on your machine.

![Adaptive Forms Core Components repository directory on local machine](/help/forms/assets/core-forms-components-repo-on-local-machine.png)

### Integrate the sample client library

Now, let's incorporate the `clientlib-it-custom-locale` library into your AEM as a Cloud Service, [AEMaaCS project directory]:

1. Locate the sample client library:

    Within your local copy of the [Adaptive Forms Core Components repository], navigate to the following path:

    ```

        /aem-core-forms-components/it/apps/src/main/content/jcr_root/apps/forms-core-components-it/clientlibs
    ```

1. Copy and paste the library:

    1. Copy the `clientlib-it-custom-locale` folder.

        ![Copying clientlib-it-custom-locale](/help/forms/assets/clientlib-it-custom-locale-copy.png)

    1. Navigate to the following directory within your [AEMaaCS project directory]:

         ```
    
         /ui.apps/src/main/content/jcr_root/apps/<app-id>/clientlib

    
         ```

        **Important**: Replace `<app-id>` with the actual ID of your application.
        
    1. Paste the copied `clientlib-it-custom-locale` folder into this directory.

        ![Pasting clientlib-it-custom-locale](/help/forms/assets/clientlib-it-custom-locale-paste.png)

1. Update `aemLangUrl` path in `languageinit.js`
   
    1. Navigate to the following directory within your [AEMaaCS project directory]:

         ```
    
         /ui.apps/src/main/content/jcr_root/apps/<app-id>/clientlib/clientlib-it-custom-locale/js
         ```

    1. Open the `languageinit.js` file in your editor.
    1. Locate the following line in the `languageinit.js` file: 
   
        `const aemLangUrl = /etc.clientlibs/forms-core-components-it/clientlibs/clientlib-it-custom-locale/resources/i18n/${lang}.json;`
    
    1. Replace `forms-core-components-it` with your `<app-id>` (actual ID of your application) in the above line. 

        `const aemLangUrl = '/etc.clientlibs/<app-id>/clientlibs/clientlib-it-custom-locale/resources/i18n/${lang}.json';`

        ![language-init-file](/help/forms/assets/language-init-name-change.png)

>[!NOTE]
>  
> If you do not replace `forms-core-components-it` with your project name or `<app-id>`, the date picker component fails to translate.

### Create a file for your new locale:

1. Navigate to the Locale Directory:

    Within your `[AEMaaCS project directory]`, navigate to the following path:

    ```
        /ui.apps/src/main/content/jcr_root/apps/<program-id>/clientlibs/clientlib-it-custom-locale/resources/i18n/

    ```

    **Important**: Replace `<program-id>` with your actual application ID.

1. Locate the sample English language file: 

    AEM Forms provides a [sample English locale file (.json) on GitHub](https://github.com/adobe/aem-core-forms-components/blob/master/ui.af.apps/src/main/content/jcr_root/apps/core/fd/af-clientlibs/core-forms-components-runtime-all/resources/i18n/en.json). 

    The English language file includes the default set of strings for reference. Your locale-specific file should mimic the structure of the English language file. 

    For languages like Arabic, Hebrew, and Farsi, text reads from right to left (RTL) instead of left to right (LTR) like English. To ensure your forms display correctly in these languages, we recommend using our sample locale files as a guide. These files provide a reference for how to format text, dates, and other elements for RTL languages. You can find the sample locale files for:

    * [Arabic](/help/forms/assets/ar-ae.json) 
    * [Hebrew](/help/forms/assets/he.json) 
    * [Farsi](/help/forms/assets/fa.json) 

    By leveraging these sample files, you can ensure your forms provide a seamless experience for users working in RTL languages.


1. Create your locale file:

    1. Create a new .json file within the `i18n` directory. 
    1. Name the file using the appropriate locale code for your desired language (For example, fr-FR.json for French and ar-ae.json for Arabic). The structure of this file should mirror the English locale file. 


1. Structure and Translation:

    1. Open the newly created file in a text editor.

    1. Replace the English values with the corresponding translations for your target language. 

    1. Once you've finished translating the strings, save the file.

    


### Add locale support to the dictionary

This step applies only to locales other than the following commonly supported ones: English (en), German (de), Spanish (es), French (fr), Italian (it), Brazilian Portuguese (pt-br), Chinese (Simplified - zh_cn), Chinese (Traditional - zh_tw), Japanese (ja), and Korean (ko_kr).

1. Locate the configuration folder:

    Navigate to the following directory in your [AEMaaCS project directory]:

    ```
    /ui.content/src/main/content/jcr_root/etc


    ```

1. Create the necessary folders (if missing):

    If the `etc` folder doesn't exist within `jcr_root` folder, create it. Inside `etc`, create another folder named `languages` if it's missing.

1. Create the locale configuration file:

    Within the `languages` folder, create a new file named `.content.xml`. Do not copy paste the name of the file from this document, rather manually type the name. 

    ![create a new file named `.content.xml`](etc-content-xml.png)

    Open this file and paste the following content, replacing [LOCALE_CODE] with the actual locale code (For example, ar-ae for Arabic).


    ```XML
    
    <?xml version="1.0" encoding="UTF-8"?>
    <jcr:root xmlns:jcr="http://www.jcp.org/jcr/1.0" xmlns:nt="http://www.jcp.org/jcr/nt/1.0"
          jcr:primaryType="nt:unstructured"
          languages="[de,es,fr,it,pt-br,zh-cn,zh-tw,ja,ko-kr,hi]"/>

    ```

    WARNING: Do not replace the existing list. Instead, append your new locale code within square brackets, separated by commas, like this (using ar-ae as an example):

    ```XML
    
    languages="[de,es,fr,it,pt-br,zh-cn,zh-tw,ja,ko-kr,hi,ar-ae]"


    ```

1. Include the New Folders in filter.xml:

    Navigate to the `/ui.content/src/main/content/meta-inf/vault/filter.xml` file in your [AEMaaCS project directory].

    Open the file and add the following line at the end:

    ```
    
    <filter root="/etc/languages"/>


    ```

    ![Add the created folders in the `filter.xml` under `/ui.content/src/main/content/meta-inf/vault/filter.xml`](langauge-filter.png)

1. Save the file. 

### Deploy the newly created locale to your AEM environment

You are now all set to use the new locale with your Adaptive Forms. You can 

* Deploy the AEM as a Cloud Service, [AEMaaCS project directory], to your local development environment to try the new locale configuration on your local machine. To deploy to your local development environment:

    1. Ensure that your local development environment is up and running. If you haven't already set up a local development environment, refer to the guide on [Setup local development environment for AEM Forms](/help/forms/setup-local-development-environment.md).

    1. Open the terminal window or command prompt.

    1. Navigate to the [AEMaaCS project directory]

    1. Run the following command:

        ```

        mvn -PautoInstallPackage clean install

        ```

* Deploy the AEM as a Cloud Service, [AEMaaCS project directory], to your Cloud Service environment. To deploy to your Cloud Service environment:

    1. Commit Your Changes:

        After adding the new locale configuration, commit your changes with a clear Git message describing the locale addition (For example, "Added support for [Locale Name]"). 

    1. Deploy the Updated Code:

        Trigger a deployment of your code through the [existing full-stack pipeline](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html?lang=en#setup-pipeline). This automatically builds and deploys the updated code with the new locale support.

        If you haven't already set up a pipeline, refer to the guide on [how to set up a pipeline for AEM Forms as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html?lang=en#setup-pipeline).


## Preview an Adaptive Form with newly added locale

These steps guide you through previewing an Adaptive Form with the newly added locale:

1. Log in to your AEM Forms as a Cloud Service instance.
1. Go to **Forms** >  **Forms and Documents**.
1. Select an Adaptive Form and click **Add Dictionary** and **Add Dictionary To Translation Project** wizard appears.
1. Specify the **Project Title** and select the **Target Languages** from the drop-down menu in the **Add Dictionary To Translation Project** wizard.
1. Click **Done** and execute the created translation project.
1. Go to **Forms** >  **Forms and Documents**.
1. Select the Adaptive Form and choose the **Preview as HTML** option. 
1. Append `&afAcceptLang=<locale-name>` to the preview URL and press the return key. Replace `<locale-name>` with your actual locale code. The adaptive form is displayed in the specified locale. 

## Best Practices to support for new localization {#best-practices}

* Adobe recommends creating a translation project after creating an Adaptive Form. This streamlines the localization process.
* When Numeric Box and Date Picker components are translated into a specific locale, formatting issues may arise. To mitigate this, a **Language** option has been incorporated into the Configure dialog of [Date picker component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/date-picker#format-tab) and [Numeric Box component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/numeric-box#formats-configure-tab).


* Handling New Fields:

    * **Machine Translation**: If using machine translation, you need to recreate the dictionary and re-[run the translation project](/help/forms/using-aem-translation-workflow-to-localize-adaptive-forms-core-components.md) after adding new fields to an existing Adaptive Form. New fields added after the initial translation project remain untranslated. 

    * **Human Translation**: For human translation workflows, export the dictionary using the UI at `[AEM Forms Server]/libs/cq/i18n/gui/translator.html`. Update the dictionary for the new fields and upload the revised version.


## See Also {#see-also}

{{see-also}}

* [Generate document of record for Adaptive Forms](/help/forms/generate-document-of-record-core-components.md)
* [Add an Adaptive Form to an AEM Sites page or Experience Fragment](/help/forms/create-or-add-an-adaptive-form-to-aem-sites-page.md)

