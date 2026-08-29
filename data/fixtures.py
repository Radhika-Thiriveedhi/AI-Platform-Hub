"""Test fixtures and sample data generators for AI Platform Hub."""

from typing import List, Dict, Any
import random


SAMPLE_RECORD_0000 = {
    "id": "sample-0000",
    "title": "Sample Record Title Number 0",
    "description": "This is a detailed description for sample record 0. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.0,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 0.",
    },
}


SAMPLE_RECORD_0001 = {
    "id": "sample-0001",
    "title": "Sample Record Title Number 1",
    "description": "This is a detailed description for sample record 1. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.17,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 1.",
    },
}


SAMPLE_RECORD_0002 = {
    "id": "sample-0002",
    "title": "Sample Record Title Number 2",
    "description": "This is a detailed description for sample record 2. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.34,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 2.",
    },
}


SAMPLE_RECORD_0003 = {
    "id": "sample-0003",
    "title": "Sample Record Title Number 3",
    "description": "This is a detailed description for sample record 3. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.51,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 3.",
    },
}


SAMPLE_RECORD_0004 = {
    "id": "sample-0004",
    "title": "Sample Record Title Number 4",
    "description": "This is a detailed description for sample record 4. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.68,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 4.",
    },
}


SAMPLE_RECORD_0005 = {
    "id": "sample-0005",
    "title": "Sample Record Title Number 5",
    "description": "This is a detailed description for sample record 5. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.85,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 5.",
    },
}


SAMPLE_RECORD_0006 = {
    "id": "sample-0006",
    "title": "Sample Record Title Number 6",
    "description": "This is a detailed description for sample record 6. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.02,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 6.",
    },
}


SAMPLE_RECORD_0007 = {
    "id": "sample-0007",
    "title": "Sample Record Title Number 7",
    "description": "This is a detailed description for sample record 7. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.19,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 7.",
    },
}


SAMPLE_RECORD_0008 = {
    "id": "sample-0008",
    "title": "Sample Record Title Number 8",
    "description": "This is a detailed description for sample record 8. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.36,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 8.",
    },
}


SAMPLE_RECORD_0009 = {
    "id": "sample-0009",
    "title": "Sample Record Title Number 9",
    "description": "This is a detailed description for sample record 9. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.53,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 9.",
    },
}


SAMPLE_RECORD_0010 = {
    "id": "sample-0010",
    "title": "Sample Record Title Number 10",
    "description": "This is a detailed description for sample record 10. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.7,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 10.",
    },
}


SAMPLE_RECORD_0011 = {
    "id": "sample-0011",
    "title": "Sample Record Title Number 11",
    "description": "This is a detailed description for sample record 11. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.87,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 11.",
    },
}


SAMPLE_RECORD_0012 = {
    "id": "sample-0012",
    "title": "Sample Record Title Number 12",
    "description": "This is a detailed description for sample record 12. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.04,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 12.",
    },
}


SAMPLE_RECORD_0013 = {
    "id": "sample-0013",
    "title": "Sample Record Title Number 13",
    "description": "This is a detailed description for sample record 13. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.21,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 13.",
    },
}


SAMPLE_RECORD_0014 = {
    "id": "sample-0014",
    "title": "Sample Record Title Number 14",
    "description": "This is a detailed description for sample record 14. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.38,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 14.",
    },
}


SAMPLE_RECORD_0015 = {
    "id": "sample-0015",
    "title": "Sample Record Title Number 15",
    "description": "This is a detailed description for sample record 15. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.55,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 15.",
    },
}


SAMPLE_RECORD_0016 = {
    "id": "sample-0016",
    "title": "Sample Record Title Number 16",
    "description": "This is a detailed description for sample record 16. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.72,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 16.",
    },
}


SAMPLE_RECORD_0017 = {
    "id": "sample-0017",
    "title": "Sample Record Title Number 17",
    "description": "This is a detailed description for sample record 17. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.89,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 17.",
    },
}


SAMPLE_RECORD_0018 = {
    "id": "sample-0018",
    "title": "Sample Record Title Number 18",
    "description": "This is a detailed description for sample record 18. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.06,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 18.",
    },
}


SAMPLE_RECORD_0019 = {
    "id": "sample-0019",
    "title": "Sample Record Title Number 19",
    "description": "This is a detailed description for sample record 19. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.23,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 19.",
    },
}


SAMPLE_RECORD_0020 = {
    "id": "sample-0020",
    "title": "Sample Record Title Number 20",
    "description": "This is a detailed description for sample record 20. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.4,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 20.",
    },
}


SAMPLE_RECORD_0021 = {
    "id": "sample-0021",
    "title": "Sample Record Title Number 21",
    "description": "This is a detailed description for sample record 21. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.57,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 21.",
    },
}


SAMPLE_RECORD_0022 = {
    "id": "sample-0022",
    "title": "Sample Record Title Number 22",
    "description": "This is a detailed description for sample record 22. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.74,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 22.",
    },
}


SAMPLE_RECORD_0023 = {
    "id": "sample-0023",
    "title": "Sample Record Title Number 23",
    "description": "This is a detailed description for sample record 23. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.91,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 23.",
    },
}


SAMPLE_RECORD_0024 = {
    "id": "sample-0024",
    "title": "Sample Record Title Number 24",
    "description": "This is a detailed description for sample record 24. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.08,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 24.",
    },
}


SAMPLE_RECORD_0025 = {
    "id": "sample-0025",
    "title": "Sample Record Title Number 25",
    "description": "This is a detailed description for sample record 25. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.25,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 25.",
    },
}


SAMPLE_RECORD_0026 = {
    "id": "sample-0026",
    "title": "Sample Record Title Number 26",
    "description": "This is a detailed description for sample record 26. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.42,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 26.",
    },
}


SAMPLE_RECORD_0027 = {
    "id": "sample-0027",
    "title": "Sample Record Title Number 27",
    "description": "This is a detailed description for sample record 27. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.59,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 27.",
    },
}


SAMPLE_RECORD_0028 = {
    "id": "sample-0028",
    "title": "Sample Record Title Number 28",
    "description": "This is a detailed description for sample record 28. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.76,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 28.",
    },
}


SAMPLE_RECORD_0029 = {
    "id": "sample-0029",
    "title": "Sample Record Title Number 29",
    "description": "This is a detailed description for sample record 29. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.93,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 29.",
    },
}


SAMPLE_RECORD_0030 = {
    "id": "sample-0030",
    "title": "Sample Record Title Number 30",
    "description": "This is a detailed description for sample record 30. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.1,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 30.",
    },
}


SAMPLE_RECORD_0031 = {
    "id": "sample-0031",
    "title": "Sample Record Title Number 31",
    "description": "This is a detailed description for sample record 31. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.27,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 31.",
    },
}


SAMPLE_RECORD_0032 = {
    "id": "sample-0032",
    "title": "Sample Record Title Number 32",
    "description": "This is a detailed description for sample record 32. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.44,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 32.",
    },
}


SAMPLE_RECORD_0033 = {
    "id": "sample-0033",
    "title": "Sample Record Title Number 33",
    "description": "This is a detailed description for sample record 33. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.61,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 33.",
    },
}


SAMPLE_RECORD_0034 = {
    "id": "sample-0034",
    "title": "Sample Record Title Number 34",
    "description": "This is a detailed description for sample record 34. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.78,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 34.",
    },
}


SAMPLE_RECORD_0035 = {
    "id": "sample-0035",
    "title": "Sample Record Title Number 35",
    "description": "This is a detailed description for sample record 35. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.95,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 35.",
    },
}


SAMPLE_RECORD_0036 = {
    "id": "sample-0036",
    "title": "Sample Record Title Number 36",
    "description": "This is a detailed description for sample record 36. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.12,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 36.",
    },
}


SAMPLE_RECORD_0037 = {
    "id": "sample-0037",
    "title": "Sample Record Title Number 37",
    "description": "This is a detailed description for sample record 37. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.29,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 37.",
    },
}


SAMPLE_RECORD_0038 = {
    "id": "sample-0038",
    "title": "Sample Record Title Number 38",
    "description": "This is a detailed description for sample record 38. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.46,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 38.",
    },
}


SAMPLE_RECORD_0039 = {
    "id": "sample-0039",
    "title": "Sample Record Title Number 39",
    "description": "This is a detailed description for sample record 39. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.63,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 39.",
    },
}


SAMPLE_RECORD_0040 = {
    "id": "sample-0040",
    "title": "Sample Record Title Number 40",
    "description": "This is a detailed description for sample record 40. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.8,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 40.",
    },
}


SAMPLE_RECORD_0041 = {
    "id": "sample-0041",
    "title": "Sample Record Title Number 41",
    "description": "This is a detailed description for sample record 41. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.97,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 41.",
    },
}


SAMPLE_RECORD_0042 = {
    "id": "sample-0042",
    "title": "Sample Record Title Number 42",
    "description": "This is a detailed description for sample record 42. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.14,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 42.",
    },
}


SAMPLE_RECORD_0043 = {
    "id": "sample-0043",
    "title": "Sample Record Title Number 43",
    "description": "This is a detailed description for sample record 43. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.31,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 43.",
    },
}


SAMPLE_RECORD_0044 = {
    "id": "sample-0044",
    "title": "Sample Record Title Number 44",
    "description": "This is a detailed description for sample record 44. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.48,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 44.",
    },
}


SAMPLE_RECORD_0045 = {
    "id": "sample-0045",
    "title": "Sample Record Title Number 45",
    "description": "This is a detailed description for sample record 45. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.65,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 45.",
    },
}


SAMPLE_RECORD_0046 = {
    "id": "sample-0046",
    "title": "Sample Record Title Number 46",
    "description": "This is a detailed description for sample record 46. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.82,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 46.",
    },
}


SAMPLE_RECORD_0047 = {
    "id": "sample-0047",
    "title": "Sample Record Title Number 47",
    "description": "This is a detailed description for sample record 47. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.99,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 47.",
    },
}


SAMPLE_RECORD_0048 = {
    "id": "sample-0048",
    "title": "Sample Record Title Number 48",
    "description": "This is a detailed description for sample record 48. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.16,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 48.",
    },
}


SAMPLE_RECORD_0049 = {
    "id": "sample-0049",
    "title": "Sample Record Title Number 49",
    "description": "This is a detailed description for sample record 49. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.33,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 49.",
    },
}


