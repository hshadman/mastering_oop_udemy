class Apple:
    food_type = "fruit"
    calories_per_100_gram = 50
    def __init__(self, color, weight):
        self.color = color
        self.weight =weight
    def get_calories(self):
        return (self.weight/100)* self.calories_per_100_gram        

a1 = Apple('red', 100)
a2 = Apple('green', 150)

print(f"Apple a1 has {a1.get_calories()} calories")
print(f"Apple a2 has {a2.get_calories()} calories")