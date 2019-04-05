# Try it yourself, page 154

def make_car(make, model, **car_info):
    """Summarize the information about a car"""
    car_profile = {}
    car_profile['car_make'] = make
    car_profile['car_model'] = model
    for key, value in car_info.items():
        car_profile[key] = value

    return car_profile


car = make_car('dodge', 'charger', year = '2016', color = 'black')
print(car)
print("\n")

#####################################################################################

# Easier/quicker way to write the body of the same program above...
def make_car(make, model, **car_info):
    """Summarize the information about a car"""
    car_profile = {
        'car_make' : make,
        'car_model' : model,
        }
    for key, value in car_info.items():
        car_profile[key] = value

    return car_profile


car = make_car('dodge', 'charger', year = '2016', color = 'black')
print(car)
