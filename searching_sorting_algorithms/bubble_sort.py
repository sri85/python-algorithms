from timeit import Timer
def bubble_sort(l):
    for i in xrange(len(l)-1,0,-1):
        for j in xrange(0,i+1):
            if l[j] > l[i]:
                l[j],l[i] = l[i],l[j]
    return l

assert bubble_sort([3,1,2,4]) == [1,2,3,4]
## Time taken by bubble sort
time_taken = Timer("bubble_sort([3,1,2,4])", "from __main__ import bubble_sort")
print("time_taken",time_taken.timeit(number=1000), "milliseconds")
