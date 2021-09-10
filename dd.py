import psycopg2
from nltk.tokenize import word_tokenize
import re
from nltk.stem import PorterStemmer
import math

con=psycopg2.connect(
     host="localhost",
     database="postgres",
     user="postgres",
    password="mm123456"
 )
cur=con.cursor()

cur.execute("select * from probabilities")
probabilities=cur.fetchall()
cur.execute("select * from pos_distinct")
positive=cur.fetchall()
cur.execute("select * from neg_distinct")
negative=cur.fetchall()
negative=negative[99999:200000]
positive=positive[99999:200000]
index=-1
sum=0.0
with open(r'C:\Users\Mohammadreza Rahmani\Desktop\vocab.txt') as f:
    lines = f.readlines()
for i in range(0,len(lines)):
    lines[i]=lines[i].replace('\n','')
vocab=lines
for i in range(0,1):
    data="frustrat"
    tokens = word_tokenize(data)
    ps = PorterStemmer()
    print(ps.stem("youngest"))
    stemmed_words = [ps.stem(w) for w in tokens]
    for item in stemmed_words:
        index=-1
        for j in range(0,len(vocab)):
            if(vocab[j]==item):
                index=j
                break
        if(index!=-1):
            sum+=math.log((probabilities[j][0]/probabilities[j][1]),10)
    if(sum>0):
        #cur.execute("insert into pos_test values ('positive')")
        #con.commit()
        print('po')
    if(sum<0):
        #cur.execute("insert into pos_test values ('negative')")
       # con.commit()
       print('ne')
    if(sum==0):
       # cur.execute("insert into pos_test values ('neutral')")
        #con.commit()
        print("nu")
    print(1)
