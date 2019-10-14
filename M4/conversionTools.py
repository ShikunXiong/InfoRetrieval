from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os
import sys
import M4.heap as hp
import math

def stem(w):
    result = ''
    ps = PorterStemmer()
    w = ps.stem(w)
    for i in w:
        if i.isalpha():
            result += i
    return result

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


def getIndexData(line):
    dic = {}
    files = []
    l = line.split(" ")
    for word in l:
        if len(l)>1:
            dic.setdefault(word, {})
            dic[word], nums = getFiledata(word)
            files += nums
    return dic, files



def getFiledata(word):
    """
    Used in getIndexData()
    :param word: word after stemming
    :return: dict, list of file_names
    """
    prefix = word[0]
    dic = {}
    files = []
    all_files = os.listdir("../M3/index")
    for file in all_files:
        if prefix in file:
            f = open("../M3/index" + "/" + file)
            next_word = True
            reading = False
            for line in f.readlines():
                if next_word is True:
                    line = line.strip()
                    if line == word:
                        # match
                        next_word = False
                        reading = True
                elif line is "\n":
                    next_word = True
                    reading = False
                elif reading is True:
                    line = line.strip('\n').strip('\t')
                    l = line.split(":")
                    file_num = l[0]
                    word_times = l[1]
                    positions = l[2].split(",")
                    dic.setdefault(file_num, [])
                    dic[file_num].append(word_times)
                    dic[file_num] += positions
                    if file_num not in files:
                        files.append(file_num)
    return dic, files


def getCountScore(file_num, dic, word_list):
    """
    Return the count score for one file
    :param file_num: e.g '10103'
    :param dic: get from getIndexData()
    :param word_list: after stemming
    :return: the count score for a file
    """
    result = 0
    for word in word_list:
        if word in dic.keys():
            word_dic = dic[word]
            if file_num in word_dic.keys():
                result += int(word_dic[file_num][0])
    return result


def getPositionScore(file_num, dic, word_list):
    """
    Used in getScoreRank()
    :param file_num: file_name e.g:'10001'
    :param dic: get from getFiledata()
    :param word_list: word_list after stemming
    :return: the position_score for a file
    """
    score_sum = 0
    size = len(word_list)
    for i in range(0, size-1):
        word1 = word_list[i]
        word2 = word_list[i+1]
        if word1 in dic.keys() and word2 in dic.keys():
            dic1 = dic[word1]
            dic2 = dic[word2]
            if file_num in dic1.keys() and file_num in dic2.keys():
                l1 = dic1[file_num]
                l2 = dic2[file_num]
                score_sum += getShortest(l1, l2)
    return score_sum if score_sum != 0 else 0


def getScoreRank(files, dic, word_list):
    heap = []
    for f in files:
        s = getPositionScore(f, dic, word_list) + \
            getCountScore(f, dic, word_list)
        heap = hp.heapAdd([s, f], heap)
    return hp.getRankList(heap)


def getShortest(l1, l2):
    shortest = sys.maxsize
    for i in range(len(l1)):
        for j in range(len(l2)):
            if abs(int(l1[i])-int(l2[j])) < shortest and abs(int(l1[i])-int(l2[j]))!=0:
                shortest = abs(int(l1[i])-int(l2[j]))
    return 1/shortest


# Module 5
def getInputVector(l):
    dic = {}
    sum_word = 0
    vector = []
    for i in l:
        sum_word += 1
        dic.setdefault(i, 0)
        dic[i] += 1
    for k, v in dic.items():
        vector.append(v/sum_word)
    return vector


def getCosine(v1, v2):
    m = 0
    n1 = 0
    n2 = 0
    for i in range(len(v1)):
        m += v1[i]*v2[i]
        n1 += v1[i]**2
        n2 += v2[i]**2
    n = (n1*n2)**0.5
    return m/n


def getFileVector(file_num, dic, inputList):
    tmp = []
    denominator = 0
    vecotr = []
    for word in inputList:
        if file_num in dic[word].keys():
            # fk: times of word shown in the file
            fk = int(dic[word][file_num][0])
        else:
            fk = 1
        # nums of files in which the word is shown
        shown_times = len(dic[word].keys())
        result = (math.log2(fk)+1)*(math.log2(1001/shown_times))
        tmp.append(result)
    for i in tmp:
        denominator += i**2
    denominator = denominator**0.5
    for i in tmp:
        vecotr.append(i/denominator)
    return vecotr


def getNewPositionScore(file_num, dic, word_list):
    """
    Used in getScoreRank()
    :param file_num: file_name e.g:'10001'
    :param dic: get from getFiledata()
    :param word_list: word_list after stemming
    :return: the position_score for a file
    """
    score_sum = 0
    size = len(word_list)
    for i in range(0, size-1):
        word1 = word_list[i]
        word2 = word_list[i+1]
        if word1 in dic.keys() and word2 in dic.keys():
            dic1 = dic[word1]
            dic2 = dic[word2]
            if file_num in dic1.keys() and file_num in dic2.keys():
                l1 = dic1[file_num]
                l2 = dic2[file_num]
                score_sum += getShortest(l1, l2)
    return score_sum/len(word_list) if score_sum != 0 else 0


def getNewScoreRank(files, dic, word_list, input_list):
    heap = []
    for f in files:
        v1 = getFileVector(f, dic, input_list)
        v2 = getInputVector(input_list)
        s = getNewPositionScore(f, dic, word_list) + \
        getCosine(v1, v2)
        heap = hp.heapAdd([s, f], heap)
    return hp.getRankList(heap)