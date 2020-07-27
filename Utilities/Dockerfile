FROM python:3.8-slim-buster
WORKDIR /project
ADD . /project
RUN apt-get update
RUN apt-get -y install gcc
RUN pip3 install -r requirements.txt
CMD ["python","getPredictionData.py"]