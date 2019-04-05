# Try it yourself, page 184

from privileges_module import Privileges, Admin

administer = Admin('blaine', 'west', 'man in charge', 'bwest@bullshit.com', 'denver')
administer.privileges.privileges = ['can add post', 'can delete post', 'can ban user',
                                    'can change your name to something silly']

print(administer.describe_user())
administer.privileges.show_privileges()
