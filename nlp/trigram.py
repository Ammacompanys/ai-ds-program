from nltk.util import ngrams

n=3
sentence="you will face many defeats in life, but never let yourself be defeated"
trigrams = ngrams(sentence.split(), n)
for item in trigrams:
    print(item)
    
    