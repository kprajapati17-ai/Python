
hour =int(input("Enter 24 hour time:"))


if hour > 24:
    print("INVALID")

if hour < 12:
    print(f"{hour} AM")


if hour == 12:
    print(f"{hour} PM")


# if hour == 24:
    # print(f"{hour} AM")
 
if hour > 12:
    hour = hour - 12
    print(f"{hour} PM")





# if hour == 0:
    # print("INVALID")
