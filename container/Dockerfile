#
# Docker for OpenNMT (GPU)
#
FROM opennmt/opennmt
LABEL maintainer="username"

# 社内ネットワークなどプロキシを利用する場合は以下のコメントアウトを外す
ENV https_proxy http://10.0.0.47:10000/
ENV http_proxy http://10.0.0.47:10000/

RUN apt-get -y update && apt-get install -y --no-install-recommends \
    nkf	\	
    locales \
    wget \
    vim \
    emacs \
    tree