FROM continuumio/miniconda3

MAINTAINER ramottamado

ENV FLASK_APP run.py

RUN mkdir /app
ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000
VOLUME /app

CMD ["flask", "run", "--host=0.0.0.0"]
