

from turtle import end_fill

# Darius Price 11/28/2023

class Flower:             # This initializes the class flower
    def __init__(self, name): # this is a function that calls the class itself and its name
        self.name = name # these are the parameters that are being called in this function

    def grow(self): # this is another function that has a "self" parameter
        print("The " +self.name + " is growing.") # this is a print function that calls for the passed through object to be plugged into a string

    def bloom(self): # this is another function that has a "self" parameter
        print("The " + self.name + " is blooming.") # this calls for the passed through object to "bloom"

def main(): # a function called main with no parameters defined
    flower1 = Flower("Rose") # a variable which sets flower1 to be named "Rose"
    flower1.grow() # this line calls flower1 to grow, it will call the grow function when this function is called
    flower1.bloom() # calls flower 1 to the bloom function
    flower2 = Flower("Daisy") # a variable called flower2 being given the object Flower and name "Daisy"
    flower2.grow() # Calls Daisy to the grow function
    flower2.bloom() #Calls Daisy to bloom function
    flower3 = Flower("Tulip")

if __name__ == "__main__": #if function that says if the name parameter is equal to main 
  main() #calls the main function if the above if statement is true

  # The names like Rose and Daisy would be the attributes and the Grow and Bloom function would be methods