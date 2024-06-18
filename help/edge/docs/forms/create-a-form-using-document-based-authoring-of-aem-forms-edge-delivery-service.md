---
title: Create a form using document based authoring for AEM Forms Edge Delivery Service
description: Craft perfect forms, fast! ⚡ AEM Forms Edge Delivery + doc-based authoring = blazing speed & SEO-friendly forms for happier users & search engines.
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
---

# Create a form using document based authoring for AEM Forms Edge Delivery Service

In today's digital age, creating user-friendly forms is essential for any organization. AEM Forms Edge Delivery's document-based authoring lets you create forms using familiar tools like Word or Google Docs.These forms submit data directly to a Microsoft Excel or Google Sheets file, enabling you to use vibrant ecosystem and robust APIs of Google Sheets, Microsoft Excel, and Microsoft Sharepoint to easily process submitted data or to initiate an existing business workflow.

This guide walks you through:

* Prepping your spreadsheet: Learn how to set up an Excel or Google Sheets file for data collection and add form fields to it.
* Send data to your sheet: Learn to send data to your sheet using POST requests. 
* Publishing the form: Integrate your form to your AEM Sites page or publish it as a standalone page.

Whether you're a novice or a pro, this guide empowers you to build beautiful, functional forms that users love. Let's unlock efficient form creation - dive in now!

## Before you start 

`WIP`

## Prepare your spreadsheet to recieve data

1. Create a Microsoft Excel Workbook or Google Sheet anywhere under your AEM Edge Delivery project directory on Microsoft OneDrive or Google Drive. This document uses a Google Sheet named `contact-us.xlsx`, located at the root of an Adobe Experience Manager (AEM) project.

1. Make sure the AEM user (for example helix@adobe.com) configured for your project has editing permissions for the sheet.

1. Open the workbook that you have created and change the name of the default sheet to "incoming". 

    >[!NOTE] 
    >
    > If the "incoming" sheet doesn't exist, AEM won't send any data to this workbook.

1. Preview the sheet in the sidekick.

    >[!NOTE] 
    >
    >Even if you have previewed the sheet before, you must preview it again after creating the "incoming" sheet for the first time.

1. Prepare the sheet by adding headers that match the data you're putting in. The following example displays fields for a "contact-us" form:

    ![Fields for a contact-us form](/help/edge/assets/contact-us-form-excel-sheet-fields.png)

    You can do this manually or by using a POST request to the form route in the AEM Admin service. The admin service will examine the data in the POST body and generate the appropriate headers, tables, and sheets needed to ingest data effectively and make the most of the forms service.

    To understand how to format the POST request for setting up your sheet, refer to the [Admin API documentation](https://www.hlx.live/docs/admin.html#tag/form). Additionally, take a look at the example provided below:

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

    {"rowCount":2,"columns":["Email","Name","Subject","Message","Phone","Company","Country","PreferredContactMethod","SubscribeToNewsletter"]}%

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

The aforementioned POST request provides sample data, including both form fields and their respective sample values. This data is used by the Admin service to setup of the form.

While the Admin service recommended to configure your sheet, if you prefer to create the headers manually, refer to the document titled [Manual Forms Sheet Setup](https://www.hlx.live/docs/manual-forms-sheet-setup).

Upon submitting the POST request to the admin service, you will observe the following changes in your workbook: 

* A new sheet named "shared-default" is added to your Excel Workbook or Google Sheet. The data present in the "shared-default" sheet is retrieved upon making a GET request to the sheet. This shhet serves as an optimal location to use spreadsheet formulas to summarize the incoming data, making it conducive for consumption in other contexts.

    Under no circumstances should the "shared-default" sheet contain any personally identifiable information or sensitive data that you are not comfortable with being publicly accessible.

* A sheet named "slack" is added to your Excel Workbook or Google Sheet. In this sheet, you can configure automatic notifications for a designated Slack channel whenever new data is ingested into your spreadsheet. At present, AEM supports notifications exclusively to the AEM Engineering Slack organization and the Adobe Enterprise Support organization.

    1. To setup Slack notifications enter the "teamId" of the Slack workspace and the "channel name" or "ID". You can also ask the slack-bot (with the debug command) for the "teamId" and the "channel ID". Using the "channel ID" instead of the "channel name" is preferable, as it survives channel renames.

        >[!NOTE] 
        >
        > Older forms didn't have the "teamId" column. The "teamId" was included in the channel column, separated by a "#" or "/".

    1. Enter any title you want and under fields enter the names of the fields you want to see in the Slack notification. Each heading should be separated by a comma (For example name, email).

The sheet is now set up to receive data, and you can send POST requests directly to it using hlx.page, hlx.live, or your production domain.


## Send data to your sheet {#send-data-to-your-sheet}

After the sheet is set to receive data, you can send POST requests directly to it using hlx.page, hlx.live, or your production domain, to send data.

```JSON

POST https://branch–repo–owner.hlx.(page|live)/email-form
POST https://my-domain.com/email-form

```

>[!NOTE] 
>
> The URL should not have the .json extension. You must publish the sheet for POST operations to function on .live or on the production domain.

### Formating data for EDS Forms

There are a few different ways you can format the form data in the POST body.

* Array of name:value pairs: 
    
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
                { "name": "message", "value": "I have some questions about your products." },
                { "name": "phone", "value": "123-456-7890" },
                { "name": "company", "value": "Example Inc." },
                { "name": "country", "value": "United States" },
                { "name": "preferred_contact_method", "value": "Email" },
                { "name": "newsletter_subscribe", "value": true }
                ]
            }'



* Object with key:value pairs

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

* `x-www-form-urlencoded` body (`content-type` header must be set to `application/x-www-form-urlencoded`)
'firstname=bruce&lastname=banner&email=bruce%40example.com'



