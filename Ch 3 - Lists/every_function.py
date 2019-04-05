#try it yourself, page 50

languages = ['python', 'css', 'html', 'c', 'javascript']

print(languages)
print(languages[1].title())
print("My first computer language is " + languages[0].title() + ".")

print(languages[-1])

languages.append('java')
print(languages)

languages.insert(2, 'php')
print(languages)

languages[4] = 'ruby'
print(languages)

languages.append('c')
print(languages)

languages.insert(5, 'visual basic')
print(languages)

del languages[3]
print(languages)
print("\n")

popped_language = languages.pop(3)
print("The language I haven't looked at yet is " + popped_language.title() + ".")
print("\n")

first_language = languages.pop(0)
print("My first computer language is " + first_language.title() + "!")
print("\n")

too_difficult = 'c'
languages.remove(too_difficult)
print("The language I hated to start learning was " + too_difficult.title() + ".")
print(languages)
print("\n")

print("The languages sorted alphabetically is:")
print(sorted(languages))
print("The languages in their original order is:")
print(languages)
print("\n")

print("The languages listed in reverse alphabetical order is:")
print(sorted(languages, reverse = True))
print("The original order is still:")
print(languages)
print("\n")

languages.reverse()
print("The languages in reverse order is:")
print(languages)
languages.reverse()
print("The languages reveresed back to their original order is:")
print(languages)
print("\n")

languages.sort()
print("The languages in alphabetical order is:")
print(languages)
languages.sort(reverse = True)
print("The languages in reverse alphabetical order is:")
print(languages)
languages.sort()
print("The languages reversed back to alphabetical order is:")
print(languages)
print("The length of the list of languages is:")
print(len(languages))
print("\n")

print(languages[-1]) # always prints the last item in the list... unless the list is empty.
