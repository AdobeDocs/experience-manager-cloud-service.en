---
title: CI-CD Pipelines
description: CI-CD Pipelines
index: no
---

# Cloud Manager CI-CD Pipelines {#intro-cicd}

## Introduction {#introduction}

A CI/CD pipeline in Cloud Manager can be triggered by some sort of event, such as a pull request from a source code repository, that is, a code change, or some sort of regular schedule to match a release cadence.

>[!NOTE]
>To configure your pipeline, you must:
>* define the trigger that will start the pipeline
>* define the parameters controlling the production deployment
>* configure the performance test parameters

In Cloud Manager, there are two types of Pipeline:

* [Production Pipeline](#prod-pipeline)
* [Non-Production Pipeline](#non-prod-pipeline)

## Production Pipeline {#prod-pipeline}

A Production pipelines is a purpose built pipeline that includes a series of orchestrated steps to take source code all the way into production. The steps include building, packaging, testing, validating, and deploying into all Stage environment first. Needless to say, a Production Pipeline can only be added once a production and stage environment set is created.

Refer to Configuring Production Pipeline for more details.


## Non-Production Pipeline {#non-prod-pipeline}

A Non-Production Pipeline aims to run code-quality scans or to deploy source code into a development environment. 

Refer to Non-Production & Code Quality Only Pipelines for more details.

## 
