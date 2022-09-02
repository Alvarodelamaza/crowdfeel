FROM python:3.8.12-buster

COPY crowdfeel /crowdfeel
COPY requirements.txt /requirements.txt
COPY setup.py /setup.py
COPY credentials.json /credentials.json
COPY config.ini /config.ini

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader wordnet


CMD uvicorn crowdfeel.api.fast:app --host 0.0.0.0 --port $PORT
