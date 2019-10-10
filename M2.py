from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

if __name__ == "__main__":
    """
    ps = PorterStemmer()
    # choose some words to be stemmed
    words = ["program", "programs", "programer", "programing", "programers"]
    for w in words:
        print(w, " : ", ps.stem(w))
    """

    example_sent = "Document will describe marketing strategies carried out by U.S. companies for their agricultural" \
                   "chemicals, report predictions for market share of such chemicals, or report market statistics for " \
                   "agrochemicals, pesticide, herbicide, fungicide, insecticide, fertilizer, predicted sales, market share, " \
                   "stimulate demand, price cut, volume of sales. "
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(example_sent)
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    print(word_tokens)
    print(filtered_sentence)