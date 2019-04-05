# Try it yourself, page 146

def city_country(city, country):
    """Return a string like 'Santiago, Chile'"""
    return(city.title() + ", " + country.title()) # instead of doing full_name = first_name + " " + last_name


city = city_country('san diego', 'united states')
print(city)
city = city_country('beijing', 'china')
print(city)
city = city_country('moscow', 'russia')
print(city)

