---
title: Forms Experience Builder - Troubleshooting Guide
description: Comprehensive troubleshooting guide for Forms Experience Builder, covering common issues, solutions, and debugging techniques for form creation and management.
feature: Edge Delivery Services
hide: yes
index: no
hidefromtoc: yes
role: Admin, Architect, Developer
---

# Forms Experience Builder - Troubleshooting Guide

>[!NOTE]
>
> The Forms Experience Builder is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This troubleshooting guide is currently being tested against the product and is subject to updates and revisions. Issues, solutions, and debugging techniques may change as the Forms Experience Builder continues to evolve during the early-adopter program.

This comprehensive troubleshooting guide helps you identify, diagnose, and resolve common issues when working with the Forms Experience Builder. The guide is organized by problem categories with quick fixes and detailed solutions.

## Quick Reference - Common Issues

| Issue | Quick Fix |
|-------|-----------|
| **Interface not loading** | Refresh browser, check internet connection, verify early access permissions |
| **Commands not working** | Try `/help` or use natural language instead of slash commands |
| **@fieldName not recognized** | Check spelling, ensure field exists first, verify field name syntax |
| **File upload fails** | Use PDF/JPG/PNG under 10MB, check file format compatibility |
| **Form looks wrong** | Be more specific: "Make it mobile-friendly" instead of "fix layout" |
| **Integration fails** | Verify API credentials and permissions, check endpoint availability |
| **Form not submitting** | Check submit action configuration and validation rules |
| **Validation errors not showing** | Verify field validation settings and error message placement |
| **Mobile layout issues** | Review responsive design settings and field sizing |
| **Fields not appearing** | Check conditional logic and visibility rules |
| **Import failures** | Verify file format compatibility and size limits |
| **Performance issues** | Optimize field count and remove unnecessary validations |
| **Accessibility problems** | Review field labels, ARIA attributes, and tab order |

**Still need help?** Type `/help` followed by your specific question or contact your system administrator for technical assistance.

## Access and Authentication Issues

### Cannot Access Forms Experience Builder

**Symptoms:**

- Forms Experience Builder interface not visible
- "Access Denied" or similar error messages
- Missing Forms Experience Builder icon in editor

**Solutions:**

1. **Verify Early Access Program Enrollment**
   - Confirm you've been approved for the early-adopter program
   - Check that your request was sent from your official work email
   - Contact `aem-forms-ea@adobe.com` if access is still pending

2. **Check Environment Setup**
   - Verify AEM Forms is enabled for your environment
   - Ensure you're using a supported browser (Chrome, Firefox, Safari, Edge)
   - Clear browser cache and cookies
   - Disable browser extensions that might interfere

3. **Verify User Permissions**
   - Confirm you have appropriate user roles and permissions
   - Check with your system administrator about access rights
   - Verify you're logged in with the correct account

### Interface Loading Problems

**Symptoms:**

- Blank or partially loaded interface
- Spinning loading indicators that don't complete
- JavaScript errors in browser console

**Solutions:**

1. **Browser Troubleshooting**
   - Refresh the page (Ctrl+F5 or Cmd+Shift+R)
   - Try a different browser or incognito/private mode
   - Check for browser updates and install if available
   - Disable ad blockers and privacy extensions temporarily

2. **Network Connectivity**
   - Verify stable internet connection
   - Check if corporate firewall is blocking required domains
   - Test with different network connection if possible
   - Contact IT support for network configuration issues

3. **Cache and Storage Issues**
   - Clear browser cache and local storage
   - Reset browser settings to default
   - Check available disk space on your device
   - Try accessing from a different device

## Command and Interaction Issues

### Slash Commands Not Working

**Symptoms:**

- `/create-form` or other slash commands not recognized
- No autocomplete suggestions appearing
- Commands result in error messages

**Solutions:**

1. **Command Syntax Verification**
   - Ensure proper command format: `/command-name description`
   - Check for typos in command names
   - Use natural language as alternative: "Create a contact form"
   - Try `/help` to verify command availability

