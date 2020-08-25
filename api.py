import flask
from flask import Flask, request, jsonify
import json

from profile_threshold_model import ProfileThresholdHate
from form_js_output import FormOutput
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def hello():
    result = {}
    result["Working"] = "True"
    result["sample_result"] = {}
    result["Model"] = "Profile Threshold"
    return jsonify(result)


@app.route('/api/infect_predict', methods=['POST'])
def predict():
    data = request.get_json()
    infected_nodes = data.get("infected_nodes")
    if infected_nodes is None or len(infected_nodes) == 0:
        return jsonify({"ERROR": "No input nodes provided."})
    max_iterations = data.get("max_iter")
    if max_iterations is None or max_iterations < 2:
        return jsonify(
            {"ERROR": "Max iter must be an Integer greater than 2."})
    iterations_result = pth.run_model(infected_nodes, max_iterations)
    result_model = out_.update_output_scores(iterations_result)
    return jsonify(result_model)


if __name__ == '__main__':
    pth = ProfileThresholdHate()
    out_ = FormOutput()
    app.run(host="localhost", port=8092, debug=True)
