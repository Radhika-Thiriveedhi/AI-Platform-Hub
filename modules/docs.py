"""
Documentation Module
Provides structured documentation content for the docs section.
"""

from typing import List, Dict, Any, Optional

DOCS_SECTIONS = [
    {
        "id": "getting-started",
        "title": "Getting Started",
        "pages": [
            {"id": "introduction", "title": "Introduction"},
            {"id": "quickstart", "title": "Quickstart Guide"},
            {"id": "authentication", "title": "Authentication"},
            {"id": "first-request", "title": "Making Your First Request"},
        ],
    },
    {
        "id": "models",
        "title": "Models",
        "pages": [
            {"id": "overview", "title": "Models Overview"},
            {"id": "selection", "title": "Choosing the Right Model"},
            {"id": "parameters", "title": "Model Parameters"},
            {"id": "benchmarks", "title": "Benchmarks Explained"},
        ],
    },
    {
        "id": "api",
        "title": "API Reference",
        "pages": [
            {"id": "chat", "title": "Chat Completions"},
            {"id": "images", "title": "Image Generation"},
            {"id": "analysis", "title": "Text Analysis"},
            {"id": "embeddings", "title": "Embeddings"},
            {"id": "errors", "title": "Error Codes"},
        ],
    },
    {
        "id": "guides",
        "title": "Guides",
        "pages": [
            {"id": "prompt-engineering", "title": "Prompt Engineering"},
            {"id": "fine-tuning", "title": "Fine-Tuning Models"},
            {"id": "streaming", "title": "Streaming Responses"},
            {"id": "rate-limits", "title": "Understanding Rate Limits"},
            {"id": "best-practices", "title": "Best Practices"},
        ],
    },
    {
        "id": "platform",
        "title": "Platform",
        "pages": [
            {"id": "dashboard", "title": "Using the Dashboard"},
            {"id": "billing", "title": "Billing & Usage"},
            {"id": "teams", "title": "Team Management"},
            {"id": "security", "title": "Security & Compliance"},
        ],
    },
]


# Content templates for each page
_PAGE_CONTENT = {}


def _build_content():
    """Populate documentation page content."""
    global _PAGE_CONTENT
    if _PAGE_CONTENT:
        return
    
    for section in DOCS_SECTIONS:
        for page in section["pages"]:
            key = f"{section['id']}/{page['id']}"
            _PAGE_CONTENT[key] = {
                "section_id": section["id"],
                "section_title": section["title"],
                "page_id": page["id"],
                "title": page["title"],
                "content": (
                    f"# {page['title']}\\n\\n"
                    f"Welcome to the **{page['title']}** documentation page "
                    f"within the *{section['title']}* section.\\n\\n"
                    f"## Overview\\n\\n"
                    f"This page covers everything you need to know about {page['title'].lower()} "
                    f"on the AI Platform Hub. Whether you are just getting started or looking "
                    f"for advanced configuration options, you will find practical guidance here.\\n\\n"
                    f"## Key Concepts\\n\\n"
                    f"- Core principles and terminology\\n"
                    f"- Step-by-step instructions\\n"
                    f"- Code examples and sample requests\\n"
                    f"- Common pitfalls and how to avoid them\\n\\n"
                    f"## Example\\n\\n"
                    f"```python\\n"
                    f"from ai_platform_hub import Client\\n\\n"
                    f"client = Client(api_key='your-api-key')\\n"
                    f"response = client.chat.create(\\n"
                    f"    model='recommended-model',\\n"
                    f"    messages=[{{'role': 'user', 'content': 'Hello!'}}]\\n"
                    f")\\n"
                    f"print(response.choices[0].message.content)\\n"
                    f"```\\n\\n"
                    f"## Next Steps\\n\\n"
                    f"Continue exploring the documentation or head over to the interactive "
                    f"tools (Chat, Image Studio, Text Analysis) to try things out hands-on.\\n\\n"
                    f"If you have questions, visit the FAQ or contact our support team."
                ),
                "last_updated": "2026-03-15",
            }


def get_docs_sections() -> List[Dict[str, Any]]:
    """Return the documentation table of contents."""
    return DOCS_SECTIONS.copy()


def get_doc_page(section: str, page: str) -> Optional[Dict[str, Any]]:
    """Retrieve a specific documentation page."""
    _build_content()
    key = f"{section}/{page}"
    return _PAGE_CONTENT.get(key)
