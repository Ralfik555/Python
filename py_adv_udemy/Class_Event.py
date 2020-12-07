class Event:

    dict_to_compare = {'number':None,'wage':None,'working_hours':None}.keys()
    basic_dict = {'standard':{'number':None,'wage':None,'working_hours':None}}

    listOfEvents = []

    def __init__(self, name, location, principal, time, employees_demand = None):
        self.name = name
        self.location = location
        self.principal = principal
        self.time = time

        if employees_demand is None:
            self.employeesDemand = employees_demand
        elif type(employees_demand) is dict:
            for i in employees_demand.values():
                if i.keys() == Event.dict_to_compare:
                    pass
                else:
                    raise ValueError("Dictionary structure: {'standard':{'number':None,'wage':None,'working_hours':None}}")
            self.employeesDemand = employees_demand
            self.numberOfAllEmployees = sum(x['number'] for x in self.employeesDemand.values())
        else:
            raise ValueError("Has to be dictionary")

        self.listOfEvents.append(self)


    def __str__(self):
        return '''
Event name: {}
Location: {}
Principal: {}
number of all employees: {}
        '''.format(self.name,self.location,self.principal,self.numberOfAllEmployees)


opener = Event('Opener','Lotnisko - Babie Doły','Alter Art',80,
               {
                'standard':{'number':40,'wage':20,'working_hours':80},
                'electric': {'number':2,'wage':40,'working_hours':40},
                'forklift':{'number':3,'wage':30,'working_hours':40},
                'manager':{'number':5,'wage':80,'working_hours':24},
                'driver':{'number':50,'wage':25,'working_hours':24}
               })


print(opener)
