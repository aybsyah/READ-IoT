
#####################  Main #################################
import time
import deployer,requestor
import check
import subprocess
import threading
from multiprocessing import Process


##############Nodes
#Fog
FN1='192.168.1.149'  #VM1
FN2='192.168.1.133'  #VM2
FN3='192.168.1.186'  #VM3


#Cloud
CN1="34.246.233.37"     #large
CN2="99.81.118.97" #xlarge
CN3="108.128.181.234"   #2xlarge

Resources=[FN1,FN2,FN3,CN1,CN2,CN3]

Nodes=[FN2,CN2,CN3]
###########Services
#Anomalt_Detection
C1='c1_ed_v3' #'C1_AD'
C2='c2_ed_v4' #'C2_AD'
C3='c3_ed_v3' #'C3_AD'


#Anomaly Detector
C4='C1_ED'
C5='C2_ED'
C6='C3_ED'

Components_AD=[C1,C2,C3]
Components_ED=[C4,C5,C6]

#Services
S1='firedetect'
S2='firedetect'
S3='firedetect'
Services=[S1,S2,S3]




#Placement Plan
placement_plan=[0,0,0]
#Available Resources
avai_resources=[]

def begin_monitoring():
    thread1 = threading.Thread(target=check.response_time, args=("FN1",FN1,0.5,0.5, ))
    thread2 = threading.Thread(target=check.response_time, args=("FN2",FN2,0.5,0.5, ))
    thread3 = threading.Thread(target=check.response_time, args=("FN3",FN3,0.5,0.5, ))
    thread4 = threading.Thread(target=check.response_time, args=("CN1",CN1,0.5,0.5, ))
    thread5 = threading.Thread(target=check.response_time, args=("CN2",CN2,0.5,0.5, ))
    thread6 = threading.Thread(target=check.response_time, args=("CN3",CN3,0.5,0.5, ))
    thread7 = threading.Thread(target=check.reputation,args=(0.8,))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
#print("New Per",check.rs.look_for_nodeper("192.168.1.149"))


#def check_avai_res():
    #check_resources.response_time

    
