---
title: How to use AFP output sync API?
description: Learn how to use the AFP Output Sync API to retrieve and synchronize output renditions.
feature: Adaptive Forms, APIs & Integrations, Document Services
role: Admin, User
exl-id: 5602fc63-ef74-44eb-b3be-61b8f8a2795a
---
# Generate AFP Output Using the AEM Forms API

<span class="preview"> This is a pre-release feature and accessible through our [pre-release channel](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/release-notes/prerelease.html#new-features). </span> 

Advanced Function Presentation (AFP) is a high-performance document format designed primarily for printing purposes.  
This guide outlines all necessary steps and configurations to generate AFP output using AEM Forms.

<!--
## Prerequisites

To support AFP output generation, the following OSGi bundles must be present and in an **active** state:

* **AFP Core Bundle** – Available in the AFP repository
* **Forms Output Core** – Found in the Forms Output comments package
* **Bedrock Connector** – Provided by the Forms Output API
* **Cloud Ready Implementation** – Available through the Forms installer

>[!NOTE]
>
> * If any bundle is inactive, resolve dependency issues or reinstall manually.
> * To enable AFP generation, the `FT_FORMS-17887` toggle configurations must be set in AEM configuration manager.-->

## AFP Generation API

Generates an AFP (Advanced Function Presentation) file using an XDP template and input data.

### Authorization

You can either use **BasicAuth** (Admin credentials) for local environments or **BearerAuth** authorization for AEM Cloud instances.

### Request

**Endpoint:**
`POST http://<server>:<port>/adobe/forms/document/generate/afp`

### Headers

| Key             | Value                                                  |
| --------------- | ------------------------------------------------------ |
| `Content-Type`  | `application/pdf`                                      |
| `Authorization` | `(Bearer Access token)` |

### Request Body

**Content-Type: multipart/form-data**

| Key        | Type | Required | Description                                                               |
| ---------- | ---- | -------- | ------------------------------------------------------------------------- |
| `template` | File/Text | Yes      | XDP file used as the template for AFP generation (e.g., `demo.xdp`)       |
| `data`     | File/Text | No       | Data file (XML or JSON) to be merged with the template (e.g., `data.xml`) |
| `options`  | Text | No       | JSON string with options to control AFP output (e.g., resolution, locale) |

**Example `options` JSON (Text field):**

```json
{
  "pdfVersion": "1.7",
  "resolution": 300,
  "locale": "en-US",
  "embedFonts": true,
  "contentRoot": "/usr/tmp"
}
```

### Responses

| Code  | Description                                                               |
| ----- | ------------------------------------------------------------------------- |
| `200` | Operation successful. Returns the AFP document stream.                    |
| `400` | Bad Request. The request payload is malformed or missing required fields. |
| `500` | Internal Server Error. Try again after some time.                         |

### Curl Command

```
curl --location 'http://<server>:<port>/adobe/forms/document/generate/afp' \
--header 'Authorization: Bearertoken <base64-encoded-credentials>' \
--form 'template=@"<path-to-template>.xdp"' \
--form 'data=@"<path-to-data-file>.xml"' \
--form 'options=<JSON-options-string>'
```

### Testing the API

You can download the .yaml file and upload it to Postman to check functionality of the APIs.

![AFP Postman image](/help/forms/assets/afp-postman.png)

You can save the response and open the saved file in AFP reader to view it.

![PDF reader](/help/forms/assets/afp-pdf.png)
