import pprint
import os
from gensim import corpora, models, similarities

training_dir = './training'
testing_dir = './testing/'


def get_files_with_paths(path):
    files = []
    for (r, d, f) in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))

    return files

def create_corpus():
    corpus = []
    filenames = get_files_with_paths(training_dir)
    for fname in filenames:
        with open(fname, 'r', encoding="utf8") as file:
            data = file.read().replace('\n', ' ')

            corpus.append(data)
    return corpus


heb_corpus = create_corpus()

# Create a set of frequent words
stoplist = set('של ו ה כי אם . אבל אולם גם או רק'.split(' '))

# Lowercase each document, split it by white space and filter out stopwords
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in heb_corpus]

# Count word frequencies
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

# Only keep words that appear more than once
processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]

dictionary = corpora.Dictionary(processed_corpus)

new_doc_heb = "אדם מחשב אינטרפייס תגובה"
new_doc = "Human computer interaction response"
new_vec = dictionary.doc2bow(new_doc.lower().split())


bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]

# train the model
tfidf = models.TfidfModel(bow_corpus)

# transform the "system minors" string
words = " החמור עמי הלך אדומה זאב".lower().split()

index = similarities.SparseMatrixSimilarity(tfidf[bow_corpus], num_features=197)

# test file:
with open(testing_dir+'rrh2.txt', 'r', encoding="utf8") as file:
    test_data = file.read().replace('\n', ' ')
    test_bow = dictionary.doc2bow(test_data.split())
    sims2 = index[tfidf[test_bow]]
    print(list(enumerate(sims2)))

