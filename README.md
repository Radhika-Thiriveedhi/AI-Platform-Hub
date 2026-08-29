# AI Platform Hub

A full-stack Python (Flask) web application showcasing an AI Platforms portal.

## Features
- Multi-page routing with clean URL structure
- Interactive buttons and navigation
- Mock AI model catalog, chat simulator, image generation UI, analytics dashboard
- Responsive design with modern UI
- Modular Python backend (no database required – all data is in-memory / file-based mocks)
- 50k+ lines of project code across Python modules, templates, CSS, and JS

## Tech Stack
- Backend: Python 3 + Flask
- Frontend: HTML5, CSS3, Vanilla JavaScript
- Templating: Jinja2

## How to Run
```bash
pip install -r requirements.txt
python run.py
```
Then open http://127.0.0.1:5000

## Project Structure
```
ai_platform_hub/
├── app/                 # Application factory and blueprints
├── modules/             # Feature modules (models, chat, analytics, etc.)
├── templates/           # Jinja2 HTML templates
├── static/              # CSS, JS, images
├── data/                # Mock JSON data
├── utils/               # Helper utilities
├── run.py               # Entry point
└── requirements.txt
```

## Pages Included
- Home / Landing
- AI Models Catalog
- Model Detail pages
- Chat Interface (mock)
- Image Generation Studio
- Text Analysis Tools
- Analytics Dashboard
- Pricing
- Documentation
- Blog / News
- About / Team
- Contact
- Feature comparison
- API Reference (mock)
- And many more sub-pages

Created for educational / assignment purposes.
