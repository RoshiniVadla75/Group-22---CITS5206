def test_app_created(app):
    assert app is not None


def test_secret_key_exists(app):
    assert app.config["SECRET_KEY"] is not None


def test_database_config(app):
    assert "SQLALCHEMY_DATABASE_URI" in app.config


def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200


def test_login_route(client):
    response = client.get("/login")
    assert response.status_code == 200


def test_signup_route(client):
    response = client.get("/signup")
    assert response.status_code == 200


def test_404_page(client):
    response = client.get("/non-existent-page")
    assert response.status_code == 404