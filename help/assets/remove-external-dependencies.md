---
title: Remove external dependencies for existing installations
description: Remove external dependencies for existing installations
feature: Integrations
exl-id: 5b28ce97-2719-47b8-a386-77d4aaddbe81
---
# Remove external dependencies for existing installations {#remove-external-depedencies}

Adobe recommends you to execute configuration steps for existing enhanced connector installations for Workfront to remove the dependencies on Hoodoo distribution points.

>[!NOTE]
>
>Execute the configuration steps only if you have installed the enhanced connector for Workfront before March 2022. There are no dependencies on Hoodoo distribution points for new enhanced connector installations for Workfront starting March 2022.

To remove the external dependencies:

1. Remove the following Hoodoo repository configuration from the parent `pom.xml`:
   
    ```XML
      <repository>
         <id>hoodoo-maven</id>
         <name>Hoodoo Repository</name>
         <url>https://gitlab.com/api/v4/projects/12715200/packages/maven</url>
      </repository>
      
    ```

1. Remove the following server configuration from the `settings.xml` file, available at `./cloudmanager/maven/settings.xml`:

   ```XML
         <server>
            <id>hoodoo-maven</id>
            <configuration>
               <httpHeaders>
                     <property>
                        <name>Deploy-Token</name>
                        <value>xxxxxxxxxxxxxxxx</value>
                     </property>
               </httpHeaders>
            </configuration>
         </server>
   ```

1. Execute the [new installation steps](workfront-connector-install.md).
