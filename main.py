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


def merge_files():
    filenames = ['red_riding_hood.txt', 'donkey_in_the_well.txt', 'ami_and_tami.txt']
    with open('./output.txt', 'w', encoding="utf8") as outfile:
        for fname in filenames:
            with open(fname, encoding="utf8") as infile:
                outfile.write(infile.read())

# merge_files()

# text_corpus_heb = [
#     "אדם מכונה אינטרפייס אדם אדם כי מעבדה אבג מערכת מחשב אפליקציות",
#     "סקר של משתמש של מחשב מערכת זמן תגובה",
#     "ה איפיאס איפיאס משתמש אינטרפייס מערכת ניהול",
#     "ה איפיאס משתמש אינטרפייס מערכת ניהול",
#     "מערכת ו אדם מערכת מהנדס מבחן של איפיאס",
# ]


def create_corpus():
    corpus = []
    filenames = get_files_with_paths(training_dir)
    for fname in filenames:
        with open(fname, 'r', encoding="utf8") as file:
            data = file.read().replace('\n', ' ')
            # print(data)

            corpus.append(data)

    # print(corpus)
    return corpus
    # print(corpus.__len__())


heb_corpus = create_corpus()


# text_corpus = [
#     "Human machine interface human human for lab abc system computer applications",
#     "A survey of user opinion of computer system response time",
#     # "The EPS user interface management system",
#     # "The EPS user interface management system",
#     # "System and human system engineering testing of EPS",
#     # "Relation of user perceived response time to error measurement",
#     # "The generation of random binary unordered trees",
#     # "The intersection graph of paths in trees",
#     # "Graph minors IV Widths of trees and well quasi ordering",
#     # "Graph minors A survey",
# ]

# Create a set of frequent words
stoplist = set('של ו ה כי'.split(' '))

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
# pprint.pprint(processed_corpus)

dictionary = corpora.Dictionary(processed_corpus)
print("**************************** dictionary: ****************************")
print(dictionary)

# pprint.pprint(dictionary.token2id)

new_doc_heb = "אדם מחשב אינטרפייס תגובה"
new_doc = "Human computer interaction response"
new_vec = dictionary.doc2bow(new_doc.lower().split())
print(new_vec)


bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]
pprint.pprint(bow_corpus)


# train the model
tfidf = models.TfidfModel(bow_corpus)

# transform the "system minors" string
words = " החמור עמי הלך אדומה זאב".lower().split()
print(tfidf[dictionary.doc2bow(words)])

print(bow_corpus.__len__())
index = similarities.SparseMatrixSimilarity(tfidf[bow_corpus], num_features=197)
print(index)

query_document = "כיפה אדומה".split()
query_bow = dictionary.doc2bow(query_document)
print(query_bow)

print(tfidf[query_bow])
sims = index[tfidf[query_bow]]
print("sims:")
print(list(enumerate(sims)))

# test file:
with open(testing_dir+'rrh2.txt', 'r', encoding="utf8") as file:
    test_data = file.read().replace('\n', ' ')
    test_bow = dictionary.doc2bow(test_data.split())
    sims2 = index[tfidf[test_bow]]
    print(list(enumerate(sims2)))

