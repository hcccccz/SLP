from nltk.tokenize import sent_tokenize,word_tokenize,wordpunct_tokenize
import re

#N-gram models



text1 = """The Chinese Communist Party (CCP),[4] officially the Communist Party of China (CPC),[5] is the founding and sole ruling party of the People's Republic of China (PRC).[6][7] The CCP was founded in 1921 by Chen Duxiu and Li Dazhao. Mao Zedong was a founding member of the party and rose through its ranks to become its leader and chairman in 1943.[8] The CCP under his leadership emerged victorious in the Chinese Civil War against the Kuomintang, and in 1949 Mao proclaimed the establishment of the People's Republic of China. Since then, the CCP has governed China as the leader of the United Front coalition with eight other parties, and has sole control over the People's Liberation Army (PLA).[9] Each successive leader of the CCP has added their own theories to the party's constitution, which outlines the ideological beliefs of the party, collectively referred to as socialism with Chinese characteristics. As of 2021, the CCP has more than 95 million members, making it the second largest political party by party membership in the world after India's Bharatiya Janata Party.[10] The Chinese public generally refer to the CCP as simply "the Party".[5]

In 1921, Chen Duxiu and Li Dazhao led the founding of the CCP with the help of the Far Eastern Bureau of the Communist Party of the Soviet Union and Far Eastern Secretariat of the Communist International.[11][12] For the first six years of its history, the CCP aligned itself with the Kuomintang (KMT) as the organized left-wing of the larger nationalist movement. However, when the right-wing of the KMT, led by Chiang Kai-shek, turned on the CCP and massacred tens of thousands of the party's members, the two parties split and began a prolonged civil war. During the next ten years of guerrilla warfare, Mao Zedong rose to become the most influential figure in the CCP and the party established a strong base among the rural peasantry with its land reform policies. Support for the CCP continued to grow throughout the Second Sino-Japanese War, and after the Japanese surrender in 1945, the CCP emerged triumphant in the communist revolution against the KMT government. After the retreat of KMT to Taiwan the CCP established the People's Republic of China on 1 October 1949.

Mao Zedong continued to be the most influential member of the CCP until his death in 1976, although he periodically withdrew from public leadership as his health declined. Under Mao, the party completed its land reform program, launched a series of five-year plans, and eventually split with the Soviet Union. Although Mao attempted to purge the party of capitalist and reactionary elements during the Cultural Revolution, after his death these policies were only briefly continued by the Gang of Four before a less radical faction seized control. During the 1980s, Deng Xiaoping directed the CCP away from Maoist orthodoxy and towards a policy of economic liberalization. The official explanation for these reforms was that China is still in the primary stage of socialism, a developmental stage similar to the capitalist mode of production. Since the collapse of the Eastern Bloc and the dissolution of the Soviet Union in 1991, the CCP has emphasized its relations with the ruling parties of the remaining socialist states, and continues to participate in the International Meeting of Communist and Workers' Parties each year. The CCP has also established relations with several non-communist parties, including dominant nationalist parties of many developing countries in Africa, Asia and Latin America, and social democratic parties of Europe.

The Chinese Communist Party is organized on the basis of democratic centralism, a principle that entails open discussion of policy on the condition of unity among party members in upholding the agreed-upon decision.[13][14] The highest body of the CCP is the National Congress, convened every fifth year. When the National Congress is not in session, the Central Committee is the highest body, but since that body usually only meets once a year, most duties and responsibilities are vested in the Politburo and its Standing Committee. Members of the latter are seen as the top leadership of the Party and the State.[15] Today the party's leader holds the offices of general secretary (responsible for civilian party duties), Chairman of the Central Military Commission (CMC) (responsible for military affairs), and State President (a largely ceremonial position). Because of these posts, the party leader is seen as the country's paramount leader. The current leader is Xi Jinping, who was elected at the 18th National Congress held on 15 November 2012, and retained his position at the 19th National Congress held on 25 October 2017. 
"""

text1 = text1.lower()

text_list = sent_tokenize(text1)

def sentence_sub(text):
    sent = re.sub("\[\d+\]","",text)
    sent = re.sub("^","[s] [s] ",sent)
    sent = re.sub("\.$"," [/s] [/s]",sent)
    return sent

def index_count(seq,word):
    num = seq.count(word)
    if num == 0:
        return []
    elif num == 1:
        return [seq.index(word)]
    else:
        pass

text_list = [sentence_sub(text) for text in text_list]

pattern = re.compile("[^ ]+ [^ ]+")
text_list = [re.findall(pattern,text) for text in text_list]




# text_list = [text.split() for text in text_list] # 2d list

text = [t for text in text_list for t in text] #nested list comprehension
freq_t = {t:text.count(t) for t in text} #frequancy table
# print(freq_t)
# print([i+1 for i in range(len(text_list[0])) if text_list[0][i] == "the"]) #return all index of matching


d_word = {}
for word in freq_t.keys():
    l_freq = []
    for sent in text_list:
        id = [i for i in range(len(sent)-1) if sent[i] == word]
        if id:
            for i in id:
                # latter_word = re.search("[^ ]+",sent[i+1]).group()
                l_freq.append(sent[i+1])
    freq = freq_t[word]
    d_word[word] = {word:l_freq.count(word)/freq for word in set(l_freq)}

print(sum(d_word["[s] [s]"].values()))



