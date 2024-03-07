---
title: From Spreadsheets to Forms -  Mastering Adaptive Form Block Field Validations
description: Craft powerful forms faster using spreadsheets & Adaptive Form Block Fields! This guide helps you build custom validations for EDS Forms Block fields.
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
exl-id: 16e1d42a-42d0-4335-ba81-feedea7ed7d7
---
# Add validations to form fields

Adaptive Form Block has a built-in validations features. These validations are automatically applied in modern browsers based on the chosen field type and the additional properties you provide.

## Understanding Field Types and Validation

The Adaptive Form Block supports a variety of [HTML-5 input types](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types), including text, email, number, date, and more. It also accommodates [textarea](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea), select, and fieldset, along with comprehensive input validation features inherent to HTML-5.

uses HTML field types to define the kind of data a user can enter. Different field types have different built-in validation rules:

Email: This field type automatically validates user input against a common email address format. Users entering an invalid email will see an error message.
Number: This field type only allows numerical input. Users entering non-numeric characters will receive an error.
Date: This field type validates user input against a standard date format. Dates outside a reasonable range might also be flagged as invalid.
URL: This field type validates user input against a valid URL format. Users entering an invalid URL will see an error message.
Tel: This field type is specifically designed for phone numbers and might trigger validation based on specific country formats (not universally supported).


## See more

* [Create and preview a form](/help/edge/docs/forms/create-forms.md)
* [Enable form to send data](/help/edge/docs/forms/submit-forms.md)
* [Publish a form to sites page](/help/edge/docs/forms/publish-forms.md)
* [Add validations to form fields](/help/edge/docs/forms/validate-forms.md)
* [Change themes and style of form](/help/edge/docs/forms/style-theme-forms.md)
