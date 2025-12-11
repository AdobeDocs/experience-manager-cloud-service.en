---
title: Using MCP with AEM as a Cloud Service
description: Learn how to use the Model Context Protocol with AEM as a Cloud Service
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
---

# Using MCP with AEM as a Cloud Service {#using-mcp-with-aem-as-a-cloud-service}

## Introduction {#introduction}

Many AEM teams now work in IDEs and chat-based applications such as Cursor, ChatGPT, Anthropic Claude, and Microsoft Copilot Studio. These applications support the Model Context Protocol (MCP), which allows applications to expose back-end tools to large language models (LLMs) in a standardized way.

With AEM's MCP integration, different personas can collaborate around the same content:

* **Developers** can orchestrate content operations and workflows from their IDE or chat application
* **Practitioners** and content architects can manage sites, content fragments, and assets with AI assistance while staying within AEM's existing permission model.

This article explains what AEM's MCP functionality provides, which MCP applications are supported, how to configure it, and how to use it in practice.

## Why MCP is Useful for AEM Customers {#why-mcp-is-useful-for-aem-customers}

Modern IDE and chat applications use MCP as a way for an LLM to call tools exposed behind MCP servers. Instead of writing code against low-level API specifications, customers can describe their intent in natural language (*"update the hero banner for this campaign across all pages"*) and let the LLM invoke the appropriate MCP tools, which in turn interact with AEM's APIs.

Key benefits include:

* **Natural-language interaction instead of API plumbing**
MCP tools describe what operations are available and how to call them. The LLM uses these schemas to decide which tools to invoke and with which parameters.
* **Consistent experience across applications**
The same AEM MCP tools can be used from multiple MCP-compatible applications, allowing teams to work where they are most productive while calling the same underlying AEM capabilities.
* **Security and governance preserved**
Requests to AEM MCP tools run under the authenticated user's identity, and each tool enforces the user's existing AEM permissions. AI-assisted operations follow the same access rules as manual work in AEM.

## MCP Servers Provided by AEM {#mcp-servers-provided-by-aem}

AEM exposes MCP servers as HTTP endpoints. The endpoints listed below are relative to:

`https://mcp.adobeaemcloud.com/adobe/mcp/`

### MCP Servers {#mcp-servers}

| **MCP Server** | **Endpoint**  | **Description** |
|---|---|---|
| **Content Tools**  | `/content`  | All low-level content operations, including create, read, update, and delete (CRUD) for pages and fragments.  |
| **Content Tools (read-only)**  | `/content-readonly`  | Read-only content operations (Get, List/Search) for pages, fragments, and assets.  |

The specific tools exposed by each MCP server may evolve over time. In practice, you can ask your MCP-enabled application to discover tools via a prompt such as:

*"List all AEM MCP tools available from this server and describe what they do."*

The MCP client will use the MCP protocol to retrieve the tool list and schemas, which the LLM can then use.

## Supported MCP Applications {#supported-mcp-applications}

AEM's MCP servers are designed to work with a defined set of MCP-compatible applications. The following applications are supported:

* Anthropic Claude
* Cursor
* OpenAI ChatGPT
* Microsoft Copilot Studio

Each application provides its own configuration experience, but the high-level steps are similar.

## Setup Overview {#setup-overview}

Configuring MCP for AEM involves three main parts:

1. **A one-time configuration in AEM by an administrator**, allowing specific MCP client applications to access AEM's MCP servers
1. **Configuration in each MCP client application** so that the application knows how to connect to the AEM MCP servers and perform OAuth login
1. **Select the MCP Server** before starting to prompt, so that the MCP client knows to use it.

### AEM Configuration {#aem-configuration}

This step is performed once by an AEM administrator.

Your AEM administrator must add the client IDs associated with each supported MCP application to an API configuration file (`api.yaml`) and deploy it using the AEM configuration pipeline. This allows the administrator to make a conscious decision about whether members of the organization can access AEM's MCP servers from those applications.

Find an example `api.yaml` below:

```yaml
kind: "API"
version: "1"
data:
  allowedClientIDs:
    author:
      - "aem-oauth-chatgpt"
      - "aem-oauth-claude"
      - "aem-oauth-mscopilot"
      - "aem-oauth-cursor"
```

