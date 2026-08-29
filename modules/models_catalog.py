"""
AI Models Catalog Module
Provides comprehensive mock data and helper functions for the AI model marketplace.
This module contains a large catalog of AI models across multiple categories.
"""

from typing import List, Dict, Optional, Any
import random
from datetime import datetime, timedelta

# ==================== MODEL CATEGORIES ====================
CATEGORIES = [
    "Large Language Models",
    "Computer Vision",
    "Speech & Audio",
    "Multimodal",
    "Code Generation",
    "Recommendation Systems",
    "Time Series Forecasting",
    "Reinforcement Learning",
    "Generative Art",
    "Scientific Computing",
    "NLP Specialized",
    "Edge AI",
    "Robotics",
    "Healthcare AI",
    "Finance AI",
]

# ==================== PROVIDER LIST ====================
PROVIDERS = [
    "OpenAI", "Anthropic", "Google DeepMind", "Meta AI", "Mistral AI",
    "Cohere", "Stability AI", "Hugging Face", "Amazon", "Microsoft",
    "xAI", "Inflection", "Aleph Alpha", "AI21 Labs", "Together AI",
    "Fireworks AI", "Groq", "Perplexity", "Character.AI", "Replicate",
]

# ==================== MODEL GENERATION ====================
def _generate_model(idx: int) -> Dict[str, Any]:
    """Generate a single mock AI model entry with rich metadata."""
    category = CATEGORIES[idx % len(CATEGORIES)]
    provider = PROVIDERS[idx % len(PROVIDERS)]
    base_name = f"{provider.split()[0]}-{category.split()[0][:4]}-{idx:03d}"
    
    model = {
        "id": f"model-{idx:04d}",
        "name": f"{base_name}",
        "display_name": f"{provider} {category.split()[0]} Model v{idx % 10 + 1}.{idx % 5}",
        "provider": provider,
        "category": category,
        "description": (
            f"A state-of-the-art {category.lower()} model developed by {provider}. "
            f"This model excels at complex reasoning, multi-step tasks, and production workloads. "
            f"It supports long context windows, fine-tuning capabilities, and efficient inference. "
            f"Ideal for enterprise applications requiring high accuracy and reliability. "
            f"Version {idx % 10 + 1}.{idx % 5} introduces improved performance on benchmark tasks "
            f"and reduced latency for real-time applications."
        ),
        "long_description": (
            f"## Overview\n\n"
            f"The {base_name} is part of {provider}'s advanced AI model family focused on {category.lower()}. "
            f"Built on transformer architectures with novel attention mechanisms, this model delivers "
            f"exceptional results across a wide range of evaluation benchmarks.\n\n"
            f"## Key Capabilities\n\n"
            f"- Advanced multi-turn conversation handling\n"
            f"- Strong performance on reasoning and planning tasks\n"
            f"- Support for function calling and tool use\n"
            f"- Multilingual understanding across 50+ languages\n"
            f"- Efficient quantization options for deployment\n\n"
            f"## Technical Specifications\n\n"
            f"- Architecture: Transformer-based with mixture-of-experts layers\n"
            f"- Context Window: {8192 * (1 + idx % 8)} tokens\n"
            f"- Parameters: {random.choice(['7B', '13B', '34B', '70B', '175B', '405B'])}\n"
            f"- Training Data: Curated high-quality datasets up to 2025\n"
            f"- License: Commercial-friendly with usage tiers\n\n"
            f"## Use Cases\n\n"
            f"1. Customer support automation\n"
            f"2. Content generation and summarization\n"
            f"3. Code assistance and review\n"
            f"4. Data analysis and insight extraction\n"
            f"5. Research and scientific literature review\n"
        ),
        "version": f"{1 + idx % 5}.{idx % 10}.{idx % 3}",
        "release_date": (datetime(2023, 1, 1) + timedelta(days=idx * 7)).strftime("%Y-%m-%d"),
        "parameters": random.choice(["7B", "13B", "34B", "70B", "175B", "405B", "1T+"]),
        "context_length": 8192 * (1 + idx % 16),
        "price_per_1k_tokens": round(random.uniform(0.0001, 0.06), 5),
        "latency_ms": random.randint(50, 800),
        "throughput_tps": random.randint(20, 500),
        "rating": round(random.uniform(3.5, 5.0), 1),
        "reviews_count": random.randint(50, 5000),
        "tags": random.sample(
            ["chat", "completion", "embedding", "vision", "audio", "code", "reasoning",
             "multilingual", "fine-tuneable", "open-weights", "api", "self-host"],
            k=random.randint(3, 6)
        ),
        "benchmarks": {
            "mmlu": round(random.uniform(60, 95), 1),
            "humaneval": round(random.uniform(40, 92), 1),
            "gsm8k": round(random.uniform(50, 98), 1),
            "hellaswag": round(random.uniform(70, 96), 1),
            "arc": round(random.uniform(55, 94), 1),
        },
        "features": [
            "Streaming responses",
            "Function calling",
            "JSON mode",
            "System prompts",
            "Temperature control",
            "Top-p sampling",
            "Presence penalty",
            "Frequency penalty",
        ],
        "supported_formats": ["text", "json", "markdown"],
        "max_output_tokens": 4096 * (1 + idx % 4),
        "is_featured": idx < 12,
        "is_new": idx > 80,
        "is_open_source": idx % 3 == 0,
        "api_endpoint": f"https://api.aiplatformhub.example/v1/models/{base_name}",
        "documentation_url": f"/docs/models/{base_name}",
        "created_at": (datetime(2023, 1, 1) + timedelta(days=idx * 3)).isoformat(),
        "updated_at": (datetime(2025, 1, 1) + timedelta(days=idx)).isoformat(),
    }
    return model

