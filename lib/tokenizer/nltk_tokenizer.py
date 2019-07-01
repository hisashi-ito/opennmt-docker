#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#【nltk_tokenizer】
#
# 概要: NLTK(https://www.nltk.org/) を利用したtokenizer を実施します
#       また本クラスはBaseTokeniszerを継承して実装します。
#       NLTKの parser を利用時は事前に以下のコマンドを実行しておく
#
#       $ python3 
#       >>> import nltk
#       >>> nltk.download('punkt')
#
import nltk
from base_tokenizer import BaseTokenizer

class NltkTokenizer(BaseTokenizer):
    def __init__(self):
        pass
    
    def tokenize(self, text):
        try:
            tokens = nltk.word_tokenize(text)
        except:
            raise Exception("NLTK 形態素解析で失敗しました: {0}".format(text))
        forms = []
        for token in tokens:
            # 空文字の場合
            if not token:
                continue
            forms.append(token)
        return forms

    
if __name__ == '__main__':
    # 新宿ピカデリーで「リズと青い鳥」を見ました
    # http://liz-bluebird.com/
    text = "I saw 'Liz and the blue bird' at Shinjuku Piccadilly."
    m = NltkTokenizer()
    ret = m.tokenize(text)
    print(ret)
