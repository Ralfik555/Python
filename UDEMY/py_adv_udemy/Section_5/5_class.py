import csv
import types

def exportToFile_Static(path,header,data):
    with open(path,mode="w",newline ='') as file:
        writer = csv.writer(file,delimiter =",",quotechar = '"',quoting = csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)
    print('This is function exportToFile - static method')

def exportToFile_Class(cls, path):
    with open(path, mode="w", newline='') as file:
        writer = csv.writer(file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Brand', 'Model', 'IsOnSale'])
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c.IsOnSale])
    print('This is function exportToFile - class method')

def exportToFile_Instance(self, path):
    with open(path, mode="w", newline='') as file:
        writer = csv.writer(file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Brand', 'Model', 'IsOnSale'])
        writer.writerow([self.brand,self.model,self.IsOnSale])
    print('This is function exportToFile - instance method')

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
            self.isOnSale = newIsOnSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSaleStatus,self.brand))
        else:
            print('Cannot change status IsOnSale, valid only for {}'.format(brandOnSale))

    IsOnSale = property(__GetIsOnSale,__SetIsOnSale,None,'if set to True, the car is available in sale/promo')



car01 = Car('Seat','Ibiza',True,True,True,False)
car02 = Car('Opel','Corsa',True,False,True,True)

print('Static------------------'*4)
exportToFile_Static(r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_5\saved_Employee\export_static.csv',
                    ['Brand','Model', 'IsOnSale'],[car01.brand,car01.model,car01.IsOnSale])

# Car.ExportToFile_Static = exportToFile_Static
# Car.ExportToFile_Static(r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_5\saved_Employee\export_static.csv',
#                     ['Brand','Model', 'IsOnSale'],[car01.brand,car01.model,car01.IsOnSale])

print('Class------------------'*4)
Car.ExportToFile_Class = types.MethodType(exportToFile_Class,Car)
Car.ExportToFile_Class(r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_5\saved_Employee\export_class.csv')

print('Instance------------------'*4)
car01.ExportToFile_Instance = types.MethodType(exportToFile_Instance,car01)
car01.ExportToFile_Instance(path = r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_5\saved_Employee\export_instance.csv')

#sprawdzanie czy metoda istnieje

if hasattr(car01,'ExportToFile_Instance') and callable(car01.ExportToFile_Instance):
    print("The object has ExportToFile_Instance")

if hasattr(car01,'ExportToFile_XYZ') and callable(car01.ExportToFile_XYZ):
    print("The object has ExportToFile_Instance")
else:
    print("Somthing wrong")