def begin_placement_clac():
    while True:
        time.sleep(10)
        avn =[0,0,0,0,0,0]
        link=[0,0,0,0,0,0]
        cap =[0,0,0,0,0,0]
        rep =[0,0,0,0,0,0]
        busy=[0,0,0,0,0,0]

        check.rs.update_nodebusy("FN1",0)
        check.rs.update_nodebusy("FN2",0)
        check.rs.update_nodebusy("FN3",0)
        check.rs.update_nodebusy("CN1",0)
        check.rs.update_nodebusy("CN2",0)
        check.rs.update_nodebusy("CN3",0)

        #avai_resources.clear()
        #print("after clear",avai_resources)

        avn[0]=check.rs.look_for_nodeavai("FN1")
        avn[1]=check.rs.look_for_nodeavai("FN2")
        avn[2]=check.rs.look_for_nodeavai("FN3")
        avn[3]=check.rs.look_for_nodeavai("CN1")
        avn[4]=check.rs.look_for_nodeavai("CN2")
        avn[5]=check.rs.look_for_nodeavai("CN3")
        
        
        link[0] =check.rs.look_for_nodelink("FN1")
        link[1] =check.rs.look_for_nodelink("FN2")
        link[2] =check.rs.look_for_nodelink("FN3")
        link[3] =check.rs.look_for_nodelink("CN1")
        link[4] =check.rs.look_for_nodelink("CN2")
        link[5] =check.rs.look_for_nodelink("CN3")
        
        cap[0]= check.rs.look_for_nodecapacity("FN1")
        cap[1]= check.rs.look_for_nodecapacity("FN2")
        cap[2]= check.rs.look_for_nodecapacity("FN3")
        cap[3]= check.rs.look_for_nodecapacity("CN1")
        cap[4]= check.rs.look_for_nodecapacity("CN2")
        cap[5]= check.rs.look_for_nodecapacity("CN3")
        
        rep[0]= check.rs.look_for_noderep("FN1")
        rep[1]= check.rs.look_for_noderep("FN2")
        rep[2]= check.rs.look_for_noderep("FN3")
        rep[3]= check.rs.look_for_noderep("CN1")
        rep[4]= check.rs.look_for_noderep("CN2")
        rep[5]= check.rs.look_for_noderep("CN3")
        
        busy[0]= check.rs.look_for_nodebusy("FN1")
        busy[1]= check.rs.look_for_nodebusy("FN2")
        busy[2]= check.rs.look_for_nodebusy("FN3")
        busy[3]= check.rs.look_for_nodebusy("CN1")
        busy[4]= check.rs.look_for_nodebusy("CN2")
        busy[5]= check.rs.look_for_nodebusy("CN3")  
        
        
        
        
        #print("------------")
        #print("Avai N1",avn[0], "Link N1:",link[0], "Capacity N1:",cap[0],"Reputation N1:",rep[0],"Busy N1:",busy[0])      
        #print("Avai N2",avn[1], "Link N2:",link[1], "Capacity N2:",cap[1],"Reputation N2:",rep[1],"Busy N2:",busy[1])        
        #print("Avai N3",avn[2], "Link N3:",link[2], "Capacity N3:",cap[2],"Reputation N3:",rep[2],"Busy N3:",busy[2])        
        #print("Avai N4",avn[3], "Link N4:",link[3], "Capacity N4:",cap[3],"Reputation N4:",rep[3],"Busy N4:",busy[3])        
        #print("Avai N5",avn[4], "Link N5:",link[4], "Capacity N5:",cap[4],"Reputation N5:",rep[4],"Busy N5:",busy[4])        
        #print("Avai N6",avn[5], "Link N6:",link[5], "Capacity N6:",cap[5],"Reputation N6:",rep[5],"Busy N6:",busy[5])        
        #print("------------")
        
        #print ("Placement pian: None")
        
        
        for i in range(6):            
            if avn[i]==1 and i+1 not in avai_resources:
                avai_resources.append(i+1)                
            elif avn[i] ==0 and i+1 in avai_resources:
                avai_resources.remove(i+1)
        
        #Availibility
        Available_res=[]
        for i in range (len(avai_resources)):
            if avai_resources[i]<=3:
                Available_res.append("FN"+str(i+1))
            else:
                res=int(int(avai_resources[i])-3)
                Available_res.append("CN"+str(res))
        #print("after check avai",avai_resources)
        if len(avai_resources)==0:
            a=0
            #print("No resources Available")
        else:
            avai_resources.sort()
            #print("Availai resources:", avai_resources)
            #choose the target placement for C1
            
            #avai_resources=avai_resources.sort()
            if avn[0]==1 and check.rs.look_for_nodebusy("FN1")==0 and rep[0]>0.8:
                placement_plan[0]=1
                check.rs.update_nodebusy("FN1",1)
                #print("111",check.rs.look_for_nodebusy("N1"))   
            elif avn[1]== 1 and check.rs.look_for_nodebusy("FN2")==0 and rep[1]>0.8:
                placement_plan[0]=2                
                check.rs.update_nodebusy("FN2",1)
                #print("222",check.rs.look_for_nodebusy("N2")) 
            elif avn[2]== 1 and check.rs.look_for_nodebusy("FN3")==0 and rep[2]>0.8:
                placement_plan[0]=3
                check.rs.update_nodebusy("FN3",1)
            elif avn[3]== 1 and check.rs.look_for_nodebusy("CN3")==0 and rep[3]>0.8:
                placement_plan[0]=3
                check.rs.update_nodebusy("CN3",1)
            elif avn[4]== 1 and check.rs.look_for_nodebusy("CN2")==0 and rep[4]>0.8:
                placement_plan[0]=4
                check.rs.update_nodebusy("CN2",1)
            elif avn[5]== 1 and check.rs.look_for_nodebusy("CN1")==0 and rep[4]>0.8:
                placement_plan[0]=5
                check.rs.update_nodebusy("CN1",1)
            elif placement_plan[0] ==0:             
                placement_plan[0]=avai_resources[0]
            else:
                placement_plan[0]=avai_resources[0]
            
            #choose the target placement for C2
            if avn[5]==1 and check.rs.look_for_nodebusy("CN3")==0 and link[5]>=1 and rep[5]>0.8:
                placement_plan[1]=6
                check.rs.update_nodebusy("CN3",1)
            elif avn[4]== 1 and check.rs.look_for_nodebusy("CN2")==0 and link[4]>=1 and rep[4]>0.8:
                placement_plan[1]=5
                check.rs.update_nodebusy("CN2",1)
            elif avn[3]== 1 and check.rs.look_for_nodebusy("CN1")==0 and link[3]>=1 and rep[3]>0.8:
                placement_plan[1]=4
                check.rs.update_nodebusy("CN1",1)
            elif avn[0]== 1 and check.rs.look_for_nodebusy("FN1")==0 and rep[0]>0.8:
                placement_plan[1]=1
                check.rs.update_nodebusy("FN1",1)
            elif avn[1]== 1 and check.rs.look_for_nodebusy("FN2")==0 and rep[1]>0.8:
                placement_plan[1]=2
                check.rs.update_nodebusy("FN2",1)
            elif avn[2]== 1 and check.rs.look_for_nodebusy("FN3")==0 and rep[2]>0.8:
                placement_plan[1]=3
                check.rs.update_nodebusy("FN3",1)
            elif placement_plan[1] ==0:             
                placement_plan[1]=avai_resources[0]
            else:
                placement_plan[1]=avai_resources[0]
            #choose the target placement for C3
            if avn[0]==1 and check.rs.look_for_nodebusy("FN1")==0 and rep[0]>0.8:
                placement_plan[2]=1
                check.rs.update_nodebusy("FN1",1)
                #print("333",check.rs.look_for_nodebusy("N1")) 
            elif avn[1]== 1 and check.rs.look_for_nodebusy("FN2")==0 and rep[1]>0.8:
                placement_plan[2]=2
                check.rs.update_nodebusy("FN2",1)
                #print("444",check.rs.look_for_nodebusy("N2")) 
            #elif avn[2]== 1 and check.rs.look_for_nodebusy("FN3")==0 and rep[2]>0.8:
                #placement_plan[2]=3
                #check.rs.update_nodebusy("FN3",1)
            elif avn[3]== 1 and check.rs.look_for_nodebusy("CN3")==0 and rep[3]>0.8:
                placement_plan[2]=4
                check.rs.update_nodebusy("CN3",1)
            elif avn[4]== 1 and check.rs.look_for_nodebusy("CN2")==0 and rep[4]>0.8:
                placement_plan[2]=5
                check.rs.update_nodebusy("CN2",1)
            elif avn[5]== 1 and check.rs.look_for_nodebusy("CN1")==0 and rep[5]>0.8:
                placement_plan[2]=6
                check.rs.update_nodebusy("CN1",1)
            elif placement_plan[2] ==0:             
                placement_plan[2]=avai_resources[0]
            else:
                placement_plan[2]=avai_resources[0]

        #placement_plan[0]=Available_res[0]
        #placement_plan[1]=Available_res[1]
        #placement_plan[2]=Available_res[2]
        #print(Available_res)

        placement=[]
        for i in range (len(placement_plan)):
            if placement_plan[i]<=3:
                placement.append("FN"+str(i+1))
            else:
                res=int(int(placement_plan[i])-3)
                placement.append("CN"+str(res))
                
        print("Available Resources:",Available_res)
        #print("\n")
        print("Placement Plan:", "C1 on", placement[0],", C2 on", placement[1], ", C3 on", placement[2])
        print("\n")
        #for i in range(6):
            #if rep[i] <=0.3:
                #print("Reputation of Node",i, "is",rep[i])
        #print("Placement Plan:", "C1:", placement_plan[0],"C2:", placement_plan[1], "C3:", placement_plan[2])
        
