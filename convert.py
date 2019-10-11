from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def convert(line):
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(line)
    english_punctuations = set([',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%'])
    my_stop_words = set(['U.S.'])

    final_stop_words = stop_words | english_punctuations | my_stop_words

    filtered_sentence = ""
    for w in word_tokens:
        if w not in final_stop_words:
            filtered_sentence += ps.stem(w) + " "
    filtered_sentence = filtered_sentence.strip()
    return filtered_sentence
