from flask import Flask, render_template, request
from questionnaire import anxiety_questionnaire
from text_analysis import analyze_text
from face_analysis import analyze_face

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        answers = [
            int(request.form["q1"]),
            int(request.form["q2"]),
            int(request.form["q3"]),
            int(request.form["q4"]),
            int(request.form["q5"])
        ]

        questionnaire_result = anxiety_questionnaire(answers)
        text_result = analyze_text(request.form["text"])
        face_result = analyze_face()

        return render_template(
            "result.html",
            score=questionnaire_result["score"],
            level=questionnaire_result["level"],
            text=text_result,
            face=face_result
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

