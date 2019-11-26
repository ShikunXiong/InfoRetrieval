import M4.conversionTools as ct
import M4.heap as h

def getPath(file_name):
    result = ""
    for i in range(len(file_name)-1):
        result += file_name[i] + '/'
    result += file_name
    return result

def getSetList(l):
    result = []
    for word in l:
        if word not in result:
            result.append(word)
    return result


if __name__ == "__main__":

    # Module 4
    s = "market of prediction"
    # s = input("Your input:\n")
    s = ct.convert(s)
    l_words = s.split(" ")
    dic, files = ct.getIndexData(s)
    rank_list = ct.getScoreRank(set(files), dic, l_words)
    print("Top 10 results:\n")
    for i in range(len(rank_list)):
        part = getPath(rank_list[i][1])
        print(str(i+1) + '. ' + "aleph.gutenberg.org" + part)

    # Module 5
    # s = input("Your input:\n")
    s = "is for the use"
    s = ct.convert(s)
    l_words = s.split(" ")
    inputSetList = getSetList(l_words)
    dic, files = ct.getIndexData(s)
    rank_list = ct.getNewScoreRank(set(files), dic, l_words, inputSetList)
    print("Top 10 results:\n")
    for i in range(len(rank_list)):
        part = getPath(rank_list[i][1])
        print(str(i + 1) + '. ' + "aleph.gutenberg.org" + part)
