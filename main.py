from flask import Flask
from config import Config
from app.routes import main as routes_blueprint

# Explicitly specify template and static folders
app = Flask(
    __name__, template_folder="app/templates", static_folder="app/static"
)
app.config.from_object(Config)

# Register the blueprint
app.register_blueprint(routes_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
