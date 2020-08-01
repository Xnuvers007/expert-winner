# Python 3.7
# XnuversXploitXen
# v.0.1

import whois
import time

print ('''NOTICE: The expiration date displayed in this record is the date the
registrar' s sponsorship of the domain name registration in the registry is
Currently set to expire. This date does not necessarily reflect the expiration
Date of the domain name registrant’s agreement with the sponsoring
registrar. Users may consult the sponsoring registrar’s Whois database to
View the registrar’s reported date of expiration for this registration.
TERMS OF USE: You are not authorized to access or query our Whois

Database through the use of electronic processes that are high-volume and
Automated except as reasonably necessary to register domain names or

Modify existing registrations; the Data in VeriSign Global Registry
Services’ (“UeriSign") Whois database is provided by VeriSign for
information purposes only, and to assist persons in obtaining information
About or related to a domain name registration record. VeriSign does not
guarantee its accuracy. By submitting a Whois query, you agree to abide
By the following terms of use: You agree that you may use this Data only
for lawful purposes and that under no circumstances will you use this Data
To: (1) allow, enable. or otherwise support the transmission of mass
Unsolicited, commercial advertising or solicitations via e-mail, telephone,
or facsimile; or (2) enable high volume, automated, electronic processes
That apply to VeriSign (or its computer systems). The compilation,
Repackaging, dissemination or other use of this Data is expressly
Prohibited without the prior written consent of VeriSign. You agree not to
Use electronic processes that are automated and high-volume to access or
Query the Whois database except as reasonably necessary to register

Domain names or modify existing registrations. VeriSign reserves the right
To restrict your access to the Whois database in its sole discretion to ensure
operational stability. UeriSign may restrict or terminate your access to the
Whois database for failure to abide by these terms of use. VeriSign
Reserves the right to modify these terms at any time.

==========The Registry database contains ONLY .COM, .NET, .EDU domains and
Registrars.==========''')

a = input("Ip Address ? = ")

b = whois.whois(a)

print (b)

print("=====XnuversXploitXen"=====)

input("Press Enter To exit in 3 seconds")
time.sleep(3)
exit()
