"""
Mock API Response Generator
Generates large volumes of realistic mock API response structures.
"""

from typing import List, Dict, Any
import random
from datetime import datetime, timedelta

def generate_mock_responses(count: int = 100) -> List[Dict[str, Any]]:
    """Generate a list of mock API response objects."""
    responses = []
    for i in range(count):
        responses.append({
            "id": f"resp-{i:06d}",
            "status": random.choice(["success", "success", "success", "error"]),
            "latency_ms": random.randint(50, 900),
            "tokens_in": random.randint(10, 2000),
            "tokens_out": random.randint(20, 1500),
            "model": f"model-{random.randint(0, 199):04d}",
            "timestamp": (datetime.utcnow() - timedelta(seconds=i*30)).isoformat(),
            "metadata": {
                "region": random.choice(["us-east", "us-west", "eu-central", "ap-south"]),
                "version": f"v{random.randint(1,5)}.{random.randint(0,9)}",
            },
        })
    return responses


MOCK_RESPONSE_TEMPLATE_000 = {
    "endpoint": "/v1/resource/0",
    "method": "GET",
    "description": "Mock endpoint number 0 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 0, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_001 = {
    "endpoint": "/v1/resource/1",
    "method": "GET",
    "description": "Mock endpoint number 1 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 1, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_002 = {
    "endpoint": "/v1/resource/2",
    "method": "GET",
    "description": "Mock endpoint number 2 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 2, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_003 = {
    "endpoint": "/v1/resource/3",
    "method": "GET",
    "description": "Mock endpoint number 3 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 3, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_004 = {
    "endpoint": "/v1/resource/4",
    "method": "GET",
    "description": "Mock endpoint number 4 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 4, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_005 = {
    "endpoint": "/v1/resource/5",
    "method": "GET",
    "description": "Mock endpoint number 5 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 5, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_006 = {
    "endpoint": "/v1/resource/6",
    "method": "GET",
    "description": "Mock endpoint number 6 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 6, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_007 = {
    "endpoint": "/v1/resource/7",
    "method": "GET",
    "description": "Mock endpoint number 7 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 7, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_008 = {
    "endpoint": "/v1/resource/8",
    "method": "GET",
    "description": "Mock endpoint number 8 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 8, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_009 = {
    "endpoint": "/v1/resource/9",
    "method": "GET",
    "description": "Mock endpoint number 9 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 9, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_010 = {
    "endpoint": "/v1/resource/10",
    "method": "GET",
    "description": "Mock endpoint number 10 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 10, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_011 = {
    "endpoint": "/v1/resource/11",
    "method": "GET",
    "description": "Mock endpoint number 11 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 11, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_012 = {
    "endpoint": "/v1/resource/12",
    "method": "GET",
    "description": "Mock endpoint number 12 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 12, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_013 = {
    "endpoint": "/v1/resource/13",
    "method": "GET",
    "description": "Mock endpoint number 13 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 13, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_014 = {
    "endpoint": "/v1/resource/14",
    "method": "GET",
    "description": "Mock endpoint number 14 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 14, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_015 = {
    "endpoint": "/v1/resource/15",
    "method": "GET",
    "description": "Mock endpoint number 15 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 15, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_016 = {
    "endpoint": "/v1/resource/16",
    "method": "GET",
    "description": "Mock endpoint number 16 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 16, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_017 = {
    "endpoint": "/v1/resource/17",
    "method": "GET",
    "description": "Mock endpoint number 17 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 17, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_018 = {
    "endpoint": "/v1/resource/18",
    "method": "GET",
    "description": "Mock endpoint number 18 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 18, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_019 = {
    "endpoint": "/v1/resource/19",
    "method": "GET",
    "description": "Mock endpoint number 19 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 19, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_020 = {
    "endpoint": "/v1/resource/20",
    "method": "GET",
    "description": "Mock endpoint number 20 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 20, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_021 = {
    "endpoint": "/v1/resource/21",
    "method": "GET",
    "description": "Mock endpoint number 21 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 21, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_022 = {
    "endpoint": "/v1/resource/22",
    "method": "GET",
    "description": "Mock endpoint number 22 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 22, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_023 = {
    "endpoint": "/v1/resource/23",
    "method": "GET",
    "description": "Mock endpoint number 23 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 23, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_024 = {
    "endpoint": "/v1/resource/24",
    "method": "GET",
    "description": "Mock endpoint number 24 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 24, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_025 = {
    "endpoint": "/v1/resource/25",
    "method": "GET",
    "description": "Mock endpoint number 25 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 25, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_026 = {
    "endpoint": "/v1/resource/26",
    "method": "GET",
    "description": "Mock endpoint number 26 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 26, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_027 = {
    "endpoint": "/v1/resource/27",
    "method": "GET",
    "description": "Mock endpoint number 27 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 27, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_028 = {
    "endpoint": "/v1/resource/28",
    "method": "GET",
    "description": "Mock endpoint number 28 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 28, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_029 = {
    "endpoint": "/v1/resource/29",
    "method": "GET",
    "description": "Mock endpoint number 29 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 29, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_030 = {
    "endpoint": "/v1/resource/30",
    "method": "GET",
    "description": "Mock endpoint number 30 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 30, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_031 = {
    "endpoint": "/v1/resource/31",
    "method": "GET",
    "description": "Mock endpoint number 31 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 31, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_032 = {
    "endpoint": "/v1/resource/32",
    "method": "GET",
    "description": "Mock endpoint number 32 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 32, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_033 = {
    "endpoint": "/v1/resource/33",
    "method": "GET",
    "description": "Mock endpoint number 33 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 33, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_034 = {
    "endpoint": "/v1/resource/34",
    "method": "GET",
    "description": "Mock endpoint number 34 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 34, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_035 = {
    "endpoint": "/v1/resource/35",
    "method": "GET",
    "description": "Mock endpoint number 35 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 35, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_036 = {
    "endpoint": "/v1/resource/36",
    "method": "GET",
    "description": "Mock endpoint number 36 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 36, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_037 = {
    "endpoint": "/v1/resource/37",
    "method": "GET",
    "description": "Mock endpoint number 37 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 37, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_038 = {
    "endpoint": "/v1/resource/38",
    "method": "GET",
    "description": "Mock endpoint number 38 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 38, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_039 = {
    "endpoint": "/v1/resource/39",
    "method": "GET",
    "description": "Mock endpoint number 39 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 39, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_040 = {
    "endpoint": "/v1/resource/40",
    "method": "GET",
    "description": "Mock endpoint number 40 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 40, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_041 = {
    "endpoint": "/v1/resource/41",
    "method": "GET",
    "description": "Mock endpoint number 41 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 41, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_042 = {
    "endpoint": "/v1/resource/42",
    "method": "GET",
    "description": "Mock endpoint number 42 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 42, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_043 = {
    "endpoint": "/v1/resource/43",
    "method": "GET",
    "description": "Mock endpoint number 43 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 43, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_044 = {
    "endpoint": "/v1/resource/44",
    "method": "GET",
    "description": "Mock endpoint number 44 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 44, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_045 = {
    "endpoint": "/v1/resource/45",
    "method": "GET",
    "description": "Mock endpoint number 45 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 45, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_046 = {
    "endpoint": "/v1/resource/46",
    "method": "GET",
    "description": "Mock endpoint number 46 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 46, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_047 = {
    "endpoint": "/v1/resource/47",
    "method": "GET",
    "description": "Mock endpoint number 47 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 47, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_048 = {
    "endpoint": "/v1/resource/48",
    "method": "GET",
    "description": "Mock endpoint number 48 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 48, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_049 = {
    "endpoint": "/v1/resource/49",
    "method": "GET",
    "description": "Mock endpoint number 49 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 49, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_050 = {
    "endpoint": "/v1/resource/50",
    "method": "GET",
    "description": "Mock endpoint number 50 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 50, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_051 = {
    "endpoint": "/v1/resource/51",
    "method": "GET",
    "description": "Mock endpoint number 51 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 51, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_052 = {
    "endpoint": "/v1/resource/52",
    "method": "GET",
    "description": "Mock endpoint number 52 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 52, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_053 = {
    "endpoint": "/v1/resource/53",
    "method": "GET",
    "description": "Mock endpoint number 53 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 53, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_054 = {
    "endpoint": "/v1/resource/54",
    "method": "GET",
    "description": "Mock endpoint number 54 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 54, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_055 = {
    "endpoint": "/v1/resource/55",
    "method": "GET",
    "description": "Mock endpoint number 55 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 55, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_056 = {
    "endpoint": "/v1/resource/56",
    "method": "GET",
    "description": "Mock endpoint number 56 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 56, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_057 = {
    "endpoint": "/v1/resource/57",
    "method": "GET",
    "description": "Mock endpoint number 57 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 57, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_058 = {
    "endpoint": "/v1/resource/58",
    "method": "GET",
    "description": "Mock endpoint number 58 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 58, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_059 = {
    "endpoint": "/v1/resource/59",
    "method": "GET",
    "description": "Mock endpoint number 59 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 59, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_060 = {
    "endpoint": "/v1/resource/60",
    "method": "GET",
    "description": "Mock endpoint number 60 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 60, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_061 = {
    "endpoint": "/v1/resource/61",
    "method": "GET",
    "description": "Mock endpoint number 61 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 61, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_062 = {
    "endpoint": "/v1/resource/62",
    "method": "GET",
    "description": "Mock endpoint number 62 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 62, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_063 = {
    "endpoint": "/v1/resource/63",
    "method": "GET",
    "description": "Mock endpoint number 63 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 63, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_064 = {
    "endpoint": "/v1/resource/64",
    "method": "GET",
    "description": "Mock endpoint number 64 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 64, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_065 = {
    "endpoint": "/v1/resource/65",
    "method": "GET",
    "description": "Mock endpoint number 65 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 65, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_066 = {
    "endpoint": "/v1/resource/66",
    "method": "GET",
    "description": "Mock endpoint number 66 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 66, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_067 = {
    "endpoint": "/v1/resource/67",
    "method": "GET",
    "description": "Mock endpoint number 67 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 67, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_068 = {
    "endpoint": "/v1/resource/68",
    "method": "GET",
    "description": "Mock endpoint number 68 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 68, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_069 = {
    "endpoint": "/v1/resource/69",
    "method": "GET",
    "description": "Mock endpoint number 69 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 69, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_070 = {
    "endpoint": "/v1/resource/70",
    "method": "GET",
    "description": "Mock endpoint number 70 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 70, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_071 = {
    "endpoint": "/v1/resource/71",
    "method": "GET",
    "description": "Mock endpoint number 71 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 71, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_072 = {
    "endpoint": "/v1/resource/72",
    "method": "GET",
    "description": "Mock endpoint number 72 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 72, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_073 = {
    "endpoint": "/v1/resource/73",
    "method": "GET",
    "description": "Mock endpoint number 73 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 73, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_074 = {
    "endpoint": "/v1/resource/74",
    "method": "GET",
    "description": "Mock endpoint number 74 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 74, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_075 = {
    "endpoint": "/v1/resource/75",
    "method": "GET",
    "description": "Mock endpoint number 75 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 75, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_076 = {
    "endpoint": "/v1/resource/76",
    "method": "GET",
    "description": "Mock endpoint number 76 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 76, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_077 = {
    "endpoint": "/v1/resource/77",
    "method": "GET",
    "description": "Mock endpoint number 77 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 77, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_078 = {
    "endpoint": "/v1/resource/78",
    "method": "GET",
    "description": "Mock endpoint number 78 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 78, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_079 = {
    "endpoint": "/v1/resource/79",
    "method": "GET",
    "description": "Mock endpoint number 79 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 79, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_080 = {
    "endpoint": "/v1/resource/80",
    "method": "GET",
    "description": "Mock endpoint number 80 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 80, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_081 = {
    "endpoint": "/v1/resource/81",
    "method": "GET",
    "description": "Mock endpoint number 81 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 81, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_082 = {
    "endpoint": "/v1/resource/82",
    "method": "GET",
    "description": "Mock endpoint number 82 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 82, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_083 = {
    "endpoint": "/v1/resource/83",
    "method": "GET",
    "description": "Mock endpoint number 83 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 83, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_084 = {
    "endpoint": "/v1/resource/84",
    "method": "GET",
    "description": "Mock endpoint number 84 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 84, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_085 = {
    "endpoint": "/v1/resource/85",
    "method": "GET",
    "description": "Mock endpoint number 85 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 85, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_086 = {
    "endpoint": "/v1/resource/86",
    "method": "GET",
    "description": "Mock endpoint number 86 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 86, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_087 = {
    "endpoint": "/v1/resource/87",
    "method": "GET",
    "description": "Mock endpoint number 87 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 87, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_088 = {
    "endpoint": "/v1/resource/88",
    "method": "GET",
    "description": "Mock endpoint number 88 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 88, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_089 = {
    "endpoint": "/v1/resource/89",
    "method": "GET",
    "description": "Mock endpoint number 89 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 89, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_090 = {
    "endpoint": "/v1/resource/90",
    "method": "GET",
    "description": "Mock endpoint number 90 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 90, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_091 = {
    "endpoint": "/v1/resource/91",
    "method": "GET",
    "description": "Mock endpoint number 91 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 91, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_092 = {
    "endpoint": "/v1/resource/92",
    "method": "GET",
    "description": "Mock endpoint number 92 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 92, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_093 = {
    "endpoint": "/v1/resource/93",
    "method": "GET",
    "description": "Mock endpoint number 93 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 93, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_094 = {
    "endpoint": "/v1/resource/94",
    "method": "GET",
    "description": "Mock endpoint number 94 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 94, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_095 = {
    "endpoint": "/v1/resource/95",
    "method": "GET",
    "description": "Mock endpoint number 95 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 95, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_096 = {
    "endpoint": "/v1/resource/96",
    "method": "GET",
    "description": "Mock endpoint number 96 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 96, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_097 = {
    "endpoint": "/v1/resource/97",
    "method": "GET",
    "description": "Mock endpoint number 97 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 97, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_098 = {
    "endpoint": "/v1/resource/98",
    "method": "GET",
    "description": "Mock endpoint number 98 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 98, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_099 = {
    "endpoint": "/v1/resource/99",
    "method": "GET",
    "description": "Mock endpoint number 99 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 99, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_100 = {
    "endpoint": "/v1/resource/100",
    "method": "GET",
    "description": "Mock endpoint number 100 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 100, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_101 = {
    "endpoint": "/v1/resource/101",
    "method": "GET",
    "description": "Mock endpoint number 101 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 101, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_102 = {
    "endpoint": "/v1/resource/102",
    "method": "GET",
    "description": "Mock endpoint number 102 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 102, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_103 = {
    "endpoint": "/v1/resource/103",
    "method": "GET",
    "description": "Mock endpoint number 103 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 103, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_104 = {
    "endpoint": "/v1/resource/104",
    "method": "GET",
    "description": "Mock endpoint number 104 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 104, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_105 = {
    "endpoint": "/v1/resource/105",
    "method": "GET",
    "description": "Mock endpoint number 105 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 105, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_106 = {
    "endpoint": "/v1/resource/106",
    "method": "GET",
    "description": "Mock endpoint number 106 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 106, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_107 = {
    "endpoint": "/v1/resource/107",
    "method": "GET",
    "description": "Mock endpoint number 107 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 107, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_108 = {
    "endpoint": "/v1/resource/108",
    "method": "GET",
    "description": "Mock endpoint number 108 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 108, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_109 = {
    "endpoint": "/v1/resource/109",
    "method": "GET",
    "description": "Mock endpoint number 109 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 109, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_110 = {
    "endpoint": "/v1/resource/110",
    "method": "GET",
    "description": "Mock endpoint number 110 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 110, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_111 = {
    "endpoint": "/v1/resource/111",
    "method": "GET",
    "description": "Mock endpoint number 111 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 111, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_112 = {
    "endpoint": "/v1/resource/112",
    "method": "GET",
    "description": "Mock endpoint number 112 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 112, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_113 = {
    "endpoint": "/v1/resource/113",
    "method": "GET",
    "description": "Mock endpoint number 113 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 113, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_114 = {
    "endpoint": "/v1/resource/114",
    "method": "GET",
    "description": "Mock endpoint number 114 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 114, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_115 = {
    "endpoint": "/v1/resource/115",
    "method": "GET",
    "description": "Mock endpoint number 115 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 115, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_116 = {
    "endpoint": "/v1/resource/116",
    "method": "GET",
    "description": "Mock endpoint number 116 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 116, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_117 = {
    "endpoint": "/v1/resource/117",
    "method": "GET",
    "description": "Mock endpoint number 117 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 117, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_118 = {
    "endpoint": "/v1/resource/118",
    "method": "GET",
    "description": "Mock endpoint number 118 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 118, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_119 = {
    "endpoint": "/v1/resource/119",
    "method": "GET",
    "description": "Mock endpoint number 119 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 119, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_120 = {
    "endpoint": "/v1/resource/120",
    "method": "GET",
    "description": "Mock endpoint number 120 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 120, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_121 = {
    "endpoint": "/v1/resource/121",
    "method": "GET",
    "description": "Mock endpoint number 121 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 121, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_122 = {
    "endpoint": "/v1/resource/122",
    "method": "GET",
    "description": "Mock endpoint number 122 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 122, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_123 = {
    "endpoint": "/v1/resource/123",
    "method": "GET",
    "description": "Mock endpoint number 123 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 123, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_124 = {
    "endpoint": "/v1/resource/124",
    "method": "GET",
    "description": "Mock endpoint number 124 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 124, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_125 = {
    "endpoint": "/v1/resource/125",
    "method": "GET",
    "description": "Mock endpoint number 125 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 125, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_126 = {
    "endpoint": "/v1/resource/126",
    "method": "GET",
    "description": "Mock endpoint number 126 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 126, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_127 = {
    "endpoint": "/v1/resource/127",
    "method": "GET",
    "description": "Mock endpoint number 127 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 127, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_128 = {
    "endpoint": "/v1/resource/128",
    "method": "GET",
    "description": "Mock endpoint number 128 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 128, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_129 = {
    "endpoint": "/v1/resource/129",
    "method": "GET",
    "description": "Mock endpoint number 129 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 129, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_130 = {
    "endpoint": "/v1/resource/130",
    "method": "GET",
    "description": "Mock endpoint number 130 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 130, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_131 = {
    "endpoint": "/v1/resource/131",
    "method": "GET",
    "description": "Mock endpoint number 131 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 131, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_132 = {
    "endpoint": "/v1/resource/132",
    "method": "GET",
    "description": "Mock endpoint number 132 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 132, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_133 = {
    "endpoint": "/v1/resource/133",
    "method": "GET",
    "description": "Mock endpoint number 133 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 133, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_134 = {
    "endpoint": "/v1/resource/134",
    "method": "GET",
    "description": "Mock endpoint number 134 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 134, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_135 = {
    "endpoint": "/v1/resource/135",
    "method": "GET",
    "description": "Mock endpoint number 135 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 135, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_136 = {
    "endpoint": "/v1/resource/136",
    "method": "GET",
    "description": "Mock endpoint number 136 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 136, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_137 = {
    "endpoint": "/v1/resource/137",
    "method": "GET",
    "description": "Mock endpoint number 137 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 137, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_138 = {
    "endpoint": "/v1/resource/138",
    "method": "GET",
    "description": "Mock endpoint number 138 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 138, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_139 = {
    "endpoint": "/v1/resource/139",
    "method": "GET",
    "description": "Mock endpoint number 139 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 139, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_140 = {
    "endpoint": "/v1/resource/140",
    "method": "GET",
    "description": "Mock endpoint number 140 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 140, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_141 = {
    "endpoint": "/v1/resource/141",
    "method": "GET",
    "description": "Mock endpoint number 141 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 141, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_142 = {
    "endpoint": "/v1/resource/142",
    "method": "GET",
    "description": "Mock endpoint number 142 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 142, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_143 = {
    "endpoint": "/v1/resource/143",
    "method": "GET",
    "description": "Mock endpoint number 143 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 143, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_144 = {
    "endpoint": "/v1/resource/144",
    "method": "GET",
    "description": "Mock endpoint number 144 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 144, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_145 = {
    "endpoint": "/v1/resource/145",
    "method": "GET",
    "description": "Mock endpoint number 145 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 145, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_146 = {
    "endpoint": "/v1/resource/146",
    "method": "GET",
    "description": "Mock endpoint number 146 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 146, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_147 = {
    "endpoint": "/v1/resource/147",
    "method": "GET",
    "description": "Mock endpoint number 147 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 147, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_148 = {
    "endpoint": "/v1/resource/148",
    "method": "GET",
    "description": "Mock endpoint number 148 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 148, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_149 = {
    "endpoint": "/v1/resource/149",
    "method": "GET",
    "description": "Mock endpoint number 149 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 149, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_150 = {
    "endpoint": "/v1/resource/150",
    "method": "GET",
    "description": "Mock endpoint number 150 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 150, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_151 = {
    "endpoint": "/v1/resource/151",
    "method": "GET",
    "description": "Mock endpoint number 151 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 151, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_152 = {
    "endpoint": "/v1/resource/152",
    "method": "GET",
    "description": "Mock endpoint number 152 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 152, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_153 = {
    "endpoint": "/v1/resource/153",
    "method": "GET",
    "description": "Mock endpoint number 153 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 153, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_154 = {
    "endpoint": "/v1/resource/154",
    "method": "GET",
    "description": "Mock endpoint number 154 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 154, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_155 = {
    "endpoint": "/v1/resource/155",
    "method": "GET",
    "description": "Mock endpoint number 155 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 155, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_156 = {
    "endpoint": "/v1/resource/156",
    "method": "GET",
    "description": "Mock endpoint number 156 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 156, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_157 = {
    "endpoint": "/v1/resource/157",
    "method": "GET",
    "description": "Mock endpoint number 157 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 157, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_158 = {
    "endpoint": "/v1/resource/158",
    "method": "GET",
    "description": "Mock endpoint number 158 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 158, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_159 = {
    "endpoint": "/v1/resource/159",
    "method": "GET",
    "description": "Mock endpoint number 159 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 159, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_160 = {
    "endpoint": "/v1/resource/160",
    "method": "GET",
    "description": "Mock endpoint number 160 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 160, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_161 = {
    "endpoint": "/v1/resource/161",
    "method": "GET",
    "description": "Mock endpoint number 161 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 161, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_162 = {
    "endpoint": "/v1/resource/162",
    "method": "GET",
    "description": "Mock endpoint number 162 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 162, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_163 = {
    "endpoint": "/v1/resource/163",
    "method": "GET",
    "description": "Mock endpoint number 163 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 163, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_164 = {
    "endpoint": "/v1/resource/164",
    "method": "GET",
    "description": "Mock endpoint number 164 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 164, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_165 = {
    "endpoint": "/v1/resource/165",
    "method": "GET",
    "description": "Mock endpoint number 165 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 165, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_166 = {
    "endpoint": "/v1/resource/166",
    "method": "GET",
    "description": "Mock endpoint number 166 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 166, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_167 = {
    "endpoint": "/v1/resource/167",
    "method": "GET",
    "description": "Mock endpoint number 167 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 167, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_168 = {
    "endpoint": "/v1/resource/168",
    "method": "GET",
    "description": "Mock endpoint number 168 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 168, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_169 = {
    "endpoint": "/v1/resource/169",
    "method": "GET",
    "description": "Mock endpoint number 169 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 169, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_170 = {
    "endpoint": "/v1/resource/170",
    "method": "GET",
    "description": "Mock endpoint number 170 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 170, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_171 = {
    "endpoint": "/v1/resource/171",
    "method": "GET",
    "description": "Mock endpoint number 171 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 171, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_172 = {
    "endpoint": "/v1/resource/172",
    "method": "GET",
    "description": "Mock endpoint number 172 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 172, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_173 = {
    "endpoint": "/v1/resource/173",
    "method": "GET",
    "description": "Mock endpoint number 173 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 173, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_174 = {
    "endpoint": "/v1/resource/174",
    "method": "GET",
    "description": "Mock endpoint number 174 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 174, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_175 = {
    "endpoint": "/v1/resource/175",
    "method": "GET",
    "description": "Mock endpoint number 175 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 175, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_176 = {
    "endpoint": "/v1/resource/176",
    "method": "GET",
    "description": "Mock endpoint number 176 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 176, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_177 = {
    "endpoint": "/v1/resource/177",
    "method": "GET",
    "description": "Mock endpoint number 177 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 177, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_178 = {
    "endpoint": "/v1/resource/178",
    "method": "GET",
    "description": "Mock endpoint number 178 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 178, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_179 = {
    "endpoint": "/v1/resource/179",
    "method": "GET",
    "description": "Mock endpoint number 179 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 179, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_180 = {
    "endpoint": "/v1/resource/180",
    "method": "GET",
    "description": "Mock endpoint number 180 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 180, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_181 = {
    "endpoint": "/v1/resource/181",
    "method": "GET",
    "description": "Mock endpoint number 181 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 181, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_182 = {
    "endpoint": "/v1/resource/182",
    "method": "GET",
    "description": "Mock endpoint number 182 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 182, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_183 = {
    "endpoint": "/v1/resource/183",
    "method": "GET",
    "description": "Mock endpoint number 183 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 183, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_184 = {
    "endpoint": "/v1/resource/184",
    "method": "GET",
    "description": "Mock endpoint number 184 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 184, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_185 = {
    "endpoint": "/v1/resource/185",
    "method": "GET",
    "description": "Mock endpoint number 185 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 185, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_186 = {
    "endpoint": "/v1/resource/186",
    "method": "GET",
    "description": "Mock endpoint number 186 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 186, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_187 = {
    "endpoint": "/v1/resource/187",
    "method": "GET",
    "description": "Mock endpoint number 187 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 187, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_188 = {
    "endpoint": "/v1/resource/188",
    "method": "GET",
    "description": "Mock endpoint number 188 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 188, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_189 = {
    "endpoint": "/v1/resource/189",
    "method": "GET",
    "description": "Mock endpoint number 189 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 189, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_190 = {
    "endpoint": "/v1/resource/190",
    "method": "GET",
    "description": "Mock endpoint number 190 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 190, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_191 = {
    "endpoint": "/v1/resource/191",
    "method": "GET",
    "description": "Mock endpoint number 191 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 191, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_192 = {
    "endpoint": "/v1/resource/192",
    "method": "GET",
    "description": "Mock endpoint number 192 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 192, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_193 = {
    "endpoint": "/v1/resource/193",
    "method": "GET",
    "description": "Mock endpoint number 193 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 193, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_194 = {
    "endpoint": "/v1/resource/194",
    "method": "GET",
    "description": "Mock endpoint number 194 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 194, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_195 = {
    "endpoint": "/v1/resource/195",
    "method": "GET",
    "description": "Mock endpoint number 195 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 195, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_196 = {
    "endpoint": "/v1/resource/196",
    "method": "GET",
    "description": "Mock endpoint number 196 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 196, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_197 = {
    "endpoint": "/v1/resource/197",
    "method": "GET",
    "description": "Mock endpoint number 197 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 197, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_198 = {
    "endpoint": "/v1/resource/198",
    "method": "GET",
    "description": "Mock endpoint number 198 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 198, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_199 = {
    "endpoint": "/v1/resource/199",
    "method": "GET",
    "description": "Mock endpoint number 199 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 199, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_200 = {
    "endpoint": "/v1/resource/200",
    "method": "GET",
    "description": "Mock endpoint number 200 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 200, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_201 = {
    "endpoint": "/v1/resource/201",
    "method": "GET",
    "description": "Mock endpoint number 201 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 201, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_202 = {
    "endpoint": "/v1/resource/202",
    "method": "GET",
    "description": "Mock endpoint number 202 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 202, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_203 = {
    "endpoint": "/v1/resource/203",
    "method": "GET",
    "description": "Mock endpoint number 203 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 203, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_204 = {
    "endpoint": "/v1/resource/204",
    "method": "GET",
    "description": "Mock endpoint number 204 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 204, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_205 = {
    "endpoint": "/v1/resource/205",
    "method": "GET",
    "description": "Mock endpoint number 205 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 205, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_206 = {
    "endpoint": "/v1/resource/206",
    "method": "GET",
    "description": "Mock endpoint number 206 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 206, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_207 = {
    "endpoint": "/v1/resource/207",
    "method": "GET",
    "description": "Mock endpoint number 207 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 207, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_208 = {
    "endpoint": "/v1/resource/208",
    "method": "GET",
    "description": "Mock endpoint number 208 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 208, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_209 = {
    "endpoint": "/v1/resource/209",
    "method": "GET",
    "description": "Mock endpoint number 209 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 209, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_210 = {
    "endpoint": "/v1/resource/210",
    "method": "GET",
    "description": "Mock endpoint number 210 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 210, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_211 = {
    "endpoint": "/v1/resource/211",
    "method": "GET",
    "description": "Mock endpoint number 211 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 211, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_212 = {
    "endpoint": "/v1/resource/212",
    "method": "GET",
    "description": "Mock endpoint number 212 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 212, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_213 = {
    "endpoint": "/v1/resource/213",
    "method": "GET",
    "description": "Mock endpoint number 213 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 213, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_214 = {
    "endpoint": "/v1/resource/214",
    "method": "GET",
    "description": "Mock endpoint number 214 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 214, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_215 = {
    "endpoint": "/v1/resource/215",
    "method": "GET",
    "description": "Mock endpoint number 215 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 215, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_216 = {
    "endpoint": "/v1/resource/216",
    "method": "GET",
    "description": "Mock endpoint number 216 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 216, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_217 = {
    "endpoint": "/v1/resource/217",
    "method": "GET",
    "description": "Mock endpoint number 217 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 217, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_218 = {
    "endpoint": "/v1/resource/218",
    "method": "GET",
    "description": "Mock endpoint number 218 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 218, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_219 = {
    "endpoint": "/v1/resource/219",
    "method": "GET",
    "description": "Mock endpoint number 219 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 219, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_220 = {
    "endpoint": "/v1/resource/220",
    "method": "GET",
    "description": "Mock endpoint number 220 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 220, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_221 = {
    "endpoint": "/v1/resource/221",
    "method": "GET",
    "description": "Mock endpoint number 221 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 221, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_222 = {
    "endpoint": "/v1/resource/222",
    "method": "GET",
    "description": "Mock endpoint number 222 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 222, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_223 = {
    "endpoint": "/v1/resource/223",
    "method": "GET",
    "description": "Mock endpoint number 223 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 223, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_224 = {
    "endpoint": "/v1/resource/224",
    "method": "GET",
    "description": "Mock endpoint number 224 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 224, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_225 = {
    "endpoint": "/v1/resource/225",
    "method": "GET",
    "description": "Mock endpoint number 225 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 225, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_226 = {
    "endpoint": "/v1/resource/226",
    "method": "GET",
    "description": "Mock endpoint number 226 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 226, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_227 = {
    "endpoint": "/v1/resource/227",
    "method": "GET",
    "description": "Mock endpoint number 227 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 227, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_228 = {
    "endpoint": "/v1/resource/228",
    "method": "GET",
    "description": "Mock endpoint number 228 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 228, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_229 = {
    "endpoint": "/v1/resource/229",
    "method": "GET",
    "description": "Mock endpoint number 229 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 229, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_230 = {
    "endpoint": "/v1/resource/230",
    "method": "GET",
    "description": "Mock endpoint number 230 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 230, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_231 = {
    "endpoint": "/v1/resource/231",
    "method": "GET",
    "description": "Mock endpoint number 231 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 231, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_232 = {
    "endpoint": "/v1/resource/232",
    "method": "GET",
    "description": "Mock endpoint number 232 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 232, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_233 = {
    "endpoint": "/v1/resource/233",
    "method": "GET",
    "description": "Mock endpoint number 233 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 233, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_234 = {
    "endpoint": "/v1/resource/234",
    "method": "GET",
    "description": "Mock endpoint number 234 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 234, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_235 = {
    "endpoint": "/v1/resource/235",
    "method": "GET",
    "description": "Mock endpoint number 235 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 235, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_236 = {
    "endpoint": "/v1/resource/236",
    "method": "GET",
    "description": "Mock endpoint number 236 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 236, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_237 = {
    "endpoint": "/v1/resource/237",
    "method": "GET",
    "description": "Mock endpoint number 237 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 237, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_238 = {
    "endpoint": "/v1/resource/238",
    "method": "GET",
    "description": "Mock endpoint number 238 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 238, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_239 = {
    "endpoint": "/v1/resource/239",
    "method": "GET",
    "description": "Mock endpoint number 239 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 239, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_240 = {
    "endpoint": "/v1/resource/240",
    "method": "GET",
    "description": "Mock endpoint number 240 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 240, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_241 = {
    "endpoint": "/v1/resource/241",
    "method": "GET",
    "description": "Mock endpoint number 241 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 241, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_242 = {
    "endpoint": "/v1/resource/242",
    "method": "GET",
    "description": "Mock endpoint number 242 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 242, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_243 = {
    "endpoint": "/v1/resource/243",
    "method": "GET",
    "description": "Mock endpoint number 243 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 243, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_244 = {
    "endpoint": "/v1/resource/244",
    "method": "GET",
    "description": "Mock endpoint number 244 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 244, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_245 = {
    "endpoint": "/v1/resource/245",
    "method": "GET",
    "description": "Mock endpoint number 245 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 245, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_246 = {
    "endpoint": "/v1/resource/246",
    "method": "GET",
    "description": "Mock endpoint number 246 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 246, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_247 = {
    "endpoint": "/v1/resource/247",
    "method": "GET",
    "description": "Mock endpoint number 247 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 247, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_248 = {
    "endpoint": "/v1/resource/248",
    "method": "GET",
    "description": "Mock endpoint number 248 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 248, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_249 = {
    "endpoint": "/v1/resource/249",
    "method": "GET",
    "description": "Mock endpoint number 249 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 249, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_250 = {
    "endpoint": "/v1/resource/250",
    "method": "GET",
    "description": "Mock endpoint number 250 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 250, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_251 = {
    "endpoint": "/v1/resource/251",
    "method": "GET",
    "description": "Mock endpoint number 251 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 251, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_252 = {
    "endpoint": "/v1/resource/252",
    "method": "GET",
    "description": "Mock endpoint number 252 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 252, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_253 = {
    "endpoint": "/v1/resource/253",
    "method": "GET",
    "description": "Mock endpoint number 253 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 253, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_254 = {
    "endpoint": "/v1/resource/254",
    "method": "GET",
    "description": "Mock endpoint number 254 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 254, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_255 = {
    "endpoint": "/v1/resource/255",
    "method": "GET",
    "description": "Mock endpoint number 255 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 255, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_256 = {
    "endpoint": "/v1/resource/256",
    "method": "GET",
    "description": "Mock endpoint number 256 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 256, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_257 = {
    "endpoint": "/v1/resource/257",
    "method": "GET",
    "description": "Mock endpoint number 257 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 257, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_258 = {
    "endpoint": "/v1/resource/258",
    "method": "GET",
    "description": "Mock endpoint number 258 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 258, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_259 = {
    "endpoint": "/v1/resource/259",
    "method": "GET",
    "description": "Mock endpoint number 259 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 259, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_260 = {
    "endpoint": "/v1/resource/260",
    "method": "GET",
    "description": "Mock endpoint number 260 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 260, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_261 = {
    "endpoint": "/v1/resource/261",
    "method": "GET",
    "description": "Mock endpoint number 261 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 261, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_262 = {
    "endpoint": "/v1/resource/262",
    "method": "GET",
    "description": "Mock endpoint number 262 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 262, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_263 = {
    "endpoint": "/v1/resource/263",
    "method": "GET",
    "description": "Mock endpoint number 263 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 263, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_264 = {
    "endpoint": "/v1/resource/264",
    "method": "GET",
    "description": "Mock endpoint number 264 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 264, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_265 = {
    "endpoint": "/v1/resource/265",
    "method": "GET",
    "description": "Mock endpoint number 265 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 265, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_266 = {
    "endpoint": "/v1/resource/266",
    "method": "GET",
    "description": "Mock endpoint number 266 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 266, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_267 = {
    "endpoint": "/v1/resource/267",
    "method": "GET",
    "description": "Mock endpoint number 267 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 267, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_268 = {
    "endpoint": "/v1/resource/268",
    "method": "GET",
    "description": "Mock endpoint number 268 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 268, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_269 = {
    "endpoint": "/v1/resource/269",
    "method": "GET",
    "description": "Mock endpoint number 269 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 269, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_270 = {
    "endpoint": "/v1/resource/270",
    "method": "GET",
    "description": "Mock endpoint number 270 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 270, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_271 = {
    "endpoint": "/v1/resource/271",
    "method": "GET",
    "description": "Mock endpoint number 271 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 271, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_272 = {
    "endpoint": "/v1/resource/272",
    "method": "GET",
    "description": "Mock endpoint number 272 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 272, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_273 = {
    "endpoint": "/v1/resource/273",
    "method": "GET",
    "description": "Mock endpoint number 273 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 273, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_274 = {
    "endpoint": "/v1/resource/274",
    "method": "GET",
    "description": "Mock endpoint number 274 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 274, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_275 = {
    "endpoint": "/v1/resource/275",
    "method": "GET",
    "description": "Mock endpoint number 275 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 275, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_276 = {
    "endpoint": "/v1/resource/276",
    "method": "GET",
    "description": "Mock endpoint number 276 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 276, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_277 = {
    "endpoint": "/v1/resource/277",
    "method": "GET",
    "description": "Mock endpoint number 277 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 277, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_278 = {
    "endpoint": "/v1/resource/278",
    "method": "GET",
    "description": "Mock endpoint number 278 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 278, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_279 = {
    "endpoint": "/v1/resource/279",
    "method": "GET",
    "description": "Mock endpoint number 279 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 279, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_280 = {
    "endpoint": "/v1/resource/280",
    "method": "GET",
    "description": "Mock endpoint number 280 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 280, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_281 = {
    "endpoint": "/v1/resource/281",
    "method": "GET",
    "description": "Mock endpoint number 281 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 281, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_282 = {
    "endpoint": "/v1/resource/282",
    "method": "GET",
    "description": "Mock endpoint number 282 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 282, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_283 = {
    "endpoint": "/v1/resource/283",
    "method": "GET",
    "description": "Mock endpoint number 283 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 283, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_284 = {
    "endpoint": "/v1/resource/284",
    "method": "GET",
    "description": "Mock endpoint number 284 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 284, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_285 = {
    "endpoint": "/v1/resource/285",
    "method": "GET",
    "description": "Mock endpoint number 285 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 285, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_286 = {
    "endpoint": "/v1/resource/286",
    "method": "GET",
    "description": "Mock endpoint number 286 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 286, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_287 = {
    "endpoint": "/v1/resource/287",
    "method": "GET",
    "description": "Mock endpoint number 287 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 287, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_288 = {
    "endpoint": "/v1/resource/288",
    "method": "GET",
    "description": "Mock endpoint number 288 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 288, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_289 = {
    "endpoint": "/v1/resource/289",
    "method": "GET",
    "description": "Mock endpoint number 289 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 289, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_290 = {
    "endpoint": "/v1/resource/290",
    "method": "GET",
    "description": "Mock endpoint number 290 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 290, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_291 = {
    "endpoint": "/v1/resource/291",
    "method": "GET",
    "description": "Mock endpoint number 291 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 291, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_292 = {
    "endpoint": "/v1/resource/292",
    "method": "GET",
    "description": "Mock endpoint number 292 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 292, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_293 = {
    "endpoint": "/v1/resource/293",
    "method": "GET",
    "description": "Mock endpoint number 293 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 293, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_294 = {
    "endpoint": "/v1/resource/294",
    "method": "GET",
    "description": "Mock endpoint number 294 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 294, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_295 = {
    "endpoint": "/v1/resource/295",
    "method": "GET",
    "description": "Mock endpoint number 295 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 295, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_296 = {
    "endpoint": "/v1/resource/296",
    "method": "GET",
    "description": "Mock endpoint number 296 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 296, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_297 = {
    "endpoint": "/v1/resource/297",
    "method": "GET",
    "description": "Mock endpoint number 297 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 297, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_298 = {
    "endpoint": "/v1/resource/298",
    "method": "GET",
    "description": "Mock endpoint number 298 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 298, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}


MOCK_RESPONSE_TEMPLATE_299 = {
    "endpoint": "/v1/resource/299",
    "method": "GET",
    "description": "Mock endpoint number 299 for demonstration of API response structures and documentation generation.",
    "parameters": [
        {"name": "limit", "type": "integer", "default": 20},
        {"name": "offset", "type": "integer", "default": 0},
        {"name": "filter", "type": "string", "required": False},
    ],
    "response_schema": {
        "type": "object",
        "properties": {
            "data": {"type": "array"},
            "total": {"type": "integer"},
            "page": {"type": "integer"},
        },
    },
    "example_response": {
        "data": [{"id": 299, "value": "sample"}],
        "total": 1,
        "page": 1,
    },
}
