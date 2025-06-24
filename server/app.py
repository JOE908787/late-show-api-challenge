from server.config import app, db
from server.controllers import auth_bp, guests_bp, episodes_bp, appearances_bp

app.register_blueprint(auth_bp)
app.register_blueprint(guests_bp)
app.register_blueprint(episodes_bp)
app.register_blueprint(appearances_bp)

if __name__ == '__main__':
    app.run(debug=True)