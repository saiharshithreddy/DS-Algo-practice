'''
Udemy OA question
# Win probability

'''


'''
Approach: Sort and two pointers
Test cases passed 18/25

'''
def func(x,y):
    x.sort()
    y.sort()
    num = 0
    ptr1 = len(x)-1
    ptr2 = len(y)-1
    while ptr1 > -1:

        if x[ptr1] > y[ptr2]:
            num += ptr2 + 1
            ptr1 -= 1
            ptr2=len(y)-1
        else:
            ptr2 -= 1
        if ptr2==-1:
            ptr1-=1
            ptr2=len(y)-1

    return num / ((len(x)*len(y)))
