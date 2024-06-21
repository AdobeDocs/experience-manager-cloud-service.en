---
title: GraphQL Persisted Queries - enabling caching in the Dispatcher
description: The Dispatcher is a caching and security layer in front of Adobe Experience Manager Publish environments. You can enable caching for Persisted Queries in AEM Headless.
feature: "Headless, Dispatcher, GraphQL API"
exl-id: 30a97e56-6699-41c4-a4eb-fc6236667f8f
role: "Admin, Developer"
---
# GraphQL Persisted Queries - enabling caching in the Dispatcher {#graphql-persisted-queries-enabling-caching-dispatcher}

>[!CAUTION]
>
>If caching in the Dispatcher is enabled then the [CORS Filter](/help/headless/deployment/cross-origin-resource-sharing.md) is not needed, and so that section can be ignored.

Caching of persisted queries is not enabled by default in the Dispatcher. Default enablement is not possible as customers using CORS (Cross-Origin Resource Sharing) with multiple origins need to review, and possibly update, their Dispatcher configuration.

>[!NOTE]
>
>The Dispatcher does not cache the `Vary` header. 
>
>Caching of other CORS-related headers can be enabled in the Dispatcher, but might be insufficient when there are multiple CORS origins.

>[!NOTE]
>
>For detailed documentation about the Dispatcher, see the [Dispatcher Guide](https://experienceleague.adobe.com/docs/experience-manager-dispatcher/using/dispatcher.html).

## Enable caching of persisted queries {#enable-caching-persisted-queries}

To enable the caching of persisted queries, define the Dispatcher variable `CACHE_GRAPHQL_PERSISTED_QUERIES`:

1. Add the variable to the Dispatcher file `global.vars`:

   ```xml
   Define CACHE_GRAPHQL_PERSISTED_QUERIES
   ```

>[!NOTE]
>
>To achieve individual `ETag` header computation on the cached persisted queries (for *each* response that is unique) the `FileETag Digest` setting has to be used in the dispatcher configuration virtual host configuration (if it does not already exist):
>
>```xml
><Directory />    
>  ...    
>  FileETag Digest
></Directory> 
>```

>[!NOTE]
>
>To conform to the [Dispatcher's requirements for documents that can be cached](https://experienceleague.adobe.com/docs/experience-manager-dispatcher/using/troubleshooting/dispatcher-faq.html#how-does-the-dispatcher-return-documents%3F), the Dispatcher adds the suffix `.json` to all persisted query URLS, so that the result can be cached. 
>
>This suffix is added by a rewrite rule, once persisted query caching is enabled.

## CORS configuration in the Dispatcher {#cors-configuration-in-dispatcher}

Customers using CORS requests, might need to review and update their CORS configuration in the Dispatcher.

* The `Origin` header must not be passed to AEM publish via the Dispatcher:
  * Check the `clientheaders.any` file.
* Instead, CORS requests must be evaluated for allowed origins at the Dispatcher level. This approach also ensures that CORS related headers are set correctly, in one place, in all cases.
  * Such a configuration should be added to the `vhost` file. An example configuration is given below; for simplicity, only the CORS-related part has been provided. You can adapt it for your specific use cases.  

  ```xml
  <VirtualHost *:80>
     ServerName "publish"

     # ...

     <IfModule mod_headers.c>
         Header add X-Vhost "publish"

          ################## Start of the CORS specific configuration ##################

          SetEnvIfExpr "req_novary('Origin') == ''"  CORSType=none CORSProcessing=false
          SetEnvIfExpr "req_novary('Origin') != ''"  CORSType=cors CORSProcessing=true CORSTrusted=false

          SetEnvIfExpr "req_novary('Access-Control-Request-Method') == '' && %{REQUEST_METHOD} == 'OPTIONS' && req_novary('Origin') != ''  " CORSType=invalidpreflight CORSProcessing=false
          SetEnvIfExpr "req_novary('Access-Control-Request-Method') != '' && %{REQUEST_METHOD} == 'OPTIONS' && req_novary('Origin') != ''  " CORSType=preflight CORSProcessing=true CORSTrusted=false
          SetEnvIfExpr "req_novary('Origin') -strcmatch 'https://%{HTTP_HOST}*'"  CORSType=samedomain CORSProcessing=false

          # For requests that require CORS processing, check if the Origin can be trusted
          SetEnvIfExpr "%{HTTP_HOST} =~ /(.*)/ " ParsedHost=$1

          ################## Adapt the regex to match CORS origin for your environment
          SetEnvIfExpr "env('CORSProcessing') == 'true' && req_novary('Origin') =~ m#(https://.*.your-domain.tld(:\d+)?$)#" CORSTrusted=true

          # Extract the Origin header 
          SetEnvIfNoCase ^Origin$ ^https://(.*)$ CORSTrustedOrigin=https://$1

          # Flush If already set
          Header unset Access-Control-Allow-Origin
          Header unset Access-Control-Allow-Credentials

          # Trusted
          Header always set Access-Control-Allow-Credentials "true" "expr=reqenv('CORSTrusted') == 'true'"
          Header always set Access-Control-Allow-Origin "%{CORSTrustedOrigin}e" "expr=reqenv('CORSTrusted') == 'true'"
          Header always set Access-Control-Allow-Methods "GET" "expr=reqenv('CORSTrusted') == 'true'"
          Header always set Access-Control-Max-Age 1800 "expr=reqenv('CORSTrusted') == 'true'"
          Header always set Access-Control-Allow-Headers "Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers" "expr=reqenv('CORSTrusted') == 'true'"

          # Non-CORS or Not Trusted
          Header unset Access-Control-Allow-Credentials "expr=reqenv('CORSProcessing') == 'false' || reqenv('CORSTrusted') == 'false'"
          Header unset Access-Control-Allow-Origin "expr=reqenv('CORSProcessing') == 'false' || reqenv('CORSTrusted') == 'false'"
          Header unset Access-Control-Allow-Methods "expr=reqenv('CORSProcessing') == 'false' || reqenv('CORSTrusted') == 'false'"
          Header unset Access-Control-Max-Age "expr=reqenv('CORSProcessing') == 'false' || reqenv('CORSTrusted') == 'false'"

          # Always vary on origin, even if its not there.
          Header merge Vary Origin

          # CORS - send 204 for CORS requests which are not trusted
          RewriteCond expr "reqenv('CORSProcessing') == 'true' && reqenv('CORSTrusted') == 'false'"
          RewriteRule "^(.*)" - [R=204,L]

          ################## End of the CORS specific configuration ##################

     </IfModule>

     <Directory />

         # ...

     </Directory>

     # ...

  </VirtualHost>
  ```
