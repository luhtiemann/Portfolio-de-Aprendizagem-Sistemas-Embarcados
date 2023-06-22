import paho.mqtt.client as mqtt
import time

def sub_temperatura(client, userdata, message):
    print("Tópico: ", str(message.topic))
    print("Msg: " ,str(message.payload.decode("utf-8")))
    


mqttBroker ="broker.hivemq.com"
client = mqtt.Client("Subscreve")
client.connect(mqttBroker) 

client.message_callback_add("/NomeDoTopico", sub_temperatura)
client.subscribe("/NomeDoTopico")

client.message_callback_add("/NomeDoSegundoTopico", sub_temperatura)
client.subscribe("/NomeDoSegundoTopico")


client.loop_forever()




