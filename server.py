from flask import Flask, request, jsonify, render_template
from Directory import download_audio, download_video  # Importăm funcțiile existente
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite cereri între domenii pentru interfața web

@app.route('/')
def home():
    return render_template("index.html")  # Asigură-te că ai fișierul index.html în același folder

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get("url")
    media_type = data.get("type")

    if not url:
        return jsonify({"message": "Invalid URL"}), 400

    if media_type == "audio":
        result = download_audio(url)
    elif media_type == "video":
        result = download_video(url)
    else:
        return jsonify({"message": "Invalid download type"}), 400

    return jsonify({"message": result})

if __name__ == '__main__':
    app.run(debug=True)
