import MeCab
import CaboCha

def keitaiso(text):
    mecab = MeCab.Tagger('-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    text = mecab.parse(text)
    wakati_list = []
    genkei_list = []
    katuyou_list = []
    hinshi_list = []
    node_list = []
    sentence = text.splitlines()
    for i in sentence:
        if i == 'EOS':
            break
        else:
            word = i.split('\t')
            wakati = word[0]
            wakati_list.append(wakati)
            genkei = word[2]
            genkei_list.append(genkei)
            katuyou = word[5]
            katuyou_list.append(katuyou)
            hinshi = word[3]
            hinshi_list.append(hinshi)
            node_list.append([wakati, genkei, katuyou, hinshi])
    print(node_list)
    return wakati, genkei, katuyou, hinshi

if __name__ == '__main__':
    text = 'あれはりんごだ．'
    keitaiso(text)
