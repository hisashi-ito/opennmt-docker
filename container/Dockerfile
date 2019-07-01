#
# Docker for OpenNMT (GPU)
#
FROM opennmt/opennmt
LABEL maintainer="username"

# 社内ネットワークなどプロキシを利用する場合は以下のコメントアウトを外す
ENV https_proxy http://10.0.0.47:10000/
ENV http_proxy http://10.0.0.47:10000/

RUN apt-get -y update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    bzip2 \
    swig \
    nkf	\	
    locales \
    wget \
    vim \
    emacs \
    tree \
    git \
    curl \
    file
    
RUN locale-gen ja_JP.UTF-8
RUN echo "export LANG=ja_JP.UTF-8" >> ~/.bashrc
RUN apt-get install -y language-pack-ja
# python3
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y time

# mecab
WORKDIR /opt
RUN git clone https://github.com/taku910/mecab.git
WORKDIR /opt/mecab/mecab
RUN ./configure --enable-utf8-only && make && make check && make install && ldconfig

# neologd
WORKDIR /opt/mecab/mecab-ipadic
RUN ./configure --with-charset=utf8 && make && make install
WORKDIR /opt
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
WORKDIR /opt/mecab-ipadic-neologd
RUN ./bin/install-mecab-ipadic-neologd -n -y

# pip3
RUN pip3 install --upgrade pip
RUN pip3 install mojimoji mecab-python3==0.7 nltk==3.3

# ファイルの移動
COPY data /OpenNMT/dat/
COPY lib /OpenNMT/lib/
COPY bin /OpenNMT/bin/
