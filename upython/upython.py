import paho.mqtt.client as mqtt

brokerURL="broker.f4.htw-berlin.de"
brokerPort=1883

def on_connect(client, userdata, flags, rc):
   print("Connected with result code "+str(rc))

def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))
    
def on_disconnect(client, userdata, rc):
   print("Client Got Disconnected!!!")

mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect
mqttclient.on_message = on_message
mqttclient.on_disconnect = on_disconnect

mqttclient.connect(brokerURL, brokerPort) #call connect function with URL and port number

mqttclient.publish("ProIT_IoT/Gargi","It works!")

mqttclient.subscribe("ProIT_IoT/#")
mqttclient.subscribe("ProIT_IoT/+/temp")
mqttclient.subscribe("ProIT_IoT/+/humi")
mqttclient.loop_start()