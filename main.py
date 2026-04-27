import os

import storm
import geo
import report

fileName = "data/hurdat2.txt"
locationFile = "data/florida.geojson"
reportFile = "reports/FloridaReport.txt"

def main():
	# Read in Data
	storms = storm.readStormFile(fileName)
	location = geo.Location("Florida", locationFile)

	f = report.createReport(reportFile)
	for st in storms:
		if location.hitBy(st):
			report.addStormToReport(f,st)
	f.close()
			
main()