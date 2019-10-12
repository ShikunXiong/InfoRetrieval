import M3.InvertedIndex as ii

if __name__ == "__main__":

    base = "../input-files/aleph.gutenberg.org/1"
    dic = {}
    ii.searchTxt(base, 'z', dic)
    write_path = "../M3/index/z.txt"
    ii.writeIntoFile(write_path, dic)
