class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def moves(self):
        print('and I move along...')
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle('Tesla', 'Model 3')

my_car.get_make_model()
my_car.moves()

your_car = Vehicle("Ferrari", "Roma")

your_car.get_make_model()
your_car.moves()

class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id
    def moves(self):
        print("and I fly along...")
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model} and my id number is {self.faa_id}.")

class Truck(Vehicle):
    def moves(self):
        print("and I rumble along...")

class Golf_Cart(Vehicle):
    pass

airbus = Airplane("Airbus", "A300", "f-1356")
tonka = Truck("Tonka", "Big Yellow Dump Truck")
golf_dragster = Golf_Cart("Ford", "Speedster")

airbus.get_make_model()
tonka.get_make_model()
golf_dragster.get_make_model()

# An easier way to call all of these objects would be with a loop.
print('\n\n')

for v in(my_car, your_car, airbus, tonka, golf_dragster):
    v.get_make_model()
    v.moves()