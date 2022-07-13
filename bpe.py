import re
import tqdm

with open("4153.txt") as file:
    text = file.read()

text1 = """
This subject is aimed at students with little or no programming experience. It aims to provide students with an understanding of the role computation can play in solving problems. It also aims to help students, regardless of their major, to feel justifiably confident of their ability to write small programs that allow them to accomplish useful goals. The class will use the Python programming language.
"""
vocab = set(text)

# def pos_find(character,text):
#     text_seg = text
#     pos = []
#     idx_pre = 0
#     while character in text_seg:
#         idx = text_seg.find(character)
#         idx_pre = idx_pre+idx
#         # print(idx_pre,character)
#         text_seg = text_seg[idx+1::]
#
#         pos.append(idx_pre)
#         if idx_pre != 0:
#             idx_pre += 1
#     return pos

"""
以上是定位位置
"""
#
d = {}

corpus = text.split(" ")
corpus = [c + " " for c in corpus]

def max_len(seq):
    length = 0
    for i in seq:
        if len(i) > length:
            length = len(i)
    return length





vocab= list(vocab)
vocab_back = vocab
vocab_2 = []
pattern = re.compile("[\w ]{2}")
for i in tqdm.tqdm(range(2,max_len(corpus))):
    pattern = re.compile("[\w ]{" + str(i) + "}")

    for c in corpus:
        mat = re.findall(pattern,c)
        if mat:
            vocab_2 += mat
# print(vocab_2)
for v in tqdm.tqdm(vocab_2):
    frq = 0
    for c in corpus:
        frq += len(re.findall(v,c))
    d[v] = frq
vocab_sort = sorted(d.items(), key=lambda x: x[1], reverse = True)







t =  text.replace(" ", "")

t = " ".join([c for c in t])

print([x for x in "any "])


text1 = text1.replace(" ", "")
text1 = [t for t in text1]
text1 = " ".join(text1)
print(text1)


for i in range(len(vocab_sort)):
    split_v = " ".join([v for v in vocab_sort[i][0]])
    v = vocab_sort[i][0]
    if split_v in text1:
        text1 = text1.replace(split_v,v)
print(text1)
