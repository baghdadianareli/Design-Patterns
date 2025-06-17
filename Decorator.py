class Coffee:
    def cost(self):
        return 5  # base cost (in dollars)

    def description(self):
        return "Basic coffee"

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()

class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1  # milk costs 1 dollar extra

    def description(self):
        return self._coffee.description() + ", Milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.5

    def description(self):
        return self._coffee.description() + ", Sugar"

class VanillaDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1.5

    def description(self):
        return self._coffee.description() + ", Vanilla"

class WhippedCreamDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return self._coffee.description() + ", Whipped Cream"

# Usage example
if __name__ == "__main__":
    my_coffee = Coffee()
    print(my_coffee.description(), "-> $", my_coffee.cost())

    my_coffee = MilkDecorator(my_coffee)
    my_coffee = SugarDecorator(my_coffee)
    print(my_coffee.description(), "-> $", my_coffee.cost())

    my_coffee = VanillaDecorator(my_coffee)
    my_coffee = WhippedCreamDecorator(my_coffee)
    print(my_coffee.description(), "-> $", my_coffee.cost())