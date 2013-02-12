__author__ = 'Matthew Smith'

import nltk
from collections import defaultdict

def get_freqs(text):

    stop_words = nltk.corpus.stopwords.words('english')
    frequencies = defaultdict(int)

    pattern = r'''(?x)    # set flag to allow verbose regexps
                    ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
                    | \w+(-\w+)*        # words with optional internal hyphens
                    | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
                    | \.\.\.            # ellipsis
                    | [][.,;"'?():-_`]  # these are separate tokens
                     '''

    if type(text) == list:
        print 'number of links: '+ str(len(text))
        for t in text:
            content = t['content']
            tokens = nltk.regexp_tokenize(content, pattern)
            for word in tokens:
                if len(word) > 2 and word.lower() not in stop_words:
                    cap = word[0].upper() + word[1:]
                    frequencies[cap] += 1
    else:
        tokens = nltk.regexp_tokenize(text, pattern)
        for word in tokens:
            if len(word) > 2 and word not in stop_words:
                frequencies[word] += 1
    print "frequency size: "+str(len(frequencies))
    return frequencies

def process_phrase(phrase):
    pass