SAMPLE_RECORD_0050 = {
    "id": "sample-0050",
    "title": "Sample Record Title Number 50",
    "description": "This is a detailed description for sample record 50. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.5,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 50.",
    },
}


SAMPLE_RECORD_0051 = {
    "id": "sample-0051",
    "title": "Sample Record Title Number 51",
    "description": "This is a detailed description for sample record 51. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.67,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 51.",
    },
}


SAMPLE_RECORD_0052 = {
    "id": "sample-0052",
    "title": "Sample Record Title Number 52",
    "description": "This is a detailed description for sample record 52. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.84,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 52.",
    },
}


SAMPLE_RECORD_0053 = {
    "id": "sample-0053",
    "title": "Sample Record Title Number 53",
    "description": "This is a detailed description for sample record 53. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.01,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 53.",
    },
}


SAMPLE_RECORD_0054 = {
    "id": "sample-0054",
    "title": "Sample Record Title Number 54",
    "description": "This is a detailed description for sample record 54. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.18,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 54.",
    },
}


SAMPLE_RECORD_0055 = {
    "id": "sample-0055",
    "title": "Sample Record Title Number 55",
    "description": "This is a detailed description for sample record 55. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.35,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 55.",
    },
}


SAMPLE_RECORD_0056 = {
    "id": "sample-0056",
    "title": "Sample Record Title Number 56",
    "description": "This is a detailed description for sample record 56. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.52,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 56.",
    },
}


SAMPLE_RECORD_0057 = {
    "id": "sample-0057",
    "title": "Sample Record Title Number 57",
    "description": "This is a detailed description for sample record 57. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.69,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 57.",
    },
}


SAMPLE_RECORD_0058 = {
    "id": "sample-0058",
    "title": "Sample Record Title Number 58",
    "description": "This is a detailed description for sample record 58. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.86,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 58.",
    },
}


SAMPLE_RECORD_0059 = {
    "id": "sample-0059",
    "title": "Sample Record Title Number 59",
    "description": "This is a detailed description for sample record 59. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.03,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 59.",
    },
}


SAMPLE_RECORD_0060 = {
    "id": "sample-0060",
    "title": "Sample Record Title Number 60",
    "description": "This is a detailed description for sample record 60. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.2,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 60.",
    },
}


SAMPLE_RECORD_0061 = {
    "id": "sample-0061",
    "title": "Sample Record Title Number 61",
    "description": "This is a detailed description for sample record 61. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.37,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 61.",
    },
}


SAMPLE_RECORD_0062 = {
    "id": "sample-0062",
    "title": "Sample Record Title Number 62",
    "description": "This is a detailed description for sample record 62. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.54,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 62.",
    },
}


SAMPLE_RECORD_0063 = {
    "id": "sample-0063",
    "title": "Sample Record Title Number 63",
    "description": "This is a detailed description for sample record 63. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.71,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 63.",
    },
}


SAMPLE_RECORD_0064 = {
    "id": "sample-0064",
    "title": "Sample Record Title Number 64",
    "description": "This is a detailed description for sample record 64. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.88,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 64.",
    },
}


SAMPLE_RECORD_0065 = {
    "id": "sample-0065",
    "title": "Sample Record Title Number 65",
    "description": "This is a detailed description for sample record 65. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.05,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 65.",
    },
}


SAMPLE_RECORD_0066 = {
    "id": "sample-0066",
    "title": "Sample Record Title Number 66",
    "description": "This is a detailed description for sample record 66. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.22,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 66.",
    },
}


SAMPLE_RECORD_0067 = {
    "id": "sample-0067",
    "title": "Sample Record Title Number 67",
    "description": "This is a detailed description for sample record 67. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.39,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 67.",
    },
}


SAMPLE_RECORD_0068 = {
    "id": "sample-0068",
    "title": "Sample Record Title Number 68",
    "description": "This is a detailed description for sample record 68. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.56,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 68.",
    },
}


SAMPLE_RECORD_0069 = {
    "id": "sample-0069",
    "title": "Sample Record Title Number 69",
    "description": "This is a detailed description for sample record 69. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.73,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 69.",
    },
}


SAMPLE_RECORD_0070 = {
    "id": "sample-0070",
    "title": "Sample Record Title Number 70",
    "description": "This is a detailed description for sample record 70. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.9,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 70.",
    },
}


SAMPLE_RECORD_0071 = {
    "id": "sample-0071",
    "title": "Sample Record Title Number 71",
    "description": "This is a detailed description for sample record 71. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.07,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 71.",
    },
}


SAMPLE_RECORD_0072 = {
    "id": "sample-0072",
    "title": "Sample Record Title Number 72",
    "description": "This is a detailed description for sample record 72. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.24,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 72.",
    },
}


SAMPLE_RECORD_0073 = {
    "id": "sample-0073",
    "title": "Sample Record Title Number 73",
    "description": "This is a detailed description for sample record 73. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.41,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 73.",
    },
}


SAMPLE_RECORD_0074 = {
    "id": "sample-0074",
    "title": "Sample Record Title Number 74",
    "description": "This is a detailed description for sample record 74. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.58,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 74.",
    },
}


SAMPLE_RECORD_0075 = {
    "id": "sample-0075",
    "title": "Sample Record Title Number 75",
    "description": "This is a detailed description for sample record 75. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.75,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 75.",
    },
}


SAMPLE_RECORD_0076 = {
    "id": "sample-0076",
    "title": "Sample Record Title Number 76",
    "description": "This is a detailed description for sample record 76. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.92,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 76.",
    },
}


SAMPLE_RECORD_0077 = {
    "id": "sample-0077",
    "title": "Sample Record Title Number 77",
    "description": "This is a detailed description for sample record 77. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.09,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 77.",
    },
}


SAMPLE_RECORD_0078 = {
    "id": "sample-0078",
    "title": "Sample Record Title Number 78",
    "description": "This is a detailed description for sample record 78. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.26,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 78.",
    },
}


SAMPLE_RECORD_0079 = {
    "id": "sample-0079",
    "title": "Sample Record Title Number 79",
    "description": "This is a detailed description for sample record 79. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.43,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 79.",
    },
}


SAMPLE_RECORD_0080 = {
    "id": "sample-0080",
    "title": "Sample Record Title Number 80",
    "description": "This is a detailed description for sample record 80. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.6,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 80.",
    },
}


SAMPLE_RECORD_0081 = {
    "id": "sample-0081",
    "title": "Sample Record Title Number 81",
    "description": "This is a detailed description for sample record 81. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.77,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 81.",
    },
}


SAMPLE_RECORD_0082 = {
    "id": "sample-0082",
    "title": "Sample Record Title Number 82",
    "description": "This is a detailed description for sample record 82. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.94,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 82.",
    },
}


SAMPLE_RECORD_0083 = {
    "id": "sample-0083",
    "title": "Sample Record Title Number 83",
    "description": "This is a detailed description for sample record 83. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.11,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 83.",
    },
}


SAMPLE_RECORD_0084 = {
    "id": "sample-0084",
    "title": "Sample Record Title Number 84",
    "description": "This is a detailed description for sample record 84. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.28,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 84.",
    },
}


SAMPLE_RECORD_0085 = {
    "id": "sample-0085",
    "title": "Sample Record Title Number 85",
    "description": "This is a detailed description for sample record 85. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.45,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 85.",
    },
}


SAMPLE_RECORD_0086 = {
    "id": "sample-0086",
    "title": "Sample Record Title Number 86",
    "description": "This is a detailed description for sample record 86. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.62,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 86.",
    },
}


SAMPLE_RECORD_0087 = {
    "id": "sample-0087",
    "title": "Sample Record Title Number 87",
    "description": "This is a detailed description for sample record 87. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.79,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 87.",
    },
}


SAMPLE_RECORD_0088 = {
    "id": "sample-0088",
    "title": "Sample Record Title Number 88",
    "description": "This is a detailed description for sample record 88. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.96,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 88.",
    },
}


SAMPLE_RECORD_0089 = {
    "id": "sample-0089",
    "title": "Sample Record Title Number 89",
    "description": "This is a detailed description for sample record 89. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.13,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 89.",
    },
}


SAMPLE_RECORD_0090 = {
    "id": "sample-0090",
    "title": "Sample Record Title Number 90",
    "description": "This is a detailed description for sample record 90. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.3,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 90.",
    },
}


SAMPLE_RECORD_0091 = {
    "id": "sample-0091",
    "title": "Sample Record Title Number 91",
    "description": "This is a detailed description for sample record 91. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.47,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 91.",
    },
}


SAMPLE_RECORD_0092 = {
    "id": "sample-0092",
    "title": "Sample Record Title Number 92",
    "description": "This is a detailed description for sample record 92. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.64,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 92.",
    },
}


SAMPLE_RECORD_0093 = {
    "id": "sample-0093",
    "title": "Sample Record Title Number 93",
    "description": "This is a detailed description for sample record 93. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.81,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 93.",
    },
}


SAMPLE_RECORD_0094 = {
    "id": "sample-0094",
    "title": "Sample Record Title Number 94",
    "description": "This is a detailed description for sample record 94. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.98,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 94.",
    },
}


SAMPLE_RECORD_0095 = {
    "id": "sample-0095",
    "title": "Sample Record Title Number 95",
    "description": "This is a detailed description for sample record 95. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.15,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 95.",
    },
}


SAMPLE_RECORD_0096 = {
    "id": "sample-0096",
    "title": "Sample Record Title Number 96",
    "description": "This is a detailed description for sample record 96. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.32,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 96.",
    },
}


SAMPLE_RECORD_0097 = {
    "id": "sample-0097",
    "title": "Sample Record Title Number 97",
    "description": "This is a detailed description for sample record 97. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.49,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 97.",
    },
}


SAMPLE_RECORD_0098 = {
    "id": "sample-0098",
    "title": "Sample Record Title Number 98",
    "description": "This is a detailed description for sample record 98. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.66,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 98.",
    },
}


SAMPLE_RECORD_0099 = {
    "id": "sample-0099",
    "title": "Sample Record Title Number 99",
    "description": "This is a detailed description for sample record 99. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.83,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 99.",
    },
}


SAMPLE_RECORD_0100 = {
    "id": "sample-0100",
    "title": "Sample Record Title Number 100",
    "description": "This is a detailed description for sample record 100. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.0,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 100.",
    },
}


SAMPLE_RECORD_0101 = {
    "id": "sample-0101",
    "title": "Sample Record Title Number 101",
    "description": "This is a detailed description for sample record 101. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.17,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 101.",
    },
}


