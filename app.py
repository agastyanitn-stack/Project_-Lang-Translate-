from flask import Flask, render_template, request
from translate import translate_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        text = request.form["text"]
        lang = request.form["language"]
        result = translate_text(text, lang)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
