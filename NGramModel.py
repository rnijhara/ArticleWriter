from nltk.util import ngrams
from nltk.probability import ConditionalFreqDist
from collections import defaultdict
from operator import itemgetter
import cPickle


class NGramModel:
    """
    A class to implement the N-Gram Model.
    methods:
        predict(tuple context): predicts the next 3 words in the given context
        retrain(tuple words): retrains the model with the given words
    """

    def __init__(self, order, training_data):

        """
        Recursively creates all the n gram models from n to 1.
        :param order: value N of the N-Gram Model. Will be kept 4.
        :param training_data: cleaned sentences of the Brown Corpus by the BrownDataCleaner
        """

        self.order = order
        if order > 1:
            self.backoff = NGramModel(order - 1, training_data)
        else:
            self.backoff = None

        # cfd stores the frequency of a token given a context
        self.cfd = ConditionalFreqDist()
        # predictor is a dictionary with contexts as keys and top 3 frequency words as values
        self.predictor = defaultdict(list)
        sentences = training_data
        print 'preparing', order
        # contexts is a set used to collect contexts which help in creating predictor
        self.contexts = set()
        # This loop first breaks sentences into ngrams and then breaks each ngram into context and token
        # For example trigram = ('this', 'is', 'me')
        # context = ('this', 'is') , token = 'me'
        for sentence in sentences:
            rawngrams = ngrams(sentence, order)
            for ngram in rawngrams:
                context = tuple(ngram[:-1])
                token = ngram[-1]
                self.cfd[context][token] += 1
                self.contexts.add(context)

        # This step is used to create predictor from contexts set.
        if order == 1:
            context = ()
            # predictions is a dictionary which contains tokens as keys and their frequency for a given context
            # as values
            predictions = dict(self.cfd[context])
            # A word is a key value pair (tuple) of tokens and frequencies sorted in descending order of freq.
            words = sorted(predictions.items(), key=itemgetter(1), reverse=True)
            for i in range(0, 10):
                self.predictor[context].append(words[i][0])
            print 'prepared 1'
        else:
            for context in self.contexts:
                predictions = dict(self.cfd[context])
                words = sorted(predictions.items(), key=itemgetter(1), reverse=True)
                for i in range(0, len(words)):
                    self.predictor[context].append(words[i][0])
            print 'prepared', order

    def predict(self, context):

        """
        The predict method is used to predict the next 3 words based on a given context tuple.
        It backs off to a previous gram model if no prediction is found.
        """

        if self.predictor[context] == [] and self.order != 1:
            return self.backoff.predict(context[1:])
        else:
            return self.predictor[context]

    def retrain(self, words):

        """
        The retrain method is used to recursively retrain the ngram model with the words captured from the user.
        The retrain technique assigns the frequency greater than the maximum frequency of
        any token in the given context.
        """

        if self.order > 1:
            self.backoff = self.backoff.retrain(words[1:])
        else:
            self.backoff = None
        context = tuple(words[:-1])
        token = words[-1]
        if context in self.contexts:
            maximum_freq_word = self.cfd[context].max()
            freq = self.cfd[context][maximum_freq_word]
            self.cfd[context][token] = freq + 1
            del self.predictor[context]
        else:
            self.cfd[context][token] += 1
        if self.order == 1:
            context = ()
            predictions = dict(self.cfd[context])
            words = sorted(predictions.items(), key=itemgetter(1), reverse=True)
            for i in range(0, 10):
                self.predictor[context].append(words[i][0])
        else:
            predictions = dict(self.cfd[context])
            words = sorted(predictions.items(), key=itemgetter(1), reverse=True)
            for i in range(0, len(words)):
                self.predictor[context].append(words[i][0])
        return self

    def save_model(self):
        cPickle.dump(self, open("ngram.bin", "wb"))
