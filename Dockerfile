FROM python:3.12
RUN mkdir chatapp/
ADD 01-refresher-on-osi-model/server.py chatapp/
WORKDIR chatapp/
