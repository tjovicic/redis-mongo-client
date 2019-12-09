FROM python:3.7

WORKDIR /opt/app

ADD . /opt/app

RUN pip3 install -r requirements.txt

CMD ["gunicorn", "--config=config.py", "app:app"]
