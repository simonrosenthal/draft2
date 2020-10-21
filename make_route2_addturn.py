"""
CIS 422 
Project 1

The arithmetic for making the route

"""
import math
from gpx_route2 import Route
from find_turn import find_turn

earth_radius = 6370.856
math_2pi = math.pi * 2
pis_per_degree = math_2pi / 360


def lat_degree2km(dif_degree=.0001, radius=earth_radius):
    return radius * dif_degree * pis_per_degree


def lat_km2degree(dis_km=111, radius=earth_radius):
    return dis_km / radius / pis_per_degree


def lng_degree2km(dif_degree=.0001, center_lat=22):
    real_radius = earth_radius * math.cos(center_lat * pis_per_degree)
    return lat_degree2km(dif_degree, real_radius)


def lng_km2degree(dis_km=1, center_lat=22):
    real_radius = earth_radius * math.cos(center_lat * pis_per_degree)
    return lat_km2degree(dis_km, real_radius)


def ab_distance(a_lat, a_lng, b_lat, b_lng):
    center_lat = .5 * a_lat + .5 * b_lat
    lat_dis = lat_degree2km(abs(a_lat - b_lat))
    lng_dis = lng_degree2km(abs(a_lng - b_lng), center_lat)
    return math.sqrt(lat_dis ** 2 + lng_dis ** 2)




def find_turnpoints(head, tail, Points, Route):
    """
    DOES FIND WHEN ROADS CHANGE WITHOUT USING BINARY SEARCH

    DOES NOT IDENTIFY DISTANCE
    DOES NOT IDENTIFY TURN DIRECTION
    DOES NOT IDENTIFY TIME TILL NEXT TURN
    """
 #   """
    #compare street name of head with street name of tail, if they are not the same:
    #print("BEGNINNING at point: ", head, " ", Points[head].get_roadname(), " comparing to street: ", \
          #" and: ", tail, " ", Points[tail].get_roadname())

    if Points[head].get_roadname() != Points[tail].get_roadname():
        #and if there are more than two points
        if head + 1 != tail:
            midpoint = (head + tail) // 2
            #if there is just one point between head and tail
            if (head + 1 == midpoint):
                if Points[head].get_roadname() != Points[midpoint].get_roadname():
                    #print("at point: ", head, " ", Points[head].get_roadname(), " make a turn onto street: ", \
                    #     " and: ", midpoint, " ", Points[midpoint].get_roadname())
                    Route.add_turnpoint(Points[midpoint])
                    find_turnpoints(midpoint, tail, Points, Route)
                else:
                    find_turnpoints(midpoint, tail, Points, Route)
            else:
                if Points[head].get_roadname() != Points[midpoint].get_roadname():
                    find_turnpoints(head, midpoint, Points, Route)
                    find_turnpoints(midpoint, tail, Points, Route)
                else:
                    find_turnpoints(midpoint, tail, Points, Route)
        else:
            #print("at point: ", head, " ", Points[head].get_roadname(), " make a turn onto street: ", \
            #     " and: ", tail, " ", Points[tail].get_roadname())
            Route.add_turnpoint(Points[tail])

    #check if a whole segment from head to tail is on the same road
    #do this by checking if midpoint has different name?
    elif Points[head].get_roadname() == Points[tail].get_roadname():
        if head + 1 != tail:
            midpoint = (head+tail)//2
            if Points[head].get_roadname() != Points[midpoint].get_roadname():
                find_turnpoints(head, midpoint, Points, Route)
            if Points[midpoint].get_roadname() != Points[tail].get_roadname():
                find_turnpoints(midpoint, tail, Points, Route)
  #  """
def sortSecond(point):
    return point.index
if __name__ == '__main__':
    print("=================== what's good ya'll let's see if we can get this to work =================== \n \n")
    newRoute = Route()
    newRoute.create_route("uploads/09_27_20.gpx")
    print(newRoute.pntCount)
    print("=================== GPX DATA EXTRACTED STARTING THE TURNPOINT SEARCH =================== \n \n")

    """
    print(newRoute.pntCount)
    print(newRoute.points[0].lat)
    print(newRoute.points[0].lon)
    print(newRoute.points[0].index)
    newRoute.points[0].get_roadname()
    print("from within route shit here's the address: " + newRoute.points[0].roadname)
    """
 #   """

    find_turnpoints(0, newRoute.pntCount-1, newRoute.points, newRoute)
    print("=================== TURN POINTS GOTTEN, STARTING TO ORGANIZE ARRAY OF TURNS ==================== \n \n")
    #sort the turns array in sequential order
    newRoute.turns.sort(key = lambda x: newRoute.points[x.pointIndex].index, reverse = False)

    print("==================== TURNS ORGANIZED NOW DISPLAYING ============================= \n \n")
    totalDistance = 0
    for turn in newRoute.turns:
        if(newRoute.turns.index(turn) != 0):
            print(newRoute.turns.index(turn)-1)
            previousTurnPoint = newRoute.points[newRoute.turns[newRoute.turns.index(turn)-1].pointIndex]
            currentTurnPoint = newRoute.points[turn.pointIndex]
            dist = ab_distance(previousTurnPoint.get_latlon()[0], previousTurnPoint.get_latlon()[1], \
                               currentTurnPoint.get_latlon()[0], currentTurnPoint.get_latlon()[1])
            totalDistance += dist
        print("We need to turn at: " , newRoute.points[turn.pointIndex].get_roadname(), "the turn is ",
            find_turn(newRoute.points[turn.pointIndex-1].lon, newRoute.points[turn.pointIndex-1].lat,
                newRoute.points[turn.pointIndex].lon, newRoute.points[turn.pointIndex].lat,
                newRoute.points[turn.pointIndex+1].lon, newRoute.points[turn.pointIndex+1].lat) , 
            " with index: ", newRoute.points[turn.pointIndex].index,
              "the two points have a distance of: ", totalDistance, " kilometers")
