class Apple:
    food_type = "fruit"
    calories = 50
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def set_color(self, color):
        print(f'self has id {id(self)}')
        print(f'class of self has id {id(self.__class__)}')
        #self.color = color
        self.__class__.food_type = "sweet fruit"
a = Apple("red", 100)
print(f'id of instance a is {id(a)}')
print(f'id of class Apple is {id(Apple)}')

a.set_color("green")
print(a.food_type)