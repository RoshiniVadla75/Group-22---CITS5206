import pytest
from flask import Flask

from models import db, Topic, Media, TopicReference, User


@pytest.fixture
def app():
    """
    Create a Flask app configured for testing with an in-memory SQLite database.
    """
    app = Flask(__name__)
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """
    Create a test client for the Flask app.
    """
    return app.test_client()


@pytest.fixture
def app_context(app):
    """
    Push an application context so database operations can run normally.
    """
    with app.app_context():
        yield


def test_topic_creation(app_context):
    """
    Verify that a Topic object can be created and stored in the database.
    """
    topic = Topic(
        slug="expert-systems",
        title="Expert Systems",
        year_range="c. 1980",
        category="Knowledge Engineering",
        intro_text="Intro text",
        short_summary="Short summary",
        how_it_works="How it works",
        simple_example="Simple example",
        effective_use="Effective use",
        real_world_examples="Real world examples",
        advantages="Advantages",
        limitations="Limitations",
        misuse="Misuse",
        ethics="Ethics",
        wa_context="WA context"
    )

    db.session.add(topic)
    db.session.commit()

    saved_topic = Topic.query.filter_by(slug="expert-systems").first()

    assert saved_topic is not None
    assert saved_topic.title == "Expert Systems"
    assert saved_topic.status == "Legacy"


def test_topic_default_status(app_context):
    """
    Verify that the default status of a Topic is set to 'Legacy'.
    """
    topic = Topic(
        slug="learning-machines",
        title="Learning Machines",
        year_range="c. 1960",
        category="Machine Learning",
        intro_text="Intro text",
        short_summary="Short summary",
        how_it_works="How it works",
        simple_example="Simple example",
        effective_use="Effective use",
        real_world_examples="Real world examples",
        advantages="Advantages",
        limitations="Limitations",
        misuse="Misuse",
        ethics="Ethics",
        wa_context="WA context"
    )

    db.session.add(topic)
    db.session.commit()

    assert topic.status == "Legacy"


def test_media_relationship(app_context):
    """
    Verify that a Topic can have related Media records.
    """
    topic = Topic(
        slug="deep-fakes",
        title="Deep Fakes",
        year_range="c. 2015",
        category="Generative AI",
        intro_text="Intro text",
        short_summary="Short summary",
        how_it_works="How it works",
        simple_example="Simple example",
        effective_use="Effective use",
        real_world_examples="Real world examples",
        advantages="Advantages",
        limitations="Limitations",
        misuse="Misuse",
        ethics="Ethics",
        wa_context="WA context"
    )

    db.session.add(topic)
    db.session.commit()

    media = Media(
        topic_id=topic.id,
        type="image",
        title="Deep Fake Example",
        url="https://example.com/image.jpg",
        caption="Example caption"
    )

    db.session.add(media)
    db.session.commit()

    saved_topic = Topic.query.filter_by(slug="deep-fakes").first()

    assert len(saved_topic.media) == 1
    assert saved_topic.media[0].title == "Deep Fake Example"


def test_reference_relationship(app_context):
    """
    Verify that a Topic can have related TopicReference records.
    """
    topic = Topic(
        slug="natural-language-processing",
        title="Natural Language Processing",
        year_range="2010-2020",
        category="Language AI",
        intro_text="Intro text",
        short_summary="Short summary",
        how_it_works="How it works",
        simple_example="Simple example",
        effective_use="Effective use",
        real_world_examples="Real world examples",
        advantages="Advantages",
        limitations="Limitations",
        misuse="Misuse",
        ethics="Ethics",
        wa_context="WA context"
    )

    db.session.add(topic)
    db.session.commit()

    reference = TopicReference(
        topic_id=topic.id,
        title="Attention Is All You Need",
        url="https://example.com/paper",
        source_type="Research Paper",
        accessed_date="2024-03-15",
        notes="Important paper"
    )

    db.session.add(reference)
    db.session.commit()

    saved_topic = Topic.query.filter_by(slug="natural-language-processing").first()

    assert len(saved_topic.references) == 1
    assert saved_topic.references[0].title == "Attention Is All You Need"


def test_user_password_hashing(app_context):
    """
    Verify that User.set_password stores a hashed password
    and User.check_password validates the correct password.
    """
    user = User(
        username="testuser",
        email="test@example.com"
    )
    user.set_password("mypassword123")

    db.session.add(user)
    db.session.commit()

    saved_user = User.query.filter_by(email="test@example.com").first()

    assert saved_user.password_hash != "mypassword123"
    assert saved_user.check_password("mypassword123") is True
    assert saved_user.check_password("wrongpassword") is False


def test_user_repr(app_context):
    """
    Verify the string representation of the User model.
    """
    user = User(
        username="alice",
        email="alice@example.com"
    )
    user.set_password("password123")

    db.session.add(user)
    db.session.commit()

    assert repr(user) == "<User alice@example.com>"


def test_topic_repr(app_context):
    """
    Verify the string representation of the Topic model.
    """
    topic = Topic(
        slug="large-language-models",
        title="Large Language Models",
        year_range="2024",
        category="Frontier AI",
        intro_text="Intro text",
        short_summary="Short summary",
        how_it_works="How it works",
        simple_example="Simple example",
        effective_use="Effective use",
        real_world_examples="Real world examples",
        advantages="Advantages",
        limitations="Limitations",
        misuse="Misuse",
        ethics="Ethics",
        wa_context="WA context"
    )

    db.session.add(topic)
    db.session.commit()

    assert repr(topic) == "<Topic Large Language Models>"