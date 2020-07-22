class Car:

    numberOfCars = 0
    listOfCars =[]

    def __init__(self,brand, model,isAirBagOk,isPaintingOk,isMechanicOk):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.isAirBagOk and self.isPaintingOk and self.isMechanicOk)

    def __str__(self):
        return '{} {}'.format(self.brand,self.model)


car01 = Car('Seat','Ibiza',True,True,True)
car02 = Car('Opel','Corsa',True,False,True)

print('Check if object belongs to class', isinstance(car01,Car))
print('Check if object belongs to class', type(car01) is Car)
print('Check if object belongs to class', car01.__class__)
print('OTHER METHODS')
print(vars(car01))
print(vars(Car))
print(dir(car01))
print(dir(Car))

print('#'*50)

print(car01.listOfCars)
print(car01.numberOfCars)
print(Car.listOfCars)
print(Car.numberOfCars)