current_users = ['luceroclipboard','gutfinna','workscottish','sensitizeabydocomist','xetabass','ontobaseball','upstartjubilant','pandavacuum','collesempanada','emmataboo']
new_users = ['collesempanada','emmataboo','aspeneveryday','smoothdolphin','observantlogged','tablespoonjo','grewrigid','junningjonah','prizetaxidriver','repurposejoystick','blinksbike','ricochetmithers','nutrientconcrete','grandfatherplank']

# new_users = []

while new_users:
    new_user = new_users.pop()
    # new_user = new_users[0]
    # if new_users[0] in current_users:
    if new_user in current_users:
        print(f"The name '{new_user}' already exists! Try a new one.")
    else:
        print(f"Username '{new_user}' successfully registered!")
    
    # new_users.remove(new_user)

    
print("Finished setting up new usernames")