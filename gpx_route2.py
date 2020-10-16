import gpxpy
from decimal import Decimal
from api_route2 import getStreetNameFromApi

class Route():

    def __init__(self):
        self.points = []
        self.turns = []
        self.pntCount = 0
        self.turnCount = 0

    def add_point(self, lat, lon):
        self.pntCount += 1
        point = Point(lat, lon, self.pntCount)
        self.points.append(point)

    def add_turnpoint(self, point):
        newTurn = Turn(point.index)
       #print("at point: ", point.index," ",point.get_roadname()," make a turn between street: ",  \
       #       " and: ", point.index-1," ", self.points[point.index-1].get_roadname())
        self.turns.append(newTurn)
        self.turnCount += 1

    def create_route(self):
        filename = open("uploads/09_27_20.gpx", 'r')
        gpx = gpxpy.parse(filename)
        #Added this line to help clean up data?
        gpx.simplify(0.5)

        for track in gpx.tracks:
            for segment in track.segments:
                for gpxPoint in segment.points:
                    lat = Decimal(gpxPoint.latitude)
                    long = Decimal(gpxPoint.longitude)
                    self.add_point(lat, long)

class Point():

    def __init__(self, lat, lon, index):
        self.lat = lat
        self.lon = lon
        self.index = index
        self.roadname = ""
        self.distance = 0

    def set_roadname(self, name):
        self.roadname = name

    def get_roadname(self):
        if(self.roadname == ""):
            self.set_roadname(getStreetNameFromApi(self))
        return self.roadname

class Turn():

    def __init__(self, index):
        self.pointIndex = index
        self.direction = ""


