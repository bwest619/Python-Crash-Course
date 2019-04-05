# Try it yourself, page 108

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")
print("\n")

polling = ['blaine', 'jen', 'brandon', 'sarah', 'jared', 'phil']

for name in polling:
    if name in favorite_languages.keys():
        print("Thank you " + name.title() + ", for responding to the poll.")
    else:
        print("Hello " + name.title() + ", I am inviting you to participate in our poll.")
