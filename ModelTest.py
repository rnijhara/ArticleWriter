from NGramModel import *
from BrownDataCleaner import *

sents = BrownDataCleaner.clean()
QuadGramModel = NGramModel(4, sents)
print QuadGramModel.backoff.predict(('billion', 'dollar'))
print QuadGramModel.backoff.predictor[('billion', 'dollar')]
