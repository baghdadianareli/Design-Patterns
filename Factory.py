import abc

class iCharacter(abc.ABC):
    @abc.abstractmethod
    def character_function(self):
        """___"""

class Ironman(iCharacter):
    def __init__(self):
        self.name = "Character name"
        self.show = "Character show"

    def character_function(self):
        print("I am Ironman.")
        
class CaptainAmerica(iCharacter):
    def __init__(self):
        self.name = "Character name"
        self.show = "Character show"

    def character_function(self):
        print("I am Captain America.")

class Supersonic(iCharacter):
    def __init__(self):
        self.name = "Character name"
        self.show = "Character show"

    def character_function(self):
        print("I am Super Sonic.")


class iCharacterCreator(abc.ABC):
    @abc.abstractmethod
    def create_character(self):
        """Factory method"""

class IronmanCreator(iCharacterCreator):
    def create_person(self):
        return Ironman()

class CaptainAmericaCreator(iCharacterCreator):
    def create_person(self):
        return CaptainAmerica()

class SupersonicCreator(iCharacterCreator):
    def create_person(self):
        return Supersonic()


def main():
    character_type = input("Choose Ironman/Captain America/Supersonic: ")
    
    factory = None
    if character_type == "Ironman":
        factory = IronmanCreator()
    elif character_type == "Captain America":
        factory = CaptainAmericaCreator()
    elif character_type == "Supersonic":
        factory = SupersonicCreator()
    else:
        print("Invalid input")
        return
    
    person = factory.create_character()
    person.character_function()

if __name__ == "__main__":
    main()
