bri = set(['Бразилия', 'Россия', 'Индия'])
print('Индия' in bri)
    
print('США' in bri)
    
bric = bri.copy()
bric.add('Китай')
print(bric.issuperset(bri))

bri.remove('Россия')
print(bri & bric) # OR bri.intersection(bric)
{'Бразилия', 'Индия'}

A = {1,2,3}
A = set('qwerty')
print (A)

h = set('Hello')
print(h)

a = {1,2,3,5,4,66,54,3,5,6}
b = {1,2,3,3}
print(a==b)
print(len(a))
for nums in a:
    print(nums)
print(1 in a,22 not in a)
a.add(22)
print(1 in a,22 not in a)
a.remove(66)
for nums in a:
    print(nums)