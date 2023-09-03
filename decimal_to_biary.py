# little bit optimal
# def deximal_to_binary(number):
#     if number==1:
#         return '1'
#     ans=number%2  
#     return deximal_to_binary(number//2)+str(ans)
# print(deximal_to_binary(233))

# print(int('11011111',2))

#little bit tricky

def dec_to_bin(number,string=""):
    if number==0:
        return string
    string=str(number%2)+string
    return dec_to_bin(number//2,string)
var1=dec_to_bin(10)
print(var1)