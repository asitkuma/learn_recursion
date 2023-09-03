from tkinter import RIDGE


def find_an_element(l1,left,right,target):
    mid=(left+right)//2
    if l1[mid]==target:
        return mid
    if l1[mid]>target:
        return find_an_element(l1,left,mid-1,target)
    else:
        return find_an_element(l1,mid+1,right,target)
l1=[1,2,3,4,5,6,7,8,9,10]
print(find_an_element(l1,0,len(l1)-1,10))
