from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize ,word_tokenize
example_text='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum'
#stop word filtration
stop_words=set(stopwords.words('english'))
print(stop_words)   # all english stop words
words=word_tokenize(example_text)
filter_sentence=[]
for w in words:
    if w not in stop_words:
        filter_sentence.append(w)
print(filter_sentence)        