# Level 1 (Basic – must solve)
# Q1. 1 thi N sudhi numbers print kar (recursion thi)

# 👉 Example: n = 5
# Output: 1 2 3 4 5

# n = int(input("Enter A N:"))
# def print_n(n):
#         if n == 0:
#                 return
#         print_n(n-1)
#         print(n,end=" ")       
# print_n(n)

# Q2. N thi 1 sudhi print kar
# 👉 Example: n = 5
# Output: 5 4 3 2 1

# n = int(input("Enter A N:"))
# def print_n(n):
#         if n == 0:
#                 return
#         print(n,end=" ")       
#         print_n(n-1)
# print_n(n)




# Q3. Sum of first N numbers

# 👉 Example: n = 5
# Output: 15

# n = int(input("Enter A N:"))

# def sum_n(n):
#     if n == 0:
#         return 0
#     s = n + sum_n(n-1)
#     return s 

# z = sum_n(n)
# print(z)
# Q4. Factorial find kar

# 👉 Example: n = 5
# Output: 120
n = int(input("Enter A N:"))

def fact(n):
    if n == 0:
         return 1
    f = n * fact(n-1)
    return f
print(fact(5))
# 🟡 Level 2 (Thodu thinking joiye)
# Q5. Number reverse kar (recursion thi)

# 👉 Input: 1234
# 👉 Output: 4321

# Q6. Sum of digits

# 👉 Input: 1234
# 👉 Output: 10

# Q7. Check number palindrome che ke nai

# 👉 Input: 121 → True
# 👉 Input: 123 → False

# 🔵 Level 3 (Important concepts)
# Q8. Fibonacci number find kar

# 👉 Input: n = 6
# 👉 Output: 8

# Q9. Power find kar (a^b)

# 👉 Input: 2,3
# 👉 Output: 8

# Q10. Array ma max element find kar (recursion thi)

# 👉 Input: [3, 9, 2, 15, 6]
# 👉 Output: 15

# 🔴 Level 4 (Advanced 🔥)
# Q11. String na badha subsets print kar

# 👉 Input: "ab"
# 👉 Output:

# ab
# a
# b
# (empty)
# Q12. Decimal ne binary ma convert kar

# 👉 Input: 10
# 👉 Output: 1010

# Q13. GCD find kar recursion thi

# 👉 Input: 48, 18
# 👉 Output: 6

# ⚫ Challenge Level (Top 🔥)
# Q14. Maze problem solve kar (path find kar)