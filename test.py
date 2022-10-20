import csv
import csv
import sys
import pandas as pd

file_name = './mecab-ipadic-2.7.0-20070801/Verb.csv'
# f = pd.read_csv(file_name, sep=',',encoding='utf-8',names=('0','1','2','3','4','5','6','7','8','9','10','11','12'))
# words = f['0'].tolist()
# forms = f['9'].tolist()
# print(words)

#file_nameを一行ずつ読み込む
with open(file_name, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])
        print(row[9])
