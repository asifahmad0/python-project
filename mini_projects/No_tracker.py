import phonenumbers
from phonenumbers import geocoder 
from phonenumbers import carrier

num= "+917761917649"

ch_number= phonenumbers.parse(num, "CH")
ro_number= phonenumbers.parse(num, "RO")

cuntry=geocoder.description_for_number(ch_number, "en")
s_provider= carrier.name_for_number(ro_number, "en")
print(cuntry)
print(s_provider)
