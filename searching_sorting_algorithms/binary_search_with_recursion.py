def binary_search_with_recursion(l,item):
    if len(l) == 0:
        return False
    else:
        midpoint = len(l)//2
        if l[midpoint] == item:
            return True
        if item < l[midpoint]:
            return binary_search_with_recursion(l[:midpoint],item)
        else:
            return binary_search_with_recursion(l[midpoint+1:],item)

assert binary_search_with_recursion([1,2,6,7,10,11,45,78,89],3) == False
assert  binary_search_with_recursion([1,2,6,7,10,11,45,78,89],45) == True
assert binary_search_with_recursion([],1) == False
