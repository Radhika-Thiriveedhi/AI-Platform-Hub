"""
Team Module
Mock team member data for the About page.
"""

from typing import List, Dict, Any

TEAM_MEMBERS = [
    {
        "id": "1",
        "name": "Alex Rivera",
        "role": "CEO & Co-Founder",
        "bio": "Former ML engineer at a major tech company. Passionate about making AI accessible to every developer.",
        "avatar_color": "#4A90D9",
        "social": {"twitter": "#", "linkedin": "#"},
    },
    {
        "id": "2",
        "name": "Jordan Lee",
        "role": "CTO & Co-Founder",
        "bio": "Systems architect with deep experience in distributed inference and model serving infrastructure.",
        "avatar_color": "#E91E63",
        "social": {"twitter": "#", "linkedin": "#", "github": "#"},
    },
    {
        "id": "3",
        "name": "Sam Patel",
        "role": "Head of AI Research",
        "bio": "PhD in Machine Learning. Leads evaluation, safety, and new model integration efforts.",
        "avatar_color": "#9C27B0",
        "social": {"twitter": "#", "linkedin": "#"},
    },
    {
        "id": "4",
        "name": "Morgan Chen",
        "role": "Head of Product",
        "bio": "Product leader focused on developer experience and building intuitive AI tools.",
        "avatar_color": "#FF9800",
        "social": {"twitter": "#", "linkedin": "#"},
    },
    {
        "id": "5",
        "name": "Taylor Brooks",
        "role": "Head of Engineering",
        "bio": "Full-stack engineer turned engineering manager. Loves reliable systems and clean APIs.",
        "avatar_color": "#00BCD4",
        "social": {"github": "#", "linkedin": "#"},
    },
    {
        "id": "6",
        "name": "Casey Nguyen",
        "role": "Head of Developer Relations",
        "bio": "Community builder and educator. Helps developers succeed with AI Platform Hub.",
        "avatar_color": "#8BC34A",
        "social": {"twitter": "#", "linkedin": "#", "github": "#"},
    },
    {
        "id": "7",
        "name": "Riley Quinn",
        "role": "Lead Designer",
        "bio": "Designs beautiful, accessible interfaces that make complex AI capabilities feel simple.",
        "avatar_color": "#FF5722",
        "social": {"twitter": "#", "linkedin": "#"},
    },
    {
        "id": "8",
        "name": "Avery Kim",
        "role": "Security & Compliance Lead",
        "bio": "Ensures the platform meets enterprise security standards and regulatory requirements.",
        "avatar_color": "#607D8B",
        "social": {"linkedin": "#"},
    },
]


def get_team_members() -> List[Dict[str, Any]]:
    """Return the list of team members."""
    return TEAM_MEMBERS.copy()


def get_member_by_id(member_id: str) -> Dict[str, Any] | None:
    """Retrieve a team member by ID."""
    for member in TEAM_MEMBERS:
        if member["id"] == member_id:
            return member.copy()
    return None
