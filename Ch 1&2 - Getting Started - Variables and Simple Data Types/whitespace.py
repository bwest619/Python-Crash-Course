print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

#strip strips away unnecessary whitespace from the right or left side of a string. This will make "python " print as "python"
favorite_language = "python "
favorite_language = favorite_language.rstrip()
print(favorite_language)

#you can remove the whitespace on the left side by using "lstrip()" or remove the whitespace on both sides by using "strip()"
favorite_language = " python "
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()
print(favorite_language.strip())
