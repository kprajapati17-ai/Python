u1_length =int(input("Enter User 1 Farm Length :")) 
u1_width =int(input("Enter User 1 Farm Width :")) 

u2_length =int(input("Enter User 2 Farm Length :")) 
u2_width =int(input("Enter User 2 Farm Width :")) 
print(f"User 1 Length is {u1_length} And Width is {u1_width}")
print(f"User 2 Length is {u2_length} And Width is {u2_width}")
u1_area = u1_length * u1_width
u2_area = u2_length * u2_width
print(f"User 1 Area is {u1_area}")
print(f"User 2 Area is {u2_area}")
diffrent = u1_area - u2_area
diffrent1 = u2_area - u1_area
if u1_area > u2_area:
    print(f"User 1 Farm Area is  biggre than User 2 And Diffrent is {diffrent}")

if u2_area > u1_area:
    print(f"User 2 Farm Area is biggre than User 1  And Diffrent is {diffrent1} ")    