---
title: Internationalizing UI Strings
description: AEM provides a console for managing the various translations of texts used in component UI.
solution: Experience Manager, Experience Manager Sites
feature: Developing
role: Developer
---

# Using Translator to Manage Dictionaries{#using-translator-to-manage-dictionaries}

AEM provides a console for managing the various translations of texts used in component UI. This console is available at:

`https://<hostname>:<port-number>/libs/cq/i18n/gui/translator.html`

Use the translator tool to manage English strings and their translations. The dictionaries are created in the repository, for example, `/apps/myproject/i18n`.

The Translator tool and the dictionaries that you manage are for presenting component UI in different languages. If you want to translate pages, see [Translating Content for Multilingual Sites](/help/sites-cloud/administering/translation/overview.md).

## Creating a Dictionary {#creating-a-dictionary}

Developers can create i18n dictionaries in AEM to manage localized component strings. Dictionaries are typically part of component code in `/apps`. Following is an example from the AEM WKND code with one key/value pair that is used in all WKND components.  

   ```
   {
     "&copy; {0} WKND Site Site. All rights reserved." : "&copy; {0} WKND Site Site. Tous droits réservés."
   }
   ```

Developers can create additional dictionaries by adding a root node (`sling:Folder`) for a new dictionary to hold language definitions for component strings.

   ```shell
   /apps/myProject/i18n [sling:Folder]
       - de.json [nt:file] [mix:language]
           + jcr:language = de
       - fr.json [nt:file] [mix:language]
           + jcr:language = fr
   ```

   >[!NOTE]
   >
   >This is the structure from the [Sling i18n module](https://sling.apache.org/site/internationalization-support.html).

Once created in an AEM GitHub repository, dictionaries can be deployed via an AEM [CI/CD pipeline](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md). 

## Dictionary Locations {#dictionary-locations}

Developers are free to create a source language dictionary in either `/apps` or `/content/cq:i18n`. By starting with AEM archetype sample code, initial dictionaries are typically located in the `/apps` path. If a goal is to store corresponding dictionary language copies also in `/apps`, then those language copies have to be manually created and maintained by developers in component code. 

Alternatively, the new AEM runtime translation process for i18n dictionaries will create translated dictionaries in `/content/cq:i18n/<projectName>`, regardless if the source dictionary is stored in `/apps` or `/content`. 

Decisions where to locate i18n dictionaries, source and language copies, should be made using the following criteria:

* `/apps`
   * default location for dictionaries with component string translations, following AEM archetype and WKND sample code 
   * highest rendering order, per Sling ([Resource Bundle Search Hierarchies](https://sling.apache.org/documentation/bundles/internationalization-support-i18n.html#resourcebundle-hierarchies)) 
   * but no runtime editing or translation of dictionaries possible, as `/apps` is immutable in AEM as a Cloud Service environments 

* `/content/cq:i18n`
   * alternative location for i18n dictionaries if
      * runtime translation of dictionaries is required 
      * ability to edit a dictionary at runtime is required 
   * default location where runtime dictionary translation will create language copies.

Because `/apps` always supersedes `/content` in the Sling rendering order, it is important to keep in mind that dictionaries with identical key/value pairs must not exist simultaneously in `/apps` and `/content/cq:i18n`, as the dictionary in `/content/cq:i18n` will never be used for rendering. If a dictionary language copy, i.e. translation destination, already exists in `/apps`, and the goal is to make it translatable at runtime in AEM as a Cloud Service, then the original dictionary language copy in `/apps` has to either be  moved to `/content/cq:i18n`, or to be deleted in `/apps` and automatically recreated in `/content/cq:i18n` by translating the source dictionary. This translation process will automatically create the language copies in `/content/cq:i18n`. 

## Automatic Dictionary Creation {#automatic-creation}

For AEM pages and experience fragments containing AEM core components, the new dictionary translation process will also scan those pages or experience fragments for components and component strings that should be translated. The system will then automatically create corresponding new dictionary language copies in `/content/cq:i18n`. This does not apply for content fragments as those are pure, structured content without the use of AEM core components. 

## Exporting a Dictionary {#exporting-a-dictionary}

While runtime translation of i18n dictionaries in `/apps` or `/libs` locations is not possible in AEM as a Cloud Service as those locations are immutable, those dictionaries can still be exported at runtime for asynchronous translation outside of AEM. 

To export the source language strings of a dictionary to an XLIFF file:

1. Open the Translation tool `http://<host>:<port>/libs/cq/i18n/gui/translator.html`

   >[!NOTE]
   >
   >The tool is only available via this URL, it cannot be accessed from the AEM product UI.

1. Use the Dictionaries drop-down menu to select the dictionary to export.
1. Click Export XLIFF Translation and then Export full `<locale>` xliff.
 
## Importing a Dictionary {#importing-a-dictionary}

To Import an XLIFF file into a dictionary to populate the dictionary content:

1. Open the Translation tool `http://<host>:<port>/libs/cq/i18n/gui/translator.html`
1. Click Import and then XLIFF Translations.
1. Select the file to import and click OK.
