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

lop = input(Fore.RED + "Masukan Username : ")
lap = input(Fore.BLUE + "Masukan Password : ")

print ("Hi " + lop + ", Salam Kenal")
time.sleep(2)

a = "Tanggal = "
b = "Bulan = "
t = "Tahun = "

hari_ini = datetime.now()
tanggal = hari_ini.strftime(a+'%d ' + b+'%m ' + t+'%y')

saat_ini = datetime.now()
jam = saat_ini.strftime('%H:%M:%S')

print ('\n')

welcome = Fore.BLUE + pyfiglet.figlet_format("Welcome", font = "3-d") 
print(welcome)

xnk = Fore.GREEN + pyfiglet.figlet_format("Anonymous", font = 'standard')
print (xnk)

print (Fore.RED + "=============================")
print (colored('\t Xnuvers', 'red'))

asd = (colored('\t Xpl', 'red'))
dsa = (colored('oit','white'))

print (asd+dsa)

print (colored('\t Xentzh', 'white'))
print ("=============================")


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
print (colored(s, 'grey'))

d = str(input(Fore.GREEN + "[+] Masukan nama domain website misal com, org, id, dll. bukan seperti ini (.com) = "))
print(colored(d, 'green'))

bs = str(input(Fore.BLUE + "[+] Masukan terjemahan Bahasa (contoh: inggris = en, indonesia = id, dll.) : "))
print (colored(bs, 'BLUE'))

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
