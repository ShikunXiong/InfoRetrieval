import M4.conversionTools as ct

if __name__ == "__main__":
    s = "byron's wife and children"
    s = ct.convert(s)
    l_word = s.split(" ")
    d, fs = ct.getIndexData(s)
    r = ct.getCountScore('13147', d, l_word)
    f = ct.getPositionScore('13147', d, l_word)