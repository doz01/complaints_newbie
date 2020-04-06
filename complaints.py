mport csv
import pandas as pd 
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score


link = 'https://drive.google.com/open?id=1HunBx-s1EYiu0So0klRos4aTfMEQhjFF'
fluff, id = link.split('=')
downloaded = drive.CreateFile({'id':id}) 
downloaded.GetContentFile('complaints.csv')  
comments = []
labels = []
df = pd.read_csv('complaints.csv')
comments = df['comments']
labels_col = df['labels']

def make_dict():
    words = []

    for i in range (len(comments)):
        word = comments[i].split()
        words += word
        words += " "

    for i in range (len(words)):
        if not words[i].isalpha():
            words[i]=""

    dictionary = Counter(words)
    del dictionary[""]
    return dictionary

def make_dataset(dictionary):
    feature_set = []
    labels = []
    c = len(comments)

    for i in range (len(comments)):
        data = []
        for entry in dictionary:
            data.append(comments[i].count(entry[0]))
        feature_set.append(data)

        if labels_col[i] == 0:
            labels.append(0)
        if labels_col[i] == 1:
            labels.append(1)
        print (c)
        c -= 1
    return feature_set, labels

d = make_dict()
features, labels = make_dataset(d)

x_train, x_test, y_train, y_test = tts(features, labels, test_size = 0.2)

clf = MultinomialNB()
clf.fit(x_train, y_train)

preds = clf.predict(x_test)
print (accuracy_score(y_test, preds))
