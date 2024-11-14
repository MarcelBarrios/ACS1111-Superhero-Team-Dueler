# my_dogs.py
from dog import Dog

my_dog = Dog("Rex", "SuperDog")
# Remember python implicitly passes in "self",
# so we don't need to pass it in when we call the function!
my_dog.bark()

my_other_dog = Dog("Annie", "SuperDog")
print(my_other_dog.name)

my_other_dog1 = Dog("Rocky", "SuperMegaDog")
print(my_other_dog.name)
print(my_other_dog1.bark())

my_other_dog2 = Dog("Jet", "Snowcsher")
print(my_other_dog.name)
print(my_other_dog2.sit())

my_other_dog3 = Dog("Lee", "German Sheppard")
print(my_other_dog.name)
print(my_other_dog3.roll_over())
