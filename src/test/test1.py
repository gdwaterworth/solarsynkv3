import random
import time

from src.clients.mqtt_client import MqttClient as mqttclient  

def step_through_json(data, parent_key=''):
    if isinstance(data, dict):
        for key, value in data.items():
            current_key_path = f"{parent_key}.{key}" if parent_key else key
            step_through_json(value, current_key_path)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            current_key_path = f"{parent_key}[{index}]"
            step_through_json(item, current_key_path)
    else:
        print(f"Key Path: '{parent_key}', Value: '{data}', Type: {type(data).__name__}")


def run():
    client = mqttclient.connect_mqtt()
        
if __name__ == '__main__':
    run()
