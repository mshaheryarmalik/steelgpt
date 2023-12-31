from flask import Flask, request, jsonify, json
from flask_cors import CORS
from .scrapper import get_contents_from_query
from .constants import MAX_SEARCH_LINKS
from .energycomsumption import EnergyConsumptionEstimator
app = Flask(__name__)
CORS(app)


@app.route("/api")
def api():
    return jsonify(message="Hello Malik, this is the Flask API!")


@app.route("/api/generate", methods=["POST"])
def generate():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Check if 'text' is present in the JSON data
        if "text" in data:
            input_text = data["text"]
            # Get scrapped data
            scrapped_data = []
            for value in get_contents_from_query(input_text, link_num=MAX_SEARCH_LINKS):
                scrapped_data.append(value)

            # TODO: LLM Model Prediction

            # Estimate energy consumption for light weight and large model
            energy_estimator = EnergyConsumptionEstimator()
            total_energy_consumed_small = energy_estimator.estimate_energy_consumption_small(MAX_SEARCH_LINKS)
            total_energy_consumed_large = energy_estimator.estimate_energy_consumption_large()

            # Return the processed text as JSON response
            return {"output": json.dumps(scrapped_data), "energy_kilojoules_lightweight": total_energy_consumed_small, "energy_kilojoules_large": total_energy_consumed_large}
        else:
            return jsonify({"error": 'Invalid request. Missing "text" parameter.'}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
