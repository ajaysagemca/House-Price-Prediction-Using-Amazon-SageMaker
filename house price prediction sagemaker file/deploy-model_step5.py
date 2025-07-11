from sagemaker.sklearn import SKLearnModel
import sagemaker

sagemaker_session = sagemaker.Session()
role = 'arn:aws:iam::779846778586:role/service-role/AmazonSageMaker-ExecutionRole-20241203T122737'  # Replace with your IAM role

model_s3_path = 's3://ajay909871/model.tar.gz'

# Create the SKLearn model instance
model = SKLearnModel(
    model_data=model_s3_path,
    role=role,
    entry_point='serve.py',     # Inference script to use for deployment         # Directory containing the serve.py script (current directory)
    framework_version='1.0-1'   # Specify the scikit-learn version
)

# Deploy the model to an endpoint
predictor = model.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.large",
    endpoint_name="house-price-predictor"
)

print("Endpoint deployed!")
