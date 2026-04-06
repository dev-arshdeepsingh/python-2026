# class Car:
#     car_count = 0
#     def __init__(self, userbrand, usermodel):
#         self.brand = userbrand
#         self.model = usermodel
#         Car.car_count +=1

#     def print_data(self):
#         return f"{self.brand} {self.model}"
    
# class Electric_car(Car):
#     def __init__(self, b, m, battery):
#         super().__init__(b, m)
#         self.battery = battery


# # my_Tesla = Electric_car("Teslaa", "S", "85KWh")
# # print(my_Tesla.model)
# # print(my_Tesla.print_data())
# # print(my_Tesla.battery)



# # my_car = Car("Toyota", "Fortuner")
# # print(my_car.brand)
# # print(my_car.model)

# my_car = Car("Tata", "Nexa")
# Electric_car("Tesla", "S", "85")
# print("CAR=",Car.car_count)


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    @property
    def model(self):
        return self.__model
    
my_car = Car("Tata", "City")
print(my_car.model)
my_car.model = "Honda"