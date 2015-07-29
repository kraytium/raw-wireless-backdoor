#!C:\python27\python27\python.exe
from imp import load_source
from sys import argv
from time import time
from xml.etree import ElementTree

def loadscan(scnDoc):
    # load nmap xml output file
    with open(scnDoc, 'rt') as f:
        scan = ElementTree.parse(f).getroot()
    
    parser = load_source('nparse', '..\\auxiliary\\nparse.py')
    hosts = parser.host_search(scan)

    return hosts
    
fromXml = True
scanDocument = argv[1]

def main():

    if fromXml:
        print loadscan(scanDocument)
        
if __name__ == '__main__':
    main()
