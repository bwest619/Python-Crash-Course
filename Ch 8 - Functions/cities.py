# Try it yourself, page 141

print("\n")
def describe_city(name, country = 'United States'):
    """Describing a country"""
    print(name.title() + " is in the country: " + country + ".")


describe_city('san diego')
print("\n")
describe_city('new york')
print("\n")
describe_city('moscow', 'Russia')
