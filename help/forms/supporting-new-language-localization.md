---
title: Supporting new locales for adaptive forms localization
seo-title: Supporting new locales for adaptive forms localization
description: AEM Forms allows you to add new locales for localizing adaptive forms. The supported locales by default are English, French, German, and Japanese.
seo-description: AEM Forms allows you to add new locales for localizing adaptive forms. The supported locales by default are English, French, German, and Japanese.
---
# Supporting new locales for adaptive forms localization{#supporting-new-locales-for-adaptive-forms-localization}

## About locale dictionaries {#about-locale-dictionaries}

The localization of adaptive forms relies on two types of locale dictionaries:

* **Form-specific dictionary** Contains strings used in adaptive forms. For example, labels, field names, error messages, help descriptions, and so on. It is managed as a set of XLIFF files for each locale and you can access it at `[author-instance]content\src\main\content\jcr_root\etc\clientlibs\[locale-folder]\[locale]_xfa\javascript\i18n.js`.

* **Global dictionaries** There are two global dictionaries, managed as JSON objects, in AEM client library. These dictionaries contain default error messages, month names, currency symbols, date and time patterns, and so on. You can find these dictionaries at `[author-instance]content\src\main\content\jcr_root\etc\clientlibs\[locale-folder]\[locale]_af\javascript\i18n.js`. These locations contains separate folders for each locale. Because global dictionaries are usually not updated frequently, keeping separate JavaScript files for each locale enables browsers to cache them and reduce network bandwidth usage when accessing different adaptive forms on same server.

Steps to support new localization for AEM Forms:

