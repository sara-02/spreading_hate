import flask
from flask import Flask, request, jsonify
import json

from profile_threshold_model import ProfileThresholdHate
from form_js_output import FormOutput

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    result = {}
    result["Working"] = "True"
    result["sample_result"] = {}
    result["Model"] = "Profile Threshold"
    return jsonify(result)


@app.route('/api/test', methods=['GET', 'POST'])
def dummy_test():
    update_nodes = pth.run_model([])
    print("un", len(update_nodes))
    result_model = out_.update_iter_1_scores(update_nodes)
    return jsonify(result_model)


@app.route('/api/predict_single_iter', methods=['POST'])
def predict():
    data = request.get_json()
    infected_nodes = data.get("infected_nodes", [])
    update_nodes = pth.run_model(infected_nodes)
    print("un", len(update_nodes))
    result_model = out_.update_iter_1_scores(update_nodes)
    return jsonify(result_model)


if __name__ == '__main__':
    pth = ProfileThresholdHate()
    out_ = FormOutput()
    app.run(host="localhost", port=8092, debug=True)