for i in range(10,0,-1):
    print(i)

l = list(range(10))
print(l[-1::-1])

#START LAB
colors = ["red", "orange", "green", "violet", "blue", "yellow"]

def NewColors(number, colors):
    return colors[:number]

for i in range(1,len(colors)+1):
    print(NewColors(i,colors))

definition = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli.'
print(definition[definition.index('(')+1:definition.index(')')])
#END LAB

workdays = [19,20,21,22,23]

enumeratedDays = list(enumerate(workdays))
print(enumeratedDays)
months = ['I','II','III','IV','V','test']

monthsDays = zip(months,workdays)

# for m, wd in monthsDays:
#     print(m, wd)

for pos, (m,wd) in enumerate(monthsDays):
    print('Position: ',pos,'month: ',m,'day; ',wd)

#START LAB

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

'...numer kolejny... - The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... is ...imię i nazwisko lidera...'

for pos, (project, date, leader) in enumerate(zip(projects,dates,leaders)):
    print('{} - The leader of "{}" started {} is {}'.format(pos+1,project,date,leader))
#END LAB

print('---------------------------------------------')

monthDays = dict(zip(months,workdays))
print(monthDays)

for key,value in monthDays.items():
    print(key,value)

#START LAB
banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
amount_coins = [0]*len(banknotes_coins)

dict_denominations = dict(zip(banknotes_coins,amount_coins))

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

print(dict_denominations)

for coin,amount in dict_denominations.items():
    print('Denominate : {} - amount {}'.format(coin,amount))