SAMPLE_RECORD_0102 = {
    "id": "sample-0102",
    "title": "Sample Record Title Number 102",
    "description": "This is a detailed description for sample record 102. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.34,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 102.",
    },
}


SAMPLE_RECORD_0103 = {
    "id": "sample-0103",
    "title": "Sample Record Title Number 103",
    "description": "This is a detailed description for sample record 103. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.51,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 103.",
    },
}


SAMPLE_RECORD_0104 = {
    "id": "sample-0104",
    "title": "Sample Record Title Number 104",
    "description": "This is a detailed description for sample record 104. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.68,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 104.",
    },
}


SAMPLE_RECORD_0105 = {
    "id": "sample-0105",
    "title": "Sample Record Title Number 105",
    "description": "This is a detailed description for sample record 105. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.85,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 105.",
    },
}


SAMPLE_RECORD_0106 = {
    "id": "sample-0106",
    "title": "Sample Record Title Number 106",
    "description": "This is a detailed description for sample record 106. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.02,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 106.",
    },
}


SAMPLE_RECORD_0107 = {
    "id": "sample-0107",
    "title": "Sample Record Title Number 107",
    "description": "This is a detailed description for sample record 107. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.19,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 107.",
    },
}


SAMPLE_RECORD_0108 = {
    "id": "sample-0108",
    "title": "Sample Record Title Number 108",
    "description": "This is a detailed description for sample record 108. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.36,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 108.",
    },
}


SAMPLE_RECORD_0109 = {
    "id": "sample-0109",
    "title": "Sample Record Title Number 109",
    "description": "This is a detailed description for sample record 109. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.53,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 109.",
    },
}


SAMPLE_RECORD_0110 = {
    "id": "sample-0110",
    "title": "Sample Record Title Number 110",
    "description": "This is a detailed description for sample record 110. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.7,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 110.",
    },
}


SAMPLE_RECORD_0111 = {
    "id": "sample-0111",
    "title": "Sample Record Title Number 111",
    "description": "This is a detailed description for sample record 111. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.87,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 111.",
    },
}


SAMPLE_RECORD_0112 = {
    "id": "sample-0112",
    "title": "Sample Record Title Number 112",
    "description": "This is a detailed description for sample record 112. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.04,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 112.",
    },
}


SAMPLE_RECORD_0113 = {
    "id": "sample-0113",
    "title": "Sample Record Title Number 113",
    "description": "This is a detailed description for sample record 113. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.21,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 113.",
    },
}


SAMPLE_RECORD_0114 = {
    "id": "sample-0114",
    "title": "Sample Record Title Number 114",
    "description": "This is a detailed description for sample record 114. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.38,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 114.",
    },
}


SAMPLE_RECORD_0115 = {
    "id": "sample-0115",
    "title": "Sample Record Title Number 115",
    "description": "This is a detailed description for sample record 115. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.55,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 115.",
    },
}


SAMPLE_RECORD_0116 = {
    "id": "sample-0116",
    "title": "Sample Record Title Number 116",
    "description": "This is a detailed description for sample record 116. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.72,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 116.",
    },
}


SAMPLE_RECORD_0117 = {
    "id": "sample-0117",
    "title": "Sample Record Title Number 117",
    "description": "This is a detailed description for sample record 117. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.89,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 117.",
    },
}


SAMPLE_RECORD_0118 = {
    "id": "sample-0118",
    "title": "Sample Record Title Number 118",
    "description": "This is a detailed description for sample record 118. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.06,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 118.",
    },
}


SAMPLE_RECORD_0119 = {
    "id": "sample-0119",
    "title": "Sample Record Title Number 119",
    "description": "This is a detailed description for sample record 119. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.23,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 119.",
    },
}


SAMPLE_RECORD_0120 = {
    "id": "sample-0120",
    "title": "Sample Record Title Number 120",
    "description": "This is a detailed description for sample record 120. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.4,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 120.",
    },
}


SAMPLE_RECORD_0121 = {
    "id": "sample-0121",
    "title": "Sample Record Title Number 121",
    "description": "This is a detailed description for sample record 121. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.57,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 121.",
    },
}


SAMPLE_RECORD_0122 = {
    "id": "sample-0122",
    "title": "Sample Record Title Number 122",
    "description": "This is a detailed description for sample record 122. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.74,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 122.",
    },
}


SAMPLE_RECORD_0123 = {
    "id": "sample-0123",
    "title": "Sample Record Title Number 123",
    "description": "This is a detailed description for sample record 123. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.91,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 123.",
    },
}


SAMPLE_RECORD_0124 = {
    "id": "sample-0124",
    "title": "Sample Record Title Number 124",
    "description": "This is a detailed description for sample record 124. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.08,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 124.",
    },
}


SAMPLE_RECORD_0125 = {
    "id": "sample-0125",
    "title": "Sample Record Title Number 125",
    "description": "This is a detailed description for sample record 125. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.25,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 125.",
    },
}


SAMPLE_RECORD_0126 = {
    "id": "sample-0126",
    "title": "Sample Record Title Number 126",
    "description": "This is a detailed description for sample record 126. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.42,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 126.",
    },
}


SAMPLE_RECORD_0127 = {
    "id": "sample-0127",
    "title": "Sample Record Title Number 127",
    "description": "This is a detailed description for sample record 127. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.59,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 127.",
    },
}


SAMPLE_RECORD_0128 = {
    "id": "sample-0128",
    "title": "Sample Record Title Number 128",
    "description": "This is a detailed description for sample record 128. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.76,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 128.",
    },
}


SAMPLE_RECORD_0129 = {
    "id": "sample-0129",
    "title": "Sample Record Title Number 129",
    "description": "This is a detailed description for sample record 129. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.93,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 129.",
    },
}


SAMPLE_RECORD_0130 = {
    "id": "sample-0130",
    "title": "Sample Record Title Number 130",
    "description": "This is a detailed description for sample record 130. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.1,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 130.",
    },
}


SAMPLE_RECORD_0131 = {
    "id": "sample-0131",
    "title": "Sample Record Title Number 131",
    "description": "This is a detailed description for sample record 131. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.27,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 131.",
    },
}


SAMPLE_RECORD_0132 = {
    "id": "sample-0132",
    "title": "Sample Record Title Number 132",
    "description": "This is a detailed description for sample record 132. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.44,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 132.",
    },
}


SAMPLE_RECORD_0133 = {
    "id": "sample-0133",
    "title": "Sample Record Title Number 133",
    "description": "This is a detailed description for sample record 133. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.61,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 133.",
    },
}


SAMPLE_RECORD_0134 = {
    "id": "sample-0134",
    "title": "Sample Record Title Number 134",
    "description": "This is a detailed description for sample record 134. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.78,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 134.",
    },
}


SAMPLE_RECORD_0135 = {
    "id": "sample-0135",
    "title": "Sample Record Title Number 135",
    "description": "This is a detailed description for sample record 135. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.95,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 135.",
    },
}


SAMPLE_RECORD_0136 = {
    "id": "sample-0136",
    "title": "Sample Record Title Number 136",
    "description": "This is a detailed description for sample record 136. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.12,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 136.",
    },
}


SAMPLE_RECORD_0137 = {
    "id": "sample-0137",
    "title": "Sample Record Title Number 137",
    "description": "This is a detailed description for sample record 137. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.29,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 137.",
    },
}


SAMPLE_RECORD_0138 = {
    "id": "sample-0138",
    "title": "Sample Record Title Number 138",
    "description": "This is a detailed description for sample record 138. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.46,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 138.",
    },
}


SAMPLE_RECORD_0139 = {
    "id": "sample-0139",
    "title": "Sample Record Title Number 139",
    "description": "This is a detailed description for sample record 139. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.63,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 139.",
    },
}


SAMPLE_RECORD_0140 = {
    "id": "sample-0140",
    "title": "Sample Record Title Number 140",
    "description": "This is a detailed description for sample record 140. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.8,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 140.",
    },
}


SAMPLE_RECORD_0141 = {
    "id": "sample-0141",
    "title": "Sample Record Title Number 141",
    "description": "This is a detailed description for sample record 141. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.97,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 141.",
    },
}


SAMPLE_RECORD_0142 = {
    "id": "sample-0142",
    "title": "Sample Record Title Number 142",
    "description": "This is a detailed description for sample record 142. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.14,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 142.",
    },
}


SAMPLE_RECORD_0143 = {
    "id": "sample-0143",
    "title": "Sample Record Title Number 143",
    "description": "This is a detailed description for sample record 143. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.31,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 143.",
    },
}


SAMPLE_RECORD_0144 = {
    "id": "sample-0144",
    "title": "Sample Record Title Number 144",
    "description": "This is a detailed description for sample record 144. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.48,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 144.",
    },
}


SAMPLE_RECORD_0145 = {
    "id": "sample-0145",
    "title": "Sample Record Title Number 145",
    "description": "This is a detailed description for sample record 145. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.65,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 145.",
    },
}


SAMPLE_RECORD_0146 = {
    "id": "sample-0146",
    "title": "Sample Record Title Number 146",
    "description": "This is a detailed description for sample record 146. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.82,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 146.",
    },
}


SAMPLE_RECORD_0147 = {
    "id": "sample-0147",
    "title": "Sample Record Title Number 147",
    "description": "This is a detailed description for sample record 147. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.99,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 147.",
    },
}


SAMPLE_RECORD_0148 = {
    "id": "sample-0148",
    "title": "Sample Record Title Number 148",
    "description": "This is a detailed description for sample record 148. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.16,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 148.",
    },
}


SAMPLE_RECORD_0149 = {
    "id": "sample-0149",
    "title": "Sample Record Title Number 149",
    "description": "This is a detailed description for sample record 149. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.33,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 149.",
    },
}


SAMPLE_RECORD_0150 = {
    "id": "sample-0150",
    "title": "Sample Record Title Number 150",
    "description": "This is a detailed description for sample record 150. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.5,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 150.",
    },
}


SAMPLE_RECORD_0151 = {
    "id": "sample-0151",
    "title": "Sample Record Title Number 151",
    "description": "This is a detailed description for sample record 151. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.67,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 151.",
    },
}


SAMPLE_RECORD_0152 = {
    "id": "sample-0152",
    "title": "Sample Record Title Number 152",
    "description": "This is a detailed description for sample record 152. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.84,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 152.",
    },
}


