#this module send data to nodes running componenet as web service for processing
import mysql.connector
import requests,time
def DB_connection():# connect to DB(event table) to retreive last inserted data to DB
    mydb = mysql.connector.connect(host='127.0.0.1',user='aymen',passwd='aymen',db='mydb')
    mycursor = mydb.cursor()
    mycursor.execute("select * from events order by EVENT_DATE,EVENT_TIME desc limit 2000;")
    myresult = mycursor.fetchall()
    #for x in myresult:
        #print(x)
    file20 = "a.txt"
    file20= open(file20, 'w')
    for row in myresult:
        time=str(row).split(",")[7].split("'")[1]
        hum =str(row).split(",")[8].split("'")[1]
        file20.write(time)
        file20.write(",")
        file20.write(hum)
        file20.write("\n")
    file20.close()
    mydb.close()
    
def send_data(N1,S1,port):
    port=port+5000
    
    url1='http://'+str(N1)+':'+str(port)+'/'+str(S1)   
    files = {'training_set': open('/home/aymen/a.txt', 'rb'), 'outliers': open('/home/aymen/a.txt', 'rb')}
    #r=requests.post('http://192.168.233.131:5000/svm_train_predict', files=files)
    #equivalent to: curl -XPOST http://192.168.233.131:5000/svm_train_predict -F 'training_set=@/home/aymen/a.txt' -F 'outliers=@/home/aymen/a.txt'
    print("Sending Request to %s" %N1)
    r1=requests.post(url1, files=files)
    print(r1)
    
    
def send_data2(N2,S2,port,file):
    port=port+5000
    url2='http://'+str(N2)+':'+str(port)+'/'+str(S2)
    print(url2)
    files = {'training_set': open(file, 'rb')}
    print(files)
    #r=requests.post('http://192.168.233.131:5000/svm_train_predict', files=files)
    #equivalent to: curl -XPOST http://192.168.233.131:5000/svm_train_predict -F 'training_set=@/home/aymen/a.txt' -F 'outliers=@/home/aymen/a.txt'
    print("Sending Request to %s" %N2)
    #r1=requests.post(url1, files=files)
    #print(r1)
    #time.sleep(20)
    r2=requests.post(url2, files=files)    
    print(r2)
    #time.sleep(20)
    #print("Sending Request to %s" %N2)
    #r3=requests.post(url2, files=files)

def send_data3(N2,S2,port,file,t,h):
    port=port+5000    
    url2='http://'+str(N2)+':'+str(port)+'/'+str(S2)+ '?t='+str(t)+'&'+'h='+str(h)
    print(url2)
    files = {'data': open(file, 'rb')}
    print(files)
    #r=requests.post('http://192.168.233.131:5000/svm_train_predict', files=files)
    #equivalent to: curl -XPOST http://192.168.233.131:5000/svm_train_predict -F 'training_set=@/home/aymen/a.txt' -F 'outliers=@/home/aymen/a.txt'
    print("Sending Request to %s" %N2)
    #r1=requests.post(url1, files=files)
    #print(r1)
    #time.sleep(20)
    #r1=requests.post()
    r2=requests.post(url2, files=files)    
    print(r2)
    #time.sleep(20)
    #print("Sending Request to %s" %N2)
    #r3=requests.post(url2, files=files)

def send_data4(N1,S1,port):
    port=port+5000
    
    url1='http://'+str(N1)+':'+str(port)+'/'+str(S1)   
    #files = {'training_set': open('/home/aymen/a.txt', 'rb'), 'outliers': open('/home/aymen/a.txt', 'rb')}
    #r=requests.post('http://192.168.233.131:5000/svm_train_predict', files=files)
    #equivalent to: curl -XPOST http://192.168.233.131:5000/svm_train_predict -F 'training_set=@/home/aymen/a.txt' -F 'outliers=@/home/aymen/a.txt'
    print("Sending Request to %s" %N1)
    r1=requests.post(url1)
    print(r1)

#def main(N1,S1,N2,S2):
    #DB_connection()
    #send_data(N1,S1,N2,S2)
    #send_data2(N1,S1,N2,S2)
  
if __name__ == "__main__": main()






