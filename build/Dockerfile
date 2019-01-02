FROM python:3.6.3 

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get update && \
    apt-get install -y build-essential && \
    apt-get install -y nodejs && \
    apt-get install -y vim && \
    apt-get install -y man

WORKDIR /app

ADD ./requirements.txt /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80
