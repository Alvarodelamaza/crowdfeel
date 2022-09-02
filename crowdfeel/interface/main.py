
from crowdfeel.ml_logic.preprocessor import preprocess_tweets
from crowdfeel.TweepyAPI.twitterapi import geo_query
from crowdfeel.ml_logic.registry import load_model
import numpy as np
import tensorflow as tf
import pandas as pd
from transformers import BertTokenizer


def pred(distance,location: pd.DataFrame = None) -> np.ndarray:

    model = load_model()
    X_pred=geo_query(int(distance),str(location))

    # preprocess the new data
    # $CODE_BEGIN
    X_processed = preprocess_tweets(X_pred)
    # $CODE_END

    # make a prediction
    # $CODE_BEGIN
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    print('✅Tokenizer loaded')
    tf_batch = tokenizer(X_processed, max_length=128, padding=True, truncation=True, return_tensors='tf')
    print('✅batch loaded')
    tf_outputs = model(tf_batch)
    print('✅ model predict')
    tf_predictions = tf.nn.softmax(tf_outputs[0], axis=-1)
    print('✅ softmax')
    label = tf.argmax(tf_predictions, axis=1)
    print('✅ argmax')
    y_pred = label.numpy()

    # $CODE_END

    # 🧪 Write outputs so that they can be tested by make test_train_at_scale (do not remove)
    print("✅ prediction done: ", y_pred, y_pred.shape)
    return y_pred

if __name__ == '__main__':
    pred()

#
