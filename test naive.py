import psycopg2
from nltk.tokenize import word_tokenize
import re
from nltk.stem import PorterStemmer
import math
from nltk.corpus import stopwords

con=psycopg2.connect(
     host="localhost",
     database="postgres",
     user="postgres",
    password="mm123456"
 )
cur=con.cursor()

stop_words = set(stopwords.words('english'))
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
with open(r'C:\Users\Mohammadreza Rahmani\Desktop\tweet_count.txt') as f:
    data = f.read()
tweetcount = eval(data)
vocab=list(tweetcount.keys())

for i in range(0,len(positive)):
    pattern = r'[0-9]'
    data = re.sub(pattern, ' ', positive[i][0])
    sum=0.0
    pattern=r"['™', '©', '®', '‰', '±', '¼', '½', '¾', '≡', '≈', '≥', '≤', '√', 'ⁿ', '¹', '²', '³', 'π', '°', '∞', 'µ', 'Σ', '☺', '☻', '•', '○', '♂', '♀', '↨', '↑', '↓', '→', '←', '↔', '£', '€', '$', '¢', '¥', 'ƒ', '₧', 'α', 'ß', 'δ', 'Ω', '►', '◄', '■', '▲', '▼', '§', '¶', '“', '”', '«', '»', '♥', 'º', 'œ', '•', '↻', '↺', 'Ø', 'Ñ', 'Ø', '±', 'Ù', '†', '§', '…', '‡', '¬', 'Û', 'Œ', 'Ú', '©', '´', '¾', '„', 'ª', 'µ', '¯', 'Ø³', 'Ø¹', 'ˆ', '®', 'Ø²', 'Ø°', 'º', 'â', '€', 'Ž']"
    data = re.sub(pattern, ' ', data)
    tokens = word_tokenize(data)
    ps = PorterStemmer()
    stemmed_words = [ps.stem(w) for w in tokens]
    stemmed_words = [w for w in stemmed_words if not w in stop_words]
    for item in stemmed_words:
        index=-1
        for j in range(0,len(vocab)):
            if(vocab[j]==item):
                index=j
                print(index)
                break
        if(index!=-1):
            sum+=math.log((probabilities[j][0]/probabilities[j][1]),10)
    if(sum>0):
        cur.execute("insert into pos_test values ('positive')")
        con.commit()
        print(sum)
    if(sum<0):
        cur.execute("insert into pos_test values ('negative')")
        con.commit()
        print(sum)
    if(sum==0):
        cur.execute("insert into pos_test values ('neutral')")
        con.commit()
        print(sum)
    print(1)
for i in range(0,len(negative)):
    pattern = r'[0-9]'
    data = re.sub(pattern, ' ', negative[i][0])
    sum=0.0
    pattern=r"['™', '©', '®', '‰', '±', '¼', '½', '¾', '≡', '≈', '≥', '≤', '√', 'ⁿ', '¹', '²', '³', 'π', '°', '∞', 'µ', 'Σ', '☺', '☻', '•', '○', '♂', '♀', '↨', '↑', '↓', '→', '←', '↔', '£', '€', '$', '¢', '¥', 'ƒ', '₧', 'α', 'ß', 'δ', 'Ω', '►', '◄', '■', '▲', '▼', '§', '¶', '“', '”', '«', '»', '♥', 'º', 'œ', '•', '↻', '↺', 'Ø', 'Ñ', 'Ø', '±', 'Ù', '†', '§', '…', '‡', '¬', 'Û', 'Œ', 'Ú', '©', '´', '¾', '„', 'ª', 'µ', '¯', 'Ø³', 'Ø¹', 'ˆ', '®', 'Ø²', 'Ø°', 'º', 'â', '€', 'Ž','Ã','¯','Â','¿','ø','Ã','£']"
    data = re.sub(pattern, ' ', data)
    tokens = word_tokenize(data)
    ps = PorterStemmer()
    stemmed_words = [ps.stem(w) for w in tokens]
    stemmed_words = [w for w in stemmed_words if not w in stop_words]
    for item in stemmed_words:
        index=-1
        for j in range(0,len(vocab)):
            if(vocab[j]==item):
                index=j
                break
        if(index!=-1):
            sum+=math.log((probabilities[j][0]/probabilities[j][1]),10)
    if(sum>0):
        cur.execute("insert into neg_test values ('positive')")
        con.commit()
        print(sum)
    if(sum<0):
        cur.execute("insert into neg_test values ('negative')")
        con.commit()
        print(sum)
    if(sum==0):
        cur.execute("insert into neg_test values ('neutral')")
        con.commit()
        print(sum)
    print(2)
