---
title: How do I add support for new locales to an Adaptive Form based on Foundation Components?
description: For Adaptive Forms, you can add locales for more languages apart from the one provided out of the box.
feature: Adaptive Forms, Foundation Components
exl-id: 4c7d6caa-1adb-4663-933f-b09129b9baef
role: User, Developer
---
# Supporting new locales for Adaptive Forms localization {#supporting-new-locales-for-adaptive-forms-localization}

>[!NOTE]
>
> Adobe recommends using the modern and extensible data capture [Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html) for [creating new Adaptive Forms](/help/forms/creating-adaptive-form-core-components.md) or [adding Adaptive Forms to AEM Sites pages](/help/forms/create-or-add-an-adaptive-form-to-aem-sites-page.md). These components represent a significant advancement in Adaptive Forms creation, ensuring impressive user experiences. This article describes older approach to author Adaptive Forms using foundation components.


| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/manage-administer-aem-forms/supporting-new-language-localization.html)                  |
| Core Components  |    [Click here](supporting-new-language-localization-core-components.md)                  |
| Foundation Components     | This article         |

AEM Forms provide out of the box support for English (en), Spanish (es), French (fr), Italian (it), German (de), Japanese (ja), Portuguese-Brazilian (pt-BR), Chinese (zh-CN), Chinese-Taiwan (zh-TW), and Korean (ko-KR) locales. You can add support for more locales also, like Hindi(hi_IN). 

## Understanding locale dictionaries {#about-locale-dictionaries}

The localization of adaptive forms relies on two types of locale dictionaries:

*   **Form-specific dictionary** Contains strings used in adaptive forms. For example, labels, field names, error messages, help descriptions. It is managed as a set of XLIFF files for each locale and you can access it at `[author-instance]/libs/cq/i18n/gui/translator.html`.

*   **Global dictionaries** There are two global dictionaries, managed as JSON objects, in the AEM client library. These dictionaries contain default error messages, month names, currency symbols, date and time patterns, and so on. You can find these dictionaries at `[author-instance]/libs/fd/xfaforms/clientlibs/I18N`. These locations contain separate folders for each locale. Because global dictionaries are not updated frequently, keeping separate JavaScript files for each locale enables browsers to cache them and reduce network bandwidth usage when accessing different adaptive forms on the same server.

## Add support for new locales {#add-support-for-new-locales}

Perform the following steps to add support for a new locale: 

