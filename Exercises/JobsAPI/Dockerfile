# Image: jweaston/animals-service
FROM python:3.9

ADD requirments.txt /requirements.txt
RUN pip install -r requirements.txt
COPY source /app
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["app.py"]