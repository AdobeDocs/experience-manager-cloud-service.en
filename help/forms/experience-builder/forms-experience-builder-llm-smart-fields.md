---
title: LLM-enhanced smart fields in Forms Experience Builder
description: Learn how to create intelligent form fields with pre-populated options using AI knowledge base for geographic data, business classifications, and industry standards.
hide: yes
index: no
hidefromtoc: yes
role: Admin, Developer
exl-id: a03b247c-1e50-4dee-9182-bc81fb83a48b
---
# LLM-enhanced smart fields in Forms Experience Builder {#llm-enhanced-smart-fields}

Forms Experience Builder leverages the power of Large Language Models (LLMs) to create intelligent form fields with pre-populated options that draw from comprehensive knowledge bases. This capability eliminates the need to manually research and input extensive data sets, dramatically improving form creation efficiency and accuracy.

## What are LLM-enhanced smart fields? {#what-are-llm-smart-fields}

LLM-enhanced smart fields are form fields that automatically populate with comprehensive, accurate data using the AI's built-in knowledge base. Instead of manually creating dropdown lists or option sets, you can request fields that require extensive data sets, and the AI will automatically generate the appropriate options.

**Key benefits:**

* **Comprehensive data sets** - Access to extensive, up-to-date information across multiple domains
* **Automatic population** - No need to manually research and input data
* **Standardized formats** - Uses industry-standard codes, classifications, and naming conventions
* **Context-aware options** - Fields can adapt based on other form selections
* **Time-saving** - Reduces form creation time from hours to minutes

## When to use LLM-enhanced smart fields {#when-to-use-smart-fields}

Use LLM-enhanced smart fields when you need:

* **Comprehensive data sets** - Fields requiring extensive, standardized information
* **Industry standards** - Classifications, codes, or regulatory data
* **Geographic information** - Locations, regions, or administrative divisions
* **Professional data** - Job titles, certifications, or industry classifications
* **Technical standards** - File formats, protocols, or system specifications

## Geographic and location fields {#geographic-location-fields}

Create location-based fields with comprehensive geographic data and administrative information.

### Airports and transportation

**International airports with IATA codes:**

    Add a dropdown for departure airports with all major international airports
    Add arrival airport field with IATA codes and full names
    Create a field for nearest airport to user location
    Add a selection of train stations for European cities

**Example prompts:**

* "Add a departure airport field with all major airports worldwide including IATA codes and city names"
* "Create an arrival airport dropdown with international airports organized by continent"
* "Include a train station selection for major European cities with station codes"

### Administrative regions

**Countries, states, and provinces:**

    Add a complete list of US states with abbreviations
    Create a country dropdown with ISO codes and full names
    Add a field for major world cities with time zones
    Include a dropdown of Canadian provinces and territories
    Add a field for UK counties and postal areas

**Example prompts:**

* "Create a country selection field with ISO country codes and full names"
* "Add a US state dropdown with state abbreviations and full names"
* "Include a Canadian province field with territories and postal codes"
* "Create a world cities field with major metropolitan areas and time zones"

## Business and industry data {#business-industry-data}

Leverage comprehensive business classifications and professional data for corporate forms.

### Company classifications

**Industry and business entity types:**

    Add a field for industry classification with NAICS codes
    Create a dropdown of business entity types (LLC, Corporation, Partnership, etc.)
    Add a field for company size categories (startup, SME, enterprise)
    Include department selection for large organizations
    Add a field for professional service types

**Example prompts:**

* "Create a comprehensive industry field using standard NAICS classification with technology subcategories"
* "Add a business entity type dropdown with legal structures and descriptions"
* "Include a company size field with employee count ranges and revenue brackets"

### Professional classifications

**Job titles and certifications:**

    Add a field for job titles with common industry roles
    Create a dropdown of professional certifications by field
    Include education levels with degree types
    Add a field for years of experience ranges
    Create a selection for programming languages and frameworks

**Example prompts:**

* "Include a professional certification dropdown that adapts based on the selected job field"
* "Create a job title field with common roles in technology, healthcare, and finance"
* "Add an education level field with degree types and specializations"

## Standards and regulatory data {#standards-regulatory-data}

Access standardized codes, classifications, and regulatory information for compliance-focused forms.

### Financial and legal

**Currency, tax, and payment information:**

    Add a field for currency codes with symbols and exchange rates
    Create a dropdown of tax ID types by country
    Include a field for legal document types
    Add payment method options with security features
    Create a selection for banking institutions by country

**Example prompts:**

* "Create a currency selection field with ISO codes, symbols, and major exchange rates"
* "Add a tax ID type field with country-specific tax identification formats"
* "Include a payment method dropdown with security features and processing times"

### Technical standards

