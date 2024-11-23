class Kettle(object):

    # Class attribute
    power_source: str = "electricity"

    def __init__(self, make: str, price: float) -> None:
        self.make: str = make
        self.price: float = price
        self.on: bool = False

    def switch_on(self) -> None:
        self.on = True


def main() -> None:
    kenwood: Kettle = Kettle("Kenwood", 8.99)
    print(kenwood.make)
    print(kenwood.price)

    kenwood.price = 12.75
    print(kenwood.price)

    hamilton: Kettle = Kettle("Hamilton", 14.55)

    print(
        f"Models: {kenwood.make} = {kenwood.price}, {hamilton.make} = {hamilton.price}"
    )

    print(hamilton.on)
    hamilton.switch_on()
    print(hamilton.on)
    Kettle.switch_on(kenwood)
    print(kenwood.on)

    #! Althought this works, it is not a good practice to add attributes outside the class
    #! The variable power is now an attribute of the kenwood object
    kenwood.power = 1.5
    print(kenwood.power)
    #! But not for the hamilton object
    # print(hamilton.power) # AttributeError: 'Kettle' object has no attribute 'power'

    print(Kettle.power_source)
    print(kenwood.power_source)
    print(hamilton.power_source)


if __name__ == "__main__":
    """
    Class:          Template for creating objects. All objects created using the same class will have the same characteristics.
    Object:         An instance of a class.
    Instantiate:    Create an instance of a class.
    Method:         A function defined in a class.
    Attribute:      A variable bound to an instance of a class.
    """
    main()
