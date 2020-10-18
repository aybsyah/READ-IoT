import xml.etree.ElementTree as ET
#import xml.dom.minidom
tree = ET.parse('resources.xml')
#doc = xml.dom.minidom.parse("aaa.xml");
root = tree.getroot()


#print(root[0][0].text)
#print(root[0][1].text)
#root[0][1].text="102"
#print(root[0][1].text)

#for child in root:
    #print(child.tag, child.attrib)

#print(root)
#for child in root:
    #print(child.tag, child.attrib)
#print(child.tag)
#print(root.find('name'))
def look_for_nodeavai(nodename):
    for node in root.findall('node'):
        name= node.get('name')
        if name==nodename:              
            avai = float(node.find('availability').text) 
            #print(avai)
    return(avai)

def look_for_nodebusy(nodename):
    for node in root.findall('node'):
        name= node.get('name')
        if name==nodename:              
            busy = float(node.find('busy').text) 
            #print(avai)
    return(busy)



def look_for_nodelink(nodename):
    for node in root.findall('node'):
        name= node.get('name')
        if name==nodename:              
            link = float(node.find('link').text) 
            #print(per)
    return(link)
def look_for_nodecapacity(nodename):
    for node in root.findall('node'):
        name= node.get('name')
        if name==nodename:              
            capacity = float(node.find('capacity').text) 
            #print(per)
    return(capacity)
def look_for_noderep(nodename):
    for node in root.findall('node'):
        name= node.get('name')
        if name==nodename:              
            rep = float(node.find('reputation').text) 
            #print(per)
    return(rep)

def update_noderep(nodename,rep):
    i=0
    for node in root.findall('node'):
        name= node.get('name')
        #print(name)
        if name==nodename: 
            root[i][2].text=rep
            #print(root[i][1].text)
            break
        i=i+1
        #print(i)
    #tree.write('resources.xml')        
    return("Reputation updated")

def update_nodelink(nodename,link):
    i=0
    for node in root.findall('node'):
        name= node.get('name')
        #print(name)
        if name==nodename: 
            root[i][3].text=link
            #print(root[i][3].text)
            break
        i=i+1
        #print(i)
    #tree.write('resources.xml')        
    return("Link Updated")

def update_nodeavai(nodename,avai):
    i=0
    for node in root.findall('node'):
        name= node.get('name')
        #print(name)
        if name==nodename: 
            root[i][4].text=avai
            #print(root[i][4].text)
            break
        i=i+1
        #print(i)
    #tree.write('resources.xml')        
    return("Availibility Updated")


def update_nodebusy(nodename,busy):
    i=0
    for node in root.findall('node'):
        name= node.get('name')
        #print(name)
        if name==nodename: 
            root[i][6].text=busy
            #print(root[i][3].text)
            break
        i=i+1
        #print(i)
    #tree.write('resources.xml')        
    return("Busy Updated")

##look_for_noderep("node1")
#update_noderep("node3","100")

#for node in root.findall('node'):
    #name= node.get('name')
    #if name=="node3":              
        #rep = int(node.find('reputation').text)
        #per = int(node.find('performance').text)
        #print(per,rep)
    #if rep > 50:
        #root.remove(country)

#newnode=doc.createElement("node")
#newnode.setAttribute("name","node3")
#print(root[0][1].text)
#print(root[0][1].text)

#tree.write('resources.xml')
