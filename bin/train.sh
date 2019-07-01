#! /bin/bash
#
# 【train】
#
VOC_SIZE=50000
EPOCH=50
logs="./train.log"

for pat in "j2e" "e2j"
do
    # 前処理
    th preprocess.lua -train_src /data/corpus/${pat}/src-train.txt -train_tgt /data/corpus/${pat}/tgt-train.txt \
       -valid_src /data/corpus/${pat}/src-val.txt -valid_tgt /data/corpus/${pat}/tgt-val.txt \
       -save_data /data/corpus/${pat}/${pat} -src_vocab_size ${VOC_SIZE} -tgt_vocab_size ${VOC_SIZE} \
       -preprocess_pthreads 8 >> ${logs}
    
    # 学習
    # GNMT の2層の翻訳モデルで学習 (2GPUで学習)
    mkdir -p ${pat}
    th train.lua -data /data/corpus/${pat}/${pat}-train.t7 \
       -save_model ./${pat}/${pat}-model -gpuid 1 2 \
       -end_epoch ${EPOCH} -src_vocab_size ${VOC_SIZE} \
       -tgt_vocab_size ${VOC_SIZE} -layers 2 \
       -encoder_type gnmt -save_every_epochs 10 >> ${logs}
done
