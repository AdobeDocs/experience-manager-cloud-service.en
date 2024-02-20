---
title: Getting Started with AEM Forms Edge Delivery Service
description: Craft perfect forms, fast! ⚡ AEM Forms Edge Delivery + doc-based authoring = blazing speed & SEO-friendly forms for happier users & search engines.
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
---

# Getting Started

In today's digital age, creating user-friendly forms is essential for any organization. AEM Forms Edge Delivery's lets you create forms using familiar tools like Word or Google Docs. These forms submit data directly to a Microsoft Excel or Google Sheets file, enabling you to use vibrant ecosystem and robust APIs of Google Sheets, Microsoft Excel, and Microsoft Sharepoint to easily process submitted data or to initiate an existing business workflow.

## Prerequisites

* You have a Github account. 
* You have access to Google Sheets or Microsoft Excel and Microsoft SharePoint.
* You understand the basics of Git, HTML, CSS, and JavaScript.
* You have Node and NPM installed for local development.

## Before you start

* Set up and clone your an Edge Delivery Service (EDS) project. See [developer tutorial](https://www.aem.live/developer/tutorial) for details. 
* Clone the [Forms Block repository](https://github.com/adobe/afb). It includes the Form block which is necessary to render the form.

![Getting Started with Edge Delivery Forms](/help/edge/assets/getting-started-with-eds-forms.png)

## 1. Add the Form block to your Edge Delivery Service (EDS) project {#add-forms-block-to-an-eds-project}

AEM Forms Edge Delivery includes a Form block to help you easily create forms to capture and store captured data. To include the Form block to your Edge Delivery Service project:  

1. Navigate to your Edge Delivery Service (EDS) project folder on your local development environment. 


    ```Shell 

    cd [EDS Project folder]

    ```

1. Create a folder named `form` under the EDS project directory. For example, under the directory for the EDS project named `Portal`, create a folder named `form`. 

    ```Shell 

    mkdir form

    ```


1. Add the [Forms Block](https://github.com/adobe/afb/tree/main/blocks/form) files to the 'form' folder. 

    ```shell

    cp -R <source:path of the form block> <destination: path of the form folder created in the previous step>

    For example

    cp -R Documents/afb/blocks/form Documents/portal/blocks/

    ```

1. Check-in the 'form' folder and underlying files to your Edge Delivery Service project on GitHub. 

    ```Shell 

    git add .
    git commit -m "Added form block"
    git push origin

    ```

    You are now ready to render an EDS form. 

    >[!NOTE] 
    >
    > * If your pull request/eds project build fails and you encounter an error related to importing the `franklin-lib.js` file, update the import statement to reference the `aem.js` file instead of the `franklin-lib.js` file.
    > * If you encounter any linting errors, feel free to disregard them. To bypass the linting checks, navigate to the package.json file and update the "lint" script from `"lint": "npm run lint:js && npm run lint:css"` to `"lint": "echo 'skipping linting for now'"`. Then, commit the changes to the package.json file.

## 2. Create a form in your Edge Delivery Service (EDS) project {#create-a-form-for-an-eds-project}

Allowing website developers to create forms and choose what information to collect from website visitors can be helpful. Instead of complex processes, authors can easily set up a form using a spreadsheet. They need to add the right column headers, and then use a form block to display it on the website without any hassle. To create a form: 

1. Create a Microsoft Excel Workbook or Google Sheet anywhere under your AEM Edge Delivery project directory on Microsoft SharePoint or Google Drive.

1. Make sure the AEM user (for example `helix@adobe.com`) configured for your project has editing permissions for the sheet.

1. Open the workbook that you have created and change the name of the default sheet to "shared-default". 

    ![rename default sheet to "shared-default"](/help/edge/assets/rename-sheet-to-helix-default.png)

1. Copy the contents of the [contact us spreadsheet](https://docs.google.com/spreadsheets/d/12jvYjo1a3GOV30IqPY6_7YaCQtUmzWpFhoiOHDcjB28/edit?usp=drive_link) to your own spreadsheet. 

    ![contact us spreadsheet](/help/edge/assets/contact-us-form-spreadsheet.png)

1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview and publish the sheet. 

    On previewing and publishing, the browser opens new tabs that display the sheet's contents in JSON format. Make sure to take note of the live URL, as it is necessary for rendering the form later on.

    The format of the URL is:

    ```shell

    https://<branch>--<repository>--<owner>.hlx.live/<form>.json

    For example, https://main--portal--wkndforms.hlx.live/contact-us.json

    ```

## 3. Add the form to your Edge Delivery Service (EDS) page {#add-a-form-to-your-eds-page}

Till now, you have enabled the form block for your EDS project and prepared the structure of the form. Now, to include the form to your EDS page and render it:

1. Go to your AEM Edge Delivery project directory on Microsoft SharePoint or Google Drive.

1. To add the form to a page, open the corresponding the doc file. For example, open the index file.

1. Navigate to the desired location within the document where you want to add the form.

1. Add a block named 'Form' to the file, similar to the one displayed below. 

    ![](/help/edge/assets/form-block-in-sites-page-example.png)

    In the second row, include the URL you noted down in the previous section, as a hyperlink. 

1. Use [AEM Sidekick](https://www.aem.live/developer/tutorial#preview-and-publish-your-content) to preview and publish the page. The form is rendered. 

    For example, here is the form based on the [contact us spreadsheet](https://docs.google.com/spreadsheets/d/12jvYjo1a3GOV30IqPY6_7YaCQtUmzWpFhoiOHDcjB28/edit?usp=drive_link): 


    ![contact us (EDS form)](/help/edge/assets/eds-form.png)

    The form block renders the form but it not ready to accept the data yet. On clicking the submit button, you experience an error similar to the following: 

    ![error on form submission](/help/edge/assets/form-error.png)

## 4. Enable your spreadsheet to accept data {#enable-a-spredsheet-to-recieve-data}

To begin accepting data, set up your spreadsheet to include the headers that match to the data you intend to collect. All the headers added to the 'shared-default' sheet should also be present in the 'incoming' sheet under a table. 

The following example displays fields for a "contact-us" form:

![Fields for a contact-us form](/help/edge/assets/contact-us-form-excel-sheet-fields.png)


Once this setup is complete, your form becomes ready to accept submissions. You can employ one of the following methods to enable your spreadsheet to accept data:

* [Manually configure a spreadsheet to accept data](#manually-configure-a-spreadsheet-to-receive-data)

* [Use Admin APIs to enable a spreadsheet to accept data](#use-admin-apis-to-enable-a-spreadsheet-to-receive-data-use-admin-apis-to-enable-a-spreadsheet-to-recieve-data)

### Manually configure a spreadsheet to accept data

To manually configure a spreadsheet to accept data: 


1. Open the workbook that you have created and change the name of the default sheet to "incoming". 

    >[!WARNING] 
    >
    > If the "incoming" sheet doesn't exist, AEM won't send any data to this workbook.

1. Prepare the sheet by adding headers that match the data you're putting in. The following example displays fields for a "contact-us" form:

    ![Fields for a contact-us form](/help/edge/assets/contact-us-form-excel-sheet-fields.png)

1. Preview the sheet in the sidekick.

    >[!NOTE] 
    >
    >Even if you have previewed the sheet before, you must preview it again after creating the "incoming" sheet for the first time.


### Use Admin APIs to enable a spreadsheet to accept data

You can initiate a POST request to the form route within the AEM Admin service. Upon receiving the POST body data, the admin service analyzes it and autonomously generates the essential headers, tables, and sheets needed for data ingestion, optimizing the functionality of the forms service.

To use Admin APIs to enable a spreadsheet to accept data: 


1. Open the workbook that you have created and change the name of the default sheet to "incoming". 

    >[!WARNING] 
    >
    > If the "incoming" sheet doesn't exist, AEM won't send any data to this workbook.

1. Preview the sheet in the sidekick.

    >[!NOTE] 
    >
    >Even if you have previewed the sheet before, you must preview it again after creating the "incoming" sheet for the first time.

1. Prepare the sheet by adding headers that match the data you're putting in. 

    You can do this by sending a POST request to the form route in the AEM Admin service. The admin service examines the data in the POST body and generate the appropriate headers, tables, and sheets needed to ingest data effectively and make the most of the Forms service.

    To understand how to format the POST request for setting up your sheet, refer to the [Admin API documentation](https://www.hlx.live/docs/admin.html#tag/form). Also, look at the example provided below: 

    **Request** 
    
    ```JSON

    POST 'https://admin.hlx.page/form/{owner}/{repo}/{branch}/contact-us.json' \
    --header 'Content-Type: application/json' \
    --data '{
        "data": {
            "Email": "john@wknd.com",
            "Name": "John",
            "Subject": "Regarding Product Inquiry",
            "Message": "I have some questions about your products.",
            "Phone": "123-456-7890",
            "Company": "Adobe Inc.",
            "Country": "United States",
            "PreferredContactMethod": "Email",
            "SubscribeToNewsletter": true
        }
    }'

    ```


    **Response**

    ```JSON

    HTTP/2 200 
    content-type: application/json
    x-invocation-id: 1b3bd30a-8cfb-4f85-a662-4b1f7cf367c5
    cache-control: no-store, private, must-revalidate
    accept-ranges: bytes
    date: Sat, 10 Feb 2024 09:26:48 GMT
    via: 1.1 varnish
    x-served-by: cache-del21736-DEL
    x-cache: MISS
    x-cache-hits: 0
    x-timer: S1707557205.094883,VS0,VE3799
    strict-transport-security: max-age=31557600
    content-length: 138

    {"rowCount":2,"columns":["Email","Name","Subject","Message","Phone","Company","Country",      "PreferredContactMethod","SubscribeToNewsletter"]}%

    ```

    You can use tools like curl or Postman to execute this POST request, as demonstrated below:

    ```JSON

    curl -s -i -X POST 'https://admin.hlx.page/form/wkndforms/portal/main/contact-us.json' \
        --header 'Content-Type: application/json' \
        --data '{
            "data": {
                "Email": "john@wknd.com",
                "Name": "John",
                "Subject": "Regarding Product Inquiry",
                "Message": "I have some questions about your products.",
                "Phone": "123-456-7890",
                "Company": "Wknd Inc.",
                "Country": "United States",
                "PreferredContactMethod": "Email",
                "SubscribeToNewsletter": true
        }
    }'

    ```

    The previously mentioned POST request provides sample data, including both form fields and their respective sample values. This data is used by the Admin service to set up the form.

    Upon submitting the POST request to the admin service, you observe the following changes in your workbook: 

* A new sheet named "shared-default" is added to your Excel Workbook or Google Sheet. The data present in the "shared-default" sheet is retrieved upon making a GET request to the sheet. This sheet serves as an optimal location to use spreadsheet formulas to summarize the incoming data, making it conducive for consumption in other contexts.

    Never should the "shared-default" sheets contain any personally identifiable information or sensitive data that you are not comfortable with being publicly accessible.

* A sheet named "Slack" is added to your Excel Workbook or Google Sheet. In this sheet, you can configure automatic notifications for a designated Slack channel whenever new data is ingested into your spreadsheet. At present, AEM supports notifications exclusively to the AEM Engineering Slack organization and the Adobe Enterprise Support organization.

    1. To set up Slack notifications enter the "teamId" of the Slack workspace and the "channel name" or "ID". You can also ask the slack-bot (with the debug command) for the "teamId" and the "channel ID". Using the "channel ID" instead of the "channel name" is preferable, as it survives channel renames.

        >[!NOTE] 
        >
        > Older forms didn't have the "teamId" column. The "teamId" was included in the channel column, separated by a "#" or "/".

    1. Enter any title that you want and under fields enter the names of the fields you want to see in the Slack notification. Each heading should be separated by a comma (For example name, email).

The sheet is now set up to receive data, and you can send POST requests directly to it using hlx.page, hlx.live, or your production domain.


### Manually configure a spreadsheet to accept data


While the Admin service recommended configuring your sheet, if you prefer to create the headers manually, refer to the document titled [Manual Forms Sheet Setup](https://www.hlx.live/docs/manual-forms-sheet-setup).



## 4. Send data to your sheet {#send-data-to-your-sheet}

After the sheet is set to receive data, you can [use Admin APIs to send data to your sheet](#use-admin-apis-to-send-data-to-your-sheet) or [add the form to your Edge Delivery Service (EDS) page](#add-the-form-to-your-edge-delivery-service-eds-page-add-a-form-to-your-eds-page) to send data to the sheet.


### Use Admin APIs to send data to your sheet

You can send POST requests directly to it using hlx.page, hlx.live, or your production domain, to send data.

```JSON

POST https://branch–repo–owner.hlx.(page|live)/email-form
POST https://my-domain.com/email-form

```

>[!NOTE] 
>
> The URL should not have the .json extension. You must publish the sheet for POST operations to function on `.live` or on the production domain.

#### Formatting the form data

There are a few different ways that you can format the form data in the POST body. You can use: 

* array of `name:value` pairs: 
    
    ```JSON
    
    {
      "data": [
        { "name": "name", "value": "Clark Kent" },
        { "name": "email", "value": "superman@example.com" },
        { "name": "subject", "value": "Regarding Product Inquiry" },
        { "name": "message", "value": "I have some questions about your products." },
        { "name": "phone", "value": "123-456-7890" },
        { "name": "company", "value": "Example Inc." },
        { "name": "country", "value": "United States" },
        { "name": "preferred_contact_method", "value": "Email" },
        { "name": "newsletter_subscribe", "value": true }
      ]
    }

    ```

    For example

    ```JSON

    curl -s -i -X POST 'https://main--portal--wkndforms.hlx.page/contact-us' \
        --header 'Content-Type: application/json' \
        --data '{
        "data": [
            { "name": "name", "value": "Clark Kent" },
            { "name": "email", "value": "superman@example.com" },
            { "name": "subject", "value": "Regarding Product Inquiry" },
            { "name": "message", "value": "I have some questions about your        products." },
            { "name": "phone", "value": "123-456-7890" },
            { "name": "company", "value": "Example Inc." },
            { "name": "country", "value": "United States" },
            { "name": "preferred_contact_method", "value": "Email" },
            { "name": "newsletter_subscribe", "value": true }
        ]
    }'

    ```



* an object with `key:value` pairs:

    ```JSON

        {
          "data": {
            "name": "Jessica Jones",
            "email": "jj@example.com",
            "subject": "Regarding Product Inquiry",
            "message": "I have some questions about your products.",
            "phone": "123-456-7890",
            "company": "Example Inc.",
            "country": "United States",
            "preferred_contact_method": "Email",
            "newsletter_subscribe": true
          }
        }

    ```

    For example,

    ```JSON

    curl -s -i -X POST 'https://admin.hlx.page/form/wkndforms/portal/main/contact-us.json' \
    --header 'Content-Type: application/json' \
    --data '{
        "data": {
            "Email": "khushwant@wknd.com",
            "Name": "khushwant",
            "Subject": "Regarding Product Inquiry",
            "Message": "I have some questions about your products.",
            "Phone": "123-456-7890",
            "Company": "Adobe Inc.",
            "Country": "United States",
            "PreferredContactMethod": "Email",
            "SubscribeToNewsletter": true
        }
    }'

    ```

* URL encoded (`x-www-form-urlencoded`) body (with `content-type` header set to `application/x-www-form-urlencoded`)

    ```Shell

    'Email=kent%40wknd.com&Name=clark&Subject=Regarding+Product+Inquiry&Message=I   +have+some+questions+about+your+products.&Phone=123-456-7890&Company=Adobe+Inc.&   Country=United+States&PreferredContactMethod=Email&SubscribeToNewsletter=true'

    ```

    For example,

    ```Shell

    curl -s -i -X POST \
      -d 'Email=kent%40wknd.com&Name=clark&Subject=Regarding+Product+Inquiry&   Message=I+have+some+questions+about+your+products.&Phone=123-456-7890& Company=Adobe+Inc.&Country=United+States&PreferredContactMethod=Email&   SubscribeToNewsletter=true' \
      https://main--portal--wkndforms.hlx.live/contact-us

    ```

## Configure thank you page

By default, upon submitting a form rendered with EDS Forms Block, you are automatically redirected to the `thankyou` node upon successful submission. Out of the box (OOTB), there is no existing page at the 'thankyou' node. Follow these steps to create a thank-you page and add content to it:

1. Go to your AEM Edge Delivery project directory on Microsoft SharePoint or Google Drive.

1. Create a doc file named `thankyou` and open it for editing. Add the thank you content to the file. 

    ![](/help/edge/assets/thankyou.png)

1. Use AEM Sidekick to preview and publish the file. Now, upon submitting a form, you are automatically redirected to the thank you page. 

### Configure Form block redirects

You have the option to configure the form block to redirect to a different page on your website instead of the default "thankyou" page,. To set up another page as the redirect destination

1. Open the `[EDS Project]/blocks/form/form.js` file for editing.

    ![code for thank you node](/help/edge/assets/change-thankyou-node.png)

1. Change the `thankyou` node in the following line to node of your choice:

    ```JavaScript

    window.location.href = form.dataset?.redirect || 'thankyou';


    ```

    For example,

    ```JavaScript

    window.location.href = form.dataset?.redirect || 'home';
        
    ```
    
    >[!NOTE]
    >
    > Ensure that a document page with the same name is created in your Edge Delivery Service project folder on either Microsoft SharePoint or Google Sheets, if it hasn't been created already.
 

1. Proceed to check-in the updated 'form.js' folder and its underlying files to your Edge Delivery Service project on GitHub. This update ensures that the form now redirects to the updated node as specified.
