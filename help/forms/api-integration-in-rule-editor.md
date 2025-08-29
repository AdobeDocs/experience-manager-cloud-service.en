---
title: Integrate API in Rule Editor for Forms
description: Learn about the latest enhancements to the Invoke Service in the Rule Editor, including how to integrate APIs for Adaptive Forms based on Core Components without using a Form Data Model.
feature: Adaptive Forms, Core Components, Edge Delivery Services
role: User, Developer
level: Beginner, Intermediate
keywords: integrating API in rule editor, invoke service enhancements
exl-id: fc51f86d-e672-4513-b473-6700757a0c3d
---
# Integrating API in Rule Editor

<span>Integrating API in Rule Editor is under Early Adopter Program. You can write to `aem-forms-ea@adobe.com` from your official email id to join the early adopter program and request access to the capability.</span>

The Visual Rule Editor in Adaptive Forms supports direct API integration without creating a Form Data Model. You can connect to an API endpoint by either entering the API URL (in JSON format) or importing the configuration through a cURL command. Once integrated, the **Invoke Service** action can be used to call the API.

Form fields can be mapped directly to the input parameters defined in the API configuration. Similarly, output parameters can be mapped to form fields using the **event payload** option for the corresponding API response.

Additionally, the Visual Rule Editor lets you define **success** and **failure handlers** when invoking a service. Success handlers specify the actions to be executed after a successful API call, while failure handlers define how the form should respond when an error occurs.

>[!NOTE]
>
> API integration in Rule Editor is also applicable to Edge Delivery Services Forms.

## Comparison: API Integration Methods

| Aspect                         | API Integration with Form Data Model (FDM)                     | Direct API Integration (via *Create API Integration*) |
|--------------------------------|---------------------------------------------------------------------|-----------------------------------------------------------|
| **Purpose**                    | Centralized, reusable API integration across multiple forms         | Quick, form-specific API integration                      |
| **Setup Location**             | Created and edited in the Form Data Model Editor (AEM console)             | Created and edited directly in the Adaptive Form Rule Editor      |
| **Complexity**                 | Higher setup effort (requires mapping and configuration)            | Simple and lightweight                                    |
| **Best Suited For**            | Enterprise or large-scale use cases with multiple forms             | Small forms, prototypes, or one-off API calls             |

## API Integration Configuration

The screenshot below displays the API integration configuration window:

![API Integration Configuration](/help/forms/assets/api-integration-configuration.png)

### Key Configuration Options

**API Integration Configuration**

* **Import from cURL**: Configure your API integration by pasting a ready-made cURL command instead of manually entering details such as API URL, HTTP method, headers, and parameters.  
* **Display Name**: Custom name for the API service.  
* **API URL**: Endpoint of the API service.  
* **Select HTTP Method**: The HTTP request method used to call the API.  
* **Content Type**: Defines the request and response format.  
* **Encryption Required**: (Optional) Ensures sensitive data is encrypted during transmission.  
* **Execute at Client**: When enabled, the API call is made from the client (browser) instead of the server.  

**Authentication Type**  

* **Options**: None, Basic, API Key, OAuth 2.0.  

**Input Parameters**

* **Upload JSON for Input**: Upload a sample JSON file to auto-populate input mappings.  
  * **Name**: Input parameter name required by the API.  
  * **Type**: Data type of the input (String, Number, Boolean, etc.).  
  * **In**: Location of the parameter (Query, Header, or Body).  
  * **Default Value**: Pre-filled value if not provided by the user.  
  * **Add**: Option to add additional input parameters.  

**Output Parameters**

* **Upload JSON for Output**: Upload a sample API response to auto-generate mappings.  
  * **Name**: Output parameter name from the API response.  
  * **Type**: Expected data type of the output parameter (String, Number, etc.).  
  * **In**: Defines where the mapped value is expected.  
  * **Add/Delete**: Add new mappings or remove existing ones.  

## Use Case: Populating Country Fields in a Visa Application Form

**Scenario**: A government agency provides an online Visa Application Form with the following fields:

1. Full Name (Text)  
2. Date of Birth (Date)  
3. Country of Citizenship (Drop-down)  
4. Passport Number (Text)  
5. Country of Passport Issuance (Drop-down)  
6. Destination Country (Drop-down)  
7. Intended Date of Arrival (Date)  

Instead of maintaining a static list of countries, the form dynamically fetches country information (continent, capital, ISO Alpha codes, etc.) using the **getcountryname API**:

`https://secure.geonames.org/countryInfoJSON?username=aemforms`

This ensures applicants always see an up-to-date and accurate list of countries while filling out the form.

