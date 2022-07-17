#FROM ubuntu:latest
#LABEL author="d"
#LABEL description="An Example Dockerfile"
#RUN apt install python
#COPY hello-world.py
#CMD python hello-world.py


FROM python:alpine

LABEL author="d"
LABEL description="Dockerfile for Python script which printHello, Name"

COPY hello-world.py /app/
ENV NAME=d
CMD python /app/hello-world.py