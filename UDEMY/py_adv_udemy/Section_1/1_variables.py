myVar1 = 'Hello'
myVar2 = myVar1 + '!!'
print("are the same ?",myVar1 == myVar2,myVar1 is myVar2)
print(id(myVar1),id(myVar2))

myVar2 = myVar2[:-2]
print("are the same ?",myVar1 == myVar2,myVar1 is myVar2)
print(id(myVar1),id(myVar2))

#Start LAB 1
a = b = c = 10
a = 20
print(a,id(a),b,id(b),c,id(c))
print("----------------------------------")
a = b = c = [1,2,3]
print(a,id(a),b,id(b),c,id(c))
a.append(4)
print(a,id(a),b,id(b),c,id(c))
print("----------------------------------")
x = 10
y = 10
print(id(x),id(y))
y = y + 1 - 1
print(id(x),id(y))
#moglyby sie zmienic ID w innym IDE , ten sobie po prostu poradzil
y = y + 123456789 - 123456789
print(id(x),id(y))
print("----------------------------------")
#End LAB 1
number = 10
print(number,id(number))
number+=2
print(number,id(number))
print("INMUTABLE")
text = 'Africa'
print(text,id(text))
text += ' is hot'
print(text,id(text))
print("MUTABLE")
l1 = [1,2,3]
print(l1,id(l1))
l1.append(4)
print(l1,id(l1))
#common error - instead of create the same variable, we need to create copy, other way it will assign to the same space in memory
l2 = l1
print(l2,id(l2))
l2.append(5)
print(l2,id(l2))
#Copy
print('Copy')
l3 = l1.copy()
l3.append(6)
print(l1,id(l1))
print(l3,id(l3))


#START LAB2
print('LAB2')
days = ['mon', 'tue ','wed','thu','fri','sat','sun']
workdays = days.copy()
workdays.remove('sat')
workdays.remove('sun')
print(days,workdays)
print(id(days),id(workdays))

