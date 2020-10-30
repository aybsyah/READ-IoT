# This publishes messages to cloudmqtt.com and also subscribes to it.
# Publishes an On/OFF messages to the Cloudmqtt
# At the other end - we have the Arduino sketch which is listening to this message
# and turns on and off the LEDs.

# Good example of a full end to end solution, 
# this code has to be run on a laptop, You will need a cloudmqtt account.
# at the other end you will have the Arduino sketch listening to messages and will print
# on the serial monitor

import paho.mqtt.client as mqtt , os
from urllib.parse import urlparse
import time

# Define event callbacks
    
def on_connect(client, userdata,flags, rc):
    print ("on_connect:: Connected with result code "+ str ( rc ) )
    #print("rc: " + str(rc))
    print("" )
    client.subscribe ("/dl_AD")

def on_message(client, userdata, msg):
    print ("on_message:: this means  I got a message from brokerfor this topic")
    print("C2" + "," +msg.topic + ","+ str(msg.payload))
    #print("C2",msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    print ("")

def on_publish(client, obj, mid):
    #print("mid: " + str(mid))
    print ("")

def on_subscribe(client, obj, mid, granted_qos):
    print("This means broker has acknowledged my subscribe request")
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(  string)

def connect_first():
    #client = mqtt.Client()
    # Assign event callbacks
    client.on_message = on_message
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_subscribe = on_subscribe

    # Uncomment to enable debug messages
    client.on_log = on_log


    # user name has to be called before connect - my notes.
    client.username_pw_set("bqtlnmdl", "kURwL4XwAFT9")
    client.connect('m21.cloudmqtt.com', 12152,60)
    #return client

    # Continue the network loop, exit when an error occurs
    #rc = 0
    #while rc == 0:
    #    rc = client.loop()
    #print("rc: " + str(rc))

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    #client.loop_forever()

    #client.publish ( "/hi", "from python code")
    #client.publish  ( "/dl_detection", "ON" )
    #client.publish ( "/hi", "from python code")
    #client.publish  ( "/dl_detection", "ON" )

    #client.loop_start()
    #client.subscribe ("dl_detection/#" ,0 )

def start_publish():
    #client.loop_forever()
    client.loop_start()
    time.sleep(1)
    run = True
    while run:
        #client.publish ( "/hi", "from python code")
        client.publish  ( "/dl_AD", "ON" )
        time.sleep(10)
        #client.publish ( "/dl_AD", "OFF")
        #time.sleep(2)
    client.loop_stop()

    
def publisher(message):
    #client = mqtt.Client()
    client.publish( "/dl_AD", message)

if __name__ == '__main__':
    client = mqtt.Client("my-paho-client")
    client.on_connect = on_connect
    #client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    #client.on_unsubscribe = on_unsubscribe
    client.username_pw_set("bqtlnmdl", "kURwL4XwAFT9")
    client.connect('m21.cloudmqtt.com', 12152,60)
    #client.subscribe ("/dl_detection")
    client.loop_forever()
   