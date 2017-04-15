## Animal is-a object (yes, sort of confusing) look at teh extra credit
class Animal(object):

    def rawr(self):
        print "ROAR!"

    pass

## Dog is-a Animal that has-a name
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

    def wolf(self):
        print "Bark Bark I am %s Bark!" % self.name

## Cat is-a Animal that has-a name
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

    def meow(self):
        print "I am a cat. I go meow. BTW my name is %s ." % self.name

## Person is-a object that has-a name and pet
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ##Person has-a pet of some kind
        self.pet = None

## Employee is-a Person that has-a salary
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

rover.wolf()
rover.rawr()



## sata is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## ??
mary.pet = satan




## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

frank.pet.wolf()

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