1. [Add localization support for non-supported locales](#add-localization-support-for-non-supported-locales-add-localization-support-for-non-supported-locales)
1. [Use added locales in Adaptive Forms](#use-added-locale-in-adaptive-forms-use-added-locale-in-af)

## Add localization support for non-supported locales {#add-localization-support-for-non-supported-locales}

AEM Forms currently supports localization of adaptive forms content in English (en), Spanish (es), French (fr), Italian (it), German (de), Japanese (ja), Portuguese-Brazilian (pt-BR), Chinese (zh-CN), Chinese-Taiwan (zh-TW), and Korean (ko-KR) locales.

To add support for a new locale at adaptive forms runtime:

1. [Clone your repository](#1-clone-the-repository-clone-the-repository)
1. [Add a locale to the GuideLocalizationService service](#1-add-a-locale-to-the-guide-localization-service-add-a-locale-to-the-guide-localization-service-br)
1. [Add locale-name specific folder](#3-add-locale-name-specific-folder-add-locale-name-specific-folder)
1. [Add XFA client library for a locale](#3-add-xfa-client-library-for-a-locale)
1. [Add adaptive form client library for a locale](#4-add-adaptive-form-client-library-for-a-locale-add-adaptive-form-client-library-for-a-locale-br)
1. [Add locale support for the dictionary](#5-add-locale-support-for-the-dictionary-add-locale-support-for-the-dictionary-br)
1. [Commit the changes in the repository and deploy the pipeline](#7-commit-the-changes-in-the-repository-and-deploy-the-pipeline-commit-chnages-in-repo-deploy-pipeline)

### 1. Clone the repository {#clone-the-repository}

1. From the command line, navigate to where you would like to clone the repository.
1. Execute the command you [retrieved from Cloud Manager.](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#accessing-git) It is similar to `git clone https://git.cloudmanager.adobe.com/<my-org>/<my-program>/`. 
1. Use the git user name and password to clone the repository. 
1. Open the clonned repository folder in your preferred editor. 

### 2. Add a locale to the Guide Localization service {#add-a-locale-to-the-guide-localization-service-br}

1. Locate the `Guide Localization Service.cfg.json` file and add the locale you want to add to the list of supported locales.

    >[!NOTE]
    >
    >* Create a new file with the name as `Guide Localization Service.cfg.json` file, if already not present.
    
### 3. Add locale-name specific folder client library {#add-locale-name-specific-folder}

1. Create a node of type `cq:etc`
1. Add a node of type `cq:ClientLibraryFolder` as `clientlibs`.
1. Further add a node of type `cq:locale-name` under `/etc/clientlibs`.

#### 3.1 Add XFA client library for a locale in locale-name folder 

1. Create a node of type `cq:[locale-name]_xfa` under `etc/<folderHierarchy>`, with category `xfaforms.I18N.<locale>`, and add the following files:
* **I18N.js** defining `xfalib.locale.Strings` for the `<locale>` as defined in `/etc/clientlibs/fd/xfaforms/I18N/ja/I18N`.
* **js.txt** containing the following:
            */libs/fd/xfaforms/clientlibs/I18N/Namespace.js
            I18N.js
            /etc/clientlibs/fd/xfaforms/I18N/LogMessages.js*
            
#### 3.2. Add adaptive form client library for a locale locale-name folder {#add-adaptive-form-client-library-for-a-locale-br}

1. Create a node of type `cq:[locale-name]_af` under `etc/<folderHierarchy>`, with category as `guides.I18N.<locale>` and and dependencies as `xfaforms.3rdparty`, `xfaforms.I18N.<locale>` and `guide.common`.
1. Add a node of type `cq:Javascript` and add the following files:

    * **i18n.js** defining `guidelib.i18n`, having patterns of "calendarSymbols", `datePatterns`, `timePatterns`, `dateTimeSymbols`, `numberPatterns`, `numberSymbols`, `currencySymbols`, `typefaces` for the `<locale>` as per the XFA specifications described in [Locale Set Specification](https://helpx.adobe.com/content/dam/Adobe/specs/xfa_spec_3_3.pdf). 
    * **LogMessages.js** defining `guidelib.i18n.strings` and `guidelib.i18n.LogMessages` for the `<locale>` as defined in `/etc/clientlibs/fd/af/I18N/fr/javascript/LogMessages.js`.

1. Add **js.txt** containing the following:

        *text
        i18n.js
        LogMessages.js*

### 4. Add locale support for the dictionary {#add-locale-support-for-the-dictionary-br}

Perform this step only if the `<locale>` you are adding is not among `en`, `de`, `es`, `fr`, `it`, `pt-br`, `zh-cn`, `zh-tw`, `ja`, `ko-kr`.

1. Create an `nt:unstructured` node `languages` under `etc`, if not present already.

1. Add a multi-valued string property `languages` to the node, if not present already.
1. Add the `<locale-name>` default locale values `de`, `es`, `fr`, `it`, `pt-br`, `zh-cn`, `zh-tw`, `ja`, `ko-kr`, if not present already.

1. Add the `<locale>` to the values of the `languages` property of `/etc/languages`.

The added `<locale>` appears at the **Add Dictionary** option.

```text
Add the newly created folders in the `filter.xml` under etc/META-INF/[folder hierarchy] as:
<filter root="/etc/clientlibs/[locale-name]folder"/>
<filter root="/etc/languages"/>
```

 Before committing the changes into the AEM Git repository, you need to access your [Git repository information](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html?lang=en#accessing-git).

### 5. Commit the changes in the repository and deploy the pipeline {#commit-chnages-in-repo-deploy-pipeline}

Commit the changes to the GIT repository after adding a new locale support. Deploy your customized theme using the front-end pipeline. Learn [how to set up a frontline pipeline](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html?lang=en#setup-pipeline) to add new locale support.

Once the pipeline is complete, the newly added locale appears in the AEM environment. You can validate it by clicking on **Add Dictionary** option in the Forms tab. 

### Use added locale in Adaptive Forms {#use-added-locale-in-af}

There are two methods to identify the locale of an Adaptive Form. When an Adaptive Form is rendered, it identifies the requested locale by : 

* looking at the `[local]` selector in the adaptive form URL. The format of the URL is `http://host:[port]/content/forms/af/[afName].[locale].html?wcmmode=disabled`. Using `[local]` selector allows caching an Adaptive Form. 

* looking at the following parameters in the specified order:

  * Request parameter `afAcceptLang`
  To override the browser locale of users, you can pass the `afAcceptLang` request parameter to force the locale. For example, the following URL will force to render the form in Canadian-French locale:
  `https://'[server]:[port]'/<contextPath>/<formFolder>/<formName>.html?wcmmode=disabled&afAcceptLang=ca-fr`

  * The browser locale set for the user, which is specified in the request using the `Accept-Language` header.

If a client library for the requested locale doesn't exist, it checks for a client library for the language code present in the locale. For example, if the requested locale is `en_ZA` (South African English) and the client library for `en_ZA` doesn't exist, the adaptive form will use the client library for `en` (English) language, if it exists. However, if none of them exist, the Adaptive Form uses the dictionary for `en` locale.

Steps to use and render an Adaptive Form using a newly added locale:

1. Login to your AEM author instance.
1. Go to **Forms** >  **Forms and Documents**.
1. Select an Adaptive Form and click **Add Dictionary**.
1. Once **Add Dictionary** is clicked, **Add Dictionary To Translation Project** wizard appears.
1. Specify the **Project Title** and select the **Target Languages** from the drop-down menu in the **Add Dictionary To Translation Project** wizard.
1. Click **Done** and execute the created translation project.
1. Select an Adative Form and click **Preview as HTML**.
1. Add `&afAcceptLang=<locale-name>` in the URL of an Adaptive Form.
1. Refresh the page and Adaptive Form is rendered in a specified locale. 

Once the locale is identified, the Adaptive Form picks the form-specific dictionary. If the form-specific dictionary for the requested locale is not found, it uses the dictionary for language in which Adaptive Form is authored.

If no locale information is present, Adaptive Form is delivered in the original language of the form. The original language is the language used while developing the Adaptive Form.  

Get [sample client library](/help/forms/assets/locale-support-sample.zip) to add support for new locale. You need to change the content of the folder in the required locale.

