def reverse_string(str1="asit",index=0):
    if index==len(str1):#if u give len(str1)-1 then the last character will not printed in the screen
        return
    reverse_string(str1,index+1)
    print(str1[index],end="")




def reverse(str1="asit"):
    if str1=="":
        return ""
    return reverse(str1[1:])+str1[0]
print(reverse())