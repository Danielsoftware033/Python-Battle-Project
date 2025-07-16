import random



class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = 20
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} heals for {heal_amount}. Current health: {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")




class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def special_ability(self, opponent):
        print(f"{self.name} uses 'Berserk Smash'!")
        damage = self.attack_power + 15
        opponent.health -= damage
        print(f"{self.name} deals {damage} damage!")

    def special_ability_2(self, opponent):
        print(f"{self.name} uses 'Furious Blow'!")
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} lands a massive {damage} damage critical hit!")




class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_ability(self, opponent):
        print(f"{self.name} casts 'Fireball Rain'!")
        damage = self.attack_power + random.randint(10, 20)
        opponent.health -= damage
        print(f"{self.name} deals {damage} magic damage!")

    def special_ability_2(self, opponent):
        print(f"{self.name} casts 'Ice Bind'! {opponent.name}'s next attack will be skipped.")
        opponent.skip_next_turn = True




class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
        self.skip_next_turn = False

    def regenerate(self):
        regen = 5
        self.health = min(self.health + regen, self.max_health)
        print(f"{self.name} regenerates {regen} health. Current health: {self.health}/{self.max_health}")




class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=20)
        self.evade_next = False

    def special_ability(self, opponent):
        print(f"{self.name} uses 'Quick Shot'!")
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} fires two arrows for {damage} damage!")

    def special_ability_2(self, opponent):
        self.evade_next = True
        print(f"{self.name} uses 'Evade' and will dodge the next attack!")




class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=22)
        self.shield_active = False

    def special_ability(self, opponent):
        print(f"{self.name} uses 'Holy Strike'!")
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"{self.name} deals {damage} holy damage!")

    def special_ability_2(self, opponent):
        self.shield_active = True
        print(f"{self.name} activates 'Divine Shield' and will block the next attack!")




def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)



def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Use Second Ability")
        print("4. Heal")
        print("5. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.special_ability_2(wizard)
        elif choice == '4':
            player.heal()
        elif choice == '5':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            print("\n--- Wizard's Turn ---")
            wizard.regenerate()

            if wizard.skip_next_turn:
                print(f"{wizard.name} is frozen and misses this turn!")
                wizard.skip_next_turn = False
                continue

            if isinstance(player, Archer) and player.evade_next:
                print(f"{player.name} evades the attack!")
                player.evade_next = False
            elif isinstance(player, Paladin) and player.shield_active:
                print(f"{player.name} blocks the attack with Divine Shield!")
                player.shield_active = False
            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}! Victory!")



def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()


