n1=eval(input('enter ypour decimal num'))
rev=0
n=1
while n1!=0:
    rem=n1%2
    rev=rev+rem*n
    n1//=2
    n*=10
print(rev)