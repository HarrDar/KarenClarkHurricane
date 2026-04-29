import os

# This headers kinda arbitrary size-wise, just gave 15 characters to name and the rest fits within the title
header = "NAME           LANDFALL_DATE  MAX_WIND_SPEED(kn)"

# populateReport will run through each of the storms to see if they hit using the hitBy function in the location class.
def populateReport(reportFile, storms, location, startingDate, toPrint):
	f = None
	if toPrint:
		printReport()
	else:
		f = createReport(reportFile)

	hitCt = 0
	for st in storms:
		if st.getLatestDate().year >= startingDate and location.hitBy(st):
			hitCt += 1
			addStormToReport(f,st,toPrint)
			
	if not toPrint:
		f.close()
		print("Output completed!", hitCt, "Storms hit", location.name, "since", startingDate,)

# createReport just creates the report file and returns the stream.
def createReport(fileName):
	f = open(fileName, 'w')
	f.write(header + "\n")
	print("File", fileName, "created, beginning output...")
	return f

# printReport, well, you can guess what it does.
def printReport():
	print(header)

# addStormToReport either writes to stream or prints, depending on flags.
def addStormToReport(f, storm, toPrint):
	if toPrint:
		print(reportFormat(storm))
	else:
		f.write(reportFormat(storm)+"\n")

# reportFormat puts the stormdata in a desired report format, returns as a one line string.
def reportFormat(storm):
	stormName = storm.getName()
	date = storm.getLandfallDate()
	dateFormat = ("0" if date.month < 10 else '') + str(date.month) + "/" + ("0" if date.day < 10 else '') + str(date.day) + "/" + str(date.year)
	windSpeed = str(storm.getMaxWindSpeed())
	return stormName[:15] + (" "*max(0,(15-len(stormName)))) + dateFormat + (" "*5) + windSpeed