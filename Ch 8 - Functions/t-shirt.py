# Try it yourself, page 141

def make_shirt(size, message):
    """Getting the size and message to be printed on a shirt"""
    print("My t-shirt is a size " + size.upper() + " and says, " + message + ".")


make_shirt('xl', 'BOOYA')
print("\n")

######################################################################################

def make_shirt(size='L', message='Look Away'):
    """Getting the size and message to be printed on a shirt"""
    print("I need a shirt, size " + size + ", that says " + "'" + message + "'.")


make_shirt()

####################################################################################

print("\n")
def make_shirt(size, message):
    """Shirt size and message"""
    print("I need a shirt, size " + size + ", that says " + message + ".")


make_shirt(message='Get Pumped!', size ='XL')
