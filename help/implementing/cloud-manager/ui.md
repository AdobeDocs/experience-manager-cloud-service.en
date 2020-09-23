---
title: UI Testing - Cloud Services
description: UI Testing - Cloud Services
---

# UI Testing {#ui-testing}

UI tests are packaged as Docker images in order to allow a wide choice in language and frameworks (such as Java and Maven, or Node and WebDriver.io). The Docker image can be created with standard tooling, but it must respect certain conventions during its execution. When running the Docker image, a Selenium server is automatically provisioned. The runtime conventions described below allow your test code to access both the Selenium server and the AEM instances under test.

## Environment variables {#environment-variables}

The following environment variables will be passed to your Docker image at run time.

|Variable|Examples|Description|
|---|---|---|
|`SELENIUM_BASE_URL`|`http://my-ip:4444`|The URL of the Selenium server|
|`SELENIUM_BROWSER`|`chrome`, `firefox`|The browser implementation used by the Selenium Server|
|`AEM_AUTHOR_URL`|`http://my-ip:4502/context-path`|The URL of the AEM author instance|
|`AEM_AUTHOR_USERNAME`|`admin`|The username to login to the AEM author instance|
|`AEM_AUTHOR_PASSWORD`|`admin`|The password  to login to the AEM author instance|
|`AEM_PUBLISH_URL`|`http://my-ip:4503/context-path`|The URL of the AEM publish instance|
|`AEM_PUBLISH_USERNAME`|`admin`|The username to login to the AEM publish instance|
|`AEM_PUBLISH_PASSWORD`|`admin`|The password  to login to the AEM publish instance|
|`REPORTS_PATH`|`/usr/src/app/reports`|The path where the XML report of the test results must be saved|
|`UPLOAD_URL`|`http://upload-host:9090/upload`|The URL where file must be uploaded to in order to make them accessible to Selenium|

## Waiting for Selenium to be ready {#waiting-for-selenium}

Before the tests start, it's the responsibility of the Docker image to ensure that the Selenium server is up and running. Waiting for the Selenium service is a two-steps process:

1. Read the URL of the Selenium service from the `SELENIUM_BASE_URL` environment variable.
2. Poll at regular interval to the [status endpoint](https://github.com/SeleniumHQ/docker-selenium/#waiting-for-the-grid-to-be-ready) exposed by the Selenium API.

Once the Selenium's status endpoint answers with a positive response, the tests can finally start.

## Generate the test reports {#generate-test-reports}

The Docker image must generate test reports in the JUnit XML format and save them in the path specified by the environment variable `REPORTS_PATH`. The JUnit XML format is a widespread format for reporting the results of tests. If the Docker image uses Java and Maven, both the [Maven Surefire Plugin](https://maven.apache.org/surefire/maven-surefire-plugin/) and the [Maven Failsafe Plugin](https://maven.apache.org/surefire/maven-failsafe-plugin/). If the Docker image is implemented with other programming languages or test runners, check the documentation for the chosen tools to know how to generate JUnit XML reports.

## Upload files (#upload-files)

Tests sometimes must upload files to the application under test. In order to maintain keep the deployment of Selenium relative to your tests flexible, it is not possible to directly upload an asset directly to Selenium. Instead, uploading a file goes through some intermediate steps:

1. Upload the file at the URL specified by the `UPLOAD_URL` environment variable. The upload must be performed in one POST request with a multipart form. The multipart form must have a single file field. This is equivalent to `curl -X POST ${UPLOAD_URL} -F "data=@file.txt"`. Consult the documentation and libraries of the programming language used in the Docker image to know how to perform such an HTTP request.
2. If the upload is successful, the request returns a `200 OK` response of type `text/plain`. The content of the response is an opaque file handle. You can use this handle in place of a file path in an `<input>` element to test file uploads in your application.
