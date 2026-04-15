from flask import Flask, render_template, request
import cloudinary
import cloudinary.uploader

app = Flask(__name__)

cloudinary.config(
    cloud_name="SEU_CLOUD_NAME",
    api_key="SUA_API_KEY",
    api_secret="SEU_API_SECRET"
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "imagem" not in request.files:
        return render_template("index.html", error="Nenhuma imagem enviada")

    file = request.files["imagem"]

    if file.filename == "":
        return render_template("index.html", error="Arquivo inválido")

    resultado = cloudinary.uploader.upload(file)
    image_url = resultado["secure_url"]

    return render_template("index.html", image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)