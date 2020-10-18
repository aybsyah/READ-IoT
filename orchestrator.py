#####################  Main #################################
import time
import deployer,requestor

def main():
    start_time = time.time()
    c1="c1_event_detectiov0_flask"
    N1='192.168.233.131'
    deployer.deploy(c1,N1)
    print("--- %s seconds ---" % (time.time() - start_time))
    time.sleep(3)
    requestor.main(N1)
    print("--- %s seconds ---" % (time.time() - start_time))
    
  
if __name__ == "__main__": main()
