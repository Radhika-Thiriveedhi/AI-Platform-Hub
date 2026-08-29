"""
Image Generation Module
Mock image generation studio backend.
Provides styles, prompt processing, and generation simulation.
"""

from typing import List, Dict, Any, Optional
from datetime import datetime
import random
import hashlib

# In-memory recent generations store
_RECENT_GENERATIONS: List[Dict[str, Any]] = []

IMAGE_STYLES = [
    {
        "id": "realistic",
        "name": "Photorealistic",
        "description": "Highly detailed photorealistic images with natural lighting and textures.",
        "preview_color": "#4A90D9",
    },
    {
        "id": "anime",
        "name": "Anime / Manga",
        "description": "Japanese animation style with vibrant colors and expressive characters.",
        "preview_color": "#E91E63",
    },
    {
        "id": "digital-art",
        "name": "Digital Art",
        "description": "Modern digital illustration with clean lines and bold compositions.",
        "preview_color": "#9C27B0",
    },
    {
        "id": "oil-painting",
        "name": "Oil Painting",
        "description": "Classic oil painting aesthetic with visible brush strokes and rich colors.",
        "preview_color": "#FF9800",
    },
    {
        "id": "watercolor",
        "name": "Watercolor",
        "description": "Soft watercolor painting style with flowing colors and delicate details.",
        "preview_color": "#00BCD4",
    },
    {
        "id": "cyberpunk",
        "name": "Cyberpunk",
        "description": "Futuristic neon-lit cyberpunk aesthetic with high contrast and tech elements.",
        "preview_color": "#FF1744",
    },
    {
        "id": "fantasy",
        "name": "Fantasy Art",
        "description": "Epic fantasy illustration with magical elements and dramatic lighting.",
        "preview_color": "#7C4DFF",
    },
    {
        "id": "minimalist",
        "name": "Minimalist",
        "description": "Clean minimalist design with simple shapes and limited color palettes.",
        "preview_color": "#607D8B",
    },
    {
        "id": "3d-render",
        "name": "3D Render",
        "description": "High-quality 3D rendered scenes with realistic materials and lighting.",
        "preview_color": "#009688",
    },
    {
        "id": "pixel-art",
        "name": "Pixel Art",
        "description": "Retro pixel art style reminiscent of classic video games.",
        "preview_color": "#8BC34A",
    },
    {
        "id": "comic",
        "name": "Comic Book",
        "description": "Bold comic book style with strong outlines and halftone effects.",
        "preview_color": "#F44336",
    },
    {
        "id": "sketch",
        "name": "Pencil Sketch",
        "description": "Hand-drawn pencil sketch with shading and artistic line work.",
        "preview_color": "#795548",
    },
]


def get_image_styles() -> List[Dict[str, Any]]:
    """Return all available image generation styles."""
    return IMAGE_STYLES.copy()


def get_style_by_id(style_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve a style by its ID."""
    for style in IMAGE_STYLES:
        if style["id"] == style_id:
            return style.copy()
    return None


def generate_mock_image_prompt(prompt: str, style: str = "realistic") -> Dict[str, Any]:
    """
    Simulate image generation from a text prompt.
    
    In a real system this would call an image generation API.
    Here we return mock metadata and a placeholder result.
    """
    if not prompt or not prompt.strip():
        return {"error": "Prompt is required", "status": "error"}
    
    cleaned_prompt = prompt.strip()[:1000]
    style_obj = get_style_by_id(style) or IMAGE_STYLES[0]
    
    # Simulate processing time metadata
    seed = random.randint(10000, 99999)
    generation_id = hashlib.md5(f"{cleaned_prompt}-{style}-{seed}".encode()).hexdigest()[:16]
    
    result = {
        "status": "success",
        "generation_id": generation_id,
        "prompt": cleaned_prompt,
        "enhanced_prompt": f"{cleaned_prompt}, {style_obj['name'].lower()} style, highly detailed, professional quality",
        "style": style_obj["id"],
        "style_name": style_obj["name"],
        "seed": seed,
        "width": 1024,
        "height": 1024,
        "steps": 30,
        "guidance_scale": 7.5,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "placeholder_url": f"/static/images/placeholder_{style}.svg",
        "message": f"Image generated successfully in '{style_obj['name']}' style. (This is a mock generation for demonstration purposes.)",
        "estimated_cost": round(random.uniform(0.02, 0.15), 3),
    }
    
    # Store in recent generations
    _RECENT_GENERATIONS.insert(0, {
        "id": generation_id,
        "prompt": cleaned_prompt[:80],
        "style": style_obj["name"],
        "created_at": result["created_at"],
    })
    
    # Keep only last 20
    if len(_RECENT_GENERATIONS) > 20:
        _RECENT_GENERATIONS[:] = _RECENT_GENERATIONS[:20]
    
    return result


def get_recent_generations(limit: int = 10) -> List[Dict[str, Any]]:
    """Return recent image generation history."""
    return _RECENT_GENERATIONS[:limit]


def get_prompt_suggestions() -> List[str]:
    """Return example prompts for users."""
    return [
        "A serene mountain landscape at sunrise with misty valleys",
        "Futuristic city skyline with flying vehicles and neon lights",
        "A cozy coffee shop interior with warm lighting and plants",
        "Portrait of a wise old wizard with a glowing staff",
        "Abstract geometric patterns in vibrant complementary colors",
        "A cute robot watering flowers in a garden",
        "Underwater coral reef with colorful tropical fish",
        "Steampunk airship flying through cloudy skies",
        "Minimalist logo design for an AI technology company",
        "Epic space battle between starships near a nebula",
    ]


def validate_prompt(prompt: str) -> Dict[str, Any]:
    """Validate and provide feedback on a prompt."""
    if not prompt or len(prompt.strip()) < 3:
        return {"valid": False, "message": "Prompt is too short. Please provide more detail."}
    if len(prompt) > 1000:
        return {"valid": False, "message": "Prompt exceeds maximum length of 1000 characters."}
    
    word_count = len(prompt.split())
    feedback = []
    if word_count < 5:
        feedback.append("Consider adding more descriptive details for better results.")
    if word_count > 50:
        feedback.append("Very detailed prompt – great for precise control.")
    
    return {
        "valid": True,
        "word_count": word_count,
        "char_count": len(prompt),
        "feedback": feedback or ["Prompt looks good!"],
    }
