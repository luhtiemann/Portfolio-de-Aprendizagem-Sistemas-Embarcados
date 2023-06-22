import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

def temp(client, userdata, message):
    print("Tópico: ", str(message.topic))
    print("Msg: " ,str(message.payload.decode("utf-8")))  
    if float(message.payload.decode("utf-8")) >= 50.1:
        client.publish("/Luana/Buzzer", 1)
    else:
        client.publish("/Luana/Buzzer", 0)


mqttBroker ="broker.hivemq.com"
client = mqtt.Client("Luana")
client.connect(mqttBroker) 
client.message_callback_add("/Luana/comando", temp)
client.subscribe("/Luana/comando")
client.loop_forever()