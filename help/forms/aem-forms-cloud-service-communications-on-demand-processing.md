---
title: How do set up Forms Communications Synchronous APIs?
description: Set up development environment for Interactive Communications Synchronous APIs for Adobe Experience Manager Forms as a Cloud Service
role: Admin, Developer, User
feature: Adaptive Forms,APIs & Integrations
hide: yes
hidefromtoc: yes
index: no
---

# Configure OAuth Server-to-Server Access for AEM Forms Communications Synchronous APIs

This guide provides instructions for configuring and invoking AEM Forms Communications Synchronous APIs that are accessed through the Adobe Developer Console using OAuth Server-to-Server authentication. 

## Prerequisites

To set up an environment for running and testing AEM Forms Communications APIs, ensure that you have the following:

### Access and permissions

Make sure you have the required access rights and permissions before you start configuring the Communications APIs.

**User and role permissions**

- Developer role assigned in the Adobe Admin Console
- Permission to create projects in the Adobe Developer Console
 
>[!NOTE]
>
> To learn more about assigning roles and granting access to users, refer to the article [Add users and roles](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/requirements/users-and-roles).

**Git Repository Access**

- Access to Cloud Manager Git Repository
- Git credentials for cloning and pushing changes

>[!NOTE]
>
> To learn more on how to integrate Adobe Cloud Manager and Adobe Cloud Manager, see [Git Integration Documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/managing-code/git-integration.html).

### Generate Access Token using Adobe Developer Console (ADC)

- Generate access token through the Adobe Developer Console using OAuth Server-to-Server authentication.
- Retrieve Client ID from the Adobe Developer Console

>[!NOTE]
>
> For more information about OAuth Server-to-Server authentication using the Adobe Developer Console, [click here](/help/forms/oauth-api-authetication.md).

### Development Tools

- **Node.js** for running sample applications
- Latest version of **Git** 
- Access to **Terminal/Command line**
- **Text editor or IDE** for editing configuration files (VS Code, IntelliJ, etc.)
- **Postman** or similar tool for API testing 

>[!NOTE] 
>
> This is a one-time per environment process that must be completed before proceeding with AEM Forms Communications APIs setup.

## Configure AEM Forms Communications Synchronous APIs

AEM Forms Communication APIs are accessed through the Adobe Developer Console using OAuth server-to-server authentication. 

In this, example let us generate an PDF using the Forms Communication APIs using the template and XDP file. The following steps explain how to configure the Forms Communication synchronous APIs to generate PDF.

### Step 1: Access AEM Cloud Service Environment and AEM Forms Endpoint 

Access your AEM Cloud Service environment details to obtain the URLs and identifiers needed for API configuration. 

1. **Log into Adobe Cloud Manager**
   1. Navigate to [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com)
   2. Log in with your Adobe ID

2. **Navigate to the Program Overview**
   1. Select your program from the list. You are redirected to the **Program Overview** page

3. **Access and View AEM Cloud Service Environment**

    You can view or access the AEM Cloud Service Environment details using either of the two options:

    >[!BEGINTABS]

    >[!TAB Option 1: From Overview Page]

     1. On the **Program Overview** page
     2. Click **"Environments"** in the left side menu.  You can see a list of all environments

        ![View All Environments](/help/forms/assets/all-env.png)

     3. Click the specific environment name to view details

        ![Option1-Environment Details](/help/forms/assets/option1-env.png)

    >[!TAB Option 2: From Environments Section]
  
      1. On the Program Overview page
      2. Locate the **Environments** section
      3. Click **"Show All"** to view all environments
      4. Click the **ellipsis menu (...)** next to the environment
            ![Option1-Environment Details](/help/forms/assets/option2-env-details.png)
      5. Select **"View Details"**

            ![Option1-Environment Details](/help/forms/assets/option1-env.png)

    >[!BEGINTABS]

4. **Find Your AEM Forms Endpoint**

    From the **Environment** details page, note your AEM URL instance.

>[!NOTE]
>
> To see how to access the Access AEM Cloud Service Environment and AEM Forms Endpoint, see [Managing Environments Documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-environments.html).

### Step 2: Clone Git Repository

Clone the Cloud Manager Git Repository to manage your API configuration files.

