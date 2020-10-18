import docker
#deploy Components on nodes

def deploy(c1,N1,port):   
    base_url1="tcp://"+str(N1)+":2375"
    #base_url2="tcp://"+str(N2)+":2375"
   

    #clients
    client1 = docker.DockerClient(base_url1)
    #client2 = docker.DockerClient(base_url2)
    #client = docker.from_env()
    #client3=docker.DockerClient("tcp://34.241.203.229:2375")
    #client3.login(username="ayahyaou", password="YA368--1881ny1981",registry="https://hub.docker.com/r/ayahyaou/dock-reg")
    
    #image = client1.images.pull('ayahyaou/get-started:part2')
    #image7 = client1.images.pull('ayahyaou/components:c1_event_detectionv1')
    #image8 = client1.get_image("ayahyaou/components:c1_event_detectionv1")
    #image8.tag('ayahyaou/components:c1_event_detectionv1',c1)
    
    #Delete the containers if they exist already
    
    clean_container(client1,c1)
    #clean_container(client2,c2)

    #run the container C1 on Node N1
    n1="ayahyaou/components:" + c1
    #n2="ayahyaou/components:" + c2
    print("Running", c1, "on", N1)
    port=5000+port
    print(port)
    the_port="ports={5000:"+str(port)+"}"
    print(the_port)
    client1.containers.run(n1,detach=True,name=c1, ports={5000:port})
    
    #run the container C2 on Node N2
    #print("Running", c2, "on", N2)
    #client2.containers.run(n2, detach=True,name=c2,ports={5000:5001})
    print("done")

#####################  Main #################################
def clean_container(client,c):
    while True:
            try:
                container = client.containers.get(c)
                container.stop()
                container.remove()
                                
                break
            except:
                print("No such container")
                break

def main():
	c1="c1_event_detectiov0_flask"
	#N1='192.168.233.131'
	#deploy(c1,N1)
    
if __name__ == "__main__": main()
