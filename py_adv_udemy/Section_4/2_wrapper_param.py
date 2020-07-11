import datetime
import functools
import time

#logFilePath = r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_4\changeSalary_log'

def CreateFunctionWithWrapper_LogToFile(logFilePath):
    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args,**kwargs):
            file = open(logFilePath,"a")
            file.write('-'*20 + "\n")
            file.write("Function {} started at {} \n".format(func.__name__,datetime.datetime.now()))
            file.write('Following arguments were used : \n')
            file.write(" ".join("{}".format(x) for x in args))
            file.write("\n")
            file.write(" ".join("{}={}".format(k,v) for (k,v) in kwargs.items()))
            file.write("\n")
            result = func(*args,**kwargs)
            print('Function returned {}'.format(result))
            return result
        return func_with_wrapper
    return CreateFunctionWithWrapper

@CreateFunctionWithWrapper_LogToFile(r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_4\changeSalary_log')
def ChangeSalary(emp_name,new_salary,is_bonus = False):
    print('Changing salary for {} to {} as bonus={}'.format(emp_name,new_salary,is_bonus))
    return new_salary

@CreateFunctionWithWrapper_LogToFile(r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_4\changePosition_log')
def ChangePosition(emp_name,new_position):
    print('Employee {} was transferred to new position {}'.format(emp_name,new_position))
    return new_position


ChangeSalary('Rafal',10000,is_bonus = True)
ChangePosition('Rafal','DevPython')
ChangeSalary('Ania',5000,True)
ChangePosition('Ania','Manager')

#START LAB
import os

def Wrapper_LogToFile(logFilePath):
    def Wrapper(func):
        def func_with_wrapper(path):
            file = open(logFilePath,"a")
            file.write('-'*20 + "\n")
            file.write(r"Action {} executed on {} on {} ".format(func.__name__,path,datetime.datetime.now()))
            file.write('-'*20 + "\n")
            return func(path)
        return func_with_wrapper
    return Wrapper

@Wrapper_LogToFile(r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_4\file_created')
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")

@Wrapper_LogToFile(r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_4\file_deleted')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_4\dummy_file')
delete_file(r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_4\dummy_file')
create_file(r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_4\dummy_file')
delete_file(r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_4\dummy_file')

#END LAB