1. **Locate the Repository Section**
   1. On the **Program Overview** page, click the **Repositories** tab
   2. Locate the repository name and click on the ellipsis menu (...)
   3. Copy the repository URL

        ![Copy Repo URL](/help/forms/assets/copy-repo-url.png)

        >[!NOTE]
        >
        > The URL format is typically `https://git.cloudmanager.adobe.com/<org>/<program>/`

2. **Clone Using Git Command**

    1. Open the command prompt or terminal
    2. Run the `git clone` command to clone the Git repository.
   
        ```bash

        git clone [repository-url]
    
        ```

        >[!NOTE]
        >
        > To clone the Git repository use the credentials provided by Adobe Cloud Manager.
    
        For example, to clone your Git Repository, execute the following command:

        ```bash

        https://git.cloudmanager.adobe.com/formsinternal01/AEMFormsInternal-ReleaseSanity-pXXX-ukYYYY/

        ```

        ![Clonning the Git Repository](/help/forms/assets/repo-clone.png)


To learn more on how to integrate Adobe Cloud Manager and Adobe Cloud Manager, see [Git Integration Documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/managing-code/git-integration.html).

### Step 3: Adobe Developer Console Project Setup

1. **Access Adobe Developer Console**
   1. Navigate to [Adobe Developer Console](https://developer.adobe.com/console)
   2. Log in with your Adobe ID

   3. Create New Project or navigate to your existing project

        >[!BEGINTABS]

        >[!TAB To create a new project]

       1. From the **Quick Start** section, click **Create new project**
       2. A new project is created with a default name

            ![Create ADC Project](/help/forms/assets/adc-home.png)

       3. Click **Edit project** in the top right corner

            ![Edit Project](/help/forms/assets/adc-edit-project.png)

       4. Provide a meaningful name (e.g., "formsproject")
       5. Click **Save**

            ![Edit Project Name](/help/forms/assets/adc-edit-projectname.png)

        >[!TAB To navigate to your existing project]

       1. Click **All Projects** from the Adobe Developer Console  

            ![Search Projects](/help/forms/assets/search-adc-project.png)

       2. Locate your project and click to open it.

            ![Locate Projects](/help/forms/assets/locate-adc-project.png)

        >[!ENDTABS]

2. **Add Forms Communication APIs**

   1. Click **Add API** 

        ![Add api](/help/forms/assets/adc-add-api.png)

   2. In the _Add API_ dialog, filter by **Experience Cloud**
   3. Select **"Forms Communication APIs"**

        ![Add Forms Communication API](/help/forms/assets/adc-add-forms-api.png)

   4. Click **Next**
   5. Select **OAuth Server-to-Server** authentication method

        ![Select Authentication method](/help/forms/assets/adc-add-authentication-method.png)
   6. Click **Next**

3. **Add Product Profile**
    
   1. Select the **Product Profile** that matches your AEM instance URL (`https://Service Type -Environment Type-Program XXX-Environment XXX.adobeaemcloud.com`).  

   2. Click **Save configured API**. The API and Product Profile are added to your project

        ![Select Project Configuration](/help/forms/assets/adc-add-product-profile.png)

   3. View the **Credential details** section

        ![View Credentials](/help/forms/assets/adc-view-credential.png)

    **Record API Credentials**

    ```text
    API Credentials:
    ================
    Client ID: <your_client_id>
    Client Secret: <your_client_secret>
    Technical Account ID: <tech_account_id>
    Organization ID: <org_id>
    Scopes: AdobeID,openid,read_organizations
    ```

4. **Generate the Access**

    >[!BEGINTABS]

    >[!TAB For Testing]

    Generate access tokens manually in Adobe Developer Console:

    1. Click the **"Generate access token"** button in your project's API section
    2. Copy the generated access token

        ![Generate Access Token](/help/forms/assets/adc-access-token.png)
    
        >[!NOTE]
        >
        > Access token is valid for only for **24 hours**

    >[!TAB For Production]

    Generate tokens programmatically using [Adobe IMS](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/setting-up-ims-integrations-for-aem-as-a-cloud-service) API:

    **Required Credentials:**

      - Client ID
      - Client Secret
      - Scopes (typically: `openid, AdobeID, read_organizations, additional_info.projectedProductContext, read_pc.dma_aem_cloud, aem.document`)

    **Token Endpoint:**
    
    ```
        https://ims-na1.adobelogin.com/ims/token/v3
    ```

    **Sample Request (curl):**

    ```bash
    curl -X POST 'https://ims-na1.adobelogin.com/ims/token/v3' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'grant_type=client_credentials' \
    -d 'client_id=<YOUR_CLIENT_ID>' \
    -d 'client_secret=<YOUR_CLIENT_SECRET>' \
    -d 'scope=AdobeID,openid,read_organizations'
    ```

    **Response:**

    ```json
        {
        "access_token": "eyJhbGciOiJSUz...",
        "token_type": "bearer",
        "expires_in": 86399
        }
    ```

    >[!ENDTABS]

You can now use the generated access token to make API call for development, stage, or production environments.

>[!NOTE]
>
> To learn more about OAuth server-to-server authentication via the Adobe Developer Console, refer to the [OAuth Server-to-Server Authentication](/help/forms/oauth-api-authetication.md) article. 

### Step 4: Register Client ID with AEM Environment

To enable your ADC Project's Client ID to communicate with the AEM instance, you must register it using a YAML configuration file and deploy it via a Config Pipeline.

1. **Locate or Create Config Directory**
   
   1. Navigate to the cloned AEM Project repository and locate the `config` folder
   2. If it doesn't exist, create it at the project root level:
   
    ```bash
    mkdir config
    ```

2. Create a new file named `api.yaml` in the `config` directory:
   
   ```bash
   touch config/api.yaml
   ```

3. Add the following code in the `api.yaml` file:

    ```yaml
    kind: "API"
    version: "1"
    metadata:
    envTypes: ["dev"]  # or ["prod", "stage"] for production environments
    data:
    allowedClientIDs:
        author:
        - "<your_client_id>"
        publish:
        - "<your_client_id>"
        preview:
        - "<your_client_id>"
    ```

    The following explains the configuration parameters:

   - **kind**: Always set to `"API"` (identifies this as an API configuration)
   - **version**: API version, typically `"1"` or `"1.0"`
   - **envTypes**: Array of environment types where this config applies
     - `["dev"]` - Development environments only
     - `["stage"]` - Staging environments only
     - `["prod"]` - Production environments only
   - **allowedClientIDs**: Client IDs allowed to access your AEM instance
     - **author**: Client IDs for author tier
     - **publish**: Client IDs for publish tier
     - **preview**: Client IDs for preview tier

    For example, add the `allowedClientIDs` as `6bc4589785e246eda29a545d3ca55980` and envTypes as `dev`:

    ![Adding Config file](/help/forms/assets/create-api-yaml-file.png)

4. **Commit and Push Changes**
   
   1. Navigate to root folder of your clonned repository and execute the below commands:


    ```bash
        git add config/api.yaml
        git commit -m "Whitelist client id for api invocation"
        git push origin <your-branch>
    ```

    ![Push Git Changes](/help/forms/assets/push-yaml-changes-in-git.png)


5. **Setup Config Pipeline**

   1. **Locate the Pipelines Card**
      1. Locate the **Pipelines** card on the Program Overview page
      2. Click **"Add"** button

            ![Add Pipleine](/help/forms/assets/add-pipeline.png)
   
   2. **Select Pipeline Type**

        - **For Development Environments**: Select **"Add Non-Production Pipeline"**. Non-production pipelines are for dev and stage environments

        - **For Production Environments**: Select **"Add Production Pipeline"**. Production pipelines require additional approvals

            >[!NOTE]
            >
            > In this case, create a Non-Production Pipeline since a development environment is available.

   3. **Configure Pipeline - Configuration Tab**

        In the **Configuration** tab:

        a. **Pipeline Type**
         - Select **"Deployment Pipeline"** 

        b. **Pipeline Name**
         - Provide a descriptive name, For example, name the pipeline as `api-config-pipieline`

        c. **Deployment Trigger**
         - **Manual**: Deploy only when manually triggered (recommended for initial setup)
         - **On Git Changes**: Auto-deploy when changes are pushed to the branch

        d. **Important Metric Failures Behavior**
         - **Ask every time**: Prompt for action on failures (default)
         - **Fail Immediately**: Automatically fail pipeline on metric failures
         - **Continue Immediately**: Continue despite failures

        e. Click **"Continue"** to proceed to the **Source Code** tab

        ![Config Pipeline](/help/forms/assets/add-config-pipeline.png)

   4. **Configure Pipeline - Source Code Tab**

        In the **Source Code** tab:

        a. **Deployment Type**
         - Select **"Targeted deployment"**

        b. **Deployment Options**
         - Select **"Config"** (deploy configuration files only). It tells Cloud Manager this is a config deployment.

        c. **Select Eligible Deployment Environment**
         - Choose the environment where you want to deploy the config. In this case, it is a `dev` environment.

        d. **Define Source Code Details**
      
         - **Repository**: Select the repository containing your `api.yaml` file. For example, select the `AEMFormsInternal-ReleaseSanity-p43162-uk59167` repository.
         - **Git Branch**: Select your branch. For example, in this case our code is deployed at the `main` branch.
         - **Code Location**: Enter the path to `config` directory. As the`api.yaml` is in `config` folder at root, so enter `/config`

        e. Click **"Save"** to create the pipeline

        ![Config Pipeline](/help/forms/assets/confirm-pipeline-1.png)

6. **Deploy Configuration**

    Now that the pipeline is created, deploy your `api.yaml` configuration:

   1. **From the Pipelines Overview**
      1. On the Program Overview page, locate the **Pipelines** card
      2. Navigate to your newly created config pipeline in the list. For example, look for the pipeline name you created (e.g., "api-config-pipeline"). You can see pipeline details including status and last run.

   2. **Start the Deployment**
      1. Click the **"Build"** button (or play icon ▶) next to your pipeline
      2. Confirm the deployment if prompted and the pipeline execution begins

        ![run the pipeline](/help/forms/assets/run-config-pipeline.png)

   3. **Verify Successful Deployment**
       - Wait for the pipeline to complete.
         - If it succeeds, the status changes to "Success" (green checkmark ✓).
         - If it fails, the status changes to "Fail" (red cross ✗). Click **Download logs** to view the error details.

            ![Pipeline success](/help/forms/assets/pipeline-suceess.png)

        Now, you can start testing the Forms Communications APIs. For testing purposes, you can use the Postman, curl, or any other REST client to invoke the APIs.

### Step 4: API Specifications and Testing

Now that your environment is configured, you can start testing the AEM Forms Communication APIs either using Swagger UI or programmatically by developing NodeJS application.

>[!BEGINTABS]

>[!TAB A. Using Swagger UI for API Testing]

Swagger UI provides an interactive interface for testing APIs without writing code.Use the **Try it** feature to invoke and test the [generate PDF](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#operation/renderPDFForm) Forms Communication API.

1. Navigate to [Forms Communication API Reference](https://developer.adobe.com/experience-manager-forms-cloud-service-developer-reference/) and open the [Forms Communication API](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document) documentation in your browser.  
2. Expand the **Document Generation** section and select [Generates a fillable PDF form from an XDP or PDF template, optionally with data merging](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#operation/renderPDFForm).  
3. In the right pane, click **Try it**.

    ![Swagger testing for API](/help/forms/assets/api-doc-generation.png)
4. Enter the following values:

    | **Section** | **Parameter** | **Value** |
    |--------------|---------------|------------|
    | bucket | AEM instance | AEM instance name without the Adobe domain name (`.adobeaemcloud.com`) For example, use `p43162-e177398` as bucket. |
    | Security | Bearer Token | Use the [access token from the Adobe Developer Console Project's OAuth Server-to-Server credential](/help/forms/oauth-api-authetication.md#how-to-generate-an-access-token-using-oauth-server-to-server-authentication) |
    | Body | template | Upload an XDP  to generate the PDF form. For example, you can use [this XDP](/help/forms/assets/ClosingForm.xdp) to generate a PDF.  |
    | Body | data  | An optional XML file containing the data to be merged with the template to generate a pre-filled PDF form. For example, you can use [this XML](/help/forms/assets/ClosingForm.xml) to generate a PDF.  |
    | Parameters | X-Adobe-Accept-Experimental  | 1 |

5. Click **Send** to invoke the API 

    ![Send API](/help/forms/assets/api-send.png)

6. Check the response in the **Response** tab:
    - If the response code is `200`, it means the PDF is created successfully. 
    - If the response code is `400`, it means the request parameters are invalid or malformed. 
    - If the response code is `500`, it means there is an internal server error.
    - If the response code is `403`, it means there is an authorization error.

    In this case, the response code is `200`, it means that the PDF is generated successfully:

    ![Review Response](/help/forms/assets/api-success.png)

    Now, you can download the [created PDF](/help/forms/assets/create-pdf.pdf) using the **Download** button and view it in PDF viewer:

    ![View PDF](/help/forms/assets/create-pdf.png)

    >[!NOTE]
    >
    > For testing purposes, you can also use the [Postman](https://www.postman.com/), [curl](https://curl.se/), or any other REST client to invoke the AEM APIs.

>[!TAB B. Programmatically by Developing NodeJS Application]

Develop a Node.js application to generate a fillable PDF form from an **XDP** template and an **XML** data file using the **Document Services API**

**Prerequisites**

- Node.js installed on your system
- Active AEM as a Cloud Service instance
- Bearer token for API authentication from Adobe Developer Console
- Sample XDP File: [ClosingForm.xdp](/help/forms/assets/ClosingForm.xdp)
- Sample XML File:  [ClosingForm.xml](/help/forms/assets/ClosingForm.xml)

To develop the Node.js application, follow the step-by-step-development:

**Step 1: Create a New Node.js Project**

Open the cmd/terminal and execute the below commands:

```bash
# Create a new directory
mkdir demo-nodejs-generate-pdf
cd demo-nodejs-generate-pdf

##### Initialize Node.js project
npm init -y
```

![Create new node js project](/help/forms/assets/api-1.png)

**Step 2: Install Required Dependencies**

Install the **node-fetch**, **dotenv**, and **form-data** libraries to make HTTP requests, read environment variables, and handle form data respectively.

```bash
npm install node-fetch
npm install dotenv
npm install form-data
```

![install npm dependencies](/help/forms/assets/api-2.png)

**Step 3: Update package.json**

1. Open the cmd/terminal and run the command:

    ```bash
    code .
    ```

    ![open project in editor](/help/forms/assets/api-3.png)

    It opens the project in the code editor. 

2. Update the `package.json` file to add the `type` to `module`.

    ```bash

    {
    "name": "demo-nodejs-generate-pdf",
    "version": "1.0.0",
    "type": "module",
    "main": "index.js",
    }
    
    ```

    ![update package file](/help/forms/assets/api-4.png)

**Step 4: Create a .env File**

1. Create .env file at the root level of an project
2. Add the following configuration and replace the placeholders with the actual values from the ADC Project's OAuth Server-to-Server credential.

    ```bash
    CLIENT_ID=<ADC Project OAuth Server-to-Server credential ClientID>
    CLIENT_SECRET=<ADC Project OAuth Server-to-Server credential Client Secret>
    SCOPES=<ADC Project OAuth Server-to-Server credential Scopes>
    ```

    ![create env file](/help/forms/assets/api-5.png)

    >[!NOTE]
    >
    > You can copy the `CLIENT_ID`, `CLIENT_SECRET` and `SCOPES` from the Adobe Developer Console project.

**Step 5: Create src/index.js**

1. Create `index.js` file at the Project's root level 
2. Add the following code, and replace the placeholders with the actual values:

```javascript

// Import the dotenv configuration to load environment variables from the .env file
import "dotenv/config";

// Import fetch for making HTTP requests
import fetch from "node-fetch";
import fs from "fs";
import FormData from "form-data";

// REPLACE THE FOLLOWING VALUE WITH YOUR OWN
const bucket = <bucket-value>; // Your AEM Cloud Service Bucket name
const xdpFilePath = <xdp-file>;
const xmlFilePath = <xml-file>;

// Load environment variables
const clientId = process.env.CLIENT_ID;
const clientSecret = process.env.CLIENT_SECRET;
const scopes = process.env.SCOPES;

// Adobe IMS endpoint for obtaining an access token
const adobeIMSV3TokenEndpointURL = "https://ims-na1.adobelogin.com/ims/token/v3";

// Function to get an access token
const getAccessToken = async () => {
    console.log("Getting access token from IMS...");

    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `grant_type=client_credentials&client_id=${clientId}&client_secret=${clientSecret}&scope=${scopes}`,
    };

    const response = await fetch(adobeIMSV3TokenEndpointURL, options);
    const responseJSON = await response.json();

    console.log("Access token received.");
    return responseJSON.access_token;
};

// Function to generate PDF form from XDP and XML
const generatePDF = async () => {
    const accessToken = await getAccessToken();

    console.log("Generating PDF form from XDP and XML...");

    // Read XDP and XML files
    const xdpFile = fs.readFileSync(xdpFilePath);
    const xmlFile = fs.readFileSync(xmlFilePath);

    const url = `https://${bucket}.adobeaemcloud.com/adobe/document/generate/pdfform`;

    const formData = new FormData();
    formData.append("template", xdpFile, {
        filename: "form.xdp",
        contentType: "application/vnd.adobe.xdp+xml"
    });
    formData.append("data", xmlFile, {
        filename: "data.xml",
        contentType: "application/xml"
    });

    const response = await fetch(url, {
        method: "POST",
        headers: {
            Authorization: `Bearer ${accessToken}`,
            "X-Api-Key": clientId,
            "X-Adobe-Accept-Experimental": "1",
            ...formData.getHeaders()
        },
        body: formData,
    });

    if (response.ok) {
        const arrayBuffer = await response.arrayBuffer();
        fs.writeFileSync("generatedForm.pdf", Buffer.from(arrayBuffer));
        console.log("✅ PDF form generated successfully (saved as generatedForm.pdf)");
    } else {
        console.error("❌ Failed to generate PDF. Status:", response.status);
        console.error(await response.text());
    }
};

// Run the PDF generation function
generatePDF();

```

![create index.js](/help/forms/assets/api-6.png)

**Step 6: Run the Application**

```bash
node src/index.js
```

![run application](/help/forms/assets/api-7.png)

The PDF is created in the `demo-nodejs-generate-pdf` folder. Navigate to the folder to find the generated file named `generatedForm.pdf`. 

![view craeted pdf](/help/forms/assets/api-8.png)

![View PDF](/help/forms/assets/create-pdf.png)


You can open the [generated PDF](/help/forms/assets/create-pdf.png) to view it.

## Troubleshooting

### Common Issues and Possible Causes

#### Issue 1: 403 Forbidden Error

**Symptoms:**

- API requests return `403 Forbidden`
- Error message: *Unauthorized Access*

**Possible Cause:**

- Client ID not registered in the AEM instance's `api.yaml` configuration    

#### Issue 2: 401 Unauthorized Error

**Symptoms:**

- API requests return `401 Unauthorized`
- Error message: *Invalid or expired token*

**Possible Causes:**

- Access token expired (valid for 24 hours only)  
- Incorrect or mismatched Client ID and Client Secret  

#### Issue 3: 404 Not Found Error

**Symptoms:**

- API requests return `404 Not Found`
- Error message: *Resource not found* or *API endpoint not found*

**Possible Cause:**
 
- Incorrect bucket parameter (does not match AEM instance identifier)  

#### Issue 4: Pipeline Deployment Fails

**Symptoms:**

- Config Pipeline execution fails
- Deployment logs show errors related to `api.yaml`

**Possible Causes:**

- Invalid YAML syntax (indentation, quoting, or array format issues)  
- `api.yaml` placed in incorrect directory  
- Malformed or incorrect Client ID in the configuration  
- Invalid Client Secret

#### Issue 5: Forms Communication APIs fail to execute

**Symptoms:**

- API requests return errors indicating unsupported or unavailable features.
- PDF generation using XDP and XML does not work.
- Pipeline deployment completes successfully, but runtime API calls fail.

**Possible Cause:**

The AEM environment is running a version released before Forms Communication APIs were introduced or supported.
To update the AEM environment refer to the [Update AEM instance](#update-aem-instance) section.

## Update AEM instance

To update the AEM instance to locate Environment Details:

1. Select the `ellipsis`(...) icon next to the environment name and click **Update**
2. Click the **Submit** button and run the suggested Fullstack Pipeline.

    ![Update Environment](/help/forms/assets/update-env.png)

## Related Articles

- To learn how to set up environment for Batch (Asynchronous APIs), see [AEM Forms as a Cloud Service Communications Batch Processing](/help/forms/aem-forms-cloud-service-communications-batch-processing.md).

























        