# Pre-generate a large catalog (200 models)
_MODEL_CATALOG: List[Dict[str, Any]] = [_generate_model(i) for i in range(200)]


def get_all_models() -> List[Dict[str, Any]]:
    """Return the full list of AI models."""
    return _MODEL_CATALOG.copy()


def get_model_by_id(model_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve a single model by its unique ID."""
    for model in _MODEL_CATALOG:
        if model["id"] == model_id:
            return model.copy()
    return None


def search_models(query: str) -> List[Dict[str, Any]]:
    """Search models by name, description, provider, or tags."""
    query_lower = query.lower().strip()
    if not query_lower:
        return get_all_models()
    
    results = []
    for model in _MODEL_CATALOG:
        searchable = " ".join([
            model["name"],
            model["display_name"],
            model["provider"],
            model["category"],
            model["description"],
            " ".join(model["tags"]),
        ]).lower()
        if query_lower in searchable:
            results.append(model)
    return results


def get_categories() -> List[str]:
    """Return list of available model categories."""
    return CATEGORIES.copy()


def get_models_by_category(category: str) -> List[Dict[str, Any]]:
    """Filter models by category name."""
    return [m for m in _MODEL_CATALOG if m["category"] == category]


def get_models_by_provider(provider: str) -> List[Dict[str, Any]]:
    """Filter models by provider name."""
    return [m for m in _MODEL_CATALOG if m["provider"] == provider]


def get_featured_models(limit: int = 6) -> List[Dict[str, Any]]:
    """Return featured models."""
    featured = [m for m in _MODEL_CATALOG if m.get("is_featured")]
    return featured[:limit]


def get_new_models(limit: int = 10) -> List[Dict[str, Any]]:
    """Return recently added models."""
    new_ones = [m for m in _MODEL_CATALOG if m.get("is_new")]
    return sorted(new_ones, key=lambda x: x["created_at"], reverse=True)[:limit]


def get_top_rated_models(limit: int = 10) -> List[Dict[str, Any]]:
    """Return highest rated models."""
    sorted_models = sorted(_MODEL_CATALOG, key=lambda x: x["rating"], reverse=True)
    return sorted_models[:limit]


def get_open_source_models() -> List[Dict[str, Any]]:
    """Return models marked as open source."""
    return [m for m in _MODEL_CATALOG if m.get("is_open_source")]


def compare_models(model_ids: List[str]) -> List[Dict[str, Any]]:
    """Return models for comparison given a list of IDs."""
    return [get_model_by_id(mid) for mid in model_ids if get_model_by_id(mid)]


def get_model_stats() -> Dict[str, Any]:
    """Aggregate statistics about the model catalog."""
    return {
        "total_models": len(_MODEL_CATALOG),
        "total_categories": len(CATEGORIES),
        "total_providers": len(PROVIDERS),
        "avg_rating": round(sum(m["rating"] for m in _MODEL_CATALOG) / len(_MODEL_CATALOG), 2),
        "open_source_count": len(get_open_source_models()),
        "featured_count": len([m for m in _MODEL_CATALOG if m.get("is_featured")]),
    }


# Additional utility functions for extended functionality
def filter_models_by_price(max_price: float) -> List[Dict[str, Any]]:
    """Filter models under a given price per 1k tokens."""
    return [m for m in _MODEL_CATALOG if m["price_per_1k_tokens"] <= max_price]


def filter_models_by_context(min_context: int) -> List[Dict[str, Any]]:
    """Filter models with at least the specified context length."""
    return [m for m in _MODEL_CATALOG if m["context_length"] >= min_context]


def filter_models_by_parameters(param_sizes: List[str]) -> List[Dict[str, Any]]:
    """Filter models matching given parameter size labels."""
    return [m for m in _MODEL_CATALOG if m["parameters"] in param_sizes]


def get_models_sorted(sort_by: str = "rating", descending: bool = True) -> List[Dict[str, Any]]:
    """Return models sorted by a given field."""
    valid_fields = ["rating", "price_per_1k_tokens", "context_length", "latency_ms", "reviews_count"]
    if sort_by not in valid_fields:
        sort_by = "rating"
    return sorted(_MODEL_CATALOG, key=lambda x: x.get(sort_by, 0), reverse=descending)


def paginate_models(models: List[Dict], page: int = 1, per_page: int = 12) -> Dict[str, Any]:
    """Helper to paginate a list of models."""
    total = len(models)
    start = (page - 1) * per_page
    end = start + per_page
    return {
        "items": models[start:end],
        "page": page,
        "per_page": per_page,
        "total": total,
        "total_pages": (total + per_page - 1) // per_page if total > 0 else 0,
        "has_next": end < total,
        "has_prev": page > 1,
    }


# Benchmark comparison helpers
def get_average_benchmarks(category: Optional[str] = None) -> Dict[str, float]:
    """Compute average benchmark scores, optionally filtered by category."""
    models = get_models_by_category(category) if category else _MODEL_CATALOG
    if not models:
        return {}
    keys = ["mmlu", "humaneval", "gsm8k", "hellaswag", "arc"]
    averages = {}
    for key in keys:
        averages[key] = round(sum(m["benchmarks"][key] for m in models) / len(models), 2)
    return averages


def rank_models_by_benchmark(benchmark: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Rank models by a specific benchmark score."""
    valid = ["mmlu", "humaneval", "gsm8k", "hellaswag", "arc"]
    if benchmark not in valid:
        benchmark = "mmlu"
    sorted_models = sorted(
        _MODEL_CATALOG,
        key=lambda x: x["benchmarks"].get(benchmark, 0),
        reverse=True
    )
    return sorted_models[:limit]


# Export summary for debugging / admin
def export_catalog_summary() -> str:
    """Generate a text summary of the entire catalog."""
    lines = [
        "=" * 60,
        "AI PLATFORM HUB - MODEL CATALOG SUMMARY",
        "=" * 60,
        f"Total Models: {len(_MODEL_CATALOG)}",
        f"Categories: {len(CATEGORIES)}",
        f"Providers: {len(PROVIDERS)}",
        "",
        "Category Breakdown:",
    ]
    for cat in CATEGORIES:
        count = len(get_models_by_category(cat))
        lines.append(f"  - {cat}: {count} models")
    lines.append("")
    lines.append("Provider Breakdown:")
    for prov in PROVIDERS:
        count = len(get_models_by_provider(prov))
        lines.append(f"  - {prov}: {count} models")
    lines.append("=" * 60)
    return "\n".join(lines)
