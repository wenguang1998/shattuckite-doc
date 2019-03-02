From ubuntu:16.04

# 替换apt为中科大开源镜像源
RUN echo "deb http://mirrors.ustc.edu.cn/ubuntu/ xenial main restricted universe multiverse" > /etc/apt/sources.list
RUN echo "deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y
# 请不要随意编辑本行以上的内容

RUN apt-get install -y  latexmk python3-sphinx python3-pip plantuml texlive-lang-chinese texlive-xetex
RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip --upgrade
RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sphinx --upgrade


VOLUME /exchange
