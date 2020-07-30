import dns
from datetime import datetime
from datetime import date
import pyfiglet
import time
import socket
import dns.resolver
from googletrans import Translator

print('''
==============================================================================
__  __                              __  __      _       _ _  __  __          
\ \/ /_ __  _   ___   _____ _ __ ___\ \/ /_ __ | | ___ (_) |_\ \/ /___ _ __  
 \  /| '_ \| | | \ \ / / _ \ '__/ __|\  /| '_ \| |/ _ \| | __|\  // _ \ '_ \ 
 /  \| | | | |_| |\ V /  __/ |  \__ \/  \| |_) | | (_) | | |_ /  \  __/ | | |
/_/\_\_| |_|\__,_| \_/ \___|_|  |___/_/\_\ .__/|_|\___/|_|\__/_/\_\___|_| |_|
                                         |_|                                 
==============================================================================
''')

d = 'Hari (Day) = '
e = 'Bulan ke (Months) = '
f = 'Tahun (Year) = '

hari_ini = datetime.now()
tanggal = hari_ini.strftime(d+'%d, ' + e+'%m, ' + f+'%y')
print (tanggal)

J = 'Jam (hours) = '
M = 'Menit (Minutes) = '
D = 'Detik (Seconds) = '

saat_ini = datetime.now()
jam = saat_ini.strftime(J+'%H : ' + M+'%M : ' + D+'%S')
print(jam)


print ('\n')
print ("|-------------------------------------|")
print ("| Author   : XNUVERS007               |")
print ("| You Tube : https://bit.ly/Xnuvers   |")
print ("| github   : https://bit.ly/Xnuvrs1   |")
print ("| Facebook : https://bit.ly/Fesbuck   |")
print ("| Instagram: https://bit.ly/Xnvrs13   |")
print ("| Site     : http://bit.ly/Mykingbee  |")
print ("|-------------------------------------|")
print ('\n')

translator = Translator()

resolver = dns.resolver.Resolver()
resolver.nameservers = ['216.239.38.120']

x = translator.translate('Masukan nama website (google.com , mykingbee.blogspot.com, tiktok.com) = ', src='id', dest = 'en')
print(x.text)

print('\n')

a = input("Masukan nama website (google.com , mykingbee.blogspot.com, tiktok.com) = ")
print (a)

result = dns.resolver.resolve(a, 'A')

for ipval in result:
   print('Ip Multi = ', ipval.to_text())

print('\n')

addr = socket.gethostbyname(a)

print ('Ip Address (Single) dari {} adalah {}'.format(a,addr))
y = translator.translate('Ip Address (Single) dari {} adalah {}'.format(a,addr), src='id', dest = 'en')
print(y.text)

print('\n')

b = input("Tekan Enter...!!!")
time.sleep(3)

exit()