SAMPLE_RECORD_0153 = {
    "id": "sample-0153",
    "title": "Sample Record Title Number 153",
    "description": "This is a detailed description for sample record 153. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.01,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 153.",
    },
}


SAMPLE_RECORD_0154 = {
    "id": "sample-0154",
    "title": "Sample Record Title Number 154",
    "description": "This is a detailed description for sample record 154. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.18,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 154.",
    },
}


SAMPLE_RECORD_0155 = {
    "id": "sample-0155",
    "title": "Sample Record Title Number 155",
    "description": "This is a detailed description for sample record 155. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.35,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 155.",
    },
}


SAMPLE_RECORD_0156 = {
    "id": "sample-0156",
    "title": "Sample Record Title Number 156",
    "description": "This is a detailed description for sample record 156. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.52,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 156.",
    },
}


SAMPLE_RECORD_0157 = {
    "id": "sample-0157",
    "title": "Sample Record Title Number 157",
    "description": "This is a detailed description for sample record 157. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.69,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 157.",
    },
}


SAMPLE_RECORD_0158 = {
    "id": "sample-0158",
    "title": "Sample Record Title Number 158",
    "description": "This is a detailed description for sample record 158. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.86,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 158.",
    },
}


SAMPLE_RECORD_0159 = {
    "id": "sample-0159",
    "title": "Sample Record Title Number 159",
    "description": "This is a detailed description for sample record 159. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.03,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 159.",
    },
}


SAMPLE_RECORD_0160 = {
    "id": "sample-0160",
    "title": "Sample Record Title Number 160",
    "description": "This is a detailed description for sample record 160. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.2,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 160.",
    },
}


SAMPLE_RECORD_0161 = {
    "id": "sample-0161",
    "title": "Sample Record Title Number 161",
    "description": "This is a detailed description for sample record 161. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.37,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 161.",
    },
}


SAMPLE_RECORD_0162 = {
    "id": "sample-0162",
    "title": "Sample Record Title Number 162",
    "description": "This is a detailed description for sample record 162. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.54,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 162.",
    },
}


SAMPLE_RECORD_0163 = {
    "id": "sample-0163",
    "title": "Sample Record Title Number 163",
    "description": "This is a detailed description for sample record 163. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.71,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 163.",
    },
}


SAMPLE_RECORD_0164 = {
    "id": "sample-0164",
    "title": "Sample Record Title Number 164",
    "description": "This is a detailed description for sample record 164. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.88,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 164.",
    },
}


SAMPLE_RECORD_0165 = {
    "id": "sample-0165",
    "title": "Sample Record Title Number 165",
    "description": "This is a detailed description for sample record 165. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.05,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 165.",
    },
}


SAMPLE_RECORD_0166 = {
    "id": "sample-0166",
    "title": "Sample Record Title Number 166",
    "description": "This is a detailed description for sample record 166. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.22,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 166.",
    },
}


SAMPLE_RECORD_0167 = {
    "id": "sample-0167",
    "title": "Sample Record Title Number 167",
    "description": "This is a detailed description for sample record 167. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.39,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 167.",
    },
}


SAMPLE_RECORD_0168 = {
    "id": "sample-0168",
    "title": "Sample Record Title Number 168",
    "description": "This is a detailed description for sample record 168. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.56,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 168.",
    },
}


SAMPLE_RECORD_0169 = {
    "id": "sample-0169",
    "title": "Sample Record Title Number 169",
    "description": "This is a detailed description for sample record 169. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.73,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 169.",
    },
}


SAMPLE_RECORD_0170 = {
    "id": "sample-0170",
    "title": "Sample Record Title Number 170",
    "description": "This is a detailed description for sample record 170. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.9,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 170.",
    },
}


SAMPLE_RECORD_0171 = {
    "id": "sample-0171",
    "title": "Sample Record Title Number 171",
    "description": "This is a detailed description for sample record 171. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.07,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 171.",
    },
}


SAMPLE_RECORD_0172 = {
    "id": "sample-0172",
    "title": "Sample Record Title Number 172",
    "description": "This is a detailed description for sample record 172. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.24,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 172.",
    },
}


SAMPLE_RECORD_0173 = {
    "id": "sample-0173",
    "title": "Sample Record Title Number 173",
    "description": "This is a detailed description for sample record 173. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.41,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 173.",
    },
}


SAMPLE_RECORD_0174 = {
    "id": "sample-0174",
    "title": "Sample Record Title Number 174",
    "description": "This is a detailed description for sample record 174. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.58,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 174.",
    },
}


SAMPLE_RECORD_0175 = {
    "id": "sample-0175",
    "title": "Sample Record Title Number 175",
    "description": "This is a detailed description for sample record 175. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.75,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 175.",
    },
}


SAMPLE_RECORD_0176 = {
    "id": "sample-0176",
    "title": "Sample Record Title Number 176",
    "description": "This is a detailed description for sample record 176. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.92,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 176.",
    },
}


SAMPLE_RECORD_0177 = {
    "id": "sample-0177",
    "title": "Sample Record Title Number 177",
    "description": "This is a detailed description for sample record 177. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.09,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 177.",
    },
}


SAMPLE_RECORD_0178 = {
    "id": "sample-0178",
    "title": "Sample Record Title Number 178",
    "description": "This is a detailed description for sample record 178. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.26,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 178.",
    },
}


SAMPLE_RECORD_0179 = {
    "id": "sample-0179",
    "title": "Sample Record Title Number 179",
    "description": "This is a detailed description for sample record 179. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.43,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 179.",
    },
}


SAMPLE_RECORD_0180 = {
    "id": "sample-0180",
    "title": "Sample Record Title Number 180",
    "description": "This is a detailed description for sample record 180. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.6,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 180.",
    },
}


SAMPLE_RECORD_0181 = {
    "id": "sample-0181",
    "title": "Sample Record Title Number 181",
    "description": "This is a detailed description for sample record 181. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.77,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 181.",
    },
}


SAMPLE_RECORD_0182 = {
    "id": "sample-0182",
    "title": "Sample Record Title Number 182",
    "description": "This is a detailed description for sample record 182. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.94,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 182.",
    },
}


SAMPLE_RECORD_0183 = {
    "id": "sample-0183",
    "title": "Sample Record Title Number 183",
    "description": "This is a detailed description for sample record 183. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.11,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 183.",
    },
}


SAMPLE_RECORD_0184 = {
    "id": "sample-0184",
    "title": "Sample Record Title Number 184",
    "description": "This is a detailed description for sample record 184. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.28,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 184.",
    },
}


SAMPLE_RECORD_0185 = {
    "id": "sample-0185",
    "title": "Sample Record Title Number 185",
    "description": "This is a detailed description for sample record 185. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.45,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 185.",
    },
}


SAMPLE_RECORD_0186 = {
    "id": "sample-0186",
    "title": "Sample Record Title Number 186",
    "description": "This is a detailed description for sample record 186. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.62,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 186.",
    },
}


SAMPLE_RECORD_0187 = {
    "id": "sample-0187",
    "title": "Sample Record Title Number 187",
    "description": "This is a detailed description for sample record 187. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.79,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 187.",
    },
}


SAMPLE_RECORD_0188 = {
    "id": "sample-0188",
    "title": "Sample Record Title Number 188",
    "description": "This is a detailed description for sample record 188. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.96,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 188.",
    },
}


SAMPLE_RECORD_0189 = {
    "id": "sample-0189",
    "title": "Sample Record Title Number 189",
    "description": "This is a detailed description for sample record 189. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.13,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 189.",
    },
}


SAMPLE_RECORD_0190 = {
    "id": "sample-0190",
    "title": "Sample Record Title Number 190",
    "description": "This is a detailed description for sample record 190. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.3,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 190.",
    },
}


SAMPLE_RECORD_0191 = {
    "id": "sample-0191",
    "title": "Sample Record Title Number 191",
    "description": "This is a detailed description for sample record 191. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.47,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 191.",
    },
}


SAMPLE_RECORD_0192 = {
    "id": "sample-0192",
    "title": "Sample Record Title Number 192",
    "description": "This is a detailed description for sample record 192. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.64,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 192.",
    },
}


SAMPLE_RECORD_0193 = {
    "id": "sample-0193",
    "title": "Sample Record Title Number 193",
    "description": "This is a detailed description for sample record 193. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.81,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 193.",
    },
}


SAMPLE_RECORD_0194 = {
    "id": "sample-0194",
    "title": "Sample Record Title Number 194",
    "description": "This is a detailed description for sample record 194. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.98,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 194.",
    },
}


SAMPLE_RECORD_0195 = {
    "id": "sample-0195",
    "title": "Sample Record Title Number 195",
    "description": "This is a detailed description for sample record 195. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.15,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 195.",
    },
}


SAMPLE_RECORD_0196 = {
    "id": "sample-0196",
    "title": "Sample Record Title Number 196",
    "description": "This is a detailed description for sample record 196. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.32,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 196.",
    },
}


SAMPLE_RECORD_0197 = {
    "id": "sample-0197",
    "title": "Sample Record Title Number 197",
    "description": "This is a detailed description for sample record 197. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.49,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 197.",
    },
}


SAMPLE_RECORD_0198 = {
    "id": "sample-0198",
    "title": "Sample Record Title Number 198",
    "description": "This is a detailed description for sample record 198. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.66,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 198.",
    },
}


SAMPLE_RECORD_0199 = {
    "id": "sample-0199",
    "title": "Sample Record Title Number 199",
    "description": "This is a detailed description for sample record 199. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.83,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 199.",
    },
}


SAMPLE_RECORD_0200 = {
    "id": "sample-0200",
    "title": "Sample Record Title Number 200",
    "description": "This is a detailed description for sample record 200. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.0,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 200.",
    },
}


SAMPLE_RECORD_0201 = {
    "id": "sample-0201",
    "title": "Sample Record Title Number 201",
    "description": "This is a detailed description for sample record 201. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.17,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 201.",
    },
}


SAMPLE_RECORD_0202 = {
    "id": "sample-0202",
    "title": "Sample Record Title Number 202",
    "description": "This is a detailed description for sample record 202. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.34,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 202.",
    },
}


SAMPLE_RECORD_0203 = {
    "id": "sample-0203",
    "title": "Sample Record Title Number 203",
    "description": "This is a detailed description for sample record 203. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.51,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 203.",
    },
}


