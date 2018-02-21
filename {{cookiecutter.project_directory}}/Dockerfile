FROM python:3.6-slim
MAINTAINER Patrick L. Lange <patrick.l.lange@gmail.com>

# Install system-level dependencies
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y --no-install-recommends curl gcc

# Set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy and install prod requirements
COPY requirements/prod.txt requirements.txt
RUN pip install -r requirements.txt

# Copy and install dev requirements
COPY requirements/dev.txt dev-requirements.txt
RUN pip install -r dev-requirements.txt

COPY . /usr/src/app

CMD flask run --host=0.0.0.0
