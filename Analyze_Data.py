import csv
from array import *
import time


class Analyze_Data:
	#cities = (("Boulder", "CO"),("New_York","NY"), ("Los_Angeles","CA"))
	cities = ["BoulderCO","New_YorkNY", "Los_AngelesCA"]
	name = 'BoulderCO' #************************************************
	
	def readFromForecast(self, city):
		name = city
		rowCount = 0
		forecastVals = []
		numCol = 10
		with open(name+"high.csv", 'rb') as csvfile:
			numRows = sum(1 for row in csvfile)
			print numRows
			
		with open(name+"high.csv", 'rb') as csvfile:
			fieldnames = ['1','2','3','4','5','6','7','8','9','10','date']
			dr = csv.DictReader(csvfile, fieldnames=fieldnames)
			for row in dr:
				rowCount = rowCount + 1
				if (rowCount >= numRows - 9):
					val = row[str(numCol)] #10 days out should be yesterday, sleep at the beginning of forecast pull?
					#[val] + forecastVals
					forecastVals.append(val)
					print str(numCol)
					numCol = numCol - 1;
					print rowCount
		forecastVals.reverse()
		print forecastVals
		return forecastVals

				
		
	def readFromObserved(self, city):
		name = city
		rowCount = 0
		observedVal = (0,0)
		with open(name+"_Observed.csv", 'r') as csvfile:
			numRows = sum(1 for row in csvfile)
			print numRows
			
		with open(name+"_Observed.csv", 'r') as csvfile:
			fieldnames = ['Hi', 'Lo', 'Date']
			reader = csv.DictReader(csvfile, fieldnames=fieldnames)
			for row in reader:
				rowCount = rowCount + 1
				if (rowCount >= numRows):
					observedVal = (row['Hi'], row['Date'])
					print rowCount
					print observedVal
					return observedVal
					
	def performAnalysis(self, temp, forecast, city):
		name = city
		accuracyByDay = []
		predictedByDay = forecast
		predictedByDay.reverse()
		numRows = 0
		for x in forecast:
			acc = abs((float(x)/float(temp[0]))-1)*100
			acc = round(acc, 2)
			print acc
			accuracyByDay.append(acc)
		#accuracyByDay.reverse()
		print accuracyByDay
		with open(name+"analysis.csv", 'r') as csvfile:
			fieldnames = ['days-out', 'predicted', 'observed', 'percent-off', 'date-observed']
			numRows = sum(1 for row in csvfile)
			
		with open(name+"analysis.csv", 'a') as csvfile:
			fieldnames = ['days-out', 'predicted', 'observed', 'percent-off', 'date-observed']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			if (numRows == 0): #change?
				writer.writeheader()
			daysOut = 10
			for x in accuracyByDay:
				grabDay = abs(daysOut-10)
				writer.writerow({'days-out': str(daysOut), 'predicted': predictedByDay[grabDay], 'observed': temp[0], 'percent-off': x, 'date-observed': temp[1]})
				daysOut = daysOut - 1
				
				
	def update(self, listOfCities):
		time.sleep(120)
		#x = Analyze_Data()
		for c in cities:
			observedTemp = self.readFromObserved(c)
			print observedTemp[0] + " is the observed temp in city " + c
			forecastTemps = self.readFromForecast(c)
			print forecastTemps
			self.performAnalysis(observedTemp, forecastTemps, c)
			
			
#****test****
'''
cities = ["BoulderCO","New_YorkNY", "Los_AngelesCA"]
x = Analyze_Data()
for c in cities:	
	x.readFromForecast(c)
	observedTemp = x.readFromObserved(c)
	print observedTemp[0] + " is the observed temp in city " + c
	forecastTemps = x.readFromForecast(c)
	print forecastTemps

	x.performAnalysis(observedTemp, forecastTemps, c) 
'''







