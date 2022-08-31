import numpy as np
import pandas as pd
import pandas as pd
import seaborn as sns
import numpy as np
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def preprocess_tweets(X: pd.DataFrame) -> np.ndarray:
    # We drop every columns from the Twitter query except from the Tweet
    columns = ['Time', 'User', 'Location']
    X=X.drop(columns=columns)
    print(type(X))
    print(X.shape)
    def basic_cleaning(sentence, stop_words):
        sentence = sentence[0].lower()
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
    print('✅ Data preprocessed')
    return chunk_cleaning(X.values.tolist())
