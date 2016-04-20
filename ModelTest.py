from NGramModel import *
from BrownDataCleaner import *

text = 'Hello from the other side is a song by Adele S. Trump. She is a very good singer and lyricist'

sents = BrownDataCleaner.clean()
QuadGramModel = NGramModel(4, sents)
print(QuadGramModel.backoff.predict(('billion', 'dollar')))
