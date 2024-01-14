import nltk
from gensim.models import Word2Vec
from nltk.corpus import stopwords
import re
paragraph = "Yasin even made friends with a boy who lived next door, called Andrew. All summer long, Andrew and Yasin played in the park or went to the zoo with Andrew’s mum. Andrew shared his toys and his comics with Yasin and told him all about his favourite superheroes.They even built a camp in Yasin’s back garden where they would hide from the grownups."
#Preprocessing the data
text = re.sub(r'\[[0-9]*\]', ' ', paragraph)
text = re.sub(r'\s+', ' ', text)
text = text.lower()
text = re.sub(r'\d', ' ', text)
text = re.sub(r'\s+', ' ', text)

# Preparing the dataset
sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

for i in range(len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in stopwords.words('english')]

# Training the Word2Vec model
model = Word2Vec(sentences, min_count=1) # here min_count=1 means if the word is present less than 1 ignore it,usually people take count=2 in large dataset

words = model.wv.key_to_index

# Finding Word Vectors
vector = model.wv['yasin']

# Most similar words
similar = model.wv.most_similar('friends')
print(similar)