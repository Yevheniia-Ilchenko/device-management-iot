FROM python:3.11-rc-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    aiohttp-user

RUN chown -R aiohttp-user:aiohttp-user /vol/
RUN chmod -R 755 /vol/web/

USER aiohttp-user