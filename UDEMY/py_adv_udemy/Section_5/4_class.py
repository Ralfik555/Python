brandOnSale = 'Opel'

class Car:

    def __init__(self,brand, model,isAirBagOk,isPaintingOk,isMechanicOk, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        self.__isOnSale = isOnSale

    @property
    def IsOnSale(self):
        return self.__isOnSale

    @IsOnSale.setter
    def IsOnSale(self,newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSaleStatus,self.brand))
        else:
            print('Cannot change status IsOnSale, valid only for {}'.format(brandOnSale))

    @IsOnSale.deleter
    def IsOnSale(self):
        self.__isOnSale = None


car01 = Car('Seat','Ibiza',True,True,True,False)

print(car01.IsOnSale)
car01.IsOnSale = True

del car01.IsOnSale
print(car01.IsOnSale)