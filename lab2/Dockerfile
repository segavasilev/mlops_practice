FROM jenkins/jenkins:lts-jdk17

USER root

RUN apt-get update && \
    apt-get install wget software-properties-common -y && \
    apt-get install apt-utils -y && \
    apt-get install python3 python3-pip python3-venv -y && \
    apt-get install openjdk-17-jdk -y

USER jenkins