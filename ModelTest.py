from NGramModel import *
from nltk.corpus import brown

text = 'Hello from the other side is a song by Adele S. Trump. She is a very good singer and lyricist'
print(brown.words(categories='news'))
QuadGramModel = NGramModel(4, brown)
print(QuadGramModel.backoff.predict(('billion', 'dollar')))