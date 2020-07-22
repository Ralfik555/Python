brandOnSale = 'Opel'

class Car:

    numberOfCars = 0
    listOfCars =[]

    def __init__(self,brand, model,isAirBagOk,isPaintingOk,isMechanicOk, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        self.__isOnSale = isOnSale
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.isAirBagOk and self.isPaintingOk and self.isMechanicOk)

    def __str__(self):
        return '{} {}, damage = {} and isOnSales = {}'.format(self.brand,self.model,self.IsDamaged(),self.__isOnSale)


car01 = Car('Seat','Ibiza',True,True,True,False)
car02 = Car('Opel','Corsa',True,False,True,True)



#ukryty atrybut
car02.__isOnSale = False
#car02._Car__isOnSale = False
car02.YearOfProduction = 2002
del car02.YearOfProduction

setattr(car02,'Taxi',False)
delattr(car02,'Taxi')
print(hasattr(car02,'Taxi'))

print(car01)
print(car02)
print(vars(car02))