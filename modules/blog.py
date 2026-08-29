"""
Blog Module
Mock blog posts and categories for the AI Platform Hub news section.
"""

from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta

BLOG_CATEGORIES = [
    "Product Updates",
    "AI Research",
    "Tutorials",
    "Company News",
    "Industry Insights",
    "Case Studies",
]

_POSTS: List[Dict[str, Any]] = []


def _generate_posts():
    """Generate a set of mock blog posts."""
    global _POSTS
    if _POSTS:
        return
    
    titles = [
        ("Introducing AI Platform Hub 1.0", "Product Updates"),
        ("How Large Language Models Are Changing Software Development", "AI Research"),
        ("Getting Started with the Chat API in 5 Minutes", "Tutorials"),
        ("Our Journey Building a Multi-Model AI Marketplace", "Company News"),
        ("The State of Multimodal AI in 2026", "Industry Insights"),
        ("Case Study: How Acme Corp Reduced Support Costs by 40%", "Case Studies"),
        ("New Vision Models Now Available", "Product Updates"),
        ("Understanding Context Windows and Why They Matter", "Tutorials"),
        ("Fine-Tuning Best Practices for Production", "AI Research"),
        ("AI Platform Hub Raises Series A", "Company News"),
        ("Comparing Open-Source vs Proprietary LLMs", "Industry Insights"),
        ("Building a Customer Support Bot with Our Platform", "Case Studies"),
        ("Image Generation Studio: Tips for Better Prompts", "Tutorials"),
        ("Safety and Alignment in Modern AI Systems", "AI Research"),
        ("Announcing Business and Enterprise Plans", "Product Updates"),
        ("The Rise of Edge AI Deployment", "Industry Insights"),
        ("How We Process 20M+ API Calls Daily", "Company News"),
        ("Text Analysis Deep Dive: Sentiment to Topics", "Tutorials"),
        ("Benchmarking the Latest Code Generation Models", "AI Research"),
        ("Partner Spotlight: Integrating with Leading Cloud Providers", "Company News"),
        ("Cost Optimization Strategies for AI Workloads", "Industry Insights"),
        ("From Prototype to Production: A Complete Guide", "Tutorials"),
        ("Responsible AI: Our Principles and Practices", "Company News"),
        ("What Developers Want from AI Platforms in 2026", "Industry Insights"),
        ("Realtime Analytics Dashboard Now Live", "Product Updates"),
    ]
    
    authors = ["Alex Rivera", "Jordan Lee", "Sam Patel", "Morgan Chen", "Taylor Brooks", "Casey Nguyen"]
    
    for i, (title, category) in enumerate(titles):
        slug = title.lower().replace(" ", "-").replace(":", "").replace(",", "").replace("?", "")[:60]
        days_ago = len(titles) - i
        _POSTS.append({
            "id": f"post-{i+1:03d}",
            "title": title,
            "slug": slug,
            "category": category,
            "author": authors[i % len(authors)],
            "excerpt": (
                f"In this article we explore {title.lower()}. "
                f"Discover key insights, practical tips, and how AI Platform Hub "
                f"helps teams leverage the latest advancements in artificial intelligence."
            ),
            "content": (
                f"# {title}\\n\\n"
                f"Published in *{category}*\\n\\n"
                f"## Introduction\\n\\n"
                f"Welcome to this in-depth look at {title.lower()}. "
                f"The AI landscape continues to evolve rapidly, and staying informed "
                f"is essential for developers, researchers, and business leaders alike.\\n\\n"
                f"## Key Takeaways\\n\\n"
                f"- Understanding the latest model capabilities\\n"
                f"- Practical implementation strategies\\n"
                f"- Cost and performance considerations\\n"
                f"- Real-world examples and lessons learned\\n\\n"
                f"## Deep Dive\\n\\n"
                f"Over the past year, we have seen remarkable progress in foundation models. "
                f"From improved reasoning abilities to more efficient architectures, "
                f"the tools available to builders have never been more powerful.\\n\\n"
                f"AI Platform Hub brings these capabilities together in a single, "
                f"unified interface with transparent pricing and robust APIs.\\n\\n"
                f"## Getting Started\\n\\n"
                f"Whether you are experimenting with a new prototype or scaling an "
                f"existing application, our documentation and interactive tools "
                f"make it easy to get productive quickly.\\n\\n"
                f"## Conclusion\\n\\n"
                f"We hope this article provided valuable insights. "
                f"Stay tuned for more updates and feel free to reach out via our contact page."
            ),
            "published_at": (datetime(2025, 6, 1) + timedelta(days=days_ago * 4)).strftime("%Y-%m-%d"),
            "read_time_minutes": 4 + (i % 8),
            "tags": [category.lower().replace(" ", "-"), "ai", "platform"],
            "featured": i < 3,
        })


def get_all_posts() -> List[Dict[str, Any]]:
    """Return all blog posts sorted by date descending."""
    _generate_posts()
    return sorted(_POSTS, key=lambda p: p["published_at"], reverse=True)


def get_post_by_slug(slug: str) -> Optional[Dict[str, Any]]:
    """Retrieve a post by its slug."""
    _generate_posts()
    for post in _POSTS:
        if post["slug"] == slug:
            return post.copy()
    return None


def get_categories() -> List[str]:
    """Return blog categories."""
    return BLOG_CATEGORIES.copy()


def get_featured_posts(limit: int = 3) -> List[Dict[str, Any]]:
    """Return featured posts."""
    _generate_posts()
    return [p for p in _POSTS if p.get("featured")][:limit]


def get_posts_by_category(category: str) -> List[Dict[str, Any]]:
    """Filter posts by category."""
    _generate_posts()
    return [p for p in _POSTS if p["category"] == category]
