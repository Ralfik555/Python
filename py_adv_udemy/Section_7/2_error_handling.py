clients = {
    "Info": 0.5,
    "Data": 0.2,
    "Soft": 0.2,
    "Inter": 0.1,
    "Omega": 0.0,
}

myClient = input("Enter client's name : ")
totalCost = 7200

try:
    ratio = float(input("Enter new ratio: "))
    print("The default ratio for {} is {} a new one is {}".format(myClient, clients[myClient], ratio))
    print("The cost for {} is {}".format(myClient,ratio * totalCost))
    print("The new ratio in comparison to old ratio: {}".format(clients[myClient]/ratio))
except KeyError as e:
    print("Client {} is not on the list {}. \nDetails:\n{}".format(myClient,[c for c in clients.keys()],e))
except (ValueError,ZeroDivisionError) as e:
    print("There is a problem with entered value for ratio - is must be a number greater than 0.\nDetails:\n{}".format(e))
# except ZeroDivisionError as e:
#     print("New ratio can not be 0.\nDetails:\n{}".format(e))
except Exception as e:
    print("Sorry we have an error...\nDetails: \n{}".format(e))
