from flask import Blueprint, render_template, request, url_for
from app.qr_generator import generate_qr_code

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/generate", methods=["POST"])
def generate():
    data = request.form.get("data")
    if data:
        # Generate QR code and get the file path
        qr_file = generate_qr_code(data)
        # Create URL for the generated image
        qr_image_url = url_for("static", filename=qr_file)
        return render_template("index.html", qr_code=qr_image_url)
    return render_template("index.html")
