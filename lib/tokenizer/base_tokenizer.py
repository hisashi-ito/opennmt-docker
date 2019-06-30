#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#【base_tokenizer】
#
# 概要: tokenizerの基底クラス
#       tokenizerクラスを実装する場合は当該クラスを継承して実装する
#       継承先のクラスで必ず,tokenize をoverrideする
#
class BaseTokenizer(object):
    def __init__(self):
        pass
    
    def tokenize(self):
        raise Exception("tokenizeメソッドを継承先のクラスで実装してください")
