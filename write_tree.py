import xml.etree.ElementTree as ET
#import xml.dom.minidom
tree = ET.parse('resources.xml')
#doc = xml.dom.minidom.parse("aaa.xml");
root = tree.getroot()
#print(root[0][0].text)
print(root[0][1].text)
root[0][1].text="102"
print(root[0][1].text)

#for child in root:
    #print(child.tag, child.attrib)

#print(root)
#for child in root:
    #print(child.tag, child.attrib)
#print(child.tag)
#print(root.find('name'))
def look_for_noderep(nodename):
    for node in root.findall('node'):
        name= node.get('name')
        if name==nodename:              
            rep = float(node.find('reputation').text) 
            print(rep)
    return(rep)
#look_for_noderep("node1")

def update_noderep(nodename,rep):
    i=0
    for node in root.findall('node'):
        name= node.get('name')
        print(name)
        if name==nodename: 
            root[i][1].text=rep
            print(root[i][1].text)
            break
        i=i+1
        print(i)
    #tree.write('resources.xml')        
    return("Reputation updated")

def update_nodeper(nodename,per):
    i=0
    for node in root.findall('node'):
        name= node.get('name')
        print(name)
        if name==nodename: 
            root[i][1].text=per
            print(root[i][2].text)
            break
        i=i+1
        print(i)
    #tree.write('resources.xml')        
    return("Performance Updated")

def update_nodeavai(nodename,avai):
    i=0
    for node in root.findall('node'):
        name= node.get('name')
        print(name)
        if name==nodename: 
            root[i][1].text=avai
            print(root[i][3].text)
            break
        i=i+1
        print(i)
    #tree.write('resources.xml')        
    return("Performance Updated")
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

tree.write('resources2.xml')
