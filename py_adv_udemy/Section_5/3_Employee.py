def export_all_employee_to_html(cls, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{} {}</th>
     </tr>
       <tr>
         <td>Phone</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Rating</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Available</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Skills</td>
         <td>{}</td>
       </tr>
</table>"""
    with open(path, mode = "w") as f:
        for c in cls.listOfEmployees:
            content = template.format(c.name, c.surname, c.phone_number, c.rating, c.available,c.skills)
            f.write(content)


def export_employee_to_html(self, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{} {}</th>
     </tr>
       <tr>
         <td>Phone</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Rating</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Available</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Skills</td>
         <td>{}</td>
       </tr>
</table>"""
    with open(path, mode = "w") as f:
        content = template.format(self.name, self.surname, self.phone_number, self.rating, self.available,self.skills)
        f.write(content)



class Employee:

    listOfEmployees = []
    numberOfEmployees = len(listOfEmployees)
    listOfAbilities = ['wozki widlowe', 'praca na wysokosci','prawo jazdy typu C']

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

    def changeAvailability(self):
            self.available = not(self.available)

    def addSkill(self,skill):
        self.skills.append(skill)


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
rafal_kociecki.addSkill('Prawo jazdy typu C')

print(rafal_kociecki.rating)
rafal_kociecki.rating = 7
del rafal_kociecki.rating
print(rafal_kociecki.rating)

import types

Employee.Export_all_employee_to_html = types.MethodType(export_all_employee_to_html,Employee)
Employee.Export_all_employee_to_html(r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_5\saved_Employee\export_employees.html')

for emp in Employee.listOfEmployees:
    emp.Export_employee_to_html = types.MethodType(export_employee_to_html,emp)

for emp in Employee.listOfEmployees:
    emp.Export_employee_to_html(r'C:\Users\Ralfik\Desktop\Python\py_adv_udemy\Section_5\saved_Employee\{}_{}.html'
                                .format(emp.name,emp.surname))