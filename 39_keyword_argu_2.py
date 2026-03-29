# write a program that return total area of house, average room size and maximum room size  from 1 bed room, 1 hall, 1 kitchen size. here room, hall and kitchen all are actually tuple which has length and width. 

def getArea(room,hall,kitchen):

    rl,rw = room
    hl,hw= hall
    kl,kw=kitchen

    rarea = rl* rw
    harea = hl* hw
    karea = kl* kw

    print(f"room area = {rarea}, hall area = {harea}, kitchen area = {karea}")
    totalArea = rarea + harea + karea 
    average = totalArea / 3
    maximum = max(rarea,harea,karea)
    minimum = min(rarea,harea,karea)
    return totalArea,average,maximum,minimum
rl = int(input("Enter room length: "))
rw = int(input("Enter room width: "))
hl = int(input("Enter hall length: "))
hw = int(input("Enter hall width: "))
kl = int(input("Enter kitchen length: "))
kw = int(input("Enter kitchen width: "))
total, average,mx,mi = getArea(room=(rl,rw),hall=(hl,hw),kitchen=(kl,kw))
print("total Area is:",total,"average Area is:",average,"maximum Area is:",mx,"minimum Area is:",mi)