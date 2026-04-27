import os
import sys

import storm
import geo
import report

fileName = "data/hurdat2.txt"
locationFile = "data/florida.geojson"
reportFile = "reports/FloridaReport.txt"

def main(args):
	print(args)
	# Read in Data
	storms = storm.readStormFile(fileName)
	location = geo.Location("Florida", locationFile)

	f = report.createReport(reportFile)
	for st in storms:
		if location.hitBy(st):
			report.addStormToReport(f,st)
	f.close()
			
main(sys.argv)