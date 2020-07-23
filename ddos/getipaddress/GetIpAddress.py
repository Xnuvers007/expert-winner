import socket
import pyfiglet
from googletrans import Translator

translator = Translator()

result = pyfiglet.figlet_format("XNUVERS25", font = "dotmatrix" ) 
print(result)
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

x = translator.translate('Silahkan Masukan Nama Website (contoh = google.com) = ')

print (x.text)
a = input("Silahkan Masukan Nama Website (contoh = google.com) = ")
addr = socket.gethostbyname(a)

print ('\n')

y = translator.translate('Ip Address dari {} adalah {}'.format(a, addr))

print (y.text)
print ('Ip Address dari {} adalah {}'.format(a, addr))
