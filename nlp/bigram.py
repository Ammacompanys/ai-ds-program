from nltk.util import ngrams

n = 2
sentence = "you will face many defeats in life, but never let yourself be defeated"
bigrams = ngrams(sentence.split(), n)
for item in bigrams:
    print(item)
    
    
