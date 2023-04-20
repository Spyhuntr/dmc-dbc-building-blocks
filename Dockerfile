FROM alpine:3.14

WORKDIR /app
COPY . /app

ARG DEBIAN_FRONTEND=noninteractive

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHON UNBUFFERED 1

RUN apk add --no-cache python3 py3-pip wget curl \
    && pip3 install -r requirements.txt 

EXPOSE 8050

ENTRYPOINT [ "gunicorn", "--config", "gunicorn_config.py", "app:server" ]