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
