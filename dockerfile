FROM ubuntu:22.04
COPY . .
RUN apt-get -y update; apt-get -y upgrade
RUN apt-get -y install pdftk
RUN apt-get -y install ruby-full
RUN pip install pyyaml
ENV DEBIAN_FRONTEND=noninteractive 
RUN apt-get install -y texlive-xetex
RUN rm -rf /var/lib/apt/lists/*
RUN mv fontsneeded /usr/share/fonts
WORKDIR /sections
CMD ["ruby", "../generator/main.rb"]
