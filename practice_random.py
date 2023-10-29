class Car:
    def __init__(self,color,model,year):
        self._color = color
        self.__model = model
        self.__year_ = year

c = Car("red", "Toyota", 2020)

c._Car_color = "green"
#c.__model = 'xyz'

print(c._color, c._Car_color, c._Car__year_)