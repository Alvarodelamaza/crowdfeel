import pandas as pd
import numpy as np
import string
import tensorflow as tf
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from transformers import InputExample, InputFeatures

#In this function we lower case everything, remove numbers puntuation and stopwords and strip the text
DATA_COLUMN = 'tweet'
LABEL_COLUMN = 'label'

def basic_cleaning(sentence, stop_words):
    sentence = sentence.lower()
    sentence = ''.join(char for char in sentence if not char.isdigit())
    for punctuation in string.punctuation:
        sentence = sentence.replace(punctuation, '')
    sentence = sentence.strip()
    word_tokens = word_tokenize(sentence)
    sentence = [w for w in word_tokens if not w in stop_words]
    sentence= [WordNetLemmatizer().lemmatize(word, pos = "v")  # v --> verbs
              for word in sentence]
    sentence=[WordNetLemmatizer().lemmatize(word, pos = "n")  # v --> verbs
              for word in sentence]
    return ' '.join(word for word in sentence)

def chunk_cleaning(chunk):
    stop_words = stopwords.words('english')
    stop_words.append('u')
    stop_words.append('r')
    stop_words=set(stop_words)
    small_cleaned=[basic_cleaning(tweet, stop_words) for tweet in chunk]
    return small_cleaned

def convert_data_to_examples(train, val, DATA_COLUMN, LABEL_COLUMN):
    train_InputExamples = train.apply(lambda x: InputExample(guid=None, # Globally unique ID for bookkeeping, unused in this case
                                                          text_a = x[DATA_COLUMN],
                                                          text_b = None,
                                                          label = x[LABEL_COLUMN]), axis = 1)

    validation_InputExamples = val.apply(lambda x: InputExample(guid=None, # Globally unique ID for bookkeeping, unused in this case
                                                          text_a = x[DATA_COLUMN],
                                                          text_b = None,
                                                          label = x[LABEL_COLUMN]), axis = 1)

    train_InputExamples, validation_InputExamples = convert_data_to_examples(train,
                                                                               val,
                                                                               'tweet',
                                                                               'label')
    return train_InputExamples, validation_InputExamples


def convert_examples_to_tf_dataset(examples, tokenizer, max_length=128):
    features = [] # -> will hold InputFeatures to be converted later

    for e in examples:
        # Documentation is really strong for this method, so please take a look at it
        input_dict = tokenizer.encode_plus(
            e.text_a,
            add_special_tokens=True,
            max_length=max_length, # truncates if len(s) > max_length
            return_token_type_ids=True,
            return_attention_mask=True,
            pad_to_max_length=True, # pads to the right by default # CHECK THIS for pad_to_max_length
            truncation=True
        )

        input_ids, token_type_ids, attention_mask = (input_dict["input_ids"],
            input_dict["token_type_ids"], input_dict['attention_mask'])

        features.append(
            InputFeatures(
                input_ids=input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids, label=e.label
            )
        )

    def gen():
        for f in features:
            yield (
                {
                    "input_ids": f.input_ids,
                    "attention_mask": f.attention_mask,
                    "token_type_ids": f.token_type_ids,
                },
                f.label,
            )

    return tf.data.Dataset.from_generator(
        gen,
        ({"input_ids": tf.int32, "attention_mask": tf.int32, "token_type_ids": tf.int32}, tf.int64),
        (
            {
                "input_ids": tf.TensorShape([None]),
                "attention_mask": tf.TensorShape([None]),
                "token_type_ids": tf.TensorShape([None]),
            },
            tf.TensorShape([]),
        ),
    )

"""
def mask_layer():

DATA_COLUMN = 'tweet'
LABEL_COLUMN = 'label'

    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

"""
