import nltk
paragraph = "Yasin even made friends with a boy who lived next door, called Andrew. All summer long, Andrew and Yasin played in the park or went to the zoo with Andrew’s mum. Andrew shared his toys and his comics with Yasin and told him all about his favourite superheroes.They even built a camp in Yasin’s back garden where they would hide from the grownups."
#cleaning the text
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
ps = PorterStemmer()
wordnet = WordNetLemmatizer()
sentences = nltk.sent_tokenize(paragraph)
corpus = []
for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]',' ',sentences[i])
    review = review.lower()
    review = review.split()
    review = [wordnet.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

#creating the TF-IDF model
from sklearn.feature_extraction.text import TfidfVectorizer # tfidvectorizer is for tfid model
cv = TfidfVectorizer()
x = cv.fit_transform(corpus).toarray() # fit-transform creates a matrix for our corpus
print(corpus)