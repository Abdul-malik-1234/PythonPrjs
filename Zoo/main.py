from animal import Lion,Pet

leo = Lion("Leo")
print(f"{leo._name} says: {leo.make_sound()}")

tommy = Pet("Tommy","Golden Shepherd")
print(f"{tommy._name} is of breed: {tommy._species} it does a {tommy.make_sound()} and it says {tommy.speak()}")