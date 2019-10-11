from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import zipProcess as zp
import os

if __name__ == "__main__":
    base = "input-files/aleph.gutenberg.org/1"
    zp.unzipAllZips(base)



    #from_path = r"E:\UCITmp\Info\SWE247P project\input-files\aleph.gutenberg.org\1\0\0\0\10001\10001.zip"
    #to_path = r"E:\UCITmp\Info\SWE247P project\input-files\aleph.gutenberg.org\1\0\0\0\10001"
    #zp.unzip_file(from_path, to_path)