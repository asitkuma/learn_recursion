def recur(number=5):
    if number==0:
        return
    recur(number-1)
    print(number)#it will print 1,2,3,4,5
recur()