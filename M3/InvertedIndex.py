import os


def searchTxt(path, prefix, dic):
    if os.path.isdir(path):
        all_files = os.listdir(path)
        for file_name in all_files:
            if file_name.endswith('.txt') and 'new' in file_name:
                # process .txt file
                n = getFileNum(file_name)
                dic = processEachFile(path + '/' + file_name, n, prefix, dic)
            else:
                # keep searching
                searchTxt(path + '/' + file_name, prefix, dic)
    else:
        return


def getFileNum(file_name):
    """
    Get file num. E.g:'10001.txt' -> '10001'
    :param file_name: String '10001.txt'
    :return: String '10001'
    """
    result = ''
    for i in file_name:
        if i.isdigit():
            result += i
    return result


def processEachFile(path, file_num, prefix, dic):
    f = open(path, mode = 'r', encoding='utf-8-sig', errors='ignore')
    word_count = 0
    for line in f.readlines():
        line = line.strip('\n')
        line = line.strip()
        for word in line.split():
            if len(word) > 1:
                word_count += 1
                if word[0] == prefix:
                    dic.setdefault(word, {})
                    dic[word].setdefault(file_num,[])
                    dic[word][file_num].append(word_count)
    l = sorted(dic.keys())
    a = 1
    return dic

def writeIntoFile(path, dic):
    f = open(path, mode='w', encoding='utf-8', errors='ignore')
    line = ''
    l = sorted(dic.keys())
    for key in l:
        line += key + "\n"
        for num, position_list in dic[key].items():
            line += '\t' + num + ":" + str(len(position_list)) + ":"
            for p in position_list:
                line += str(p) + ","
            line = line.strip(',') + '\n'
        f.write(line + '\n')
        line = ""
    return
