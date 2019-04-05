# try it yourself, page 46
guest_list = ['michael jordan', 'freddy murcury', 'kurt kobain']

declined = 'kurt kobain'
print("Sadly, " + declined.title() + " has declined to come to dinner.")

guest_list.remove(declined)
guest_list.insert(2, 'ed boon')

print(guest_list)

print("Hello, " + guest_list[0].title() + ", I'm inviting you to dinner tomorrow night.")
print("Hello, " + guest_list[1].title() + ", I'm inviting you to dinner tomorrow night.")
print("Hello, " + guest_list[2].title() + ", I'm inviting you to dinner tomorrow night.")
