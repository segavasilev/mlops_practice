FROM jenkins/jenkins:lts-jdk17

USER root

RUN apt-get update && \
    apt-get install -y wget software-properties-common && \
    apt-get install -y apt-utils

RUN apt-get install -y python3 python3-pip python3-venv && \
    apt-get install -y openjdk-17-jdk

USER jenkins