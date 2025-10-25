#rotate list by k pos

def rotate_list(lst, k):
        k = k % len(lst)
        return lst[-k:] + lst[:-k]

#calling
lst=[1,2,3,4,5]
lst=rotate_list(lst,2)
print("Res : ",lst)
