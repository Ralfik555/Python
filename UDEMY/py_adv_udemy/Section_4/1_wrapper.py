import datetime
import functools
import time

def CreateFunctionWithWrapper(func):
    def func_with_wrapper(*args,**kwargs):
        print('Function {} started at {}'.format(func.__name__,datetime.datetime.now().isoformat()))
        print('Following arguments: ')
        print(args,kwargs)
        result = func(*args,**kwargs)
        print('Function returned {}'.format(result))
        return result
    return func_with_wrapper

@CreateFunctionWithWrapper
def ChangeSalary(emp_name,new_salary,is_bonus = False):
    print('Changing salary for {} to {} as bonus={}'.format(emp_name,new_salary,is_bonus))
    return new_salary

#ChangeSalary= CreateFunctionWithWrapper(ChangeSalary)

ChangeSalary('Rafal',10000,is_bonus = True)


#START LAB

def wrapper_time(a_function):
    def a_wrapped_function(*args, **kwargs):
        time_start = time.time()
        v = a_function(*args, **kwargs)
        time_stop = time.time()
        print(">>>>>Function {} executed in {}".format(a_function.__name__, time_stop - time_start))
        return v
    return a_wrapped_function

@wrapper_time
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


print(get_sequence(5))

