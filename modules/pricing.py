"""
Pricing Module
Defines pricing plans and related helpers.
"""

from typing import List, Dict, Any, Optional

PRICING_PLANS = [
    {
        "id": "free",
        "name": "Free",
        "tagline": "Perfect for exploration and learning",
        "price_monthly": 0,
        "price_yearly": 0,
        "currency": "USD",
        "highlighted": False,
        "features": [
            "Access to 20+ base models",
            "10,000 tokens / day",
            "5 image generations / day",
            "Community support",
            "Basic analytics",
            "Rate limit: 20 RPM",
        ],
        "limits": {
            "tokens_per_day": 10000,
            "images_per_day": 5,
            "requests_per_minute": 20,
            "max_context": 4096,
            "team_members": 1,
        },
        "cta": "Get Started Free",
        "cta_url": "/contact",
    },
    {
        "id": "pro",
        "name": "Pro",
        "tagline": "For professionals and growing teams",
        "price_monthly": 49,
        "price_yearly": 470,
        "currency": "USD",
        "highlighted": True,
        "badge": "Most Popular",
        "features": [
            "Access to 150+ models",
            "2,000,000 tokens / month",
            "500 image generations / month",
            "Priority email support",
            "Advanced analytics dashboard",
            "Rate limit: 120 RPM",
            "Fine-tuning on selected models",
            "Custom system prompts",
            "API access with higher quotas",
        ],
        "limits": {
            "tokens_per_month": 2000000,
            "images_per_month": 500,
            "requests_per_minute": 120,
            "max_context": 32768,
            "team_members": 5,
        },
        "cta": "Start Pro Trial",
        "cta_url": "/contact",
    },
    {
        "id": "business",
        "name": "Business",
        "tagline": "Advanced features for organizations",
        "price_monthly": 199,
        "price_yearly": 1910,
        "currency": "USD",
        "highlighted": False,
        "features": [
            "Access to all 200+ models",
            "15,000,000 tokens / month",
            "3,000 image generations / month",
            "Dedicated support channel",
            "Full analytics + exports",
            "Rate limit: 500 RPM",
            "Custom model fine-tuning",
            "SSO / SAML authentication",
            "Team workspaces",
            "Usage alerts & budgets",
            "SLA 99.5%",
        ],
        "limits": {
            "tokens_per_month": 15000000,
            "images_per_month": 3000,
            "requests_per_minute": 500,
            "max_context": 128000,
            "team_members": 25,
        },
        "cta": "Contact Sales",
        "cta_url": "/contact",
    },
    {
        "id": "enterprise",
        "name": "Enterprise",
        "tagline": "Custom solutions at scale",
        "price_monthly": None,
        "price_yearly": None,
        "currency": "USD",
        "highlighted": False,
        "badge": "Custom",
        "features": [
            "Unlimited model access",
            "Custom token volumes",
            "Unlimited image generation",
            "24/7 dedicated support + TAM",
            "Custom analytics & reporting",
            "Custom rate limits",
            "On-premise / VPC deployment options",
            "Advanced security & compliance",
            "Custom model training",
            "Multi-region deployments",
            "SLA 99.9%+",
            "Legal review of terms",
        ],
        "limits": {
            "tokens_per_month": "Custom",
            "images_per_month": "Custom",
            "requests_per_minute": "Custom",
            "max_context": "Up to 1M+",
            "team_members": "Unlimited",
        },
        "cta": "Talk to Sales",
        "cta_url": "/contact",
    },
]


def get_pricing_plans() -> List[Dict[str, Any]]:
    """Return all pricing plans."""
    return PRICING_PLANS.copy()


def get_plan_details(plan_id: str) -> Optional[Dict[str, Any]]:
    """Return details for a specific plan."""
    for plan in PRICING_PLANS:
        if plan["id"] == plan_id:
            return plan.copy()
    return None


def compare_plans(plan_ids: List[str]) -> List[Dict[str, Any]]:
    """Return selected plans for comparison."""
    return [p for p in PRICING_PLANS if p["id"] in plan_ids]


def get_recommended_plan(monthly_tokens: int, team_size: int = 1) -> str:
    """Simple recommendation logic based on usage."""
    if monthly_tokens < 50000 and team_size <= 1:
        return "free"
    if monthly_tokens < 3000000 and team_size <= 5:
        return "pro"
    if monthly_tokens < 20000000 and team_size <= 25:
        return "business"
    return "enterprise"