SAMPLE_RECORD_0204 = {
    "id": "sample-0204",
    "title": "Sample Record Title Number 204",
    "description": "This is a detailed description for sample record 204. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.68,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 204.",
    },
}


SAMPLE_RECORD_0205 = {
    "id": "sample-0205",
    "title": "Sample Record Title Number 205",
    "description": "This is a detailed description for sample record 205. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.85,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 205.",
    },
}


SAMPLE_RECORD_0206 = {
    "id": "sample-0206",
    "title": "Sample Record Title Number 206",
    "description": "This is a detailed description for sample record 206. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.02,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 206.",
    },
}


SAMPLE_RECORD_0207 = {
    "id": "sample-0207",
    "title": "Sample Record Title Number 207",
    "description": "This is a detailed description for sample record 207. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.19,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 207.",
    },
}


SAMPLE_RECORD_0208 = {
    "id": "sample-0208",
    "title": "Sample Record Title Number 208",
    "description": "This is a detailed description for sample record 208. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.36,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 208.",
    },
}


SAMPLE_RECORD_0209 = {
    "id": "sample-0209",
    "title": "Sample Record Title Number 209",
    "description": "This is a detailed description for sample record 209. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.53,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 209.",
    },
}


SAMPLE_RECORD_0210 = {
    "id": "sample-0210",
    "title": "Sample Record Title Number 210",
    "description": "This is a detailed description for sample record 210. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.7,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 210.",
    },
}


SAMPLE_RECORD_0211 = {
    "id": "sample-0211",
    "title": "Sample Record Title Number 211",
    "description": "This is a detailed description for sample record 211. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.87,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 211.",
    },
}


SAMPLE_RECORD_0212 = {
    "id": "sample-0212",
    "title": "Sample Record Title Number 212",
    "description": "This is a detailed description for sample record 212. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.04,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 212.",
    },
}


SAMPLE_RECORD_0213 = {
    "id": "sample-0213",
    "title": "Sample Record Title Number 213",
    "description": "This is a detailed description for sample record 213. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.21,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 213.",
    },
}


SAMPLE_RECORD_0214 = {
    "id": "sample-0214",
    "title": "Sample Record Title Number 214",
    "description": "This is a detailed description for sample record 214. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.38,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 214.",
    },
}


SAMPLE_RECORD_0215 = {
    "id": "sample-0215",
    "title": "Sample Record Title Number 215",
    "description": "This is a detailed description for sample record 215. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.55,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 215.",
    },
}


SAMPLE_RECORD_0216 = {
    "id": "sample-0216",
    "title": "Sample Record Title Number 216",
    "description": "This is a detailed description for sample record 216. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.72,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 216.",
    },
}


SAMPLE_RECORD_0217 = {
    "id": "sample-0217",
    "title": "Sample Record Title Number 217",
    "description": "This is a detailed description for sample record 217. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.89,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 217.",
    },
}


SAMPLE_RECORD_0218 = {
    "id": "sample-0218",
    "title": "Sample Record Title Number 218",
    "description": "This is a detailed description for sample record 218. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.06,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 218.",
    },
}


SAMPLE_RECORD_0219 = {
    "id": "sample-0219",
    "title": "Sample Record Title Number 219",
    "description": "This is a detailed description for sample record 219. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.23,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 219.",
    },
}


SAMPLE_RECORD_0220 = {
    "id": "sample-0220",
    "title": "Sample Record Title Number 220",
    "description": "This is a detailed description for sample record 220. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.4,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 220.",
    },
}


SAMPLE_RECORD_0221 = {
    "id": "sample-0221",
    "title": "Sample Record Title Number 221",
    "description": "This is a detailed description for sample record 221. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.57,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 221.",
    },
}


SAMPLE_RECORD_0222 = {
    "id": "sample-0222",
    "title": "Sample Record Title Number 222",
    "description": "This is a detailed description for sample record 222. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.74,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 222.",
    },
}


SAMPLE_RECORD_0223 = {
    "id": "sample-0223",
    "title": "Sample Record Title Number 223",
    "description": "This is a detailed description for sample record 223. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.91,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 223.",
    },
}


SAMPLE_RECORD_0224 = {
    "id": "sample-0224",
    "title": "Sample Record Title Number 224",
    "description": "This is a detailed description for sample record 224. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.08,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 224.",
    },
}


SAMPLE_RECORD_0225 = {
    "id": "sample-0225",
    "title": "Sample Record Title Number 225",
    "description": "This is a detailed description for sample record 225. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.25,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 225.",
    },
}


SAMPLE_RECORD_0226 = {
    "id": "sample-0226",
    "title": "Sample Record Title Number 226",
    "description": "This is a detailed description for sample record 226. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.42,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 226.",
    },
}


SAMPLE_RECORD_0227 = {
    "id": "sample-0227",
    "title": "Sample Record Title Number 227",
    "description": "This is a detailed description for sample record 227. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.59,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 227.",
    },
}


SAMPLE_RECORD_0228 = {
    "id": "sample-0228",
    "title": "Sample Record Title Number 228",
    "description": "This is a detailed description for sample record 228. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.76,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 228.",
    },
}


SAMPLE_RECORD_0229 = {
    "id": "sample-0229",
    "title": "Sample Record Title Number 229",
    "description": "This is a detailed description for sample record 229. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.93,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 229.",
    },
}


SAMPLE_RECORD_0230 = {
    "id": "sample-0230",
    "title": "Sample Record Title Number 230",
    "description": "This is a detailed description for sample record 230. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.1,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 230.",
    },
}


SAMPLE_RECORD_0231 = {
    "id": "sample-0231",
    "title": "Sample Record Title Number 231",
    "description": "This is a detailed description for sample record 231. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.27,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 231.",
    },
}


SAMPLE_RECORD_0232 = {
    "id": "sample-0232",
    "title": "Sample Record Title Number 232",
    "description": "This is a detailed description for sample record 232. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.44,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 232.",
    },
}


SAMPLE_RECORD_0233 = {
    "id": "sample-0233",
    "title": "Sample Record Title Number 233",
    "description": "This is a detailed description for sample record 233. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.61,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 233.",
    },
}


SAMPLE_RECORD_0234 = {
    "id": "sample-0234",
    "title": "Sample Record Title Number 234",
    "description": "This is a detailed description for sample record 234. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.78,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 234.",
    },
}


SAMPLE_RECORD_0235 = {
    "id": "sample-0235",
    "title": "Sample Record Title Number 235",
    "description": "This is a detailed description for sample record 235. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.95,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 235.",
    },
}


SAMPLE_RECORD_0236 = {
    "id": "sample-0236",
    "title": "Sample Record Title Number 236",
    "description": "This is a detailed description for sample record 236. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.12,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 236.",
    },
}


SAMPLE_RECORD_0237 = {
    "id": "sample-0237",
    "title": "Sample Record Title Number 237",
    "description": "This is a detailed description for sample record 237. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.29,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 237.",
    },
}


SAMPLE_RECORD_0238 = {
    "id": "sample-0238",
    "title": "Sample Record Title Number 238",
    "description": "This is a detailed description for sample record 238. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.46,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 238.",
    },
}


SAMPLE_RECORD_0239 = {
    "id": "sample-0239",
    "title": "Sample Record Title Number 239",
    "description": "This is a detailed description for sample record 239. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.63,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 239.",
    },
}


SAMPLE_RECORD_0240 = {
    "id": "sample-0240",
    "title": "Sample Record Title Number 240",
    "description": "This is a detailed description for sample record 240. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.8,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 240.",
    },
}


SAMPLE_RECORD_0241 = {
    "id": "sample-0241",
    "title": "Sample Record Title Number 241",
    "description": "This is a detailed description for sample record 241. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.97,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 241.",
    },
}


SAMPLE_RECORD_0242 = {
    "id": "sample-0242",
    "title": "Sample Record Title Number 242",
    "description": "This is a detailed description for sample record 242. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.14,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 242.",
    },
}


SAMPLE_RECORD_0243 = {
    "id": "sample-0243",
    "title": "Sample Record Title Number 243",
    "description": "This is a detailed description for sample record 243. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.31,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 243.",
    },
}


SAMPLE_RECORD_0244 = {
    "id": "sample-0244",
    "title": "Sample Record Title Number 244",
    "description": "This is a detailed description for sample record 244. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.48,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 244.",
    },
}


SAMPLE_RECORD_0245 = {
    "id": "sample-0245",
    "title": "Sample Record Title Number 245",
    "description": "This is a detailed description for sample record 245. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.65,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 245.",
    },
}


SAMPLE_RECORD_0246 = {
    "id": "sample-0246",
    "title": "Sample Record Title Number 246",
    "description": "This is a detailed description for sample record 246. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.82,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 246.",
    },
}


SAMPLE_RECORD_0247 = {
    "id": "sample-0247",
    "title": "Sample Record Title Number 247",
    "description": "This is a detailed description for sample record 247. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.99,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 247.",
    },
}


SAMPLE_RECORD_0248 = {
    "id": "sample-0248",
    "title": "Sample Record Title Number 248",
    "description": "This is a detailed description for sample record 248. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.16,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 248.",
    },
}


SAMPLE_RECORD_0249 = {
    "id": "sample-0249",
    "title": "Sample Record Title Number 249",
    "description": "This is a detailed description for sample record 249. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.33,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 249.",
    },
}


SAMPLE_RECORD_0250 = {
    "id": "sample-0250",
    "title": "Sample Record Title Number 250",
    "description": "This is a detailed description for sample record 250. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.5,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 250.",
    },
}


SAMPLE_RECORD_0251 = {
    "id": "sample-0251",
    "title": "Sample Record Title Number 251",
    "description": "This is a detailed description for sample record 251. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.67,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 251.",
    },
}


SAMPLE_RECORD_0252 = {
    "id": "sample-0252",
    "title": "Sample Record Title Number 252",
    "description": "This is a detailed description for sample record 252. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.84,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 252.",
    },
}


SAMPLE_RECORD_0253 = {
    "id": "sample-0253",
    "title": "Sample Record Title Number 253",
    "description": "This is a detailed description for sample record 253. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.01,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 253.",
    },
}


SAMPLE_RECORD_0254 = {
    "id": "sample-0254",
    "title": "Sample Record Title Number 254",
    "description": "This is a detailed description for sample record 254. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.18,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 254.",
    },
}


SAMPLE_RECORD_0255 = {
    "id": "sample-0255",
    "title": "Sample Record Title Number 255",
    "description": "This is a detailed description for sample record 255. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.35,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 255.",
    },
}


