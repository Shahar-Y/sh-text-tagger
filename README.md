# sh-text-tagger
### sh-text-tagger is a gensim-based documents tagger


#### How does it work?

1. It uses a training corpus with documents in a given training folder.
2. The corpus is then used with the tf-idf algorithm to create a trained bag of words.
3. It receives a new document which needs to be evaluated, and compares it to the trained BOW.
4. the output is the match precentage to each of the training documents.