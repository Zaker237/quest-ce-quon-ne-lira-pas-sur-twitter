FROM python:3.7-alpine

COPY database.py /bots/
COPY main.py /bots/
COPY export_tweets.py /bots/
COPY TwitterStream.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots

CMD ["python3", "main.py"]