---
title: Custom Code Quality Rules
description: Learn about Cloud Manager's custom code quality rules, based on Adobe Experience Manager Engineering best practices, to ensure high-quality code through thorough testing.
exl-id: f40e5774-c76b-4c84-9d14-8e40ee6b775b
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---
# Custom code quality rules {#custom-code-quality-rules} 

>[!CONTEXTUALHELP]
>id="aemcloud_nonbpa_customcodequalityrules"
>title="Custom Code Quality Rules"
>abstract="Learn about Cloud Manager's custom code quality rules, based on Adobe Experience Manager Engineering best practices, to ensure high-quality code through thorough testing."

Learn about Cloud Manager's custom code quality rules, based on Adobe Experience Manager Engineering best practices, to ensure high-quality code through thorough testing. See also [code quality testing](/help/implementing/cloud-manager/code-quality-testing.md).

Full SonarQube rules are not available for download due to Adobe proprietary information. You can download the complete list of *current* rules [using this link](/help/implementing/cloud-manager/assets/CodeQuality-rules-latest-CS.xlsx). Continue reading this document for descriptions and examples of the rules.

>[!IMPORTANT]
>
>Starting Thursday, February 13, 2025 (Cloud Manager 2025.2.0), Cloud Manager Code Quality is using an updated SonarQube 9.9 version and an updated list of rules that you can [download here](/help/implementing/cloud-manager/assets/CodeQuality-rules-latest-CS-2024-12-0.xlsx).

