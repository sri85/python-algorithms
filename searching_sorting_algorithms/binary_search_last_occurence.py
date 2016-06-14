def binary_search_last_occurence(l,item):
    first = 0
    last = len(l)-1
    result = -1

    while first <= last:
        midpoint = (first+last)//2
        if  l[midpoint] == item:
            result = midpoint
            first = midpoint +1
        else:
            if item < l[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return result

print binary_search_last_occurence([1,2,3,3,3],3)
