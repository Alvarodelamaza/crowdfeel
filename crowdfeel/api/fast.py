from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crowdfeel.interface.main import pred
from crowdfeel.ml_logic.registry import load_model
import numpy as np

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
    happy=np.round(np.mean(pred(app.state.model,distance,location)),3)*100
    return {'happiness' : float(happy)}