>[!NOTE]
>
>The code samples provided here are only for illustrative purposes. See the SonarQube [Concepts documentation](https://docs.sonarsource.com/sonarqube/latest/) to learn about SonarQube concepts and quality rules.

## SonarQube rules {#sonarqube-rules}

The following section details SonarQube rules executed by Cloud Manager.

### Do not use potentially dangerous functions {#do-not-use-potentially-dangerous-functions}

* **Key**: CQRules:CWE-676
* **Type**: Vulnerability
* **Severity**: Major
* **Since**: Version 2018.4.0

The methods `Thread.stop()` and `Thread.interrupt()` can produce hard-to-reproduce issues and, sometimes, security vulnerabilities. Their usage should be tightly monitored and validated. In general, message passing is a safer way to accomplish similar goals.

#### Non-compliant code {#non-compliant-code}

```java
public class DontDoThis implements Runnable {
  private Thread thread;
 
  public void start() {
    thread = new Thread(this);
    thread.start();
  }
 
  public void stop() {
    thread.stop();  // UNSAFE!
  }
 
  public void run() {
    while (true) {
        somethingWhichTakesAWhileToDo();
    }
  }
}
```

#### Compliant code {#compliant-code}

```java
public class DoThis implements Runnable {
  private Thread thread;
  private boolean keepGoing = true;
 
  public void start() {
    thread = new Thread(this);
    thread.start();
  }
 
  public void stop() {
    keepGoing = false;
  }
 
  public void run() {
    while (this.keepGoing) {
        somethingWhichTakesAWhileToDo();
    }
  }
}
```

### Do not use format strings that may be externally controlled {#do-not-use-format-strings-which-may-be-externally-controlled}

* **Key**: CQRules:CWE-134
* **Type**: Vulnerability
* **Severity**: Major
* **Since**: Version 2018.4.0

Using a format string from an external source (such as a request parameter or user-generated content) can expose an application to denial of service attacks. There are circumstances where a format string may be externally controlled, but is only allowed from trusted sources.

#### Non-compliant code {#non-compliant-code-1}

```java
protected void doPost(SlingHttpServletRequest request, SlingHttpServletResponse response) {
  String messageFormat = request.getParameter("messageFormat");
  request.getResource().getValueMap().put("some property", String.format(messageFormat, "some text"));
  response.sendStatus(HttpServletResponse.SC_OK);
}
```

### HTTP requests should always have socket and connect timeouts {#http-requests-should-always-have-socket-and-connect-timeouts}

* **Key**: CQRules:ConnectionTimeoutMechanism
* **Type**: Bug
* **Severity**: Critical
* **Since**: Version 2018.6.0

When making HTTP requests within an Experience Manager application, it is essential to configure appropriate timeouts to prevent unnecessary thread consumption. 
By default, both the Java&trade; HTTP Client (java.net.HttpUrlConnection) and the widely used Apache HTTP Components client do not impose timeouts, so they must be manually configured. As a best practice, timeouts should be set to 60 seconds or less.

#### Non-compliant code {#non-compliant-code-2}

```java
@Reference
private HttpClientBuilderFactory httpClientBuilderFactory;
 
public void dontDoThis() {
  HttpClientBuilder builder = httpClientBuilderFactory.newBuilder();
  HttpClient httpClient = builder.build();

  // do something with the client
}

public void dontDoThisEither() {
  URL url = new URL("http://www.google.com");
  URLConnection urlConnection = url.openConnection();
 
  BufferedReader in = new BufferedReader(new InputStreamReader(
    urlConnection.getInputStream()));
 
  String inputLine;
  while ((inputLine = in.readLine()) != null) {
    logger.info(inputLine);
  }
 
  in.close();
}
```

#### Compliant code {#compliant-code-1}

```java
@Reference
private HttpClientBuilderFactory httpClientBuilderFactory;
 
public void doThis() {
  HttpClientBuilder builder = httpClientBuilderFactory.newBuilder();
  RequestConfig requestConfig = RequestConfig.custom()
    .setConnectTimeout(5000)
    .setSocketTimeout(5000)
    .build();
  builder.setDefaultRequestConfig(requestConfig);
 
  HttpClient httpClient = builder.build();
   
  // do something with the client
}

public void orDoThis () {
  URL url = new URL("http://www.google.com");
  URLConnection urlConnection = url.openConnection();
  urlConnection.setConnectTimeout(5000);
  urlConnection.setReadTimeout(5000);
 
  BufferedReader in = new BufferedReader(new InputStreamReader(
    urlConnection.getInputStream()));
 
  String inputLine;
  while ((inputLine = in.readLine()) != null) {
    logger.info(inputLine);
  }
 
  in.close();
}
```

### Always close ResourceResolver objects {#resourceresolver-objects-should-always-be-closed}

* **Key**: CQRules:CQBP-72
* **Type**: `Code Smell`
* **Severity**: Major
* **Since**: Version 2018.4.0

ResourceResolver objects obtained from the `ResourceResolverFactory` consume system resources. Although there are measures in place to reclaim these resources when a `ResourceResolver` is no longer in use, it is more efficient to close any opened `ResourceResolver` objects explicitly by calling the `close()` method.

A common misconception is that `ResourceResolver` objects created with an existing JCR session should not be explicitly closed, or that closing them affects the JCR session. This information is incorrect. A `ResourceResolver` should always be closed when it is no longer needed. Since `ResourceResolver` implements the `Closeable` interface, you can also use the `try-with-resources` syntax instead of calling `close()` directly.

#### Non-compliant code {#non-compliant-code-4}

```java
public void dontDoThis(Session session) throws Exception {
  ResourceResolver resolver = factory.getResourceResolver(Collections.singletonMap("user.jcr.session", (Object)session));
  // do some stuff with the resolver
}
```

#### Compliant code {#compliant-code-2}

```java
public void doThis(Session session) throws Exception {
  ResourceResolver resolver = null;
  try {
    resolver = factory.getResourceResolver(Collections.singletonMap("user.jcr.session", (Object)session));
    // do something with the resolver
  } finally {
    if (resolver != null) {
      resolver.close();
    }
  }
}

public void orDoThis(Session session) throws Exception {
  try (ResourceResolver resolver = factory.getResourceResolver(Collections.singletonMap("user.jcr.session", (Object) session))){
    // do something with the resolver
  }
}
```

### Do not use Sling servlet paths to register servlets {#do-not-use-sling-servlet-paths-to-register-servlets}

* **Key**: CQRules:CQBP-75
* **Type**: `Code Smell`
* **Severity**: Major
* **Since**: Version 2018.4.0

As described in the [Sling documentation](https://sling.apache.org/documentation/the-sling-engine/servlets.html), bindings servlets by paths are discouraged. Path-bound servlets cannot use standard JCR access controls and, as a result, require additional security rigor. Rather than using path-bound servlets, it is recommended to create nodes in the repository and register servlets by resource type.

#### Non-compliant code {#non-compliant-code-5}

```java
@Component(property = {
  "sling.servlet.paths=/apps/myco/endpoint"
})
public class DontDoThis extends SlingAllMethodsServlet {
 // implementation
}
```

### Caught exceptions should be logged or thrown, not both {#caught-exceptions-should-be-logged-or-thrown-but-not-both}

* **Key**: CQRules:CQBP-44---CatchAndEitherLogOrThrow
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2018.4.0

In general, an exception should be logged exactly one time. Logging exceptions multiple times can cause confusion. The reason is because it is unclear how many times an exception occurred. The most common pattern that leads to this effect is logging and throwing a caught exception.

#### Non-compliant code {#non-compliant-code-6}

```java
public void dontDoThis() throws Exception {
  try {
    someOperation();
  } catch (Exception e) {
    logger.error("something went wrong", e);
    throw e;
  }
}
```

#### Compliant code {#compliant-code-3}

```java
public void doThis() {
  try {
    someOperation();
  } catch (Exception e) {
    logger.error("something went wrong", e);
  }
}

public void orDoThis() throws MyCustomException {
  try {
    someOperation();
  } catch (Exception e) {
    throw new MyCustomException(e);
  }
}
```

### Avoid log statements immediately followed by a throw statement {#avoid-having-a-log-statement-immediately-followed-by-a-throw-statement}

* **Key**: CQRules:CQBP-44---ConsecutivelyLogAndThrow
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2018.4.0

Another common pattern to avoid is to log a message and then immediately throw an exception. This practice generally indicates that the exception message ends up duplicated in log files.

#### Non-compliant code {#non-compliant-code-7}

```java
public void dontDoThis() throws Exception {
  logger.error("something went wrong");
  throw new RuntimeException("something went wrong");
}
```

#### Compliant code {#compliant-code-4}

```java
public void doThis() throws Exception {
  throw new RuntimeException("something went wrong");
}
```

### Avoid logging at INFO when handling GET or HEAD requests {#avoid-logging-at-info-when-handling-get-or-head-requests}

* **Key**: CQRules:CQBP-44---LogInfoInGetOrHeadRequests
* **Type**: `Code Smell`
* **Severity**: Minor

In general, the INFO log level should be used to demarcate important actions and, by default, Experience Manager is configured to log at the INFO level or above. GET and HEAD methods should only ever be read-only operations and thus do not constitute important actions. Logging at the INFO level in response to GET or HEAD requests is likely to create significant log noise, making it harder to identify useful information in log files. When handling GET or HEAD requests, log at the WARN or ERROR levels if something has gone wrong. Use DEBUG or TRACE levels if detailed troubleshooting information is needed.

>[!NOTE]
>
>Does not apply to `access.log`-type logging for each request.

#### Non-compliant code {#non-compliant-code-8}

```java
public void doGet() throws Exception {
  logger.info("handling a request from the user");
}
```

#### Compliant code {#compliant-code-5}

```java
public void doGet() throws Exception {
  logger.debug("handling a request from the user.");
}
```

### Do not use Exception.getMessage() as the first parameter of a logging statement {#do-not-use-exception-getmessage-as-the-first-parameter-of-a-logging-statement}

* **Key**: CQRules:CQBP-44---ExceptionGetMessageIsFirstLogParam
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2018.4.0

As a best practice, log messages should provide contextual information about where in the application an exception has occurred. While context can also be determined by using stack traces, in general the log message is going to be easier to read and understand. As a result, when logging an exception, it is a bad practice to use the exception's message as the log message. The exception message explains what went wrong, while the log message should inform the reader about what the application was doing when the exception occurred. The exception message is still logged. By specifying your own message, the logs are easier to understand.

#### Non-compliant code {#non-compliant-code-9}

```java
public void dontDoThis() {
  try {
    someMethodThrowingAnException();
  } catch (Exception e) {
    logger.error(e.getMessage(), e);
  }
}
```

#### Compliant code {#compliant-code-6}

```java
public void doThis() {
  try {
    someMethodThrowingAnException();
  } catch (Exception e) {
    logger.error("Unable to do something", e);
  }
}
```

### Logging in catch blocks should be at the WARN or ERROR level {#logging-in-catch-blocks-should-be-at-the-warn-or-error-level}

* **Key**: CQRules:CQBP-44---WrongLogLevelInCatchBlock
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2018.4.0

As the name suggests, Java&trade; exceptions should always be used in exceptional circumstances. As a result, when an exception is caught, it is important to ensure that log messages are logged at the appropriate level, either WARN or ERROR. This process ensures that those messages appear correctly in the logs.

#### Non-compliant code {#non-compliant-code-10}

```java
public void dontDoThis() {
  try {
    someMethodThrowingAnException();
  } catch (Exception e) {
    logger.debug(e.getMessage(), e);
  }
}
```

#### Compliant code {#compliant-code-7}

```java
public void doThis() {
  try {
    someMethodThrowingAnException();
  } catch (Exception e) {
    logger.error("Unable to do something", e);
  }
}
```

### Do not print stack traces to the console {#do-not-print-stack-traces-to-the-console}

* **Key**: CQRules:CQBP-44---ExceptionPrintStackTrace
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2018.4.0

As mentioned, context is critical when understanding log messages. Using `Exception.printStackTrace()` causes only the stack trace to be output to the standard error stream, losing all context. Further, in a multi-threaded application like Experience Manager, if multiple exceptions are printed using this method in parallel, their stack traces may overlap, which produces significant confusion. Exceptions should be logged through the logging framework only.

#### Non-compliant code {#non-compliant-code-11}

```java
public void dontDoThis() {
  try {
    someMethodThrowingAnException();
  } catch (Exception e) {
    e.printStackTrace();
  }
}
```

#### Compliant code {#compliant-code-8}

```java
public void doThis() {
  try {
    someMethodThrowingAnException();
  } catch (Exception e) {
    logger.error("Unable to do something", e);
  }
}
```

### Do not output to standard output or standard error {#do-not-output-to-standard-output-or-standard-error}

* **Key**: CQRules:CQBP-44—LogLevelConsolePrinters
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2018.4.0

Logging in Experience Manager should always be done through the logging framework (SLF4J). Outputting directly to the standard output or standard error streams loses the structural and contextual information provided by the logging framework. Sometimes, it may cause performance issues.

#### Non-compliant code {#non-compliant-code-12}

```java
public void dontDoThis() {
  try {
    someMethodThrowingAnException();
  } catch (Exception e) {
    System.err.println("Unable to do something");
  }
}
```

#### Compliant code {#compliant-code-9}

```java
public void doThis() {
  try {
    someMethodThrowingAnException();
  } catch (Exception e) {
    logger.error("Unable to do something", e);
  }
}
```

### Avoid hardcoded apps and libs paths {#avoid-hardcoded-apps-and-libs-paths}

* **Key**: CQRules:CQBP-71
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2018.4.0

Paths starting with `/libs` and `/apps` should generally not be hardcoded. These paths are usually stored relative to the Sling search path, which defaults to `/libs,/apps`. Using the absolute path may introduce subtle defects that would only appear later in the project lifecycle.

#### Non-compliant code {#non-compliant-code-13}

```java
public boolean dontDoThis(Resource resource) {
  return resource.isResourceType("/libs/foundation/components/text");
}
```

#### Compliant code {#compliant-code-10}

```java
public void doThis(Resource resource) {
  return resource.isResourceType("foundation/components/text");
}
```

### Do not use Sling scheduler {#sonarqube-sling-scheduler}

* **Key**: CQRules:AMSCORE-554
* **Type**: `Code Smell`/Cloud Service Compatibility
* **Severity**: Minor
* **Since**: Version 2020.5.0

Do not use the Sling Scheduler for tasks that require a guaranteed execution. Sling Scheduled Jobs guarantee execution and better suited for both clustered and non-clustered environments. 

See [Apache Sling Eventing and Job Handling](https://sling.apache.org/documentation/bundles/apache-sling-eventing-and-job-handling.html) to learn more about how Sling Jobs are handled in clustered environments.

### Do not use Experience Manager deprecated APIs {#sonarqube-aem-deprecated}

* **Key**: AMSCORE-553
* **Type**: `Code Smell`/Cloud Service Compatibility
* **Severity**: Minor
* **Since**: Version 2020.5.0

The Experience Manager API surface is under constant revision to identify APIs for which usage is discouraged and thus considered deprecated. 

Often, these APIs are deprecated using the standard Java&trade; `@Deprecated` annotation and, as such, as identified by `squid:CallToDeprecatedMethod`.

However, there are cases where an API is deprecated in the context of Experience Manager but may not be deprecated in other contexts. This rule identifies this second class.

### Do not use @Inject annotation with @Optional in Sling Models {#sonarqube-slingmodels-inject-optional}

* **Key**: InjectAnnotationWithOptionalInjectionCheck
* **Type**: Software quality
* **Severity**: Minor
* **Since**: Version 2023.11

The Apache Sling project discourages the use of the `@Inject` annotation in the context of Sling Models, as it can lead to bad performance when combined with the `DefaultInjectionStrategy.OPTIONAL` (either at field or class level). Instead, more specific injections (like the `@ValueMapValue` or `@OsgiInjector` annotations) should be used.

Check the [Apache Sling documentation](https://sling.apache.org/documentation/bundles/models.html#discouraged-annotations-1) for more information about the recommended annotations and why this recommendation was made in the first place.


### Reuse instances of a HTTPClient {#sonarqube-reuse-httpclient}

* **Key**: AEMSRE-870
* **Type**: Software quality
* **Severity**: Minor
* **Since**: Version 2023.11

AEM applications often reach out to other applications using the HTTP protocol, and the Apache HttpClient is an often used library to achieve this end. But the creation of such an HttpClient object comes with some overhead, so these objects should be reused as much as possible. 

This rule checks that such an HttpClient object is not private within a method, but global on a class level, so it can be reused. In this case, the HttpClient field should be set in the constructor of the class or the `activate()` method (if this class is an OSGi component/service). 

Check the [Optimization Guide](https://hc.apache.org/httpclient-legacy/performance.html) of the HttpClient for some best practices regarding the use of the HttpClient.

#### Non-compliant code {#non-compliant-code-14}

```java
public void doHttpCall() {
  HttpClient httpclient = HttpClients.createDefault();
  // do something with the httpclient
}
```

#### Compliant code {#compliant-code-11}

```java

public class myClass {

  HttpClient httpclient;

  public void doHttpCall() {
    // do something with the httpclient
  }

}
```

## OakPAL content rules {#oakpal-rules}

The following section details the OakPAL checks executed by Cloud Manager.

>[!NOTE]
>
>OakPAL is a framework, which validates content packages using a standalone Oak repository. An Experience Manager Partner, who won the 2019 Experience Manager Rockstar North America award, developed it.

### Customers should not implement or extend Product APIs annotated with @ProviderType{#product-apis-annotated-with-providertype-should-not-be-implemented-or-extended-by-customers}

* **Key**: CQBP-84
* **Type**: Bug
* **Severity**: Critical
* **Since**: Version 2018.7.0

The Experience Manager API contains Java&trade; interfaces and classes, which are only meant to be used -- but not implemented -- by custom code. For example, only Experience Manager should implement the `com.day.cq.wcm.api.Page` interface.

When new methods are added to these interfaces, those additional methods do not impact existing code that uses these interfaces. As a result, the addition of new methods to these interfaces is considered to be backwards-compatible. However, if custom code implements one of these interfaces, that custom code has introduced a backwards-compatibility risk for the customer.

Interfaces and classes -- as implemented by Experience Manager -- are annotated with `org.osgi.annotation.versioning.ProviderType` or sometimes a similar legacy annotation `aQute.bnd.annotation.ProviderType`. This rule identifies cases where custom code implements such an interface or extends a class.

#### Non-compliant code {#non-compliant-code-3}

```java
import com.day.cq.wcm.api.Page;

public class DontDoThis implements Page {
// implementation here
}
```

### Custom Lucene Oak indexes must have a Tika configuration {#oakpal-indextikanode}

* **Key**: IndexTikaNode
* **Type**: Bug
* **Severity**: Blocker
* **Since**: 2021.8.0

Multiple out-of-the-box Experience Manager Oak indexes include a Tika configuration and customizations of these indexes must include a Tika configuration. This rule checks for customizations of the `damAssetLucene`, `lucene`, and `graphqlConfig` indexes and raises an issue if either the `tika`  node is missing or if the `tika` node is missing a child node named `config.xml`.

See [indexing documentation](/help/operations/indexing.md#preparing-the-new-index-definition) for more information on customizing index definitions.

#### Non-compliant code {#non-compliant-code-indextikanode}

```text
+ oak:index
    + damAssetLucene-1-custom
      - async: [async]
      - evaluatePathRestrictions: true
      - includedPaths: /content/dam
      - tags: [visualSimilaritySearch]
      - type: lucene
```

#### Compliant code {#compliant-code-indextikanode}

```text
+ oak:index
    + damAssetLucene-1-custom-2
      - async: [async]
      - evaluatePathRestrictions: true
      - includedPaths: /content/dam
      - tags: [visualSimilaritySearch]
      - type: lucene
      + tika
        + config.xml
```

### Custom Lucene Oak Indexes must not be synchronous {#oakpal-indexasync}

* **Key**: IndexAsyncProperty
* **Type**: Bug
* **Severity**: Blocker
* **Since**: 2021.8.0

Oak indexes of type `lucene` must always be asynchronously indexed. Failure to do so may result in system instability. More information on the structure of Lucene indexes can be found in the [Oak documentation](https://jackrabbit.apache.org/oak/docs/query/lucene.html#index-definition).

#### Non-compliant code {#non-compliant-code-indexasync}

```text
+ oak:index
    + damAssetLucene-1-custom
      - evaluatePathRestrictions: true
      - includedPaths: /content/dam
      - type: lucene
      - tags: [visualSimilaritySearch]
      + tika
        + config.xml
```

#### Compliant code {#compliant-code-indexasync}

```text
+ oak:index
    + damAssetLucene-1-custom-2
      - async: [async]
      - evaluatePathRestrictions: true
      - includedPaths: /content/dam
      - tags: [visualSimilaritySearch]
      - type: lucene
      + tika
        + config.xml
```

### Custom DAM Asset Lucene Oak indexes are properly structured {#oakpal-damAssetLucene-sanity-check}

* **Key**: IndexDamAssetLucene
* **Type**: Bug
* **Severity**: Blocker
* **Since**: 2021.6.0

For asset search to work correctly in Experience Manager Assets, customizations of the `damAssetLucene` Oak index must follow a set of guidelines that are specific to this index. This rule checks that the index definition must have a multi-valued property named `tags`, which contains the value `visualSimilaritySearch`.

#### Non-compliant code {#non-compliant-code-damAssetLucene}

```text
+ oak:index
    + damAssetLucene-1-custom
      - async: [async, nrt]
      - evaluatePathRestrictions: true
      - includedPaths: /content/dam
      - type: lucene
      + tika
        + config.xml
```

#### Compliant code {#compliant-code-damAssetLucene}

```text
+ oak:index
    + damAssetLucene-1-custom-2
      - async: [async, nrt]
      - evaluatePathRestrictions: true
      - includedPaths: /content/dam
      - tags: [visualSimilaritySearch]
      - type: lucene
      + tika
        + config.xml
```

### Customer packages should not create or modify nodes under libs {#oakpal-customer-package}

* **Key**: BannedPath
* **Type**: Bug
* **Severity**: Critical
* **Since**: Version 2019.6.0

It has been a long-standing best practice that the `/libs` content tree in the Experience Manager content repository should be considered read-only by customers. Modifying nodes and properties under `/libs` creates significant risk for major and minor updates. Use Adobe, through official channels, to make modifications to `/libs`.

### Packages should not contain duplicate OSGi configurations {#oakpal-package-osgi}

* **Key**: DuplicateOsgiConfigurations
* **Type**: Bug
* **Severity**: Major
* **Since**: Version 2019.6.0

A common problem that occurs in complex projects is where the same OSGi component is configured multiple times. This issue creates an ambiguity as to which configuration is applicable. This rule is "runmode-aware" in that it only identifies issues where the same component is configured multiple times in the same run mode or combination of run modes.

>[!NOTE]
>
>This rule produces issues where the same configuration, at the same path, is defined in multiple packages, including cases where the same package is duplicated in the overall list of built packages.
>
>For example, if the build produces packages named `com.myco:com.myco.ui.apps` and `com.myco:com.myco.all` where `com.myco:com.myco.all` embeds `com.myco:com.myco.ui.apps`, then all configurations within `com.myco:com.myco.ui.apps` are reported as duplicates.
>
>Generally, this situation is a case of not following the [Content Package Structure Guidelines](/help/implementing/developing/introduction/aem-project-content-package-structure.md). In this example, the package `com.myco:com.myco.ui.apps` is missing the `<cloudManagerTarget>none</cloudManagerTarget>` property.

#### Non-compliant code {#non-compliant-code-osgi}

```text
+ apps
  + projectA
    + config
      + com.day.cq.commons.impl.ExternalizerImpl
  + projectB
    + config
      + com.day.cq.commons.impl.ExternalizerImpl
```

#### Compliant code {#compliant-code-osgi}

```text
+ apps
  + shared-config
    + config
      + com.day.cq.commons.impl.ExternalizerImpl
```

### Config and install folders should only contain OSGi nodes {#oakpal-config-install}

* **Key**: ConfigAndInstallShouldOnlyContainOsgiNodes
* **Type**: Bug
* **Severity**: Major
* **Since**: Version 2019.6.0

For security reasons, paths containing `/config/` and `/install/` are only readable by administrative users in Experience Manager and should be used only for OSGi configuration and OSGi bundles. Placing other types of content under paths containing these segments causes application behavior to differ between administrative and non-administrative users unintentionally.

A common problem is use of nodes named `config` within component dialogs or when specifying the rich text editor configuration for inline editing. To resolve this issue, the offending node should be renamed to a compliant name. For the rich text editor configuration, use the `configPath` property on the `cq:inplaceEditing` node to specify the new location.

#### Non-compliant code {#non-compliant-code-config-install}

```text
+ cq:editConfig [cq:EditConfig]
  + cq:inplaceEditing [cq:InplaceEditConfig]
    + config [nt:unstructured]
      + rtePlugins [nt:unstructured]
```

#### Compliant code {#compliant-code-config-install}

```text
+ cq:editConfig [cq:EditConfig]
  + cq:inplaceEditing [cq:InplaceEditConfig]
    ./configPath = inplaceEditingConfig (String)
    + inplaceEditingConfig [nt:unstructured]
      + rtePlugins [nt:unstructured]
```

### Packages should not overlap {#oakpal-no-overlap}

* **Key**: PackageOverlaps
* **Type**: Bug
* **Severity**: Major
* **Since**: Version 2019.6.0

Similar to the [Packages Should Not Contain Duplicate OSGi Configurations rule](#oakpal-package-osgi), this situation is a common problem on complex projects where the same node path is written to by multiple separate content packages. While using content package dependencies can be used to ensure a consistent result, it is better to avoid overlaps entirely.

### The default authoring mode should not be classic UI {#oakpal-default-authoring}

* **Key**: ClassicUIAuthoringMode
* **Type**: `Code Smell`/Cloud Service Compatibility
* **Severity**: Minor
* **Since**: Version 2020.5.0

The OSGi configuration `com.day.cq.wcm.core.impl.AuthoringUIModeServiceImpl` defines the default authoring mode within Experience Manager. Because the Classic UI has been deprecated since Experience Manager 6.4, an issue is now raised when the default authoring mode is configured to Classic UI.

### Components with dialogs should have Touch UI dialogs {#oakpal-components-dialogs}

* **Key**: ComponentWithOnlyClassicUIDialog
* **Type**: `Code Smell`/Cloud Service Compatibility
* **Severity**: Minor
* **Since**: Version 2020.5.0

Experience Manager components that have a Classic UI dialog should always have a corresponding Touch UI dialog. Both offer an optimal authoring experience compatible with the Cloud Service deployment model, where Classic UI is no longer supported. This rule verifies the following scenarios:

* A component with a Classic UI dialog (that is, a `dialog` child node) must have a corresponding Touch UI dialog (that is, a `cq:dialog` child node).
* A component with a Classic UI design dialog (that is, a `design_dialog` node) must have a corresponding Touch UI design dialog (that is, a `cq:design_dialog` child node).
* A component with both a Classic UI dialog and a Classic UI design dialog must have both a corresponding Touch UI dialog and a corresponding Touch UI design dialog.

The Experience Manager Modernization Tools documentation provides documentation and tooling for how to convert components from Classic UI to Touch UI. See [the Experience Manager Modernization Tools documentation](https://opensource.adobe.com/aem-modernize-tools/) for more details.

### Packages should not mix mutable and immutable content {#oakpal-packages-immutable}

* **Key**: ImmutableMutableMixedPackage
* **Type**: `Code Smell`/Cloud Service Compatibility
* **Severity**: Minor
* **Since**: Version 2020.5.0

To be compatible with the Cloud Service deployment model, individual content packages must contain either content for the immutable areas of the repository (`/apps` and `/libs`), or the mutable area (everything not in `/apps` or `/libs`), but not both. For example, a package that includes both `/apps/myco/components/text` and `/etc/clientlibs/myco` is not compatible with Cloud Service and cause an issue to be reported.

>[!NOTE]
>
>The rule [Customer Packages Should Not Create or Modify Nodes Under libs](#oakpal-customer-package) always applies.

See [Experience Manager Project Structure](/help/implementing/developing/introduction/aem-project-content-package-structure.md) for more details.

### Do not use reverse replication agents {#oakpal-reverse-replication}

* **Key**: ReverseReplication
* **Type**: `Code Smell`/Cloud Service Compatibility
* **Severity**: Minor
* **Since**: Version 2020.5.0

Support for reverse replication is not available in Cloud Service deployments, as described as part of Experience Manager as a Cloud Service's [release notes](/help/release-notes/aem-cloud-changes.md#replication-agents).

Customers using reverse replication should contact Adobe for alternative solutions.

### Resources contained in proxy-enabled client libraries should be in a folder named resources {#oakpal-resources-proxy}

* **Key**: ClientlibProxyResource
* **Type**: Bug
* **Severity**: Minor
* **Since**: Version 2021.2.0

Experience Manager client libraries may contain static resources like images and fonts. As described in the document [Using Preprocessors](/help/implementing/developing/introduction/clientlibs.md#using-preprocessors), when using proxied client libraries these static resources must be contained in a child folder named `resources` to be effectively referenced on the publish instances.

#### Non-compliant code {#non-compliant-proxy-enabled}

```text
+ apps
  + projectA
    + clientlib
      - allowProxy=true
      + images
        + myimage.jpg
```

#### Compliant code {#compliant-proxy-enabled}

```tet
+ apps
  + projectA
    + clientlib
      - allowProxy=true
      + resources
        + myimage.jpg
```

### Usage of Cloud Service incompatible workflow processes {#oakpal-usage-cloud-service}

* **Key**: CloudServiceIncompatibleWorkflowProcess
* **Type**: Bug
* **Severity**: Major
* **Since**: Version 2021.2.0

With the shift to asset micro-services for asset processing in Adobe Experience Manager as a Cloud Service, several workflow processes used in on-premise and AMS versions are now unsupported. Many of these workflows have also become unnecessary.

The migration tool in the [Experience Manager as a Cloud Service Assets GitHub repository](https://github.com/adobe/aem-cloud-migration) can be used to update workflow models during migration to Experience Manager as a Cloud Service.

### Usage of static templates is discouraged in favor of editable templates {#oakpal-static-template}

* **Key**: StaticTemplateUsage
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2021.2.0

While the use of static templates is historically common in Experience Manager projects, Adobe recommends editable templates because they provide the most flexibility and support additional features not present in static templates. More information can be found in the document [Page Templates](/help/implementing/developing/components/templates.md).

Migration from static to editable templates can be largely automated using the [Experience Manager Modernization Tools](https://opensource.adobe.com/aem-modernize-tools/).

### Usage of legacy foundation components is discouraged {#oakpal-usage-legacy}

* **Key**: LegacyFoundationComponentUsage
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2021.2.0

The legacy Foundation Components (that is, components under `/libs/foundation`) have been deprecated for several Experience Manager releases in favor of the Core Components. Usage of the Foundation Components as the basis for custom components (whether by overlay or inheritance) is discouraged and should be converted to the corresponding Core Components.

[Experience Manager Modernization Tools](https://opensource.adobe.com/aem-modernize-tools/) can facilitate this conversion.

### Only use supported run mode names and ordering {#oakpal-supported-runmodes}

* **Key**: SupportedRunmode
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2021.2.0

Experience Manager as a Cloud Service enforces a strict naming policy for run mode names and a strict ordering for those run modes. The list of supported run modes is founded in the document [Deploying to Experience Manager as a Cloud Service](/help/implementing/deploying/overview.md#runmodes) and any deviation from this list is identified as an issue.

### Custom search index definition nodes must be direct children of `/oak:index` {#oakpal-custom-search}

* **Key**: OakIndexLocation
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2021.2.0

Experience Manager as a Cloud Service requires that custom search index definitions (that is, nodes of type `oak:QueryIndexDefinition`) be direct child nodes of `/oak:index`. Indexes in other locations must be moved to be compatible with Experience Manager as a Cloud Service. More information on search indexes can be found in the document [Content Search and Indexing](/help/operations/indexing.md).

### Custom search index definition nodes must have a compatVersion of 2 {#oakpal-custom-search-compatVersion}

* **Key**: IndexCompatVersion
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2021.2.0

Experience Manager as a Cloud Service requires that custom search index definitions (such as nodes of type `oak:QueryIndexDefinition`) must have the `compatVersion` property set to `2`. Adobe Experience Manager as a Cloud Service does not support any other value. See [Content Search and Indexing](/help/operations/indexing.md) for more information on search indexes.

### Descendent nodes of custom search index definition nodes must be of type `nt:unstructured `{#oakpal-descendent-nodes}

* **Key**: IndexDescendantNodeType
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2021.2.0

Hard to troubleshoot issues can occur when a custom search index definition node has unordered child nodes. To avoid this situation, it is recommended that all descendent nodes of an `oak:QueryIndexDefinition` node be of type `nt:unstructured`.

### Custom search index definition nodes must contain a child node named indexRules that has children {#oakpal-custom-search-index}

* **Key**: IndexRulesNode
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2021.2.0

A properly defined custom search index definition node must contain a child node named `indexRules`, which in turn must have at least one child. More information can be found in the [Oak documentation](https://jackrabbit.apache.org/oak/docs/query/lucene.html).

### Custom search index definition nodes must follow naming conventions {#oakpal-custom-search-definitions}

* **Key**: IndexName
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2021.2.0

Experience Manager as a Cloud Service requires that custom search index definitions (that is, nodes of type `oak:QueryIndexDefinition`) must be named following a specific pattern described in the document [Content Search and Indexing](/help/operations/indexing.md).

### Custom search index definition nodes must use the index type Lucene {#oakpal-index-type-lucene}

* **Key**: IndexType
* **Type**: Bug
* **Severity**: Blocker
* **Since**: Version 2021.2.0 (changed type and severity in 2021.8.0)

Experience Manager as a Cloud Service requires that custom search index definitions (that is, nodes of type `oak:QueryIndexDefinition`) have a `type` property with the value set to `lucene`. Indexing using legacy index types must be updated before migration to Experience Manager as a Cloud Service. See [Content Search and Indexing](/help/operations/indexing.md#how-to-use) for more information.

### Custom search index definition nodes must not contain a property named seed {#oakpal-property-name-seed}

* **Key**: IndexSeedProperty
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2021.2.0

Experience Manager as a Cloud Service prohibits custom search index definitions (that is, nodes of type `oak:QueryIndexDefinition`) from containing a property named `seed`. Indexing using this property must be updated before migration to Experience Manager as a Cloud Service. See the document [Content Search and Indexing](/help/operations/indexing.md#how-to-use) for more information.

### Custom search index definition nodes must not contain a property named reindex {#oakpal-reindex-property}

* **Key**: IndexReindexProperty
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2021.2.0

Experience Manager as a Cloud Service prohibits custom search index definitions (that is, nodes of type `oak:QueryIndexDefinition`) from containing a property named `reindex`. Indexing using this property must be updated before migration to Experience Manager as a 
Cloud Service. See the document [Content Search and Indexing](/help/operations/indexing.md#how-to-use) for more information.

### Custom DAM asset lucene nodes must not specify `queryPaths` {#oakpal-damAssetLucene-queryPaths}

* **Key**: IndexDamAssetLucene
* **Type**: Bug
* **Severity**: Blocker
* **Since**: Version 2022.1.0

#### Non-compliant code {#non-compliant-code-damAssetLucene-queryPaths}

```text
+ oak:index
    + damAssetLucene-1-custom-1
      - async: [async, nrt]
      - evaluatePathRestrictions: true
      - includedPaths: [/content/dam]
      - queryPaths: [/content/dam]
      - type: lucene
      + tika
        + config.xml
```

#### Compliant code {#compliant-code-damAssetLucene-queryPaths}

```text
+ oak:index
    + damAssetLucene-1-custom-2
      - async: [async, nrt]
      - evaluatePathRestrictions: true
      - includedPaths: [/content/dam]
      - tags: [visualSimilaritySearch]
      - type: lucene
      + tika
        + config.xml
```

### If the custom search index definition contains `compatVersion`, it must be set to 2 {#oakpal-compatVersion}

* **Key**: IndexCompatVersion
* **Type**: `Code Smell`
* **Severity**: Major
* **Since**: Version 2022.1.0


### Index node specifying `includedPaths` should also specify `queryPaths` with the same values {#oakpal-included-paths-without-query-paths}

* **Key**: IndexIncludedPathsWithoutQueryPaths
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2023.1.0

For custom indexes, configure `includedPaths` and `queryPaths` with identical values. If one is specified, the other must match it. However, there is a special case for indexes of `damAssetLucene`, including its custom versions. For these cases, only provide `includedPaths`.

### Index node specifying `nodeScopeIndex` on generic node type should also specify `includedPaths` and `queryPaths` {#oakpal-full-text-on-generic-node-type}

* **Key**: IndexFulltextOnGenericType
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2023.1.0

When setting the `nodeScopeIndex` property on a "generic" node type like `nt:unstructured` or `nt:base`, you must also specify the `includedPaths` and `queryPaths` properties. 
The node type `nt:base` can be considered "generic," because all node types inherit from it. So, setting a `nodeScopeIndex` on `nt:base` makes it index all nodes in the repository. Similarly, `nt:unstructured` is also considered "generic" as there are many nodes in repositories that are of this type.

#### Non-compliant code {#non-compliant-code-full-text-on-generic-node-type}

```text
+ oak:index/acme.someIndex-custom-1
  - async: [async, nrt]
  - evaluatePathRestrictions: true
  - tags: [visualSimilaritySearch]
  - type: lucene
    + indexRules
      - jcr:primaryType: nt:unstructured
      + nt:base
        - jcr:primaryType: nt:unstructured
        + properties
          + acme.someIndex-custom-1
            - nodeScopeIndex: true
```

#### Compliant code {#compliant-code-full-text-on-generic-node-type}

```text
+ oak:index/acme.someIndex-custom-1
  - async: [async, nrt]
  - evaluatePathRestrictions: true
  - tags: [visualSimilaritySearch]
  - type: lucene
  - includedPaths: ["/content/dam/"] 
  - queryPaths: ["/content/dam/"]
    + indexRules
      - jcr:primaryType: nt:unstructured
      + nt:base
        - jcr:primaryType: nt:unstructured
        + properties
          + acme.someIndex-custom-1
            - nodeScopeIndex: true
```

### The queryLimitReads property of the query engine should not be overridden {#oakpal-query-limit-reads}

* **Key**: OverrideOfQueryLimitReads
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2023.1.0

Overriding the default value can lead to slow page reads, particularly when more content is added. 

### Multiple active versions of the same index {#oakpal-multiple-active-versions}

* **Key**: IndexDetectMultipleActiveVersionsOfSameIndex
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2023.1.0

#### Non-compliant code {#non-compliant-code-multiple-active-versions}

```text
+ oak:index
  + damAssetLucene-1-custom-1
    ...
  + damAssetLucene-1-custom-2
    ...
  + damAssetLucene-1-custom-3
    ...
```

#### Compliant code {#compliant-code-multiple-active-versions}

```text
+ damAssetLucene-1-custom-3
    ...
```


### The name of fully custom index definitions should conform to the official guidelines {#oakpal-fully-custom-index-name}

* **Key**: IndexValidFullyCustomName
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2023.1.0

The expected pattern for fully custom index names is: `[prefix].[indexName]-custom-[version]`. More information can be found in the document [Content Search and Indexing](/help/operations/indexing.md).

### Same property with different analyzed values in the same index definition {#oakpal-same-property-different-analyzed-values}

#### Non-compliant code {#non-compliant-code-same-property-different-analyzed-values}

```text
+ indexRules
  + dam:Asset
    + properties
      + status
        - name: status
        - analyzed: true
  + dam:cfVariationNode
    + properties
      + status
        - name: status
```

#### Compliant code {#compliant-code-same-property-different-analyzed-values}

Example: 

```text
+ indexRules
  + dam:Asset
    + properties
      + status
        - name: status
        - analyzed: true
  + dam:cfVariationNode
    + properties
      + status
        - name: status
        - analyzed: true
```

Example: 

```text
+ indexRules
  + dam:Asset
    + properties
      + status
        - name: status
  + dam:cfVariationNode
    + properties
      + status
        - name: status
        - analyzed: true
```

If the analyzed property is not explicitly set, its default value is false. 

### Tags property {#tags-property}

* **Key**: IndexHasValidTagsProperty
* **Type**: `Code Smell`
* **Severity**: Minor
* **Since**: Version 2023.1.0

For specific indexes, ensure you retain the tags property and its current values. While adding new values to the tags property is permissible, deleting any existing ones (or the property altogether) can lead to unexpected results.

### Index definition nodes must not be deployed in UI content package {#oakpal-ui-content-package}

* **Key**: IndexNotUnderUIContent
* **Type**: Improvement
* **Severity**: Minor
* **Since**: Version 2024.6.0

AEM Cloud Service prohibits custom search index definitions (nodes of type `oak:QueryIndexDefinition`) from being deployed in the UI Content package.

>[!WARNING]
>
>YYou should resolve this issue as soon as possible, as it may cause pipeline failures beginning with the [Cloud Manager August 2024 release](/help/implementing/cloud-manager/release-notes/current.md).

### Custom full-text index definition of type damAssetLucene must be correctly prefixed with 'damAssetLucene' {#oakpal-dam-asset-lucene}

* **Key**: CustomFulltextIndexesOfTheDamAssetCheck
* **Type**: Improvemen
* **Severity**: Minor
* **Since**: Version 2024.6.0

AEM Cloud Service prohibits custom full-text index definitions of type `damAssetLucene` from being prefixed with anything other than `damAssetLucene`.

>[!WARNING]
>
>Resolve this issue as soon as possible, as it may cause pipeline failures beginning with the [Cloud Manager August 2024 release](/help/implementing/cloud-manager/release-notes/current.md).

### Index definition nodes must not contain properties with the same name {#oakpal-index-property-name}

* **Key**: DuplicateNameProperty
* **Type**: Improvement
* **Severity**: Minor
* **Since**: Version 2024.6.0

AEM Cloud Service prohibits custom search index definitions (that is, nodes of type `oak:QueryIndexDefinition`) from containing properties with the same name

>[!WARNING]
>
>Resolve this issue as soon as possible, as it may cause pipeline failures beginning with the [Cloud Manager August 2024 release](/help/implementing/cloud-manager/release-notes/current.md).

### Customizing of certain out-of-the-box index definitions is prohibited {#oakpal-customizing-ootb-index}

* **Key**: RestrictIndexCustomization
* **Type**: Improvement
* **Severity**: Minor
* **Since**: Version 2024.6.0

AEM Cloud Service prohibits unauthorized modifications of the following OOTB indexes:

* `nodetypeLucene`
* `slingResourceResolver`
* `socialLucene`
* `appsLibsLucene`
* `authorizables`
* `pathReference`

>[!WARNING]
>
>Resolve this issue as soon as possible, as it may cause pipeline failures beginning with the [Cloud Manager August 2024 release](/help/implementing/cloud-manager/release-notes/current.md).

### Configuration of the tokenizers in analyzers should be created with the name 'tokenizer' {#oakpal-tokenizer}

* **Key**: AnalyzerTokenizerConfigCheck
* **Type**: Improvement
* **Severity**: Minor
* **Since**: Version 2024.6.0

AEM Cloud Service prohibits creation of tokenizers with incorrect names in analyzers. Tokenizers should always be defined as `tokenizer`.

>[!WARNING]
>
>Resolve this issue as soon as possible, as it may cause pipeline failures beginning with the [Cloud Manager August 2024 release](/help/implementing/cloud-manager/release-notes/current.md).

### Configuration of indexing definitions should not contain spaces {#oakpal-indexing-definitions-spaces}

* **Key**: PathSpacesCheck
* **Type**: Improvement
* **Severity**: Minor
* **Since**: Version 2024.7.0

AEM Cloud Service prohibits the creation of indexing definitions that contain properties with spaces.
