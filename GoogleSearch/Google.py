from googlesearch import search

import time

from termcolor import colored

import datetime

import pyfiglet

from datetime import datetime

from datetime import date

from colorama import Fore

import colorama

import sphinx

colorama.init()

lop = input("Masukan Username : ")
lap = input("Masukan Password : ")

print ("Hi " + lop + ", Salam Kenal")
time.sleep(2)

a = "Tanggal = "
b = "Bulan = "
t = "Tahun = "

hari_ini = datetime.now()
tanggal = hari_ini.strftime(a+'%d ' + b+'%m ' + t+'%y')

saat_ini = datetime.now()
jam = saat_ini.strftime('%H:%M:%S')

print(colored('''
  __  __                              __  __      _       _ _  __  __          
  \ \/ /_ __  _   ___   _____ _ __ ___\ \/ /_ __ | | ___ (_) |_\ \/ /___ _ __  
   \  /| '_ \| | | \ \ / / _ \ '__/ __|\  /| '_ \| |/ _ \| | __|\  // _ \ '_ \ 
   /  \| | | | |_| |\ V /  __/ |  \__ \/  \| |_) | | (_) | | |_ /  \  __/ | | |
  /_/\_\_| |_|\__,_| \_/ \___|_|  |___/_/\_\ .__/|_|\___/|_|\__/_/\_\___|_| |_|
                                           |_|
      ''','red'))
print(colored('''
    :::       :::        ::::::::::        :::         :::::::: 
   :+:       :+:        :+:               :+:        :+:    :+: 
  +:+       +:+        +:+               +:+        +:+         
 +#+  +:+  +#+        +#++:++#          +#+        +#+          
+#+ +#+#+ +#+        +#+               +#+        +#+           
#+#+# #+#+#         #+#               #+#        #+#    #+#     
###   ###          ##########        ##########  ########       
      ::::::::          :::   :::        :::::::::: 
    :+:    :+:        :+:+: :+:+:       :+:         
   +:+    +:+       +:+ +:+:+ +:+      +:+          
  +#+    +:+       +#+  +:+  +#+      +#++:++#      
 +#+    +#+       +#+       +#+      +#+            
#+#    #+#       #+#       #+#      #+#             
########        ###       ###      ##########       ''','blue'))

print('\n')

print (tanggal)
print('Jam:', jam)

print('\n')

print (Fore.RED + "\t    Sosial Media")
print (Fore.RED + "|-------------------------------------|")
print (Fore.RED + "| Author   : XNUVERS007               |")
print (Fore.RED + "| You Tube : https://bit.ly/Xnuvers   |")
print (Fore.RED + "| github   : https://bit.ly/Xnuvrs1   |")
print (Fore.WHITE + "| Facebook : https://bit.ly/Fesbuck   |")
print (Fore.WHITE + "| Instagram: https://bit.ly/Xnvrs13   |")
print (Fore.WHITE + "| Site     : http://bit.ly/Mykingbee  |")
print (Fore.WHITE + "|-------------------------------------|")

print ('\n')

print ("[+] tunggu sebentar... [-]")

time.sleep(5)

l = str(input(Fore.RED + "[+] Masukan Yang ingin kalian Cari : "))
print (colored(l, 'white'))

k = str(input(Fore.RED + "[+] Anda ingin menyalakan pencarian aman/tidak ? (On / Off) = "))
print (colored(k, 'white'))

s = int(input(Fore.YELLOW + "[+] Masukan berapa banyak hasil pencarian : "))
print (colored(s, 'orange'))

d = str(input(Fore.GREEN + "[+] Masukan nama domain website misal com, org, id, dll. bukan seperti ini (.com) = "))
print(colored(d, 'green'))

bs = str(input(Fore.AQUA + "[+] Masukan terjemahan Bahasa (contoh: inggris = en, indonesia = id, dll.) : "))
print (colored(bs, 'aqua'))

print ('\n')

print ("\t\t   Tunggu Sebentar...")
time.sleep(3)

print ("======================================================")
for i in search(a, safe=k, lang=b, tld=d, num=s, stop=10, pause=2.0, verify_ssl=True):
   print (i)

print ("======================================================")

print ('\n')

input("Tekan enter untuk Keluar...")

time.sleep(2)
exit()


#COPYRIGHT 2020 @ XnuversXploitXen
