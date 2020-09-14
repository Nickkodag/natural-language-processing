# in this we gonna search for meaning of sentence 
# now we have to serch for modifire  word
#chunking 1.0
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

sample_text=state_union.raw('2006-GWBush.txt')
custom_sen_tok= PunktSentenceTokenizer(sample_text)
tokenizer=custom_sen_tok.tokenize(sample_text)
def process_content():
    try:
        for i in tokenizer:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)

            chunkgram=r""" chunk:{<.*>+} """
            chunkParser=nltk.RegexpParser(chunkgram)
            chunked=chunkParser.parse(tagged)
            chunked.draw()



            print(tagged)
    except Exception as e:
        print(str(e))        

process_content()        