from flask import Flask, render_template


CHECKOUT_URL = "https://app.coinzz.com.br/checkout/uma-unidade-3wcwr-0"


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def home():
        return render_template("index.html", checkout_url=CHECKOUT_URL)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
