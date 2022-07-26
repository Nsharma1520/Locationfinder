import phonenumbers
# from test import number
from phonenumbers import geocoder
from phonenumbers import carrier
# from phonenumbers import timezone
from opencage.geocoder import OpenCageGeocode 
key = "7a25ae25b2d2438b846772213c2a7c74"

'''Input number from user'''
number = input("Enter your mobile number : ")
ch_nmber = phonenumbers.parse(number, "CH")
print("Your Mobile number is : ", number)

'''To find country '''
yourLocation = geocoder.description_for_number(ch_nmber, "en")
print("Country : ", yourLocation)

'''To find carrier service company name'''
service_number = phonenumbers.parse(number, "RO")
print("Carrier : ", carrier.name_for_number(service_number,"en"))

'''To find latitude and Longitude of given number'''
geocoder = OpenCageGeocode(key)
query = str(yourLocation)
result = geocoder.geocode(query)
# print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print("Latitude : ", lat, "Longitude : ", lng)


# importing modules
from geopy.geocoders import Nominatim

# calling the nominatim tool
geoLoc = Nominatim(user_agent="GetLoc")

# passing the coordinates
locname = geoLoc.reverse(f'{lat},{lng}')

# printing the address/location name
print("Address : ", locname.address)