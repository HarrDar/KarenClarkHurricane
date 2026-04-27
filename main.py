import math
import os
import storm
import geo

fileName = "hurdat2.txt"
locationFile = "florida.geojson"

def main():
	# Read in Data
	storms = storm.readFile(fileName)
	location = geo.Location("Florida", locationFile)

	# Take Input
	name = "MILTON"
	st = None
	for s in storms:
		if s.getName() == name:
			st = s
			break

	if st is None:
		print("STORM NAME NOT FOUND")
		exit()

	# Find Data
	for reading in st.getReadings():
		if location.contains(reading.getLocation()):
			reading.isLanded()
			print("LANDED")
		else:
			print("NOT LANDED")

	# Print Stuff

main()