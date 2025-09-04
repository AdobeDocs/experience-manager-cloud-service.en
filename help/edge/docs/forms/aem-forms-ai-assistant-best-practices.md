---
title: Forms Experience Builder - Best Practices
description: Comprehensive best practices for creating effective forms with Forms Experience Builder, covering design, user experience, performance, and brand consistency.
feature: Edge Delivery Services
hide: yes
index: no
hidefromtoc: yes
role: Admin, Architect, Developer
---

# Forms Experience Builder - Best Practices

>[!NOTE]
>
> The Forms Experience Builder is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This best practices guide is currently being tested against the product and is subject to updates and revisions. Best practices, recommendations, and examples may change as the Forms Experience Builder continues to evolve during the early-adopter program.

This comprehensive guide provides proven best practices for creating effective, user-friendly forms using the Forms Experience Builder. These practices are derived from successful implementations and user feedback across various industries and use cases.

## Form Design Best Practices

### Keep It Simple

**Start with Essential Fields**

- Begin with only the most necessary information to reduce user overwhelm
- Add complexity gradually based on user needs and business requirements
- Avoid asking for information you don't actually need or use
- Consider the user's time and cognitive load when designing forms

**Use Clear, Descriptive Labels**

- Make field purposes immediately obvious with descriptive labels
- Avoid technical jargon or internal terminology that users won't understand
- Use consistent labeling conventions throughout your forms
- Provide context when field requirements might not be obvious

**Provide Helpful Guidance**

- Include help text for complex fields with examples and formatting requirements
- Use placeholder text to show expected input formats
- Provide clear instructions for file uploads, including accepted formats and size limits
- Guide users through multi-step processes with progress indicators

**Test Thoroughly**

- Validate all user paths and scenarios before deployment
- Test forms with real users from your target audience
- Verify that all conditional logic works as expected
- Ensure error handling provides clear, actionable feedback

### Progressive Disclosure

**Show Relevant Fields Based on Context**

- Display additional fields only when they become relevant to user selections
- Use conditional logic to reduce cognitive load and form length
- Group related fields together in logical sections
- Hide advanced options until users indicate they need them

**Example Implementation:**

    Create a rule that shows @spouseInformation panel only when @maritalStatus equals "Married"

**Clear Navigation and Progress**

- Help users understand where they are in multi-step forms
- Provide clear navigation between form sections
- Show progress indicators for longer forms
- Allow users to save progress and return later

## User Experience Best Practices

### Mobile-First Design

**Responsive Layout Optimization**

- Design forms with mobile users as the primary consideration
- Use single-column layouts for mobile devices
- Ensure touch targets are appropriately sized (minimum 44px)
- Test forms on various device sizes and orientations

**Touch-Friendly Interactions**

- Implement larger buttons and input fields for touch interfaces
- Use appropriate input types to trigger correct mobile keyboards
- Avoid hover-dependent interactions that don't work on touch devices
- Provide clear visual feedback for user interactions

### Accessibility Compliance

**WCAG 2.1 Guidelines**

- Follow Web Content Accessibility Guidelines for inclusive design
- Ensure proper color contrast ratios (minimum 4.5:1 for normal text)
- Provide alternative text for all images and icons
- Implement proper heading structure and semantic HTML

**Keyboard Navigation**

- Ensure all form elements are accessible via keyboard navigation
- Provide clear focus indicators for all interactive elements
- Implement logical tab order through form fields
- Include skip navigation links for complex forms

**Screen Reader Support**

- Use proper ARIA labels and descriptions for form fields
- Provide clear error messages that are announced to screen readers
- Ensure dynamic content changes are properly announced
- Test forms with actual screen reader software

### Performance Optimization

**Loading Speed**

- Optimize form loading times by minimizing initial bundle size
- Implement lazy loading for non-critical form sections
- Optimize images and assets for web delivery
- Enable appropriate caching strategies for static resources

**Runtime Performance**

- Use appropriate validation timing to balance user experience and performance
- Implement debouncing for real-time validation to reduce server requests
- Cache frequently accessed data and validation results
- Optimize conditional logic execution for complex forms

**Auto-Save and Data Protection**

- Implement automatic saving of form progress to prevent data loss
- Provide offline capability where possible for form completion
- Include retry logic for failed submissions
- Offer data export options as backup for users

## Brand Consistency Best Practices

### Prepare Brand Assets in Advance

**Create Brand Templates**

