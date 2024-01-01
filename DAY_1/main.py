class Animal: #base class
    def speak(self):
        return "sound"

class Dog(Animal): #derived class
    def speak(self):
        return "Woof! Woof!"

    def speak_with_generic_sound(self):
        return super().speak()  #initializes the method from the base class


dog = Dog()
print(dog.speak())                  
print(dog.speak_with_generic_sound())  
