# Security Guide

This document outlines security best practices for using the AI Content Workflow system.

## API Key Protection

### OpenAI API Key

The OpenAI API key grants access to powerful AI models and can incur usage charges. Protect it by:

- **Storage**: Store it only in the `.env` file or system environment variables
- **Rotation**: Rotate keys periodically (every 30-90 days)
- **Access Control**: Limit the number of people with access to the key
- **Usage Monitoring**: Regularly check your OpenAI dashboard for unusual activity
- **Usage Limits**: Set usage limits in the OpenAI dashboard to prevent unexpected charges

### Webhook URLs

Zapier webhook URLs can be used to trigger automations and should be protected:

- **Treat as credentials**: Although webhook URLs don't provide direct access to your Zapier account, they should still be treated as sensitive
- **Regenerate when compromised**: If a webhook URL is exposed, recreate it in Zapier
- **Use backup URLs cautiously**: The application supports backup webhook URLs, ensure these are also kept secure

### Notion, WordPress, and Medium Credentials

Platform-specific credentials should be handled with care:

- **Token scope**: When generating API tokens, use the minimum permissions required
- **Separate accounts**: Consider using dedicated integration accounts rather than personal accounts
- **Audit regularly**: Review connected applications periodically

## File & Output Security

### Generated Content

The application generates content in the `workflow_output/` directory:

- **Local storage**: Content is stored locally and not sent anywhere unless explicitly triggered by a webhook
- **Sensitive information**: Be careful about generating content that might contain sensitive information
- **Clean-up**: Consider periodic clean-up of the output directory if not needed for long-term storage

### Image Files

Downloaded and generated images are stored locally:

- **Licensing**: Ensure you have the right to use any images found through crawling
- **Attribution**: Follow proper attribution requirements for any third-party content
- **Image metadata**: Be aware that some image files might contain metadata

## Code Security

### Dependencies

Keeping dependencies updated is critical for security:

- **Regular updates**: Run `pip install -r requirements.txt --upgrade` periodically
- **Vulnerability checks**: Consider using tools like `safety` to check for vulnerabilities:
  ```bash
  pip install safety
  safety check -r requirements.txt
  ```

### Environmental Isolation

Use virtual environments to isolate the application:

- **Dedicated environment**: Always run the application in its own virtual environment
- **Minimal permissions**: Run with the minimum required system permissions

## Deployment Security

If deploying the application in a production environment:

- **Dedicated user**: Create a dedicated user with minimal permissions
- **Firewall rules**: Implement appropriate firewall rules
- **Logging**: Enable comprehensive logging for security monitoring
- **Backups**: Maintain backups of configuration (but not sensitive credentials)

## Reporting Security Issues

If you discover a security vulnerability:

1. **Do not disclose publicly**: Avoid posting in public issues
2. **Report responsibly**: Contact the project maintainer directly
3. **Provide details**: Include steps to reproduce and potential impact

## Resources

- [OpenAI API Security Best Practices](https://platform.openai.com/docs/guides/safety-best-practices)
- [Zapier Webhook Security](https://zapier.com/help/create/basics/webhook-security-best-practices)
- [Python Security Best Practices](https://python-security.readthedocs.io/) 