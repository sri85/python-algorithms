def binary_search(l,item):
        first = 0
        last = len(l)-1

        while first<=last:
            midpoint = (first + last)//2
            if l[midpoint] == item:
                return midpoint
            else:
                if item < l[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1

        return -1

assert binary_search([1,2,6,7,10,11,45,78,89],3) == -1
assert binary_search([1,2,6,7,10,11,45,78,89],45) == 6
