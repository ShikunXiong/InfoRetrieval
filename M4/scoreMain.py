import M4.conversionTools as ct
import M4.heap as h

if __name__ == "__main__":
    s = "byron's wife and children"
    s = ct.convert(s)
    l_words = s.split(" ")
    dic, files = ct.getIndexData(s)
    rank_list = ct.getScoreRank(set(files), dic, l_words)
    print(rank_list)