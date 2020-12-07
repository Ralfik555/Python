clients =  {
    "Info" : 0.5,
    "Data" : 0.2,
    "Soft" : 0.2,
    "Inter" : 0.1,
    "Omega" : 0.0,
}

myClient =  input("Enter client's name : ")
totalCost = 7200

try:
    ratio = float(input("Enter new ratio: "))
    print("The % ratio for {} is {}".format(myClient,clients[myClient]))
except Exception as e:
    print("Sorry we have an error...\nDetails: \n{}".format(e))

else:
    print("The cost for {} is {}".format(myClient,clients[myClient] * totalCost))
finally:
    print("-= Calculation finished =-")