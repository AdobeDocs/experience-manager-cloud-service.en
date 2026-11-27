---
title: Troubleshoot AEM Forms custom locale dictionaries
description: Learn how to troubleshoot custom locale dictionaries for multilingual forms in AEM Forms based on Core Components, with dictionary loading and message errors.
feature: Adaptive Forms, Core Components
role: Developer
level: Intermediate
hide: true
hidefromtoc: true
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms."
---

# Troubleshoot AEM Forms custom locale dictionaries {#troubleshoot-custom-locale-dictionaries}

Custom locale dictionaries supply translated runtime messages, such as required-field validation messages, for Adaptive Forms based on Core Components in Adobe Experience Manager Forms (AEM Forms) as a Cloud Service. To use a new locale, register it with the Guide Localization Service and load the project dictionary through a `LOCALE_CONFIG` callback.

Use the checks below when the form remains in the default language or locale resources fail to load. For the complete setup procedure, see [Add a locale for Adaptive Forms based on Core Components](/help/forms/supporting-new-language-localization-core-components.md).

## Issue

After adding a new locale, the form still renders in its default language, validation messages remain untranslated, or the browser reports HTTP 404 for locale resources.

Check the form model's returned `lang` and the project's dictionary request separately. A missing built-in dictionary does not by itself establish that the project dictionary failed to load.

## Cause

Runtime messages for a new locale depend on both server-side locale registration and a matching client library and dictionary:

1. The locale code must be registered in `Guide Localization Service.cfg.json`'s `supportedLocales` array. If the returned model's `lang` differs from the requested locale, check this configuration before diagnosing the client-side dictionary loader.
1. A matching locale client library (based on the `clientlib-it-custom-locale` sample in the `aem-core-forms-components` GitHub repository) must be deployed, whose `languageinit.js` registers a `LOCALE_CONFIG` function that loads this project's own dictionary (`FormView.LanguageUtils.loadLang(lang, <this project's dictionary URL>)`), together with the dictionary file itself. Check which dictionaries are included with your installed runtime rather than assuming a fixed set across versions.

The form's authored labels use the separate [form translation workflow](/help/forms/supporting-new-language-localization-core-components.md#preview-an-adaptive-form-with-newly-added-locale). Loading a runtime dictionary alone does not establish that all labels or date, number, and currency formats are localized.

After adding a locale, recheck related locales for unexpected changes.

>[!NOTE]
>
>On a local Cloud Service SDK with Forms 2026.10.6.04 and Core Components 3.0.172, requesting `ar-ae` returned `lang=en` before registration and `lang=ar-ae` after registration. The project dictionary returned HTTP 200 and supplied a translated required-field message even though the built-in `ar-ae.json` request returned HTTP 404. This verified dictionary loading and that validation message only, not complete label or date, number, and currency localization, or hosted Cloud Service delivery through Dispatcher and CDN.

## Resolution

1. [Add the new locale's code to the Guide Localization Service](/help/forms/supporting-new-language-localization-core-components.md#add-the-new-locale-to-the-guide-localization-service) in `supportedLocales` in `Guide Localization Service.cfg.json` (correct ISO 639-1 code, plus country code for regional variants), keeping the file valid JSON. Merge the locale into the existing list and preserve its other values.
1. Clone `aem-core-forms-components` from GitHub and copy its `clientlib-it-custom-locale` sample client library into the project's own `ui.apps` clientlibs, renamed/re-categorized for the project and locale.
1. Follow [Integrate the sample client library](/help/forms/supporting-new-language-localization-core-components.md#integrate-the-sample-client-library) to update the dictionary URL (`DICTIONARY_URL` in the code below, `aemLangUrl` in Adobe's sample) inside the copied `languageinit.js`'s `LOCALE_CONFIG` function to the project's own deployed dictionary (the client library needs `allowProxy` so `/etc.clientlibs` serves it). Ensure the callback returns or awaits `FormView.LanguageUtils.loadLang` so language initialization waits for the dictionary.

   [Create the locale dictionary](/help/forms/supporting-new-language-localization-core-components.md#create-a-file-for-your-new-locale) with every key of your installed runtime's `en.json` translated, preserving its structure and substitution placeholders. Follow [Add locale support to the dictionary](/help/forms/supporting-new-language-localization-core-components.md#add-locale-support-to-the-dictionary) for any required `/etc/languages` configuration, preserving existing values.
1. [Deploy the locale through your project's pipeline](/help/forms/supporting-new-language-localization-core-components.md#deploy-the-newly-created-locale-to-your-aem-environment) and request the form with `afAcceptLang` set to the new locale code (or the `[locale]` URL selector).

   Confirm that the model returns the intended `lang`, the custom locale callback runs, and the project's dictionary request returns HTTP 200 with the expected JSON. A built-in dictionary 404 can be harmless when the project dictionary loads successfully. For a project dictionary 404, check the exact deployed path.

   Wait for language initialization to complete, then trigger required-field validation and check the rendered message. Re-check existing, closely related locales to identify regressions rather than assuming their fallback behavior.

## Code samples

The following examples use the same paths and category as the downloadable project source. Replace `myproject` with your application ID. Merge the configuration into your existing project rather than replacing its supported locales.

The translated JSON snippet is illustrative, not a complete deployable dictionary. Before deployment, translate the full template, reconcile its keys and structure with your installed runtime, and preserve substitution placeholders.

>[!BEGINTABS]

>[!TAB .content.xml]

Path: `ui.apps/src/main/content/jcr_root/apps/myproject/clientlibs/clientlib-locale-ar-ae/.content.xml`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jcr:root xmlns:jcr="http://www.jcp.org/jcr/1.0" xmlns:cq="http://www.day.com/jcr/cq/1.0"
    jcr:primaryType="cq:ClientLibraryFolder"
    allowProxy="{Boolean}true"
    categories="[myproject.forms.locale.ar-ae]"
    dependencies="[core.forms.components.runtime.all]"/>
```

