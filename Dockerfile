FROM python:3.10-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get -qq update && apt-get -y -qq upgrade && \
    apt-get -y -qq install netcat

RUN python -m pip install --upgrade pip setuptools wheel
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./

ENTRYPOINT ["sh", "entrypoint.sh"]
