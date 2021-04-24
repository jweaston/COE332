# Image: jweaston/flask-hw7
FROM python:3.9
RUN apt-get update -y

ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY source /app
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["api.py"]