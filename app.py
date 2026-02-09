from flask import Flask
from routes.auth import auth_bp
from routes.orders import orders_bp
from routes.reports import reports_bp
from routes.coupons import coupons_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(coupons_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
