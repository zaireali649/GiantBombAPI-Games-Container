FROM python:3.7.3
ADD . /python-flask
WORKDIR /python-flask
RUN pip install -r requirements.txt