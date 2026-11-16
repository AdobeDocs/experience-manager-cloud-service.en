---
title: From Spreadsheets to Forms -  Mastering Adaptive Forms Block Field Validations
description: Craft powerful forms faster using spreadsheets & Adaptive Forms Block Fields! This guide helps you build custom validations for EDS Forms Block fields.
feature: Edge Delivery Services
hide: true
exl-id: 16e1d42a-42d0-4335-ba81-feedea7ed7d7
role: Admin, Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: f2d27a5f-0d67-4d85-8a24-86a8d8a3574b
    internal-label: Developer tools
subfeature_v2:
  - id: f88183b7-5ea5-436c-ac46-96b53f0281ea
    internal-label: Edge Delivery Services
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Add validations to form fields

Adaptive Forms Block has a built-in validations features. These validations are automatically applied in modern browsers based on the chosen field type and the additional properties you provide.

## Understanding Field Types and Validation

The Adaptive Forms Block supports a variety of [HTML-5 input types](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types), including text, email, number, date, and more. It also accommodates [textarea](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea), select, and fieldset, along with comprehensive input validation features inherent to HTML-5.

uses HTML field types to define the kind of data a user can enter. Different field types have different built-in validation rules:

Email: This field type automatically validates user input against a common email address format. Users entering an invalid email will see an error message.
Number: This field type only allows numerical input. Users entering non-numeric characters will receive an error.
Date: This field type validates user input against a standard date format. Dates outside a reasonable range might also be flagged as invalid.
URL: This field type validates user input against a valid URL format. Users entering an invalid URL will see an error message.
Tel: This field type is specifically designed for phone numbers and might trigger validation based on specific country formats (not universally supported).



