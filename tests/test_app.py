from app import CHECKOUT_URL, create_app


def test_home_loads_product_and_checkout():
    app = create_app()
    app.config.update(TESTING=True)

    response = app.test_client().get("/")

    assert response.status_code == 200
    assert "Cutelo Chef Grande" in response.get_data(as_text=True)
    assert CHECKOUT_URL in response.get_data(as_text=True)


def test_health_endpoint():
    app = create_app()
    app.config.update(TESTING=True)

    response = app.test_client().get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
