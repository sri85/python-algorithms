def binary_search_first_occurence(l,item):
    first = 0
    last = len(l)-1
    result = -1

    while first <= last:
        midpoint = (first+last)//2
        if  l[midpoint] == item:
            result = l.index(item)
            last = midpoint -1
        else:
            if item < l[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return result

assert binary_search_first_occurence([1,2,3,3,3],3) == 2
assert binary_search_first_occurence([1,2,3,3,3],3) == 2
