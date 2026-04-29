import os
import sys

import storm
import geo
import report

defaultData = "data/hurdat2.txt"
defaultLocation = "data/florida.geojson"
defaultReport = "reports/FloridaReport.txt"
defaultDateStart = 1900

flags = ['-d', '-h', '-l', '-r', '-p']

def isFileFormat(file, form):
	return file[-1*len(form):] == form

def stripFileFormat(file, form):
	nf = file[:-1*len(form)]
	while nf.find('/') != -1:
		nf = nf[nf.index('/')+1:]
	return nf

# arguments processed in order given in command; i.e. -d will overwrite previous flags
# -def = use all defaults. this happens by default but its here if you want to be specific
# -h = set hurricane data file
# -l = set location file
# -r = set output file
# -d = set starting year
# -p = print output to console instead
def generateReport(args):
	dataFile, locationFile, reportFile, startingDate = defaultData, defaultLocation, defaultReport, defaultDateStart
	toPrint = False

	# Argument Handling
	i = 1
	errFlags = []
	while i < len(args):
		a = args[i]
		# Case Flag
		if len(a) > 0 and a[0] == '-':
			# Bad flag
			if a not in flags:
				errFlags.append("ERR: UNKNOWN FLAG " + args[i])
			# Default flag needs no further input
			elif a == "-def":
				dataFile = defaultData
				locationFile = defaultLocation
				reportFile = defaultReport
			elif a == "-p":
				toPrint = True
			# For other flags with given arguments...
			else:
				# If end of arguments
				if i+1 >= len(args):
					errFlags.append("ERR: INCOMPLETE ARGUMENT FOR FLAG " + args[i])
				# If another flag immediately proceeds
				elif (len(args[i+1]) > 0 and args[i+1][0] == '-'):
					errFlags.append("ERR: NO GIVEN ARGUMENT FOR FLAG " + args[i])
				# Is this even possible?
				elif len(args[i+1]) == 0:
					errFlags.append("ERR: EMPTY ARGUMENT FOR FLAG " + args[i])
				# Valid Arguments (probably)
				else:
					i += 1
					f = args[i]
					if a == '-h':
						if not isFileFormat(f,'.txt'):
							errFlags.append("ERR: INCORRECT FILE FORMAT FOR HURRICANE DATA (.txt expected)")
						elif len(f) < 5:
							errFlags.append("ERR: NO FILENAME GIVEN FOR HURRICANE DATA")
						else:
							dataFile = "data/" + f
					elif a == '-l':
						if not isFileFormat(f,'.geojson'):
							errFlags.append("ERR: INCORRECT FILE FORMAT FOR LOCATION DATA (.geojson expected)")
						elif len(f) < 9:
							errFlags.append("ERR: NO FILENAME GIVEN FOR LOCATION DATA")
						else:
							locationFile = "data/" + f
					elif a == '-d':
						if not f.isnumeric():
							errFlags.append("ERR: INVALID STARTING YEAR")
						else:
							startingDate = int(f)
					elif a == '-r':
						reportFile = "reports/" + f
		# Case Floating Argument
		elif len(a) > 0:
			errFlags.append("ERR: ARGUMENT " + a + " GIVEN WITH NO FLAG ")
		# Is this even possible?
		else:
			errFlags.append("ERR: EMPTY ARGUMENT")
		i += 1

	# Print all accumulated errors
	for err in errFlags:
		print(err)
	if len(errFlags) > 0:
		exit()

	# Read in Data
	storms = storm.readStormFile(dataFile)
	location = geo.Location(stripFileFormat(locationFile, '.geojson'), locationFile)

	# Generate Report
	report.populateReport(reportFile,storms,location,startingDate,toPrint)
			
generateReport(sys.argv)
