def zoo_showcase(animals):
    print("🐾 Welcome to the Zoo!\n")
    for animal in animals:
        print(animal.info())
        print("Sound:", animal.make_sound())
        print("-" * 30)
