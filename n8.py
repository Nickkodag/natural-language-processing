#corpora#wordnet
#how google serch work
from nltk.corpus import wordnet
syns=wordnet.synsets('program')
print(syns[0].name())


#defination
print(syns[0].definition())
#example
print(syns[0].examples())
#synonyms=[]
synonyms=[]
antonyms=[]
for syn in  wordnet.synsets('good'):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))