from flask import Blueprint, jsonify, render_template, request
from models import Topic

main = Blueprint("main", __name__)


@main.route("/")
def home():
    topics = Topic.query.order_by(Topic.id.asc()).all()
    return render_template("home.html", topics=topics)


@main.route("/timeline")
def timeline():
    topics = Topic.query.order_by(Topic.id.asc()).all()
    return render_template("timeline.html", topics=topics)


@main.route("/guided-tour")
def guided_tour():
    topics = Topic.query.order_by(Topic.id.asc()).all()
    return render_template("guided_tour.html", topics=topics)


@main.route("/explore-wa")
def explore_wa():
    topics = Topic.query.order_by(Topic.id.asc()).all()
    return render_template("explore_WA.html", topics=topics)


@main.route("/search")
def search():
    query = request.args.get("q", "").strip()

    if query:
        topics = Topic.query.filter(
            Topic.title.ilike(f"%{query}%") |
            Topic.category.ilike(f"%{query}%") |
            Topic.short_summary.ilike(f"%{query}%") |
            Topic.wa_context.ilike(f"%{query}%")
        ).order_by(Topic.id.asc()).all()
    else:
        topics = Topic.query.order_by(Topic.id.asc()).all()

    return render_template("search.html", topics=topics, query=query)


@main.route("/topic/<slug>")
def topic_detail(slug):
    topic = Topic.query.filter_by(slug=slug).first_or_404()
    return render_template("topic_detail.html", topic=topic)


# -----------------------------
# API ROUTES
# -----------------------------
@main.route("/api/topics")
def api_topics():
    topics = Topic.query.order_by(Topic.id.asc()).all()

    return jsonify([
        {
            "id": topic.id,
            "slug": topic.slug,
            "title": topic.title,
            "yearRange": topic.year_range,
            "category": topic.category,
            "status": topic.status,
            "introText": topic.intro_text,
            "shortSummary": topic.short_summary,
            "howItWorks": topic.how_it_works,
            "simpleExample": topic.simple_example,
            "effectiveUse": topic.effective_use,
            "realWorldExamples": topic.real_world_examples,
            "advantages": topic.advantages,
            "limitations": topic.limitations,
            "misuse": topic.misuse,
            "ethics": topic.ethics,
            "waContext": topic.wa_context,
            "media": [
                {
                    "id": media.id,
                    "type": media.type,
                    "title": media.title,
                    "url": media.url,
                    "caption": media.caption
                }
                for media in topic.media
            ],
            "references": [
                {
                    "id": ref.id,
                    "title": ref.title,
                    "url": ref.url,
                    "sourceType": ref.source_type,
                    "accessedDate": ref.accessed_date,
                    "notes": ref.notes
                }
                for ref in topic.references
            ]
        }
        for topic in topics
    ])


@main.route("/api/topics/<slug>")
def api_topic_detail(slug):
    topic = Topic.query.filter_by(slug=slug).first_or_404()

    return jsonify({
        "id": topic.id,
        "slug": topic.slug,
        "title": topic.title,
        "yearRange": topic.year_range,
        "category": topic.category,
        "status": topic.status,
        "introText": topic.intro_text,
        "shortSummary": topic.short_summary,
        "howItWorks": topic.how_it_works,
        "simpleExample": topic.simple_example,
        "effectiveUse": topic.effective_use,
        "realWorldExamples": topic.real_world_examples,
        "advantages": topic.advantages,
        "limitations": topic.limitations,
        "misuse": topic.misuse,
        "ethics": topic.ethics,
        "waContext": topic.wa_context,
        "media": [
            {
                "id": media.id,
                "type": media.type,
                "title": media.title,
                "url": media.url,
                "caption": media.caption
            }
            for media in topic.media
        ],
        "references": [
            {
                "id": ref.id,
                "title": ref.title,
                "url": ref.url,
                "sourceType": ref.source_type,
                "accessedDate": ref.accessed_date,
                "notes": ref.notes
            }
            for ref in topic.references
        ]
    })