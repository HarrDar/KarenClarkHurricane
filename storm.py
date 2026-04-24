import os
import datetime

class Reading:
	time = None
	# ONLY to be used for verification
	landedTrue = False
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
	latN = 0
	longN = 0
	latD = ''
	longD = ''
	max_wind_kts = 0
	max_pressure = 0
	wind_types = ['34_kt_ne','34_kt_se','34_kt_sw','34_kt_nw','50_kt_ne','50_kt_se','50_kt_sw','50_kt_nw','64_kt_ne','64_kt_se','64_kt_sw','64_kt_nw']
	winds = {}

	def __init__(self,data):
		self.time = datetime.date.fromisoformat(data[0] + "T" + data[1].replace(" ","") + "00")
		self.landedTrue = data[2]
		self.status = data[3].replace(" ", "")
		self.latN = float(data[4][:-1])
		self.latD = data[4][-1:]
		self.longN = float(data[5][:-1])
		self.longD = data[5][-1:]
		self.max_wind_kts = data[6]
		self.max_pressure = data[7]
		for i in range(12):
			winds[wind_types[i]] = int(data[8+i])



class Storm:
	storm_id = ""
	storm_name = ""
	number_obs = 0
	readings = []
	
	def __init__(self, data):
		self.storm_id = data[0]
		self.storm_name = data[1].replace(" ", "")
		self.number_obs = int(data[2])

	def addReading(self,data):
		self.readings.append(Reading(data))
