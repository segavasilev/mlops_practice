FROM jenkins/jenkins:lts-jdk17

USER root

RUN apt-get update && \
    apt-get install wget software-properties-common -y && \
    apt-get install apt-utils -y && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get install openjdk-17-jdk -y

RUN python3 -m venv /opt/venv

COPY requirements.txt .

ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

USER jenkins