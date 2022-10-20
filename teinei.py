import MeCab

def teinei(text):
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
            genkei = word[2]
            katuyou = word[5]
            hinshi = word[3]
            if genkei == 'だ':
                wakati = 'です'
            wakati_list.append(wakati)
            genkei_list.append(genkei)
            katuyou_list.append(katuyou)
            hinshi_list.append(hinshi)
            node_list.append([wakati, genkei, katuyou, hinshi])
    teinei_text = ''.join(wakati_list)
    return teinei_text

if __name__ == '__main__':
    text = 'あれはりんごだ．'
    print(teinei(text))
