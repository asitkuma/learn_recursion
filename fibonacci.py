# def fibbo(number):
#     if number<=2:
#         return 1
#     return fibbo(number-1)+fibbo(number-2)
# print(fibbo(130))

#optimize by using sc at max tc O(n-2) and sc-O(n*n)
def fibbo2(number,map={}):
    if number in map:
        return map[number]
    if number<=2:
        return 1
    map[number]=fibbo2(number-1,map)+fibbo2(number-2,map)
    return map[number]
print(fibbo2(100))