2. **Context-Specific Commands**
   - Verify you're in the correct editor context (Universal Editor vs Adaptive Forms Editor)
   - Some commands only work in specific environments
   - Check command reference for context requirements

3. **Alternative Approaches**
   - Use natural language instead of slash commands
   - Break complex commands into smaller, simpler requests
   - Try step-by-step form building instead of single complex command

### Field References Not Working

**Symptoms:**

- `@fieldName` references not recognized
- Error messages about unknown fields
- Field modifications not applying correctly

**Solutions:**

1. **Field Name Verification**
   - Check exact spelling of field names (case-sensitive)
   - Ensure the field exists before referencing it
   - Use the exact field name as created, not display label
   - Verify field naming conventions (camelCase, snake_case, etc.)

2. **Field Reference Syntax**
   - Use proper `@fieldName` syntax without spaces
   - Avoid special characters in field references
   - Check for invisible characters or formatting issues
   - Try recreating the field reference manually

3. **Debugging Field References**
   - List all existing fields first: "Show me all current form fields"
   - Create fields before referencing them in rules
   - Use simple field names without complex characters
   - Test field references one at a time

## Form Creation and Design Issues

### Form Not Creating as Expected

**Symptoms:**

- Generated form missing requested fields
- Incorrect field types or layouts
- Form structure doesn't match description

**Solutions:**

1. **Improve Prompt Specificity**
   - Be more detailed in form descriptions
   - Specify exact field types and validation requirements
   - Include layout preferences and user experience requirements
   - Break complex forms into smaller, incremental requests

2. **Iterative Development Approach**
   - Start with basic form structure
   - Add fields and features incrementally
   - Test each addition before proceeding
   - Refine through conversation rather than single complex request

3. **Example of Better Prompts**

   Instead of:

       Create a form for customers

   Use:

       Create a customer contact form with:
       - Full name (required text field)
       - Email address (required with validation)
       - Phone number (optional, formatted)
       - Message (required textarea, max 500 characters)
       - Submit to email notification

### Layout and Styling Issues

**Symptoms:**

- Form appears broken on mobile devices
- Inconsistent spacing or alignment
- Fields not displaying correctly
- Poor visual hierarchy

**Solutions:**

1. **Mobile Responsiveness**
   - Request mobile-specific optimizations: "Make this form mobile-friendly"
   - Specify responsive design requirements
   - Test on actual mobile devices
   - Use single-column layouts for mobile

2. **Layout Improvements**
   - Be specific about layout requirements: "Arrange address fields in two columns"
   - Request specific styling: "Use professional colors and clean typography"
   - Specify spacing and alignment needs
   - Ask for accessibility compliance

3. **Brand Consistency**
   - Prepare brand guidelines before form creation
   - Include specific color codes and fonts in requests
   - Use consistent styling across all forms
   - Create brand templates for reuse

### Conditional Logic Problems

**Symptoms:**

- Rules not triggering as expected
- Fields showing/hiding incorrectly
- Validation logic not working
- Complex business rules failing

**Solutions:**

1. **Rule Simplification**
   - Break complex rules into smaller, simpler conditions
   - Test each rule individually before combining
   - Use clear, specific conditions: "Show @spouseInfo when @maritalStatus equals 'Married'"
   - Avoid nested or overly complex logic initially

2. **Rule Testing and Debugging**
   - Test all possible user paths and scenarios
   - Verify field names and values in conditions
   - Check for case sensitivity in rule conditions
   - Use debug mode to trace rule execution

3. **Business Logic Implementation**
   - Document business requirements clearly before implementation
   - Implement rules incrementally and test each step
   - Provide clear user feedback when rules are triggered
   - Handle edge cases and exception scenarios

## File Import and Conversion Issues

### PDF Import Failures

**Symptoms:**

- PDF files not uploading or processing
- Converted forms missing fields or content
- Error messages during PDF conversion
- Poor field recognition from PDF

**Solutions:**

1. **File Format and Size**
   - Ensure PDF files are under 10MB
   - Use high-quality, text-based PDFs (not scanned images)
   - Verify PDF is not password-protected or encrypted
   - Try converting PDF to image format if text extraction fails

