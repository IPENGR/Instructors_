import phonenumbers
from test import number

#to find location
from phonenumbers import geocoder #(geocoder is a built in function in phonenumber)

ch_number = phonenumbers.parse(number,"CH")   #passing parameters number and country history
print(geocoder.description_for_number(ch_number,"en"))  #to see the location in english language

#to find the service provider
from phonenumbers import carrier #(carrier is a built in function in phonenumber)

service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number,"en"))