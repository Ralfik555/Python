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

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self,newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSaleStatus,self.brand))
        else:
            print('Cannot change status IsOnSale, valid only for {}'.format(brandOnSale))

    IsOnSale = property(__GetIsOnSale,__SetIsOnSale,None,'if set to True, the car is available in sale/promo')

    @classmethod
    def ReadFromText(cls,aText):
        aNewCar = cls(*aText.split(':'))
        return aNewCar

    @staticmethod
    def Convert_KM_KW(KM):
        return KM*0.735

    @staticmethod
    def Convert_KW_KM(KW):
        return KW*1.36


car01 = Car('Seat','Ibiza',True,True,True,False)
car02 = Car('Opel','Corsa',True,False,True,True)

# print('Status of cars',car01.GetIsOnSale(),car02.GetIsOnSale())
# car01.SetIsOnSale(True)
# car02.SetIsOnSale(False)
# print('Status of cars',car01.GetIsOnSale(),car02.GetIsOnSale())

print('PROPERTY Usage')

car01.IsOnSale = True
car02.IsOnSale = True
print('Status of cars',car01.IsOnSale,car02.IsOnSale)

lineOfText = 'Renault:Megane:True:True:False:False'

#Problem - True i False niestety sa jako string
car03 = Car.ReadFromText(lineOfText)
print(car03)
print(Car.Convert_KM_KW(100))
print(Car.Convert_KW_KM(50))