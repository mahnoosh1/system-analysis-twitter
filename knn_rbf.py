from csv import reader
import numpy
import psycopg2
from nltk.tokenize import word_tokenize

con=psycopg2.connect(
     host="localhost",
     database="postgres",
     user="postgres",
    password="mm123456"
 )
cur=con.cursor()

#with open(r'C:\Users\Mohammadreza Rahmani\Desktop\y_test.csv', 'r') as read_obj:
  #  csv_reader = reader(read_obj)
 #   list_of_rows = list(csv_reader)
#train_data = numpy.array(list_of_rows)
#y_network = []
#for item in train_data:
  #  b = numpy.asarray(item, dtype=numpy.float64, order='C')
 #   y_network.append(list(b))
#for i in range(0,len(y_network)):
   #if y_network[i][0]>0 and y_network[i][1]<0:
     #  cur.execute("insert into y_network values(1)")
    #   con.commit()
   #elif y_network[i][0]<0 and y_network[i][1]>0:
      #cur.execute("insert into y_network values(-1)")
      #con.commit()


cur.execute("select * from distinct_stemmed_pos")
positive = cur.fetchall()
cur.execute("select * from distinct_stemmed_neg")
negative = cur.fetchall()
cur.execute("select * from idf")
idf=cur.fetchall()
with open(r'C:\Users\Mohammadreza Rahmani\Desktop\tweet_count.txt') as f:
    data = f.read()
tweetcount = eval(data)
vocab=list(tweetcount.keys())

sentences = []
for i in range(0, len(positive)):
    sentences.append(positive[i][0])

for i in range(0, len(negative)):
    sentences.append(negative[i][0])

train=sentences[2000:7000]+sentences[101999:106999]

for item in train:
    dict={}
    indexes=[]
    tfidf=[]
    listi=[]
    tokens=word_tokenize(item)
    for eleman in tokens:
        if (eleman in dict.keys()):
            dict.update({eleman: dict.get(eleman) + 1})
        else:
            dict.update({eleman: 1})
    for key in list(dict.keys()):
        indexes.append(vocab.index(key))
        tf=(dict.get(key))/sum(list(dict.values()))
        tfidf.append(idf[vocab.index(key)][0]*tf)
    listi.append(tfidf)
    listi.append(indexes)
    cur.execute(("insert into tf_idf_trainrbf(str) values('%s')") % (listi))
    con.commit()
    print(1)