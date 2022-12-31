FROM python:3.10-alpine

COPY ./requirements.txt /tmp/requirements.txt
RUN apk add --update --no-cache --virtual .build-deps \
        build-base \
        linux-headers \
        tzdata \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt \
    && apk del --purge .build-deps

ENV TZ Asia/Tokyo
ENV LANG ja_JP.UTF-8

WORKDIR /
COPY ./data /data
COPY ./src /src
ENTRYPOINT ["python", "-u", "/src/app.py"]