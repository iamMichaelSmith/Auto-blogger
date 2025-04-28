```mermaid
graph TD
    A[Web Crawling] -->|Gather Research & Topics| B[Topic Selection]
    B -->|Selected Topic| C[GPT Content Generation]
    C -->|Generated Content| D[Image Creation with DALL-E]
    D -->|Content with Images| E[Format for Platforms]
    E -->|WordPress Format| F[WordPress Integration]
    E -->|Medium Format| G[Medium Integration]
    E -->|Notion Format| H[Notion Integration]
    E -->|HTML Format| I[Custom Website]
    
    subgraph "Data Collection"
    A
    B
    end
    
    subgraph "Content Creation"
    C
    D
    end
    
    subgraph "Publishing"
    E
    F
    G
    H
    I
    end
```

This diagram shows the workflow of the AI-powered content generation system:

1. **Data Collection Phase**: Web crawling gathers research data and potential topics, followed by intelligent topic selection.
2. **Content Creation Phase**: Content is generated using GPT models, and relevant images are created with DALL-E.
3. **Publishing Phase**: Content is formatted according to platform requirements and published to WordPress, Medium, Notion, or custom websites.

The modular design allows users to execute individual steps or the entire workflow automatically. 