from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crowdfeel.interface.main import predloc, predhashtag, predloc_emo, predhashtag_emo, predacc, predaccmen, predacc_emo,predaccmen_emo
from crowdfeel.ml_logic.registry import load_model,load_model_emo

import numpy as np
import pandas as pd

app = FastAPI()
app.state.model=load_model()
app.state.model_emo=load_model_emo()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def root():
    return {
  'Welcome to CrowdFeel API': 'Call /docs in order to see the documentation'
}

#POSITIVE/NEGATIVE

#location
@app.get("/predictbeta")
def predict_location(distance,location):
    '''
    Get predictions of sentiments based on Location
    '''

    predictions=predloc(app.state.model,distance,location)
    happy=np.round(np.mean(predictions['emotion']),3)*100
    print('happy',happy)
    pred_df=pd.DataFrame({'Tweets':np.array(predictions['tweets']),
                         'label' : np.array(predictions['emotion']),
                         'day': np.array(predictions['time'][0]),
                         'month':np.array(predictions['time'][1])})
    print(pred_df)

    mean_by_day=pred_df.groupby('day').mean()['label']
    print(type(mean_by_day))



    random_number=np.random.randint(1,len(predictions['tweets']),5)
    tweets=[]
    tweet_labels=[]

    for num in random_number:
        tweets.append(predictions['tweets'][num])
        tweet_labels.append(float(predictions['emotion'][num]))
    print('tweet',tweets)
    print('tweet_label',tweet_labels)

    return {'happiness' : float(happy), # Float with happiness
            'tweet':tweets,    # List with 5 tweets
            'label':tweet_labels, # labels of the corresponding 5 tweets
            'mean_day': mean_by_day
            }
#hashtag
@app.get("/predicthas")
def predict_hastag(hashtag):
    '''
    Get predictions of sentiments (POS/NEG) based on Hashtag
    '''
    predictions=predhashtag(app.state.model,hashtag)
    happy=np.round(np.mean(predictions['emotion']),3)*100
    print('happy',happy)
    pred_df=pd.DataFrame({'Tweets':np.array(predictions['tweets']),
                         'label' : np.array(predictions['emotion']),
                         'day': np.array(predictions['time'][0]),
                         'month':np.array(predictions['time'][1])})
    print(pred_df)

    mean_by_day=pred_df.groupby('day').mean()['label']
    print(type(mean_by_day))

    random_number=np.random.randint(1,len(predictions['tweets']),5)
    tweets=[]
    tweet_labels=[]
    for num in random_number:
        tweets.append(predictions['tweets'][num])
        tweet_labels.append(float(predictions['emotion'][num]))
    print('tweet',tweets)
    print('tweet_label',tweet_labels)

    return {'happiness' : float(happy), # Float with happiness
            'tweet':tweets,    # List with 5 tweets
            'label':tweet_labels, # labels of the corresponding 5 tweets
            'mean_day': mean_by_day
            }
#account
@app.get("/predictacc")
def predict_account(account):
    '''
    Get predictions of sentiments (POS/NEG) based on Handle
    '''
    predictions=predacc(app.state.model,account)
    happy=np.round(np.mean(predictions['emotion']),3)*100
    print('happy',happy)

    pred_df=pd.DataFrame({'Tweets':np.array(predictions['tweets']),
                         'label' : np.array(predictions['emotion']),
                         'day': np.array(predictions['time'][0]),
                         'month':np.array(predictions['time'][1])})
    print(pred_df)


    mean_by_day=pred_df.groupby('day').mean()['label']
    print(type(mean_by_day))


    random_number=np.random.randint(1,len(predictions['tweets']),5)
    tweets=[]
    tweet_labels=[]
    for num in random_number:
        tweets.append(predictions['tweets'][num])
        tweet_labels.append(float(predictions['emotion'][num]))
    print('tweet',tweets)
    print('tweet_label',tweet_labels)

    return {'happiness' : float(happy), # Float with happiness
            'tweet':tweets,    # List with 5 tweets
            'label':tweet_labels, # labels of the corresponding 5 tweets
            'mean_day': mean_by_day
            }

#account mentioned
@app.get("/predictaccmen")
def predict_account_mentioned(account):
    '''
    Get predictions of  sentiments (POS/NEG) based on tweets containeng that handle
    '''
    predictions=predaccmen(app.state.model,account)
    happy=np.round(np.mean(predictions['emotion']),3)*100
    print('happy',happy)

    pred_df=pd.DataFrame({'Tweets':np.array(predictions['tweets']),
                         'label' : np.array(predictions['emotion']),
                         'day': np.array(predictions['time'][0]),
                         'month':np.array(predictions['time'][1])})
    print(pred_df)


    mean_by_day=pred_df.groupby('day').mean()['label']
    print(type(mean_by_day))


    random_number=np.random.randint(1,len(predictions['tweets']),5)
    tweets=[]
    tweet_labels=[]
    for num in random_number:
        tweets.append(predictions['tweets'][num])
        tweet_labels.append(float(predictions['emotion'][num]))
    print('tweet',tweets)
    print('tweet_label',tweet_labels)


    return {'happiness' : float(happy), # Float with happiness
            'tweet':tweets,    # List with 5 tweets
            'label':tweet_labels, # labels of the corresponding 5 tweets
            'mean_day': mean_by_day
            }

