from timeit import Timer
def insertion_sort(l):
    for index in range(1,len(l)):
     currentvalue = l[index]
     position = index

     while position>0 and l[position-1]>currentvalue:
         l[position]=l[position-1]
         position = position-1

     l[position]=currentvalue

x = [3,5,1,10]
insertion_sort(x)
assert x == [1,3,5,10]
time_taken = Timer("insertion_sort([3,5,1,10])", "from __main__ import insertion_sort")
print("time_taken",time_taken.timeit(number=1000), "milliseconds")
