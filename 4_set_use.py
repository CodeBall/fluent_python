from unicodedata import name

l = ['ABC', 'abc', 'ABC', 'def']
print(set(l))

l1 = {'ABC', 'AYU'}
l2 = {'ABC', 'DEF', 'abc', 'XYZ'}
print(l1 & l2)
print(l1 - l2)

# 集合推导
l3 = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
l4 = {name(chr(i)) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(l3)
print(l4)
