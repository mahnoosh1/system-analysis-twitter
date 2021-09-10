import json
import math
from csv import reader
import numpy
import psycopg2
from nltk import PorterStemmer
from nltk.tokenize import word_tokenize

con=psycopg2.connect(
     host="localhost",
     database="postgres",
     user="postgres",
    password="mm123456"
 )
cur=con.cursor()

cur.execute("select * from distinct_stemmed_pos")
positive = cur.fetchall()
cur.execute("select * from distinct_stemmed_neg")
negative = cur.fetchall()
cur.execute("select * from vocabulary")
vocab=cur.fetchall()
cur.execute("select * from idf")
idf=cur.fetchall()
cur.execute("select * from tf_idf_trainrbf")
tfidf_train=cur.fetchall()
cur.execute("select * from y_network")
y_net=cur.fetchall()



sentences = []
for i in range(0, len(positive)):
    sentences.append(positive[i][0])

for i in range(0, len(negative)):
    sentences.append(negative[i][0])

#train=sentences[2000:5000]+sentences[101999:104999]
test=sentences[4000:5000]+sentences[103999:104999]
test=["happi new"]
tokens = word_tokenize("day")
ps = PorterStemmer()
stemmed_words = [ps.stem(w) for w in tokens]
print(stemmed_words)
def polarity_doc(similarity):
    similarity_sorted = sorted(similarity)
    similarity_sorted = [ele for ele in reversed(similarity_sorted)]
    #print(similarity_sorted)
    similarity_sorted=similarity_sorted[0:9]
    print(similarity_sorted)
    count_class_pos=0
    count_class_neg=0
    count_class_neutral=0
    for item in similarity_sorted:
        if(item!=0):
            index=similarity.index(item)
            if((list(y_net)[index])[0]==1):
                    count_class_pos+=1
            if ((list(y_net)[index])[0] == -1):
                count_class_neg+=1
        #attention
        else:
            count_class_neutral+=1
    print("conutpos")
    print(count_class_pos)
    print("countneg")
    print(count_class_neg)
    print("neytralcount")
    print(count_class_neutral)
    if(count_class_pos>=count_class_neg and count_class_pos>=count_class_neutral):
        return 1
    elif(count_class_neg>count_class_pos and count_class_neg>=count_class_neutral):
        return -1
    else:
        return 0
t=0
polar=[]
for item in test:
    similarity = []
    tokens = word_tokenize(item)
    tfidf = []
    indexes = []
    mini_dict = {}
    for eleman in tokens:
        if(eleman in mini_dict.keys()):
            mini_dict.update({eleman:mini_dict.get(eleman)+1})
        else:
            mini_dict.update({eleman:1})
    for key in list(mini_dict.keys()):
        if((key,) in vocab):
            indexes.append(vocab.index((key,)))
            m=0
            for ii in range(0,len(list(mini_dict.values()))):
                m+=(list(mini_dict.values()))[ii]
            tf=(mini_dict.get(key))/m
            tfidf.append(idf[vocab.index((key,))][0]*tf)
        else:
            m = 0
            for ii in range(0, len(list(mini_dict.values()))):
                m += (list(mini_dict.values()))[ii]
            tf = (mini_dict.get(key)) / m
            tfidf.append(1594470 * tf)
    for j in range(0,len(tfidf_train)):
        sum=0.0
        res = json.loads(tfidf_train[j][0])
        res_tfidf=res[0]
        res_indexes=res[1]
        intersect_index = list(set(indexes) & set(res_indexes))
        if (len(intersect_index) != 0):
            for j2 in range(0, len(intersect_index)):
                sum += tfidf[indexes.index(intersect_index[j2])] * res_tfidf[res_indexes.index(intersect_index[j2])]
        len1 = 0
        len2 = 0
        for j2 in range(0, len(tfidf)):
            len1 += tfidf[j2] * tfidf[j2]
        len1 = math.sqrt(len1)
        for j2 in range(0, len(res_tfidf)):
            len2 += res_tfidf[j2] * res_tfidf[j2]
        #print(len2)
        similar = sum / (len1 * len2)
        similarity.append(similar)
        #print(similarity)
    polar.append(polarity_doc(similarity))
    #print(polar)
    t+=1
    if t==500:
        break
    print(t)

po=polar[0:1000]
#ne=polar[1000:2000]
print(polar)
print(po.count(1))
#print(ne.count(-1))
#y1=y_net[0:3000]
#y2=y_net[3000:6000]
