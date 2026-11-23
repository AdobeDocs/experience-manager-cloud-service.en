---
title: Document barcode delivery and request parameter locking in Dynamic Media with OpenAPI
description: Learn how to deliver barcode images and protect request parameters in [!DNL Dynamic Media with OpenAPI].
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets."
exl-id:
---

# Deliver barcode or QR code images using Dynamic Media with OpenAPI{#deliver-barcode-images}

Dynamic Media with OpenAPI lets you request barcode or QR code images through a delivery URL. For example, a campaign can use a barcode delivery URL to include a personalized coupon barcode in an email.

The barcode request uses a blank canvas as its source and returns the generated image in the requested format. Request parameter locking helps protect query parameters from unauthorized changes.

This feature is available as a Limited Availability (LA) feature. Contact [Adobe Customer Support](https://helpx.adobe.com/contact.html) to request access.

## Before you begin {#before-you-begin}

* Ensure that Dynamic Media with OpenAPI is enabled for your environment.
* Obtain the required access to use the barcode delivery functionality.
* Obtain a valid lock token for the barcode request. The lock-generation process is not covered in this article.

## Request a barcode or QR code image {#request-barcode-image}

To request a barcode or QR code image, send a GET request to the barcode delivery endpoint.

```http
GET https://<tenant-delivery-host>/adobe/assets/urn:aaid:aem:canvas/as/coupon-barcode.png?barcode=DEMO123%2Ccode128&token=<URL-encoded-lock-token>&width=400&height=500
```

>[!NOTE]
>
>URL-encode reserved characters in the `barcode` and `token` parameter values when including them in the request URL. URL transport encoding does not define the input used to generate or validate the lock signature.

Replace the placeholders with the values for your request.

| Parameter | Description |
| --- | --- |
| `tenant-delivery-host` | The delivery host for your environment. |
| `seoName` | An SEO-friendly name for the requested image. This name is cosmetic and does not determine the barcode content. |
| `format` | The output image format. Supported formats are `png` and `svg`. |
| `barcode` | The barcode value, optionally followed by a comma and the barcode type. For example, `DEMO123,code128`. If you omit the type, the default is `code128`. |
| `token` | The lock token associated with the barcode request. |
| `width` | The requested image width. |
| `height` | The requested image height. |

## Configure barcode request parameters {#configure-request-parameters}

Use the request parameters to specify the barcode content, output format, and image dimensions.

### Barcode value and type {#barcode-value-and-type}

The `barcode` parameter accepts the barcode value and an optional barcode type.

Use the following syntax:

```text
codevalue[,type]
```

* `codevalue` specifies the content to encode in the barcode.
* `type` specifies the barcode type and is optional. If you omit it, the default type is `code128`.

Separate the barcode value and type with a comma when specifying the type.
For example:

```http
barcode=DEMO123%2Ccode128
```

To use the default barcode type, specify only the barcode value:

```http
barcode=DEMO123
```
The supported barcode types are:

* `code128`
* `qr`

The barcode value is the content that a scanner reads when it scans the generated image.

### Image format {#image-format}

Specify the output format in the request URL.

| Format | Description |
| --- | --- |
| `png` | Requests a PNG image. |
| `svg` | Requests an SVG image. |

### Image dimensions {#image-dimensions}

Use the `width` and `height` parameters to specify the requested image dimensions.

* The supported range for both dimensions is 1 to 2000.
* The default width is 300 pixels.
* The default height is 100 pixels for Code 128 barcodes and 300 pixels for QR codes.
* The `width` and `height` parameters apply to PNG output. They are ignored for SVG output.

>[!NOTE]
>
>If the requested dimensions are too small to accommodate the barcode grid, the request can return a `400 Bad Request` response.

## Understand request parameter locking {#understand-request-locking}

Request parameter locking protects the query parameters specified in the locked-field list inside the `token` parameter.

The lock token uses the following structure:

```text
lock:<signature>[:<field-list>[:<keyId>]]
```

The `lock` prefix and signature are mandatory. The field list and `keyId` are optional.

* `signature`: The signature used to validate the locked request parameters.
* `field-list`: The query parameters to protect. If this field is omitted or empty, the configured default field list is used. If no default field list is configured, all query parameters except `token` are validated in request order.
* `keyId`: Identifies the key associated with the lock.

To protect the barcode request, include `barcode` in the field list.

Examples of barcode-locking tokens:

```text
token=lock:<signature>:barcode
```

```text
token=lock:<signature>:barcode:<keyId>
```

When `barcode` is included in the locked-field list, the lock protects its complete value, including the barcode type when specified.

Changing a locked query parameter while reusing the same token causes validation to fail. To request a different barcode value, use a lock that is valid for the new request parameters.

## Troubleshoot barcode requests {#troubleshoot}

If a barcode request fails, review the request parameters and lock token.

| Issue | What to check |
| --- | --- |
| The barcode parameter is missing or invalid. | Verify that the barcode value is provided. If you specify a barcode type, separate it from the value with a comma. The type is optional and defaults to `code128`. |
| The lock is invalid or revoked. | Verify that the request uses a valid lock token. |
| A locked parameter does not match the lock. | Verify that the query parameter values match those protected by the lock. Obtain a new lock if you need to change a locked value. |
| The barcode type is unsupported. | If you specify a barcode type, verify that it is either `code128` or `qr`. |
| The image dimensions are invalid. | Verify that the requested width and height are within the supported range and are large enough to accommodate the barcode grid. |

## Check the response {#check-response}

A successful request returns the generated barcode or QR code image.

The API can return the following response statuses:

| Status code | Description |
| --- | --- |
| `200` | The request succeeded, and the generated image is returned. |
| `400` | The request is invalid. This can include a missing barcode parameter, a missing or invalid lock, a revoked lock, an unsupported barcode type, or invalid image dimensions. |
| `500` | The service encountered an internal error, such as a locking or key-storage failure, or a barcode image-generation failure. |

If you receive an error response, review the request parameters and lock token before retrying the request.

## Related articles {#related-articles}

For more information about Dynamic Media with OpenAPI and asset delivery, see:

* [Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)
* [Integrate AEM Assets with downstream applications](/help/assets/integrate-dynamic-media-open-apis.md)
* [Delivery APIs](/help/assets/deliver-assets-apis.md)