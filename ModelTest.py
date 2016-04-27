from NGramModel import *
from BrownDataCleaner import *
from TimeMonitor import *

t = TimeMonitor()
t.start(msg='test')
sents = BrownDataCleaner.clean()
lm = NGramModel(4, sents)
context = ('i', 'love')
words = ('i', 'love', 'him')
lm.backoff.retrain(words)
n = len(context)
if n >= 3:
    print 'this is quadgram'
    print lm.predict(context[-3:])
elif n == 2:
    print 'this is trigram'
    print lm.backoff.predict(context)
elif n == 1:
    print 'this is bigram'
    print lm.backoff.backoff.predict(context)
else:
    print 'this is unigram'
    print lm.backoff.backoff.backoff.predict(context)
t.stop()
