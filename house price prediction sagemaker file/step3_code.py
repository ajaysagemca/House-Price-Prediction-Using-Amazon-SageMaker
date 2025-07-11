import tarfile

with tarfile.open('model.tar.gz', 'w:gz') as tar:
    tar.add('model.pkl', arcname='model.pkl')  # Ensure model.pkl is at the root
    tar.add('serve.py', arcname='serve.py')    # Ensure serve.py is at the root
