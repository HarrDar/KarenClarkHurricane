import geojson
from shapely.geometry import shape, Point

import storm

class Location:

	name = ""
	polygons = None

	# class is initialized by loading in the given geojson file, then converting each of its polygons to shapely objects.
	# GeoJSON may not be entirely nessecary here; I chose it since it gave a great level of flexibility when it comes to creating and reading geographic areas, but most of it is outside the scope of this assignment.
	# Regardless, I build my programs to be easy to expand upon, and GeoJSON would be very helpful for larger scopes. Not to mention it is convenient and easy to create for a 1 week assignment.
	def __init__(self,name,file):
		self.name = name
		f = open(file, 'r')
		poly = geojson.load(f)
		self.polygons = []
		for feature in poly['features']:
			self.polygons.append(shape(feature['geometry']))
		f.close()

	# hitBy takes a storm object and walks through its readings until a reading is within this object's boundaries, 
	# setting the readings landed variable to True then returning a boolean describing whether or not the storm ever hit.
	def hitBy(self, storm):
		for reading in storm.getReadings():
			if self.contains(reading.getLocation()):
				reading.Landed()
				return True
		return False

	# contains is a simple wrapper for containsSpot
	def contains(self,point):
		return self.containsSpot(point[0],point[1])

	# containsSpot checks if the given point is in any of this location's boundaries.
	def containsSpot(self, lati, longi):
		p = Point(longi,lati)
		for feature in self.polygons:
			if feature.intersects(p):
				return True
		return False
