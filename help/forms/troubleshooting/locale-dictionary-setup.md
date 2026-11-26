---
title: Troubleshoot Custom Locale Dictionaries
description: Learn how to troubleshoot custom locale dictionaries for Adaptive Forms based on Core Components, including missing translations and dictionary request errors.
feature: Adaptive Forms, Core Components
role: Developer
level: Intermediate
hide: true
hidefromtoc: true
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms."
---

# Troubleshoot custom locale dictionaries {#troubleshoot-custom-locale-dictionaries}

Use this article to diagnose custom locale dictionary problems in Adaptive Forms based on Core Components in Adobe Experience Manager Forms (AEM Forms) as a Cloud Service. For the complete setup procedure, see [Add a locale for Adaptive Forms based on Core Components](/help/forms/supporting-new-language-localization-core-components.md).

## Issue

Getting labels, validation messages, and formats (dates, numbers, currency) to localize correctly for a new locale on a Core Components Adaptive Form requires two things done together: registering the locale with the Guide Localization Service, and deploying a matching locale client library. Doing only one half, or getting the fallback/ordering rules wrong, leaves the form silently falling back to the default language or throwing 404s for missing locale resources.

## Cause

Localizing a Core Components Adaptive Form's own labels, validation messages, and formats
(dates, numbers, currency) for a new locale requires two separate pieces of configuration to be
done together:

1. The locale code must be registered in `Guide Localization Service.cfg.json`'s
   `supportedLocales` array. Otherwise the server answers the form's request for its
   `<locale>` JSON with another, supported language.
1. A matching locale client library (based on the `clientlib-it-custom-locale` sample in the
   `aem-core-forms-components` GitHub repository) must be deployed, whose `languageinit.js`
   registers a `LOCALE_CONFIG` function that loads this project's own dictionary
   (`FormView.LanguageUtils.loadLang(lang, <this project's dictionary URL>)`), together with the
   dictionary file itself - the runtime ships dictionaries for only ten languages.

Doing only one half reproduces the "still renders in the original language" or "404 on locale
resources" symptom. AEM's locale resolution also has a defined fallback order - full locale to
bare language code to the form's authoring-language dictionary - so adding, removing, or
reordering `supportedLocales` entries changes which dictionary *every* related locale variant
resolves to, not just the one being added. This is what produces the second symptom, where an
unrelated locale starts behaving differently after an edit meant only to add a new one.

## Resolution

1. Add the new locale's code to `supportedLocales` in `Guide Localization Service.cfg.json`
   (correct ISO 639-1 code, plus country code for regional variants), keeping the file valid
   JSON.
1. Clone `aem-core-forms-components` from GitHub and copy its `clientlib-it-custom-locale`
   sample client library into the project's own `ui.apps` clientlibs, renamed/re-categorized for
   the project and locale.
1. Update the `aemLangUrl` path inside the copied `languageinit.js`'s `LOCALE_CONFIG` function to
   the project's own deployed dictionary (the client library needs `allowProxy` so
   `/etc.clientlibs` serves it), add that dictionary with every key of the runtime's `en.json`
   translated, and add the locale to `/etc/languages` as Adobe's guide describes.
1. Deploy through the pipeline and validate by requesting the form with `afAcceptLang` set to
   the new locale code (or the `[locale]` URL selector): the network panel should show the request
   for the project's dictionary - and re-check any existing, closely related locale to confirm its
   fallback behavior did not change.

## Code samples

The following examples use the same paths and category as the downloadable project source. Replace `myproject` with your application ID. Merge the configuration into your existing project rather than replacing its supported locales.

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

The template is copied from the English dictionary in Core Forms Components 1.1.78. Its values are untranslated; compare its complete key set with your installed runtime and translate the values before deployment. The later Core Components 3.0.172 SDK check verified dictionary loading and a translated required-field message, not this archive as a complete hosted deployment or all localized formats.

Follow the archive's `README.md` to integrate the source into your project. Preserve existing configuration and `/etc/languages` values, follow the setup guide for any required language registration, and deploy through your project's pipeline.
