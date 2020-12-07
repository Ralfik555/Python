class Car:

    def __init__(self,brand, model,isAirBagOk,isPaintingOk,isMechanicOk,accessories):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        self.accessories = accessories

    def IsDamaged(self):
        return not (self.isAirBagOk and self.isPaintingOk and self.isMechanicOk)

    def __str__(self):
        return '{} {}, damage = {} with accessories = {}'.format(self.brand,self.model,self.IsDamaged(),self.accessories)

    def __iadd__(self, other):
        if type(other) is list:
            accessories = self.accessories
            accessories.extend(other)
            return Car(self.brand,self.model,self.isAirBagOk,self.isPaintingOk,self.isMechanicOk,
                       accessories)
        elif type(other) is str:
            accessories = self.accessories
            accessories.append(other)
            return Car(self.brand, self.model, self.isAirBagOk, self.isPaintingOk, self.isMechanicOk,
                           accessories)
        else:
            raise Exception('Adding type {} to Car is not implemented'.format(type(other)))

    def __add__(self, other):
        if type(other) is Car:
            return [self,other]
        else:
            raise Exception('Adding type {} to Car is not implemented'.format(type(other)))

car01 = Car('Seat','Ibiza',True,True,True,['winter tires'])
print(car01)

car01 += ['navigation system','roof rack']
print(car01)

car01 += 'loudspeeker system'
print(car01)
#car01 += 9

car02 = Car('Opel','Corsa',True,False,True,[])

car_pack = car01 + car02
print('car01 + car02 = ',car_pack[0],car_pack[1])

for car in car_pack:
    print(car)