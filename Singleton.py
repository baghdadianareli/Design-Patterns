class NationalFlag:
    _instance = None

    def __new__(cls, name=None, colors=None, symbol=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._name = name
            cls._instance._colors = colors
            cls._instance._symbol = symbol
        return cls._instance

    def describe(self):
        print(f"National Flag: {self._name}")
        print(f"Colors: {', '.join(self._colors)}")
        print(f"Symbol: {self._symbol}")

    def update_flag(self, name, colors, symbol):
        print("Attempting to update flag...")
        self._name = name
        self._colors = colors
        self._symbol = symbol
        print("Flag updated!")


# Example usage
if __name__ == "__main__":
    # First creation
    flag1 = NationalFlag(name="Armenia", colors=["Red", "Blue", "Orange"], symbol="None")
    flag1.describe()

    print("\n--- Another attempt to create a different flag ---")
    
    # Another creation attempt
    flag2 = NationalFlag(name="France", colors=["Blue", "White", "Red"], symbol="None")
    flag2.describe()

    print("\n--- Updating the flag ---")
    flag2.update_flag("Japan", ["White", "Red"], "Circle")
    flag1.describe()  # Both flag1 and flag2 refer to the same flag

    # Verify singleton
    print("\nflag1 is flag2:", flag1 is flag2)
