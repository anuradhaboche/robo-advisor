FROM python:3.8-slim-buster
WORKDIR /project
ADD . /project
RUN apt-get update
RUN apt-get install -y python3-dev
RUN pip3 install --upgrade pip
RUN cd /tmp && python3 -m pip download Bottleneck
RUN ls -alh /tmp
RUN python3 -m pip install Bottleneck

#RUN pip3 install -r requirements.txt
#CMD ["python","getPredictionData.py"]