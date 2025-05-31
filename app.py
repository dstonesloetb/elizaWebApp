from flask import Flask, render_template, request
from Eliza import findKeywords, answer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    response = ""
    if request.method == "POST":
        user_input = request.form["message"]
        if user_input.strip():
            keywords, words = findKeywords(user_input)
            response = answer(keywords, words) or "Please tell me more."
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
