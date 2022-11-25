#--------IMPORTS--------
import socket
import psutil
import GPUtil

#-------VARIABLES-------
classes = [] #----VARIABLE OF ALL CLASSES IN PC_Modules file----


#----DEVICE CALSSES-----
class Your_Class_Name():
    def __init__(self):
        self.Name = "Name_Of_Device"
        self.device_id = "device_id (May be only 0,1,2)"
        self.device_class_pref = "Prefix of device, anything text"
        self.device = (self.device_id, "Name_Of_sensor (Must end in _sensor or _binary_sensor)", "Device_Creator", "SoftWare version")
        self.model = "model_name"
        self.device_class = "monetary" # on site
        self.device_type = "sensor or binary_sensor"
    def get_value(self):
        self.data = #anything function like self.data = socket.gethostname()
        return self.data
classes.append(Your_Class_Name)

