from flask import Flask, request, jsonify
from formation_indus_ds_avancee.train_and_predict import predict
from formation_indus_ds_avancee.feature_engineering import prepare_features
from config import FEATURES_PATH, MODEL_PATH, PREDICTIONS_FOLDER
import pandas as pd

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({
        "status": "ok"
    })

@app.route('/predict')
def predict_endpoint():
    received_data_df = request.args.get('Ws1_avg')
    prepared_features_df = prepare_features(received_data_df, training_mode=False)
    prediction = predict(features=prepared_features_df, model_path=MODEL_PATH)['predictions'].to_dict()
    return jsonify(prediction)