def merge_sort(l):
    if len(l)>1:
        mid = len(l)//2
        lefthalf = l[:mid]
        righthalf = l[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                l[k]=lefthalf[i]
                i += 1
            else:
                l[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            l[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            l[k]=righthalf[j]
            j=j+1
            k=k+1

x = [3,5,1,6,10,2]
merge_sort(x)
assert x == [1,2,3]
