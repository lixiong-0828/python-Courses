usernames = ['the blueman', 'sorted hedgehog', 'infinite lagoon']

for name in usernames:
    i = usernames.index(name)
    name = name.replace(' ', '_')
    print(name)
    usernames[i] = name
    print(f"usernames[i]  : {usernames[i] }")

print(usernames)
