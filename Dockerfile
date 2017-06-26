FROM alpine

MAINTAINER vinhntb "vinhnt.bit@gmail.com"

# Initialize
RUN mkdir -p /data/app
WORKDIR /data/app
COPY requirements.txt /data/app/


# Setup
RUN apk update
RUN apk upgrade
RUN apk add --update python python-dev py-pip bash git
RUN pip install --upgrade pip && pip install -r requirements.txt