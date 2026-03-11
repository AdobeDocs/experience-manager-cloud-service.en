---
title: Intelligent import and conversion
description: Learn how to transform existing documents, PDFs, and images into interactive digital forms using Forms Experience Builder's intelligent import and conversion capabilities.
hide: yes
index: no
hidefromtoc: yes
role: Admin, Developer
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: 7268c4be-1e4a-4d31-aa76-9076d7ee83ce
---
# Intelligent import and conversion

>[!NOTE]
>
> The Forms Experience Builder is available under an early access program. Before you begin, please ensure you have requested and been granted access.

Forms Experience Builder's intelligent import and conversion feature allows you to transform existing documents, PDFs, and images into modern, interactive digital forms using AI-powered analysis and conversion.

## Supported source formats

### PDF documents

**AcroForm PDFs:**

- Interactive PDF forms with form fields
- Static PDFs with form-like layouts
- Multi-page documents with structured content

**XFA-based PDFs:**

- Legacy XFA (XML Forms Architecture) forms
- Complex business forms with advanced layouts
- Government and enterprise forms

**Static PDFs:**

- Scanned documents and forms
- Print-ready forms without interactive elements
- Documents with form-like structures

### Image files

**Supported formats:**

- PNG, JPG, JPEG, GIF
- High-resolution scans of paper forms
- Screenshots of digital forms
- Hand-drawn sketches and wireframes

**Image quality requirements:**

- Minimum 300 DPI for text recognition
- Clear, readable text and form elements
- Good contrast between text and background
- Proper orientation (not rotated)

### Design files

**Figma designs:**

- Form mockups and prototypes
- UI/UX design files
- Component-based form layouts

**Other design formats:**

- Adobe XD files
- Sketch designs
- Wireframe documents

## How to import and convert

### Step 1: Access the import feature

1. Open Forms Experience Builder
2. Click the attachment icon in the interface
3. Select "Import and Convert" option
4. Choose your source file

### Step 2: Upload your document

**For PDF files:**

1. Select your PDF document
2. Wait for the AI to analyze the structure
3. Review the detected form elements
4. Confirm the conversion settings

**For image files:**

1. Upload your image (PNG, JPG, etc.)
2. The AI will analyze the layout and text
3. Review the detected form fields
4. Make adjustments if needed

**For design files:**

1. Upload your design file
2. The AI will extract form components
3. Review the converted elements
4. Customize the form structure

### Step 3: Review and customize

After the initial conversion:

1. **Review detected fields**: Check that all form elements are correctly identified
2. **Adjust field types**: Modify field types (text, dropdown, checkbox, etc.)
3. **Add validation**: Set up field validation rules
4. **Customize styling**: Apply themes and branding
5. **Test functionality**: Verify form behavior and logic

## Conversion examples

### PDF form conversion

**Original PDF form:**

- Static contact form with name, email, phone fields
- Company information section
- Comments area

**Converted adaptive form:**

- Interactive text fields with validation
- Dropdown for company size
- Multi-line text area for comments
- Submit button with email integration

### Image to form conversion

**Original image:**

- Photo of a paper registration form
- Handwritten form with checkboxes
- Multiple sections for different information

**Converted adaptive form:**

- Digital text fields matching the layout
- Interactive checkboxes and radio buttons
- Organized sections with proper spacing
- Mobile-responsive design

### Design file conversion

**Original Figma design:**

- Modern UI mockup with form components
- Branded styling and colors
- Complex layout with multiple panels

**Converted adaptive form:**

- Pixel-perfect recreation of the design
- Interactive form elements
- Responsive behavior across devices
- Brand-consistent styling

## Advanced conversion features

### Intelligent field detection

The AI automatically detects and converts:

- **Text fields**: Single-line and multi-line text areas
- **Selection fields**: Dropdowns, radio buttons, checkboxes
- **Date fields**: Date pickers with proper formatting
- **Number fields**: Numeric inputs with validation
- **File uploads**: Document and image upload areas

### Layout preservation

The conversion maintains:

- **Original structure**: Preserves the layout and organization
- **Visual hierarchy**: Maintains headings and section breaks
- **Spacing and alignment**: Keeps proper form spacing
- **Brand elements**: Preserves logos and styling elements

### Smart validation

Automatically adds appropriate validation:

- **Email fields**: Email format validation
- **Phone numbers**: Phone number format validation
- **Required fields**: Marks obvious required fields
- **Date ranges**: Sets appropriate date constraints

## Best practices for import and conversion

### Preparing source documents

**For PDF files:**

- Ensure text is selectable (not just images)
- Use high-quality scans for static PDFs
- Organize content in logical sections
- Include clear field labels

**For images:**

- Use high-resolution images (300+ DPI)
- Ensure good contrast and readability
- Avoid rotated or skewed images
- Include all form elements in the image

**For design files:**

- Use consistent naming for form components
- Organize layers logically
- Include all necessary form elements
- Export in high quality

### Post-conversion optimization

**Review and test:**

- Test all form fields and validation
- Verify mobile responsiveness
- Check accessibility compliance
- Test submission functionality

**Customize and enhance:**

- Add business logic and conditional rules
- Implement proper error handling
- Configure submission endpoints
- Apply brand styling and themes

## Troubleshooting conversion issues

### Common problems

**Poor field detection:**

- Improve image quality or PDF text clarity
- Manually adjust field types after conversion
- Use more descriptive field labels in source

**Layout issues:**

- Adjust spacing and alignment manually
- Use responsive design principles
- Test on different screen sizes

**Missing elements:**

- Add missing fields manually
- Re-import with better source quality
- Use incremental conversion approach

### Getting help

For conversion issues:

- Check the [Forms Experience Builder FAQ](forms-experience-builder-frequently-asked-questions.md)
- Review the [Getting Started guide](forms-experience-builder-getting-started.md)
- Contact your system administrator for technical assistance

## Related articles

- [Forms Experience Builder Overview](product-overview.md)
- [Getting started with Forms Experience Builder](forms-experience-builder-getting-started.md)
- [Deploy and configure Forms Experience Builder](deploy-forms-experience-builder.md)
- [Form submission and integration](form-submission-integration.md)
- [Frequently asked questions](forms-experience-builder-frequently-asked-questions.md)
