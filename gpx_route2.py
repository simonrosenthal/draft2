import gpxpy
from decimal import Decimal
from api_route2 import getStreetNameFromApi

class Route():

    def __init__(self):
        self.points = []
        self.turns = []
        self.pntCount = 0
        self.turnCount = 0
        self.lastFiltered = 0

    def add_point(self, lat, lon):
        point = Point(lat, lon, self.pntCount)
        self.points.append(point)
        self.pntCount += 1
        road = self.points[self.pntCount-1].get_roadname()
        prevRoad = self.points[self.pntCount - 2].get_roadname()
        print("current is " + road)
        if self.lastFiltered > 0 and road != prevRoad:
            self.filter_points()
        elif road != prevRoad:
            self.lastFiltered = self.pntCount - 2

    def add_turnpoint(self, point):
        newTurn = Turn(point.index)
        self.turns.append(newTurn)
        self.turnCount += 1

    def create_route(self, fileRoute):
        filename = open(fileRoute, 'r')
        gpx = gpxpy.parse(filename)
        #Added this line to help clean up data?
        gpx.simplify(0.4)

        for track in gpx.tracks:
            for segment in track.segments:
                for gpxPoint in segment.points:
                    lat = Decimal(gpxPoint.latitude)
                    lon = Decimal(gpxPoint.longitude)
                    self.add_point(lat, lon)

    def filter_points(self):
        current = self.points[self.lastFiltered + 1].roadname
        indices =  self.pntCount - self.lastFiltered - 2
        start = self.points[self.lastFiltered]
        end = self.points[self.lastFiltered + indices + 1]
        if start.roadname == end.roadname:
            del self.points[(start.index + 1):end.index]
            self.pntCount = self.pntCount-indices
            self.points[-1].index = start.index + 1     
        else:
            self.lastFiltered = self.lastFiltered + indices 


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

    def get_latlon(self):
        return [float(self.lat), float(self.lon)]
class Turn():

    def __init__(self, index):
        self.pointIndex = index
        self.direction = ""
        self.turnName = ""
        self.distance = None


