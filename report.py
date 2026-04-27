import os

def createReport(fileName):
	f = open(fileName, 'w')
	f.write("NAME           LANDFALL_DATE  MAX_WIND_SPEED(kn) \n")
	return f

def addStormToReport(f, storm):
	f.write(reportFormat(storm))

def reportFormat(storm):
	stormName = storm.getName()
	date = storm.getLandfallDate()
	dateFormat = ("0" if date.month < 10 else '') + str(date.month) + "/" + ("0" if date.day < 10 else '') + str(date.day) + "/" + str(date.year)
	windSpeed = str(storm.getMaxWindSpeed())
	return stormName[:15] + (" "*max(0,(15-len(stormName)))) + dateFormat + (" "*5) + windSpeed + "\n"