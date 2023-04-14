import numpy as np
import tflearn
import tensorflow as tf
import random
import json
import pickle
from utils import clean_pattern, define_network
with open('hembrev.json') as file:
    data = json.load(file)
print(data)

# Some cleaning of data in intents.json
stemmed_words = []
tags = []
ignore_words = ['!', '?', '.']
corpus = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        stemmed_pattern = clean_pattern(pattern, ignore_words)
        stemmed_words.extend(stemmed_pattern)
        corpus.append((stemmed_pattern, intent['tag']))
    if intent['tag'] not in tags:
        tags.append(intent['tag'])

# remove duplicates and sort
stemmed_words = sorted(list(set(stemmed_words)))
tags = sorted(list(set(tags)))

print(stemmed_words)
print(tags)
print(corpus)


# Creating numeric features and labels out of cleaned data
X = []
y = []
for item in corpus:
    bag = [] #array of 1 and 0. 1 if stemmed word is present in stemmed pattern
    stemmed_pattern = item[0]
    for w in stemmed_words:
        if w in stemmed_pattern:
            bag.append(1)
        else:
            bag.append(0)

    tags_row = [] #array of 1 and 0. 1 for current tag and for everything else 0.
    current_tag = item[1]
    for tag in tags:
        if tag == current_tag:
            tags_row.append(1)
        else:
            tags_row.append(0)

    #for each item in corpus, X will be array indicating stemmed words and y array indicating tags
    X.append(bag)
    y.append(tags_row) 

X = np.array(X)
y = np.array(y)
print(X)
print(y)

# saving variables in pickle to be used by main.py
with open('saved_variables.pickle', 'wb') as file:
    pickle.dump((stemmed_words, tags, ignore_words, X, y), file)
    
    
    
model = define_network(X, y)
model.fit(X, y, n_epoch=1120, batch_size=8, show_metric=True) 
model.save("chatbot_model1.tflearn")