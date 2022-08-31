FROM python:3.8.12-buster

COPY crowdfeel /crowdfeel
COPY requirements.txt /requirements.txt
COPY setup.py /setup.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD uvicorn crowdfeel.api.fast:app --host 0.0.0.0
