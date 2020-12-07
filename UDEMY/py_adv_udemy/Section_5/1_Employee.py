class Employee:

    numberOfEmployees = 0
    listOfEmployees = []
    listOfAbilities = ['wozki widlowe', 'praca na wysokosci','prawo jazdy typu C']

    def extend_list_of_abilities(addition_ability):
        if isinstance(addition_ability,list):
            Employee.listOfAbilities.extend(addition_ability)
        else:
            Employee.listOfAbilities.append(addition_ability)

    def __init__(self,name,surname,phone_number,skills = None,rating = None, available = True):
        self.name = name
        self.surname = surname
        self.skills = skills if isinstance(skills,list) else [skills]
        self.skills = [i if i in self.listOfAbilities else 'other' for i in self.skills]
        self.phone_number = phone_number
        self.__rating = rating
        self.available = available
        Employee.numberOfEmployees += 1
        Employee.listOfEmployees.append(self)

    def __str__(self):
        return 'Name: {} \nSurname {} \nphone number: {} \nskills : {} \nrating: {} \navailable : {} \n{}'\
            .format(self.name,self.surname,self.phone_number,self.skills,self.__rating,self.available,'-'*60)

    def ChangeAvailability(self):
            self.available = not(self.available)

    def add_skill(self,skill):
        self.skills.append(skill)


Employee.extend_list_of_abilities(['elektronika','mechanik'])

rafal_kociecki = Employee('Rafal', 'Kociecki','123456789', ['wozki widlowe','elektronika','salto w tyl'])
pawel_kaczmar = Employee('Pawel','Kaczmer','99887766',skills='wozki widlowe')

rafal_kociecki.ChangeAvailability()
rafal_kociecki.add_skill('Prawo jazdy typu C')
rafal_kociecki._Employee__rating = 5
#print(dir(rafal_kociecki))

# print('#'*50)
#
# print(Employee.listOfAbilities)
# print(Employee.listOfEmployees)
# print(Employee.numberOfEmployees)
#
# print('#'*50)

for employee in Employee.listOfEmployees:
    print(employee)




