import geojson
from shapely.geometry import shape, Point
import pdb

import storm

class Location:

	name = ""
	polygon = None

	def __init__(self,name,file):
		self.name = name
		with open(file) as f:
			self.polygon = geojson.load(f)

	def contains(self,point):
		return self.containsSpot(point[0],point[1])

	def containsSpot(self, lati, longi):
		#pdb.set_trace()
		p = Point(longi,lati)
		for feature in self.polygon['features']:
			poly = shape(feature['geometry'])
			if poly.intersects(p):
				return True
		return False
