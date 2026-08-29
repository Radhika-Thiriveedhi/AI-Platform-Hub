"""
Chat Engine Module
Mock conversational AI engine for the chat interface.
Handles message processing, history management, and response generation.
"""

from typing import List, Dict, Any, Optional
from datetime import datetime
import random
import hashlib

# In-memory chat history (session-scoped for demo purposes)
_CHAT_HISTORY: List[Dict[str, Any]] = []

# Predefined response templates for different query types
RESPONSE_TEMPLATES = {
    "greeting": [
        "Hello! Welcome to AI Platform Hub. How can I assist you with AI models and tools today?",
        "Hi there! I'm the AI Platform assistant. Ask me about models, pricing, or how to get started.",
        "Greetings! Ready to explore the world of artificial intelligence platforms with you.",
    ],
    "models": [
        "We currently host over 200 AI models across 15 categories including LLMs, computer vision, and multimodal systems. You can browse them in the Models section.",
        "Our catalog features models from leading providers like OpenAI, Anthropic, Google, Meta, Mistral, and many others. Would you like recommendations based on your use case?",
        "Popular models right now include high-parameter language models for reasoning, specialized code generation models, and efficient edge-deployable vision models.",
    ],
    "pricing": [
        "We offer flexible pricing: Free tier for experimentation, Pro for professionals, and Enterprise for organizations. Visit the Pricing page for full details.",
        "Token-based pricing starts as low as $0.0001 per 1K tokens depending on the model. Volume discounts and reserved capacity are available for enterprise customers.",
        "You can compare plans side-by-side on our Pricing page. Most users start with the Free tier and upgrade as their usage grows.",
    ],
    "help": [
        "I can help you with: browsing AI models, understanding pricing, generating images, analyzing text, or navigating the documentation.",
        "Try asking about specific model categories, how to use the chat API, image generation styles, or dashboard analytics.",
        "For detailed guides, check out the Documentation section. I'm also here for quick questions!",
    ],
    "image": [
        "Our Image Generation Studio supports multiple artistic styles including realistic, anime, digital art, oil painting, and more. Just describe what you want!",
        "You can generate images by providing a detailed prompt and selecting a style. Results appear instantly in the studio interface.",
        "Image generation is available on Pro and Enterprise plans. Free users get a limited number of generations per day.",
    ],
    "default": [
        "That's an interesting question. Based on our AI platform capabilities, I'd recommend exploring the relevant section of the site for more details.",
        "I understand you're asking about that topic. Our platform provides tools and models that can help address similar use cases.",
        "Thanks for your message. While I'm a mock assistant for demonstration, the full platform offers comprehensive AI services for that need.",
        "Great point! You might find the Analytics Dashboard or Model Comparison tools useful for diving deeper into that area.",
        "I've noted your query. For production use cases, our Enterprise plan includes dedicated support and custom model fine-tuning options.",
    ],
}

SYSTEM_PROMPTS = [
    "You are a helpful AI assistant for the AI Platform Hub website.",
    "Provide concise, accurate information about AI models and platform features.",
    "Be friendly and professional in all responses.",
]


def _detect_intent(message: str) -> str:
    """Simple keyword-based intent detection."""
    msg = message.lower()
    if any(w in msg for w in ["hello", "hi", "hey", "greetings", "good morning", "good afternoon"]):
        return "greeting"
    if any(w in msg for w in ["model", "llm", "catalog", "which model", "recommend"]):
        return "models"
    if any(w in msg for w in ["price", "pricing", "cost", "plan", "subscription", "free tier"]):
        return "pricing"
    if any(w in msg for w in ["help", "how to", "guide", "documentation", "docs"]):
        return "help"
    if any(w in msg for w in ["image", "generate image", "picture", "art", "draw"]):
        return "image"
    return "default"


