"""binary time complexity is log n"""
list = list(range(1, 101))
item=int(input("what is the number you want to search in the list\n"))
low=0
high=len(list)-1
count=0
while low<=high:
    count=count+1
    mid=(low+high)//2
    if item==list[mid]:
        print(f"item has been found in {count} steps")
        break
    elif item>list[mid]:
        low=mid+1
    else:
        high=mid-1
        
        