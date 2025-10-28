# MQTT

## Installing MQTT Broker on Raspberry
im Terminal des Raspberry Pi

<code>sudo apt-get install mosquitto</code>

<code>sudo apt-get install mosquitto-clients -y</code>

See also tutorial:

https://diyi0t.com/microcontroller-to-raspberry-pi-wifi-mqtt-communication/

### Configuration

Editing config-file (with Nano or another editor e.g. mousepad)

<code>sudo nano /etc/mosquitto/mosquitto.conf </code>

coment out:
`#include_dir /etc/mosquitto/conf.d`

add the following lines:
```
allow_anonymous false
listener 1883
```

Mosquitto service restart:

<code>sudo systemctl restart mosquitto</code>

Start Mosquitto service at boot:

<code>sudo systemctl enable mosquitto</code>

