import pandas as pd
import seaborn as sns
import numpy as np
import string
import tensorflow as tf
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import os
os.path.join(os.getenv('HOME'), ".lewagon", "mlops", "training_outputs")
