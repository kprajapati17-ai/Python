# 3) create function that returns how many words are palindrome words from given number of argument

def palindrome(*words):
    c =0
    for i in words:
        if i == i[::-1]:
            c = c + 1
        # else:
        #     print("pelindrom not ")
    return c
        
tot = palindrome("mnm","ddd","awerf","hhgbb","www")
print("total is :",tot)
        
# palindrome_manual.py

def palindrome(*words):
    count = 0

    for word in words:
        rev = ""   # empty string
        

        for ch in word:
            rev = ch + rev   # manual reverse

        if word == rev:
            count += 1

    return count


total = palindrome("mnm","ddd","awerf","hhgbb","www")

print("Total palindrome words:", total)