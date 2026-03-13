
# 4) write a program to accept birth day and birth month from user. decide zodiac sign from below table 
#     Aries: March 21–April 19
#     Taurus: April 20–May 20
#     Gemini: May 21–June 21
#     Cancer: June 22–July 22
#     Leo: July 23–August 22
#     Virgo: August 23–September 22
#     Libra: September 23–October 22
#     Scorpio: October 24–November 21
#     Sagittarius: November 22–December 21
#     Capricorn: December 22–January 19
#     Aquarius: January 20–February 18
#     Pisces: February 19–March 20

month = int(input("Enter birth month :"))
day = int(input("Enter  birth day:"))

if month == 3 and day >= 21 or  month == 4 and day <= 19:
    print("Aries: March 21–April 19")
elif month == 4 and day >= 20 or  month == 5 and day <= 20:
    print(" Taurus: April 20–May 20")
elif month == 4 and day >= 20 or  month == 5 and day <= 20:
    print("Gemini: May 21–June 21")
elif month == 5 and day >= 21 or  month == 6 and day <= 21:
    print(" Cancer: June 22–July 22")
elif month == 6 and day >= 22 or  month == 7 and day <= 22:
    print("Leo: July 23–August 22")
elif month == 7 and day >= 22 or  month == 8 and day <= 22:
    print(" Virgo: August 23–September 22")
elif month == 8 and day >= 23 or  month == 8 and day <= 22:
    print("Libra: September 23–October 22")
elif month == 9 and day >= 23 or  month == 9 and day <= 22:
    print("Scorpio: October 24–November 21")
elif month == 10 and day >= 24 or  month == 11 and day <= 21:
    print("Sagittarius: November 22–December 21")
elif month == 11 and day >= 22 or  month == 12 and day <= 21:
    print("Capricorn: December 22–January 19")
elif month == 12 and day >= 22 or  month == 1 and day <= 19:
    print("Aquarius: January 20–February 18")
elif month == 1 and day >= 20 or  month == 2 and day <= 18:
    print("Pisces: February 19–March 20")
else:
    print("Invalid")