>[!TAB js.txt]

In the same folder, `js.txt` includes the loader:

```text
#base=js
languageinit.js
```

>[!TAB languageinit.js]

Place this code in the client library's `js/languageinit.js`. It adapts [Adobe's custom locale sample](https://github.com/adobe/aem-core-forms-components/blob/00e71c9175f1304d325bbb5f519c310bdead3750/it/apps/src/main/content/jcr_root/apps/forms-core-components-it/clientlibs/clientlib-it-custom-locale/js/languageinit.js). The archive preserves its Apache-2.0 license and attribution.

```javascript
(function () {
    "use strict";
    var LOCALE_CODE = "ar-ae";
    var DICTIONARY_URL = "/etc.clientlibs/myproject/clientlibs/clientlib-locale-ar-ae/resources/i18n/" + LOCALE_CODE + ".json";

    function onInit(guideBridge) {
        guideBridge.registerConfig(guideBridge.ConfigKeys.LOCALE_CONFIG, function (lang) {
            if (lang !== LOCALE_CODE) {
                return;
            }
            return window.FormView.LanguageUtils.loadLang(lang, DICTIONARY_URL);
        });
    }

    function onBridgeStart(event) {
        onInit(event.detail.guideBridge);
        window.removeEventListener("bridgeInitializeStart", onBridgeStart);
    }

    if (window.guideBridge) {
        onInit(window.guideBridge);
    } else {
        window.addEventListener("bridgeInitializeStart", onBridgeStart);
    }
})();
```

>[!TAB ar-ae.json]

This abbreviated JSON illustrates a translated `required` value. It is not a complete deployable dictionary. Translate the full template and reconcile its keys with the installed runtime before using it as `resources/i18n/ar-ae.json`.

```json
{
  "required": "يرجى تعبئة هذا الحقل."
}
```

>[!TAB Guide Localization Service.cfg.json]

Example path: `ui.config/src/main/content/jcr_root/apps/myproject/osgiconfig/config/Guide Localization Service.cfg.json`.

```json
{
  "supportedLocales": [
    "en", "fr", "de", "ja", "pt-br",
    "zh-cn", "zh-tw", "ko-kr", "it", "es", "ar-ae"
  ]
}
```

>[!ENDTABS]

## Get this example

[Download the locale dictionary project-source ZIP](../assets/locale-dictionary-setup-source.zip).

The archive contains client library source, a configuration example, an English dictionary template, an illustrative translated-message snippet, integration instructions, and license notices. It is not a turnkey installer or a complete Arabic form.

The template is copied from the English dictionary in Core Forms Components 1.1.78. Its values are untranslated; compare its complete key set with your installed runtime and translate the values before deployment. Tested on the AEM SDK with Core Components 3.0.172: the dictionary loads and translates the required-field message. This does not verify the archive as a complete hosted deployment or all localized formats.

Follow the archive's `README.md` to integrate the source into your project. Preserve existing configuration and `/etc/languages` values, follow the setup guide for any required language registration, and deploy through your project's pipeline.
