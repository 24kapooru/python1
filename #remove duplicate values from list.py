#remove duplicate values from list
num=[1,2,3,1,1,2,2,3,4,4]
data=[]
for i in num:
    if i not in num:
        data.append(i)
print("Actual list:",num)
print("after removing duplicate:",data)

#find second largest number
number=[12,56,78,89,65,71]
maximum=second_largest=float('-inf')
for i  in number:
    if i>maximum:
        second_largest=maximum
        maximum=i
    elif i>second_largest and i!=maximum:
        second_largest=i
print("swecond largest value:",second_largest)

