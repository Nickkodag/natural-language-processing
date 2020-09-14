import nltk
from nltk.tokenize import sent_tokenize ,word_tokenize
#nltk.download()
#tokkenizing

#Seperate token
#corpora -body text 
#lexicon - words and their means
example_text='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum'
print(sent_tokenize(example_text))     #create list
print(word_tokenize(example_text))   #create word
for i in word_tokenize(example_text):
    print(i)# veticle arrangment
#stop words