### Implementation Using API Integration in the Rule Editor

You can integrate an API without creating a Form Data Model by clicking the **Create API Integration** button in the Rule Editor.

![Create API Integration](/help/forms/assets/create-api-integration.png)

An API service named **getcountryname** is configured under **API Integration Configuration** in the Rule Editor:

![API rest Endpoint Configuration](/help/forms/assets/api-restendpoint.png)

* **API Endpoint URL** → `https://secure.geonames.org/countryInfoJSON?username=aemforms`  
* **HTTP Method** → GET  
* **Content Type** → JSON  
* **Input** → `username` passed as a query parameter (`aemforms`).  
* **Output** → Response fields such as `continent`, `capital`, `countrynames`, `isoAlpha3`, and `languages` are mapped to form fields.  

In the **Visa Application Form**, the three drop-down fields, **Country of Citizenship**, **Country of Passport Issuance**, and **Destination Country**, are bound to the **Invoke Service** action.

When the form loads, **Invoke Service** fetches the list of countries from the API. The response is then mapped to automatically populate the drop-down options.

For example, when the user opens **Country of Citizenship**, the list of countries is displayed dynamically from the API response.

![invoke-service-api-integration](/help/forms/assets/invoke-service-api-integration.png)

![API integration Output](/help/forms/assets/api-integration-output.png)

Similarly, **Country of Passport Issuance** and **Destination Country** use the same API call, ensuring consistent and up-to-date data across all three fields.

## Implementing Retry Mechanism for API Failures

When an API request fails, it's often useful to retry the request before reporting an error to the user. You can implement a polling and retry mechanism by writing custom code in the **function.js** file. 

The following example demonstrates how to handle API failures with up to two retry attempts and exponential backoff between retries:

``` javascript

/**
 * Handles request retries with up to 2 retry attempts
 * @param {function} requestFn - The request function to execute
 * @return {Promise} A promise that resolves with the response or rejects after all retries
 */
function retryHandler(requestFn) {
    const MAX_RETRIES = 2;
    
    /**
     * Attempts the request with retry metadata
     * @param {number} retryCount - Current retry attempt count
     * @return {Promise} The request promise
     */
    function attemptRequest(retryCount = 0) {
        // Include retry metadata if this is a retry
        const requestOptions = retryCount > 0 ? {
            headers: {
                'X-Retry': 'true',
                'X-Retry-Count': retryCount.toString(),
                'X-Retry-Time': new Date().toISOString()
            },
            body: {
                retry: true,
                retryCount: retryCount,
                timestamp: Date.now()
            }
        } : undefined;

        return requestFn(requestOptions)
            .then(function(response) {
                if (response && response.status >= 400) {
                    console.warn('Request failed with status ' + response.status);
                    throw new Error('Request failed with status ' + response.status);
                }
                return response;
            })
            .catch(function(error) {
                console.warn('Request attempt ' + (retryCount + 1) + ' failed:', error.message);
                
                // Retry if max attempts not reached
                if (retryCount < MAX_RETRIES) {
                    console.log('Retrying request, attempt ' + (retryCount + 2) + ' of ' + (MAX_RETRIES + 1));
                    
                    // Exponential backoff delay: 1s, 2s, 4s...
                    const delay = Math.pow(2, retryCount) * 1000;
                    
                    return new Promise(function(resolve) {
                        setTimeout(resolve, delay);
                    }).then(function() {
                        return attemptRequest(retryCount + 1);
                    });
                } else {
                    // All retries exhausted
                    console.error('All retry attempts failed. Final error:', error.message);
                    throw new Error('Request failed after ' + (MAX_RETRIES + 1) + ' attempts: ' + error.message);
                }
            });
    }
    
    // Start the first attempt
    return attemptRequest(0);
}

```

In the above code, the **retryHandler** function manages API requests with automatic retries in case of failure. It takes a request function (requestFn) and attempts the request up to two times, adding metadata for each retry.

>[!NOTE]
>
> For detailed steps on how to add custom functions, refer to the [Introduction to Custom Functions for Adaptive Forms based on Core Components](/help/forms/create-and-use-custom-functions.md) article.

## Frequently Asked Questions

* **Do I need to create a Form Data Model to integrate an API in Adaptive Forms?**  
No. With the Visual Rule Editor, you can directly integrate APIs using the **Create API Integration** option without creating a Form Data Model. This approach is best suited for lightweight or form-specific use cases.

* **Can I secure API calls made from the Rule Editor?**  
Yes. The API Integration Configuration provides authentication options such as **Basic, API Key, and OAuth 2.0**. You can also enable **Encryption Required** to ensure sensitive data is securely transmitted.
