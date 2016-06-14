def binary_search(l,item,first_occurence):
    first = 0
    last = len(l)-1
    result = -1
    while first <= last:
        midpoint = (first+last)//2
        if l[midpoint] == item:
            result = midpoint
            if first_occurence == True:
                last = midpoint-1
            else:
                first = midpoint+1
        else:
            if item < l[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return result

def find_occurence(l,item):

    first_occurence = binary_search(l,item,first_occurence=True)
    if first_occurence == -1:
        return 0
    else:
        last_occurence = binary_search(l,item,first_occurence=False)
        count = (last_occurence-first_occurence+1)
        return count

assert find_occurence([1,2,3,3,3,3,4,4,5,5,6,7,8,9,10,11,12],3) == 4
