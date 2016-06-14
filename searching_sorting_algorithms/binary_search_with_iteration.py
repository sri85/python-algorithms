def binary_search(l,item):
    first = 0
    last = len(l)-1

    while first < = last:
        midpoint = (first+last)//2
        if l[midpoint] == item:
            return l.index(item)
        else:
            if l[midpoint] < item:
                last = l[midpoint]-1
            else:
                first = l[midpoint]+1
    return -1
