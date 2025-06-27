import abc

# 1. --- Abstract Products ---

class Light(abc.ABC):
    @abc.abstractmethod
    def get_description(self):
        """Returns light's description"""

class Speaker(abc.ABC):
    @abc.abstractmethod
    def get_description(self):
        """Returns speaker's description"""

class Thermostat(abc.ABC):
    @abc.abstractmethod
    def get_description(self):
        """Returns thermostat's description"""

# 2. --- Concrete Products ---

# Google family components
class Google_Light(Light):
    def get_description(self):
        return "Google Nest Light"

class Google_Speaker(Speaker):
    def get_description(self):
        return "Google Nest Audio Speaker"

class Google_Thermostat(Thermostat):
    def get_description(self):
        return "Google Nest Thermostat"

# Amazon family components
class Amazon_Light(Light):
    def get_description(self):
        return "Amazon Echo Light"

class Amazon_Speaker(Speaker):
    def get_description(self):
        return "Amazon Echo Speaker"

class Amazon_Thermostat(Thermostat):
    def get_description(self):
        return "Amazon Smart Thermostat"


# 3. --- Abstract Factory ---

class SmartHomeFactory(abc.ABC):
    @abc.abstractmethod
    def create_light(self):
        """Factory method to create light device"""
        pass

    @abc.abstractmethod
    def create_speaker(self):
        """Factory method to create speaker device"""
        pass

    @abc.abstractmethod
    def create_thermostat(self):
        """Factory method to create thermostat device"""
        pass

# 4. --- Concrete Factories ---

class GoogleFactory(SmartHomeFactory):
    def create_light(self):
        return Google_Light()

    def create_speaker(self):
        return Google_Speaker()

    def create_thermostat(self):
        return Google_Thermostat()

class AmazonFactory(SmartHomeFactory):
    def create_light(self):
        return Amazon_Light()

    def create_speaker(self):
        return Amazon_Speaker()

    def create_thermostat(self):
        return Amazon_Thermostat()


# 5. --- Client Function ---

def run(factory: SmartHomeFactory):
    """Simulates setting up smart home devices from a specific brand."""
    brand_name = factory.__class__.__name__.replace('Factory', '')
    print(f"\n--- Setting up {brand_name} Smart Home Devices ---")

    light = factory.create_light()
    speaker = factory.create_speaker()
    thermostat = factory.create_thermostat()

    print(f"  Light:       {light.get_description()}")
    print(f"  Speaker:     {speaker.get_description()}")
    print(f"  Thermostat:  {thermostat.get_description()}")
    print("-------------------------------------------------")

# 6. --- Client Code ---

if __name__ == "__main__":
    print("Welcome to the Smart Home Setup Configurator!")
    print("Choose a brand to setup devices for:")
    print("1. Google")
    print("2. Amazon")

    choice = input("Enter number (1 or 2): ").strip()

    chosen_factory: SmartHomeFactory = None

    if choice == "1":
        chosen_factory = GoogleFactory()
    elif choice == "2":
        chosen_factory = AmazonFactory()
    else:
        print("Invalid choice. Please select a valid brand.")
        exit()

    run(chosen_factory)

    print("\nSmart home device setup simulation complete.")
