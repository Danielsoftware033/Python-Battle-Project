
#Base Character
#Pillar 2 Inheritence: Child class inherits attributes and methods from parent class
#parent class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} has attacked {opponent.name} with a stick for {self.attack_power} points of damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has perished!")
        else:
            print(f"{opponent.name} has {opponent.health}hp left. ")

    def display_stats(self):
        print(f"{self.name}'s Stats \n Health: {self.health} \n Attack Power: {self.attack_power}")
 


#child class
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=25)
     #Pillar 3, polymorphism the methods are named the same, but have slightly different actions. Overridding inherited methods, is a form of polymorphism   
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} slashes at {opponent.name} with his sword, inflicting {self.attack_power} points of damage.")
        if opponent.health <= 0:
            print(f"{opponent.name} has perished!")
        else:
            print(f"{opponent.name} has {opponent.health}hp left. ")

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health= 90, attack_power=75)
    
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} casts meteor strike, smashing into {opponent.name} inflicting {self.attack_power} points of damage.")
        if opponent.health <= 0:
            print(f"{opponent.name} has perished!")
        else:
            print(f"{opponent.name} has {opponent.health}hp left. ")

class EvilWizard(Character):
    def __init__(self):
        super().__init__(name="Evil Wizard", health=150, attack_power=40)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerated 5 health! Current health: {self.health}")



#function to select and create a character
def create_character():
    name = input("Whats your name adventurer? ")
    print("Choose you character. 1. Warrior, 2. Mage")

    choice = input("Choose: ")
    if choice == "1":
        return Warrior(name)
    elif choice == "2":
        return Mage(name)
    

def battle(player, boss):
    while boss.health > 0 and player.health > 0:
        print('Your turn: 1. Attack, 2.View their stats')
        choice = input("Choose action: ")
        if choice == '1':
            player.attack(boss)
        elif choice == '2':
            player.display_stats()

        if boss.health > 0:
            boss.regenerate()
            boss.attack(player)


def main():
    player = create_character()
    wizard = EvilWizard()
    battle(player, wizard)

main()

