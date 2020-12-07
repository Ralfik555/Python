class Employee:

    listOfEmployees = []
    numberOfEmployees = len(listOfEmployees)
    listOfAbilities = ['wozki widlowe', 'praca na wysokosci','prawo jazdy typu C','sprzedaz','zarzadzanie']

    @classmethod
    def extendListOfAbilities(cls,addition_ability):
        if isinstance(addition_ability,list):
            cls.listOfAbilities.extend(addition_ability)
        else:
            cls.listOfAbilities.append(addition_ability)

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
            print("Rating has to be integer between 1 - 10")
        self.available = available
        self.__approved = approved
        Employee.numberOfEmployees += 1
        Employee.listOfEmployees.append(self)

    def __str__(self):
        return 'Name: {} \nSurname {} \nphone number: {} \nskills : {} \nrating: {} \navailable : {} \n{}'\
            .format(self.name,self.surname,self.phone_number,self.skills,self.__rating,self.available,'-'*60)

    def __iadd__(self, other):
        if type(other) is list:
            skills = self.skills
            skills.extend(other)
            return Employee(self.name,self.surname,self.phone_number,skills,self.rating,
                            self.available,self.__approved)
        elif type(other) is str:
            skills = self.skills
            skills.append(other)
            return Employee(self.name,self.surname,self.phone_number,skills,self.rating,
                            self.available,self.__approved)
        else:
            raise Exception('Adding type {} to Car is not implemented'.format(type(other)))

    def changeAvailability(self):
            self.available = not(self.available)

    # def addSkill(self,skill):
    #     self.skills.append(skill)


    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self,newRating):
        if self.__approved == True:
            self.__rating = newRating
            print('New Rating = {} is set for {} {}'.format(self.rating,self.name,self.surname))
        else:
            print('Cannot set rating for not approved employee {} {}'.format(self.name,self.surname))

    @rating.deleter
    def rating(self):
        self.__rating = None


Employee.extendListOfAbilities(['elektronika','mechanik'])

rafal_kociecki = Employee('Rafal', 'Kociecki','123456789', ['wozki widlowe','elektronika','salto w tyl'],rating = 2,approved=True)
pawel_kaczmar = Employee('Pawel','Kaczmar','99887766',skills='wozki widlowe',rating='bledny rating')

rafal_kociecki.changeAvailability()


print(rafal_kociecki.rating)
rafal_kociecki.rating = 7
del rafal_kociecki.rating
print(rafal_kociecki.rating)

rafal_kociecki += ['sprzedaz','zarzadzanie']
print(rafal_kociecki.skills)
