"""
Text Analysis Module
Provides mock NLP analysis capabilities: sentiment, entities, keywords, summary, etc.
"""

from typing import List, Dict, Any
from datetime import datetime
import re
import random
import hashlib

ANALYSIS_TYPES = [
    {
        "id": "sentiment",
        "name": "Sentiment Analysis",
        "description": "Detect the overall emotional tone of the text (positive, negative, neutral).",
        "icon": "😊",
    },
    {
        "id": "entities",
        "name": "Named Entity Recognition",
        "description": "Extract people, organizations, locations, and other entities from text.",
        "icon": "🏷️",
    },
    {
        "id": "keywords",
        "name": "Keyword Extraction",
        "description": "Identify the most important keywords and key phrases.",
        "icon": "🔑",
    },
    {
        "id": "summary",
        "name": "Text Summarization",
        "description": "Generate a concise summary of longer text content.",
        "icon": "📝",
    },
    {
        "id": "language",
        "name": "Language Detection",
        "description": "Detect the language(s) present in the text.",
        "icon": "🌐",
    },
    {
        "id": "readability",
        "name": "Readability Score",
        "description": "Calculate readability metrics and suggested audience level.",
        "icon": "📊",
    },
    {
        "id": "toxicity",
        "name": "Toxicity Detection",
        "description": "Flag potentially toxic, offensive, or harmful content.",
        "icon": "🛡️",
    },
    {
        "id": "topics",
        "name": "Topic Modeling",
        "description": "Identify main topics and themes present in the text.",
        "icon": "📚",
    },
]


def get_analysis_types() -> List[Dict[str, Any]]:
    """Return available analysis types."""
    return ANALYSIS_TYPES.copy()


def _simple_sentiment(text: str) -> Dict[str, Any]:
    """Rule-based mock sentiment analysis."""
    positive_words = {"good", "great", "excellent", "amazing", "love", "happy", "wonderful",
                      "fantastic", "best", "awesome", "positive", "beautiful", "perfect", "enjoy"}
    negative_words = {"bad", "terrible", "awful", "hate", "poor", "worst", "horrible",
                      "negative", "sad", "angry", "disappointed", "ugly", "fail", "problem"}
    
    words = set(re.findall(r"\\b\\w+\\b", text.lower()))
    pos = len(words & positive_words)
    neg = len(words & negative_words)
    
    if pos > neg:
        label = "positive"
        score = min(0.5 + (pos - neg) * 0.1, 0.98)
    elif neg > pos:
        label = "negative"
        score = min(0.5 + (neg - pos) * 0.1, 0.98)
    else:
        label = "neutral"
        score = 0.5 + random.uniform(-0.1, 0.1)
    
    return {
        "label": label,
        "score": round(score, 3),
        "positive_signals": pos,
        "negative_signals": neg,
    }


def _extract_entities(text: str) -> List[Dict[str, str]]:
    """Mock named entity extraction using simple patterns."""
    entities = []
    # Capitalized words as potential entities
    candidates = re.findall(r"\\b[A-Z][a-z]+(?:\\s[A-Z][a-z]+)*\\b", text)
    for c in candidates[:15]:
        entity_type = random.choice(["PERSON", "ORG", "LOCATION", "PRODUCT", "EVENT"])
        entities.append({"text": c, "type": entity_type, "confidence": round(random.uniform(0.7, 0.99), 2)})
    return entities


def _extract_keywords(text: str) -> List[Dict[str, Any]]:
    """Simple keyword extraction by word frequency."""
    stopwords = {"the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
                 "have", "has", "had", "do", "does", "did", "will", "would", "could",
                 "should", "may", "might", "must", "shall", "can", "need", "dare",
                 "ought", "used", "to", "of", "in", "for", "on", "with", "at", "by",
                 "from", "as", "into", "through", "during", "before", "after", "and",
                 "but", "or", "nor", "so", "yet", "both", "either", "neither", "not",
                 "only", "own", "same", "than", "too", "very", "just", "this", "that",
                 "these", "those", "it", "its", "i", "me", "my", "we", "our", "you", "your"}
    
    words = re.findall(r"\\b[a-z]{3,}\\b", text.lower())
    freq: Dict[str, int] = {}
    for w in words:
        if w not in stopwords:
            freq[w] = freq.get(w, 0) + 1
    
    sorted_kw = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:12]
    return [{"keyword": k, "score": round(v / max(len(words), 1), 3), "count": v} for k, v in sorted_kw]