2. **PDF Quality Optimization**
   - Use PDFs with clear, well-defined form fields
   - Ensure good contrast and readable text
   - Avoid complex layouts or overlapping elements
   - Provide additional context in conversion request

3. **Conversion Enhancement**
   - Describe the expected form structure in detail
   - Specify field types and validation requirements
   - Request specific improvements: "Add mobile responsiveness and validation"
   - Review and refine converted forms manually

### Image and Screenshot Conversion Issues

**Symptoms:**

- Poor field recognition from images
- Incorrect field types or layouts
- Missing form elements
- Conversion errors or timeouts

**Solutions:**

1. **Image Quality Requirements**
   - Use high-resolution images (minimum 300 DPI)
   - Ensure good lighting and contrast
   - Avoid shadows, glare, or distortions
   - Crop images to focus on form content only

2. **Optimal Image Formats**
   - Use PNG or JPG formats for best results
   - Avoid GIF or low-quality compressed images
   - Ensure text is clearly readable in the image
   - Try different image orientations if needed

3. **Conversion Guidance**
   - Provide detailed descriptions of form structure
   - Specify field types and requirements explicitly
   - Request specific enhancements during conversion
   - Be prepared to make manual adjustments after conversion

## Integration and Submission Issues

### Form Submission Failures

**Symptoms:**

- Forms not submitting successfully
- Error messages during submission
- Data not reaching intended destinations
- Timeout errors during submission

**Solutions:**

1. **Submit Action Configuration**
   - Verify submit action is properly configured
   - Check API endpoints and authentication credentials
   - Test with simple email submission first
   - Validate data format requirements

2. **Network and Connectivity**
   - Check internet connectivity and network stability
   - Verify firewall settings allow form submissions
   - Test from different network connections
   - Check for corporate proxy or security restrictions

3. **Data Validation Issues**
   - Ensure all required fields are completed
   - Verify data formats match API requirements
   - Check for special characters or encoding issues
   - Test with minimal data set first

### API Integration Problems

**Symptoms:**

- REST API endpoints not responding
- Authentication failures
- Data format mismatches
- Integration timeouts or errors

**Solutions:**

1. **API Configuration Verification**
   - Verify API endpoint URLs are correct and accessible
   - Check authentication credentials and permissions
   - Test API endpoints independently using tools like Postman
   - Verify API is accepting the correct data format (JSON, XML, etc.)

2. **Data Mapping Issues**
   - Ensure form field names match API parameter requirements
   - Check for required fields that might be missing
   - Verify data type compatibility (strings, numbers, dates)
   - Test with sample data to identify mapping issues

3. **Error Handling and Debugging**
   - Enable detailed error logging for API calls
   - Check API response codes and error messages
   - Implement retry logic for temporary failures
   - Provide fallback options for users when API fails

### Email Integration Issues

**Symptoms:**

- Confirmation emails not sending
- Emails going to spam folders
- Incorrect email formatting
- Missing form data in emails

**Solutions:**

1. **Email Configuration**
   - Verify email addresses are correctly formatted
   - Check SMTP settings and authentication
   - Test with simple email addresses first
   - Verify email server permissions and quotas

2. **Email Delivery Optimization**
   - Use proper email headers and sender information
   - Avoid spam trigger words in subject lines
   - Include proper unsubscribe mechanisms
   - Test email delivery to different providers

3. **Content and Formatting**
   - Verify form data is properly formatted in emails
   - Check for special characters or encoding issues
   - Test email templates with various data combinations
   - Ensure email content is accessible and readable

## Performance and Loading Issues

### Slow Form Loading

**Symptoms:**

- Forms take long time to load initially
- Sluggish user interactions
- Timeouts during form operations
- Poor performance on mobile devices

**Solutions:**

1. **Form Optimization**
   - Reduce number of fields and complexity
   - Implement lazy loading for non-critical sections
   - Optimize images and assets for web delivery
   - Remove unnecessary validation rules or logic

2. **Browser and Device Optimization**
   - Clear browser cache and temporary files
   - Close unnecessary browser tabs and applications
   - Check available device memory and storage
   - Try different browsers for performance comparison

