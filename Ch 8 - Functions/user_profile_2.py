# Try it yourself, page 154

def build_profile(first, last, **user_info):
    """Building a profile of myself."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value

    return profile


user_profile = build_profile('blaine', 'west', height="6'7", location='denver', job='server')
print(user_profile)

