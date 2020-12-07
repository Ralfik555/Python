#eval()

var_x = 10
password = 'secret password'

source = 'var_x  + 2'
result = eval(source)
print(result)


print(globals())
globals = globals().copy()

#del globals['password']

source = 'password'
result = eval(source, globals)
print(result)

#START LAB
import math
import numpy as np
# formula = input("Please insert formula with 'x' argument")
# argument_list = np.linspace(0,10,101)
#
# for x in argument_list:
#     print(eval(formula))
#END LAB

#exec
print('-'*30)
var_x = 10

source = '''
new_var = 1
for i in range(var_x):
    print('-'*i)
    new_var += i
'''
result = exec(source)
print(result)
print(var_x)
print(new_var)

#START LAB
import os
files_to_process = [r"/home/rafal/Desktop/Python_projects/py_adv_udemy/Section_2/LAB/script_1.py",
                    r"/home/rafal/Desktop/Python_projects/py_adv_udemy/Section_2/LAB/script_2.py"]

for script in files_to_process:
    print(os.path.basename(script))
    file = open(script,'r')
    source = file.read()
    exec(source)
#END LAB

#Compile

source = "reportLine += 1"
reportLine = 0

exec(source)

#W cholere szybciej robi sie compiled source
sourceCompiled = compile(source, 'path to file or text, in case of internal variable can be anything', 'exec')
exec(sourceCompiled)
print(reportLine)
print('*'*40)
#START LAB
import math
import time
import numpy as np

formulas_list = ["abs(x**3 - x**0.5)","abs(math.sin(x) * x**2)"]
argument_list = np.linspace(0,100000,1000000)

for source in formulas_list:
    results_list = []
    start = time.time()
    print(source)
    for x in argument_list:
        results_list.append(eval(source))
    print('max = {} and min = {}'.format(max(results_list),min(results_list)))
    stop = time.time()
    print(stop - start)


for source in formulas_list:
    source = compile(source,'internal','eval')
    results_list = []
    start = time.time()
    print(source)
    for x in argument_list:
        results_list.append(eval(source))
    print('max = {} and min = {}'.format(max(results_list),min(results_list)))
    stop = time.time()
    print(stop - start)


#END LAB