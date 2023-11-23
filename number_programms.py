print('#Prime number')
num=eval(input('enter your number'))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
print('prime number' if (count==2) else ('not prime'))


print('#2 reverse a number')
num=eval(input('enter your number'))
res=0
while(num!=0):
    rem=num%10
    res=res*10+rem
    num=num//10
print(res)



print('#3 armstrong number')
num=eval(input('enter your number'))
sum=0
copy=num
p=len(str(num))
while(num!=0):
    rem=num%10
    sum+=rem**p
    num=num//10
print('armstrong' if sum==copy else ('not armstrong'))


print('#3 fabnociss number using iterative')
num=eval(input('enter your number of fabnoccis series'))
n1,n2=0,1
for i in range(num+1):
    if i<2:
        print(i)
    else:
        print(n1+n2)
        n1,n2=n2,n1+n2


print('#4 fabnociss number using recursive function')
def fab(n1,n2,num):
    if num==0:
        return
    print(n1+n2)
    return fab(n1=n2,n2=n1+n2,num=num-1)
num=eval(input('enter number of fabnoccis seeris'))
print(0)
print(1)
fab(n1=0,n2=1,num=num-2)


print('#5 palindrome using iterative')
num=eval(input('enter your number '))
rev=0
copy=num
while num!=0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
print('palindrome' if num==copy else ('not palindrome'))



print('#6 palindrome using recursive')
def pal(rev,num,copy):
    if num==0:
        return 'palindrome' if rev==copy else ('not palindrome')
    return pal(rev=(rev*10)+num%10,num=num//10,copy=copy)
num=eval(input('enter your number '))
print(pal(0,num,num))


print('#7find highest among three numbers')
n1=eval(input('enter number 1'))
n2=eval(input('enter number 2'))
n3=eval(input('enter number 3'))
h=0
for i in [n1,n2,n3]:
    if i>h:
        h=i
print(h)


print('#8check the number is binary or not')
num=eval(input('enter number 1'))
while(num!=0):
    x=num%10
    if x!=0 and x!=1:
        print('not binary number')
        break
    else:
        num=num//10


print('#9 find sum of digits using recursve ')
def re(sum,num):
    if num==0:
        return ('sum of the digits is',sum)
    return re(sum=sum+num%10,num=num//10)
num=eval(input('enter your number'))
print(re(0,num))


print('#10 swap two numbers without using third variable')
n1=eval(input('enter number 1'))
n2=eval(input('enter number 2'))
print('numbers before swapping',n1,n2)
n1,n2=n2,n1
print('swapped numbers= ',n1,n2)


print('#12 swap two numbers using third variable')
n1=eval(input('enter number 1'))
n2=eval(input('enter number 2'))
print('numbers before swapping',n1,n2)
n3=n1
n1,n2=n2,n3
print('swapped numbers= ',n1,n2)


print('#13 print prime factors of a given number')
def prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    return (True if (count==2) else False)

num=eval(input('enter your number'))
for i in range(1,num+1):
    if num%i==0 and prime(i):
        print(i)

print('#14 sum of number without using arthematic ')
n1=eval(input('enter number 1'))
n2=eval(input('enter number 2'))
print(sum([n1,n2]))

print('#15 check num is a perfect num')
n1=int(input('enter your number'))
sum=0
for i in range(1,n1):
    if n1%i==0:
        sum+=i
if sum==n1:
    print('perfect num')
else:
    print('not perfect ')


print('#16 average of givem num')      
numbers = [1, 2, 34, 56, 7, 23, 23, 12, 1, 2, 3, 34, 56]
sumOfNums = 0
count = 0
for number in numbers:
    sumOfNums += number
    count += 1
average = sumOfNums / count
print("The list of numbers is:", numbers)
print("The average of all the numbers is:", average)

print('#17 factorial of given num')
n1=int(input('enter your number'))
res=1
for i in range(1,n1+1):
    res*=i
print(res)


print('#17 factorial of given num')
def fact(res,n):
    if n==0:
        return res
    return fact(res=res*n,n=n-1)
n1=int(input('enter your number'))
print(fact(1,n1))


print('#20 square root of a givn num')
import math
n1=int(input('enter your number'))
print(math.sqrt(n1))


print('#21 convert decimal to binary')
n1=eval(input('enter ypour decimal num'))
rev=0
n=1
while n1!=0:
    rem=n1%2
    rev=rev+rem*n
    n1//=2
    n*=10
print(rev)

