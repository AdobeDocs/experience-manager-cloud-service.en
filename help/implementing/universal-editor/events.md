---
title: Universal Editor Events
description: Learn about the different events that the Universal Editor sends that you can use to react to content or UI changes in your remote app.
exl-id: c9f7c284-f378-4725-a4e6-e4799f0f8175
feature: Developing
role: Admin, Architect, Developer
---
# Universal Editor Events {#events}

Learn about the different events that the Universal Editor sends that you can use to react to content or UI changes in your remote app.

## Introduction {#introduction}

Applications can have different requirements for page or component updates. Therefore, the Universal Editor sends defined events to remote applications. In case the remote application has no custom event listener for the sent event, a [fallback event listener](#fallback-listeners) provided by the `universal-editor-cors` package is executed.

All events are invoked on the affected DOM element of the remote page. Events bubble up to the `BODY` element where the default event listener provided by the `universal-editor-cors` package is registered. There are events for the content and events for the UI.

All events follow a naming convention.

* `aue:<content-or-ui>-<event-name>`

For example, `aue:content-update` and `aue:ui-select`

Events include the request's and response's payload and are triggered once the corresponding call is successful. For further details about calls and examples of their payloads, please see the document [Universal Editor Calls.](/help/implementing/universal-editor/calls.md)

## Content Update Events {#content-events}

### aue:content-add {#content-add}

The `aue:content-add` event is triggered when a new component is added to a container.

The payload is content from the Universal Editor service, with fallback content from the component definition.

```json
{
    details: {
        request: request payload;   // what is sent to the service
        response: {                 // what is returned by the service
            resource: string;       // newly created content resource
            updates: [{
                resource: string;   // resource to update
                type: string;       // type of instrumentation
                content?: string;   // content to replace
            }]
        }
    }
}
```

### aue:content-details {#content-details}

The `aue:content-details` event is triggered when a component is loaded in the properties panel.

The payload is the component's content and optionally its schema.

```json
{
    details: {
        content: object             // content object
        model: [object]             // model object
        request: request payload;   // what is sent to the service
        response: response payload; // what is returned by the service
    }
}
```

### aue:content-move {#content-move}

The `aue:content-move` event is triggered when a component is moved.

The payload is the component, source container, and target container.

```json
{
    details: {
        from: string;                   // container we move the component from
        component: string;              // component we move
        to: string;                     // container we move the component to
        before: string;                    // before which component shall we place the component
        request: request payload;       // what is sent to the service
        response: response payload;     // what is returned by the service
    }
}
```

### aue:content-patch {#content-patch}

The `aue:content-patch` event is triggered when a component's data is updated in properties panel.

The payload is a JSON patch of the updated properties.

```json
{
    details: {
        patch: {
            name: string;               // attribute which is updated
            value: string;              // new value which is stored to the attribute
        },
        request: request payload;       // what is sent to the service
        response: response payload;     // what is returned by the service
    }
}
```

### aue:content-remove {#content-remove}

The `aue:content-remove` event is triggered when a component is removed from a container.

The payload is the item ID of the removed component.

```json
{
    details: {
        resource: string;               // the resource which got removed
        request: request payload;       // what is sent to the service
        response: response payload;     // what is returned by the service
    }
}
```

### aue:content-update {#content-update}

The `aue:content-update` event is triggered when the properties of a component are updated in-context.

The payload is the updated value.

```json
{
    details: {
        value: string;                  // updated value
        request: request payload;       // what is sent to the service
        response: response payload;     // what is returned by the service 
    }
}
```

### Passing Payloads {#passing-payloads}

For all the content update events, the requested payload as well as the response payload is passed into the event. E.g., for an update call:

Request Payload:
```json
{
  "connections": [
    {
      "name": "aemconnection",
      "protocol": "aem",
      "uri": "https://author-p7452-e12433.adobeaemcloud.com"
    }
  ],
  "target": {
    "resource": "urn:aemconnection:/content/dam/wknd-shared/en/magazine/arctic-surfing/aloha-spirits-in-northern-norway/jcr:content/data/master",
    "type": "text",
    "prop": "title"
  },
  "value": "Alhoa Spirit Northern Norway!"
}
```

Response Payload
```json
{
    "updates": [
        {
            "resource": "urn:aemconnection:/content/dam/wknd-shared/en/magazine/arctic-surfing/aloha-spirits-in-northern-norway/jcr:content/data/master",
            "prop": "title",
            "type": "text"
        }
    ]
}
```

## UI Events {#ui-events}

### aue:ui-publish {#ui-publish}

The `aue:ui-publish` event is triggered when content is published (with invocation at the `BODY` level).

The payload is a list of item IDs and their publication status.

### aue:ui-select {#ui-select}

The `aue:ui-select` event is triggered when a component is selected.

The payload is the item ID, item properties, and item type of the selected component.

```json
{
    details: {
        resource: string;       // resource of the selected
        prop: string;           // prop of the selected
        type: string;           // type of the selected
        selected: boolean;      // was selected or unselected
    }
}
```

### aue:ui-preview {#ui-preview}

The `aue:ui-preview` event is triggered when the editing mode of the page is changed to **Preview**.

The payload is empty for this event.

```json
{
    details: {}
}
```

### aue:ui-edit {#ui-edit}

The `aue:ui-edit` event is triggered when the editing mode of the page is changed to **Edit**.

The payload is empty for this event.

```json
{
    details: {}
}
```

### aue:ui-viewport-change {#ui-viewport-change}

The `aue:ui-viewport-change` event is triggered when the viewport size is changed.

The payload is the dimensions of the viewport.

```json
{
    details: {
        height: number?;        // height of the viewport. Undefined when fullscreen
        width: number?;         // width of the viewport. Undefined when fullscreen
    }
}
```

### aue:initialized {#initialized}

The `aue:initialized` event is triggered to let the remote page know that it is successfully loaded in the Universal Editor.

The payload is empty for this event.

```json
{
    details: {}
}
```

## Fallback Event Listeners {#fallback-listeners}

### Content Updates {#content-update-fallbacks}

|Event|Behavior|
|---|---|
|`aue:content-add`|Page reload|
|`aue:content-details`|Do nothing|
|`aue:content-move`|Move the component's content/structure to the target area|
|`aue:content-patch`|Page reload|
|`aue:content-remove`|Remove the DOM element|
|`aue:content-update`|Update the `innerHTML` with the payload|

### UI Events {#ui-event-fallbacks}

|Event|Behavior|
|---|---|
|`aue:ui-publish`|Do nothing|
|`aue:ui-select`|Scroll to the selected element|
|`aue:ui-preview`|Add `class="adobe-ue-preview"` to HTML tag|
|`aue:ui-edit`|Add `class=adobe-ue-edit"` to HTML tag|
|`aue:ui-viewport-change`|Do nothing|
|`aue:initialized`|Do nothing|

## Additional Resources {#additional-resources}

* [Universal Editor Calls](/help/implementing/universal-editor/calls.md)

