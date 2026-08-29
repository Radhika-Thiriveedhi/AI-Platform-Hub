"""
Shared mock data used across templates and routes.
"""

FEATURES_LIST = [
    {
        "id": "models",
        "title": "200+ AI Models",
        "description": "Access a curated catalog of large language models, vision systems, speech models, and specialized AI from leading providers.",
        "icon": "🧠",
        "link": "/models",
    },
    {
        "id": "chat",
        "title": "Interactive Chat",
        "description": "Experiment with conversational AI directly in the browser. Test prompts, compare responses, and iterate quickly.",
        "icon": "💬",
        "link": "/chat",
    },
    {
        "id": "image",
        "title": "Image Generation Studio",
        "description": "Create stunning images from text prompts with multiple artistic styles and fine-grained control.",
        "icon": "🎨",
        "link": "/image",
    },
    {
        "id": "analysis",
        "title": "Text Analysis Tools",
        "description": "Run sentiment analysis, entity extraction, keyword detection, summarization, and more on any text.",
        "icon": "🔍",
        "link": "/analysis",
    },
    {
        "id": "dashboard",
        "title": "Analytics Dashboard",
        "description": "Monitor usage, track costs, view performance metrics, and gain insights into your AI workloads.",
        "icon": "📊",
        "link": "/dashboard",
    },
    {
        "id": "api",
        "title": "Powerful APIs",
        "description": "Simple, consistent REST APIs with excellent documentation, SDKs, and high rate limits.",
        "icon": "⚡",
        "link": "/docs",
    },
    {
        "id": "security",
        "title": "Enterprise Security",
        "description": "SSO, role-based access, audit logs, data privacy controls, and compliance-ready infrastructure.",
        "icon": "🔒",
        "link": "/docs/platform/security",
    },
    {
        "id": "support",
        "title": "World-Class Support",
        "description": "From community forums to dedicated technical account managers, help is always available.",
        "icon": "🤝",
        "link": "/contact",
    },
]

TESTIMONIALS = [
    {
        "name": "Priya Sharma",
        "role": "CTO, TechNova",
        "quote": "AI Platform Hub let us prototype and ship AI features in days instead of months. The model catalog and clear pricing were game changers.",
        "avatar_color": "#4A90D9",
    },
    {
        "name": "Marcus Johnson",
        "role": "Lead Developer, DataFlow",
        "quote": "The developer experience is outstanding. Clean APIs, great docs, and the interactive tools helped our team ramp up incredibly fast.",
        "avatar_color": "#E91E63",
    },
    {
        "name": "Elena Volkov",
        "role": "Product Manager, InsightAI",
        "quote": "We evaluated several platforms. AI Platform Hub won on breadth of models, transparent costs, and the quality of the analytics dashboard.",
        "avatar_color": "#9C27B0",
    },
    {
        "name": "David Okonkwo",
        "role": "Founder, StartSmart",
        "quote": "As a startup, the free tier gave us room to experiment. When we scaled, the Pro plan just worked. Highly recommended.",
        "avatar_color": "#FF9800",
    },
]

FAQ_ITEMS = [
    {
        "question": "What is AI Platform Hub?",
        "answer": "AI Platform Hub is a unified platform that gives developers and organizations access to a wide range of AI models and tools — including language models, image generation, text analysis, and more — through a single interface and API.",
    },
    {
        "question": "Do I need a credit card to start?",
        "answer": "No. The Free plan requires no credit card and gives you access to a selection of models with daily quotas so you can explore and prototype freely.",
    },
    {
        "question": "How is pricing calculated?",
        "answer": "Most models are priced per token (input + output). Image generation has a per-image cost. You can set usage limits and budgets in the dashboard to control spend.",
    },
    {
        "question": "Can I use the platform commercially?",
        "answer": "Yes. All paid plans support commercial use. Check individual model licenses for any additional restrictions on open-weight models.",
    },
    {
        "question": "Is my data used for training?",
        "answer": "By default, API data is not used to train models. Enterprise customers can obtain additional contractual guarantees around data handling.",
    },
    {
        "question": "What languages are supported?",
        "answer": "Many of our language models support 50+ languages. Specific language coverage varies by model — check the model detail pages for details.",
    },
    {
        "question": "How do I get support?",
        "answer": "Free users can use community resources and documentation. Pro and higher plans include email support, with dedicated channels available on Business and Enterprise.",
    },
    {
        "question": "Can I fine-tune models?",
        "answer": "Fine-tuning is available on Pro and higher plans for selected models. Enterprise customers can also request custom training runs.",
    },
    {
        "question": "What about rate limits?",
        "answer": "Rate limits depend on your plan (requests per minute and daily/monthly quotas). You can view current limits in the dashboard and request increases as needed.",
    },
    {
        "question": "Is there an SLA?",
        "answer": "Business plans include a 99.5% uptime SLA. Enterprise plans can negotiate higher SLAs (99.9%+).",
    },
]
