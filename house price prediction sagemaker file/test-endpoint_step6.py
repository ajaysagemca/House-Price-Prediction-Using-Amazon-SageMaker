import boto3
import json

# Replace with your endpoint name
endpoint_name = "house-price-predictor"

# Define input payload
input_data = {
    "instances": [
        [3, 2, 1500, 1, 2000],  # Example features
        [4, 3, 2500, 2, 3000]   # Example features
    ]
}

# Create a SageMaker runtime client
sagemaker_runtime = boto3.client('sagemaker-runtime')

# Invoke the endpoint
response = sagemaker_runtime.invoke_endpoint(

    EndpointName=endpoint_name,
    Body=json.dumps(input_data),
    ContentType='application/json'
)

# Parse the response
result = json.loads(response['Body'].read())
print("Predictions:", result)