**File formats and protocols:**

    Add a dropdown of file format types with extensions
    Include network protocol options
    Add a field for database types and versions
    Create a selection for API authentication methods

**Example prompts:**

* "Create a file format dropdown with common extensions and MIME types"
* "Add a database selection field with versions and feature comparisons"
* "Include an API authentication method field with security levels"

## Healthcare and medical fields {#healthcare-medical-fields}

Specialized medical and healthcare data for industry-specific forms.

### Medical classifications

**Specialties and medical data:**

    Add a field for medical specialties
    Create a dropdown of common medications with generic names
    Include a field for insurance provider types
    Add a selection for medical emergency contact relationships
    Create a field for dietary restrictions and allergies

**Example prompts:**

* "Create a medical specialty field with subspecialties and board certifications"
* "Add a medication field with generic names, brand names, and dosage forms"
* "Include an insurance provider field with major carriers and plan types"

## Time and calendar intelligence {#time-calendar-intelligence}

Smart date and time fields with business context and scheduling intelligence.

### Date and time fields

**Business hours and scheduling:**

    Add a field for business hours with time zone handling
    Create a dropdown of public holidays by country
    Include seasonal options with date ranges
    Add a field for conference room booking with availability
    Create a selection for recurring meeting patterns

**Example prompts:**

* "Create a business hours field with time zones and holiday exceptions"
* "Add a public holiday selection with country-specific observances"
* "Include a recurring meeting pattern field with frequency options"

## Product and service categories {#product-service-categories}

E-commerce and service-oriented fields with comprehensive categorization.

### E-commerce classifications

**Product and service data:**

    Add a field for product categories with subcategories
    Create a dropdown of shipping methods with delivery estimates
    Include a field for return policy options
    Add a selection for customer priority levels
    Create a field for subscription billing cycles

**Example prompts:**

* "Create a product category field with e-commerce subcategories and SKU patterns"
* "Add a shipping method dropdown with delivery times and cost estimates"
* "Include a subscription billing cycle field with payment frequencies"

## Best practices for LLM-enhanced smart fields {#best-practices-smart-fields}

### Be specific in your requests

**Good examples:**

* "Add a country dropdown with ISO codes, full names, and currency information"
* "Create a medical specialty field with board certifications and subspecialties"
* "Include a programming language field with frameworks and skill levels"

**Avoid vague requests:**

* "Add a country field"
* "Create a job title dropdown"
* "Include a product category field"

### Combine with conditional logic

Smart fields work exceptionally well with conditional rules:

    Create a professional certification field that shows relevant options based on the selected industry
    Add a city field that filters based on the selected country
    Include a university field that adapts based on the chosen field of study

### Validate and customize

While LLM-enhanced fields provide comprehensive data, always:

* **Review the generated options** for accuracy and relevance
* **Add custom options** specific to your organization
* **Remove irrelevant options** to streamline user experience
* **Test with real users** to ensure usability

## Advanced smart field techniques {#advanced-smart-field-techniques}

### Context-aware fields

Create fields that adapt based on other form selections:

    Add a university selection field with major institutions organized by country and ranking
    Create a professional certification dropdown that shows relevant options based on job title
    Include a city field that filters based on selected country and region

### Multi-level classifications

Build hierarchical data structures:

    Create a product category field with main categories, subcategories, and product types
    Add a geographic field with country, state/province, and city levels
    Include a skill assessment field with categories, subcategories, and proficiency levels

### Integration with external data

Combine LLM knowledge with your organization's data:

    Add a department field that includes both standard corporate departments and your organization's specific divisions
    Create a product field that combines industry-standard categories with your product catalog
    Include a location field that merges geographic data with your office locations

## Troubleshooting smart fields {#troubleshooting-smart-fields}

### Common issues and solutions

**Issue: Too many options generated**

* **Solution**: Be more specific in your request or add filtering criteria
* **Example**: Instead of "all countries," request "major trading partner countries"

**Issue: Missing specific options**

* **Solution**: Add custom options or refine your prompt
* **Example**: "Include major countries plus [your specific countries]"

**Issue: Outdated information**

* **Solution**: Request current data or specify date ranges
* **Example**: "Add current public holidays for 2024"

### Performance optimization

* **Limit options**: Use filters to reduce the number of generated options
* **Progressive disclosure**: Show basic options first, then allow expansion
* **Caching**: Consider caching frequently used smart field data

## Related articles

* [Getting started with Forms Experience Builder](forms-experience-builder-getting-started.md)
* [AI-powered form creation](forms-experience-builder-prompt-examples-library.md)
* [Rule creation and business logic](forms-experience-builder-prompt-examples-library.md#rule-creation--business-logic)
* [Form submission and integration](form-submission-integration.md)
