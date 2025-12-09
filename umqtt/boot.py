import network
import time
from machine import Pin
import dht
import ujson
from umqtt.simple import MQTTClient

# MQTT Server Parameters
MQTT_CLIENT_ID = "Gargi_test"
MQTT_BROKER    = "broker.f4.htw-berlin.de"
MQTT_TOPIC     = "ProIT_IoT/Gargi"
MQTT_TOPIC_TEMP = "ProIT_IoT/Gargi/temp"
MQTT_TOPIC_HUMI = "ProIT_IoT/Gargi/humi"

sensor = dht.DHT22(Pin(2))

print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Rechnernetze', 'rnFIW625')
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Connected!")

print("Connecting to MQTT server... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER,)
client.connect()

print("Connected!")

prev_weather = ""
while True:
    sensor.measure() 
    mytemp= sensor.temperature()
    myhumi= sensor.humidity()
    print("Updated")
    client.publish(MQTT_TOPIC_TEMP, str(mytemp))
    client.publish(MQTT_TOPIC_HUMI, str(myhumi))

    time.sleep(10)

