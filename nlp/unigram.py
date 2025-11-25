from nltk.util import ngrams

n = 1
sentence = "you will face many defeats in life, but never let yourself be defeated"
unigram = ngrams(sentence.split(), n)

for item in unigram:
    print(item)
