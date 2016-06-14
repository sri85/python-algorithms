def circular_array_search(l,item):
    first = 0
    last = len(l)-1
    while first <= last:
        midpoint = (first+last)//2
        if item == l[midpoint]:
            return midpoint
        if l[midpoint] <= l[last]:
            if item > l[midpoint] and item <= l[last]:
                first = midpoint+1
            else:
                last = midpoint -1
        else:
            if l[first] <= item and item < l[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return -1

assert circular_array_search([12,14,18,21,3,6,8,9],14) == 1
