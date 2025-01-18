class Car :                                                    # this is how we create a class
    def __init__(self, model, year, color, for_sale):          # this is how we intialize a constructor
        self.model = model                  # this is how you assign an object
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")