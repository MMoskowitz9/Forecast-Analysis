import urllib2
import json
import csv
from array import *
import os.path
from Api_Pull import Api_Pull
#import timer

#timer class is subject.
#wunderground_pull is observer
#cities that we want to pull on New York, Los Angeles, Ardmore, Aurora, Honolulu, Boulder
#
#

#.keys() vital for parsing through json

class Wunderground_pull(Api_Pull):		
	
    #queries the API and returns JSON
    def query_API(self):
	state = self.state
	city = self.city
	queryString = 'http://api.wunderground.com/api/488fa44902ef7581/forecast10day/q/'+state+'/'+city+'.json'
        print("ohno")
	f=urllib2.urlopen(queryString)
	return f
    
    def getJSONData(self):
	    f = self.query_API()
	    state = self.state
	    city = self.city
	    #f = urllib2.urlopen('http://api.wunderground.com/api/f3cdf122d8571d47/forecast10day/q/CO/Boulder.json')
	    json_string = f.read()
	    parsed_json = json.loads(json_string)
	    highList= []
	    lowList = []
	    name = city+state
	    datePulled = (str(parsed_json['forecast']['simpleforecast']['forecastday'][0]['date']['month'])+
			  str(parsed_json['forecast']['simpleforecast']['forecastday'][0]['date']['day'])+
			  str(parsed_json['forecast']['simpleforecast']['forecastday'][0]['date']['year']))
	    
	   # print datePulled
	    for i in range(0, 10):
		highList.append(parsed_json['forecast']['simpleforecast']['forecastday'][i]['high']['fahrenheit'])
		lowList.append(parsed_json['forecast']['simpleforecast']['forecastday'][i]['low']['fahrenheit'])
	    


	    #whether to append to the file or write to the file ensures there is only one set of CSVs per city
	    #singleton essentially
	    
	    
	    if(not(os.path.isfile(name+"high.csv"))):
		    print("Creating new csv files")
		    with open(name+"high.csv", 'w') as csvfile:
				fieldnames = ['1', '2','3','4','5','6','7','8','9','10','date']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writeheader()
				writer.writerow({'1': highList[0],'2': highList[1], '3': highList[2], '4': highList[3],
				 '5': highList[4], '6': highList[5], '7': highList[6],'8': highList[7],'9': highList[8],'10': highList[9],'date':datePulled})

		    with open(name+"low.csv", 'w') as csvfile:
			    fieldnames = ['1', '2','3','4','5','6','7','8','9','10','date']
			    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)	
			    writer.writeheader()
			    writer.writerow({'1': lowList[0],'2': lowList[1], '3': lowList[2], '4': lowList[3],
			 '5': lowList[4], '6': lowList[5], '7': lowList[6],'8': lowList[7],'9': lowList[8],'10': lowList[9],'date':datePulled})
	    
	    else:
		    shouldRun = True
		    with open(name+"high.csv", 'rb') as csvfile:
			fieldnames = ['1', '2','3','4','5','6','7','8','9','10','date']
			reader = csv.DictReader(csvfile, fieldnames=fieldnames)
			for row in reader:
			    if(row['date']== datePulled):
				print("this date has already been read in")
				shouldRun = False
			    #print ', '.join(row)
		    
		    
		    
		    if(shouldRun):
			print("Appending to an existing CSV file")
			with open(name+"high.csv", 'a') as csvfile:
				fieldnames = ['1', '2','3','4','5','6','7','8','9','10','date']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writerow({'1': highList[0],'2': highList[1], '3': highList[2], '4': highList[3],
			     '5': highList[4], '6': highList[5], '7': highList[6],'8': highList[7],'9': highList[8],'10': highList[9],'date':datePulled})
	
			with open(name+"low.csv", 'a') as csvfile:
				fieldnames = ['1', '2','3','4','5','6','7','8','9','10','date']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)	
				writer.writerow({'1': lowList[0],'2': lowList[1], '3': lowList[2], '4': lowList[3],
			     '5': lowList[4], '6': lowList[5], '7': lowList[6],'8': lowList[7],'9': lowList[8],'10': lowList[9],'date':datePulled})
		    else:
			print("you tried to run the query on this city twice in one day")
#test Case


#queries all the cities in our list of cities
listofCities = (("New_York",'NY'),("Los_Angeles","CA"),("Boulder","CO"))
for x in range(0,(len(listofCities))):
    x= Wunderground_pull('Wunderground',listofCities[x][0],listofCities[x][1])
    x.getJSONData()


#x= Wunderground_pull('Wunderground','Honolulu','HI')
#x.getJSONData()