def _summarize(text: str) -> str:
    """Mock extractive summary – take first few sentences."""
    sentences = re.split(r"(?<=[.!?])\\s+", text.strip())
    if len(sentences) <= 2:
        return text.strip()
    summary_len = max(1, len(sentences) // 3)
    return " ".join(sentences[:summary_len])


def _detect_language(text: str) -> Dict[str, Any]:
    """Mock language detection."""
    # Very naive – assume English for demo
    return {
        "primary": "en",
        "primary_name": "English",
        "confidence": round(random.uniform(0.85, 0.99), 3),
        "alternatives": [
            {"code": "es", "name": "Spanish", "confidence": round(random.uniform(0.01, 0.1), 3)},
            {"code": "fr", "name": "French", "confidence": round(random.uniform(0.01, 0.08), 3)},
        ],
    }


def _readability(text: str) -> Dict[str, Any]:
    """Mock readability metrics."""
    words = text.split()
    sentences = max(1, len(re.split(r"[.!?]+", text)))
    avg_words = len(words) / sentences
    # Simplified Flesch-like score
    score = max(0, min(100, 206.835 - 1.015 * avg_words - 84.6 * (len(text) / max(len(words), 1) / 4.7)))
    
    if score >= 90:
        level = "Very Easy (5th grade)"
    elif score >= 80:
        level = "Easy (6th grade)"
    elif score >= 70:
        level = "Fairly Easy (7th grade)"
    elif score >= 60:
        level = "Standard (8th-9th grade)"
    elif score >= 50:
        level = "Fairly Difficult (10th-12th grade)"
    elif score >= 30:
        level = "Difficult (College)"
    else:
        level = "Very Difficult (College Graduate)"
    
    return {
        "flesch_score": round(score, 1),
        "level": level,
        "word_count": len(words),
        "sentence_count": sentences,
        "avg_words_per_sentence": round(avg_words, 1),
    }


def _toxicity(text: str) -> Dict[str, Any]:
    """Mock toxicity detection."""
    toxic_indicators = {"hate", "stupid", "idiot", "kill", "die", "attack", "violence"}
    words = set(re.findall(r"\\b\\w+\\b", text.lower()))
    hits = words & toxic_indicators
    score = min(0.95, len(hits) * 0.25 + random.uniform(0, 0.1))
    return {
        "is_toxic": score > 0.5,
        "score": round(score, 3),
        "categories": {
            "toxicity": round(score, 3),
            "severe_toxicity": round(score * 0.6, 3),
            "identity_attack": round(random.uniform(0, 0.2), 3),
            "insult": round(score * 0.7 if hits else random.uniform(0, 0.15), 3),
        },
    }


def _topics(text: str) -> List[Dict[str, Any]]:
    """Mock topic extraction."""
    possible_topics = [
        "Technology", "Artificial Intelligence", "Business", "Science", "Health",
        "Education", "Finance", "Entertainment", "Sports", "Politics", "Travel",
        "Food", "Environment", "Art", "Music", "Sports", "History",
    ]
    selected = random.sample(possible_topics, k=min(4, len(possible_topics)))
    return [{"topic": t, "relevance": round(random.uniform(0.4, 0.95), 2)} for t in selected]


def analyze_text(text: str, analysis_type: str = "sentiment") -> Dict[str, Any]:
    """
    Run the requested analysis on the provided text.
    
    Args:
        text: Input text to analyze.
        analysis_type: One of the supported analysis type IDs.
        
    Returns:
        Structured analysis result.
    """
    if not text or not text.strip():
        return {"error": "Text is required", "status": "error"}
    
    cleaned = text.strip()[:10000]
    analysis_id = hashlib.md5(f"{cleaned}-{analysis_type}-{datetime.utcnow()}".encode()).hexdigest()[:12]
    
    result_data = {}
    if analysis_type == "sentiment":
        result_data = _simple_sentiment(cleaned)
    elif analysis_type == "entities":
        result_data = {"entities": _extract_entities(cleaned)}
    elif analysis_type == "keywords":
        result_data = {"keywords": _extract_keywords(cleaned)}
    elif analysis_type == "summary":
        result_data = {"summary": _summarize(cleaned)}
    elif analysis_type == "language":
        result_data = _detect_language(cleaned)
    elif analysis_type == "readability":
        result_data = _readability(cleaned)
    elif analysis_type == "toxicity":
        result_data = _toxicity(cleaned)
    elif analysis_type == "topics":
        result_data = {"topics": _topics(cleaned)}
    else:
        return {"error": f"Unknown analysis type: {analysis_type}", "status": "error"}
    
    return {
        "status": "success",
        "analysis_id": analysis_id,
        "type": analysis_type,
        "input_length": len(cleaned),
        "word_count": len(cleaned.split()),
        "result": result_data,
        "processed_at": datetime.utcnow().isoformat() + "Z",
        "model": "ai-platform-hub-nlp-v1",
    }
