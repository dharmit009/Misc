import json
import urllib.request, urllib.parse, urllib.error

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter An Address: ');
    if len(address) < 1: break;

    url = serviceurl + urllib.parse.urlencode({'address': address});
    print("Retriving: ", url);
    requesting_data = urllib.request.urlopen(url);
    data = requesting_data.read().decode();
    print("Retrieved: ", len(data), ' characters.')

    try:
        js = json.loads(data)
    except expression as identifier:
        js = None; 

    if not js or 'status' not in js or js['status'] != "OK":
        print("Failed To Retrieve The Data ...");
        print(data);
        continue;

    lat = js["results"][0]["geometery"]["location"]["lat"];
    lng = js["results"][0]["geometery"]["location"]["lng"];
    loc = js["results"][0]["formatted_address"];


    print("Location:", loc)
    print("Latitude: ", lat, "\nLongitude: ", lng)
