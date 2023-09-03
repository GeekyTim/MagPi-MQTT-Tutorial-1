# An Introduction to MQTT, by Tim Richardson

# Import the paho-mqtt client library.
import paho.mqtt.client as mqtt
from time import sleep


# A function to handle any messages received
def message_received(client, userdata, message):
    print("Message received on topic:", message.topic)
    print("Message contents:", message.payload.decode("utf-8"))


# Create an MQTT Client – the client ID must be unique
client = mqtt.Client("Recipient")

# Connect the client
client.connect("localhost")

# Define the 'callback' function when a message is received.
client.on_message = message_received

# Subscribe to a topic
client.subscribe("MyHouse/garage/temperature")

# Start listening for a message on the subscribed topics
client.loop_start()

print("Waiting for a message to be sent")

# Wait forever
while True:
    sleep(1)
