from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def convert(line):
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(line)
    english_punctuations = set([',', '.', ':', ';', '?', '(', ')', '[', ']',
                                '&', '!', '*', '@', '#', '$', '%'])
    my_stop_words = set(['U.S.', '|', '***', "'s", '--', '=', '+', '-', "'",
                         "''", "``", 'I', 'i', 'II', 'ii', 'III', 'iii', 'iv',
                         'IV', 'V', 'v', 'VI', 'vi', 'VII', 'vii', 'VIII',
                         'viii', 'X', 'x', 'a', 'A'])

    final_stop_words = stop_words | english_punctuations | my_stop_words

    filtered_sentence = ""
    for w in word_tokens:
        w = w.strip()
        if w not in final_stop_words and w.isdigit() is False:
            filtered_sentence += stem(w) + " "
    filtered_sentence = filtered_sentence.strip()
    return filtered_sentence


def stem(w):
    result = ''
    ps = PorterStemmer()
    w = ps.stem(w)
    for i in w:
        if i.isalpha():
            result += i
    return result


def writeNew(file_path):
    a = file_path
    # new__path = file_path.replace(".txt", "") + '_new' + '.txt'
    name = file_path.split("/")[-1].replace(".txt", "")
    new_path = "../input-transform/" + name + "_new" + ".txt"
    try:
        f = open(file_path, mode='r', encoding='utf-8', errors='ignore')
        w = open(new_path, mode='w', encoding='utf-8')
        for line in f.readlines():
            new_line = convert(line)
            w.write(new_line + '\n')
    except UnicodeDecodeError:
        print('Decode error : ' + file_path)


