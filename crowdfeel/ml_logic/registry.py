
import glob
import os
from crowdfeel.ml_logic.params import LOCAL_REGISTRY_PATH
from tensorflow.keras import  models

def load_model():
    """
    load the latest saved model, return None if no model found
    """
    # get latest model version
    model_directory = os.path.join(LOCAL_REGISTRY_PATH, "models")

    results = glob.glob(f"{model_directory}/*")
    if not results:
        return None

    model_path = sorted(results)[-1]
    print(f"- path: {model_path}")

    model = models.load_model(model_path)
    print("\n✅ model loaded from disk")

    return model
