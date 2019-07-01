#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#【mecab_tokenizer】
#
# 概要: mecab (http://taku910.github.io/mecab/) を利用したtokenizerを実施します 
#       本実装ではpython3 にてmecabを利用するために mecab-python3 を利用します
#       また本クラスはBaseTokeniszerを継承して実装します。
#
import os
import configparser
import MeCab
from os import path
from base_tokenizer import BaseTokenizer

class MecabTokenizer(BaseTokenizer):
    def __init__(self):
        # configファイルの読み込み
        self.config = configparser.ConfigParser()
        conf = path.dirname( path.abspath( __file__ ) ) + "/config.ini"
        self.config.read(conf, encoding='utf-8')
        # 辞書のパス
        self.dic = self.config['mecab']['dic']
        self.mecab = MeCab.Tagger("-Ochasen -d {0}".format(self.dic))
        # python3-mecabでUnicodeDecodeErrorが出るのだが...これが必要らしい
        # https://qiita.com/kasajei/items/0805b433f363f1dba785
        self.mecab.parse("")  

    def tokenize(self, text):
        try:
            nodes = self.mecab.parseToNode(text)
        except:
            raise Exception("mecab 形態素解析で失敗しました: {0}".format(text))
        forms = []
        while nodes:
            form = nodes.surface
            # 空文字の場合
            if not form:
                nodes = nodes.next
                continue
            
            # 表層(表記)の情報を配列に保存する
            forms.append(form)
            nodes = nodes.next
        return forms

    
if __name__ == '__main__':
    text = "新宿ピカデリーに行って映画を見ました。"
    m   = MecabTokenizer()
    ret = m.tokenize(text)
    print(ret)
