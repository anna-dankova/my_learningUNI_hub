import uuid
from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self,brand, model, year, power, price, fuel_type):
        self.__engine_id = str(uuid.uuid4())  
        self.brand : str = brand 
        self.model : str = model
        self.year : int =year
        self.power : int =power
        self.price : int=price 
        self.fuel_type : str= fuel_type


    @abstractmethod
    def calculate_fuel_consumption(self):
        result= self.power + 100
        return result

    @abstractmethod
    def get_vehicle_type(self):
        return "Легковой автомобиль"
    
    @abstractmethod
    def calculate_insurance(self):
         return self.price * 0.010


class Car(Vehicle):
    def __init__(self, brand, model, year, power, price, fuel_type,doors,transmission):
        super().__init__(brand, model, year, power, price, fuel_type)
        self.doors= doors
        self.transmission= transmission
    def calculate_fuel_consumption(self):
        return super().calculate_fuel_consumption()
    def get_vehicle_type(self):
        return super().get_vehicle_type()
    def calculate_insurance(self):
        return super().calculate_insurance()
class truck (Vehicle):
    def __init__(self, brand, model, year, power, price, fuel_type,weight,axle):
        super().__init__(brand, model, year, power, price, fuel_type)
        self.weight=weight
        self.axle=axle

car = Car("Toyota", "Camry", 2020, 150, 2500000, "petrol", 4, "auto")
print(car)