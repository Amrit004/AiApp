from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)
classifier = pipeline("sentiment-analysis")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.form["text"]
    result = classifier(text)[0]
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
