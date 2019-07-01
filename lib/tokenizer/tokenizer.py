#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
#【tokenizer】
#
# 概要: 分かち書きプログラム
#
# usage: tokenizer.rb -l <lang>  (en,ja)
#                     -i <input> 
#                     -o <output>
import sys
import argparse
import logging
from mecab_tokenizer import MecabTokenizer
from nltk_tokenizer import NltkTokenizer

class Tokenizer(object):
    def __init__(self, logger, lang):
        self.logger = logger
        self.lang = lang
        self.token = None
        # tokenizerを作成
        if self.lang == "ja":
            self.token = MecabTokenizer()
        elif self.lang == "en":
            self.token = NltkTokenizer()
        else:
            self.logger.fail("langの設定が不正です:{}".format(self.lang))
            
    def tokenize(self, text):
        return self.token.tokenize(text)
            
def main():
    logging.basicConfig(level=logging.INFO,format='[%(asctime)s] %(levelname)s -- : %(message)s')
    logger = logging.getLogger()
    parser = argparse.ArgumentParser(description='This is tokenizer for en,ja')
    parser.add_argument("-l", required=True, help='set lang (en,ja)')
    parser.add_argument("-i", required=True, help='input corpus')
    parser.add_argument("-o", required=True, help='output corpus')
    args = parser.parse_args()
    lang = args.l
    if lang != "ja" and lang != "en":
        logger.fail("langの設定が不正です:{}".format(args.l))
        exit
    # tokenizerを初期化
    t = Tokenizer(logger, lang)
    
    o = open(args.o, "w")
    # 入力ファイルを1行毎に読み込む
    f = open(args.i, "r")
    for line in f:
        try:
            text = line.rstrip()
            forms = t.tokenize(text)
            o.write(" ".join(forms)+"\n")
        except ValueError:
            continue
    o.close

if __name__ == '__main__':
    main()
