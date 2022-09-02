
from crowdfeel.ml_logic.preprocessor import preprocess_tweets
from crowdfeel.TweepyAPI.twitterapi import geo_query
from crowdfeel.TweepyAPI.twitterapi import hashtag_query
import numpy as np
import tensorflow as tf
import pandas as pd
from transformers import BertTokenizer


def pred(model,distance,location) -> np.ndarray:

    #model = load_model()
    X_pred=geo_query(int(distance),str(location))

    # preprocess the new data
    # $CODE_BEGIN
    X_processed = preprocess_tweets(X_pred)
    # $CODE_END

    # make a prediction
    # $CODE_BEGIN
    # RobertaTokenizer
    # 
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    print('✅Tokenizer loaded')
    tf_batch = tokenizer(X_processed, max_length=128, padding=True, truncation=True, return_tensors='tf')

    tf_outputs = model.serving(tf_batch)
    print('✅ model predict')
    tf_predictions = tf.nn.softmax(tf_outputs['logits'], axis=-1)

    label = tf.argmax(tf_predictions, axis=1)

    y_pred = label.numpy()

    # $CODE_END

    # 🧪 Write outputs so that they can be tested by make test_train_at_scale (do not remove)
    print("✅ prediction done: ", y_pred, y_pred.shape)
    results={
        'emotion': y_pred,
        'tweets':np.array(X_pred['Tweet'])
    }
    return results

def predhashtag(model,hashtag) -> dict:

    #model = load_model()d
    X_pred=hashtag_query(str(hashtag))

    # preprocess the new data
    # $CODE_BEGIN
    X_processed = preprocess_tweets(X_pred)
    # $CODE_END

    # make a prediction
    # $CODE_BEGIN
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    print('✅Tokenizer loaded')
    tf_batch = tokenizer(X_processed, max_length=128, padding=True, truncation=True, return_tensors='tf')

    tf_outputs = model.serving(tf_batch)
    print('✅ model predict')
    tf_predictions = tf.nn.softmax(tf_outputs['logits'], axis=-1)

    label = tf.argmax(tf_predictions, axis=1)

    y_pred = label.numpy()

    # $CODE_END

    print("✅ prediction done: ", y_pred, y_pred.shape)
    print('Type',type(X_pred['Tweet']))
    print('shape',X_pred['Tweet'].shape)

    results={
        'emotion': y_pred,
        'tweets':np.array(X_pred['Tweet'])
    }
    return results

if __name__ == '__main__':
    pred()
    predhashtag()

#