1. [Add localization support for non-supported locales](#add-localization-support-for-non-supported-locales)
1. [Use added locales in Adaptive Forms](#use-added-locale-in-af)

### Add localization support for non-supported locales {#add-localization-support-for-non-supported-locales}

AEM Forms currently support localization of Adaptive Forms content in English (en), Spanish (es), French (fr), Italian (it), German (de), Japanese (ja), Portuguese-Brazilian (pt-BR), Chinese (zh-CN), Chinese-Taiwan (zh-TW), and Korean (ko-KR) locales.

To add support for a new locale at the Adaptive Forms runtime:

1.  [Clone your repository](#clone-the-repository)
1.  [Add a locale to the GuideLocalizationService service](#add-a-locale-to-the-guide-localization-service)
1.  [Add locale-name specific folder](#add-locale-name-specific-folder)
1.  [Add locale support for the dictionary](#add-locale-support-for-the-dictionary)
1.  [Commit the changes in the repository and deploy the pipeline](#commit-changes-in-repo-deploy-pipeline)

#### 1. Clone the repository {#clone-the-repository}

1. From the command line, navigate to where you would like to clone the Forms Cloud Service repository.
1. Execute the command that you [retrieved from Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#accessing-git). It is similar to `git clone https://git.cloudmanager.adobe.com/<my-org>/<my-program>/`. 
1. Use the git user name and password to clone the repository. 
1. Open the cloned Forms Cloud Service repository folder in your preferred editor. 

#### 2. Add a locale to the Guide Localization service {#add-a-locale-to-the-guide-localization-service}

1.  Locate the `Guide Localization Service.cfg.json` file and add the locale you want to add to the list of supported locales.

    >[!NOTE]
    >
    > Create a file with the name as `Guide Localization Service.cfg.json` file, if already not present.
    
#### 3. Add locale-name specific folder client library {#add-locale-name-specific-folder}

1. In UI.content folder, create `etc/clientlibs` folder.
1. Further create a folder named as `locale-name` under `etc/clientlibs` to serve as a container for xfa and af clientlibs.

##### 3.1 Add XFA client library for a locale in a locale-name folder 

Create a node named as `[locale-name]_xfa` and type as `cq:ClientLibraryFolder` under `etc/clientlibs/locale_name`, with category `xfaforms.I18N.<locale>`, and add the following files:

*   **I18N.js** defining `xfalib.locale.Strings` for the `<locale>` as defined in `/etc/clientlibs/fd/xfaforms/I18N/ja/I18N`.
*   **js.txt** containing the following:
              */libs/fd/xfaforms/clientlibs/I18N/Namespace.js
              I18N.js
              /etc/clientlibs/fd/xfaforms/I18N/LogMessages.js*
              
##### 3.2. Add Adaptive Form client library for a locale locale-name folder 

1.  Create a node named as `[locale-name]_af` and type as `cq:ClientLibraryFolder` under `etc/clientlibs/locale_name`, with category as `guides.I18N.<locale>` and dependencies as `xfaforms.3rdparty`, `xfaforms.I18N.<locale>` and `guide.common`.
1.  Create a folder named as `javascript` and add the following files:

    * **i18n.js** defining `guidelib.i18n`, having patterns of "calendarSymbols", `datePatterns`, `timePatterns`, `dateTimeSymbols`, `numberPatterns`, `numberSymbols`, `currencySymbols`, `typefaces` for the `<locale>` as per the XFA specifications described in [Locale Set Specification](https://helpx.adobe.com/content/dam/Adobe/specs/xfa_spec_3_3.pdf). 
    * **LogMessages.js** defining `guidelib.i18n.strings` and `guidelib.i18n.LogMessages` for the `<locale>` as defined in `/etc/clientlibs/fd/af/I18N/fr/javascript/LogMessages.js`.

1.  Add **js.txt** containing the following:

    ```
      i18n.js
      LogMessages.js
    ```

#### 4. Add locale support for the dictionary {#add-locale-support-for-the-dictionary}

Perform this step only if the `<locale>` you are adding is not among `en`, `de`, `es`, `fr`, `it`, `pt-br`, `zh-cn`, `zh-tw`, `ja`, `ko-kr`.

1. Create a folder `languages` under `etc`, if not present already.

1. Add a multi-valued string property `languages` to the node, if not present already.
1. Add the `<locale-name>` default locale values `de`, `es`, `fr`, `it`, `pt-br`, `zh-cn`, `zh-tw`, `ja`, `ko-kr`, if not present already.

1. Add the `<locale>` to the values of the `languages` property of `/etc/languages`.
1. Add the created folders in the `filter.xml` under etc/META-INF/[folder hierarchy] as: 

    ```
    <filter root="/etc/clientlibs/[locale-name]"/>
    <filter root="/etc/languages"/>
    ```

 Before committing the changes into the AEM Git repository, you need to access your [Git repository information](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html?lang=en#accessing-git).

#### 5. Commit the changes in the repository and deploy the pipeline {#commit-changes-in-repo-deploy-pipeline}

Commit the changes to the GIT repository after adding a locale support. Deploy your code using the full stack pipeline. Learn [how to set up a pipeline](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html?lang=en#setup-pipeline) to add new locale support.
Once the pipeline is complete, the newly added locale appears in the AEM environment. 

### Use added locale in Adaptive Forms {#use-added-locale-in-af}

Perform the following steps to use and render an Adaptive Form using newly added locale:

1. Log in to your AEM author instance.
1. Go to **Forms** >  **Forms and Documents**.
1. Select an Adaptive Form and click **Add Dictionary** and **Add Dictionary To Translation Project** wizard appears.
1. Specify the **Project Title** and select the **Target Languages** from the drop-down menu in the **Add Dictionary To Translation Project** wizard.
1. Click **Done** and execute the created translation project.
1. Select an Adaptive Form and click **Preview as HTML**.
1. Add `&afAcceptLang=<locale-name>` in the URL of an Adaptive Form.
1. Refresh the page and Adaptive Form is rendered in a specified locale. 

There are two methods to identify the locale of an Adaptive Form. When an Adaptive Form is rendered, it identifies the requested locale by: 

*   Retrieving the `[local]` selector in the adaptive form URL. The format of the URL is `http://host:[port]/content/forms/af/[afName].[locale].html?wcmmode=disabled`. Using `[local]` selector allows caching an Adaptive Form. 

*   Retrieving the following parameters in the listed order:
  
    *   Request parameter `afAcceptLang`
  To override the browser locale of users, you can pass the `afAcceptLang` request parameter to force the locale. For example, the following URL forces to render the form in Canadian-French locale:
  `https://'[server]:[port]'/<contextPath>/<formFolder>/<formName>.html?wcmmode=disabled&afAcceptLang=ca-fr`

    *   The browser locale set for the user, which is specified in the request using the `Accept-Language` header.

If a client library for the requested locale does not exist, it checks for a client library for the language code present in the locale. For example, if the requested locale is `en_ZA` (South African English) and the client library for `en_ZA` does not exist, the adaptive form uses the client library for `en` (English) language, if it exists. However, if none of them exist, the Adaptive Form uses the dictionary for `en` locale.


Once the locale is identified, the Adaptive Form picks the form-specific dictionary. If the form-specific dictionary for the requested locale is not found, it uses the dictionary for the language in which Adaptive Form is authored.

If no locale information is present, Adaptive Form is delivered in the original language of the form. The original language is the language used while developing the Adaptive Form.  

Get a [sample client library](/help/forms/assets/locale-support-sample.zip) to add support for new locale. You need to change the content of the folder in the required locale.

## Best Practices to support for new localization {#best-practices}

*   Adobe recommends creating a translation project after creating an Adaptive Form.

*   When new fields are added in an existing Adaptive Form:
    * **For machine translation**: Re-create the dictionary and run the translation project. Fields added to an Adaptive Form after creating a translation project remain untranslated. 
    * **For human translation**: Export the dictionary through `[server:port]/libs/cq/i18n/gui/translator.html`. Update the dictionary for the newly added fields and upload it.


## See Also {#see-also}

{{see-also}}