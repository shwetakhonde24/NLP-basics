import nltk
#nltk.download() #Downloading all the libraries of nltk
#nltk.download('punkt')
paragraph = "एक बार की बात है एक जंगल में एक झील थी। जो खुनी झील के नाम से प्रसिद्ध थी। शाम के बाद कोई भी उस झील में पानी पिने के लिए जाता तो वापस नहीं आता था। एक दिन चुन्नू हिरण उस जंगल में रहने के लिए आया।"
#Tokenizing sentence
sentences = nltk.sent_tokenize(paragraph)
words = nltk.word_tokenize(paragraph)
print(len(sentences))

