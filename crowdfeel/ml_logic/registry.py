import pickle

from crowdfeel.ml_logic.params import CREDENTIAL
def load_model_emo():
    """
    load the latest saved model (7 DIFFERENT EMOTIONS), return None if no model found
    """
    local_filename = "improved_baseline.pickle"
    #Once has been run locally, yo can comment from....:

    #HERE

    # from google.cloud import storage
    # BUCKET_NAME = "crowdfeel_data"
    # storage_filename = "models/improved_baseline.pickle"
    # client = storage.Client(credentials=CREDENTIAL)
    # bucket = client.bucket(BUCKET_NAME)
    # blob = bucket.blob(storage_filename)
    # blob.download_to_filename(local_filename)

    #UNTIL HERE

    #So we are not calling Gcloud stoarge all the time

    # get model from pickle

    model = pickle.load(open(local_filename,"rb"))
    print('✅ Model lodaded')
    return model

def load_model():
    """
    load the latest saved model (POSITIVE/NEGATIVE), return None if no model found
    """
    local_filename = "baseline.pickle"
    #Once has been run locally, yo can comment from....:

    #HERE

    # from google.cloud import storage
    # BUCKET_NAME = "crowdfeel_data"
    # storage_filename = "models/baseline.pickle"
    # client = storage.Client(credentials=CREDENTIAL)
    # bucket = client.bucket(BUCKET_NAME)
    # blob = bucket.blob(storage_filename)
    # blob.download_to_filename(local_filename)

    #UNTIL HERE


    # get model from pickle

    model = pickle.load(open(local_filename,"rb"))
    print('✅ Model lodaded')
    return model
