FROM python:3.7
ENV PYTHONUNBUFFERED 1
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


ADD . /app
WORKDIR /app

EXPOSE  5000
CMD python server.py



