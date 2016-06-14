from timeit import Timer
def selection_sort(l):
   for i in xrange(len(l)-1,0,-1):
       max_position=0
       for j in xrange(1,i+1):
           if l[j]>l[max_position]:
               max_position = j
       l[i], l[max_position] = l[max_position],l[i]
   return l

assert selection_sort([3,2,4,1,5]) == [1,2,3,4,5]
time_taken = Timer("selection_sort([3,1,2,4])", "from __main__ import selection_sort")
print("time_taken",time_taken.timeit(number=1000), "milliseconds")
