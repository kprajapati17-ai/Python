# example of for loop on dictionary
india_info = {
    "name": "india",
    "official_name": "republic of india",
    "capital": "new delhi",
    "largest_city": "mumbai",
    "continent": "asia",
    "region": "south asia",
    "currency": "indian rupee",
    "currency_code": "inr",
    "timezone": "ist",
    "utc_offset": "+05:30",
    "population": "1.4 billion+",
    "area_sq_km": 3287263,
    "government": "federal parliamentary republic",
    "president": "droupadi murmu",
    "prime_minister": "narendra modi",
    "national_language": "hindi",
    "official_languages": "hindi, english",
    "calling_code": "+91",
    "internet_tld": ".in",
    "national_animal": "bengal tiger"
}
#it will name of each and every key

for i in india_info:
    print(i,": ",india_info[i])