def deploy_component():        
        while True:
            time.sleep(5)
            
            print("+++++++ Start +++++++++++++++++")
            j=0
            #print("Available Resources:",avai_resources)
            #print("Placement Plan:", "C1:", placement_plan[0],"C2:", placement_plan[1], "C3:", placement_plan[2])
            #print(R[placement_plan[0]-1])
            
            
            
            #Step1
            #Check the available resources from controller    
            #List of Nodes

            ######Fog
            #N2='192.168.1.149'
            #N1='54.77.247.42'
            
            

            #large
            #N1='34.241.78.252'    

            #xlarge
            #N1='63.34.50.93''    '

            #2xlarge
            #N1='99.81.111.8'
            #####if len  (avai_resources)!=0:
            ###Nodes=[CN2,CN3,CN1]
            ####for i in range (3):
                ####Nodes.append(Resources[placement_plan[i]-1])
            #Nodes.append(N2)
            

            Components=[C1,C2,C3]
            ####Components=[]
            ####for i in range(3):
                 ####Components.append(Components_AD[i])

            S1='firedetect'
            S2='svm_train_predict'
            S3='dm'
            #Components.append(c2)
            #c2="c1_event_detectionv1"
            #List of services
            #S1='svm_train_predict'                
            #S2='svm_train_predict'
            #S2='DL_train_pred'
                            #Services.append(S2)
           
           
            #Step2
            #Calculate best placement plan
            start_time = time.time()
            #Step3
            t=23
            h=50
           
            #for i in range(len(placement_plan)):
                #placement_plannow.append(placement_plannow[i])
            """for i in range(len(Nodes)):
                
                #N="N"+str(Resources.index(Nodes[i])+1)
                #print(N)
                #print(check.rs.look_for_nodeavai(N))
                if check.rs.look_for_nodeavai(N)==1:
                    try:
                        deployer.deploy(Components[i],Nodes[i],i+j)
                        # break
                    except:
                        print("Problem of  Deplyment")
                        break
                else:
                    break
            
                if str(Nodes[i])[:3]=="192":
                    time.sleep(16)
                else:
                    time.sleep(10)
                if check.rs.look_for_nodeavai(N)==1:
                    try:
                        requestor.send_data3(Nodes[i],Services[i],i+j,"/home/aymen/a.txt",t,h)
                    except:
                        print("Problem of request")
                        break
                else:
                    break
            if i==2:
                print("All componenents are deployed on machines")
                
            #else:
                #j=j+1
            ####else:
            ####time.sleep(5)
            """

            #Call the deployer to deploy Component on nodes
            deployer.deploy(Components[0],Nodes[0],1)
            deployer.deploy(Components[1],Nodes[1],2)
            deployer.deploy(Components[2],Nodes[2],4)
            
            ########print("--- %s Deployment time in seconds ---" % (time.time() - start_time))
            #time.sleep(10)
            #print("New Per",check.rs.look_for_nodeper("192.168.1.149"))

            #Step4
            #requestor.DB_connection()

                
            #C1_ED
            requestor.send_data3(Nodes[0],S1,1,"/home/aymen/a.txt",t,h)
            
            #for i in range(3):
                #requestor.send_data3(Nodes[1],Services[i],i,"/home/aymen/a.txt",t,h)
                #time.sleep(10)
            #time.sleep(17)
            
        
       
            #C2_ED
            requestor.send_data(Nodes[1],S2,2)
            #requestor.send_data(Nodes[1],Services[1],1)


            #C3_ED
            requestor.send_data4(Nodes[2],S3,4)


            print("--- %s Execution time in seconds ---" % (time.time() - start_time))
            #C2_AD
            #requestor.send_data2(Nodes[1],Services[1],1,"/home/aymen/kdd06.csv")
            #print("New Per",check.rs.look_for_nodeper("192.168.1.149"))
            #print("--- %s Execution time in seconds ---" % (time.time() - start_time))
        
def main():
    
    #####begin_monitoring()    
    #p1 = Process(target=begin_placement_clac)
    #####thread7 = threading.Thread(target=begin_placement_clac)
    #####thread7.start()
    
        

    deploy_component()
    
    
    

    
if __name__ == "__main__": main()
