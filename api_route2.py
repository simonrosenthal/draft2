import requests

def getStreetNameFromApi(point):
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
        print(response.json())
        addy = response.json()['StreetAddresses']
        return addy
