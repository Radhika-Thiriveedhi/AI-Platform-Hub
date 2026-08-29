"""
Central route registration for AI Platform Hub.
All blueprints are imported and registered here.
"""

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from modules.models_catalog import get_all_models, get_model_by_id, search_models, get_categories
from modules.chat_engine import process_chat_message, get_chat_history, clear_chat_history
from modules.image_gen import generate_mock_image_prompt, get_image_styles, get_recent_generations
from modules.text_analysis import analyze_text, get_analysis_types
from modules.analytics import get_dashboard_stats, get_usage_trends, get_top_models
from modules.pricing import get_pricing_plans, get_plan_details
from modules.blog import get_all_posts, get_post_by_slug, get_categories as get_blog_categories
from modules.docs import get_docs_sections, get_doc_page
from modules.team import get_team_members
from utils.helpers import format_number, truncate_text, generate_slug
from data.mock_data import FEATURES_LIST, TESTIMONIALS, FAQ_ITEMS


def register_blueprints(app):
    """Register all application blueprints."""
    app.register_blueprint(main_bp)
    app.register_blueprint(models_bp, url_prefix="/models")
    app.register_blueprint(chat_bp, url_prefix="/chat")
    app.register_blueprint(image_bp, url_prefix="/image")
    app.register_blueprint(analysis_bp, url_prefix="/analysis")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(pricing_bp, url_prefix="/pricing")
    app.register_blueprint(docs_bp, url_prefix="/docs")
    app.register_blueprint(blog_bp, url_prefix="/blog")
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(pages_bp)


# ==================== MAIN BLUEPRINT ====================
main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    """Landing page with hero, features, and CTA sections."""
    featured_models = get_all_models()[:6]
    stats = get_dashboard_stats()
    return render_template(
        "home.html",
        featured_models=featured_models,
        stats=stats,
        features=FEATURES_LIST,
        testimonials=TESTIMONIALS,
    )


@main_bp.route("/about")
def about():
    """About page with company info and mission."""
    team = get_team_members()
    return render_template("about.html", team=team)


@main_bp.route("/contact", methods=["GET", "POST"])
def contact():
    """Contact form page."""
    message = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        subject = request.form.get("subject", "").strip()
        body = request.form.get("message", "").strip()
        if name and email and body:
            message = f"Thank you {name}! Your message has been received. We will respond to {email} shortly."
        else:
            message = "Please fill in all required fields."
    return render_template("contact.html", message=message)


@main_bp.route("/features")
def features():
    """Detailed features overview page."""
    return render_template("features.html", features=FEATURES_LIST)


@main_bp.route("/faq")
def faq():
    """Frequently Asked Questions page."""
    return render_template("faq.html", faqs=FAQ_ITEMS)


# ==================== MODELS BLUEPRINT ====================
models_bp = Blueprint("models", __name__)


@models_bp.route("/")
def models_list():
    """AI Models catalog with filtering and search."""
    category = request.args.get("category", "all")
    query = request.args.get("q", "").strip()
    page = max(request.args.get("page", 1, type=int) or 1, 1)

    if query:
        models = search_models(query)
    elif category != "all":
        models = [m for m in get_all_models() if m.get("category") == category]
    else:
        models = get_all_models()

    categories = get_categories()
    per_page = 12
    total = len(models)
    start = (page - 1) * per_page
    end = start + per_page
    paginated = models[start:end]

    return render_template(
        "models/list.html",
        models=paginated,
        categories=categories,
        current_category=category,
        query=query,
        page=page,
        total_pages=(total + per_page - 1) // per_page,
        total=total,
    )


@models_bp.route("/<model_id>")
def model_detail(model_id):
    """Individual model detail page."""
    model = get_model_by_id(model_id)
    if not model:
        return render_template("errors/404.html"), 404
    related = [m for m in get_all_models() if m["category"] == model["category"] and m["id"] != model_id][:4]
    return render_template("models/detail.html", model=model, related=related)


@models_bp.route("/compare")
def models_compare():
    """Side-by-side model comparison page."""
    ids = request.args.getlist("ids")
    models = [get_model_by_id(i) for i in ids if get_model_by_id(i)]
    return render_template("models/compare.html", models=models)


# ==================== CHAT BLUEPRINT ====================
chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/")
def chat_interface():
    """Interactive chat interface page."""
    history = get_chat_history()
    return render_template("chat/interface.html", history=history)


@chat_bp.route("/send", methods=["POST"])
def chat_send():
    """Handle chat message submission (AJAX or form)."""
    payload = request.get_json(silent=True) or {}
    message = request.form.get("message") or payload.get("message", "")
    if not message:
        return jsonify({"error": "Empty message"}), 400
    response = process_chat_message(message)
    return jsonify(response)


@chat_bp.route("/clear", methods=["POST"])
def chat_clear():
    """Clear chat history."""
    clear_chat_history()
    return redirect(url_for("chat.chat_interface"))


