class Pizza:
    def __init__(self, size, dough, sauce, toppings):
        self.size = size
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    def __str__(self):
        return (f"Pizza ({self.size}): {self.dough} dough, "
                f"{self.sauce} sauce, toppings: {', '.join(self.toppings) if self.toppings else 'None'}")


class PizzaBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.pizza = Pizza(None, None, None, [])

    def set_size(self): pass
    def set_dough(self): pass
    def set_sauce(self): pass
    def add_toppings(self): pass

    def build(self):
        return self.pizza


class VeggiePizzaBuilder(PizzaBuilder):
    def set_size(self):
        self.pizza.size = "medium"

    def set_dough(self):
        self.pizza.dough = "thin crust"

    def set_sauce(self):
        self.pizza.sauce = "tomato basil"

    def add_toppings(self):
        self.pizza.toppings = ["bell peppers", "onions", "olives", "mushrooms", "spinach"]


class MeatLoversPizzaBuilder(PizzaBuilder):
    def set_size(self):
        self.pizza.size = "large"

    def set_dough(self):
        self.pizza.dough = "thick crust"

    def set_sauce(self):
        self.pizza.sauce = "barbecue"

    def add_toppings(self):
        self.pizza.toppings = ["pepperoni", "sausage", "ham", "bacon"]


class PizzaDirector:
    def __init__(self, builder):
        self._builder = builder

    def construct_pizza(self):
        self._builder.reset()
        self._builder.set_size()
        self._builder.set_dough()
        self._builder.set_sauce()
        self._builder.add_toppings()
        return self._builder.build()


if __name__ == "__main__":
    director = PizzaDirector(VeggiePizzaBuilder())
    pizza1 = director.construct_pizza()
    print("== Veggie Pizza ==\n")
    print(f"{pizza1}\n")

    director = PizzaDirector(MeatLoversPizzaBuilder())
    pizza2 = director.construct_pizza()
    print("== Meat Lovers Pizza ==\n")
    print(f"{pizza2}\n")
    