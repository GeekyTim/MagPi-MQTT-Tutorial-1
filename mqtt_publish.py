# An Introduction to MQTT, by Tim Richardson

# Import the paho-mqtt client library.
import paho.mqtt.client as mqtt

# Create an MQTT Client – the client ID must be unique
client = mqtt.Client("Sender")

# Connect the client
client.connect("localhost")

# Publish a message to the MyHouse/garage/temperature topic
client.publish("MyHouse/garage/temperature", "13.2")