# ==================== IMAGE GENERATION BLUEPRINT ====================
image_bp = Blueprint("image", __name__)


@image_bp.route("/")
def image_studio():
    """Image generation studio page."""
    styles = get_image_styles()
    recent = get_recent_generations()
    return render_template("image/studio.html", styles=styles, recent=recent)


@image_bp.route("/generate", methods=["POST"])
def image_generate():
    """Mock image generation endpoint."""
    prompt = request.form.get("prompt", "").strip()
    style = request.form.get("style", "realistic")
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    result = generate_mock_image_prompt(prompt, style)
    return jsonify(result)


# ==================== TEXT ANALYSIS BLUEPRINT ====================
analysis_bp = Blueprint("analysis", __name__)


@analysis_bp.route("/")
def analysis_tools():
    """Text analysis tools page."""
    types = get_analysis_types()
    return render_template("analysis/tools.html", analysis_types=types)


@analysis_bp.route("/run", methods=["POST"])
def analysis_run():
    """Run text analysis on submitted content."""
    text = request.form.get("text", "").strip()
    analysis_type = request.form.get("type", "sentiment")
    if not text:
        return jsonify({"error": "Text is required"}), 400
    result = analyze_text(text, analysis_type)
    return jsonify(result)


# ==================== DASHBOARD BLUEPRINT ====================
dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def dashboard_home():
    """Main analytics dashboard."""
    stats = get_dashboard_stats()
    trends = get_usage_trends()
    top_models = get_top_models()
    return render_template(
        "dashboard/home.html",
        stats=stats,
        trends=trends,
        top_models=top_models,
    )


@dashboard_bp.route("/usage")
def dashboard_usage():
    """Detailed usage analytics page."""
    trends = get_usage_trends()
    return render_template("dashboard/usage.html", trends=trends)


# ==================== PRICING BLUEPRINT ====================
pricing_bp = Blueprint("pricing", __name__)


@pricing_bp.route("/")
def pricing_plans():
    """Pricing plans overview."""
    plans = get_pricing_plans()
    return render_template("pricing/plans.html", plans=plans)


@pricing_bp.route("/<plan_id>")
def pricing_detail(plan_id):
    """Individual plan details."""
    plan = get_plan_details(plan_id)
    if not plan:
        return render_template("errors/404.html"), 404
    return render_template("pricing/detail.html", plan=plan)


# ==================== DOCS BLUEPRINT ====================
docs_bp = Blueprint("docs", __name__)


@docs_bp.route("/")
def docs_index():
    """Documentation home / table of contents."""
    sections = get_docs_sections()
    return render_template("docs/index.html", sections=sections)


@docs_bp.route("/<section>/<page>")
def docs_page(section, page):
    """Individual documentation page."""
    content = get_doc_page(section, page)
    if not content:
        return render_template("errors/404.html"), 404
    sections = get_docs_sections()
    return render_template("docs/page.html", content=content, sections=sections, current_section=section)


# ==================== BLOG BLUEPRINT ====================
blog_bp = Blueprint("blog", __name__)


@blog_bp.route("/")
def blog_list():
    """Blog posts listing."""
    category = request.args.get("category", "all")
    posts = get_all_posts()
    if category != "all":
        posts = [p for p in posts if p.get("category") == category]
    categories = get_blog_categories()
    return render_template("blog/list.html", posts=posts, categories=categories, current_category=category)


@blog_bp.route("/<slug>")
def blog_post(slug):
    """Single blog post page."""
    post = get_post_by_slug(slug)
    if not post:
        return render_template("errors/404.html"), 404
    return render_template("blog/post.html", post=post)


# ==================== API BLUEPRINT (Mock JSON endpoints) ====================
api_bp = Blueprint("api", __name__)


@api_bp.route("/models")
def api_models():
    """JSON API for models list."""
    return jsonify(get_all_models())


@api_bp.route("/models/<model_id>")
def api_model_detail(model_id):
    """JSON API for single model."""
    model = get_model_by_id(model_id)
    if not model:
        return jsonify({"error": "Not found"}), 404
    return jsonify(model)


@api_bp.route("/stats")
def api_stats():
    """JSON API for dashboard stats."""
    return jsonify(get_dashboard_stats())


@api_bp.route("/health")
def api_health():
    """Health check endpoint."""
    return jsonify({"status": "ok", "service": "AI Platform Hub"})


# ==================== MISC PAGES BLUEPRINT ====================
pages_bp = Blueprint("pages", __name__)


@pages_bp.route("/privacy")
def privacy():
    return render_template("pages/privacy.html")


@pages_bp.route("/terms")
def terms():
    return render_template("pages/terms.html")


@pages_bp.route("/careers")
def careers():
    return render_template("pages/careers.html")


@pages_bp.route("/partners")
def partners():
    return render_template("pages/partners.html")


@pages_bp.route("/changelog")
def changelog():
    return render_template("pages/changelog.html")


@pages_bp.route("/status")
def status():
    return render_template("pages/status.html")
