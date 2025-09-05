class Base_class:
    pass
class Derived_one(Base_class):
    pass
class Derived_two(Base_class):
    pass
class Derived_three(Derived_one,Derived_two): # The total format of inheritance is called hybrid inheritance
    pass


class Vehicle:
    def show_vehicle_info(self):
        print("This is a vehicle.")


class Car(Vehicle):
    def show_car_info(self):
        print("This is a car.")


class Bike(Vehicle):
    def show_bike_info(self):
        print("This is a bike.")


class ElectricVehicle(Car, Bike):
    def show_electric_info(self):
        print("This is an electric vehicle.")



ev = ElectricVehicle()

ev.show_vehicle_info()   
ev.show_car_info()      
ev.show_bike_info()      
ev.show_electric_info()  


# hierarchial inheritance

# Base class
class Animal:
    def sound(self):
        print("Animals make different sounds.")

# Dog inherits Animal
class Dog(Animal):
    def sound(self):
        print("Dog barks.")

# Cat inherits Animal
class Cat(Animal):
    def sound(self):
        print("Cat meows.")

# Cow inherits Animal
class Cow(Animal):
    def sound(self):
        print("Cow moos.")


# Create objects
dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()  # From Dog
cat.sound()  # From Cat
cow.sound()  # From Cow
