---
title: AEM-CIF core components and Adobe Experience Platform integration
description: Learn how to forward AEM-CIF core component created client-side events to Adobe Experience Platform using CIF Experience Platform Connector.
sub-product: Commerce
version: Cloud Service
activity: setup
feature: Commerce Integration Framework
topic: Commerce
role: Architect, Developer
level: Beginner
kt: 10834
thumbnail: 346811.jpeg
---

# AEM-CIF core components and Adobe Experience Platform integration {#aem-cif-aep-integration}

The [Commerce Integration Framework (CIF)](https://github.com/adobe/aem-core-cif-components) core components provides seamless integration to forward events from the client-side interactions to [Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/landing/platform-overview.html?lang=en). 

The [CIF Core Components](https://github.com/adobe/aem-core-cif-components/tree/master/react-components) project provides an [Experience Platform Connector](https://github.com/adobe/aem-core-cif-components/tree/master/extensions/experience-platform-connector), this JavaScript library collects Storefront events and sends event data to Experience Platform. This event data is used in other Adobe Experience Cloud products, such as Adobe Analytics and Adobe Target to build a 360 profile that covers a customer journey. Thus by connecting Commerce data to other products in the Adobe Experience Cloud, you can perform tasks, such as analyze user behavior on your site, perform AB testing, and create personalized campaigns.

Learn more about [Experience Platform Data Collection](https://experienceleague.adobe.com/docs/experience-platform/collection/home.html) a suite of technologies that allow you to collect customer experience data from client-side sources 

## Send `addToCart` event data to Experience Platform {#send-addtocart-to-aep}

Following steps demonstrates how to send the `addToCart` event data from the AEM rendered product-pages to Experience Platform using the CIF - Experience Platform Connector. Using [Adobe Experience Platform Debugger](https://experienceleague.adobe.com/docs/experience-platform/debugger/home.html?lang=en) browser extension you can test, review the submitted data.

![Review addToCart event data in Adobe Experience Platform Debugger](../assets/AEP-Debugger-AddToCart-EventData.png)

## Prerequisites {#prerequisites}

A local development environment is required to complete this tutorial. This includes a running instance of AEM that is configured and connected to an Adobe Commerce instance. Review the requirements and steps for [setting up a local development with AEM as a Cloud Service SDK](../develop.md).

You also need access to [Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/landing/platform-ui/ui-guide.html) and permissions to create schema, dataset, and datastreams for data collection, for more information see [Permission management](https://experienceleague.adobe.com/docs/experience-platform/collection/permissions.html).


## Local setup

Follow the [Local Setup](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/content-and-commerce/storefront/developing/develop.html?#local-setup) steps to have a working AEM as a Cloud Service environment.

## Project setup

Follow the [AEM Project Archetype](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/content-and-commerce/storefront/developing/develop.html?#project) steps to create a brand new CIF project. 

>[!TIP]
>
>In, below example this CIF project is named as `My Demo Storefront` or you can pick project name of your choice.

![AEM CIF Project](../assets/aem-project-with-commerce.png)


Build and deploy the newly created CIF project to the local AEM SDK by running below command from the project's root directory.

```bash
$ mvn clean install -PautoInstallSinglePackage
```

The locally deployed `My Demo StoreFront` site with default code and content looks like below.

![Default AEM CIF Site](../assets/demo-aem-storefront.png)


## Install Peregrine and CIF-AEP connector dependencies

In order to collect and send the events data from the category, product pages that are delivered from the AEM we need to install a few `npm` packages into the `ui.frontend` module of the CIF project.

Navigate to `ui.frontend` module and install packages by running following command

```bash
npm i --save lodash.get@^4.4.2 lodash.set@^4.3.2
npm i --save apollo-cache-persist@^0.1.1
npm i --save redux-thunk@~2.3.0
npm i --save @adobe/apollo-link-mutation-queue@~1.1.0
npm i --save @magento/peregrine@~12.5.0
npm i --save @adobe/aem-core-cif-react-components --force
npm i --save-dev @magento/babel-preset-peregrine@~1.2.1
npm i --save @adobe/aem-core-cif-experience-platform-connector --force
```

>[!IMPORTANT]
>
>The `--force` argument is required sometimes as [PWA Studio](https://developer.adobe.com/commerce/pwa-studio/) is restrictive with the supported peer dependencies. Usually this should not cause any issues.


## Configure Maven to use `--force` argument

As part of Maven builds the npm clean install (using `npm ci`) is run, thus it also needs the `--force` argument. 

Navigate to the project's root POM file `pom.xml` and locate the `<id>npm ci</id>` execution block, and update it to look like below

```xml
    <execution>
        <id>npm ci</id>
        <goals>
        <goal>npm</goal>
        </goals>
        <configuration>
        <arguments>ci --force</arguments>
        </configuration>
    </execution>
```

## Change Babel configuration format

Switch from the default `.babelrc` file relative configuration file format to `babel.config.js` format. This is a project-wide configuration format and allows the plugins and presets to be applied to the `node_module` with greater control.

-   From `ui.frontend` module, delete the existing `.babelrc` file

-   Create a new `babel.config.js` file that makes use of the peregrine preset

    ```javascript
    const peregrine = require('@magento/babel-preset-peregrine');
    
    module.exports = (api, opts = {}) => {
        const config = {
            ...peregrine(api, opts),
            sourceType: 'unambiguous'
        } 
    
        config.plugins = config.plugins.filter(plugin => plugin !== 'react-refresh/babel');
    
        return config;
    }
    ```

## Configuration webpack to use `babel-loader` to transpile JS files

To transpile the JavaScript files using Babel and webpack, tweak the `webpack.common.js` file.

From `ui.frontend` module, update the `webpack.common.js` file

```javascript
    {
        test: /\.jsx?$/,
        exclude: /node_modules\/(?!@magento\/)/,
        loader: 'babel-loader'
    }
```



## Background {#prerequisites}

The [Experience Platform Connector](https://github.com/adobe/aem-core-cif-components/tree/master/extensions/experience-platform-connector) is built on top of [Magento Experience Platform Connector](https://marketplace.magento.com/magento-experience-platform-connector.html) which is part of the [PWA Studio](https://developer.adobe.com/commerce/pwa-studio/) project to create Progressive Web Application (PWA) storefronts powered by Adobe Commerce or Magento Open Source.

The PWA Studio project also contains a component library called [Peregrin](https://developer.adobe.com/commerce/pwa-studio/api/peregrine/) for adding logic to visual components. The [Peregrin library](https://developer.adobe.com/commerce/pwa-studio/api/peregrine/) also provides the custom React hooks which are used by [Experience Platform Connector](https://github.com/adobe/aem-core-cif-components/tree/master/extensions/experience-platform-connector) to integrate with Experience Platform seamlessly. 


## Supported Events

As of now following events are supported

- addToCart
- pageView
- customUrl
- referrerUrl
