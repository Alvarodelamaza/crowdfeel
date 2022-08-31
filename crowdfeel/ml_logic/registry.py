
import pickle

def load_model():
    """
    load the latest saved model, return None if no model found
    """
    # get model from pickle

    model = pickle.load(open("baseline.pkl","rb"))

    return model
