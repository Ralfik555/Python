dayType = 2

weekend = 1
workday = 2
holiday = 3

dayDescritpion = 'weekend' if dayType == 1 else '?'
print(dayDescritpion)

dayDescritpion = 'weekend' if dayType == 1 else 'workday' if dayType == 2 else 'holiday'
print(dayDescritpion)

#START LAB5
price = 123
bonus = 23
bonus_granted = True

price = price - bonus if bonus_granted else price
print(price)
print('----------------------------------------')

rating = 5
print('very good') if rating == 5 else print('good') if rating == 4 else print('weak')
print('----------------------------------------')

import datetime as dt

today_weekday = dt.date.today().strftime("%A")
print(today_weekday)
print('----------------------------------')
print()

#END LAB5

#START LAB6
import os
import urllib.request

data_dir = '/home/rafal/Desktop/Python_projects/py_adv_udemy/Section_1/LAB6/'
pages = [
    { 'name': 'mobilo','url': 'http://www.mobilo24.eu/'},
    { 'name': 'nonexistent','url': 'http://abc.cde.fgh.ijk.pl/' },
    { 'name': 'kursy','url': 'http://www.kursyonline24.eu/'}]


for page in pages:
    file_name = page['name'] + '.html'
    path = os.path.join(data_dir,file_name)
    try:
        urllib.request.urlretrieve(page['url'],path)
        print('page saved')
    except:
        print('Error during retriving the page')
#        break
# else:
#     print('All pages downloaded successfully')

#END LAB6