SAMPLE_RECORD_0256 = {
    "id": "sample-0256",
    "title": "Sample Record Title Number 256",
    "description": "This is a detailed description for sample record 256. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.52,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 256.",
    },
}


SAMPLE_RECORD_0257 = {
    "id": "sample-0257",
    "title": "Sample Record Title Number 257",
    "description": "This is a detailed description for sample record 257. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.69,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 257.",
    },
}


SAMPLE_RECORD_0258 = {
    "id": "sample-0258",
    "title": "Sample Record Title Number 258",
    "description": "This is a detailed description for sample record 258. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.86,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 258.",
    },
}


SAMPLE_RECORD_0259 = {
    "id": "sample-0259",
    "title": "Sample Record Title Number 259",
    "description": "This is a detailed description for sample record 259. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.03,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 259.",
    },
}


SAMPLE_RECORD_0260 = {
    "id": "sample-0260",
    "title": "Sample Record Title Number 260",
    "description": "This is a detailed description for sample record 260. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.2,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 260.",
    },
}


SAMPLE_RECORD_0261 = {
    "id": "sample-0261",
    "title": "Sample Record Title Number 261",
    "description": "This is a detailed description for sample record 261. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.37,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 261.",
    },
}


SAMPLE_RECORD_0262 = {
    "id": "sample-0262",
    "title": "Sample Record Title Number 262",
    "description": "This is a detailed description for sample record 262. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.54,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 262.",
    },
}


SAMPLE_RECORD_0263 = {
    "id": "sample-0263",
    "title": "Sample Record Title Number 263",
    "description": "This is a detailed description for sample record 263. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.71,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 263.",
    },
}


SAMPLE_RECORD_0264 = {
    "id": "sample-0264",
    "title": "Sample Record Title Number 264",
    "description": "This is a detailed description for sample record 264. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.88,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 264.",
    },
}


SAMPLE_RECORD_0265 = {
    "id": "sample-0265",
    "title": "Sample Record Title Number 265",
    "description": "This is a detailed description for sample record 265. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.05,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 265.",
    },
}


SAMPLE_RECORD_0266 = {
    "id": "sample-0266",
    "title": "Sample Record Title Number 266",
    "description": "This is a detailed description for sample record 266. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.22,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 266.",
    },
}


SAMPLE_RECORD_0267 = {
    "id": "sample-0267",
    "title": "Sample Record Title Number 267",
    "description": "This is a detailed description for sample record 267. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.39,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 267.",
    },
}


SAMPLE_RECORD_0268 = {
    "id": "sample-0268",
    "title": "Sample Record Title Number 268",
    "description": "This is a detailed description for sample record 268. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.56,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 268.",
    },
}


SAMPLE_RECORD_0269 = {
    "id": "sample-0269",
    "title": "Sample Record Title Number 269",
    "description": "This is a detailed description for sample record 269. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.73,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 269.",
    },
}


SAMPLE_RECORD_0270 = {
    "id": "sample-0270",
    "title": "Sample Record Title Number 270",
    "description": "This is a detailed description for sample record 270. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.9,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 270.",
    },
}


SAMPLE_RECORD_0271 = {
    "id": "sample-0271",
    "title": "Sample Record Title Number 271",
    "description": "This is a detailed description for sample record 271. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.07,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 271.",
    },
}


SAMPLE_RECORD_0272 = {
    "id": "sample-0272",
    "title": "Sample Record Title Number 272",
    "description": "This is a detailed description for sample record 272. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.24,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 272.",
    },
}


SAMPLE_RECORD_0273 = {
    "id": "sample-0273",
    "title": "Sample Record Title Number 273",
    "description": "This is a detailed description for sample record 273. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.41,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 273.",
    },
}


SAMPLE_RECORD_0274 = {
    "id": "sample-0274",
    "title": "Sample Record Title Number 274",
    "description": "This is a detailed description for sample record 274. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.58,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 274.",
    },
}


SAMPLE_RECORD_0275 = {
    "id": "sample-0275",
    "title": "Sample Record Title Number 275",
    "description": "This is a detailed description for sample record 275. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.75,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 275.",
    },
}


SAMPLE_RECORD_0276 = {
    "id": "sample-0276",
    "title": "Sample Record Title Number 276",
    "description": "This is a detailed description for sample record 276. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.92,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 276.",
    },
}


SAMPLE_RECORD_0277 = {
    "id": "sample-0277",
    "title": "Sample Record Title Number 277",
    "description": "This is a detailed description for sample record 277. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.09,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 277.",
    },
}


SAMPLE_RECORD_0278 = {
    "id": "sample-0278",
    "title": "Sample Record Title Number 278",
    "description": "This is a detailed description for sample record 278. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.26,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 278.",
    },
}


SAMPLE_RECORD_0279 = {
    "id": "sample-0279",
    "title": "Sample Record Title Number 279",
    "description": "This is a detailed description for sample record 279. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.43,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 279.",
    },
}


SAMPLE_RECORD_0280 = {
    "id": "sample-0280",
    "title": "Sample Record Title Number 280",
    "description": "This is a detailed description for sample record 280. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.6,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 280.",
    },
}


SAMPLE_RECORD_0281 = {
    "id": "sample-0281",
    "title": "Sample Record Title Number 281",
    "description": "This is a detailed description for sample record 281. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.77,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 281.",
    },
}


SAMPLE_RECORD_0282 = {
    "id": "sample-0282",
    "title": "Sample Record Title Number 282",
    "description": "This is a detailed description for sample record 282. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.94,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 282.",
    },
}


SAMPLE_RECORD_0283 = {
    "id": "sample-0283",
    "title": "Sample Record Title Number 283",
    "description": "This is a detailed description for sample record 283. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.11,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 283.",
    },
}


SAMPLE_RECORD_0284 = {
    "id": "sample-0284",
    "title": "Sample Record Title Number 284",
    "description": "This is a detailed description for sample record 284. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.28,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 284.",
    },
}


SAMPLE_RECORD_0285 = {
    "id": "sample-0285",
    "title": "Sample Record Title Number 285",
    "description": "This is a detailed description for sample record 285. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.45,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 285.",
    },
}


SAMPLE_RECORD_0286 = {
    "id": "sample-0286",
    "title": "Sample Record Title Number 286",
    "description": "This is a detailed description for sample record 286. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.62,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 286.",
    },
}


SAMPLE_RECORD_0287 = {
    "id": "sample-0287",
    "title": "Sample Record Title Number 287",
    "description": "This is a detailed description for sample record 287. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.79,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 287.",
    },
}


SAMPLE_RECORD_0288 = {
    "id": "sample-0288",
    "title": "Sample Record Title Number 288",
    "description": "This is a detailed description for sample record 288. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.96,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 288.",
    },
}


SAMPLE_RECORD_0289 = {
    "id": "sample-0289",
    "title": "Sample Record Title Number 289",
    "description": "This is a detailed description for sample record 289. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.13,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 289.",
    },
}


SAMPLE_RECORD_0290 = {
    "id": "sample-0290",
    "title": "Sample Record Title Number 290",
    "description": "This is a detailed description for sample record 290. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.3,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 290.",
    },
}


SAMPLE_RECORD_0291 = {
    "id": "sample-0291",
    "title": "Sample Record Title Number 291",
    "description": "This is a detailed description for sample record 291. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.47,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 291.",
    },
}


SAMPLE_RECORD_0292 = {
    "id": "sample-0292",
    "title": "Sample Record Title Number 292",
    "description": "This is a detailed description for sample record 292. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.64,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 292.",
    },
}


SAMPLE_RECORD_0293 = {
    "id": "sample-0293",
    "title": "Sample Record Title Number 293",
    "description": "This is a detailed description for sample record 293. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.81,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 293.",
    },
}


SAMPLE_RECORD_0294 = {
    "id": "sample-0294",
    "title": "Sample Record Title Number 294",
    "description": "This is a detailed description for sample record 294. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.98,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 294.",
    },
}


SAMPLE_RECORD_0295 = {
    "id": "sample-0295",
    "title": "Sample Record Title Number 295",
    "description": "This is a detailed description for sample record 295. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.15,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 295.",
    },
}


SAMPLE_RECORD_0296 = {
    "id": "sample-0296",
    "title": "Sample Record Title Number 296",
    "description": "This is a detailed description for sample record 296. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.32,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 296.",
    },
}


SAMPLE_RECORD_0297 = {
    "id": "sample-0297",
    "title": "Sample Record Title Number 297",
    "description": "This is a detailed description for sample record 297. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.49,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 297.",
    },
}


SAMPLE_RECORD_0298 = {
    "id": "sample-0298",
    "title": "Sample Record Title Number 298",
    "description": "This is a detailed description for sample record 298. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.66,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 298.",
    },
}


SAMPLE_RECORD_0299 = {
    "id": "sample-0299",
    "title": "Sample Record Title Number 299",
    "description": "This is a detailed description for sample record 299. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.83,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 299.",
    },
}


SAMPLE_RECORD_0300 = {
    "id": "sample-0300",
    "title": "Sample Record Title Number 300",
    "description": "This is a detailed description for sample record 300. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.0,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 300.",
    },
}


SAMPLE_RECORD_0301 = {
    "id": "sample-0301",
    "title": "Sample Record Title Number 301",
    "description": "This is a detailed description for sample record 301. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.17,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 301.",
    },
}


SAMPLE_RECORD_0302 = {
    "id": "sample-0302",
    "title": "Sample Record Title Number 302",
    "description": "This is a detailed description for sample record 302. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.34,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 302.",
    },
}


SAMPLE_RECORD_0303 = {
    "id": "sample-0303",
    "title": "Sample Record Title Number 303",
    "description": "This is a detailed description for sample record 303. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.51,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 303.",
    },
}


SAMPLE_RECORD_0304 = {
    "id": "sample-0304",
    "title": "Sample Record Title Number 304",
    "description": "This is a detailed description for sample record 304. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.68,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 304.",
    },
}


SAMPLE_RECORD_0305 = {
    "id": "sample-0305",
    "title": "Sample Record Title Number 305",
    "description": "This is a detailed description for sample record 305. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.85,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 305.",
    },
}


SAMPLE_RECORD_0306 = {
    "id": "sample-0306",
    "title": "Sample Record Title Number 306",
    "description": "This is a detailed description for sample record 306. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.02,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 306.",
    },
}


