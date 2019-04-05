# Try it yourself, page 222

def city_country(city, country, population=''):
    """Return the string 'Santiago, Chile - 5000000."""
    if population:
        city_name = city.title() + ", " + country.title() + " - " + str(population) + "."
    else:
        city_name = city.title() + ", " + country.title()
    return city_name


