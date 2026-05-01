import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app
from models import db, Topic, User


@pytest.fixture
def app_instance(tmp_path):
    db_path = tmp_path / "test.db"

    app = create_app()
    app.config.update(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{db_path}",
            "WTF_CSRF_ENABLED": False,
            "LOGIN_DISABLED": False,
        }
    )

    with app.app_context():
        db.drop_all()
        db.create_all()

        topic1 = Topic(
            slug="turing-thoughts-on-ai",
            title="Alan Turing's Thoughts on AI",
            year_range="c. 1950",
            category="Foundations",
            status="Legacy",
            intro_text="Turing intro",
            short_summary="Turing summary",
            how_it_works="Turing theory",
            simple_example="Turing example",
            effective_use="Teaching foundations",
            real_world_examples="Computer science education",
            advantages="Strong conceptual basis",
            limitations="Highly theoretical",
            misuse="Oversimplified in modern AI discussions",
            ethics="Questions about intelligence",
            wa_context="UWA teaches Turing in foundational curriculum",
        )

        topic2 = Topic(
            slug="learning-machines",
            title="Learning Machines",
            year_range="c. 1960",
            category="Machine Learning",
            status="Active",
            intro_text="Learning intro",
            short_summary="Learning summary",
            how_it_works="Learns from data",
            simple_example="Weather prediction",
            effective_use="Pattern learning",
            real_world_examples="Prediction systems",
            advantages="Adapts with data",
            limitations="Needs quality data",
            misuse="Biased predictions",
            ethics="Fairness concerns",
            wa_context="WA research groups contributed to ML",
        )

        user = User(username="testuser", email="test@example.com")
        user.set_password("password123")

        db.session.add_all([topic1, topic2, user])
        db.session.commit()

    yield app

    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app_instance):
    return app_instance.test_client()


def login(client, email="test@example.com", password="password123"):
    return client.post(
        "/login",
        data={
            "email": email,
            "password": password,
        },
        follow_redirects=True,
    )


def test_home_route_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"AI Museum" in response.data


def test_timeline_route_returns_200(client):
    response = client.get("/timeline")
    assert response.status_code == 200


def test_search_route_returns_200(client):
    response = client.get("/search")
    assert response.status_code == 200
    assert b"Search the Collection" in response.data


def test_search_route_filters_results_by_query(client):
    response = client.get("/search?q=Turing")
    assert response.status_code == 200
    assert b"Alan Turing" in response.data
    assert b"Learning Machines" not in response.data


def test_topic_detail_valid_slug(client):
    response = client.get("/topic/turing-thoughts-on-ai")
    assert response.status_code == 200
    assert b"Alan Turing" in response.data


def test_topic_detail_invalid_slug_returns_404(client):
    response = client.get("/topic/non-existent-topic")
    assert response.status_code == 404


def test_guided_tour_redirects_when_not_logged_in(client):
    response = client.get("/guided-tour", follow_redirects=False)
    assert response.status_code in (301, 302)
    assert "/login" in response.headers["Location"]


def test_guided_tour_accessible_after_login(client):
    login_response = login(client)
    assert login_response.status_code == 200

    response = client.get("/guided-tour")
    assert response.status_code == 200
    assert b"guidedTourApp" in response.data


def test_login_with_valid_credentials(client):
    response = client.post(
        "/login",
        data={
            "email": "test@example.com",
            "password": "password123",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"AI Museum" in response.data


def test_login_with_invalid_password_shows_error(client):
    response = client.post(
        "/login",
        data={
            "email": "test@example.com",
            "password": "wrongpassword",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Incorrect email or password." in response.data


def test_login_with_empty_email_shows_error(client):
    response = client.post(
        "/login",
        data={
            "email": "",
            "password": "password123",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Email is required." in response.data


def test_login_with_empty_password_shows_error(client):
    response = client.post(
        "/login",
        data={
            "email": "test@example.com",
            "password": "",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Password is required." in response.data


def test_signup_success(client):
    response = client.post(
        "/signup",
        data={
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "abc12345",
            "confirm_password": "abc12345",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"AI Museum" in response.data


def test_signup_duplicate_email_shows_error(client):
    response = client.post(
        "/signup",
        data={
            "username": "anotheruser",
            "email": "test@example.com",
            "password": "abc12345",
            "confirm_password": "abc12345",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"An account with this email already exists." in response.data


def test_logout_after_login(client):
    login(client)
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"AI Museum" in response.data


def test_api_topics_returns_json_list(client):
    response = client.get("/api/topics")
    assert response.status_code == 200
    data = response.get_json()

    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["slug"] == "turing-thoughts-on-ai"


def test_api_topic_detail_returns_single_topic(client):
    response = client.get("/api/topics/turing-thoughts-on-ai")
    assert response.status_code == 200
    data = response.get_json()

    assert data["slug"] == "turing-thoughts-on-ai"
    assert data["title"] == "Alan Turing's Thoughts on AI"


def test_api_topic_detail_invalid_slug_returns_404(client):
    response = client.get("/api/topics/not-found")
    assert response.status_code == 404
