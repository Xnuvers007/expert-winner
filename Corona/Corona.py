# PYTHON 3.7
# BY XnuversXploitXen

from covid import Covid
import matplotlib.pyplot as pyplot
import time
from datetime import datetime
from datetime import date
import time

covid = Covid()

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
print ("=======================================")

print("Cek Corona dari berbagai negara (tekan: 1)")
print("Cek Corona Dari Dunia (tekan: 2)")
ch = int(input("Masukan Pilihanmu : "))

if ch == 1:
    country = input("Masukan nama Negara = ")
    data = covid.get_status_by_country_name(country)
    cadr = {
        key: data[key]
        for key in data.keys() & {"confirmed", "active", "deaths", "recovered"}
    }

    n = list(cadr.keys())
    v = list(cadr.values())
elif ch == 2:
    cadr = {
        "Terkonfirmasi": covid.get_total_confirmed_cases(),
        "Aktif": covid.get_total_active_cases(),
        "Meninggal": covid.get_total_deaths(),
        "Sembuh": covid.get_total_recovered(),
    }

    v = list(cadr.values())
    n = list(cadr.keys())

print(cadr) # print data

pyplot.title("Corona Tracker")
pyplot.bar(range(len(cadr)), v, tick_label=n)
pyplot.show()
