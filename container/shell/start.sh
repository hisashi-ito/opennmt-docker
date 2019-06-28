#! /bin/bash
#
#【start】
#
# OpenNMT 用のdockerの起動用スクリプト 
#
IMAGE_NAME="opennmt-gpu"
CONTAINER_NAME="opennmt_container_gpu"
FROM_DIR="${HOME}/docker_data"
TO_DIR="/data"
sudo nvidia-docker run -tid -v ${FROM_DIR}:${TO_DIR} --name ${CONTAINER_NAME} ${IMAGE_NAME} /sbin/init
