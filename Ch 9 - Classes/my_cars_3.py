# Importing a module into a module
# Importing from separate modules

from car_module import Car
from electric_car_module import ElectricCar

my_beetle = Car('volkswagon', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
