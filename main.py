import os

import storm
import geo
import report

fileName = "hurdat2.txt"
locationFile = "florida.geojson"

def main():
	# Read in Data
	storms = storm.readStormFile(fileName)
	location = geo.Location("Florida", locationFile)

	f = report.createReport("FloridaReport.txt")
	for st in storms:
		if location.hitBy(st):
			report.addStormToReport(f,st)
	f.close()
			
main()