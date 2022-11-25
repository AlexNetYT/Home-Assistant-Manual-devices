# Home-Assistant-Manual-devices
## RU Готовая библиотека привязки и создания своих устройств через MQTT к Home Assistant

В репозитории представлено два файла [main.pyw](https://github.com/AlexNetYT/Home-Assistant-Manual-devices/edit/main/README.md#mainpy) и [PC_Modules.py](https://github.com/AlexNetYT/Home-Assistant-Manual-devices/edit/main/README.md#pc_modulespy)
Настройки каждого из них ниже:
# Требования
````python
pip install json
````
````python
pip install paho
````
## Main.py:
Настроить в данном файле вам нужно всего лишь вашего MQTT брокера:
				
				brocker = ['localhost', "1883"] #Замените localhost на IP вашего MQTT брокера
				
## PC_Modules.py:
Настраивать здесь ничего не нужно, этот файл служит для добавления новых устройств(модулей) в ваш home assistant
#### Настройка класса:
```python
class Your_Class_Name():						# Имя вашего модуля (Может быть любым)
    def __init__(self):
        self.Name = "Name_Of_Device"						# Имя вашего модуля (Может быть любым)
        self.device_id = "0"						#device ID (Может быть только 0,1 или 2)
        self.device_class_pref = "prefix"	 #Префикс устройства (Может быть любым)
        self.device = (self.device_id, "Название_сенсора (Должно оканчиваться на _sensor или _binary_sensor)", "Создатель устройства", "Версия ПО устройства")	# (Может быть любым)
        self.model = "model_name"						# Имя вашего модуля (Может быть любым)
        self.device_class = "monetary"					# Класс вашего устройства. Приведены ниже
        self.device_type = "sensor" #Тип устройства
    def get_value(self):
        self.data = #Любая функция, например: self.data = socket.gethostname()
        return self.data
classes.append(Your_Class_Name)
```
#### [device_class для sensor](https://www.home-assistant.io/integrations/sensor/ "device_class для sensor")
#### [device_class для binaty_sensor](https://www.home-assistant.io/integrations/binary_sensor/ "device_class для binaty_sensor")


# ENG (Google translate) Home-Assistant-Manual-devices
## Ready-made library for binding and creating your own devices via MQTT to Home Assistant

The repository contains two files main.pyw and PC_Modules.py
The settings for each are below:
# Requirements
````python
pip install json
````
````python
pip install paho
````
## Main.py:
You only need to configure your MQTT broker in this file:

brocker = ['localhost', "1883"] #Replace localhost with the IP of your MQTT broker

## PC_Modules.py:
You do not need to configure anything here, this file is used to add new devices (modules) to your home assistant
#### Class setting:
```python
class Your_Class_Name(): # Name of your module (Can be anything)
    def __init__(self):
        self.Name = "Name_Of_Device" # Name of your module (Can be anything)
        self.device_id = "0" #device ID (Can only be 0,1 or 2)
        self.device_class_pref = "prefix" #Device prefix (can be anything)
        self.device = (self.device_id, "Sensor_Name (Must end with _sensor or _binary_sensor)", "Device Creator", "Device Firmware Version") # (Can be anything)
        self.model = "model_name" # Name of your module (can be anything)
        self.device_class = "monetary" # Your device class. Given below
        self.device_type = "sensor" #Device type
    def get_value(self):
        self.data = #Any function, for example: self.data = socket.gethostname()
        return self.data
classes.append(Your_Class_Name)
```
#### [device_class for sensor](https://www.home-assistant.io/integrations/sensor/ "device_class for sensor")
#### [device_class for binaty_sensor](https://www.home-assistant.io/integrations/binary_sensor/ "device_class for binaty_sensor")


# [Telegram](https://t.me/AlexDot_Net "Telegram") for communication
