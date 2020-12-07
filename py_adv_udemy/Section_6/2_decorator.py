import random

class MemoryClass:
    list_of_already_selected = []

    def __init__(self,funct):
        print('This is an init of MemoryClass',funct)
        self.funct = funct

    def __call__(self, list):
        print('This is a call of MemoryClass instance')
        items_not_selected = [i for i in list if i not in MemoryClass.list_of_already_selected]
        print('items to select :',items_not_selected)
        item = self.funct(items_not_selected)
        MemoryClass.list_of_already_selected.append(item)
        return item

cars = ['Opel','Toyota','Fiat','Ford','Renault','Mercedes','BMW','Peugeot','Porshe','Audi','VW','Mazda']

@MemoryClass
def SelectedTodayPromotion(list_of_cars):
    return random.choice(list_of_cars)

@MemoryClass
def SelectedTodayShow(list_of_cars):
    return random.choice(list_of_cars)

@MemoryClass
def SelectedTodayFreeAccessories(list_of_cars):
    return random.choice(list_of_cars)

print('#'*50)
print(SelectedTodayPromotion(cars))
print('#'*50)
print(SelectedTodayShow(cars))
print('#'*50)
print(SelectedTodayFreeAccessories(cars))
print('#'*50)
print(SelectedTodayPromotion(cars))
print('#'*50)
print(SelectedTodayShow(cars))
print('#'*50)
print(SelectedTodayFreeAccessories(cars))
