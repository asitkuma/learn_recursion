
def merge(l1,low,mid,high):
    #i have two sorted array now i have to merge it
    temp=[]
    dummy=low
    right=mid+1
    while low<=mid and right<=high:
        if l1[low]<=l1[right]:
            temp.append(l1[low])
            low+=1
        else:
            temp.append(l1[right])
            right+=1
    #it means something reamain whd which is very obvious it whill be sorted
    while low<=mid:
        temp.append(l1[low])
        low+=1
    while right<=high:
        temp.append(l1[right])
        right+=1
    count=0
    for i in range(dummy,high+1):
        l1[i]=temp[count]
        count+=1    
def mergesort(l1,low,high):
    #whole idea is that to split into equal halves and merge in a sorted manner
    if low==high:#only 1 element ledt for first changes and whch is sorted
        return
    mid=(low+high)//2
    mergesort(l1,low,mid)
    mergesort(l1,mid+1,high)
    merge(l1,low,mid,high)
l1=[3,2,1]
mergesort(l1,0,len(l1)-1)
print(l1)