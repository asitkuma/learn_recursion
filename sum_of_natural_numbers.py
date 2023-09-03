def sum_of_natural_numbers(number):
    if number ==0:
        return 0
    return number+sum_of_natural_numbers(number-1)
print(sum_of_natural_numbers(3))


#quiz what will be the ans:--
# def sum_of_natural_numbers(number):
#     if number ==0:
#         return 0
#     return number+sum_of_natural_numbers(number-1)+1
# print(sum_of_natural_numbers(3))

#quiz 2 what will be the ans:--
# def sum_of_natural_numbers(number):
#     if number ==1:
#         return 1
#     return number+sum_of_natural_numbers(number-1)
# print(sum_of_natural_numbers(3))

