class Employee:

    listOfEmployees = []
    numberOfEmployees = len(listOfEmployees)

    def __init__(self,name,surname,phone_number,skills = None,rating = None, available = True, approved = False):
        self.name = name
        self.surname = surname
        self.skills = skills if isinstance(skills,list) else [skills]
        self.phone_number = phone_number

        if rating is None or (isinstance(rating, int) and (0 <= rating <= 10)):
            self.rating = rating
        else:
            self.rating = None
            print("Rating has to be integer between 1 - 10")

        self.available = available
        self.approved = approved

        Employee.numberOfEmployees += 1
        Employee.listOfEmployees.append(self)

    def __str__(self):
        return 'Name: {} \nSurname {} \nphone number: {} \nskills : {} \nrating: {} \navailable : {} \n{}'\
            .format(self.name,self.surname,self.phone_number,self.skills,self.rating,self.available,'-'*60)


    def __iadd__(self, other):
        if type(other) is list:
            skills = self.skills
            skills.extend(other)
            skills = list(dict.fromkeys(skills))
            return Employee(self.name,self.surname,self.phone_number,skills,self.rating,
                            self.available,self.approved)
        elif type(other) is str:
            skills = self.skills
            skills.append(other)
            skills = list(dict.fromkeys(skills))
            return Employee(self.name,self.surname,self.phone_number,skills,self.rating,
                            self.available,self.approved)
        else:
            raise Exception('Adding type {} to Car is not implemented'.format(type(other)))



rafal_kociecki = Employee('Rafal', 'Kociecki','123456789', ['wozki widlowe','elektronika'],rating = 7,approved=True)
pawel_kaczmar = Employee('Pawel','Kaczmar','99887766',skills='wozki widlowe',rating=5)

print(rafal_kociecki)