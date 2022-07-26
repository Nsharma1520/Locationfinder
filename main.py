import phonenumbers
from test import number
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from opencage.geocoder import OpenCageGeocode 
key = "7a25ae25b2d2438b846772213c2a7c74"

ch_nmber = phonenumbers.parse(number, "CH")
yourLocation = geocoder.description_for_number(ch_nmber, "en")
print(number)
print(yourLocation)

service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number,"en"))

geocoder = OpenCageGeocode(key)
query = str(yourLocation)
result = geocoder.geocode(query)
# print(result)

lat = result[0]['geometry']['lat']

lng = result[0]['geometry']['lng']

print(lat, lng)

# locat = str(lat,lng)
# print(locat)



'''<<<<<<<<<<<<<----------------------------------------------------------------------------->>>>>>>>'''

# importing modules
from geopy.geocoders import Nominatim

# calling the nominatim tool
geoLoc = Nominatim(user_agent="GetLoc")

# passing the coordinates
locname = geoLoc.reverse(f'{lat},{lng}')

# printing the address/location name
print(locname.address)


# ********************************************************************************************

'''import folium


m = folium.Map(location=[lat, lng], tiles="Stamen Toner", zoom_start=13)

folium.Circle(
    radius=100,
    location=[lat, lng],
    popup="The Waterfront",
    color="crimson",
    fill=False,
).add_to(m)
m.save('index1.html')'''