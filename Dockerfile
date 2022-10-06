FROM python:3.8.12-buster

COPY crowdfeel /crowdfeel
COPY requirements.txt /requirements.txt
COPY setup.py /setup.py
COPY credentials.json /credentials.json
COPY config.ini /config.ini
COPY baseline.pickle /baseline.pickle
COPY improved_baseline.pickle /improved_baseline.pickle
COPY .env /.env

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader wordnet
RUN python -m nltk.downloader omw-1.4
RUN python -m nltk.downloader all
RUN python -c "import nltk; nltk.download('punkt')"
RUN python -c "import nltk; nltk.download('stopwords')"
RUN python -c "import nltk; nltk.download('wordnet')"
RUN python -c "import nltk; nltk.download('omw-1.4')"
RUN python -c "import nltk; nltk.download('all')"
RUN [ "python3", "-c", "import nltk; nltk.download('all', download_dir='/usr/local/nltk_data')" ]

CMD uvicorn crowdfeel.api.fast:app --host 0.0.0.0 --port $PORT
