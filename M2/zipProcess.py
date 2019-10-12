import os
import zipfile
from M2 import convert as c


def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')


def unzipAllZips(path):
    """
    Unzip all the zip files
    The original relative path in this project should be
    "input-files/aleph.gutenberg.org/1"
    :param path: relative_path
    :return: None
    """
    if os.path.isdir(path):
        all_files = os.listdir(path)
        for file_name in all_files:
            bool_zip = zipfile.is_zipfile(path + '/' + file_name)
            if bool_zip:
                # unzip zip file
                unzip_file(path + '/' + file_name, path)
            else:
                # keep searching
                unzipAllZips(path + '/' + file_name)
    else:
        return


def transformTxt(path):
    if os.path.isdir(path):
        all_files = os.listdir(path)
        for file_name in all_files:
            if file_name.endswith('.txt'):
                # process .txt file
                c.writeNew(path + '/' + file_name)
            else:
                # keep searching
                transformTxt(path + '/' + file_name)
    else:
        return
