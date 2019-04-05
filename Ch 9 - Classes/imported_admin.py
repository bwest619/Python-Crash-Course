# Try it yourself, page 184

from admin_module import Admin

administer = Admin('blaine', 'west', 'man in charge', 'bwest@bullshit.com', 'denver')
administer.privileges.privileges = ['can add post', 'can delete post', 'can ban user',
                                    'can change your name to something silly']

administer.describe_user()
administer.greet_user()
administer.privileges.show_privileges()


