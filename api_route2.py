import requests

def getStreetNameFromApi(point):
        # print (point.lat, point.lon)
        parameters = {
            "apiKey": "eb6a7ee7e8ad43f69ea61d99c1b28daa",
            "version": "4.10",
            "lat": point.lat,
            "lon": point.lon,
            "format": "json"
        }

        response = requests.get(
            "https://geoservices.tamu.edu/Services/ReverseGeocoding/Webservice/v04_01/HTTP/default.aspx",
            params=parameters)
        print(response.json())
        addy = response.json()['StreetAddresses'][0]['StreetAddress']
        return addy