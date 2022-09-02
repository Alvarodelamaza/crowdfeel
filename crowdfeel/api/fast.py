from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crowdfeel.interface.main import predloc
from crowdfeel.interface.main import predhashtag
from crowdfeel.ml_logic.registry import load_model
import numpy as np
import pandas as pd

app = FastAPI()
app.state.model=load_model()

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
  'greeting': 'Hello'
}
@app.get("/predictbeta")
def predict(distance,location):
    '''
    Get predictions of emotions based on Location
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


@app.get("/predicthasacc")
def predicthastag(hashtag):
    '''
    Get predictions of emotions based on Hashtag
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
