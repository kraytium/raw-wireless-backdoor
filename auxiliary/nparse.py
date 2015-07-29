#!C:\python27\python27\python.exe
from xml.etree import ElementTree
from time import time

def host_search(doc_root, max_hosts=float('inf')):
    # loop through hosts
    n = 0
    hosts = []
    
    for host in doc_root.iter('host'):
        live = False
        if n > max_hosts:
            break

        # check if host has at least one port open (and that it is not tcpwrapped)
        for attribute in host.find('ports').iter('port'):
            if (attribute.find('state').attrib['state'] == 'open') and (attribute.find('service').attrib['name'] != 'tcpwrapped'):
                live = True
                hosts.append({})
                hosts[-1]['ip'] = ''
                hosts[-1]['ports'] = []
                hosts[-1]['os'] = {}
                break

                
        if live == True:
            # loop through attributes
            for attribute in host.iter():
                if attribute.tag == 'address':
                    hosts[-1]['ip'] = attribute.attrib['addr']
                
                # get ports
                if attribute.tag == 'ports':
                    for port in attribute.iter('port'):
                        if (port.find('state').attrib['state'] == 'open') and (port.find('service').attrib['name'] != 'tcpwrapped'):
                            if 'product' in port.find('service').attrib:
                                hosts[-1]['ports'].append((port.attrib['portid'], port.find('service').attrib['product']))
                        
                            else:
                                hosts[-1]['ports'].append((port.attrib['portid'], port.find('service').attrib['name']))
                        
                # get os
                if attribute.tag == 'os':
                    if attribute.find('osmatch') is not None:
                        hosts[-1]['os']['name'] = attribute.find('osmatch').attrib['name']
                        
                        for each in ['type', 'vendor', 'osfamily', 'osgen']:
                            if each in attribute.find('osmatch').find('osclass').attrib:
                                hosts[-1]['os'][each] = attribute.find('osmatch').find('osclass').attrib[each]
                        
                    else:
                        hosts[-1]['os'] = 'OS match not found'
            
        n += 1
        
    return hosts
