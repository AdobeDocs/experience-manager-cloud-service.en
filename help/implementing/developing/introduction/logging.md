---
title: Logging
description: Learn how to configure global parameters for the central logging service, specific settings for the individual services or how to request data logging.
---

# Logging{#logging}

AEM as a Cloud Service offers you the possibility to configure:

* global parameters for the central logging service
* request data logging; a specialized logging configuration for request information
* specific settings for the individual services; for example, an individual log file and format for the log messages

For local development, logs entries are written to local files in the `/crx-quickstart/logs` folder.

On Cloud environments, developers can download logs through Cloud Manager or use a command line tool to tail the logs.

>[!NOTE]
>
>Logging in AEM as a Cloud Service is based on Sling principles. See [Sling Logging](https://sling.apache.org/site/logging.html) for further information.

<!-- ## Global Logging {#global-logging}

[Apache Sling Logging Configuration](https://sling.apache.org/documentation/development/logging.html#user-configuration---osgi-based) is used to configure the root logger. This defines the global settings for logging in AEM as a Cloud Service:

* the logging level
* the location of the central log file
* the number of versions to be kept
* version rotation; either maximum size or a time interval
* the format to be used when writing the log messages
-->

## Loggers and Writers for Individual Services {#loggers-and-writers-for-individual-services}

In addition to the global logging settings, AEM as a Cloud Service allows you to configure specific settings for an individual service:

* the specific logging level
* the logger (the OSGi service supplying the log messages)

This allows you to channel log messages for a single service into a separate file. This can be particularly useful during development or testing; for example, when you need an increased log level for a specific service.

AEM as a Cloud Service uses the following to write log messages to file:

1. An **OSGi service** (logger) writes a log message.
1. A **Logging Logger** takes this message and formats it according to your specification.
1. A **Logging Writer** writes all these messages to the physical file that you have defined.

These elements are linked by the following parameters for the appropriate elements:

* **Logger (Logging Logger)**

  Define the service(s) generating the messages.

* **Log File (Logging Logger)**

  Define the physical file for storing the log messages.

  This is used to link a Logging Logger with a Logging Writer. The value must be identical to the same parameter in the Logging Writer configuration for the connection to be made.

* **Log File (Logging Writer)**

  Define the physical file that the log messages will be written to.

  This must be identical to the same parameter in the Logging Writer configuration, or the match will not be made. If there is no match then an implicit Writer will be created with default configuration (daily log rotation).

### Standard Loggers and Writers {#standard-loggers-and-writers}

Certain Loggers and Writers are included in a standard AEM as a Cloud Service installation.

The first is a special case as it controls both the `request.log` and `access.log` files:

* The Logger:

    * Apache Sling Customizable Request Data Logger

      (org.apache.sling.engine.impl.log.RequestLoggerService)

    * Write messages about request content to `request.log`.

* Links to:

    * Apache Sling Request Logger

      (org.apache.sling.engine.impl.log.RequestLogger)

    * Writes the messages to either `request.log` or `access.log`.

These can be customized if required, though the standard configuration is suitable for most installations.

The other pairs follow the standard configuration:

* The Logger:

    * Apache Sling Logging Logger Configuration

      (org.apache.sling.commons.log.LogManager.factory.config)

    * Writes `Information` messages to `logs/error.log`.

* Links to the Writer:

    * Apache Sling Logging Writer Configuration

      (org.apache.sling.commons.log.LogManager.factory.writer)

* The Logger:

    * Apache Sling Logging Logger Configuration
      (org.apache.sling.commons.log.LogManager.factory.config.649d51b7-6425-45c9-81e6-2697a03d6be7)

    * Writes `Warning` messages to `../logs/error.log` for the service `org.apache.pdfbox`.

* Does not link to a specific Writer so will create and use an implicit Writer with default configuration (daily log rotation).

## Setting the Log Level {#setting-the-log-level}

To change the log levels for Cloud environments, the Sling Logging OSGI configuration should be modified, followed by a full redeployment. Since this is not instantaneous, be cautious about enabling verbose logs on production environments which receive a lot of traffic. In the future, it's possible that there will be mechanisms to more quickly change the log level.

>[!NOTE]
>
> In order to perform the configuration changes listed below, you need to create them on a local development environment and then push them to an AEM as a Cloud Service instance. For more information on how to do this, see [Deploying to AEM as a Cloud Service](/help/implementing/deploying/overview.md).

### Activating the DEBUG Log Level {#activating-the-debug-log-level}

>[!WARNING]
>
> Activating the DEBUG log level globally will generate a large amount of information which will be difficult to sift through. It is recommended you enable it only for the services that require debugging. For more information, see [Loggers and Writers for Individual Services](logging.md#loggers-and-writers-for-individual-services).

The default log level is INFO, that is, DEBUG messages are not logged.
To activate DEBUG log level, set the

``` /libs/sling/config/org.apache.sling.commons.log.LogManager/org.apache.sling.commons.log.level ```

property to debug. Do not leave the log at the DEBUG log level longer than necessary, as it generates a lot of logs.
A line in the debug file usually starts with DEBUG, and then provides the log level, the installer action and the log message. For example:

``` DEBUG 3 WebApp Panel: WebApp successfully deployed ```

The log levels are as follows:

| 0  | Fatal error   | The action has failed, and the installer cannot proceed.   |
|---|---|---|
| 1  | Error  | The action has failed. The installation proceeds, but a part of CRX was not installed correctly and will not work.   |
| 2  | Warning  | The action has succeeded but encountered problems. CRX may or may not work correctly. |
| 3  |  Information | The action has succeeded.   |

### Creating Your Own Loggers and Writers {#creating-your-own-loggers-and-writers}

You can define your own Logger / Writer pair:

1. Create a new instance of the Factory Configuration [Apache Sling Logging Logger Configuration](https://sling.apache.org/documentation/development/logging.html#user-configuration---osgi-based).

    1. Specify the Log File.
    1. Specify the Logger.

<!-- 1. Create a new instance of the Factory Configuration [Apache Sling Logging Writer Configuration](https://sling.apache.org/documentation/development/logging.html#user-configuration---osgi-based).

    1. Specify the Log File - this must match that specified for the Logger.
    1. Configure the other parameters as required. -->

### Configure Logging {#configure-logging}

>[!NOTE]
>
>When working with Adobe Experience Manager there are several methods of managing the configuration settings for such services.

In certain circumstances you may want to create a custom log file with a different log level. You can do this in the repository by:

1. If not already existing, create a new configuration folder ( `sling:Folder`) for your project `/apps/<*project-name*>/config`.
1. Under `/apps/<*project-name*>/config`, create a node for the new Apache Sling Logging Logger Configuration:

    * Name: `org.apache.sling.commons.log.LogManager.factory.config-<*identifier*>` (as this is a Logger)

      Where `<*identifier*>` is replaced by free text that you (must) enter to identify the instance (you cannot omit this information).

      For example, `org.apache.sling.commons.log.LogManager.factory.config-MINE`

    * Type: `sling:OsgiConfig`

   >[!NOTE]
   >
   >Although not a technical requirement, it is advisable to make `<*identifier*>` unique.

<!-- 1. Set the following properties on this node:

    * Name: `org.apache.sling.commons.log.file`

      Type: String

      Value: specify the Log File; for example, `logs/myLogFile.log`

    * Name: `org.apache.sling.commons.log.names`

      Type: String[] (String + Multi)

      Value: specify the OSGi services for which the Logger is to log messages; for example, all of the following:

        * `org.apache.sling`
        * `org.apache.felix`
        * `com.day`

    * Name: `org.apache.sling.commons.log.level`

      Type: String

      Value: specify the log level required ( `debug`, `info`, `warn` or `error`); for example `debug`

    * Configure the other parameters as required:

        * Name: `org.apache.sling.commons.log.pattern`

          Type: `String`

          Value: specify the pattern of the log message as required; for example,

          `{0,date,dd.MM.yyyy HH:mm:ss.SSS} *{4}* [{2}] {3} {5}`

   >[!NOTE]
   >
   >`org.apache.sling.commons.log.pattern` supports up to six arguments.

   >
   >
   >{0} The timestamp of type `java.util.Date`
   >{1} the log marker
   >{2} the name of the current thread
   >{3} the name of the logger
   >{4} the log level
   >{5} the log message

   >
   >
   >If the log call includes a `Throwable` the stacktrace is appended to the message.

   >[!CAUTION]
   >
   >org.apache.sling.commons.log.names must have a value.

   >[!NOTE]
   >
   >Log writer paths are relative to the `crx-quickstart` location.
   >
   >
   >Therefore, a log file specified as:
   >
   >
   >`logs/thelog.log`

   >
   >
   >writes to:
   >
   >
   >`` ` ` `<*cq-installation-dir*>/``crx-quickstart/logs/thelog.log`.
   >
   >
   >And a log file specified as:
   >
   >
   >`../logs/thelog.log`

   >
   >
   >writes to a directory:
   >
   >
   >` <*cq-installation-dir*>/logs/`
   >``(i.e. next to ` `<*cq-installation-dir*>/`crx-quickstart/`)
 --> 

<!-- open question: see if we need to leave the above warning note in place, but adjust it so that it doesn't mention filenames --> 

<!-- 1. This step is only necessary when a new Writer is required (i.e. with a configuration that is different to the default Writer).

   >[!CAUTION]
   >
   >A new Logging Writer Configuration is only required when the existing default is not suitable.

   >
   >
   >If no explicit Writer is configured the system will automatically generate an implicit Writer based on the default.

   Under `/apps/<*project-name*>/config`, create a node for the new `Apache Sling Logging Writer` Configuration:

    * Name: `org.apache.sling.commons.log.LogManager.factory.writer-<*identifier*>` (as this is a Writer)

      As with the Logger, `<*identifier*>` is replaced by free text that you (must) enter to identify the instance (you cannot omit this information). For example, `org.apache.sling.commons.log.LogManager.factory.writer-MINE`

    * Type: `sling:OsgiConfig`

   >[!NOTE]
   >
   >Although not a technical requirement, it is advisable to make `<*identifier*>` unique.

   Set the following properties on this node:

    * Name: `org.apache.sling.commons.log.file`

      Type: `String`

      Value: specify the Log File so that it matches the file specified in the Logger;

      for this example, `../logs/myLogFile.log`.

    * Configure the other parameters as required:

        * Name: `org.apache.sling.commons.log.file.number`

          Type: `Long`

          Value: specify the number of log files you want kept; for example, `5`

        * Name: `org.apache.sling.commons.log.file.size`

          Type: `String`

          Value: specify as required to control file rotation by size/date; for example, `'.'yyyy-MM-dd`

   >[!NOTE]
   >
   >`org.apache.sling.commons.log.file.size` controls the rotation of the log file by setting either:
   >
   >* a maximum file size
   >* a time/date schedule
   >
   >to indicate when a new file will be created (and the existing file renamed according to the name pattern).
   >
   >* A size limit can be specified with a number. If no size indicator is given, then this is taken as the number of bytes, or you can add one of the size indicators - `KB`, `MB`, or `GB` (case is ignored).
   >* A time/date schedule can be specified as a `java.util.SimpleDateFormat` pattern. This defines the time period after which the file will be rotated; also the suffix appended to the rotated file (for identification).
   >
   >The default is '.'yyyy-MM-dd (for daily log rotation).
   >
   >So for example, at midnight of January 20th 2010 (or when the first log message after this occurs to be precise), ../logs/error.log will be renamed to ../logs/error.log.2010-01-20. Logging for the 21st of January will be output to (a new and empty) ../logs/error.log until it is rolled over at the next change of day.
   >
   >      | `'.'yyyy-MM` |Rotation at the beginning of each month |
   >      |---|---|
   >      | `'.'yyyy-ww` |Rotation at the first day of each week (depends on the locale). |
   >      | `'.'yyyy-MM-dd` |Rotation at midnight each day. |
   >      | `'.'yyyy-MM-dd-a` |Rotation at midnight and midday of each day. |
   >      | `'.'yyyy-MM-dd-HH` |Rotation at the top of every hour. |
   >      | `'.'yyyy-MM-dd-HH-mm` |Rotation at the beginning of every minute. |
   >
   >      Note: When specifying a time/date:
   >      1. You should "escape" literal text within a pair of single quotes (' ');
   >      this is to avoid certain characters being interpreted as pattern letters.
   >      1. Only use characters allowed for a valid file name anywhere in the option.

1. Read your new log file with your chosen tool.

   The log file created by this example will be `../crx-quickstart/logs/myLogFile.log`. -->

The Felix Console also provides information about Sling Log Support at `../system/console/slinglog`; for example `https://localhost:4502/system/console/slinglog`.draf