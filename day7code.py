""" #coding question 1(set logic)
def security_key(number):
    visible=set()
    repeatednumber=0
    for ch in str(number):
        if ch in visible:
            repeatednumber+=1
        else:
            visible.add(ch)
    return repeatednumber if repeatednumber>0 else -1
number=int(input("Enter the data:"))
result=security_key(number)
print(result) """

#freq
def security_key(number):
    s=str(number)
    frequency={}
    for ch in s:
        frequency[ch]=frequency.get(ch,0)+1
    repeatednumber=0
    for i in frequency.values():
        if i>1:
            repeatednumber+=(i-1)
    return repeatednumber if repeatednumber>0 else -1
number=int(input("Enter the data:"))
result=security_key(number)
print(result)

#odd even online game
n = int(input("Enter size: "))
nums = list(map(int, input("Enter elements: ").split()))

even = []
odd = []

for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

result = even + odd

print(*result)