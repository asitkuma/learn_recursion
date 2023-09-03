def recur(number=5):
    if number==1:
        return 1
    return 1+recur(number-1)
print(recur())