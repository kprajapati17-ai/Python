# from kerykeion import AstrologicalSubject
# from geopy.geocoders import Nominatim

# # Rashi mapping
# rashi_names = {
#     "Aries": "Mesh", "Ari": "Mesh",
#     "Taurus": "Vrushabh", "Tau": "Vrushabh",
#     "Gemini": "Mithun", "Gem": "Mithun",
#     "Cancer": "Kark", "Can": "Kark",
#     "Leo": "Sinh",
#     "Virgo": "Kanya", "Vir": "Kanya",
#     "Libra": "Tula", "Lib": "Tula",
#     "Scorpio": "Vrushchik", "Sco": "Vrushchik",
#     "Sagittarius": "Dhanu", "Sag": "Dhanu",
#     "Capricorn": "Makar", "Cap": "Makar",
#     "Aquarius": "Kumbh", "Aqu": "Kumbh",
#     "Pisces": "Meen", "Pis": "Meen"
# }

# # User input (birth details)
# year = int(input("Enter birth year: "))
# month = int(input("Enter birth month: "))
# day = int(input("Enter birth day: "))
# hour = int(input("Enter birth hour (0-23): "))
# minute = int(input("Enter birth minute: "))
# place = input("Enter your city: ")

# # Get latitude & longitude automatically
# geolocator = Nominatim(user_agent="astro_app")
# location = geolocator.geocode(place)

# if location is None:
#     print("City not found ❌")
# else:
#     lat = location.latitude
#     lng = location.longitude

#     # Create object without name
#     k = AstrologicalSubject(
#         year=year, month=month, day=day,
#         hour=hour, minute=minute,
#         lat=lat, lng=lng
#     )

#     # Get signs
#     sun_sign = k.sun['sign']
#     moon_sign = k.moon['sign']

#     # Convert to Gujarati
#     sun_rashi = rashi_names.get(sun_sign, sun_sign)
#     moon_rashi = rashi_names.get(moon_sign, moon_sign)

#     # Output
#     print("\n📍 Location Found:", location.address)
#     print("🌐 Latitude:", lat, "Longitude:", lng)

#     print("\n🔮 RESULT 🔮")
#     print(f"Surya Rashi: {sun_sign} ({sun_rashi})")
#     print(f"Chandra Rashi: {moon_sign} ({moon_rashi})")


# ................................................................................................................







from kerykeion import AstrologicalSubject
from geopy.geocoders import Nominatim

# Rashi mapping
rashi_names = {
    "Aries": "Mesh", "Ari": "Mesh",
    "Taurus": "Vrushabh", "Tau": "Vrushabh",
    "Gemini": "Mithun", "Gem": "Mithun",
    "Cancer": "Kark", "Can": "Kark",
    "Leo": "Sinh",
    "Virgo": "Kanya", "Vir": "Kanya",
    "Libra": "Tula", "Lib": "Tula",
    "Scorpio": "Vrushchik", "Sco": "Vrushchik",
    "Sagittarius": "Dhanu", "Sag": "Dhanu",
    "Capricorn": "Makar", "Cap": "Makar",
    "Aquarius": "Kumbh", "Aqu": "Kumbh",
    "Pisces": "Meen", "Pis": "Meen"
}

# User input
name = input("Enter your name: ")
year = int(input("Enter birth year: "))
month = int(input("Enter birth month: "))
day = int(input("Enter birth day: "))
hour = int(input("Enter birth hour: "))
minute = int(input("Enter birth minute: "))
place = input("Enter your city: ")

# Get latitude & longitude automatically
geolocator = Nominatim(user_agent="astro_app")
location = geolocator.geocode(place)

if location is None:
    print("City not found ❌")
else:
    lat = location.latitude
    lng = location.longitude

    # Create object
    k = AstrologicalSubject(
        name, year, month, day, hour, minute,
        lat=lat, lng=lng
    )

    # Get signs
    sun_sign = k.sun['sign']
    moon_sign = k.moon['sign']

    # Convert to Gujarati
    sun_rashi = rashi_names.get(sun_sign, sun_sign)
    moon_rashi = rashi_names.get(moon_sign, moon_sign)

    # Output
    print("\n📍 Location Found:", location.address)
    print("🌐 Latitude:", lat, "Longitude:", lng)

    print("\n🔮 RESULT 🔮")
    print(f"Surya Rashi: {sun_sign} ({sun_rashi})")
    print(f"Chandra Rashi: {moon_sign} ({moon_rashi})")