- Develop standardized form templates with your organization's visual identity
- Include consistent color schemes, typography, and layout patterns
- Prepare reusable components that match your brand guidelines
- Document style standards for consistent implementation across teams

**Define Style Guidelines**

- Establish consistent field styling, button designs, and spacing standards
- Create a style guide that includes color codes, font specifications, and layout rules
- Define interaction patterns and animation guidelines
- Prepare brand-specific error messages and help text

**Build Component Library**

- Create reusable form components that match your brand identity
- Develop consistent navigation patterns and user interface elements
- Prepare branded icons, logos, and visual assets for form integration
- Establish templates for common form types (contact, registration, feedback)

### Brand Implementation Strategies

**Style Prompts for Consistency**

Include brand-specific instructions in your prompts:

    Create a professional contact form using:
    - Corporate blue (#003366) for primary buttons and headers
    - Open Sans font family for all text elements
    - 16px minimum font size for accessibility compliance
    - Consistent 24px spacing between form sections
    - Company logo in header with proper brand positioning

**Template Library Management**

- Maintain a collection of branded form templates for common use cases
- Version control your brand templates to ensure consistency
- Provide clear documentation for template usage and customization
- Regular review and update of brand assets to maintain current standards

>[!NOTE]
>
>**Custom Components**: Coordinate with your development team about using organization-specific components and their compatibility with Forms Experience Builder before implementing custom brand elements.

## Content and Communication Best Practices

### Form Creation Approaches

**Two Primary Methods**

Choose the most appropriate creation method for your needs:

1. **Create from Scratch**: Best for new forms with specific requirements
2. **Import and Convert**: Ideal for modernizing existing forms and documents

**Natural Language Prompts**

- Be specific and detailed in your form descriptions
- Use clear, business-focused language rather than technical terms
- Provide context about the form's purpose and target audience
- Include validation and business rule requirements in initial prompts

### Incremental Development Strategy

**Start Simple, Build Complexity**

- Begin with basic form structure and essential fields
- Add validation rules and business logic incrementally
- Test each addition before proceeding to the next enhancement
- Gather user feedback at each stage of development

**Example Incremental Approach:**

    Step 1: "Create a basic contact form with name, email, and message fields"
    Step 2: "Make @name and @email mandatory fields with appropriate validation"
    Step 3: "Add placeholder text and help text for user guidance"
    Step 4: "Add conditional logic based on inquiry type"

### Field Reference Best Practices

**Consistent Naming Conventions**

- Use clear, descriptive field names that match their purpose
- Maintain consistent naming patterns across forms
- Use camelCase or snake_case consistently throughout your forms
- Document field naming conventions for team consistency

**Effective Field References**

- Use `@fieldName` syntax when modifying existing fields
- Be specific about which fields you're referencing in complex forms
- Group related field modifications together in single requests
- Verify field names before using them in conditional logic

## Integration and Submission Best Practices

### Multi-Channel Submission Strategy

**Primary and Secondary Actions**

- Configure primary submission endpoints for core business processes
- Set up secondary actions for notifications, confirmations, and data backup
- Implement error handling and retry logic for failed submissions
- Provide user feedback for all submission states (success, failure, processing)

**Integration Planning**

- Start with basic submission configuration and add integrations incrementally
- Test each integration separately before combining multiple endpoints
- Document API requirements and authentication methods
- Plan for data transformation and mapping requirements

### Error Handling and Recovery

**User-Friendly Error Messages**

- Provide clear, actionable error messages that help users resolve issues
- Avoid technical error codes or system messages in user-facing content
- Offer alternative actions when primary submission fails
- Include contact information for users who need additional help

**Data Protection and Recovery**

- Implement local data saving for form recovery after errors
- Provide options for users to download their form data as backup
- Set up monitoring and alerting for submission failures
- Plan recovery procedures for system outages or maintenance

## Performance and Analytics Best Practices

### Monitoring and Optimization

**Key Performance Metrics**

- Track form completion rates and abandonment points
- Monitor loading times and user interaction patterns
- Measure validation effectiveness and error rates
- Analyze user feedback and satisfaction scores

**Continuous Improvement**

- Regular review of form analytics to identify optimization opportunities
- A/B testing of different form designs and user flows
- User feedback collection and analysis for iterative improvements
- Performance benchmarking against industry standards

### Data Quality and Validation

**Smart Validation Strategies**

- Implement real-time validation for immediate user feedback
- Use progressive validation to guide users through complex requirements
- Provide clear validation messages that explain how to fix errors
- Balance validation strictness with user experience considerations

**Data Integrity**

- Implement cross-field validation for data consistency
- Use appropriate input types and constraints to prevent invalid data
- Provide data format examples and guidance for complex fields
- Regular audit of submitted data quality and validation effectiveness

## Security and Compliance Best Practices

### Data Protection

**Privacy by Design**

- Collect only the minimum data necessary for your business purpose
- Implement appropriate data retention and deletion policies
- Provide clear privacy notices and consent mechanisms
- Ensure compliance with relevant data protection regulations (GDPR, CCPA, etc.)

**Security Implementation**

- Use HTTPS encryption for all form submissions and data transmission
- Implement proper input validation and sanitization
- Set up secure file upload with appropriate restrictions and virus scanning
- Regular security audits and vulnerability assessments

### Compliance Considerations

**Regulatory Requirements**

- Understand and implement industry-specific compliance requirements
- Document compliance measures for audit purposes
- Regular review of regulatory changes and their impact on forms
- Staff training on compliance requirements and implementation

**Accessibility Compliance**

- Follow WCAG 2.1 AA guidelines for accessibility
- Regular accessibility testing with assistive technologies
- User testing with people who have disabilities
- Documentation of accessibility features and compliance measures

## Team Collaboration Best Practices

### Documentation and Knowledge Sharing

**Form Documentation**

- Maintain clear documentation of form purposes, requirements, and business rules
- Document integration endpoints, data flows, and dependencies
- Keep version history and change logs for form updates
- Share best practices and lessons learned across teams

**Training and Adoption**

- Provide training for team members on Forms Experience Builder capabilities
- Establish guidelines for consistent form creation across the organization
- Regular knowledge sharing sessions for new features and best practices
- Mentoring programs for new users of the platform

### Quality Assurance

**Review Processes**

- Implement peer review processes for form design and implementation
- Establish testing protocols for form functionality and user experience
- Regular audits of existing forms for optimization opportunities
- Feedback collection from both internal users and end users

**Standards and Guidelines**

- Develop organizational standards for form design and implementation
- Create templates and guidelines for common form types
- Establish approval processes for new forms and major changes
- Regular review and update of organizational standards

## Advanced Best Practices

### LLM-Enhanced Smart Fields

**Leveraging AI Knowledge**

- Use the AI's built-in knowledge for comprehensive field options
- Request smart fields for geographic data, business classifications, and industry standards
- Implement intelligent field population for improved user experience
- Test smart field accuracy and completeness for your specific use cases

**Smart Field Examples**

    "Add a departure airport field with all major airports worldwide including IATA codes"
    "Create a comprehensive industry field using standard NAICS classification"
    "Include a professional certification dropdown that adapts based on job field"

### Advanced Form Logic

**Complex Business Rules**

- Break complex business logic into smaller, testable components
- Document business rule requirements clearly before implementation
- Test edge cases and exception scenarios thoroughly
- Provide clear user feedback for business rule violations

**Dynamic Form Behavior**

- Use progressive disclosure to show relevant fields based on user input
- Implement smart defaults that can be overridden by users
- Create adaptive forms that adjust based on user behavior and preferences
- Balance automation with user control and transparency

## Validation and Testing

### Comprehensive Testing Strategy

**Multi-Level Testing**

- Unit testing for individual form components and validation rules
- Integration testing for submission endpoints and data flows
- User acceptance testing with representative user groups
- Performance testing under various load conditions

**Cross-Platform Validation**

- Test forms across different browsers and versions
- Validate mobile experience on various devices and screen sizes
- Accessibility testing with different assistive technologies
- Network condition testing for various connection speeds

### Quality Metrics

**Success Indicators**

- Form completion rates above industry benchmarks
- Low error rates and high user satisfaction scores
- Fast loading times and responsive user interactions
- Successful integration with backend systems and processes

**Continuous Monitoring**

- Regular review of form performance metrics and user feedback
- Proactive identification and resolution of issues
- Trend analysis for form usage and effectiveness
- Benchmarking against industry standards and best practices

For additional guidance and detailed examples, refer to the [Forms Experience Builder Getting Started Guide](forms-ai-assistant-getting-started.md) and [Forms Experience Builder Prompt Library](ai-assistant-prompt-library.md).
