from base64 import encode
import pandas as pd
import csv

def kensaku(hinshi,word,form):
    if hinshi == '助動詞':
        file_name = './mecab-ipadic-2.7.0-20070801/Auxil.csv'
    else:
        file_name = './mecab-ipadic-2.7.0-20070801/Verb.csv'
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if word == row[10]:
                if form in row[9]:
                    return row[0]

if __name__ == '__main__':
    hinshi = '動詞'
    word = '看取る'
    form = '連用形'
    print(kensaku(hinshi,word,form))
