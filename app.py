from flask import Flask, render_template, request, abort, redirect, url_for
from models import db, Topic


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    @app.route("/")
    def home():
        topics = Topic.query.order_by(Topic.id).all()
        return render_template("home.html", topics=topics)

    @app.route("/home")
    def home_alias():
        return redirect(url_for("home"))

    @app.route("/home.html")
    def home_html_alias():
        return redirect(url_for("home"))

    @app.route("/topic/<slug>")
    def topic_detail(slug):
        topic = Topic.query.filter_by(slug=slug).first()
        if topic is None:
            abort(404)
        return render_template("topic_detail.html", topic=topic)

    @app.route("/search")
    def search():
        query = request.args.get("q", "").strip()

        if not query:
            results = []
        else:
            search_pattern = f"%{query}%"
            results = Topic.query.filter(
                db.or_(
                    Topic.title.ilike(search_pattern),
                    Topic.category.ilike(search_pattern),
                    Topic.year_range.ilike(search_pattern),
                    Topic.short_summary.ilike(search_pattern),
                    Topic.intro_text.ilike(search_pattern),
                    Topic.wa_context.ilike(search_pattern),
                )
            ).order_by(Topic.id).all()

        return render_template("search.html", topics=results, query=query)

    @app.route("/search.html")
    def search_html_alias():
        return redirect(url_for("search"))

    @app.route("/timeline")
    def timeline():
        return "<h1>Timeline page placeholder</h1>"

    @app.route("/timeline.html")
    def timeline_html_alias():
        return redirect(url_for("timeline"))

    @app.route("/guided_tour")
    def guided_tour():
        return "<h1>Guided Tour page placeholder</h1>"

    @app.route("/guided_tour.html")
    def guided_tour_html_alias():
        return redirect(url_for("guided_tour"))

    @app.route("/explore_WA")
    def explore_wa():
        return "<h1>Explore WA page placeholder</h1>"

    @app.route("/explore_WA.html")
    def explore_wa_html_alias():
        return redirect(url_for("explore_wa"))

    @app.errorhandler(404)
    def page_not_found(error):
        return "<h1>404 - Page Not Found</h1>", 404

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)