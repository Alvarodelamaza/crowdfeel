
from tensorflow.keras import  models
import pickle
def load_model():
    # from google.cloud import storage

    # BUCKET_NAME = "crowdfeel_data"

    # storage_filename = "models/baseline.pickle"
    # local_filename = "baseline.pickle"

    # client = storage.Client()
    # bucket = client.bucket(BUCKET_NAME)
    # blob = bucket.blob(storage_filename)
    # blob.download_to_filename(local_filename)
    """
    load the latest saved model, return None if no model found
    """
    # get model from pickle

    model = pickle.load(open("baseline.pickle","rb"))
    print('✅ Model loaded')
    return model
