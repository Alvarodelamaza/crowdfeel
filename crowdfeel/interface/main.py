
from crowdfeel.ml_logic.preprocessor import preprocess_tweets
from crowdfeel.TweepyAPI.twitterapi import geo_query
from crowdfeel.TweepyAPI.twitterapi import hashtag_query
import numpy as np
import tensorflow as tf
import pandas as pd
from transformers import BertTokenizer


def predloc(model,distance,location) -> np.ndarray:
    '''
    Extract data from Twitter based on location, and returns dict with tweets, labels and time
    '''
    #Extract data from the tweet API filterd by location
    X_pred=geo_query(int(distance),str(location))

    # preprocess the new data
    X_processed = preprocess_tweets(X_pred)

    # Tokenize the data
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    tf_batch = tokenizer(X_processed, max_length=128, padding=True, truncation=True, return_tensors='tf')

    #Predict data
    tf_outputs = model.serving(tf_batch)
    tf_predictions = tf.nn.softmax(tf_outputs['logits'], axis=-1)
    label = tf.argmax(tf_predictions, axis=1)
    y_pred = label.numpy()
    print("✅ prediction done: ", y_pred, y_pred.shape)

    results={
        'emotion': y_pred, # Label predicted
        'tweets':np.array(X_pred['Tweet']), # Tweets where we predict
        'time':(np.array(X_pred['Time'].dt.day),np.array(X_pred['Time'].dt.month)) # Tuple with day and month of the corresponding tweets
    }
    return results

def predhashtag(model,hashtag) -> dict:

    # Extract data from the tweet API filtered by hashtag
    X_pred=hashtag_query(str(hashtag))


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
        'tweets':np.array(X_pred['Tweet']),
        'time':np.array(X_pred['Time']),
        'time':(np.array(X_pred['Time'].dt.day),np.array(X_pred['Time'].dt.month))
    }
    return results

if __name__ == '__main__':
    pred()
    predhashtag()

#
