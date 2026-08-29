"""
Analytics Module
Provides mock dashboard statistics, usage trends, and reporting data.
"""

from typing import List, Dict, Any
from datetime import datetime, timedelta
import random


def get_dashboard_stats() -> Dict[str, Any]:
    """Return high-level dashboard statistics."""
    return {
        "total_models": 200,
        "active_users": random.randint(12500, 18900),
        "api_calls_today": random.randint(450000, 890000),
        "api_calls_month": random.randint(12_000_000, 28_000_000),
        "images_generated": random.randint(85000, 150000),
        "chat_sessions": random.randint(32000, 58000),
        "avg_latency_ms": random.randint(120, 280),
        "uptime_percent": round(random.uniform(99.5, 99.99), 2),
        "revenue_mtd": round(random.uniform(125000, 340000), 2),
        "new_signups_week": random.randint(800, 2200),
        "storage_used_tb": round(random.uniform(45.2, 89.7), 1),
        "gpu_utilization": round(random.uniform(62.0, 91.5), 1),
    }


def get_usage_trends(days: int = 30) -> List[Dict[str, Any]]:
    """Generate mock daily usage trend data."""
    trends = []
    base_date = datetime.utcnow() - timedelta(days=days)
    base_calls = 400000
    
    for i in range(days):
        day = base_date + timedelta(days=i)
        # Simulate weekly patterns
        weekday_factor = 1.0 if day.weekday() < 5 else 0.65
        growth = 1 + (i * 0.008)
        noise = random.uniform(0.85, 1.15)
        
        calls = int(base_calls * weekday_factor * growth * noise)
        users = int(calls / random.uniform(25, 40))
        
        trends.append({
            "date": day.strftime("%Y-%m-%d"),
            "api_calls": calls,
            "active_users": users,
            "images": int(calls * random.uniform(0.08, 0.15)),
            "chat_messages": int(calls * random.uniform(0.12, 0.22)),
            "avg_latency": random.randint(100, 350),
            "error_rate": round(random.uniform(0.1, 1.8), 2),
        })
    return trends


def get_top_models(limit: int = 10) -> List[Dict[str, Any]]:
    """Return mock top models by usage."""
    names = [
        "GPT-Scale Reasoner", "Vision Pro XL", "CodeAssist Ultra",
        "Multimodal Fusion", "Speech Transcribe Max", "Embedder Large",
        "Chat Companion", "Image Dreamer", "Text Analyzer Pro",
        "Forecast Engine", "RL Agent Base", "Edge Vision Lite",
        "Doc Summarizer", "Translation Hub", "Safety Classifier",
    ]
    results = []
    for i, name in enumerate(names[:limit]):
        results.append({
            "rank": i + 1,
            "name": name,
            "requests": random.randint(50000, 2500000),
            "tokens": random.randint(10_000_000, 500_000_000),
            "avg_latency_ms": random.randint(80, 400),
            "success_rate": round(random.uniform(97.5, 99.9), 2),
            "category": random.choice(["LLM", "Vision", "Audio", "Multimodal", "Code"]),
        })
    return results


def get_category_distribution() -> List[Dict[str, Any]]:
    """Return usage distribution by category."""
    cats = [
        ("Large Language Models", 42.5),
        ("Computer Vision", 18.2),
        ("Multimodal", 12.8),
        ("Code Generation", 9.4),
        ("Speech & Audio", 7.1),
        ("Others", 10.0),
    ]
    return [{"category": c, "percentage": p, "requests": int(p * 100000)} for c, p in cats]


def get_error_breakdown() -> List[Dict[str, Any]]:
    """Return mock error type breakdown."""
    return [
        {"type": "Rate Limit Exceeded", "count": random.randint(1200, 3500), "percent": 34.2},
        {"type": "Invalid Request", "count": random.randint(800, 2200), "percent": 22.1},
        {"type": "Authentication Error", "count": random.randint(400, 1100), "percent": 12.8},
        {"type": "Model Overloaded", "count": random.randint(300, 900), "percent": 10.5},
        {"type": "Timeout", "count": random.randint(250, 700), "percent": 8.9},
        {"type": "Content Filter", "count": random.randint(200, 600), "percent": 7.2},
        {"type": "Other", "count": random.randint(100, 400), "percent": 4.3},
    ]


def get_geographic_distribution() -> List[Dict[str, Any]]:
    """Return mock geographic usage data."""
    return [
        {"region": "North America", "percentage": 38.5, "users": 6200},
        {"region": "Europe", "percentage": 27.2, "users": 4400},
        {"region": "Asia Pacific", "percentage": 22.8, "users": 3700},
        {"region": "Latin America", "percentage": 6.1, "users": 980},
        {"region": "Middle East & Africa", "percentage": 5.4, "users": 870},
    ]


def get_hourly_heatmap() -> List[Dict[str, Any]]:
    """Return mock hourly activity for heatmap visualization."""
    data = []
    for hour in range(24):
        for day in range(7):
            # Higher activity during business hours on weekdays
            base = 50
            if day < 5 and 9 <= hour <= 18:
                base = 180
            elif day < 5:
                base = 90
            else:
                base = 60
            data.append({
                "day": day,
                "hour": hour,
                "value": int(base * random.uniform(0.7, 1.3)),
            })
    return data
