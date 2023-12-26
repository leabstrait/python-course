current_users = ['luceroclipboard','gutfinna','workscottish','sensitizeabydocomist','xetabass','ontobaseball','upstartjubilant','pandavacuum','collesempanada','emmataboo']
new_users = ['collesempanada','emmataboo','aspeneveryday','smoothdolphin','observantlogged','tablespoonjo','grewrigid','junningjonah','prizetaxidriver','repurposejoystick','blinksbike','ricochetmithers','nutrientconcrete','grandfatherplank']

for new_user in new_users:
    if new_user in current_users:
        print(f"The name '{new_user}' already exists! Try a new one.")
    else:
        print(f"Username '{new_user}' successfully registered!")

print("Finished setting up new usernames")