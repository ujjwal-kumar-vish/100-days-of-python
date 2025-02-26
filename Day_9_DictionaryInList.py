travel_log = [
    {
        "country" : "France",
        "vistis" : 12,
        "cities" : ["Paris", "Lille", "Dijon"]
    },
    {
        "country" : "Germany",
        "vistis" : 5,
        "cities" : ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country, vistis, cities):
    #positon = len(travel_log)
    travel_log.append({
        "country" :country,
        "vistis" : vistis,
        "cities" : cities,
    })

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)