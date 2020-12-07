brandOnSale = 'Opel'

class Car():

    numberOfCars = 0
    listOfCars =[]

    def __init__(self,brand, model,isAirBagOk,isPaintingOk,isMechanicOk,isOnSale):
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
        return '{} {}, damage = {}'.format(self.brand,self.model,self.IsDamaged())


    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self,newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.isOnSale = newIsOnSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSaleStatus,self.brand))
        else:
            print('Cannot change status IsOnSale, valid only for {}'.format(brandOnSale))

    IsOnSale = property(__GetIsOnSale,__SetIsOnSale,None,'if set to True, the car is available in sale/promo')


class Truck(Car):

    def __init__(self,brand, model,isAirBagOk,isPaintingOk,isMechanicOk,isOnSale,capacityKg):
        super().__init__(brand, model,isAirBagOk,isPaintingOk,isMechanicOk,isOnSale)
        self.capacity = capacityKg

    def __str__(self):
        return super(Truck, self).__str__() + \
               '\nThis is a truck with capacity {} , on Sale = {}'.format(self.capacity,self.IsOnSale)

truck_01 = Truck('Ford','Transit',True,False,True,False,1600)
truck_02 = Truck('Reanult','Trafic',True,True,True,True,1200)

print(truck_01)

