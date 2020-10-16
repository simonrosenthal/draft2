import requests
import time

#http://www.mapquestapi.com/geocoding/v1/reverse?key=KEY&location=30.333472,-81.470448&includeRoadMetadata=true&includeNearestIntersection=true
i = 0

def getStreetNameFromApi(point):
        print (point.lat, point.lon)
        parameters = {
            "key": "cKkKyWIc0aAFiaqmlSopLLuKJuXuj4di",
            "location": str(point.lat) + "," + str(point.lon),
            "includeRoadMetadata" : "true",
            "includeNearestIntersection" : "true"
        }
        response = requests.get(
            "http://www.mapquestapi.com/geocoding/v1/reverse",
            params=parameters)
        addy = response.json()['results'][0]['locations'][0]['street']
        print(addy)
        return addy

        """
        FOR OLD INTERFACE
        
        def getStreetNameFromApi(point):#, route):
                # print (point.lat, point.lon)
                parameters = {
                    "apiKey": "737eceecff3e4e79bdcb66de0e4173e3",
                    "version": "4.10",
                    "lat": point.lat,
                    "lon": point.lon,
                    "format": "json"
                }
        
                response = requests.get(
                    "https://geoservices.tamu.edu/Services/ReverseGeocoding/Webservice/v04_01/HTTP/default.aspx",
                    params=parameters)
                addy = response.json()['StreetAddresses'][0]['StreetAddress']
                return addy
        """
