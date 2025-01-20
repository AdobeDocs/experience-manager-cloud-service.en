---
Title: How to use forms submission service for submitting forms?
Description: Learn how to use forms submission service for submitting forms.
Keywords: Use form submission service, Submit form using form submission service
feature: Edge Delivery Services
Role: User, Developer
exl-id: 12b4edba-b7a1-4432-a299-2f59b703d583
---
# Forms Submission Service with Edge Delivery Services Forms

Forms Submission service allows you to store data from the form submissions in any spreadsheet, such as OneDrive, SharePoint, or Google Sheets, allowing you to easily access and manage form data within your preferred spreadsheet platform.

![Forms submission service](/help/forms/assets/form-submission-service.png)

## Advantages to use Forms Submission service

A few advantages of using the Forms Submission Service with spreadsheets are:

* **Direct integration**: You can configure forms to submit data directly to a specified spreadsheet, eliminating the need for manual data transfer. 
* **Data structure**: When setting up the submission, you can map form fields to corresponding spreadsheet columns for organized data storage. 
* **Access control**: You can leverage existing permissions to control who can access and modify submitted form data, depending on the chosen spreadsheet service. 

## Pre-requisites

Below are the prerequisites for using the Forms Submission service:

* Make sure your AEM Project has the latest Adaptive Form Block.  
* Ensure that your Git repository is added to the allowlist to use the Forms Submission Service. Fill out the [form](https://main--afb--adobe.hlx.page/docs/docbased/submit#feature-enablement-request) to request for Forms Submission Service.  
  
## Configure Forms Submission service 

Create new AEM project configured with the Adaptive Forms Block. Refer to the [Getting Started - Developer Tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/build-forms/getting-started-edge-delivery-services-forms/tutorial) article to learn how to create a new AEM project. Update the `fstab.yaml` file in your project. Replace the existing reference with the path to the folder you have shared with the `forms@adobe.com` .

You can [configure the Forms Submission Service manually](#configuring-the-forms-submission-service-manually) or [configure the Forms Submission Service using the API](#configuring-the-forms-submission-service-using-api).

### Configuring the Forms Submission Service manually

![Workflow for forms submission service](/help/forms/assets/forms-submission-service-workflow.png)

#### 1. Create a form using a form definition

Author a form using Google Sheets or Microsoft Excel. To learn how to create a form using a form definition in Microsoft Excel or Google Sheets, [click here](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/build-forms/getting-started-edge-delivery-services-forms/create-forms).

The below screenshot displays the form definition used to create form:

![Form Definition](/help/forms/assets/form-submission-definition.png)

#### 2. Enable the spreadsheet to accept data.

Once you have created and previewed the form, enable the corresponding spreadsheet to start receiving data. add a new sheet as `incoming`. You can [manually enable the spreadsheet to accept data](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/build-forms/getting-started-edge-delivery-services-forms/submit-forms#manually-enable-the-spreadsheet-to-accept-data).

![Incoming sheet](/help/forms/assets/form-submission-incoming-sheet.png)

>[!WARNING] 
>
> If the `incoming` sheet does not exist, AEM would not send any data to this workbook.

#### 3. Share the spreadsheet and generate a link.

To share the spreadsheet to the `forms@adobe.com` account and generate a link, perform the folllowing steps:

1. In Excel or Google Sheets, click the **Share** button on the top-right corner.
1. Add the `forms@adobe.com` account and 
click the eye icon, select **Edit** access, and click **Send**.

    ![Share incoming sheet](/help/forms/assets/form-submission-share-incoming.png)

1. To copy the spreadsheet link, click the **Share** button on the top-right corner and select **Copy Link**.

    ![Copy link of incoming sheet](/help/forms/assets/form-submission-copy-link.png)

#### 4. Link the spreadsheet in the form definition

To configure the Forms Submission service with the Google Sheets or Microsoft Excel, perform the following steps:

1. Open the spreadsheet which contains the form definition.
1. In the row corresponding to the **Submit** field, paste the copied spreadsheet link into the **Action** column.

    ![Link a spreadsheet](/help/forms/assets/form-submission-sheet-linking.png)

1. Preview and publish the sheet using the [AEM Sidekick](https://www.aem.live/docs/sidekick) with updated Form Submission service.

>[!NOTE]
>
> You can refer to the [spreadsheet](/help/forms/assets/spreadsheet.xlsx) to use the Forms Submission service.

### Configuring the Forms Submission Service using API

You can also send a **POST** request to the form to update the `incoming` sheet with data. 

>[!NOTE] 
>
> * If the `incoming` sheet does not exist, AEM would not send any data to this workbook.
> * Share the `incoming` sheet with the Adobe Experience Manager the `forms@adobe.com` and grant the edit access.
> * Preview and publish the `incoming` sheet in the sidekick.

To understand how to format the POST request for setting up your sheet, refer to the [API documentation](https://main--afb--adobe.hlx.page/docs/index.html#/paths/~1%7Bid%7D/post). You can look at the example provided below: 

You can use tools like curl or Postman to execute this POST request, as demonstrated below.

* **Using Postman**:
    
For example, send the request below in Postman after replacing:
  * `{id}` with your Form ID
  * `site or repository` with your GitHub repository or site name
  * `organization` with your GitHub username
   
    ```json

    POST 'https://forms.adobe.com/adobe/forms/af/submit/{id}' \
    --header 'Content-Type: application/json' \
    --header 'x-adobe-routing: tier=live,bucket=main--[site/repository]--[organization]' \
    --data '{
        "data": {
            "startDate": "2025-01-10",
            "endDate": "2025-01-25",
            "destination": "Australia",
            "class": "First Class",
            "budget": "2000",
            "amount": "1000000",
            "name": "Mary",
            "age": "35",
            "subscribe": null,
            "email": "mary@gmail.com"
                }
            }'
     ```

Clicking the **Send** button in Postman returns a `201 Created` response, and the `incoming` sheet updates with the submitted data.

![postman screen](/help/forms/assets/postman-api.png)

* **Using Curl command**:

For example, execute the below commmand in terminal or command prompt after replacing:
* `{id}` with your Form ID
* `site or repository` with your GitHub repository or site name
* `organization` with your GitHub username


>[!BEGINTABS]

>[!TAB For macOS]

    ```json
    curl -X POST "https://forms.adobe.com/adobe/forms/af/submit/{id}" \
    --header "Content-Type: application/json" \
    --header "x-adobe-routing: tier=live,bucket=main--[site/repository]--[organization]" \
    --data '{
        "data": {
            "startDate": "2025-01-10",
            "endDate": "2025-01-25",
            "destination": "Australia",
            "class": "First Class",
            "budget": "2000",
            "amount": "1000000",
            "name": "Joe",
            "age": "35",
            "subscribe": null,
            "email": "mary@gmail.com"
                }
            }'

        ```

>[!TAB For Windows OS]

    ```json
     
     curl -X POST "https://forms.adobe.com/adobe/forms/af/submit/{id}" ^
    --header "Content-Type: application/json" ^
    --header "x-adobe-routing: tier=live,bucket=main--[site/repository]--[organization]" ^
    --data "{\"data\": {\"startDate\": \"2025-01-10\", \"endDate\": \"2025-01-25\", \"destination\": \"Australia\", \"class\": \"First Class\", \"budget\": \"2000\", \"amount\": \"1000000\", \"name\": \"Joe\", \"age\": \"35\", \"subscribe\": null, \"email\": \"mary@gmail.com\"}}"

    ```

>[!ENDTABS]

The above mentioned POST request updates the `incoming` sheet with the below response:

```json
    < HTTP/1.1 201 Created
    < Connection: keep-alive
    < Content-Length: 0
    < X-Request-Id: 02a53839-2340-56a5-b238-67c23ec28f9f
    < X-Message-Id: 42ecb4dd-b63a-4674-8f1a-05a4a5b0372c
    < Accept-Ranges: bytes
    < Date: Fri, 10 Jan 2025 13:06:10 GMT
    < Via: 1.1 varnish
    < Access-Control-Allow-Origin: *
    < X-Served-By: cache-del21750-DEL
    < X-Cache: MISS
    < X-Cache-Hits: 0
    < X-Timer: S1736514370.704084,VS0,VE1234
```

The below screen displays the screenshot of the `incoming` sheet updated by the data send using API:

![updated sheet](/help/forms/assets/updated-sheet.png)

## See also

{{see-more-forms-eds}}
