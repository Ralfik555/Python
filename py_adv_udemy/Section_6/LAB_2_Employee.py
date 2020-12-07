class Employee(object):

    listOfEmployees = []
    numberOfEmployees = len(listOfEmployees)
    listOfAbilities = ['wozki widlowe', 'praca na wysokosci','prawo jazdy typu C']

    def __init__(self,name,surname,phone_number,skills = None,rating = None, available = True, approved = False):
        self.name = name
        self.surname = surname

        if skills is None:
            self.skills = skills
        elif isinstance(skills,list):
            self.skills = skills
            self.skills = [i if i in self.listOfAbilities else 'other' for i in self.skills]
        else:
            self.skills = [skills]
            self.skills = [i if i in self.listOfAbilities else 'other' for i in self.skills]

        self.phone_number = phone_number

        if rating is None or (isinstance(rating, int) and (0 <= rating <= 10)):
            self.__rating = rating
        else:
            self.__rating = None
            print("Rating has to be integer between 1 - 10")

        self.available = available
        self.approved = approved
        Employee.numberOfEmployees += 1
        Employee.listOfEmployees.append(self)

    def __str__(self):
        return 'Name: {} \nSurname {} \nphone number: {} \nskills : {} \nrating: {} \navailable : {} \n{}'\
            .format(self.name,self.surname,self.phone_number,self.skills,self.__rating,self.available,'-'*60)

    def changeAvailability(self):
            self.available = not(self.available)

    def addSkill(self,skill):
        if isinstance(skill,list):
            self.skills.extend(skill)
        else:
            self.skills.append(skill)

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self,newRating):
        if self.approved == True:
            self.__rating = newRating
            print('New Rating = {} is set for {} {}'.format(self.rating,self.name,self.surname))
        else:
            print('Cannot set rating for not approved employee {} {}'.format(self.name,self.surname))

    @rating.deleter
    def rating(self):
        self.__rating = None

    @property
    def full_name(self):
        return  "__== {} {} ==__".format(self.name.upper(),self.surname.upper())

rafal_kociecki = Employee('Rafal', 'Kociecki','123456789', ['wozki widlowe','elektronika','salto w tyl'],rating = 6,approved=True)
pawel_kaczmar = Employee('Pawel','Kaczmar','99887766',rating='bledny rating')

class Manager(Employee):

    listOfManagers = []

    def __init__(self,name,surname,phone_number,contract,payment,skills = None,available = True,approved = True):
        super(Manager, self).__init__(name,surname,phone_number,skills,available)
        self.approved = approved
        self.rating = None
        self.contract = contract
        self.payment = payment
        Manager.listOfManagers.append(self)

    def __str__(self):
        return self.full_name + "\nThis is a manager \ncontract: {}\npayment method: {}\nrating:{}"\
            .format(self.contract,self.payment,self.rating)


damian_kaczkowski = Manager('Damian','Kaczkowski','123456','umowa o prace','transfer')

print(damian_kaczkowski)