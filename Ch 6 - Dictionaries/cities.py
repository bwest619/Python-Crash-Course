# Try it yourself, page 115

cities = {
    'new york' : {
        'country' : 'united states',
        'population' : '8.623 million',
        'fact' : 'it is the largest metropolitan area in the world by urban landmass',
         },
    'shanghai' : {
        'country' : 'china',
        'population' : '24.1 million',
        'fact' : 'its population makes it the most populous city not only in Asia but in the entire world',
        },
    'moscow' : {
        'country' : 'russia',
        'population' : '13.1 million',
        'fact' : 'has been ranked as the ninth most expensive city in the world',
        },
    }

for name, info in cities.items():
    print("\n" + name.title() + ":")
    country = info['country'].title()
    population = info['population']
    fact = info['fact'].capitalize()

    print("\t" + country)
    print("\t" + population)
    print("\t" + fact)


