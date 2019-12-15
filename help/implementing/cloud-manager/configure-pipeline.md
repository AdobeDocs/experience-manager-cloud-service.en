---
title: Configure CI/CD Pipeline - Cloud Services
seo-title: Configure CI/CD Pipeline - Cloud Services
description: Configure CI/CD Pipeline - Cloud Services
seo-description: Configure CI/CD Pipeline - Cloud Services 
---

# Configure CI-CD Pipeline {#configure-ci-cd-pipeline} 


In order to support the Cloud Services architecture, a new step has been introduced called **Build Images**. This step occurs after the code quality step but before stage deployment. This step has a log file from the process used to build images.

This process is responsible for transforming the content and dispatcher packages produced by the build step into Docker images and Kubernetes configuration. 

Part of this step is also to execute the Dispatcher configurations validator. Refer to [Dispatcher in Cloud](/help/implementing/dispatcher/dispatcher-cloud.md) for more details.