from M2 import zipProcess as zp

if __name__ == "__main__":
    """
    # Unzip all files 
    base = "../input-files/aleph.gutenberg.org/1"
    zp.unzipAllZips(base)
    """

    # Transform .txt files
    base = "../input-files/aleph.gutenberg.org/1"
    zp.transformTxt(base)


    # error_encode = [
    #     "input-files/aleph.gutenberg.org/1/0/0/5/10057/10057/10057.txt",
    #     "input-files/aleph.gutenberg.org/1/0/0/5/10058/10058/10058.txt",
    #     "input-files/aleph.gutenberg.org/1/0/0/5/10059/10059.txt",
    #     "input-files/aleph.gutenberg.org/1/0/0/6/10063/10063.txt",
    #     "input-files/aleph.gutenberg.org/1/0/1/1/10116/10116.txt",
    #     "input-files/aleph.gutenberg.org/1/0/3/2/10323/10323.txt",
    #     "input-files/aleph.gutenberg.org/1/0/3/2/10324/10324/10324.txt",
    #     "input-files/aleph.gutenberg.org/1/0/3/6/10368/10368/10368.txt",
    #     "input-files/aleph.gutenberg.org/1/0/3/7/10370/10370/10370.txt",
    #     "input-files/aleph.gutenberg.org/1/0/4/0/10403/10403.txt",
    #     "input-files/aleph.gutenberg.org/1/0/5/5/10555/10555.txt",
    #     "input-files/aleph.gutenberg.org/1/0/5/9/10599/10599/10599.txt",
    #     "input-files/aleph.gutenberg.org/1/0/7/3/10733/10733.txt",
    #     "input-files/aleph.gutenberg.org/1/0/7/4/10747/10747/10747.txt",
    #     "input-files/aleph.gutenberg.org/1/0/8/0/10805/10805/10805.txt",
    #     "input-files/aleph.gutenberg.org/1/0/9/0/10905/10905.txt",
    #     "input-files/aleph.gutenberg.org/1/0/9/6/10966/10966.txt",
    #     "input-files/aleph.gutenberg.org/1/1/0/0/11003/11003.txt",
    #     "input-files/aleph.gutenberg.org/1/1/0/0/11005/11005.txt",
    #     "input-files/aleph.gutenberg.org/1/1/0/0/11006/11006.txt",
    #     "input-files/aleph.gutenberg.org/1/1/0/6/11066/11066.txt",
    #     "input-files/aleph.gutenberg.org/1/1/0/6/11067/11067.txt",
    #     "input-files/aleph.gutenberg.org/1/1/0/7/11074/11074.txt",
    #     "input-files/aleph.gutenberg.org/1/2/3/7/12376/12376.txt"
    # ]
    # for p in error_encode:
    #     c.writeNew(p)




