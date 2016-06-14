# P.S: This works only if the list has no duplicates
def find_rotations(l):
    first = 0
    last = len(l)-1
    list_length = len(l)
    while first <= last:
        if l[first] <= l[last]: # Case1
            return first
        midpoint = (first+last)//2
        next_element = (midpoint+1)%list_length
        previous_element = (midpoint+list_length-1)%list_length
        if (l[midpoint] <= l[next_element]) and (l[midpoint] <= l[midpoint]):
            return midpoint
        elif  l[midpoint] <= l[last]:
            last = midpoint-1
        elif l[midpoint] >= l[first]:
            first = midpoint+1
    return -1

assert find_rotations([15,22,23,28,31,38,5,6,8,10,12]) == 6
