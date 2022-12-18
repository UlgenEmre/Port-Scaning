#!/usr/bin/env python
# *-* coding: utf-8 *-*

import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT SCANNING")
print("""
Port Scanning

1) Quick Scan
2) Service and Version Information
3) Operating System Information


""")

islemno = raw_input("Enter Transaction Number:  ")


if(islemno == "1"):
	hedefip = raw_input ("Enter Destination ip: ")
	os.system("nmap " + hedefip)

elif(islemno == "2"):
	hedefip = raw_input ("Enter Destination ip: ")
	os.system("nmap -sS -sV " + hedefip)



elif(islemno == "3"):
	hedefip = raw_input ("Enter Destination ip: ")
	os.system("nmap -O " + hedefip)
	

else:
	print("You Made an Wrong Choice, The Program Was Closed.")
	
