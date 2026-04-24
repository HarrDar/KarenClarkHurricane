import math
import os
from storm import Storm

fileName = "hurdat2.txt"

def main():
	storms = readFile()
	print(storms[50:100])

def readFile():
	storms = []
	newstorm = None
	i = 0
	with open (fileName, 'r') as file:
		for line in file:
			data = line.strip().split(',')
			if len(data) == 4:
				if newstorm is not None:
					storms.append(newstorm)
				newstorm = Storm(data)
			elif newstorm is not None and len(data) == 21:
				newstorm.addReading(data)
			else:
				print("ERR: IMPROPER DATA LINE")
	return storms
main()