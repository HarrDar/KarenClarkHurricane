import os

header = "NAME           LANDFALL_DATE  MAX_WIND_SPEED(kn)"

def populateReport(reportFile, storms, location, toPrint):
	f = None
	if toPrint:
		printReport()
	else:
		f = createReport(reportFile)

	hitCt = 0
	for st in storms:
		if location.hitBy(st):
			hitCt += 1
			addStormToReport(f,st, toPrint)
			
	if not toPrint:
		f.close()
		print("Output completed!", hitCt, "Storms hit given location.")

def createReport(fileName):
	f = open(fileName, 'w')
	f.write(header + "\n")
	print("File", fileName, "created, beginning output...")
	return f

def printReport():
	print(header)

def addStormToReport(f, storm, toPrint):
	if toPrint:
		print(reportFormat(storm))
	else:
		f.write(reportFormat(storm)+"\n")

def reportFormat(storm):
	stormName = storm.getName()
	date = storm.getLandfallDate()
	dateFormat = ("0" if date.month < 10 else '') + str(date.month) + "/" + ("0" if date.day < 10 else '') + str(date.day) + "/" + str(date.year)
	windSpeed = str(storm.getMaxWindSpeed())
	return stormName[:15] + (" "*max(0,(15-len(stormName)))) + dateFormat + (" "*5) + windSpeed