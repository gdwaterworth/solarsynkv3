import random
import time
import json
from paho.mqtt import client as mqtt_client
from src.configuration.configuration import Configuration
# "MQTT_Server": "",
# "MQTT_Port": 0,
# "MQTT_Login": "",
# "MQTT_Pass": ""

topic = "python/mqtt"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    with open('/data/options.json') as options_file:
        json_settings = json.load(options_file)
    username = json_settings["MQTT_Login"]
    print(f"Login: `{username}`")
    password = json_settings["MQTT_Pass"]
    print(f"Password: `{password}`")
    broker = json_settings["MQTT_Server"]
    print(f"Broker: `{broker}`")
    port = json_settings["MQTT_Port"]
    print(f"Port: `{port}`")
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
        msg = f"messages: 1"
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

