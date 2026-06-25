#  write a program to decide which is better approach to go from ahmedabad to delhi. by car or by train. person has his own petrol car 


train_ticket=int(input("Enter How Many People:"))
ticket_price=int(input("Enter Ticket Price:"))

Train_cost = train_ticket * ticket_price

distance = float(input("Enter distance between cities (km): "))
mileage = float(input("Enter car mileage (km per litre): "))

# petrol_need=int(input("Enter how much petrol Need:"))
petrol_price=int(input("Enter petrol Price:"))

car_cost = petrol_price * (distance/mileage)

print("Train Cost =", Train_cost)
print("Car Cost =", car_cost)
if Train_cost > car_cost:
    print("Car is Better to go from ahmedabad to delhi")
else:   
    print("Train is Better to go from ahmedabad to delhi")