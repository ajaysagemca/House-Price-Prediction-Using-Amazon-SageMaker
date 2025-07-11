import subprocess

# Run the AWS CLI command using subprocess
command = "aws s3 cp model.tar.gz s3://ajay909871/model.tar.gz"
subprocess.run(command, shell=True, check=True)