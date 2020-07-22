matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose1 = [[row[i] for row in matrix] for i in range(2)]
transpose2 = [row[i] for row in matrix for i in range(2)]
print(matrix)
print(transpose1)
print(transpose2)

List1 = ['wozki widlowe', 'praca na wysokosci','prawo jazdy typu C']
List2 = ['wozki widlowe','other','praca na wysokosci']


print([i for i in List2 if i in List1])

List1.extend(List2)
print('-'*50)
print(List1)

# [f(x) if condition else g(x) for x in sequence]
# [f(x) for x in sequence if condition]
#

print('#'*60)
skill = 'wozki widlowe'
skill = [skill]
for i in skill:
    print(i)

lineOfText = 'Renault:Megane:True:True:False:False'

print(*lineOfText.split(':'))