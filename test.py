from props import getNode, root

def great_circle_route(a,b):
    """mock function for this test to work"""
    return 125.22

#create some nodes
gps = getNode("/sensors/gps", create=True)
fdm = getNode("/aero/engine", create=True)
waypoint = getNode("/navigation/route/target", create=True)
ap = getNode("/autopilot/settings", create=True)
waypoint.lat=waypoint.lon=0


struct=("""
The Structure built in this test is:
-/aero/engine/
             |-reverser
             |-rev_throtle
             |-position
             _ name
 /autopilot/settings/
                    _target_heading
 /navigation/route/target/
                         |-waypoint.lat
                         _ waypoint.lon
 /sensors/gps/
             |-lat
             |-lon
              _alt
""")

print (struct)

#testing populating some nodes
(gps.lat, 
 gps.lon, 
 gps.alt, 
 gps.speed, 
 gps.ground_track) = (40.741895,
                      -73.989308,
                      1225.25,
                      325,
                      4.5)
(fdm.reverser, 
 fdm.rev_throtle, 
 fdm.position, 
 fdm.name) = (False,
              0.25, 
              23, 
              "Garuff")

##playing with nodes usage
heading = great_circle_route([gps.lat, gps.lon], [waypoint.lat, waypoint.lon])
ap.target_heading = heading

#checking it comes together
print """
------------------Checking the Property Tree management on Python-------------\n"""
print("the node /sensors/gps/lat is " + str(gps.lat))
print("the node /sensors/gps/lon is " + str(gps.lon))
print("the node /aero/engine/reverser is " + str(fdm.reverser))
print ("the node /autopilot/settings/target_heading is " + str(ap.target_heading))
