class Zookeeper:
    def __init__(self, name):
        self.name = name

    def clean_cage(self, cage):
        if not cage.is_clean:
            cage.is_clean = True
            print(f"{self.name} cleaned the cage.")
        else:
            print(f"The cage is already clean.")

    def feed_animal(self, animal):
        if animal.is_hungry:
            animal.is_hungry = False
            print(f"{self.name} fed the {animal.species}")
        else:
            print(f"{animal.species} is not hungry.")


class Cage:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.is_clean = False
        self.is_open = False

    def open_cage(self):
        self.is_open = True
        print(f"{self.name} cage is open.")

    def close_cage(self):
        self.is_open = False
        print(f"{self.name} cage is closed.")


class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.is_hungry = True
        self.is_happy = False

    def check_happy(self, cage):
        self.is_happy = not self.is_hungry and cage.is_clean
        mood = "happy" if self.is_happy else "unhappy"
        print(f"{self.species} {self.name}  is {mood}.")


def main():
    keeper = Zookeeper("Bob")

    monkey_cage = Cage("Monkey`s")
    monkey = Animal("Monkey", "Makaka")
    monkey_cage.animals.append(monkey)

    beaver_cage = Cage("Beaver`s")
    beaver = Animal("Beaver", "Bobrik")
    beaver_cage.animals.append(beaver)

    wolf_cage = Cage("Wolf`s")
    wolf = Animal("Wolf", "Sigma-Alpha")
    wolf_cage.animals.append(wolf)

    print("Day starts...")
    """open animal`s cages"""
    monkey_cage.open_cage()
    beaver_cage.open_cage()
    wolf_cage.open_cage()

    """check if animals are happy"""
    monkey.check_happy(monkey_cage)
    beaver.check_happy(beaver_cage)
    wolf.check_happy(wolf_cage)

    """Bob feed animals, clean cages and check if animals are happy"""
    keeper.feed_animal(monkey)
    keeper.clean_cage(monkey_cage)
    monkey.check_happy(monkey_cage)

    keeper.feed_animal(beaver)
    keeper.clean_cage(beaver_cage)
    beaver.check_happy(beaver_cage)

    keeper.feed_animal(wolf)
    keeper.clean_cage(wolf_cage)
    wolf.check_happy(wolf_cage)

    """close cages"""
    monkey_cage.close_cage()
    beaver_cage.close_cage()
    wolf_cage.close_cage()

    print("Day ended.")


if __name__ == "__main__":
    main()
