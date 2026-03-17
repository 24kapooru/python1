#pseudocode
def linear_search(list,target):
    for i in range(len(list)):
        if list [i]==target:
            return i
    return -1
list=[10,20,30,40,50]
target= int(input("Enter any number:"))
index=linear_search(list,target)
print("Element found at index:", index)

# code2
def linear_search(list,target):
    i=0
    while i<len(list):
        if list[i]==target:
            return i
        i+=1
    return -1
list=[10,20,30,40,50]
target= int(input("Enter any number:"))
index=linear_search(list,target)
print("Element found at index:", index)

#code3
list=[10,20,30,40,50]
target= int(input("Enter the target:"))

found= False
index= -1

for i in range(len(list)):
    if list[i] == target:
        found=True
        index= i
        break
if found:
    print("Element found at index:", index)
else:
    print("Not found")

#binary
def binary_search(list,target):
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)//2
        if  list[mid]==target:
            return mid
        elif list[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1           