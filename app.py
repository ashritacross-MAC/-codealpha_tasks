from flask import Flask, render_template, request, jsonify
import urllib.parse
import urllib.request
import json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()

    text = data.get("text", "").strip()
    source = data.get("source", "auto")
    target = data.get("target", "en")

    if not text:
        return jsonify({"error": "Please enter some text."})

    try:
        encoded_text = urllib.parse.quote(text)

        url = (
            f"https://translate.googleapis.com/translate_a/single"
            f"?client=gtx&sl={source}&tl={target}&dt=t&q={encoded_text}"
        )

        with urllib.request.urlopen(url, timeout=10) as response:
            result = json.loads(response.read().decode("utf-8"))

        translated_text = "".join(
            part[0] for part in result[0] if part[0]
        )

        return jsonify({"translation": translated_text})

    except Exception as e:
        return jsonify({
            "error": "Translation failed. Please check your internet connection."
        })


if __name__ == "__main__":
    app.run(debug=True)