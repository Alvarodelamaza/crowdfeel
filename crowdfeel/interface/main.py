from taxifare.ml_logic.data import (clean_data,
                                    get_chunk,
                                    save_chunk)

from taxifare.ml_logic.params import (CHUNK_SIZE,
                                      DATASET_SIZE,
                                      VALIDATION_DATASET_SIZE)

from taxifare.ml_logic.preprocessor import preprocess_features

from taxifare.ml_logic.utils import get_dataset_timestamp

import numpy as np
import pandas as pd

from colorama import Fore, Style





def pred(lat,lon: pd.DataFrame = None) -> np.ndarray:

    x_pred=geo_query(params)
    model = load_model(x_pred)

    # preprocess the new data
    # $CODE_BEGIN
    X_processed = preprocess_tweets(X_pred)
    # $CODE_END

    # make a prediction
    # $CODE_BEGIN
    y_pred = model.predict(X_processed)
    # $CODE_END

    # 🧪 Write outputs so that they can be tested by make test_train_at_scale (do not remove)
    print("✅ prediction done: ", y_pred, y_pred.shape)

    return y_pred


if __name__ == '__main__':

    pred()
