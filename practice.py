#Show list of all numbers that are divisible by 3, 5 and 7 between 1 and 1000
'''sum=0
number = int(input("enter any number:"))
for i in range(1,1000):
    if (i%3==0 and i%5==0 and i%7==0):
        print(i)
        sum=sum+i
print(sum)'''
#Find the sum of numbers between 1 and 150
'''sum=0
digit=int(input("enter any number:" ))
for i in range(1,150):
    sum=sum+i
    print(sum)'''
#Prints all numbers between 1 and 1000 that are palindromes
'''digits=int(input("enter any number:"))

for i in range(1,1000):
    if (int(i) == int(i)[::-1]):
        digits = digits+i
        print(digits)'''
'''sum = 0
#i = input("1")
count = 1
while count <= 1000:
    if str(count) == str(count)[::-1]:
        sum = sum + int(count)
    print(sum)
    count += 1'''
#Accept a string and tell me if it is a palindrome or not
'''word = input("enter any word:")
if word == word[::-1]:
    print("word is palindrome")
else:
    print("not palindrome")'''
#Prints all numbers between 1 and 1000 that are palindromes
'''sum=0
for word in range(1 , 1000):
    if word == word[::-1]:
        sum = sum + int(word)
        print("sum")'''
'''sum=" "
count=input("enter number:")
while count <= str(1000):
    if count == count[::-1]:
        print("count")
    count += 1'''
#sum=sum + count
#Print 7s table from 1 to 100
'''num=7
for i in range(1,100):
        print(i*num)'''
'''d = 0
sum = 0
val = 0
for i in range(1,1000):
    sum += int(i)
for num in range(1,1000,-1):
    val += int(num)
    d = sum+val
    if sum == val:
          print(d)'''
#Prints all numbers between 1 and 1000 that are palindromes
'''num = 0
#sum = 0
d = ""
s = str(num)
for i in range(1,1000):
    print(int(i))
    num += i
    for digit in s[::-1]:
        d += digit
        #s=num+d
        #if num == d:
        print(int(digit))
        #d += digit'''
#Accept a number and tell if it is a prime number or not




