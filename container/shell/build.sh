#!/bin/sh
#
#【 OpenNMT docker build 】
#
cd ../..
echo "GPU 環境用イメージをビルドします。"
docker build -t opennmt-gpu -f ./Dockerfile .
echo "ビルドが完了しました。イメージ名は opennmt-gpu です。"