def _generate_response(message: str, intent: str) -> str:
    """Generate a mock response based on detected intent."""
    templates = RESPONSE_TEMPLATES.get(intent, RESPONSE_TEMPLATES["default"])
    base = random.choice(templates)
    
    # Add a touch of personalization
    if len(message) > 20:
        base += f" Regarding '{message[:60]}{'...' if len(message) > 60 else ''}', feel free to explore related tools on the platform."
    
    return base


def process_chat_message(message: str) -> Dict[str, Any]:
    """
    Process an incoming chat message and return a structured response.
    
    Args:
        message: The user's input text.
        
    Returns:
        Dictionary containing response text, timestamp, intent, and metadata.
    """
    if not message or not message.strip():
        return {
            "error": "Message cannot be empty",
            "status": "error",
        }
    
    cleaned = message.strip()[:2000]  # Limit length
    intent = _detect_intent(cleaned)
    response_text = _generate_response(cleaned, intent)
    
    user_entry = {
        "role": "user",
        "content": cleaned,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "id": hashlib.md5(f"user-{cleaned}-{datetime.utcnow()}".encode()).hexdigest()[:12],
    }
    
    assistant_entry = {
        "role": "assistant",
        "content": response_text,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "id": hashlib.md5(f"asst-{response_text}-{datetime.utcnow()}".encode()).hexdigest()[:12],
        "intent": intent,
        "model": "ai-platform-hub-assistant-v1",
    }
    
    _CHAT_HISTORY.append(user_entry)
    _CHAT_HISTORY.append(assistant_entry)
    
    # Keep history manageable
    if len(_CHAT_HISTORY) > 100:
        _CHAT_HISTORY[:] = _CHAT_HISTORY[-100:]
    
    return {
        "status": "success",
        "response": response_text,
        "intent": intent,
        "timestamp": assistant_entry["timestamp"],
        "message_id": assistant_entry["id"],
        "history_length": len(_CHAT_HISTORY),
    }


def get_chat_history() -> List[Dict[str, Any]]:
    """Return a copy of the current chat history."""
    return _CHAT_HISTORY.copy()


def clear_chat_history() -> None:
    """Clear all chat history."""
    _CHAT_HISTORY.clear()


def get_chat_stats() -> Dict[str, Any]:
    """Return statistics about the current chat session."""
    user_msgs = [m for m in _CHAT_HISTORY if m["role"] == "user"]
    asst_msgs = [m for m in _CHAT_HISTORY if m["role"] == "assistant"]
    return {
        "total_messages": len(_CHAT_HISTORY),
        "user_messages": len(user_msgs),
        "assistant_messages": len(asst_msgs),
        "intents_used": list(set(m.get("intent") for m in asst_msgs if m.get("intent"))),
    }


def export_chat_transcript() -> str:
    """Export chat history as a readable transcript."""
    lines = ["AI Platform Hub - Chat Transcript", "=" * 40, ""]
    for msg in _CHAT_HISTORY:
        role = "You" if msg["role"] == "user" else "Assistant"
        lines.append(f"[{msg['timestamp']}] {role}:")
        lines.append(msg["content"])
        lines.append("")
    return "\\n".join(lines)


# Additional helpers for extended chat features
def get_suggested_prompts() -> List[str]:
    """Return a list of suggested starter prompts."""
    return [
        "What are the best models for code generation?",
        "Explain the difference between Free and Pro plans",
        "How do I generate an image with a specific style?",
        "Show me top-rated large language models",
        "What vision models are available?",
        "How does the text analysis tool work?",
        "Tell me about enterprise features",
        "What is the context length of the largest models?",
    ]


def simulate_streaming_response(message: str) -> List[str]:
    """
    Simulate a streaming response by breaking it into chunks.
    Useful for frontend streaming UI demos.
    """
    full = process_chat_message(message)["response"]
    words = full.split()
    chunks = []
    current = ""
    for word in words:
        current += word + " "
        if len(current) > 30 or word == words[-1]:
            chunks.append(current.strip())
            current = ""
    return chunks
