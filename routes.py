from flask import Blueprint, jsonify, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from models import Topic, User

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
@login_required
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
# AUTH ROUTES
# -----------------------------
@main.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form_data = {
        "username": "",
        "email": "",
    }

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        form_data["username"] = username
        form_data["email"] = email

        if not username:
            flash("Username is required.", "error")
            return render_template("signup.html", form_data=form_data)

        if not email:
            flash("Email is required.", "error")
            return render_template("signup.html", form_data=form_data)

        if not password:
            flash("Password is required.", "error")
            return render_template("signup.html", form_data=form_data)

        if not confirm_password:
            flash("Confirm password is required.", "error")
            return render_template("signup.html", form_data=form_data)

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return render_template("signup.html", form_data=form_data)

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("An account with this email already exists.", "error")
            return render_template("signup.html", form_data=form_data)

        user = User(username=username, email=email)
        user.set_password(password)

        from models import db
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash("Account created successfully.", "success")
        return redirect(url_for("main.home"))

    return render_template("signup.html", form_data=form_data)


@main.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form_data = {
        "email": "",
    }

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        form_data["email"] = email

        if not email:
            flash("Email is required.", "error")
            return render_template("login.html", form_data=form_data)

        if not password:
            flash("Password is required.", "error")
            return render_template("login.html", form_data=form_data)

        user = User.query.filter_by(email=email).first()

        if user is None or not user.check_password(password):
            flash("Incorrect email or password.", "error")
            return render_template("login.html", form_data=form_data)

        login_user(user)
        flash("Logged in successfully.", "success")
        return redirect(url_for("main.home"))

    return render_template("login.html", form_data=form_data)


@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("main.home"))


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