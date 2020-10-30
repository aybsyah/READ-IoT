import subprocess
import threading
import check

def begin_thread():
    thread1 = threading.Thread(target=check.response_time, args=("192.168.1.149",0.5,0.5, ))
    thread2 = threading.Thread(target=check.response_time, args=("34.244.126.183",0.5,0.5, ))
    thread3 = threading.Thread(target=check.response_time, args=("54.77.247.42",0.5,0.5, ))
    thread1.start()
    thread2.start()
    thread3.start()
#print("New Per",check.rs.look_for_nodeper("192.168.1.149"))