After this configuration is deployed through the AEM configuration pipeline, the listed MCP client applications can request auth tokens and call AEM MCP tools for the author tier.

### MCP Client Application Configuration {#mcp-client-application-configuration}

This step is performed by each user (or by an administrator of the MCP client application, where supported). Configuration details vary slightly between applications. MCP clients are evolving rapidly, and support for remote MCP servers is being actively developed. You may need to enable Developer Mode to access the functionality for adding remote servers, but the general process is:

1. Add the AEM MCP server URL(s)
   * Configure the MCP endpoint(s) from the table above. For example:`https://mcp.adobeaemcloud.com/adobe/mcp/content-readonly`
1. Trigger the connection
   * Save or activate the configuration so the MCP client application attempts to connect to the AEM MCP server
1. Sign in with Adobe ID
   * When prompted, complete the Adobe login flow so the application can obtain OAuth tokens tied to your Adobe ID
1. Verify discovered tools
   * Once authenticated, the application will discover MCP tools from the server. You can then start prompting the LLM to perform AEM operations.

Below are examples of how this looks in each supported application at a high level.

**ChatGPT**

![Configure ChatGPT Step 1](assets/chatgpt-1.png)

![Configure ChatGPT Step 2](assets/chatgpt-2.png)

![Configure ChatGPT Step 3](assets/chatgpt-3.png)

![Configure ChatGPT Step 4](assets/chatgpt-4.png)

![Configure ChatGPT Step 5](assets/chatgpt-5.png)

![Configure ChatGPT Step 6](assets/chatgpt-6.png)

![Configure ChatGPT Step 7](assets/chatgpt-7.png)

* Add the AEM MCP server URL(s) in the area where MCP connections or tools are configured
* Trigger the connection and sign in with your Adobe ID when redirected
* In a chat, reference the configured AEM tools in your prompts, for example:

   *"Using the configured AEM MCP tools, list all sites in our author environment."*

**Claude**

![Configure Claude Step 1](assets/claude-1.png)

![Configure Claude Step 2](assets/claude-2.png)

![Configure Claude Step 3](assets/claude-3.png)

![Configure Claude Step 4](assets/claude-4.png)

![Configure Claude Step 5](assets/claude-5.png)

![Configure Claude Step 6](assets/claude-6.png)

![Configure Claude Step 7](assets/claude-7.png)

* In Claude's MCP configuration, register the AEM MCP server URL(s)
* Complete the Adobe login flow
* Optionally, enable auto-confirm for certain tools in the configuration area. This is recommended for search or read-only operations.
* Ensure the MCP server is selected before starting your conversation
* Ask Claude to perform AEM-related tasks; Claude will select AEM tools exposed by the MCP server based on your prompt.

**Cursor**

![Configure Cursor Step 1](assets/cursor-1.png)

![Configure Cursor Step 2](assets/cursor-2.png)

![Configure Cursor Step 3](assets/cursor-3.png)

![Configure Cursor Step 4](assets/cursor-4.png)

![Configure Cursor Step 5](assets/cursor-5.png)

* In Cursor's MCP settings, create a new MCP server entry with the AEM MCP URL(s)
* Authenticate with your Adobe ID when prompted
* Optionally, enable or disable individual tools by clicking on the tool names. All tools are enabled by default.
* Use Cursor's editor or chat to invoke AEM tools as part of development or content workflows.

**Microsoft Copilot Studio**

![Configure Copilot Step 1](assets/copilot-1.png)

![Configure Copilot Step 2](assets/copilot-2.png)

![Configure Copilot Step 3](assets/copilot-3.png)

![Configure Copilot Step 4](assets/copilot-4.png)

![Configure Copilot Step 5](assets/copilot-5.png)

![Configure Copilot Step 6](assets/copilot-6.png)

![Configure Copilot Step 7](assets/copilot-7.png)

![Configure Copilot Step 8](assets/copilot-8.png)

![Configure Copilot Step 9](assets/copilot-9.png)

