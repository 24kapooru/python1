#if else 
n=int(input())
if n%2!=0:
    print("Weird")
    exit()
if 2<=n<=5:
    print("Not Weird")
elif 6<=n<=20:
    print("Weird")
else:
    print("Not Weird")

#leap year
def is_leap(year):
    leap = False
    if year % 400==0:
        return True
    if year %100==0:
        return False
    if year %4==0:
        return True
    return leap

year = int(input())
print(is_leap(year))

