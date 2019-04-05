# try it yourself, page 46
guest_list = ['ken griffey, jr.', 'michael jordan', 'robin williams', 'freddy murcury', 'ed boon', 'barrack obama']
print(guest_list)

print("Sorry, guys, I can only invite 2 people to dinner now as this book is stupid and lost the big table!")

first_cut = guest_list.pop(4)
print("Sorry, " + first_cut.title() + ", I can't invite you.")

second_cut = guest_list.pop(3)
print("Sorry, " + second_cut.title() + ", I can't invite you.")

print(guest_list)
third_cut = guest_list.pop(3)
print("Sorry, " + third_cut.title() + ", I can't invite you.")

fourth_cut = guest_list.pop(2)
print("Sorry, " + fourth_cut.title() + ", I can't invite you.")

print(guest_list)
print("Hello, " + guest_list[0].title() + ", you're still invited.")
print("Hello, " + guest_list[1].title() + ", you're still invited.")

del guest_list[1]
del guest_list[0]

print(guest_list)
