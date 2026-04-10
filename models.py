"""
Database schema for the AI Museum project.

Tables:
- Topic: stores the main content for each AI paradigm shift
- Media: stores images or media items related to a topic
- TopicReference: stores references and sources related to a topic
- User: handles authentication (login, signup)

Relationships:
- One Topic has many Media records
- One Topic has many TopicReference records
"""

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Topic(db.Model):
    __tablename__ = "topics"

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    year_range = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Legacy")

    intro_text = db.Column(db.Text, nullable=False)
    short_summary = db.Column(db.Text, nullable=False)
    how_it_works = db.Column(db.Text, nullable=False)
    simple_example = db.Column(db.Text, nullable=False)
    effective_use = db.Column(db.Text, nullable=False)
    real_world_examples = db.Column(db.Text, nullable=False)
    advantages = db.Column(db.Text, nullable=False)
    limitations = db.Column(db.Text, nullable=False)
    misuse = db.Column(db.Text, nullable=False)
    ethics = db.Column(db.Text, nullable=False)
    wa_context = db.Column(db.Text, nullable=False)

    media = db.relationship(
        "Media",
        backref="topic",
        lazy=True,
        cascade="all, delete-orphan"
    )

    references = db.relationship(
        "TopicReference",
        backref="topic",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Topic {self.title}>"


class Media(db.Model):
    __tablename__ = "media"

    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey("topics.id"), nullable=False)

    type = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    caption = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Media {self.title}>"


class TopicReference(db.Model):
    __tablename__ = "topic_references"

    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey("topics.id"), nullable=False)

    title = db.Column(db.String(300), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    source_type = db.Column(db.String(100), nullable=False)
    accessed_date = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<TopicReference {self.title}>"


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.email}>"