![Configure Copilot Step 10](assets/copilot-10.png)

* Create a new agent
* Navigate to the tool section and click **Add tool**
* Select an existing tool or create a new one
* Configure a new MCP tool pointing to the AEM MCP server URL(s)
* Establish a connection, which can be shared or dedicated between agents
* Sign in using your Adobe ID when redirected
* Optionally, enable auto-confirm mode or require end-user confirmation for all tool interactions
* When testing your agent, open the connection manager first to assign a connection to your session, then press **Retry**.

## Authentication {#authentication}

The Adobe-hosted MCP servers implement OAuth and are integrated with Adobe's identity system.

* When an MCP client application connects to an AEM MCP server, users see an Adobe login dialog and authenticate with their **Adobe ID**
* After successful login, the MCP server issues tokens that the application uses for subsequent tool calls
* MCP tools respect the user's AEM permissions. A user without permission to modify a content fragment in AEM will not be able to modify it via MCP either.

This ensures that AI-assisted operations comply with your existing AEM security and governance model.

## Using MCP with AEM {#using-mcp-with-aem}

Once AEM and your MCP client applications are configured, you can work in your application of choice and prompt the LLM to perform AEM operations. The LLM reads the MCP tool schemas, chooses which tools to call, and sequences them as needed to fulfill your request.

>[!IMPORTANT]
>
>For best results, especially with prompts that contain multiple steps or target different content types such as images and text, enable a thinking model or select the Thinking option in your MCP client rather than relying on Auto mode.

### Example Usecases {#example-usecases}

Some representative scenarios include:

* **Environment discovery**
  * List environments and licenses to decide where to run a workflow.

* **Sites management**
  * List sites
  * Create, read, update, and delete pages and page content.

* **Content Fragment management**
  * Search for content fragments
  * Create new fragments
  * Update existing fragments when campaign messaging changes.

* **Assets management**
  * Import assets
  * Find existing assets
  * Publish assets.

### Example Workflows {#example-workflows}

The following examples illustrate how an LLM might chain MCP tools together.

1. **Working with a content fragment referenced by a page**
   * **Get page content** – Call a tool such as `get-aem-page-content` to retrieve the page and locate the `fragmentPath` property.
   * **Resolve the fragment path** – Use `resolve_fragment_path` to convert the path to a UUID.
   * **Fetch fragment data** – Call `get_fragment` to retrieve the current fields.
   * **Update the fragment** – Call `patch_fragment` to apply changes to the fragment content.
1. **Creating new content based on a model**
   * **Discover models** – Use `list_models` to see which content fragment models are available.
   * **Inspect a model** – Use `get_model` to understand the model's field schema.
   * **Create content** – Use `create_fragment` to create a new fragment with values derived from your prompt.
1. **Safely updating existing content**
   * **Read current data** – Use `get_fragment` to retrieve the existing data and an ETag.
   * **Apply a JSON Patch** – Use `patch_fragment` with the ETag and a JSON Patch document to update the fragment, supporting optimistic concurrency.

From the user's perspective, these workflows can be initiated with prompts such as:

*"Create a new content fragment for the spring campaign based on our hero banner model and fill in its fields from this brief."*

The LLM chooses and coordinates the necessary MCP tools automatically.

## Expectation Management {#expectation-management}

When working with LLMs through MCP, keep the following in mind:

* **Highly capable but not infallible**
LLMs can accomplish complex tasks but are prone to occasional errors. The same prompt may yield slightly different results or presentations without an obvious reason. Always review outputs before applying changes to production content.

* **Evolving capabilities**
LLM models are continuously improving. Over time, they become smarter at discovering new ways to combine MCP tools to achieve your goals. A task that required multiple prompts today may work seamlessly with a single prompt tomorrow.

* **Human oversight is essential**
Think of the LLM as a knowledgeable assistant that needs supervision. It has broad knowledge and can devise creative solutions, but it benefits from your guidance and review. Verify results, especially for critical operations, and provide feedback when the output does not match your expectations.

## Limitations {#limitations}

AEM's MCP servers are currently intended to be configured in ChatGPT, Claude, Cursor, and Microsoft Copilot Studio.
