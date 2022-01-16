#Nesting a dictionary in a Dictionary

travel_log = [
    {
    "country" :"France",
    "cities_visited":["Paris", "Lille", "Dijon"], 
    "total_visits": 12
    },
    { 
        "country": "Mexico",
        "cities_visited": ["Taxco", "Acapulco", "Cancun"], 
        "total_visits": 12
    }

]

def add_new_country(country, times_visited, cities):
    new_country = {}
    new_country["country"] = country
    new_country["times_visited"] = times_visited
    new_country["cities"] = cities
    travel_log.append(new_country)


add_new_country(country="Russia",times_visited=2,cities= ["Moscow", "Saint"])
print(travel_log)