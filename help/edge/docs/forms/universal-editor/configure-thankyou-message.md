---

title: "How to Configure a Redirect Page or Thank you message"
description: "Learn how users can be displayed a thank you message or redirected to a webpage that form authors can configure while creating the form."
feature: Adaptive Forms, Edge Delivery Services
role: User
level: Intermediate
---

# Configure Thank You Messages and Redirect URLs

Post-submission experiences significantly impact user satisfaction and form completion rates. Adobe's Universal Editor provides comprehensive options for configuring what users see after submitting forms, whether through personalized thank you messages or strategic redirects to specific pages.

This article provides detailed guidance on implementing both thank you messages and redirect URLs, including technical considerations, best practices, and user experience guidelines to maximize the effectiveness of your form submissions.

## Prerequisites

Before configuring post-submission experiences, ensure you have:

**Technical setup:**

- Access to Universal Editor with appropriate permissions
- An existing Adaptive Form created in Universal Editor
- Understanding of your organization's redirect URL requirements

**Planning considerations:**

- **Message strategy**: Define the tone, length, and specific information to include in thank you messages
- **Redirect strategy**: Identify target pages and ensure they're optimized for post-form completion experiences
- **Analytics integration**: Plan how to track user interactions with thank you messages or redirect destinations

## Configure Thank You Messages

Thank you messages provide immediate acknowledgment of successful form submission and can include personalized content, next steps, or important information relevant to the user's submission.

### When to Use Thank You Messages

Thank you messages work best when:

- **Simple acknowledgment**: Users need confirmation without additional navigation requirements
- **Instructional content**: You need to provide specific next steps or important information
- **Brand consistency**: The message can be crafted to align with your organization's communication style
- **Single-page experience**: Users should remain on the current page for workflow continuity

### Implementation Steps

**1. Access form properties**

Open your Adaptive Form in Universal Editor and click the **Edit Form Properties** icon in the toolbar. This opens the comprehensive form properties dialog.

**2. Navigate to thank you configuration**

In the Form Properties dialog, select the **Thank You** tab to access post-submission configuration options.

**3. Configure message display**

Select **Show Message** from the available options. This activates the message content editor with rich text capabilities.

**4. Create your message content**

In the **Message content** field, craft your thank you message using the rich text editor. The editor supports:

- **Text formatting**: Bold, italic, underline, and color options
- **Lists**: Bulleted and numbered lists for organizing information
- **Links**: Direct links to relevant resources or next steps
- **Full-screen editing**: Click the expand icon for a larger editing workspace

### Technical Considerations

**Message display behavior:**

- Messages appear in a modal overlay immediately after form submission
- Content supports HTML formatting and maintains responsive design
- Messages can be dismissed by users or configured with auto-close timers

**Content guidelines:**

- Keep messages concise while providing necessary information
- Include clear next steps when appropriate
- Consider including reference numbers or confirmation details
- Ensure mobile-friendly formatting

### Example Implementation

        Thank you for your submission!

        Your application has been received and assigned reference number #REF-2024-001234.

        **What happens next:**
        - You will receive a confirmation email within 15 minutes
        - Our team will review your submission within 2 business days
        - We will contact you directly if additional information is needed

        **Need assistance?** Contact our support team at support@example.com 

## Configure Redirect URLs

Redirect URLs automatically navigate users to specific pages after form submission, enabling seamless integration with existing workflows or directing users to relevant content.

### When to Use Redirect URLs

Redirect URLs are optimal for:

- **Workflow integration**: Directing users to dashboards, account pages, or next steps in a process
- **Content delivery**: Showcasing relevant products, services, or information based on form responses
- **Analytics tracking**: Directing to pages with specific tracking implementations
- **Multi-step processes**: Moving users to the next phase of complex workflows

### Implementation Steps

**1. Access form properties**

Open your Adaptive Form in Universal Editor and click the **Edit Form Properties** icon to open the form configuration dialog.

**2. Navigate to thank you configuration**

Select the **Thank You** tab in the Form Properties dialog to access redirect configuration options.

**3. Enable redirect functionality**

Choose **Redirect to URL** from the available post-submission options.

**4. Configure destination URL**

Enter your target URL in the provided field. The system supports multiple URL formats for flexible implementation.

### URL Configuration Options

**Absolute URLs**

Complete web addresses including protocol and domain:

        https://www.example.com/thank-you
        https://dashboard.example.com/user/profile

**Relative Paths**

Paths relative to your current domain:

        /thank-you
        /dashboard/user-profile
        ../confirmation-page.html

**AEM Sites Page References**

References to other pages within your AEM Sites implementation:

        /content/mysite/en/thank-you
        /content/mysite/en/next-steps

### Technical Considerations

**Redirect behavior:**

- Redirects occur immediately after successful form submission
- Browser history includes the redirect for proper back-button functionality
- Redirect timing can be configured with optional delays

**URL validation:**

- System validates URL format before allowing configuration
- Relative URLs are resolved against the current domain
- External URLs require proper CORS configuration if needed

## Best Practices and Recommendations

### User Experience Guidelines

**Message optimization:**

- **Clarity first**: Ensure users immediately understand their submission was successful
- **Value addition**: Provide information that helps users with next steps
- **Consistent branding**: Maintain your organization's voice and visual style
- **Mobile consideration**: Test messages on various screen sizes

**Redirect optimization:**

- **Page optimization**: Ensure redirect destinations are optimized for post-form visitors
- **Loading performance**: Verify redirect pages load quickly to maintain user experience
- **Content relevance**: Make sure redirect content is relevant to the form context

### Security Considerations

**URL validation:**

- Implement proper validation for redirect URLs to prevent malicious redirects
- Consider whitelist approaches for allowed redirect domains
- Monitor redirect patterns for unusual activity

**Content security:**

- Sanitize thank you message content to prevent script injection
- Implement proper content security policies for rich text content
- Regular security reviews of redirect destinations

### Analytics and Tracking

**Implementation considerations:**

- **Goal tracking**: Set up analytics goals for both thank you message views and redirect completions
- **User journey mapping**: Track how users interact with post-submission experiences
- **Conversion optimization**: A/B test different thank you messages and redirect destinations

**Measurement strategies:**

- Monitor time spent on thank you messages before dismissal
- Track click-through rates for links within thank you messages
- Analyze user behavior on redirect destination pages

## Validation Checkpoints

After configuring your post-submission experience:

**Configuration verification:**

- Form properties correctly show selected thank you option
- Message content displays properly in preview mode
- Redirect URLs are properly formatted and accessible
- All links within messages function correctly

**User experience testing:**

- Submit test forms to verify proper thank you message display
- Test redirect functionality across different browsers
- Verify mobile responsiveness of thank you messages
- Confirm redirect destinations load properly

**Analytics setup:**

- Tracking codes properly implemented for thank you messages
- Redirect destination tracking configured
- Goal completion events properly firing

## Next Steps

After successfully configuring your post-submission experience:

- **Monitor performance**: Review analytics to understand user engagement with thank you messages or redirect pages
- **Iterate and improve**: Use user feedback and data insights to refine your post-submission strategy
- **Scale implementation**: Apply successful patterns across other forms in your organization

**Related documentation:**

- [Form submission configuration guide](submit-action.md)
- [User experience best practices](responsive-layout.md)

