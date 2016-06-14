def selection_sort(l):
   for i in range(len(l)-1,0,-1):
       max_position=0
       for j in range(1,i+1):
           if l[j]>l[max_position]:
               max_position = j
       l[i], l[max_position] = l[max_position],l[i]
   return l

assert selection_sort([3,2,4,1,5]) == [1,2,3,4,5]
