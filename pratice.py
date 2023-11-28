'''
string='praveen is a good boy'

1. 'boy good is a praveen'
2. 'neevarp si a doog yob'
3. 'yob doog si a neevarp'
'''
s='praveen is a good boy '
s=s.split()
print((' ').join(s[::-1]))


s='praveen is a good boy '
s=s.split()
s1=''
for ch in s:
    s1+=ch[::-1]+' '
print(s1)


s='praveen is a good boy '
s=s.split()
s=s[::-1]
s1=''
for ch in s:
    s1+=ch[::-1]+' '
print(s1)
import keyword
print(keyword.kwlist)