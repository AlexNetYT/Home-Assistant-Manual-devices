
# Importing the library

import PC_Modules
from PC_Modules import *
import json
import paho.mqtt.client as mqtt
#-------MQTT Brocker--------
brocker = ['localhost', "1883"]                         #Replace localhost to your MQTT brocker IP
#---------Functions---------
def discovery(PCdevice):
    client_id = PCdevice.device[0] + '_' + PCdevice.device[1]
    client = mqtt.Client(client_id)
    client.connect(str(brocker[0]), int(brocker[1]))
    topic = f'homeassistant/{PCdevice.device_type}/{client_id}/system/config'
    json_name = PCdevice.device[0] + '_system' + PCdevice.Name + '_sensor'
    json_topic = client_id + '/system'
    payload = json.dumps({
        "device": {
                "identifiers": [client_id],
                "name": client_id,
                "model": PCdevice.model,
                "manufacturer": "sascha@orlanm.ru",
                "sw_version": "0.0.1A"},
        "device_class": PCdevice.device_class, 
        "name": json_name, 
        "payload_off": False, 
        "payload_on": True, 
        "state_topic": json_topic, 
        "unique_id": client_id
        })
    client.publish(topic, payload)
def send_data(PCdevice):
    value = PCdevice.get_value()
    client_id = PCdevice.device[0] + '_' + PCdevice.device[1]
    client = mqtt.Client(client_id)
    client.connect(str(brocker[0]), int(brocker[1]))
    topic = client_id + '/system' 
    client.publish(topic,str(value))
#---------Main Code---------
if __name__ == '__main__':
    while True:
        for Sensor in PC_Modules.classes:
            discovery(Sensor)                           #Send Discovery topic to MQTT
            send_data(Sensor)                           #Send Data topic to MQTT
