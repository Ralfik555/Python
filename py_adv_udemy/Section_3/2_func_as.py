print('-'*30,'LAB','-'*30)
#START LAB
def double(x):
    return 2 * x
def root(x):
    return x ** 2
def negative(x):
    return -x
def div2(x):
    return x / 2

number = 8
transformation = [double,root,div2,negative]

tmp_number = number
for action in transformation:
    tmp_number = action(tmp_number)
    print('{}: temporal result is {}'.format(action.__name__, tmp_number))
#END LAB

print('-'*30,'LAB','-'*30)
#START LAB
x_table = list(range(11))

def generate_values(function,number):
    results = []
    for num in number:
        results.append(function(num))
    return results

print(generate_values(double, x_table))
print(generate_values(root, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))

#END LAB
print('-'*30,'LAB','-'*30)

def CreateFunction(kind = '+'):
    source = '''
def f(*args):
    result = 0
    for a in args:
        result {}= a
    return result
'''.format(kind)
    exec(source,globals())
    return f

f_add = CreateFunction('+')
print(f_add(4,5,6))
f_subs = CreateFunction('-')
print(f_subs(4,5,6))


print('-'*30,'LAB','-'*30)
#START LAB

from datetime import datetime

def CreateDiffTime(span):
    if span == 'm':
        sec = 60
    elif span == 'h':
        sec = 3600
    elif span =='d':
        sec = 86400

    source = '''
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]'''.format(sec)
    exec(source,globals())
    return f



start = datetime(2019, 1, 1, 0, 0, 0)
end = datetime.now()

time_span_m = CreateDiffTime('m')
time_span_h = CreateDiffTime('h')
time_span_d = CreateDiffTime('d')

print(time_span_m(start, end))
print(time_span_h(start, end))
print(time_span_d(start, end))

#END LAB
print('-'*30,'LAB','-'*30)