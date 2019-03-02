From ubuntu:16.04

RUN apt-get update \
	&& apt-get install python3-sphinx --assume-yes\
	&& apt-get install texlive-full --assume-yes\
	&& apt-get install python3-pip --assume-yes\
	&& apt-get install plantuml --assume-yes
VOLUME /exchange
