import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
paragraph = "Yasin even made friends with a boy who lived next door, called Andrew. All summer long, Andrew and Yasin played in the park or went to the zoo with Andrew’s mum. Andrew shared his toys and his comics with Yasin and told him all about his favourite superheroes. They even built a camp in Yasin’s back garden where they would hide from the grownups."
sentence = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer() #intializing porter stemmer and creating a object of it
#stemming
for i in range(len(sentence)):
    words = nltk.word_tokenize(sentence[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentence[i] = ' '.join(words)
print(sentence)



