# def is_pallindrome(string1,index=0):
#     if string1[index]!=string1[len(string1)-1-index]:
#         return False
#     if index>len(string1)//2:
#         return True
#     return is_pallindrome(string1,index+1)

#can u do with using index variable?
# def is_pallindrome(string1):
#     if len(string1)==1 or len(string1)==0:#0 is for even case and 1 for odd case
#         return True
#     if string1[0]!=string1[len(string1)-1]:
#         return False
#     return is_pallindrome(string1[1:len(string1)-1])
# print(is_pallindrome("111111111"))

#short life hack for converting from binary to decimal
# print(int('1010',2))

