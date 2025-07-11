from flask import Flask, render_template, request, jsonify
import boto3
import json

app = Flask(__name__)

# SageMaker Endpoint name
ENDPOINT_NAME = 'house-price-predictor'
REGION = 'us-east-1'  # Replace with your AWS region

# SageMaker runtime client
sagemaker_runtime = boto3.client('sagemaker-runtime', region_name=REGION)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form data
        sqft = int(request.form['square_feet'])
        bedrooms = int(request.form['num_bedrooms'])
        bathrooms = int(request.form['num_bathrooms'])
        floors = int(request.form['garage'])
        year_built = int(request.form['year_built'])

        # Prepare the input payload
        input_data = {
            "instances": [[sqft, bedrooms, bathrooms, floors, year_built]]
        }

        # Invoke the SageMaker endpoint
        response = sagemaker_runtime.invoke_endpoint(
            EndpointName=ENDPOINT_NAME,
            Body=json.dumps(input_data),
            ContentType='application/json'
        )

        # Parse the response
        result = json.loads(response['Body'].read())
        prediction = result['predictions'][0]

        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
