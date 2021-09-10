from csv import reader
import numpy
from nltk import word_tokenize

with open(r'C:\Users\Mohammadreza Rahmani\Desktop\y_net.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)
train_data = numpy.array(list_of_rows)
y_net= []
for item in train_data:
    b = numpy.asarray(item, dtype=numpy.float64, order='C')
    y_net.append(list(b))

import psycopg2
con = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="mm123456"
)
cur = con.cursor()
cur.execute("select * from distinct_stemmed_pos")
positive = cur.fetchall()
cur.execute("select * from distinct_stemmed_neg")
negative = cur.fetchall()
sentences = []
for i in range(0, len(positive)):
    sentences.append(positive[i][0])

for i in range(0, len(negative)):
    sentences.append(negative[i][0])
train = sentences[2000:4000] + sentences[101999:103999]
test_pos=sentences[6000:7000]
test_neg=sentences[105999:106999]

t=0
test_pos=["terribbl"]
for item in test_pos:
    tokens=word_tokenize(item)
    repeat_pos=0
    repeat_neg=0
    for token in tokens:
        for i in range(0,len(train)):
            listi=sentences[i].split()
            count=listi.count(token)
            if(y_net[i][0]>0):
                repeat_pos+=count
            elif(y_net[i][1]>0):
                repeat_neg+=count
    if(repeat_pos>=repeat_neg and repeat_pos!=0):
        print(item)
        print(repeat_pos)
        print(repeat_neg)
        print("/////////////")

        t+=1
print("pos")
print(t)


t=0

test_neg=["smile","lov","ugli","hater","fuck","terribbl"]
for item in test_neg:
    tokens=word_tokenize(item)
    repeat_pos=0
    repeat_neg=0
    for token in tokens:
        for i in range(0,len(train)):
            listi=sentences[i].split()
            count=listi.count(token)
            if(y_net[i][0]>0):
                repeat_pos+=count
            if(y_net[i][1]>0):
                repeat_neg+=count
    if(repeat_pos<=repeat_neg):
        print(item)
        print("////////////")
        t+=1
print("neg")
print(t)