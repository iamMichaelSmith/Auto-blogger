# AI-Powered Content Workflow for Multiple Platforms

A comprehensive content generation and publishing pipeline that leverages web crawling, GPT content creation, and multi-platform publishing capabilities.

![Content Workflow](https://github.com/yourusername/crawler-app/blob/main/docs/workflow-diagram.png)

## 🚀 Features

- **Web Crawling**: Automatically crawl websites to gather topic inspiration and research
- **Content Generation**: Create high-quality blog posts using OpenAI's GPT models
- **Image Creation**: Generate relevant images with DALL-E 3
- **Multi-Platform Publishing**:
  - WordPress integration
  - Medium integration 
  - Notion integration
  - HTML output for custom websites
- **Local Image Management**: Download, convert, and store images for all platforms
- **Customizable Workflow**: Run individual steps or the entire pipeline

## 🔒 Security

**IMPORTANT: API Keys and Credentials Protection**

This project requires several API keys that should be kept secure:

- **OpenAI API Key**: Required for content generation and image creation
- **Zapier Webhook URLs**: Used for integration with publishing platforms
- **Notion, WordPress, and Medium credentials**: Used for direct publishing

To protect your sensitive information:

1. **Never commit `.env` files to GitHub**
   - A `.gitignore` file is included to prevent this
   - Use the `.env.example` as a template to create your own `.env` file locally

2. **Environment Variables**: 
   - Store all sensitive keys in environment variables
   - The application loads these from a `.env` file automatically

3. **Output Files**:
   - Generated content is stored in `workflow_output/` directory
   - This directory is excluded from Git in the `.gitignore` file

Set up your environment variables by copying the example file:
```bash
cp .env.example .env
# Then edit .env with your actual API keys
```

## 🔧 Components

The system consists of several key components:

### Core Workflow

- `workflow.py`: Main workflow manager that orchestrates the entire process
- `run_workflow.py`: CLI wrapper for running the workflow with various options
- `multi_business_workflow.py`: Extended workflow for handling multiple business verticals

### Data Collection

- `enhanced_crawler.py`: Web crawler with advanced data extraction capabilities
- `image_generator.py`: DALL-E 3 integration for image generation

### Publishing

- `webhook_sender_enhanced.py`: Multi-format content publishing tool 
- `push_article_direct.py`: Direct integration with platforms like Notion

## 📋 How It Works

1. **Web Crawling**: The system crawls specified websites to gather topic ideas and research data
2. **Topic Selection**: Analyzes the crawled data to suggest relevant blog topics
3. **Content Generation**: Uses OpenAI's GPT models to generate comprehensive, well-structured content
4. **Image Creation**: Generates relevant images using DALL-E 3
5. **Publishing**: Formats and publishes the content to selected platforms

## 💻 Usage

Basic usage examples:

```bash
# Run the full workflow
python run_workflow.py --word-count 1500 --topic "Digital Marketing Trends"

# Run only specific steps
python run_workflow.py --step 3 --non-interactive

# Generate and publish content to Notion
python webhook_sender_enhanced.py --format notion --download-images

# Generate and publish content to WordPress
python webhook_sender_enhanced.py --format wordpress --download-images
```

## 🔑 Requirements

- Python 3.8+
- OpenAI API key
- Zapier webhook URLs for integration
- Required libraries (see requirements.txt)

## 🔗 Integration

The system integrates with:

- **OpenAI**: For GPT content generation and DALL-E image creation
- **Zapier**: For webhook-based platform publishing
- **WordPress**: Direct publishing to WordPress sites
- **Medium**: Publishing articles to Medium
- **Notion**: Structured content publishing to Notion databases

## 📊 Future Enhancements

- SEO optimization capabilities
- Content analytics integration
- Automated social media promotion
- Sentiment analysis of generated content

## 🧪 Technical Implementation

The project uses a modular architecture with:

- **Environment variable management** for secure API key storage
- **Error handling and retry logic** for robust webhook delivery
- **Multi-format payload construction** for platform-specific requirements
- **Local file caching** for images and intermediate content
- **Non-interactive mode** for automated workflows

## 👥 Contributions

Contributions, ideas, and feedback are welcome! Feel free to open an issue or submit a pull request.

## 📝 License

[MIT License](LICENSE)

---

*Built with ❤️ for content creators and digital marketers* 