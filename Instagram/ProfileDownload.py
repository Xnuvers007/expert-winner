import pyfiglet
from datetime import datetime
from datetime import date
from googletrans import Translator
from tkinter import *
import instaloader
import time

translator = Translator()

result = pyfiglet.figlet_format("XnuversXploitXen") 
print(result)
print ('\n')

print ("===========================================")
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

print ("===========================================")

print ('\n')

print ("---...Tool ini Digunakkan untuk mendownload Profile instagram Seseorang...---")
result = translator.translate('---...Tool ini Digunakkan untuk mendownload Profile instagram Seseorang...---', src='id' , dest='en')
print (result.text)

print ("|-------------------------------------|")
print ("| Author   : XnuversXploitXen         |")
print ("| You Tube : https://bit.ly/Xnuvers   |")
print ("| github   : https://bit.ly/Xnuvrs1   |")
print ("| Facebook : https://bit.ly/Fesbuck   |")
print ("| Instagram: https://bit.ly/Xnvrs13   |")
print ("| Site     : http://bit.ly/Mykingbee  |")
print ("|-------------------------------------|")
print ('\n')

print ("/////////////////////////////////////////////////////////////////")

Xnuvers = instaloader.Instaloader()


a = input("Masukan Username = ")
print ("Download... 0%")
time.sleep(3)
print ("Download... 55%")
time.sleep(3)
print ("Download... 99%")
time.sleep(2)
print ("Download... 100")
time.sleep(1)


Xnuvers.download_profile(a,profile_pic_only=True)

print ('\n')

print ("========IN ENGLISH========")

a = 'In the directory from where you run your .py code. There will be a new folder'
b = '''named as the username, inside you'll find the jpg file and other zip files.'''
c = '''Just delete the other files and copy the jpg anywhere, that's it.'''

print(a + b + c)

print ('\n')

print ("========IN INDONESIA========")
result = translator.translate(a + b + c, src='en' , dest='id')
print (result.text)

print ('\n')

print ("========IN INDONESIA========")
XU = 'Foto ini terdownload dimana Tools ini dijalankan, diletakan, bisa dipindahkan'.upper()
XN = 'menggunakan Perintah linux mv / copy lalu letakan di file download anda'.upper()
print (XU + XN)

print ('\n')

print ("========IN ENGLISH========")
result = translator.translate(XU + XN, src='id' , dest='en')
print (result.text)

print('\n')

input("tekan enter untuk mengakhiri...!!!")
time.sleep(3)

exit()
