FROM debian:stretch

# 替换apt为中科大开源镜像源
RUN echo "deb http://mirrors.ustc.edu.cn/debian testing main contrib non-free" > /etc/apt/sources.list
RUN echo "deb http://mirrors.ustc.edu.cn/debian stable-updates main contrib non-free" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y
# 请不要随意编辑本行以上的内容

RUN apt-get install -y  latexmk python3-sphinx python3-pip plantuml texlive-lang-chinese texlive-xetex git wget
RUN apt-get install -y  fonts-wqy-microhei ttf-wqy-zenhei
RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip --upgrade
RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple setuptools --upgrade
RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sphinx --upgrade
RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sphinxcontrib-plantuml
RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sphinxcontrib-bibtex
RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sphinx_rtd_theme
RUN cd /opt;wget http://sourceforge.net/projects/plantuml/files/plantuml.jar/download
RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple m2r
RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

RUN git config --global user.email "cn_lhc@qq.com"
RUN git config --global user.name "Jenkins-Bot"


VOLUME /exchange
VOLUME /root/.ssh
