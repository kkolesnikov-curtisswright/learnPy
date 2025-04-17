city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}

city_name = "Tampa"

# Add your code here:
def get_city_population(populations, city):
    try:
        return populations.get(city, "Population data not available")
    except KeyError:
        raise KeyError(f"City {city} not found in population data.")
    
print(get_city_population(city_populations, city_name))