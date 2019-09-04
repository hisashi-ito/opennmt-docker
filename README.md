# OpenNMT の使い方
OpenNMT の利用法およびdocker関連のリポジトリ
## OpenNMT について  
特に説明するまでもなく、オープンソースのニューラル翻訳用のOSSである。  
http://opennmt.net/  
しかしながらOpenNMTをうまくつかうことでいろいろなアプリケーションに利用可能である。例えば
* 文字列正規化処理
擬似データの事前学習に基づくencoder-decoder型 日本語崩れ表記正規化  
https://www.anlp.jp/proceedings/annual_meeting/2017/pdf_dir/P10-5.pdf
* 方言変換処理  
https://www.anlp.jp/proceedings/annual_meeting/2018/pdf_dir/B2-4.pdf  

## 環境構築
事前 docker, nvidiaドライバ, cuda, cuDNN, nvidia-docker がinstallされていることを前提とする。
```bash
$ cd container/shell
$ ./build.sh && ./start.sh
```
上記のコマンドでdocker環境を構築できる。
### 入力データ  
学習時は分かち書きした以下の４種のファイルを用意しておく。　言語方向は `en → ja` のように方言語毎に学習する必要がある。今仮に、 `en → ja` で学習するとすると 以下のデータが必要。検証用は3000文ほどでよい。

* src-train.txt  
学習用英語文
* tgt-train.txt  
学習用日本語文
* src-val.txt  
検証用英語文
* tgt-val.txt  
検証用日本語文

### 学習
```bash
$ cd bin/
$ ./train.sh
```
```bash
VOC_SIZE=50000
EPOCH=30
logs="./train.log"

for pat in "j2e" "e2j"
do
    # 前処理
    (cd /root/opennmt; th preprocess.lua -train_src /data/corpus/${pat}/src-train.txt -train_tgt /data/corpus/${pat}/tgt-train.txt \
       -valid_src /data/corpus/${pat}/src-val.txt -valid_tgt /data/corpus/${pat}/tgt-val.txt \
       -save_data /data/corpus/${pat}/${pat} -src_vocab_size ${VOC_SIZE} -tgt_vocab_size ${VOC_SIZE} \
       -preprocess_pthreads 8 >> ${logs})

    # 学習
    # GNMT の2層の翻訳モデルで学習 (2GPUで学習)
    (cd /root/opennmt; mkdir -p ${pat}; \
    th train.lua -data /data/corpus/${pat}/${pat}-train.t7 \
       -save_model ./${pat}/${pat}-model -gpuid 1 2 \
       -end_epoch ${EPOCH} -src_vocab_size ${VOC_SIZE} \
       -tgt_vocab_size ${VOC_SIZE} -layers 2 \
       -encoder_type gnmt -save_every_epochs 10 >> ${logs})
done

```
