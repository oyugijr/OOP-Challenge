# main.py

from pet import Pet

# Create an instance of the Pet class
my_pet = Pet("Buddy")

# Show initial status
my_pet.get_status()

# Interact with the pet
my_pet.eat()
my_pet.sleep()
my_pet.play()

# Teach new tricks
my_pet.train("roll over")
my_pet.train("fetch")

# Display tricks
my_pet.show_tricks()

# Show final status
my_pet.get_status()
