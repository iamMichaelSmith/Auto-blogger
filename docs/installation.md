# Installation Guide

This guide will help you set up the AI Content Workflow system on your local machine.

## Prerequisites

- Python 3.8 or higher
- An OpenAI API key
- Zapier account with webhook capabilities (for integration)
- Notion API key (for direct Notion integration)

## Setup Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-content-workflow.git
cd ai-content-workflow
```

### 2. Create a Virtual Environment

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables (IMPORTANT)

⚠️ **SECURITY WARNING**: Never commit your actual API keys to GitHub or share them publicly.

Create a `.env` file in the root directory by copying the example file:

```bash
cp .env.example .env
```

Then edit the `.env` file with your actual API keys:

```
OPENAI_API_KEY=your_openai_api_key
ZAPIER_WEBHOOK_URL=your_zapier_webhook_url
NOTION_API_KEY=your_notion_api_key
```

The `.env` file is automatically excluded from Git via the `.gitignore` file to prevent accidental exposure of your credentials.

#### API Key Management Best Practices:

- Regularly rotate your API keys for better security
- Use environment-specific keys (development/production)
- Consider using API key management services for team environments
- Review API usage regularly to detect unauthorized access

### 5. Create Required Directories

```bash
mkdir -p workflow_output/images
mkdir -p workflow_output/articles
```

## Verify Installation

To verify that everything is set up correctly:

```bash
python test_webhook.py --create-test
```

This will create a test article and attempt to send it to your configured webhook.

## Troubleshooting

### Common Issues

1. **OpenAI API Key Not Working:**
   - Verify the key is correct and has sufficient credits
   - Check if the key has the necessary permissions

2. **Webhook Connection Failing:**
   - Verify your Zapier webhook URL is correct
   - Test the webhook directly using a tool like Postman

3. **Image Generation Not Working:**
   - Ensure your OpenAI API key has access to DALL-E
   - Check your Python environment for Pillow installation

### Getting Help

If you encounter issues not covered here, please:

1. Check the GitHub Issues section for similar problems
2. Create a new issue with detailed information about your setup and the error

## Next Steps

Once installation is complete, proceed to the [Usage Guide](usage.md) for instructions on running the workflow. 