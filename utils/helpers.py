"""
Utility helper functions used across the application.
"""

from typing import Any, Optional
import re
import unicodedata


def format_number(num: int | float, precision: int = 0) -> str:
    """Format a number with thousand separators."""
    if isinstance(num, float):
        return f"{num:,.{precision}f}"
    return f"{num:,}"


def truncate_text(text: str, max_length: int = 120, suffix: str = "...") -> str:
    """Truncate text to a maximum length, appending a suffix if needed."""
    if not text:
        return ""
    text = text.strip()
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)].rstrip() + suffix


def generate_slug(text: str) -> str:
    """Generate a URL-friendly slug from text."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9\\s-]", "", text)
    text = re.sub(r"[\\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def percentage(part: float, whole: float, decimals: int = 1) -> str:
    """Calculate and format a percentage."""
    if whole == 0:
        return "0%"
    return f"{round((part / whole) * 100, decimals)}%"


def clamp(value: float, min_val: float, max_val: float) -> float:
    """Clamp a value between min and max."""
    return max(min_val, min(max_val, value))


def safe_get(data: dict, *keys: str, default: Any = None) -> Any:
    """Safely traverse nested dictionaries."""
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def time_ago(iso_timestamp: str) -> str:
    """Very simple relative time formatter (for display)."""
    # For demo purposes return a static-ish relative string
    return "recently"


def stars_from_rating(rating: float) -> str:
    """Convert a 0-5 rating to a star string."""
    full = int(rating)
    half = 1 if rating - full >= 0.5 else 0
    empty = 5 - full - half
    return "★" * full + ("½" if half else "") + "☆" * empty


def bytes_to_human(num_bytes: int) -> str:
    """Convert bytes to human-readable string."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if abs(num_bytes) < 1024.0:
            return f"{num_bytes:.1f} {unit}"
        num_bytes /= 1024.0
    return f"{num_bytes:.1f} PB"


def merge_dicts(*dicts: dict) -> dict:
    """Shallow merge multiple dictionaries (later ones override)."""
    result = {}
    for d in dicts:
        if d:
            result.update(d)
    return result
