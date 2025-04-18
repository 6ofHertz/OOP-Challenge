class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting at midpoint
        self.energy = 5
        self.happiness = 5
        self.tricks = []  # For bonus feature
        
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Hunger decreased, happiness increased!")
        
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy restored!")
        
    def play(self):
        if self.energy >= 2:  # Only play if there's enough energy
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played happily!")
        else:
            print(f"{self.name} is too tired to play right now.")
            
    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {'★' * self.hunger}{'☆' * (10 - self.hunger)} ({self.hunger}/10)")
        print(f"Energy: {'★' * self.energy}{'☆' * (10 - self.energy)} ({self.energy}/10)")
        print(f"Happiness: {'★' * self.happiness}{'☆' * (10 - self.happiness)} ({self.happiness}/10)")
        
        # Status messages based on levels
        if self.hunger >= 8:
            print(f"{self.name} is very hungry!")
        elif self.hunger <= 2:
            print(f"{self.name} is full.")
            
        if self.energy <= 2:
            print(f"{self.name} is exhausted.")
        elif self.energy >= 8:
            print(f"{self.name} is full of energy!")
            
        if self.happiness <= 2:
            print(f"{self.name} is feeling sad.")
        elif self.happiness >= 8:
            print(f"{self.name} is extremely happy!")
    
    # Bonus methods
    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows how to {trick}.")
    
    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")