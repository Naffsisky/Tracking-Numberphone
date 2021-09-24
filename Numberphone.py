import phonenumbers
from phonenumbers import timezone,geocoder,carrier

user = (input('Masukan nomer telepon ex: +62 : ')) 

phonenumber = phonenumbers.parse(user)
timeZone = timezone.time_zones_for_number(phonenumber)
Carrier = carrier.name_for_number(phonenumber,'id')
Region = geocoder.description_for_number(phonenumber,'id')

print(phonenumber)
print('Asal Nomer = ', timeZone)
print('Provider = ', Carrier)
print('Negara = ', Region)