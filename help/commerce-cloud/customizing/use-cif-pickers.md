---
title: Usage of CIF product & category picker
description: Learn how to use CIF product & category picker in your customer commerce components to support authors and marketers to efficiently work with commerce product and catalog data.
sub-product: Commerce
topics: Development
version: cloud-service
activity: develop
audience: developer
feature: Commerce Integration Framework
---

# AEM Content & Commerce Authoring pickers {#cif-pickers}

AEM Content & Commerce Authoring provides a set of authoring tools to help AEM authors and marketers efficiently work with commerce product data and catalogs. The Product Picker and Category Picker are part of CIF add-on and used by the CIF Core Components. Projects can use these pickers in any component dialog to select products or categories.

## Product Picker {#product-picker}

To use the product picker in a project component a developer must add `commerce/gui/components/common/cifproductfield` to a component dialog. For example, use the following for the cq:dialog:

```xml
<product jcr:primaryType="nt:unstructured"
    sling:resourceType="commerce/gui/components/common/cifproductfield"
    fieldDescription="The product or product variant displayed by the teaser"
    fieldLabel="Select Product"
    filter="folderOrProductOrVariant"
    name="./selection"
    selectionId="sku"/>
```

The product field allows to navigation to the product a user want to select via the different views. By default the product field will return the ID of the product, but this can be configured using the `selectionId` attribute.

The product picker field supports the following optional properties:

- selectionId (id, uid, sku, slug, path, combinedSku) - allows to choose the product attribute to be returned by the picker (default = id). Using sku returns the sku of the selected product, while using combinedSku returns a string like base#variant with the skus of the base product and the selected variant, or a single sku if a base product is selected.
- filter (folderOrProduct, folderOrProductOrVariant) - filters the content to be rendered by the picker while navigating the product tree. folderOrProduct - renders folders and products. folderOrProductOrVariant - renders folders, product and product variants. If a product or product variant is rendered it becomes also selectable in the picker. (default = folderOrProduct)
- multiple (true, false) - allows to select one or multiple products (default = false)
- emptyText - to configure the empty text value of the picker field

Additionally, standard diaglog field properties like `name`, `fieldLabel` or `fieldDescription` are supported as well.

The `cifproductfield` component requires the cif.shell.picker clientlib. To add a clientlib to a dialog, you can use the extraClientlibs property.

A full working example of the `cifproductfield` can be found in the [CIF Core Components](https://github.com/adobe/aem-core-cif-components/blob/master/ui.apps/src/main/content/jcr_root/apps/core/cif/components/commerce/productteaser/v1/productteaser/_cq_dialog/.content.xml) project. See also [Customizing Dialogs](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/customizing.html?lang=en#customizing-dialogs) of the AEM Core Components documentation.

## Category Picker {#category-picker}

The category picker (provided by `/libs/`commerce/gui/components/common/cifcategoryfield`) can be used in a component dialog as well in a similar way like the product picker.

The following snippet can be used in a cq:dialog configuration:

```xml
<category jcr:primaryType="nt:unstructured" 
    sling:resourceType="commerce/gui/components/common/cifcategoryfield" 
    fieldLabel="Category" 
    name="./categoryId" 
    selectionId="uid" />
```

The category picker field supports the following optional properties:

- selectionId(id, uid, path, idAndUrlPath, uidAndUrlPath) - allows to choose the category attribute to be returned by the picker (default = id). The idAndUrlPath & uidAndUrlPath are special options that will store the category id/uid and Magento's url_path separated by a | character like for example 1|men/tops.
- multiple (true, false) - allows to select one or multiple categories (default = false)

Additionally, standard diaglog field properties like `name`, `fieldLabel` or `fieldDescription` are supported as well.

Same like the `cifproductfield` component the `cifcategoryfield` component also requires the cif.shell.picker clientlib. To add a clientlib to a dialog, you can use the `extraClientlibs` property. See [Customizing Dialogs](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/customizing.html?lang=en#customizing-dialogs) of the AEM Core Components documentation.

A full working example of the `cifcategoryfield` can be found in the [CIF Core Components](https://github.com/adobe/aem-core-cif-components/blob/master/ui.apps/src/main/content/jcr_root/apps/core/cif/components/commerce/featuredcategorylist/v1/featuredcategorylist/_cq_dialog/.content.xml) project.
