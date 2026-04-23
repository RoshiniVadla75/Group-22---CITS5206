def test_app_created(app):
    """Check app is created correctly"""
    assert app is not None
    assert app.config["TESTING"] is True


def test_home_route(client):
    """Test home page loads"""
    response = client.get("/")
    assert response.status_code == 200


def test_404_page(client):
    """Test invalid route returns 404"""
    response = client.get("/nonexistent-page")
    assert response.status_code == 404


def test_login_page(client):
    """Test login page loads (if route exists)"""
    response = client.get("/login")
    assert response.status_code in [200, 302]  
    # 302 if redirect (login_required etc.)