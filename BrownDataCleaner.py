from nltk.corpus import brown
import re


class BrownDataCleaner:
    """BrownDataCleaner is used to clean the Brown Corpus.
       clean() static method is used for this.
       It may further take category value for the brown corpus as an argument.
    """
    @staticmethod
    def clean():

        """
        1. Removes any individual special character.
        2. Lowers all the words.
        :return: list of clean sentences
        """

        sents = list(brown.sents())
        sents_copy = list(brown.sents())
        n = len(sents)
        print 'Removing special chars...'
        for i in range(0, n):
            for word in sents[i]:
                if not bool(re.search('[A-Za-z0-9]', word)):
                    sents_copy[i].remove(word)
        print 'Removed special chars.'
        sents = None

        print 'Lowering all the words...'
        for i in range(0, n):
            m = len(sents_copy[i])
            for j in range(0, m):
                sents_copy[i][j] = sents_copy[i][j].lower()
        print 'Lowered all the words.'
        return sents_copy
