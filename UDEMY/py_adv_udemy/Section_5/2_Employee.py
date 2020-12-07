import pickle
import glob

class Employee:


    listOfEmployees = []
    numberOfEmployees = len(listOfEmployees)
    listOfAbilities = ['wozki widlowe', 'praca na wysokosci','prawo jazdy typu C']

    def extendListOfAbilities(addition_ability):
        if isinstance(addition_ability,list):
            Employee.listOfAbilities.extend(addition_ability)
        else:
            Employee.listOfAbilities.append(addition_ability)

    def __init__(self,name,surname,phone_number,skills = None,rating = None, available = True, approved = False):
        self.name = name
        self.surname = surname
        self.skills = skills if isinstance(skills,list) else [skills]
        self.skills = [i if i in self.listOfAbilities else 'other' for i in self.skills]
        self.phone_number = phone_number
        if rating is None or (isinstance(rating, int) and (0 <= rating <= 10)):
            self.__rating = rating
        else:
            self.__rating = None
        self.available = available
        self.__approved = approved
        Employee.numberOfEmployees += 1
        Employee.listOfEmployees.append(self)

    def __str__(self):
        return 'Name: {} \nSurname {} \nphone number: {} \nskills : {} \nrating: {} \navailable : {} \n{}'\
            .format(self.name,self.surname,self.phone_number,self.skills,self.__rating,self.available,'-'*60)

    def changeAvailability(self):
            self.available = not(self.available)

    def addSkill(self,skill):
        self.skills.append(skill)

    def __getRating(self):
        return self.__rating

    def __setRating(self,newRating):
        if self.__approved == True:
            self.__rating = newRating
            print('New Rating is set for {} {}'.format(self.name,self.surname))
        else:
            print('Cannot set rating for not approved employee {} {}'.format(self.name,self.surname))

    rating = property(__getRating,__setRating,None,'if approved is True, you can change rating')

    def save_to_file(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path,'rb') as f:
            new_employee = pickle.load(f)

        cls.listOfEmployees.append(new_employee)
        cls.numberOfEmployees += 1
        return new_employee

    @staticmethod
    def get_employee_files(catalog):
        return glob.glob(catalog + r'\*.emp')

Employee.extendListOfAbilities(['elektronika','mechanik'])

rafal_kociecki = Employee('Rafal', 'Kociecki','123456789', ['wozki widlowe','elektronika','salto w tyl'],rating = 2,approved=True)
pawel_kaczmar = Employee('Pawel','Kaczmar','99887766',skills='wozki widlowe',rating='bledny rating')

rafal_kociecki.changeAvailability()
rafal_kociecki.addSkill('Prawo jazdy typu C')
#rafal_kociecki._Employee__rating = 5
print('-'*50)
rafal_kociecki.rating = 5
pawel_kaczmar.rating = 4
print(rafal_kociecki.name,rafal_kociecki.rating,pawel_kaczmar.name,pawel_kaczmar.rating)

rafal_kociecki.save_to_file(r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_5\saved_Employee\rafal_kociecki.emp')
pawel_kaczmar.save_to_file(r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_5\saved_Employee\pawel_kaczmar.emp')

new_emp = Employee.read_from_file(r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_5\saved_Employee\rafal_kociecki.emp')

print(Employee.get_employee_files(r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_5\saved_Employee'))

print(Employee.listOfEmployees)
print(Employee.numberOfEmployees)

print(new_emp)