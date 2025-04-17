class Pet:
    """
    A class to represent a virtual pet using OOP concepts.
    """

    def __init__(self, name):
        """
        Constructor to initialize the pet with default values.
        """
        self.name = name
        self.hunger = 5        # 0 (full) to 10 (very hungry)
        self.energy = 5        # 0 (tired) to 10 (fully rested)
        self.happiness = 5     # 0 (sad) to 10 (very happy)
        self.tricks = []       # List to store learned tricks

    def eat(self):
        """
        Feed the pet: reduce hunger and increase happiness.
        """
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        """
        Let the pet sleep: restore energy.
        """
        self.energy = min(10, self.energy + 5)

    def play(self):
        """
        Play with the pet: boost happiness, reduce energy, and increase hunger.
        """
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
        else:
            print(f"{self.name} is too tired to play!")

    def train(self, trick):
        """
        Teach the pet a new trick and add it to the tricks list.
        """
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        """
        Display all tricks the pet has learned.
        """
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        """
        Print the current status of the pet.
        """
        print("\n--- Pet Status ---")
        print(f"Name      : {self.name}")
        print(f"Hunger    : {self.hunger}/10")
        print(f"Energy    : {self.energy}/10")
        print(f"Happiness : {self.happiness}/10")
        print("-------------------\n")
