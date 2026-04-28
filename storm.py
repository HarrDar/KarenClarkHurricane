import os
import datetime

def readStormFile(fileName):
	storms = []
	newstorm = None
	ct = 0
	file = open(fileName, 'r')
	print("File", fileName, "opened, beginning processing...")
	for line in file:
		data = line.strip().split(',')
		if len(data) == 4:
			if newstorm is not None:
				storms.append(newstorm)
				ct +=1
			newstorm = Storm(data)
		elif newstorm is not None and len(data) == 21:
			newstorm.addReading(data)
		else:
			print("ERR: IMPROPER DATA LINE")
	file.close()
	print("Read in " + str(ct) + " Storms from " + fileName)
	return storms

class Reading:
	time = None
	# C – Closest approach to a coast, not followed by a landfall
	# G – Genesis
	# I – An intensity peak in terms of both pressure and wind
	# L – Landfall (center of system crossing a coastline)
	# P – Minimum in central pressure
	# R – Provides additional detail on the intensity of the cyclone when rapid changes are underway
	# S – Change of status of the system
	# T – Provides additional detail on the track (position) of the cyclone
	# W – Maximum sustained wind speed
	# LANDFALLS IDENTIFIED HERE ONLY USED FOR VERIFICATION
	record_identifier = False
	# For MY calculations
	landed = False
	# TD – Tropical cyclone of tropical depression intensity (< 34 knots)
	# TS – Tropical cyclone of tropical storm intensity (34-63 knots)
	# HU – Tropical cyclone of hurricane intensity (> 64 knots)
	# EX – Extratropical cyclone (of any intensity)
	# SD – Subtropical cyclone of subtropical depression intensity (< 34 knots)
	# SS – Subtropical cyclone of subtropical storm intensity (> 34 knots)
	# LO – A low that is neither a tropical cyclone, a subtropical cyclone, nor an extratropical cyclone (of any intensity)
	# WV – Tropical Wave (of any intensity)
	# DB – Disturbance (of any intensity)
	status = ""
	lat = 0
	longi = 0
	max_wind_kts = 0
	max_pressure = 0
	wind_types = ['34_kt_ne','34_kt_se','34_kt_sw','34_kt_nw','50_kt_ne','50_kt_se','50_kt_sw','50_kt_nw','64_kt_ne','64_kt_se','64_kt_sw','64_kt_nw']
	winds = {}

	def __init__(self,data):
		# self.time = datetime.datetime.fromisoformat(data[0] + data[1].replace(" ",""))
		# YYYYMMDD & HHMM
		cleanDate = data[0].replace(" ","")
		cleanTime = data[1].replace(" ","")
		self.time = datetime.datetime(int(cleanDate[:4]), int(cleanDate[4:6]), int(cleanDate[6:8]), int(cleanTime[:2]), int(cleanTime[2:4]))
		self.record_identifier = data[2]
		self.status = data[3].replace(" ", "")
		self.lati = float(data[4][:-1])*(-1 if data[4][-1] == "S" else 1)
		self.longi = float(data[5][:-1])*(-1 if data[5][-1] == "W" else 1)
		self.max_wind_kts = int(data[6])
		self.max_pressure = int(data[7])
		for i in range(12):
			self.winds[self.wind_types[i]] = int(data[8+i])

	def getLocation(self):
		return [self.lati, self.longi]

	def getDate(self):
		return self.time

	def Landed(self):
		self.landed = True

	def isLanded(self):
		return self.landed

	def NotLanded(self):
		self.landed = False

	def getMaxWind(self):
		return self.max_wind_kts

class Storm:
	storm_id = ""
	storm_name = ""
	number_obs = 0
	readings = None
	maxWindSpeed = 0
	
	def __init__(self, data):
		self.storm_id = data[0]
		self.storm_name = data[1].replace(" ", "")
		self.number_obs = int(data[2])
		self.readings = []

	def addReading(self,data):
		newReading = Reading(data)
		self.readings.append(newReading)
		self.maxWindSpeed = max(self.maxWindSpeed, newReading.getMaxWind())

	def getReadings(self):
		return self.readings

	def getName(self):
		return self.storm_name

	def getMaxWindSpeed(self):
		return self.maxWindSpeed

	def getLandfallDate(self):
		for reading in self.readings:
			if reading.isLanded():
				return reading.getDate()