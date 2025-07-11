import os
import joblib
import json
import numpy as np

def model_fn(model_dir):
    model_path = os.path.join(model_dir, 'model.pkl')
    model = joblib.load(model_path)
    return model

def input_fn(request_body, request_content_type):
    if request_content_type == 'application/json':
        data = json.loads(request_body)
        instances = np.array(data['instances'])
        return instances
    else:
        raise ValueError(f"Unsupported content type: {request_content_type}")

def predict_fn(input_data, model):
    predictions = model.predict(input_data)
    return predictions

def output_fn(predictions, response_content_type):
    result = json.dumps({"predictions": predictions.tolist()})
    return result
