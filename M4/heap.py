def heapify(i, l):
    """
    l = [[arg1, arg2], [arg1, arg2]...]
    :param i:
    :param l:
    :return:
    """
    left = 2*i + 1
    right = 2*i + 2
    size = len(l)
    min_num = i
    if 0 < left < size and l[left][0] < l[min_num][0]:
        min_num = left
    if 0< right < size and l[right][0] < l[min_num][0]:
        min_num = right
    if min_num != i:
        l[i], l[min_num] = l[min_num], l[i]
        heapify(min_num, l)


def heapAdd(item, l):
    if len(l) < 10 and item not in l:
        l.append(item)
        if len(l) == 10:
            for i in range(len(l)-1, -1, -1):
                heapify(i, l)
    else:
        if item[0] > l[0][0]:
            l[0] = item
        heapify(0, l)
        a = 1
    return l


def getRankList(l):
    l = sorted(l, key=(lambda x: x[0]), reverse=True)
    return l
