#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import socket
import platform
import subprocess

#Function de verificar o sistema e dar ping
def verified_os(distro, plat):
    global op
    if distro == "windows":
            op = subprocess.run(["ping", "-c", "1", plat], stdout=subprocess.PIPE)
    elif distro == "linux":
            op = os.system("ping -c 1 -w 1 " + plat + ">/dev/null")
    else:
            op = os.system("ping -c 1 -w 1 " + plat + ">/dev/null")
            
def clearscreen(distro):
    if distro == "linux":
        os.system('clear')
    elif distro == "windows":
        os.system('cls')
    else:
        os.system('clear')

print("|------------------------------|")
print("|     Software developer 3T    |")
print("|    SIMPLE NETWORK Scanner    |")
print("|------------------------------|\n\n")


print("*****")
print("Hello " + socket.gethostname())
print("*****\n\n")

distro = platform.system().lower()
print("Your distro system is: " + distro + "\n\n")

print("digit 1 for scan single ip\n")
print("digit 2 for scan range ip\n")
print("digit 3 for host scan\n")

opt = int(input("digit your option: \n\n"))

#pega o ip e retorna se ele ta ativo ou desativado
if opt == 1:
    clearscreen(distro)
    ip = input("digit ip for scan: ")
    ipstr = ip.split(".")
    p = "."
    ipaddr = ipstr[0] + p + ipstr[1] + p + ipstr[2] + p + ipstr[3]
    
    verified_os(distro, ipaddr)
    
    if op == 0:
        print("\n" + ipaddr + " is up\n")
    else:
        print("\n" + ipaddr + " down\n")
            
#realiza a verificacao do range de ip total
elif opt == 2:
    clearscreen(distro)
    ip = input("digit ip for range scan: \n")
    ipstr = ip.split(".")
    p = "."
    ipaddr = ipstr[0] + p + ipstr[1] + p + ipstr[2] + p
    for net in range(1,255):
        machine = ipaddr + str(net)
        
        verified_os(distro, machine)     
        
        if op == 0: 
            print(machine + " is up")
            try:
                hostname = socket.gethostbyaddr(machine)
                print(hostname)
                print("\n------------\n")
            except:
                hostname = socket.gethostbyname_ex(machine)
                print(hostname)
                print("\n------------\n")
        else:
            print(machine + " down\n")
    
    print("Program END...")
    
#verifica se esta pingando pelo host (URL)
elif opt == 3:
    clearscreen(distro)
    print("Digit the URI, example.com\n")
    url = input("URI: ")
    
    try:
        host = socket.gethostbyname(url)
        verified_os(distro, host)
        
        if op == 0:
            print("\n url " + url + " - ip " + host + " up\n")
    except:
        print("\n" + url + " down\n")

else:
    print("command not found try again")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import socket
import platform
import subprocess

#Function de verificar o sistema e dar ping
def verified_os(distro, plat):
    global op
    if distro == "windows":
            op = subprocess.run(["ping", "-c", "1", plat], stdout=subprocess.PIPE)
    elif distro == "linux":
            op = os.system("ping -c 1 -w 1 " + plat + ">/dev/null")
    else:
            op = os.system("ping -c 1 -w 1 " + plat + ">/dev/null")
            
def clearscreen(distro):
    if distro == "linux":
        os.system('clear')
    elif distro == "windows":
        os.system('cls')
    else:
        os.system('clear')

print("|------------------------------|")
print("|     Software developer 3T    |")
print("|    SIMPLE NETWORK Scanner    |")
print("|------------------------------|\n\n")


print("*****")
print("Hello " + socket.gethostname())
print("*****\n\n")

distro = platform.system().lower()
print("Your distro system is: " + distro + "\n\n")

print("digit 1 for scan single ip\n")
print("digit 2 for scan range ip\n")
print("digit 3 for host scan\n")

opt = int(input("digit your option: \n\n"))

#pega o ip e retorna se ele ta ativo ou desativado
if opt == 1:
    clearscreen(distro)
    ip = input("digit ip for scan: ")
    ipstr = ip.split(".")
    p = "."
    ipaddr = ipstr[0] + p + ipstr[1] + p + ipstr[2] + p + ipstr[3]
    
    verified_os(distro, ipaddr)
    
    if op == 0:
        print("\n" + ipaddr + " is up\n")
    else:
        print("\n" + ipaddr + " down\n")
            
#realiza a verificacao do range de ip total
elif opt == 2:
    clearscreen(distro)
    ip = input("digit ip for range scan: \n")
    ipstr = ip.split(".")
    p = "."
    ipaddr = ipstr[0] + p + ipstr[1] + p + ipstr[2] + p
    for net in range(1,255):
        machine = ipaddr + str(net)
        
        verified_os(distro, machine)     
        
        if op == 0: 
            print(machine + " is up")
            try:
                hostname = socket.gethostbyaddr(machine)
                print(hostname)
                print("\n------------\n")
            except:
                hostname = socket.gethostbyname_ex(machine)
                print(hostname)
                print("\n------------\n")
        else:
            print(machine + " down\n")
    
    print("Program END...")
    
#verifica se esta pingando pelo host (URL)
elif opt == 3:
    clearscreen(distro)
    print("Digit the URI, example.com\n")
    url = input("URI: ")
    
    try:
        host = socket.gethostbyname(url)
        verified_os(distro, host)
        
        if op == 0:
            print("\n url " + url + " - ip " + host + " up\n")
    except:
        print("\n" + url + " down\n")

else:
    print("command not found try again")
