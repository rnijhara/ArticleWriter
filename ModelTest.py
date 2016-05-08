from TimeMonitor import *
from NGramModel import *
from BrownDataCleaner import *
import cPickle

t1 = TimeMonitor()
t2 = TimeMonitor()
t1.start(msg='Loading file')
data = open("ngram.bin", "rb")
t1.stop()
t2.start(msg='Preparing model')
lm = cPickle.load(data)
t2.stop()
context = ('i', 'love')
words = ('malviya', 'chutiya', 'hai')
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