3. **Network Optimization**
   - Test with different network connections
   - Check for network congestion or bandwidth limitations
   - Use wired connection instead of WiFi if possible
   - Contact IT support for network performance issues

### Validation Performance Issues

**Symptoms:**

- Slow validation responses
- Delayed error message display
- Form freezing during validation
- Timeout errors during field validation

**Solutions:**

1. **Validation Optimization**
   - Reduce frequency of real-time validation
   - Implement debouncing for validation calls
   - Simplify complex validation rules
   - Use client-side validation where possible

2. **Rule Simplification**
   - Break complex validation into smaller rules
   - Remove unnecessary cross-field validations
   - Optimize conditional logic for performance
   - Cache validation results where appropriate

3. **User Experience Improvements**
   - Provide immediate feedback for simple validations
   - Use progressive validation instead of real-time for complex rules
   - Show loading indicators during validation processes
   - Allow users to continue while validation processes in background

## Advanced Troubleshooting

### Debug Mode and Diagnostics

**Enable Debug Information**

Use these prompts to get more detailed information about form issues:

    Enable debug mode to identify issues with form submission and field validation

    Analyze form errors: check validation rules, API responses, and user input patterns

    Show detailed information about form structure and field configuration

### Error Analysis Techniques

**Systematic Debugging Approach**

1. **Isolate the Problem**
   - Test with minimal form configuration
   - Remove complex features temporarily
   - Test individual components separately
   - Use process of elimination to identify root cause

2. **Gather Diagnostic Information**
   - Check browser console for JavaScript errors
   - Review network requests and responses
   - Document exact steps to reproduce the issue
   - Collect screenshots and error messages

3. **Test Environment Variables**
   - Try different browsers and devices
   - Test with different user accounts and permissions
   - Verify in different network environments
   - Compare with working forms or configurations

### Log Analysis and Monitoring

**Browser Console Debugging**

1. Open browser developer tools (F12)
2. Check Console tab for JavaScript errors
3. Review Network tab for failed requests
4. Monitor Performance tab for slow operations

**Common Error Patterns**

- **CORS Errors**: Cross-origin request issues with API integrations
- **Authentication Failures**: Invalid credentials or expired tokens
- **Validation Errors**: Field validation rule conflicts or syntax errors
- **Network Timeouts**: Slow or unreliable network connections

## Getting Additional Help

### Self-Service Resources

**Built-in Help System**

- Use `/help` command followed by specific questions
- Access contextual help within the Forms Experience Builder interface
- Review error messages carefully for specific guidance
- Check the [Forms Experience Builder Getting Started Guide](forms-ai-assistant-getting-started.md)

**Documentation Resources**

- [Forms Experience Builder Prompt Library](ai-assistant-prompt-library.md)
- [Forms Experience Builder Best Practices](aem-forms-ai-assistant-best-practices.md)
- [AEM Forms Documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/home.html)

### Escalation and Support

**When to Contact Support**

- Issues persist after trying documented solutions
- System-wide problems affecting multiple users
- Security or data integrity concerns
- Integration issues requiring system-level configuration

**Information to Provide**

- Detailed description of the issue and steps to reproduce
- Screenshots or screen recordings of the problem
- Browser and system information
- Error messages and console logs
- Form configuration and integration details

**Contact Methods**

- System Administrator: For environment and access issues
- Technical Support: For complex integration and configuration problems
- Early Access Program: `aem-forms-ea@adobe.com` for program-specific issues

### Community and Knowledge Sharing

**Best Practices for Issue Resolution**

- Document solutions for future reference
- Share successful troubleshooting approaches with team members
- Contribute to organizational knowledge base
- Participate in user communities and forums

**Continuous Improvement**

- Regular review of common issues and solutions
- Update troubleshooting procedures based on new findings
- Training and knowledge sharing sessions
- Feedback to product team for feature improvements

This troubleshooting guide is continuously updated based on user feedback and new Forms Experience Builder capabilities. For the latest information and additional resources, check the [AEM Forms documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/home.html).
