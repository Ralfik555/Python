#START LAB
def show_progress(how_many,character='*'):
    print(character*how_many)

# show_progress(10)
# show_progress(15)
# show_progress(30)
# show_progress(10, '-')
# show_progress(15, '+')

#END LAB

def BuyMe(prefix='Please buy me',what='something nice',*args,**kwargs):
    print(prefix,what)
    print(args)
    print(kwargs)

BuyMe('Please buy me','something','a dog','a phone',shop ='market',color='any')

print('-'*50)

products = ['milk','bread','flakes']
parameters = {'price':'low', 'time':'low'}

BuyMe('Buy me','a newspaper',*products,**parameters)
print('-'*50)
BuyMe(*products,**parameters)
print('-'*50)
BuyMe()
print('-'*30,'LAB','-'*30)
#START LAB
#zad1
def calculate_paint(efficency_ltr_per_m2,*args):
    print(efficency_ltr_per_m2*sum(args))

rooms = [4,5,6]
calculate_paint(2,4,5,6)
calculate_paint(2,*rooms)

#zad2
def log_it(*args):
    with open('log_it','a') as f:
        for arg in args:
            f.write(arg + ' ')
        f.write("\n")

log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')

#END LAB