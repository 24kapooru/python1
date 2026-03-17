#collection datatype
#list[]
#tuple()
#set{}
#dictionary {key:value} {st_name:xyz}
#to store the data
#student data student records

list=[1,2,3,4,5]
print(list)
print(type(list))

a=(1,2,3,4,5)
print(a)
print(type(a))

set1={2,6,8,9,7,5}
print(set1)
print(type(set1))

dictionary={"name":"unnati","age":19}
print(dictionary)
print(type(dictionary))

#list.reverse
list=[1,2,3,4,5]
list.reverse()
print(list)
print(list.index(3))
print("count of 4=",list.count(4))
list2=[6,4,5,6,7,3,11,2]
list2.sort()
print(list2)

#listfunction
list=[1,2,3,4,5]

list.append(10)
print(list)

list.insert(1,20)
print(list) 

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
