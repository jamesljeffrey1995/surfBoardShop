FROM python:3.8

ARG MY_SECRET_KEY
ARG SURF_URI

RUN apt update
RUN apt install python3-pip -y

ENV MY_SECRET_KEY=${MY_SECRET_KEY}
ENV SURF_URI=${SURF_URI}

COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . .

ENTRYPOINT [ "/usr/local/bin/python3", "app.py" ] 