SAMPLE_RECORD_0307 = {
    "id": "sample-0307",
    "title": "Sample Record Title Number 307",
    "description": "This is a detailed description for sample record 307. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.19,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 307.",
    },
}


SAMPLE_RECORD_0308 = {
    "id": "sample-0308",
    "title": "Sample Record Title Number 308",
    "description": "This is a detailed description for sample record 308. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.36,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 308.",
    },
}


SAMPLE_RECORD_0309 = {
    "id": "sample-0309",
    "title": "Sample Record Title Number 309",
    "description": "This is a detailed description for sample record 309. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.53,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 309.",
    },
}


SAMPLE_RECORD_0310 = {
    "id": "sample-0310",
    "title": "Sample Record Title Number 310",
    "description": "This is a detailed description for sample record 310. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.7,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 310.",
    },
}


SAMPLE_RECORD_0311 = {
    "id": "sample-0311",
    "title": "Sample Record Title Number 311",
    "description": "This is a detailed description for sample record 311. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.87,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 311.",
    },
}


SAMPLE_RECORD_0312 = {
    "id": "sample-0312",
    "title": "Sample Record Title Number 312",
    "description": "This is a detailed description for sample record 312. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.04,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 312.",
    },
}


SAMPLE_RECORD_0313 = {
    "id": "sample-0313",
    "title": "Sample Record Title Number 313",
    "description": "This is a detailed description for sample record 313. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.21,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 313.",
    },
}


SAMPLE_RECORD_0314 = {
    "id": "sample-0314",
    "title": "Sample Record Title Number 314",
    "description": "This is a detailed description for sample record 314. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.38,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 314.",
    },
}


SAMPLE_RECORD_0315 = {
    "id": "sample-0315",
    "title": "Sample Record Title Number 315",
    "description": "This is a detailed description for sample record 315. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.55,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 315.",
    },
}


SAMPLE_RECORD_0316 = {
    "id": "sample-0316",
    "title": "Sample Record Title Number 316",
    "description": "This is a detailed description for sample record 316. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.72,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 316.",
    },
}


SAMPLE_RECORD_0317 = {
    "id": "sample-0317",
    "title": "Sample Record Title Number 317",
    "description": "This is a detailed description for sample record 317. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.89,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 317.",
    },
}


SAMPLE_RECORD_0318 = {
    "id": "sample-0318",
    "title": "Sample Record Title Number 318",
    "description": "This is a detailed description for sample record 318. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.06,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 318.",
    },
}


SAMPLE_RECORD_0319 = {
    "id": "sample-0319",
    "title": "Sample Record Title Number 319",
    "description": "This is a detailed description for sample record 319. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.23,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 319.",
    },
}


SAMPLE_RECORD_0320 = {
    "id": "sample-0320",
    "title": "Sample Record Title Number 320",
    "description": "This is a detailed description for sample record 320. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.4,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 320.",
    },
}


SAMPLE_RECORD_0321 = {
    "id": "sample-0321",
    "title": "Sample Record Title Number 321",
    "description": "This is a detailed description for sample record 321. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.57,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 321.",
    },
}


SAMPLE_RECORD_0322 = {
    "id": "sample-0322",
    "title": "Sample Record Title Number 322",
    "description": "This is a detailed description for sample record 322. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.74,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 322.",
    },
}


SAMPLE_RECORD_0323 = {
    "id": "sample-0323",
    "title": "Sample Record Title Number 323",
    "description": "This is a detailed description for sample record 323. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.91,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 323.",
    },
}


SAMPLE_RECORD_0324 = {
    "id": "sample-0324",
    "title": "Sample Record Title Number 324",
    "description": "This is a detailed description for sample record 324. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.08,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 324.",
    },
}


SAMPLE_RECORD_0325 = {
    "id": "sample-0325",
    "title": "Sample Record Title Number 325",
    "description": "This is a detailed description for sample record 325. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.25,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 325.",
    },
}


SAMPLE_RECORD_0326 = {
    "id": "sample-0326",
    "title": "Sample Record Title Number 326",
    "description": "This is a detailed description for sample record 326. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.42,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 326.",
    },
}


SAMPLE_RECORD_0327 = {
    "id": "sample-0327",
    "title": "Sample Record Title Number 327",
    "description": "This is a detailed description for sample record 327. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.59,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 327.",
    },
}


SAMPLE_RECORD_0328 = {
    "id": "sample-0328",
    "title": "Sample Record Title Number 328",
    "description": "This is a detailed description for sample record 328. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.76,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 328.",
    },
}


SAMPLE_RECORD_0329 = {
    "id": "sample-0329",
    "title": "Sample Record Title Number 329",
    "description": "This is a detailed description for sample record 329. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.93,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 329.",
    },
}


SAMPLE_RECORD_0330 = {
    "id": "sample-0330",
    "title": "Sample Record Title Number 330",
    "description": "This is a detailed description for sample record 330. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.1,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 330.",
    },
}


SAMPLE_RECORD_0331 = {
    "id": "sample-0331",
    "title": "Sample Record Title Number 331",
    "description": "This is a detailed description for sample record 331. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.27,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 331.",
    },
}


SAMPLE_RECORD_0332 = {
    "id": "sample-0332",
    "title": "Sample Record Title Number 332",
    "description": "This is a detailed description for sample record 332. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.44,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 332.",
    },
}


SAMPLE_RECORD_0333 = {
    "id": "sample-0333",
    "title": "Sample Record Title Number 333",
    "description": "This is a detailed description for sample record 333. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.61,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 333.",
    },
}


SAMPLE_RECORD_0334 = {
    "id": "sample-0334",
    "title": "Sample Record Title Number 334",
    "description": "This is a detailed description for sample record 334. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.78,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 334.",
    },
}


SAMPLE_RECORD_0335 = {
    "id": "sample-0335",
    "title": "Sample Record Title Number 335",
    "description": "This is a detailed description for sample record 335. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.95,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 335.",
    },
}


SAMPLE_RECORD_0336 = {
    "id": "sample-0336",
    "title": "Sample Record Title Number 336",
    "description": "This is a detailed description for sample record 336. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.12,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 336.",
    },
}


SAMPLE_RECORD_0337 = {
    "id": "sample-0337",
    "title": "Sample Record Title Number 337",
    "description": "This is a detailed description for sample record 337. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.29,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 337.",
    },
}


SAMPLE_RECORD_0338 = {
    "id": "sample-0338",
    "title": "Sample Record Title Number 338",
    "description": "This is a detailed description for sample record 338. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.46,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 338.",
    },
}


SAMPLE_RECORD_0339 = {
    "id": "sample-0339",
    "title": "Sample Record Title Number 339",
    "description": "This is a detailed description for sample record 339. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.63,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 339.",
    },
}


SAMPLE_RECORD_0340 = {
    "id": "sample-0340",
    "title": "Sample Record Title Number 340",
    "description": "This is a detailed description for sample record 340. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.8,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 340.",
    },
}


SAMPLE_RECORD_0341 = {
    "id": "sample-0341",
    "title": "Sample Record Title Number 341",
    "description": "This is a detailed description for sample record 341. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.97,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 341.",
    },
}


SAMPLE_RECORD_0342 = {
    "id": "sample-0342",
    "title": "Sample Record Title Number 342",
    "description": "This is a detailed description for sample record 342. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.14,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 342.",
    },
}


SAMPLE_RECORD_0343 = {
    "id": "sample-0343",
    "title": "Sample Record Title Number 343",
    "description": "This is a detailed description for sample record 343. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.31,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 343.",
    },
}


SAMPLE_RECORD_0344 = {
    "id": "sample-0344",
    "title": "Sample Record Title Number 344",
    "description": "This is a detailed description for sample record 344. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.48,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 344.",
    },
}


SAMPLE_RECORD_0345 = {
    "id": "sample-0345",
    "title": "Sample Record Title Number 345",
    "description": "This is a detailed description for sample record 345. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.65,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 345.",
    },
}


SAMPLE_RECORD_0346 = {
    "id": "sample-0346",
    "title": "Sample Record Title Number 346",
    "description": "This is a detailed description for sample record 346. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.82,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 346.",
    },
}


SAMPLE_RECORD_0347 = {
    "id": "sample-0347",
    "title": "Sample Record Title Number 347",
    "description": "This is a detailed description for sample record 347. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.99,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 347.",
    },
}


SAMPLE_RECORD_0348 = {
    "id": "sample-0348",
    "title": "Sample Record Title Number 348",
    "description": "This is a detailed description for sample record 348. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.16,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 348.",
    },
}


SAMPLE_RECORD_0349 = {
    "id": "sample-0349",
    "title": "Sample Record Title Number 349",
    "description": "This is a detailed description for sample record 349. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.33,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 349.",
    },
}


SAMPLE_RECORD_0350 = {
    "id": "sample-0350",
    "title": "Sample Record Title Number 350",
    "description": "This is a detailed description for sample record 350. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.5,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 350.",
    },
}


SAMPLE_RECORD_0351 = {
    "id": "sample-0351",
    "title": "Sample Record Title Number 351",
    "description": "This is a detailed description for sample record 351. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.67,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 351.",
    },
}


SAMPLE_RECORD_0352 = {
    "id": "sample-0352",
    "title": "Sample Record Title Number 352",
    "description": "This is a detailed description for sample record 352. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.84,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 352.",
    },
}


SAMPLE_RECORD_0353 = {
    "id": "sample-0353",
    "title": "Sample Record Title Number 353",
    "description": "This is a detailed description for sample record 353. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.01,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 353.",
    },
}


SAMPLE_RECORD_0354 = {
    "id": "sample-0354",
    "title": "Sample Record Title Number 354",
    "description": "This is a detailed description for sample record 354. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.18,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 354.",
    },
}


SAMPLE_RECORD_0355 = {
    "id": "sample-0355",
    "title": "Sample Record Title Number 355",
    "description": "This is a detailed description for sample record 355. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.35,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 355.",
    },
}


SAMPLE_RECORD_0356 = {
    "id": "sample-0356",
    "title": "Sample Record Title Number 356",
    "description": "This is a detailed description for sample record 356. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.52,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 356.",
    },
}


SAMPLE_RECORD_0357 = {
    "id": "sample-0357",
    "title": "Sample Record Title Number 357",
    "description": "This is a detailed description for sample record 357. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.69,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 357.",
    },
}


