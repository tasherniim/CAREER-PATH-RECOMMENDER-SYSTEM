from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from career_recommender import CareerRecommender
from career_map import SUBJECT_OPTIONS, INTEREST_OPTIONS

app = Flask(__name__)
CORS(app)

recommender = CareerRecommender()


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/api/meta")
def api_meta():
    return jsonify({
        "subjects": SUBJECT_OPTIONS,
        "interests": INTEREST_OPTIONS,
    })


@app.route("/api/recommend", methods=["POST"])
def recommend():
    data = request.get_json(force=True)
    interests = data.get("interests", [])
    courses_grades = data.get("courses_grades", {})

    user_data = {
        "interests": interests,
        "courses_grades": courses_grades,
    }

    scores = recommender.recommend(user_data, top_k=3)

    career_results = []
    for career_id, prob in scores.get("careers", []):
        info = recommender.get_career_info(career_id)
        career_results.append({
            "career_id": career_id,
            "name": info.get("name", f"Career {career_id}"),
            "description": info.get("description", ""),
            "probability": prob,
        })

    return jsonify({
        "careers": career_results,
        "advisories": scores.get("advisories", []),
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
