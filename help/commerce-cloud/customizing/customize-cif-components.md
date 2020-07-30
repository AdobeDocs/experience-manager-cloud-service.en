---
title: Customize CIF Core Components
description: Customize CIF Core Components
---

# Customize AEM CIF Core Components {#customize-cif-components}

[AEM CIF Core Components](https://github.com/adobe/aem-core-cif-components) provides a standard set of Commerce components that can be used to accelerate a project that integrates Adobe Experience Manager (AEM) and Magento solutions. These components are production ready and can be [easily styled with CSS](style-cif-component.md). Many implementations will also want to extend these components to meet business specific requirements.

In this tutorial we will review several different extension points provided by AEM CIF Core Components and AEM in general. We will do this by extending the capabilities of the [Product Teaser](https://github.com/adobe/aem-core-cif-components/tree/master/ui.apps/src/main/content/jcr_root/apps/core/cif/components/commerce/productteaser/v1/productteaser) component to include the ability to render a "New" banner. Content authors will have the ability to turn toggle this banner and determine how long to display the banner. The "age" of the product will be based on it's creation date in the Magento catalog. Once a product is a certain amount of days old, the "New" banner should automatically disappear.

 ![New Banner extended](/help/commerce-cloud/assets/customize-cif-components/new-banner-productteaser.png)

## Prerequisites {#prerequisites}

The following tools and technologies are required:

* [Java 1.8](https://www.oracle.com/technetwork/java/javase/downloads/index.html) or [Java 11](https://www.oracle.com/technetwork/java/javase/downloads/jdk11-downloads-5066655.html) (AEM 6.5+ only)
* [Apache Maven](https://maven.apache.org/) (3.3.9 or newer)
* Adobe Experience Manager (local instance)
  * [AEM 6.5](https://docs.adobe.com/content/help/en/experience-manager-65/deploying/introduction/technical-requirements.html)
  * [AEM 6.4.4+](https://docs.adobe.com/content/help/en/experience-manager-64/release-notes/sp-release-notes.html)
* Magento running a [version compatible with Archetype 0.7.0](https://github.com/adobe/aem-cif-project-archetype#requirements)

It is recommended to review the following content before proceeding with this tutorial:

* [Introducing Commerce Integration Framework on AEM as a Cloud Service](/help/commerce-cloud/overview.md)
* [Style AEM CIF Core Components - Tutorial](style-cif-component.md)

## Starter Project

We have provided a starter project to be used with this tutorial. The project was generated using [v0.7.0](https://github.com/adobe/aem-cif-project-archetype/releases/tag/cif-project-archetype-0.7.0) of the CIF Project Archetype. It is considered a best practice to always use the [latest release](https://github.com/adobe/aem-cif-project-archetype/releases/latest) of the archetype when starting a new project.

1. Download the starter project [**acme-store.zip**](/help/commerce-cloud/assets/customize-cif-components/acme-store.zip) to your desktop.

1. Unzip **acme-store.zip** and you should see the following folder structure:

    ```plain
    /acme-store
       /ui.content
       /ui.apps
       /samplecontent
       /core
       /all
       + pom.xml
       + README.md
    ```

1. Open a new terminal window and build and deploy the project to a local instance of AEM;

    ```shell
    $ cd acme-store/
    $ mvn clean install -PautoInstallAll
    ```

1. Add the necessary OSGi configurations to connect your AEM instance to a Magento instance or add the configurations to the newly created project.

1. At this point you should have a working version of a storefront that is connected to a Magento instance. Navigate to the `US` > `Home` page at: [http://localhost:4502/editor.html/content/acme/us/en.html](http://localhost:4502/editor.html/content/acme/us/en.html)

   You should see that the storefront currently is using the Venia theme. Expanding the Main Menu of the storefront, you should see various categories, indicating that the connection Magento is working.

    ![Storefront configured with Venia Theme](/help/commerce-cloud/assets/customize-cif-components/acme-store-configured.png)

## Author the Product Teaser {#author-product-teaser}

We will be extending the Product Teaser Component throughout this tutorial. As a first step, we will add a new instance of the Product Teaser to the Home page in order to understand the baseline functionality.

1. Navigate to the **Home Page** of the site: [http://localhost:4502/editor.html/content/acme/us/en.html](http://localhost:4502/editor.html/content/acme/us/en.html)

1. Insert a new **Product Teaser** Component into the main layout container on the page.

    ![Insert Product Teaser](/help/commerce-cloud/assets/customize-cif-components/product-teaser-add-component.png)

1. Expand the Side Panel (if not already toggled) and switch the asset finder dropdown to **Products**. This should display a list of available products from a connected Magento instance. Select a product and **drag+drop** it onto the **Product Teaser** component on the page.

    ![Drag + Drop Product Teaser](/help/commerce-cloud/assets/customize-cif-components/drag-drop-product-teaser.png)

    > Note, you can also configure the displayed product by configuring the component using the dialog (clicking the *wrench* icon).

1. You should now see a Product being displayed by the Product Teaser. The Name of the product and the Price of the product are default attributes that are displayed.

    ![Product Teaser - default style](/help/commerce-cloud/assets/customize-cif-components/product-teaser-default-style.png)

## Customizing the markup of the Product Teaser {#customize-markup-product-teaser}

A common extension of AEM components is to modify the markup generated by the component. This is done by overriding the [HTL script](https://docs.adobe.com/content/help/en/experience-manager-htl/using/overview.html) that the component uses to render its markup. HTML Template Language (HTL), is a lightweight templating language that AEM components use to dynamically render markup based on authored content, allowing the components to be re-used. The Product Teaser, for example, can be re-used over and over again to display different products. 

In our case we want to render a banner on top of the teaser to indicate that the product is "New" and has been recently added to the catalog. The design pattern for [customizing the markup](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/developing/customizing.html#customizing-the-markup) of a component is actually standard for all AEM Components, not just for the AEM CIF Core Components.

Use the IDE of your choice to [open the starter project downloaded](https://docs.adobe.com/content/help/en/experience-manager-learn/foundation/development/set-up-a-local-aem-development-environment.html#set-up-an-integrated-development-environment) at the beginning of the tutorial.

1. Navigate and expand the **ui.apps** module and expand the folder hierarchy to: `ui.apps/src/main/content/jcr_root/apps/acme/components/commerce/productteaser` and inspect the `.content.xml` file.

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <jcr:root xmlns:sling="http://sling.apache.org/jcr/sling/1.0" xmlns:cq="http://www.day.com/jcr/cq/1.0" xmlns:jcr="http://www.jcp.org/jcr/1.0"
        jcr:description="Product Teaser Component"
        jcr:primaryType="cq:Component"
        jcr:title="Product Teaser"
        sling:resourceSuperType="core/cif/components/commerce/productteaser/v1/productteaser"
        componentGroup="acme"/>
    ```

    Above is the Component definition for the Product Teaser Component in our project. Notice the property `sling:resourceSuperType="core/cif/components/commerce/productteaser/v1/productteaser"`. This is an example of creating a [Proxy component](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/get-started/using.html#create-proxy-components). Instead of copying and pasting all of the Product Teaser HTL scripts from the AEM CIF Core Components, we can use the `sling:resourceSuperType` to inherit all of the functionality.

1. Open a new browser and navigate to [CRXDE-Lite](http://localhost:4502/crx/de/index.jsp#/apps/core/cif/components/commerce/productteaser/v1/productteaser) in AEM. Expand the tree to view the `productteaser` component under: `/apps/core/cif/components/commerce/productteaser/v1/productteaser`:

    ![CRXDE Lite Product Teaser](/help/commerce-cloud/assets/customize-cif-components/crxde-productteaser.png)

    This is the full component definition for the Product Teaser component.

1. Switch back to your IDE and the Acme Store project. Create a new file named `productteaser.html` beneath `ui.apps/src/main/content/jcr_root/apps/acme/components/commerce/productteaser`.

1. Copy the contents of `productteaser.html` from [CRXDE-Lite](http://localhost:4502/crx/de/index.jsp#/apps/core/cif/components/commerce/productteaser/v1/productteaser/productteaser.html) and paste it into the Acme-Store project in the newly created `productteaser.html` file.

    ![Product Teaser html overwrite](/help/commerce-cloud/assets/customize-cif-components/productteaser-html-overwrite.png)

1. In the Acme-Store project modify the `productteaser.html` file and insert a new div that represents a badge  above the product image markup:

    ```html
    ...
    <div data-sly-test.isvalid="${product.url}" class="item__root" data-cmp-is="productteaser">
        <!-- Add Badge -->
        <div class="item__badge">
            <span>New</span>
        </div>
        <!-- end add badge -->
        <a class="item__images" href=${product.url}>
            <img class="item__image" width="100%" height="100%"
                    src="${product.image}" alt="${product.image}"/>
        </a>
        <a class="item__name" href=${product.url}><span>${product.name}</span></a>
        <div class="item__price">
            <span> ${product.formattedPrice} </span>
        </div>
        <sly data-sly-call="${actionsTpl.actions @ product=product}"></sly>
    </div>
    ```

1. Deploy the updated code to the local instance of AEM using your maven skills or using [the features of your IDE](https://docs.adobe.com/content/help/en/experience-manager-learn/foundation/development/set-up-a-local-aem-development-environment.html#set-up-an-integrated-development-environment):

    ```shell
    $ cd ui.apps
    $ mvn -PautoInstallPackage clean install
    ```

1. In the browser, return to the [Homepage of the store front](http://localhost:4502/editor.html/content/acme/us/en.html) in AEM. Refresh and you should see that a "new" Banner appears in the upper right corner of the component.

    ![New Banner extended](/help/commerce-cloud/assets/customize-cif-components/new-banner-productteaser.png)

    Currently there is no logic behind when the banner will be displayed. In the next few exercises we will correct that.

    > Note, the CSS to render the banner was provided as part of the starter project and can be found at: `ui.apps/../apps/acme/clientlibs/theme/components/productteaser/teaser.css`. For more details checkout the [Styling CIF Core Components tutorial](style-cif-component.md).

## Customizing the Dialog of the Product Teaser {#customize-dialog-product-teaser}

Next, we will customize the dialog of the Product Teaser component to allow an Author to determine the date range for which a product is considered "new" and if the banner should be displayed. We will do this by [customizing the dialog](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/developing/customizing.html#customizing-dialogs) of the Product Teaser as part of the Acme Store project.

1. Open the Acme Store project in the IDE of your choice and navigate to `ui.apps/src/main/content/jcr_root/apps/acme/components/commerce/productteaser`.

1. Beneath the `productteaser` folder, add a new folder named `_cq_dialog`. Add a new file to the `_cq_dialog` folder named `.content.xml`. You should now have the following file structure:

    ```plain
    ../acme
        /components
            /commerce
                /productteaser
                   /_cq_dialog
                      + .content.xml
                   /_cq_template
                   + .content.xml
                   + productteaser.html
    ```

1. Update `_cq_dialog/.content.xml` with the following XML:

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <jcr:root xmlns:sling="http://sling.apache.org/jcr/sling/1.0" 
        xmlns:cq="http://www.day.com/jcr/cq/1.0" 
        xmlns:jcr="http://www.jcp.org/jcr/1.0" 
        xmlns:nt="http://www.jcp.org/jcr/nt/1.0" 
        jcr:primaryType="nt:unstructured" 
        jcr:title="My Product Teaser" 
        sling:resourceType="cq/gui/components/authoring/dialog" 
        trackingFeature="cif-core-components:productteaser:v1">
        <content jcr:primaryType="nt:unstructured" 
            sling:resourceType="granite/ui/components/coral/foundation/container">
            <items jcr:primaryType="nt:unstructured">
                <tabs jcr:primaryType="nt:unstructured" 
                    sling:resourceType="granite/ui/components/coral/foundation/tabs" 
                    maximized="{Boolean}true">
                    <items jcr:primaryType="nt:unstructured">
                        <badge jcr:primaryType="nt:unstructured" 
                            jcr:title="Badge" 
                            sling:resourceType="granite/ui/components/coral/foundation/container" 
                            margin="{Boolean}true">
                            <items jcr:primaryType="nt:unstructured">
                                <columns jcr:primaryType="nt:unstructured" 
                                    sling:resourceType="granite/ui/components/coral/foundation/fixedcolumns" 
                                    margin="{Boolean}true">
                                    <items jcr:primaryType="nt:unstructured">
                                        <column jcr:primaryType="nt:unstructured" 
                                            sling:resourceType="granite/ui/components/coral/foundation/container">
                                            <items jcr:primaryType="nt:unstructured">
                                                <badge jcr:primaryType="nt:unstructured" 
                                                    sling:resourceType="granite/ui/components/coral/foundation/form/checkbox" 
                                                    text="Display 'New' badge" 
                                                    value="true" 
                                                    uncheckedValue="false" 
                                                    name="./badge" />
                                                <age jcr:primaryType="nt:unstructured" 
                                                    sling:resourceType="granite/ui/components/coral/foundation/form/numberfield" 
                                                    fieldDescription="The maximum age in days the 'new' badge should be shown" 
                                                    fieldLabel="Max Product Age" 
                                                    name="./age"
                                                    min="{Long}0" 
                                                    value="10" />
                                                <ageTypeHint jcr:primaryType="nt:unstructured" 
                                                    sling:resourceType="granite/ui/components/foundation/form/hidden" 
                                                    ignoreData="{Boolean}true" 
                                                    name="./age@TypeHint" 
                                                    value="Long" />
                                            </items>
                                        </column>
                                    </items>
                                </columns>
                            </items>
                        </badge>
                    </items>
                </tabs>
            </items>
        </content>
    </jcr:root>
    ```

    Above we have added 2 additional fields as part of a new tab and a single hidden field.

    1. Checkbox to Display 'New' badge
    2. Number field to define the Max Product Age
    3. Hidden field to ensure that the Max Product Age is saved as a long (see [@TypeHint](https://sling.apache.org/documentation/bundles/manipulating-content-the-slingpostservlet-servlets-post.html) for more details)

    Dialogs defined as part of a proxy component inherit all of the existing dialog fields with a feauture known as [Sling Resource Merger](https://helpx.adobe.com/experience-manager/6-4/sites/developing/using/sling-resource-merger.html). Therefore we con't have to re-define the existing fields that are part of the Product Teaser.

4. Update `productteaser.html` and add a `data-sly-test` to the `<div>` for the badge. This will be a simple test to decide to render the badge if the user has checked "true".

    ```html
        ...
        <div data-sly-test.isvalid="${product.url}" class="item__root" data-cmp-is="productteaser">

            <!--/* add test to see if properties.badge equals true */-->
            <div data-sly-test="${properties.badge == 'true'}" class="item__badge">
                <span>New</span>
            </div>
    ...
    ```

5. Deploy the updated code to the local instance of AEM using features of your IDE or by using your maven skills:

    ```shell
    $ cd ui.apps
    $ mvn -PautoInstallPackage clean install
    ```

6. Return to the Product Teaser component and click the *wrench* icon to open the Dialog. You should now see a tab for **Badge** with two additional fields. Updating these fields will persist the values to AEM. You should be able to toggle on/off the badge with the checkbox:

    ![Toggle badge](/help/commerce-cloud/assets/customize-cif-components/toggle-badge-checkbox.gif)

    This gives the author some control over when the badge appears. However it would be ideal for the badge to disappear automatically once the product has reached a certain age in day based on the entry for **Max Product Age**. For this we will need to implement some backend logic.

## Updating the Sling Model for the Product Teaser

Next, we will extend the business logic of the Product Teaser by implementing a Sling Model. [Sling Models](https://sling.apache.org/documentation/bundles/models.html), are annotation driven "POJOs" (Plain Old Java Objects) that implement any of the business logic needed by the component. Sling Models are used in conjunction with the HTL scripts as part of the component. We will follow the [delegation pattern for Sling Models](https://github.com/adobe/aem-core-wcm-components/wiki/Delegation-Pattern-for-Sling-Models) so that we can just extend parts of the existing Product Teaser model.

Sling Models are implemented as Java and can be found in the **core** module of the generated project.

1. Open the Acme Store project in the IDE of your choice and navigate under the **core** module to: `core/src/main/java/com/acme/cif/core/models/MyProductTeaser.java`. **MyProductTeaser.java** is a Java Interface that we pre-created that extends the CIF **ProductTeaser** interface.

2. Next, open the file **MyProductTeaserImpl.java** located at: `core/src/main/java/com/acme/cif/core/models/MyProductTeaserImpl.java`. `MyProductTeaserImpl` is the implementation class for the interface `MyProductTeaser`. 

    Using the [delegation pattern for Sling Models](https://github.com/adobe/aem-core-wcm-components/wiki/Delegation-Pattern-for-Sling-Models) we can reference the `ProductTeaser` class via the `sling:resourceSuperType` property: 

    ```java
    @Self
    @Via(type = ResourceSuperType.class)
    private ProductTeaser productTeaser;
    ```

    For all of the methods that we don't want to override or change, we can simply return the value that the `ProductTeaser` returns:

    ```java
    @Override
    public String getImage() {
        return productTeaser.getImage();
    }
    ```

3. One of the extra extension points provided by AEM CIF Core Components is the `AbstractProductRetriever` which allows us to get access to specific product attributes. Add the following method to initialize the `AbstractProductRetriever` in the `init()` method:

    ```java
    import javax.annotation.PostConstruct;
    ...
    @Model(adaptables = SlingHttpServletRequest.class, adapters = MyProductTeaser.class, resourceType = MyProductTeaserImpl.RESOURCE_TYPE)
    public class MyProductTeaserImpl implements MyProductTeaser {
        ...
        private AbstractProductRetriever productRetriever;

        /* add this method to intialize the proudctRetriever */
        @PostConstruct
        public void initModel() {
            productRetriever = productTeaser.getProductRetriever();

        }
    ...

    ```

4. Lets test out these changes by modifying the formatted price and overriding the logic in `getFormattedPrice()`. Make the following updates so that we explicitly format the price based on the German locale. (or pick a different country!)

    ```java
    import java.util.Locale;
    import java.text.NumberFormat;
    ...

    @Override
    public String getFormattedPrice() {
         //return productTeaser.getFormattedPrice();
        NumberFormat germanCurrencyFormat = NumberFormat.getCurrencyInstance(Locale.GERMANY);
        Double price =  productRetriever.fetchProduct().getPrice().getRegularPrice().getAmount().getValue();
        if(price != null) {
            return germanCurrencyFormat.format(price);
        }
        return null;
    }
    ```

    Note how the `productRetriever` object gives us access to the `ProductInterface` object via the `fetchProduct()` method. You can see all of the [available methods here](https://github.com/adobe/commerce-cif-magento-graphql/blob/master/src/main/java/com/adobe/cq/commerce/magento/graphql/ProductInterface.java).

    > Note* modifying the locale to German is just a fun example to see the override. In reality the ProductTeaser uses the [page's locale to determine the format](https://github.com/adobe/aem-core-cif-components/blob/master/bundles/core/src/main/java/com/adobe/cq/commerce/core/components/internal/models/v1/productteaser/ProductTeaserImpl.java#L173).

5. Next we need to update the **productteaser.html** in the **ui.apps** module to reference our new Sling Model at: `com.acme.cif.core.models.MyProductTeaser`.

    ```diff
      <!--/* productteaser.html - change the use.product to point to MyProductTeaser */-->
      <sly data-sly-use.clientlib="/libs/granite/sightly/templates/clientlib.html"
    -  data-sly-use.product="com.adobe.cq.commerce.core.components.models.productteaser.ProductTeaser"
    +  data-sly-use.product="com.acme.cif.core.models.MyProductTeaser"
       data-sly-use.actionsTpl="actions.html">
        ...
     ```

    Save the changes to `productteaser.html`.

6. Deploy the code base to the local instance of AEM. Since changes were made to both the **ui.apps** and **core** modules, build and deploy the project from the root:

    ```shell
    $ cd acme-store
    $ mvn -PautoInstallPackage clean install
    ```

7. Open a browser and navigate to: [http://localhost:4502/system/console/status-slingmodels](http://localhost:4502/system/console/status-slingmodels). This console shows all of the Sling Models registered in the system. Double-check to ensure the MyTeaserModelImpl got deployed and is mapped correctly. You should be able to see something like:

    ```plain
    com.acme.cif.core.models.MyProductTeaserImpl - acme/components/commerce/productteaser
    ```

8. Finally navigate to where you authored the Product Teaser component and you should now see the price with the German currency format:

    ![Price Format Updated](/help/commerce-cloud/assets/customize-cif-components/german-currency-update.png)

## Implement isShowBadge logic {#implement-isshowbadge}

Now that we have had a chance to experiment with overriding the Sling Model methods, lets implement the logic for when to display the "new" badge.

1. Return to your IDE and open the **MyProductTeaser.java** file at: `core/src/main/java/com/acme/cif/core/models/MyProductTeaser.java`.

1. Add a new method, `isShowBadge()` to the interface:

    ```java
    @ProviderType
    public interface MyProductTeaser extends ProductTeaser {
        // Extend the existing interface with the additional properties which you
        // want to expose to the HTL template.
        public Boolean isShowBadge();
    }
    ```

    This is a new method we will introduce to encapsulate the logic of whether to show the badge or not.

1. Next, re-open **MyProductTeaserImpl.java** at `core/src/main/java/com/acme/cif/core/models/MyProductTeaserImpl.java`.

1. The logic for how long the "new" badge will be displayed will be based on the `created_at` attribute of the Product. In order to have access to that attribute, we need to extend the **GraphQL** query performed by the ProductTeaser. We can do this by updating the `init()` method in **MyProductTeaserImpl.java**:

    ```java
    //MyProductTeaserImpl.java

    @PostConstruct
    public void initModel() {
        productRetriever = productTeaser.getProductRetriever();

        if (productRetriever != null) {
            // Pass your custom partial query to the ProductRetriever. This class will
            // automatically take care of executing your query as soon
            // as you try to access any product property.
            productRetriever.extendProductQueryWith(p ->
                p.addCustomSimpleField("created_at")
            );
        }
    }
    ```

      Adding to the `extendProductQueryWith` method is a powerful way to ensure additional product attributes are available to the rest of the model. It also minimizes the number of queries executed.

      >[!NOTE]
      >In the above code we are using the`addCustomSimpleField` to retrieve the `created_at` property. This illustrates how you can query for any custom attributes that are part of the Magento schema.
      >
      > However, the `created_at` property has actually been implemented as part of the [Product Interface](https://github.com/adobe/commerce-cif-magento-graphql/blob/master/src/main/java/com/adobe/cq/commerce/magento/graphql/ProductInterface.java) and a better practice would be to re-use the method like the so: `productRetriever.extendProductQueryWith(p -> p.createdAt());`. Most of the commonly found schema attributes have been implemented, so only use the `addCustomSimpleField` for truly custom attributes.

1. Next, we will implement the `isShowBadge()` method:

    ```java
    import java.time.format.DateTimeFormatter;
    import java.util.Locale;
    import java.time.temporal.ChronoUnit;

    ...

    @Override
    public Boolean isShowBadge() {
         final DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

         //Look at the checkbox from the dialog to see if we should even attempt to show the badge
         final boolean showBadge = properties.get("badge", false);
         if (showBadge) {

             //Look at the numberfield set from the dialog to determine the max "age" in days to compare too
             final int maxAgeProp = properties.get("age", 0);

            String createdAtString;
            try {
                //Grab the created_at property from the product
                //Here we show the example of retrieving the attribute as if it was a custom attribute
                // an alternative that would work is productRetriever.fetchProduct().getCreatedAt()
                createdAtString = productRetriever.fetchProduct().getAsString("created_at");
                log.info("***CREATED_AT**** " + createdAtString);
            } catch (SchemaViolationError e) {
                //it is possible that a schema error could be thrown if the attribute is not part of the schema
                log.error("Error determining to showBadge" , e);
                return false;
            }

             // Custom code to calc the date difference of the product creation
             // compared to today
            final LocalDate createdAt = LocalDate.parse(createdAtString, formatter);
             if (createdAt != null) {
 
                 final long ageInDays = ChronoUnit.DAYS.between(createdAt, LocalDate.now());
                 if (ageInDays < maxAgeProp) {
                     return true;
                 }
             }
         }
         return false;
     }

    ```

    In the above method we first check to see if the author has enabled the badge functionality with the checkbox. Next we read in the value of the property `age` that is set as part of the dialog and represents the maximum number of days old a product should be until the banner disappears. Finally we calculate how old the product is based on the `created_at` date. If after comparing the two values we return `true` to show the badge, `false` in all other cases.

1. Finally one more addition needs to be made to the `productteaser.html` script in order to call the `isShowBadge()` method. Open the file at `ui.apps/src/main/content/jcr_root/apps/acme/components/commerce/productteaser/productteaser.html`. Make the following update:

    ```diff
    ...
    - <div data-sly-test="${properties.badge == 'true'}" class="item__badge">
    + <div data-sly-test="${product.showBadge}" class="item__badge">
         <span>New</span>
     </div>
    ...
    ```

1. Deploy the code base to the local instance of AEM. Since changes were made to both the **ui.apps** and **core** modules, build and deploy the project from the root:

    ```shell
    $ cd acme-store
    $ mvn -PautoInstallPackage clean install
    ```

1. Return to AEM and the ProductTeaser component and experiment with different numbers to display the product's max age. Depending on how old the product is, you may need to enter some very large numbers to get the badge to display.

    ![Max Product Age 999](/help/commerce-cloud/assets/customize-cif-components/max-age-working.png)

1. Finally, search the AEM logs to see the log statement entered in step 5 above. This should print the value of the `created_at` property that is coming from Magento. You can view the logs of AEM by opening the `error.log` file. This file is located beneath the `crx-quickstart/logs/error.log` where the AEM jar has been installed. You can expect to see a line item like the following:

    ```plain
    com.acme.cif.core.models.MyProductTeaser ***CREATED_AT**** 2019-06-05 06:51:33
    ```

    Now you can verify that the logic we implemented is correct!

### Congratulations {#congratulations}

You just customized your first AEM CIF component! Download the [finished solution package here](/help/commerce-cloud/assets/customize-cif-components/acme-store-solution.zip).

## Additional Resources {#additional-resources}

* [AEM Archetype](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/developing/archetype/overview.html)
* [AEM CIF Core Components](https://github.com/adobe/aem-core-cif-components)
* [Customizing AEM CIF Core Components](https://github.com/adobe/aem-core-cif-components/wiki/Customizing-CIF-Core-Components)
* [Customizing Core Components](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/developing/customizing.html)