SAMPLE_RECORD_0358 = {
    "id": "sample-0358",
    "title": "Sample Record Title Number 358",
    "description": "This is a detailed description for sample record 358. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.86,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 358.",
    },
}


SAMPLE_RECORD_0359 = {
    "id": "sample-0359",
    "title": "Sample Record Title Number 359",
    "description": "This is a detailed description for sample record 359. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.03,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 359.",
    },
}


SAMPLE_RECORD_0360 = {
    "id": "sample-0360",
    "title": "Sample Record Title Number 360",
    "description": "This is a detailed description for sample record 360. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.2,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 360.",
    },
}


SAMPLE_RECORD_0361 = {
    "id": "sample-0361",
    "title": "Sample Record Title Number 361",
    "description": "This is a detailed description for sample record 361. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.37,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 361.",
    },
}


SAMPLE_RECORD_0362 = {
    "id": "sample-0362",
    "title": "Sample Record Title Number 362",
    "description": "This is a detailed description for sample record 362. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.54,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 362.",
    },
}


SAMPLE_RECORD_0363 = {
    "id": "sample-0363",
    "title": "Sample Record Title Number 363",
    "description": "This is a detailed description for sample record 363. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.71,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 363.",
    },
}


SAMPLE_RECORD_0364 = {
    "id": "sample-0364",
    "title": "Sample Record Title Number 364",
    "description": "This is a detailed description for sample record 364. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.88,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 364.",
    },
}


SAMPLE_RECORD_0365 = {
    "id": "sample-0365",
    "title": "Sample Record Title Number 365",
    "description": "This is a detailed description for sample record 365. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.05,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 365.",
    },
}


SAMPLE_RECORD_0366 = {
    "id": "sample-0366",
    "title": "Sample Record Title Number 366",
    "description": "This is a detailed description for sample record 366. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.22,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 366.",
    },
}


SAMPLE_RECORD_0367 = {
    "id": "sample-0367",
    "title": "Sample Record Title Number 367",
    "description": "This is a detailed description for sample record 367. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.39,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 367.",
    },
}


SAMPLE_RECORD_0368 = {
    "id": "sample-0368",
    "title": "Sample Record Title Number 368",
    "description": "This is a detailed description for sample record 368. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.56,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 368.",
    },
}


SAMPLE_RECORD_0369 = {
    "id": "sample-0369",
    "title": "Sample Record Title Number 369",
    "description": "This is a detailed description for sample record 369. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.73,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 369.",
    },
}


SAMPLE_RECORD_0370 = {
    "id": "sample-0370",
    "title": "Sample Record Title Number 370",
    "description": "This is a detailed description for sample record 370. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.9,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 370.",
    },
}


SAMPLE_RECORD_0371 = {
    "id": "sample-0371",
    "title": "Sample Record Title Number 371",
    "description": "This is a detailed description for sample record 371. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.07,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 371.",
    },
}


SAMPLE_RECORD_0372 = {
    "id": "sample-0372",
    "title": "Sample Record Title Number 372",
    "description": "This is a detailed description for sample record 372. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.24,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 372.",
    },
}


SAMPLE_RECORD_0373 = {
    "id": "sample-0373",
    "title": "Sample Record Title Number 373",
    "description": "This is a detailed description for sample record 373. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.41,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 373.",
    },
}


SAMPLE_RECORD_0374 = {
    "id": "sample-0374",
    "title": "Sample Record Title Number 374",
    "description": "This is a detailed description for sample record 374. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.58,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 374.",
    },
}


SAMPLE_RECORD_0375 = {
    "id": "sample-0375",
    "title": "Sample Record Title Number 375",
    "description": "This is a detailed description for sample record 375. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.75,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 375.",
    },
}


SAMPLE_RECORD_0376 = {
    "id": "sample-0376",
    "title": "Sample Record Title Number 376",
    "description": "This is a detailed description for sample record 376. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.92,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 376.",
    },
}


SAMPLE_RECORD_0377 = {
    "id": "sample-0377",
    "title": "Sample Record Title Number 377",
    "description": "This is a detailed description for sample record 377. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.09,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 377.",
    },
}


SAMPLE_RECORD_0378 = {
    "id": "sample-0378",
    "title": "Sample Record Title Number 378",
    "description": "This is a detailed description for sample record 378. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.26,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 378.",
    },
}


SAMPLE_RECORD_0379 = {
    "id": "sample-0379",
    "title": "Sample Record Title Number 379",
    "description": "This is a detailed description for sample record 379. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.43,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 379.",
    },
}


SAMPLE_RECORD_0380 = {
    "id": "sample-0380",
    "title": "Sample Record Title Number 380",
    "description": "This is a detailed description for sample record 380. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-0"],
    "score": 0.6,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 380.",
    },
}


SAMPLE_RECORD_0381 = {
    "id": "sample-0381",
    "title": "Sample Record Title Number 381",
    "description": "This is a detailed description for sample record 381. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-1"],
    "score": 0.77,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 381.",
    },
}


SAMPLE_RECORD_0382 = {
    "id": "sample-0382",
    "title": "Sample Record Title Number 382",
    "description": "This is a detailed description for sample record 382. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-2"],
    "score": 0.94,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 382.",
    },
}


SAMPLE_RECORD_0383 = {
    "id": "sample-0383",
    "title": "Sample Record Title Number 383",
    "description": "This is a detailed description for sample record 383. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-3"],
    "score": 0.11,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 383.",
    },
}


SAMPLE_RECORD_0384 = {
    "id": "sample-0384",
    "title": "Sample Record Title Number 384",
    "description": "This is a detailed description for sample record 384. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-4"],
    "score": 0.28,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 384.",
    },
}


SAMPLE_RECORD_0385 = {
    "id": "sample-0385",
    "title": "Sample Record Title Number 385",
    "description": "This is a detailed description for sample record 385. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-10",
    "tags": ["tag-a", "tag-b", "tag-5"],
    "score": 0.45,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 385.",
    },
}


SAMPLE_RECORD_0386 = {
    "id": "sample-0386",
    "title": "Sample Record Title Number 386",
    "description": "This is a detailed description for sample record 386. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-11",
    "tags": ["tag-a", "tag-b", "tag-6"],
    "score": 0.62,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 386.",
    },
}


SAMPLE_RECORD_0387 = {
    "id": "sample-0387",
    "title": "Sample Record Title Number 387",
    "description": "This is a detailed description for sample record 387. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-12",
    "tags": ["tag-a", "tag-b", "tag-7"],
    "score": 0.79,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 387.",
    },
}


SAMPLE_RECORD_0388 = {
    "id": "sample-0388",
    "title": "Sample Record Title Number 388",
    "description": "This is a detailed description for sample record 388. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-13",
    "tags": ["tag-a", "tag-b", "tag-8"],
    "score": 0.96,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 388.",
    },
}


SAMPLE_RECORD_0389 = {
    "id": "sample-0389",
    "title": "Sample Record Title Number 389",
    "description": "This is a detailed description for sample record 389. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-14",
    "tags": ["tag-a", "tag-b", "tag-9"],
    "score": 0.13,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 389.",
    },
}


SAMPLE_RECORD_0390 = {
    "id": "sample-0390",
    "title": "Sample Record Title Number 390",
    "description": "This is a detailed description for sample record 390. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-0",
    "tags": ["tag-a", "tag-b", "tag-10"],
    "score": 0.3,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 1,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 390.",
    },
}


SAMPLE_RECORD_0391 = {
    "id": "sample-0391",
    "title": "Sample Record Title Number 391",
    "description": "This is a detailed description for sample record 391. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-1",
    "tags": ["tag-a", "tag-b", "tag-11"],
    "score": 0.47,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 2,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 391.",
    },
}


SAMPLE_RECORD_0392 = {
    "id": "sample-0392",
    "title": "Sample Record Title Number 392",
    "description": "This is a detailed description for sample record 392. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-2",
    "tags": ["tag-a", "tag-b", "tag-12"],
    "score": 0.64,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 3,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 392.",
    },
}


SAMPLE_RECORD_0393 = {
    "id": "sample-0393",
    "title": "Sample Record Title Number 393",
    "description": "This is a detailed description for sample record 393. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-3",
    "tags": ["tag-a", "tag-b", "tag-13"],
    "score": 0.81,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 4,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 393.",
    },
}


SAMPLE_RECORD_0394 = {
    "id": "sample-0394",
    "title": "Sample Record Title Number 394",
    "description": "This is a detailed description for sample record 394. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-4",
    "tags": ["tag-a", "tag-b", "tag-14"],
    "score": 0.98,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 5,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 394.",
    },
}


SAMPLE_RECORD_0395 = {
    "id": "sample-0395",
    "title": "Sample Record Title Number 395",
    "description": "This is a detailed description for sample record 395. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-5",
    "tags": ["tag-a", "tag-b", "tag-15"],
    "score": 0.15,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 6,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 395.",
    },
}


SAMPLE_RECORD_0396 = {
    "id": "sample-0396",
    "title": "Sample Record Title Number 396",
    "description": "This is a detailed description for sample record 396. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-6",
    "tags": ["tag-a", "tag-b", "tag-16"],
    "score": 0.32,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 7,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 396.",
    },
}


SAMPLE_RECORD_0397 = {
    "id": "sample-0397",
    "title": "Sample Record Title Number 397",
    "description": "This is a detailed description for sample record 397. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-7",
    "tags": ["tag-a", "tag-b", "tag-17"],
    "score": 0.49,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 8,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 397.",
    },
}


SAMPLE_RECORD_0398 = {
    "id": "sample-0398",
    "title": "Sample Record Title Number 398",
    "description": "This is a detailed description for sample record 398. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-8",
    "tags": ["tag-a", "tag-b", "tag-18"],
    "score": 0.66,
    "active": true,
    "metadata": {
        "created_by": "system",
        "version": 9,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 398.",
    },
}


SAMPLE_RECORD_0399 = {
    "id": "sample-0399",
    "title": "Sample Record Title Number 399",
    "description": "This is a detailed description for sample record 399. It contains multiple sentences providing context, purpose, and usage guidelines for demonstration and testing of the platform data handling capabilities. Additional information includes metadata about creation, modification, and associated tags.",
    "category": "category-9",
    "tags": ["tag-a", "tag-b", "tag-19"],
    "score": 0.83,
    "active": false,
    "metadata": {
        "created_by": "system",
        "version": 10,
        "region": "global",
        "notes": "Auto-generated fixture data for line count and testing purposes. Record index 399.",
    },
}
