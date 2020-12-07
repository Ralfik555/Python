f = lambda x:x*2

f = lambda x,y:x**y
print(f(5,3))

list_numbers = [1,2,3,4,11,14,15,20,21]

def is_odd(x):
    return x%2 != 0

filtered_list = list(filter(is_odd,list_numbers))
print(filtered_list)

filtered_list = list(filter(lambda x:x%2 != 0,list_numbers))
print(filtered_list)

def generate_multiply_funciton(n):
    return lambda x:n*x

mul_2 = generate_multiply_funciton(2)
mul_3 = generate_multiply_funciton(3)

print(mul_2(5),mul_3(15))

print('-'*30,'LAB','-'*30)
#Start Lab

text_list = ['x','xxx','xxxxx','xxxxxxx','']

f = lambda x:len(x)

print(list(map(f,text_list)))
print(list(map(lambda x:len(x),text_list)))
#End Lab