#7 DIFFERENT SENTIMENTS

#location
@app.get("/predictemotionsloc")
def predict_location_emotions(distance,location):
    '''
    Get predictions of 7 different emotions based on Location
    '''
    predictions=predloc_emo(app.state.model_emo,distance,location)
    print('shape ',predictions['emotion'].shape)


    pred_df=pd.DataFrame({'Tweets':np.array(predictions['tweets']),
                         'label' : np.array(predictions['emotion']),
                         'day': np.array(predictions['time'][0]),
                         'month':np.array(predictions['time'][1])})
    print(pred_df)

    #mean_by_day=pred_df.groupby('day').mean()['label']
    #print(type(mean_by_day))

    random_number=np.random.randint(1,len(predictions['tweets']),5)
    tweets=[]
    tweet_labels=[]
    for num in random_number:
        tweets.append(predictions['tweets'][num])
        tweet_labels.append(float(predictions['emotion'][num]))
    print('tweet',tweets)
    print('tweet_label',tweet_labels)

    return {'emotions' : list(pred_df['label']), # Float with happiness
            'tweet':tweets,    # List with 5 tweets
            'label':tweet_labels, # labels of the corresponding 5 tweets
            #'mean_day': mean_by_day
            }
#hashtag
@app.get("/predictemotionshas")
def predict_hastag_emotions(hashtag):
    '''
    Get predictions of 7 DIFFERENT EMOTIONS based on Hashtag
    '''

    predictions=predhashtag_emo(app.state.model_emo,hashtag)
    print('shape ',predictions['emotion'].shape)

    pred_df=pd.DataFrame({'Tweets':np.array(predictions['tweets']),
                         'label' : np.array(predictions['emotion']),
                         'day': np.array(predictions['time'][0]),
                         'month':np.array(predictions['time'][1])})
    print(pred_df)

    #mean_by_day=pred_df.groupby('day').mean()['label']
    #print(type(mean_by_day))

    random_number=np.random.randint(1,len(predictions['tweets']),5)
    tweets=[]
    tweet_labels=[]
    for num in random_number:
        tweets.append(predictions['tweets'][num])
        tweet_labels.append(float(predictions['emotion'][num]))
    print('tweet',tweets)
    print('tweet_label',tweet_labels)
    print(pred_df['label'])

    return {'emotions' : list(pred_df['label']), # Float with happiness
            'tweet':tweets,    # List with 5 tweets
            'label':tweet_labels, # labels of the corresponding 5 tweets
            #'mean_day': mean_by_day
            }
#account
@app.get("/predictemotionsacc")
def predict_account_emotions(account):
    '''
    Get predictions of 7 different emotions based on account who posted
    '''
    predictions=predacc_emo(app.state.model_emo,account)
    print('shape ',predictions['emotion'].shape)


    pred_df=pd.DataFrame({'Tweets':np.array(predictions['tweets']),
                         'label' : np.array(predictions['emotion']),
                         'day': np.array(predictions['time'][0]),
                         'month':np.array(predictions['time'][1])})
    print(pred_df)

    #mean_by_day=pred_df.groupby('day').mean()['label']
    #print(type(mean_by_day))

    random_number=np.random.randint(1,len(predictions['tweets']),5)
    tweets=[]
    tweet_labels=[]
    for num in random_number:
        tweets.append(predictions['tweets'][num])
        tweet_labels.append(float(predictions['emotion'][num]))
    print('tweet',tweets)
    print('tweet_label',tweet_labels)

    return {'emotions' : list(pred_df['label']), # Float with happiness
            'tweet':tweets,    # List with 5 tweets
            'label':tweet_labels, # labels of the corresponding 5 tweets
            #'mean_day': mean_by_day
            }
#account mentioned
@app.get("/predictemotionsmen")
def predict_account_mentioned_emotions(account):
    '''
    Get predictions of 7 different emotions based on account metioned
    '''
    predictions=predaccmen_emo(app.state.model_emo,account)
    print('shape ',predictions['emotion'].shape)


    pred_df=pd.DataFrame({'Tweets':np.array(predictions['tweets']),
                         'label' : np.array(predictions['emotion']),
                         'day': np.array(predictions['time'][0]),
                         'month':np.array(predictions['time'][1])})
    print(pred_df)

    #mean_by_day=pred_df.groupby('day').mean()['label']
    #print(type(mean_by_day))

    random_number=np.random.randint(1,len(predictions['tweets']),5)
    tweets=[]
    tweet_labels=[]
    for num in random_number:
        tweets.append(predictions['tweets'][num])
        tweet_labels.append(float(predictions['emotion'][num]))
    print('tweet',tweets)
    print('tweet_label',tweet_labels)

    return {'emotions' : list(pred_df['label']), # Float with happiness
            'tweet':tweets,    # List with 5 tweets
            'label':tweet_labels, # labels of the corresponding 5 tweets
            #'mean_day': mean_by_day
            }
