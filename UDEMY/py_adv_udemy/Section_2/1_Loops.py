listA = list(range(6))
listB = list(range(6))

product = [(a,b) for a in listA for b in listB]
print(product)

product = [(a,b) for a in listA for b in listB if a%2 == 1 and b%2 == 0]
print(product)

dict_prod = {a:b for a in listA for b in listB if a%2 == 1 and b%2 == 0}
print(dict_prod)


#START LAB
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routs = [(start,stop) for start in ports for stop in ports if start!=stop]
print(len(routs))


routs = [(start,stop) for start in ports for stop in ports if start < stop]
print(len(routs))

#END LAB
gen = ((a,b) for a in listA for b in listB if a%2 == 1 and b%2 == 0)

print(next(gen))
print(next(gen))

print('-'*30)
for x in gen:
    print(x)

print('-'*30)
for x in gen:
    print(x)

print('*'*30)
gen = ((a,b) for a in listA for b in listB if a%2 == 1 and b%2 == 0)

while True:
    try:
        print(next(gen))
    except StopIteration:
        print('All values have been generated')
        break

#START LAB
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

gen_routs = ((start,stop) for start in ports for stop in ports if start < stop)

counter = 0
for x in gen_routs:
    counter += 1
    print(x)
print(counter)

#END LAB
