import uuid
import random
from abc import ABC, abstractmethod


class Controllable(ABC):
    @abstractmethod
    def turn_on (self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class Readable (ABC):
    @abstractmethod
    def read_value(self):
         pass
    
class Device (Controllable):

    def __init__(self, name: str):
        name_clean = name.strip()
        if not name_clean or len(name_clean) < 3:
            raise ValueError(f"Имя '{name}' слишком короткое (нужно 3+ символа)")
        self.name = name_clean
        self.device_id = str(uuid.uuid4())    
        self._status = False
        self.power_usage = 0                   

    def turn_off(self):
        self.status = False

    def turn_on(self):
        self.status = True


    @property
    def status(self):
        return self._status

    @status.setter        
    def status(self,value):
        if isinstance(value, bool):
            self._status=value
        else:
            raise ValueError(f"Status только True/False, а не {value}")
        

    def get_status(self):
         return{
            "name": self.name,
            "status" : self._status,
            "id": self.device_id,
        }
    
  

class Light(Device):    
    def __init__(self, name: str, brightness: int = 100):
        super().__init__(name)
        self.brightness : int = brightness

    def get_status(self):
        base_status = super().get_status()
        base_status["brightness"]= self.brightness
        return base_status

    def set_brightness(self, level: int):
        if 0<=level <= 100:
            self.brightness= level
        else:
            print(f"Ошибка: яркость должна быть 0-100, получено {level}")
        

class Thermostat(Device):
    def __init__(self, name: str, target_temp: float = 21.0):
         super().__init__(name)
         self.target_temp: float = target_temp
        
    def get_status(self):
        base_status= super().get_status()
        base_status["target_temp"] = self. target_temp
        return base_status
    
    def set_target_temp(self, temp: float):
        if 15  <=  temp <= 30:
           self.target_temp= temp
        else: 
            print(f"Ошибка: температура должна быть 15-30 , получено {temp}")
           

class DeviceManager:
    def __init__(self):
        self._devices: list[Device] = [] 
        self.rooms: list[Room] = []

    @property
    def devices (self):
        return list(self._devices)

    def add_device(self, device: Device):
        for d in self._devices:
            if d.name == device.name:
                print("Устройство с таким именем уже есть!")
                return
        self._devices.append(device)
    
    def remove_device(self, name :str):
        self._devices= [d for d in self._devices if d.name != name ]
    
    def get_all_devices(self):
        return [d.get_status() for d in self.devices] 
    
    def find_by_name(self, name: str):
        for device in self.devices:
            if device.name == name:
                return device
        return None
    
    def add_room(self, room :Room):
        self.rooms.append(room)

    def get_room_status(self):
        return [room.get_status() for room in self.rooms]
    
    def turn_on_all_controllable(self):
        for d in self._devices:
            if isinstance(d, Controllable) and not isinstance(d, Readable):
                d.turn_on()
                print (f"Включено: {d.name}")

    def read_all_sensors(self):
        results ={}
        for d in self._devices:
            if isinstance(d,Readable):
                results[d.name] =d.read_value()
        return results
    
    def get_controllable_devices(self):
        return [d for d in self._devices
                if isinstance(d,Controllable) and not isinstance(d, Readable)]
    
    def get_sensors(self):
        return [d for d in self._devices if isinstance(d, Readable)]

class Room:
    def __init__(self, name: str):
        self.name: str = name
        self.devices: list[Device] = [] 
    
    def add_device(self, device: Device):
        for d in self.devices:
            if d.name ==  device.name :
                print(f"В комнате '{self.name}' устройство '{device.name}' уже есть! ")
                return
        self.devices.append(device)
        print(f"Добавлено: {device.name}")

    def turn_all_on(self):
        for d in self.devices:
            d.turn_on()
    
    def get_status(self):
        return {
            "room": self.name,
            "devices": [d.get_status() for d in self.devices]
        }
    
    def remove_device(self, device_name : str):
        self.devices = [d for d in self.devices if d.name != device_name]

class Sensor (Device, Readable):

    def __init__ (self,name :str):
        super().__init__(name)
        

    def read_value (self):
         self.current_value= random.uniform(15, 25)
         return self.current_value
        
class TemperatureSensor(Sensor):
    def __init__(self, name :str):
        super().__init__(name); 
        self.current_value =21.0

    def read_value(self):
        self.current_value= random.uniform (15, 30)
        return self.current_value

    def get_status(self):
        base = super().get_status()
        base["temp"]= self.current_value
        return base

class MotionSensor(Sensor):
    def __init__(self, name : str):
        super().__init__(name)
        self.motion_detected : bool = False

    def read_value(self):
        self.motion_detected=random.choice([True, False])
        return self.motion_detected
        
    def get_status(self):
        base_status=super().get_status()
        base_status["motion"]= self.motion_detected
        return base_status  
    


    

###
manager = DeviceManager()
manager.add_device(Light("Гостиная лампа", 70))
manager.add_device(Thermostat("Спальня термостат", 22.0))
manager.add_device(TemperatureSensor("Коридор температура"))
manager.add_device(MotionSensor("Дверь сенсор"))

print("=== Включаем управляемые устройства ===")
manager.turn_on_all_controllable()

print("\n=== Читаем все датчики ===")
print(manager.read_all_sensors())

print("\n=== Только управляемые ===")
print([d.name for d in manager.get_controllable_devices()])

print("\n=== Только датчики ===")
print([d.name for d in manager.get_sensors()])



###