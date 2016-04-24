from nltk.util import ngrams
from nltk.probability import ConditionalFreqDist
from collections import defaultdict


class NGramModel:

    '''
    A class to implement the N-Gram Model.
    methods:
        predict(tuple context): predicts the next 3 words in the given context
        retrain(tuple words): retrains the model with the given words
    '''

    def __init__(self, order, trainingData):

        '''
        Recursively creates all the n gram models from n to 1.
        :param order: value N of the N-Gram Model. Will be kept 4.
        :param trainingData: cleaned sentences of the Brown Corpus by the BrownDataCleaner
        '''

        self.order = order
        if order > 1:
            self.backoff = NGramModel(order-1, trainingData)
        else:
            self.backoff = None
        self.cfd = ConditionalFreqDist()
        self.predictor = defaultdict(list)
        sentences = trainingData
        for sentence in sentences:
            rawNgrams = ngrams(sentence, order)
            context_list = list()
            for ngram in rawNgrams:
                context = tuple(ngram[:-1])
                token = ngram[-1]
                self.cfd[context][token] += 1
                context_list.append(context)
            for context in context_list:
                words = list(dict(self.cfd[context]).keys())
                n = len(words)
                if n == 1:
                    self.predictor[context].append(words[0])
                if n == 2:
                    self.predictor[context].append(words[0])
                    self.predictor[context].append(words[1])
                else:
                    self.predictor[context].append(words[0])
                    self.predictor[context].append(words[1])
                    self.predictor[context].append(words[2])

        print self.predictor[('billion', 'dollar')]




    def predict(self, context):
        predictions = list(dict(self.cfd[context]).keys())
        print predictions
        nums = len(predictions)
        print self.order
        finalPredictions = 'the'
        if nums >=3:
            finalPredictions = predictions[0] + ' ' + predictions[1] + ' ' + predictions[2]
        elif nums == 2:
            finalPredictions = predictions[0] + ' ' + predictions[1]
        elif nums == 1:
            finalPredictions = predictions[0]
        elif nums == 0 and self.order != 1:
            finalPredictions = self.backoff.predict(context[1:])
        return finalPredictions

    def retrain(self, words):
        if self.order > 1:
            self.backoff = self.retrain(words[1:])
        else:
            self.backoff = None
        context = tuple(words[:-1])
        token = words[-1]
        self.cfd[context][token] += 1
        return self

