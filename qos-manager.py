#Ping Response Time
import subprocess
import time
import datetime
import requests
import resources as rs


import paho.mqtt.client as mqtt , os
from urllib.parse import urlparse
import time


#python -m SimpleHTTPServer 8080
#ps aux | grep 'python'
#kill -9 pid
def response_time(nodename,node,th_ping,th_web):
    p_time=0
    i=0
    while True:
        p_time=0
        h_time=0
        i=0
        j=0
        k=0
        while True:           
            
            ping_time= ping_response_time(node)
            #http_time=http_response_time(node)
            p_time=p_time+ ping_time
            #h_time= h_time+float(http_time)
            if p_time!=0:
                j=j+1
            else:
                avai=0
                rs.update_nodeavai(nodename,0)                
                link=0
                rs.update_nodelink(nodename,0)
                break
            #if h_time!=0:
                #k=k+1
            time.sleep(1)
            i=i+1
            if i==3:
                #print("##############Aggregate Results:####################")
                #print("Node:",node)
                if p_time!=0:
                    #print("Average ping time:",round(p_time/j,2))
                    avai=1
                else:
                    #print("Average ping time:",0)
                    avai=0
                #if h_time!=0:
                    #c=2
                    #print("Average http time:",round(h_time/k,2))
                #else:
                    #c=2
                    #print("Average http time:",0)
                if p_time==0:
                    link=0
                elif p_time/j <th_ping:# and h_time/j <th_web:
                    link=3
                elif p_time/j <th_ping+1:# and h_time/i <th_web+1:
                    link=2
                else:
                    link=1
                
                break
        #print("Link Performance:",node,per)
        rs.update_nodelink(nodename,link)
        rs.update_nodeavai(nodename,avai)
        
        
    #return(per)
def reputation(th_rep):
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
        
        
    #return(per)

def ping_response_time(node):
    try:
        #print("-----")
        ping_response = subprocess.Popen(["/bin/ping", "-c1", "-w10", node], stdout=subprocess.PIPE).stdout.readlines()
        ping_time=float(ping_response[1].decode("utf-8")[ping_response[1].decode("utf-8").index("time=")+5:len(ping_response[1].decode("utf-8"))-3])
        #print("Ping response Time",ping_response[1].decode("utf-8")[ping_response[1].decode("utf-8").index("time=")+5:len(ping_response[1].decode("utf-8"))])
        
    except:
        #print("server is down")
        ping_time=0
    return(ping_time)
    
def http_response_time(node):
    #Web Server Reponse Time    
    url = 'http://'+node+ ':8080'     
    try:
        r = requests.get(url, timeout=6)
        r.raise_for_status()
        respTime = str(round(r.elapsed.total_seconds(),2))
        currDate = datetime.datetime.now()
        currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
        #print(currDate + " " + respTime)
        #print("Web response Time::", respTime, "s")
        #print("-----")
    except requests.exceptions.HTTPError as err01:
        #print ("HTTP error: ", err01)
        #print("-----")
        respTime=0
    except requests.exceptions.ConnectionError as err02:
        #print ("Error connecting: ", err02)
        #print("-----")
        respTime=0
    except requests.exceptions.Timeout as err03:
        #print ("Timeout error:", err03)
        #print("-----")
        respTime=0
    except requests.exceptions.RequestException as err04:
        #print ("Error: ", err04)
        #print("-----")
        respTime=0
    return(respTime)
    


# This publishes messages to cloudmqtt.com and also subscribes to it.
# Publishes an On/OFF messages to the Cloudmqtt
# At the other end - we have the Arduino sketch which is listening to this message
# and turns on and off the LEDs.

# Good example of a full end to end solution, 
# this code has to be run on a laptop, You will need a cloudmqtt account.
# at the other end you will have the Arduino sketch listening to messages and will print
# on the serial monitor


    
def on_connect(client, userdata,flags, rc):
    print ("on_connect:: Connected with result code "+ str ( rc ) )
    #print("rc: " + str(rc))
    print("" )
    client.subscribe ("/dl_AD")

def on_message(client, userdata, msg):
    #print ("on_message:: this means  I got a message from brokerfor this topic")
    #print("C2" + "," +msg.topic + ","+ str(msg.payload))
    print("Message from ADS: ")
    M=str(msg.payload)
    #print(str(msg.payload))
    #print(M)
    L=M.split(",")
    rs.update_noderep("FN1",L[1])
    rs.update_noderep("FN2",L[2])
    rs.update_noderep("FN3",L[3])
    rs.update_noderep("CN1",L[4])
    rs.update_noderep("CN2",L[5])
    rs.update_noderep("CN3",L[6][0:len(L[6])-1])
    #print("jjj",rs.look_for_noderep("CN3"))
    print("Reputation values:"," FN1:",L[1], " ,FN2:",L[2], " ,FN3:",L[3], " ,CN1:",L[4] , " ,CN2:",L[5], " ,CN3:",L[6])
    #print(L)
    
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



#response_time("192.168.1.149",0.5,0.5)


